# Page audit an agent can run with a browser

A pass/fail audit for one money page (landing page, service page, product page, booking or checkout path). Run it with a browser tool (Playwright, Chrome DevTools, the T3 or Claude preview browser) plus PageSpeed Insights. Every failure goes in the report with: check, evidence (screenshot or value), fix, priority. Sources in [sources.md](sources.md).

## Setup

1. Ask the owner for: the page URLs that receive paid, organic and email traffic; the conversion that counts (purchase, booked appointment, qualified lead); a test card or test booking slot; analytics access (GA4, Shopify, booking tool) if they will grant it.
2. Get one real ad and one real search result that lead to the page, so you audit the page against the promise.
3. Viewports: mobile 390 x 844 (iPhone 14-class) and desktop 1440 x 900. Run mobile first.
4. Throttle once to "Slow 4G" for the speed pass.
5. Never submit real orders or bookings on a live business without the owner's go-ahead; use test mode, a test product or a slot the owner will cancel.

## Automated checks (paste into the browser console or `evaluate`)

```js
(() => {
  const vh = innerHeight, r = {};
  const inView = el => { const b = el.getBoundingClientRect(); return b.top < vh && b.bottom > 0 && b.width > 0 && b.height > 0; };
  r.h1 = [...document.querySelectorAll('h1')].map(h => h.innerText.trim()).slice(0, 3);
  r.lang = document.documentElement.lang || 'MISSING';
  r.title = document.title;
  const clickables = [...document.querySelectorAll('a,button,input[type=submit]')];
  const ctas = clickables.filter(e => /book|buy|add to (cart|bag)|quote|call|schedule|get|start|check|order|reserve|contact/i.test(e.innerText || e.value || ''));
  r.ctaAboveFold = ctas.filter(inView).map(e => (e.innerText || e.value).trim().slice(0, 40));
  r.genericCtas = clickables.map(e => (e.innerText || e.value || '').trim()).filter(t => /^(submit|send|learn more|click here|get started)$/i.test(t));
  r.telLinks = [...document.querySelectorAll('a[href^="tel:"]')].map(a => a.getAttribute('href'));
  r.navLinks = document.querySelectorAll('nav a, header a').length;
  const imgs = [...document.images];
  r.imgsNoAlt = imgs.filter(i => !i.hasAttribute('alt')).length;
  r.lazyAboveFold = imgs.filter(i => i.loading === 'lazy' && inView(i)).map(i => i.currentSrc.slice(-60));
  r.imgsNoDims = imgs.filter(i => !i.getAttribute('width') || !i.getAttribute('height')).length;
  const inputs = [...document.querySelectorAll('input,select,textarea')].filter(i => !['hidden','submit','button'].includes(i.type));
  r.formFields = inputs.length;
  r.requiredFields = inputs.filter(i => i.required).length;
  r.unlabeled = inputs.filter(i => !(i.labels && i.labels.length) && !i.getAttribute('aria-label') && !i.getAttribute('aria-labelledby')).map(i => i.name || i.id || i.placeholder || i.type);
  r.wrongKeyboards = inputs.filter(i => (/mail/i.test(i.name + i.id) && i.type !== 'email') || (/phone|tel/i.test(i.name + i.id) && i.type !== 'tel')).map(i => i.name || i.id);
  r.noAutocomplete = inputs.filter(i => /name|mail|phone|tel|address|zip|postal|city/i.test(i.name + i.id) && !i.autocomplete).map(i => i.name || i.id);
  r.smallTapTargets = ctas.filter(e => { const b = e.getBoundingClientRect(); return b.height > 0 && b.height < 44; }).map(e => (e.innerText || '').trim().slice(0, 30)).slice(0, 10);
  r.emptyButtons = [...document.querySelectorAll('button,a')].filter(e => !e.innerText.trim() && !e.getAttribute('aria-label') && !e.querySelector('img[alt]:not([alt=""])')).length;
  r.thirdPartyScripts = [...new Set([...document.scripts].map(s => s.src).filter(s => s && !s.includes(location.hostname)).map(s => new URL(s).hostname))];
  const nav = performance.getEntriesByType('navigation')[0];
  r.transferKB = Math.round(performance.getEntriesByType('resource').reduce((a, e) => a + (e.transferSize || 0), nav ? nav.transferSize : 0) / 1024);
  r.requests = performance.getEntriesByType('resource').length;
  r.priceVisible = /[$£€]\s?\d/.test(document.body.innerText);
  r.mentionsShippingOrReturns = /shipping|delivery|returns?/i.test(document.body.innerText);
  return r;
})()
```

For LCP and CLS on the live page, run before interacting:

```js
new Promise(res => { let lcp, cls = 0;
  new PerformanceObserver(l => { const e = l.getEntries().at(-1); lcp = { ms: Math.round(e.startTime), el: e.element && (e.element.tagName + ' ' + (e.element.currentSrc || e.element.innerText || '').slice(0, 60)), lazy: e.element && e.element.loading }; }).observe({ type: 'largest-contentful-paint', buffered: true });
  new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) cls += e.value; }).observe({ type: 'layout-shift', buffered: true });
  setTimeout(() => res({ lcp, cls: +cls.toFixed(3) }), 5000); })
```

Lab values only. Confirm with field data (PageSpeed Insights top block or Search Console) before reporting a speed failure.

## The checklist

Priority: **P1** = losing money now, fix this week; **P2** = clear friction; **P3** = polish or test candidate.

### A. Promise and first screen (mobile)

| # | Check | Pass rule | Pri |
|---|---|---|---|
| A1 | Message match | The page headline or first line repeats the ad's or search result's main promise and offer | P1 |
| A2 | Five questions | Screenshot of the first screen shows what, for whom, result, one proof element, and what the CTA does | P1 |
| A3 | Primary CTA above the fold | At least one primary CTA in `ctaAboveFold` on 390 x 844 | P1 |
| A4 | CTA wording | No generic "Submit", "Learn more", "Click here", "Get started" as the main CTA; it names the outcome or next step | P2 |
| A5 | One primary action | One visually dominant CTA; secondary actions styled as secondary | P2 |
| A6 | Distractions on paid pages | Paid landing page has no main navigation, no social links, no blog links (navLinks near 0 to 3) | P2 |
| A7 | Reading level | Headline and first 100 words readable at about grade 7; no unexplained jargon or "AI-powered" without an outcome | P2 |
| A8 | Real imagery | Hero shows the real product, work, people or premises; not stock | P3 |
| A9 | Audience fit in examples | Images and examples include every main customer segment | P3 |

### B. Proof and trust

| # | Check | Pass rule | Pri |
|---|---|---|---|
| B1 | Proof by the CTA | A rating with count, a credential or a specific testimonial within one screen of the primary CTA | P1 |
| B2 | Verifiable proof | Reviews link to or embed a platform the visitor can check; numbers on the page match the platform | P2 |
| B3 | Specific testimonials | At least 2 testimonials with a name, context and a specific result | P2 |
| B4 | Business is real | Phone, address or service area, real email domain, legal name where customary; no template residue ("[yoursitename]", lorem ipsum), no dead legal links | P1 |
| B5 | Guarantee is specific | If a guarantee is shown: condition, remedy, how to claim | P2 |
| B6 | No fake urgency | Timers only for real deadlines, stock counts from real inventory, no fabricated "X just bought" popups | P1 |
| B7 | About page | Named people, real photos, history and credentials where trust in the person matters (home, health, money, bespoke) | P3 |

### C. Price and offer

| # | Check | Pass rule | Pri |
|---|---|---|---|
| C1 | Price signal | Price, honest range or "how price is calculated" visible before the form or cart | P1 |
| C2 | Total cost early (stores) | Shipping cost or threshold and delivery date on the product page and in the cart | P1 |
| C3 | Surcharges | Product- or country-specific fees shown beside the price, not first at payment | P1 |
| C4 | Reference prices | Strikethrough prices are real recent prices; EU stores show the 30-day prior lowest price | P2 |
| C5 | Subscription terms | Recurring amount, interval, trial end and cancellation shown beside the subscribe button | P1 |
| C6 | Price in the buyer's unit | What the price buys is unambiguous (per image, per room, per month, per person) | P2 |

### D. Form, call, chat, booking

| # | Check | Pass rule | Pri |
|---|---|---|---|
| D1 | Field count | Every field maps to routing, quoting, eligibility, compliance or sales prep; lead forms usually 3 to 5 fields | P2 |
| D2 | Phone field | Optional, or required with a reason shown | P2 |
| D3 | Labels | `unlabeled` is empty; placeholders are not the only label | P1 |
| D4 | Keyboards and autofill | `wrongKeyboards` and `noAutocomplete` empty | P2 |
| D5 | Errors | Submit with one bad field: error next to the field, says how to fix, other inputs kept | P1 |
| D6 | Success | Real submit (test) shows a next step; the owner actually receives it; the conversion event fires only on success | P1 |
| D7 | After the form | High-intent forms lead to a calendar or a stated response time ("We reply within 2 business hours") | P2 |
| D8 | Click to call | `telLinks` present on mobile for service businesses; number also visible as text | P1 for local services |
| D9 | Booking widget | Can a new customer book in under 2 minutes on mobile? Count taps; card capture explained; slots within the next 7 days visible | P2 |
| D10 | Chat | If present: does not cover CTA or price on mobile; answers a pricing and an availability question correctly; offers a human | P2 |
| D11 | Popup | Not full screen on mobile before content; easy close; not on checkout; not shown again after dismissal | P2 |

### E. Speed and stability

| # | Check | Pass rule | Pri |
|---|---|---|---|
| E1 | Field CWV | LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less at p75 on mobile (PageSpeed field data) | P1 if LCP over 4 s |
| E2 | Hero not lazy | `lazyAboveFold` empty; LCP element is not lazy-loaded, not a CSS background, not faded in by script | P1 |
| E3 | Image dimensions | `imgsNoDims` near 0 (prevents layout jumps) | P2 |
| E4 | Weight | Mobile transfer under about 2 MB for a landing page; no hero over 300 KB | P2 |
| E5 | Third parties | Each `thirdPartyScripts` host has a purpose; chat, review, popup and heatmap scripts deferred | P2 |
| E6 | Console | No JavaScript errors on load or on submit | P1 if they block the CTA |
| E7 | Preloader | No splash or preloader hiding content | P1 |

### F. Mobile and device paths

| # | Check | Pass rule | Pri |
|---|---|---|---|
| F1 | Tap targets | `smallTapTargets` empty (44 px) | P2 |
| F2 | Overlays | Cookie banner, chat bubble and popup never cover the CTA or price | P1 |
| F3 | Sticky action | When the main CTA scrolls away, a sticky call, book or add-to-cart bar appears | P2 |
| F4 | In-app browser | Full path completes inside Instagram and Facebook in-app browsers (open the real ad on a phone) | P1 for social traffic |
| F5 | Safari and Chrome | Full path completes on iPhone Safari and Android Chrome | P1 |
| F6 | Key facts visible | Price, delivery, returns, area, hours readable without opening accordions | P2 |

### G. Checkout (stores)

Run the fix list in [checkout.md](checkout.md). Pass rules: guest checkout prominent; express wallets above the form; 12 to 14 form elements; phone optional or explained; delivery date shown; returns line; card fields visually encased; coupon field collapsed; test order completes on mobile. Any failure on guest checkout, hidden costs or a broken payment method is P1.

### H. Accessibility on the money path

Keyboard-only pass from landing to confirmation: focus visible, every control reachable, dialogs closable with Esc, no trap in booking or payment iframes. `lang` set, `imgsNoAlt` near 0, `emptyButtons` 0, CTA text contrast 4.5:1 or better. Details and legal context in [accessibility-and-legal.md](accessibility-and-legal.md). Missing form labels or a keyboard trap in checkout or booking is P1.

### I. Measurement

| # | Check | Pass rule | Pri |
|---|---|---|---|
| I1 | Events | Primary conversion fires once per real success, with value; micro-events for CTA click, form start, calendar view | P1 |
| I2 | Downstream | Leads can be traced to qualified, booked, held, won (CRM, booking tool or a sheet) | P1 for lead businesses |
| I3 | Source tags | UTM on every owned link (GBP, email, bio, QR) | P2 |
| I4 | Device split | Conversion reportable by device and source | P2 |
| I5 | Bot filter | Server logs or analytics show humans, not crawler floods; link clicks vs landing page views gap under about 40% | P2 |

## Report format

1. **Verdict line:** the one thing costing the most money, with the number ("Mobile visitors cannot see a price or a booking button: 81% of your traffic").
2. **P1 list** (fix this week), each with evidence screenshot, fix and the metric to watch.
3. **P2 list** (next 30 days).
4. **Test candidates** (only if traffic supports a test, see [testing.md](testing.md)).
5. **Copy alternatives:** 2 to 3 headline and CTA options using [copy-and-layout.md](copy-and-layout.md), built from the business's real facts.
6. **What you could not check** (no analytics access, could not place a test order) stated plainly.

## Tricks most owners miss

- **Audit from the ad, not the URL.** Half the P1s (message mismatch, in-app browser failures, translated ads landing on English pages) only show when you start where the visitor starts.
- **Submit the form and wait for the email.** Thank-you pages that fire conversions while nothing arrives are common.
- **Lazy-loaded hero is the single most common speed bug** on modern themes and builders.
- **Count the taps to book on a phone.** Anything over about 6 taps to a confirmed slot is a P2 at least.
