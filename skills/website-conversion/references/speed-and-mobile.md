# Page speed, Core Web Vitals and mobile

Speed is a conversion lever and a cost lever before it is a ranking lever. Sources in [sources.md](sources.md).

## The targets

Google's "good" thresholds at the 75th percentile of real users (Google Search Central, current 2026):

| Metric | Good | Poor | What it measures |
|---|---|---|---|
| LCP (Largest Contentful Paint) | 2.5 s or less | over 4.0 s | When the main hero image or headline appears |
| INP (Interaction to Next Paint) | 200 ms or less | over 500 ms | How fast the page reacts to taps and clicks; replaced FID on 12 March 2024 |
| CLS (Cumulative Layout Shift) | 0.1 or less | over 0.25 | How much the layout jumps (the "I tapped the wrong button" problem) |

Google says good CWV do **not** guarantee rankings and there is no single page-experience switch. Optimize them for conversion and paid-traffic cost, not for a ranking promise.

## Evidence that speed moves money

| Case | Change | Result | Evidence grade |
|---|---|---|---|
| Rakuten 24 (web.dev) | Landing page optimized for CWV vs identical original, 50/50 split, one month | Revenue per visitor +53.37%, conversion +33.13%, AOV +15.20%, exit rate -35.12% | A/B test, platform-published |
| Ray-Ban (web.dev, January 2025) | Speculation Rules prerendering of product pages from listing tiles | Mobile LCP 4.69 s to 2.66 s, conversion +101.47%, exit -13.25%; desktop LCP 3.03 s to 1.74 s, conversion +156.16% | A/B test on supporting browsers |
| Nuvemshop (web.dev, June 2026) | Stopped lazy-loading top-of-viewport images, fixed resource priority across 180,000+ stores | LCP-good share 57% to 96%, CWV pass 48% to 72%, mobile Google-organic conversion +8.9%, cart engagement +8.4% | Same-cohort before and after, not causal |
| Vodafone Italy (web.dev) | LCP -31% | +8% sales | Case, design not stated |
| Redbus (web.dev) | CLS 1.65 to 0 | Mobile conversion +80 to 100% | Case, design not stated |
| Lazada (web.dev) | LCP 3x faster | Mobile conversion +16.9% | Case, design not stated |
| Agrofy (web.dev) | LCP 70% better | Load abandonment -76% | Case, design not stated |
| Yottaa 2025 index (via Shopify) | 1 s faster mobile load | About +3% conversion; pages over 4 s converted 22% lower | Vendor observational |
| WordPress ads landing page (r/Wordpress, 119 upvotes) | Elementor/Divi rebuilt in core blocks, 2 MB of unused CSS/JS removed | 4.2 s to 0.8 s on 4G; owner reports better Quality Score and lower CPC, no figures | Operator report |

Large-company cases over-represent wins. The mechanism (users leave before the page is usable) is solid; the size of the effect on a small site is unknown until measured.

## The procedure (in this order)

1. **Field data first.** PageSpeed Insights "Discover what your real users are experiencing" block, or Search Console Core Web Vitals report. Lab scores (Lighthouse) are for debugging, not for judging.
2. **Pick the templates that carry money:** paid landing page, top organic landing page, product page, booking or checkout page. Test them on mobile.
3. **Find the LCP element** (PageSpeed shows it). Then check, in this order:
   - Is it lazy-loaded (`loading="lazy"`)? Remove lazy loading from anything visible in the first screen. This was Nuvemshop's main finding, not image weight.
   - Is it discovered late (CSS background image, injected by JavaScript, slider script)? Put it in the HTML as an `<img>` and add `fetchpriority="high"`.
   - Is it animated into view (fade-in, slider, Ken Burns)? A hero that fades in after a script runs is a slow LCP even when the file is small.
   - Is it fighting third-party scripts (chat widgets, review widgets, popups, heatmaps, tag managers) for bandwidth? Delay non-essential scripts until after interaction or load.
4. **Then weight:** WebP or AVIF, correct dimensions, width and height attributes set (prevents CLS).
5. **INP:** long JavaScript tasks from page builders, sliders, chat and review apps. Remove before you optimize.
6. **Measure conversion alongside CWV** on the same templates and traffic source, before and after.

## Platform-specific tricks

**WordPress (operators, r/Wordpress):**
- Audit which plugin assets load on each page; one site went from 2 s to 8 s after one badly coded all-in-one plugin; page builders inject about 400 KB of unused CSS per page (177 upvotes). Asset CleanUp or Perfmatters unloads scripts per page.
- One client had 53 plugins; half were unused and 10 more could be replaced by small snippets (266 upvotes).
- Replacing a Slider Revolution hero with a static image, cutting plugins 50% and adding caching gave a solo attorney site a desktop Speed Index of 1.7 s (177 upvotes).
- Server level: OPcache memory 64M to 256M cut average TTFB 480 ms to 290 ms; InnoDB buffer pool sized to about 80% of active data cut query time 18 ms to 7 ms; a remote Redis or database in another region can make things slower (136 upvotes).
- Rarely updated marketing pages moved to a static site ran about 20x faster in one company's test (264 upvotes).
- WooCommerce with Redis: test cart-fragment purging before launch; stale carts and ghost sessions showed only in production (288 upvotes).

**Shopify (operators, r/shopify):**
- Theme choice matters more than apps you add later: an audit of 100 popular themes found the fastest scoring 95+ and under 2.5 s, with Shopify's own themes holding 5 of the top 15 spots (73 upvotes, demo stores, not production).
- **Speed-gig scam:** $50 to $200 "PageSpeed 90+ in 24 hours" gigs detect test tools and block scripts only for them; some also inject hidden links or spam collections (one store found "FIFA coins" collections) (157 upvotes). Check theme code after any outsourced speed work; judge only on field data and a real phone.
- Every app adds script weight. Remove uninstalled apps' leftover code from the theme.

**Any stack:**
- Bot and crawler traffic can be a cost problem on serverless hosting: Meta's crawler made 11.2 million requests to one listings site, taking a Vercel bill from $30 to $1,933.93 in a month; the owner blocked `meta-externalagent` in robots.txt (r/webdev, 3,232 upvotes). Check hosting bills and logs before blaming "growth".
- A preloader that hides the page for 13 seconds is a conversion killer even when the design is praised (r/web_design, 976 upvotes; measured 8 MB page, 17.8 s load on a slow mobile profile).

## Mobile: a separate funnel

- Mobile carries most traffic and converts lower. Unbounce professional services (2024 data): 81% of visits mobile, 8.3% mobile conversion vs 11.6% desktop. Contentsquare 2026 and Littledata November 2026 show mobile dominance across stores too. Never accept an aggregate conversion rate without a device split.
- Do not strip desktop detail because "everyone is on mobile": desktop still converts better and often carries the larger orders. Fix the mobile action path; keep the depth.

**Mobile checks (run on a real phone, from the ad or search result to confirmation):**

| Check | Pass |
|---|---|
| First screen | Says what, for whom and the next step before a large image fills the screen |
| Primary action | Visible on load; sticky call, book or add-to-cart bar when the main button scrolls away |
| Thumb reach | Primary actions in the lower half; a bottom-right menu was praised by most users of one app, but one missed it (r/webdev, 3,489 upvotes), so label it |
| Tap targets | 44 px or larger, 8 px apart |
| Keyboards | `type="email"`, `type="tel"`, `inputmode="numeric"`, `autocomplete` attributes set so autofill works |
| Overlays | Cookie banner, chat bubble and popup never cover the CTA or the price; nothing full screen before content (Google intrusive interstitials guidance) |
| Key facts | Price, delivery, returns, service area, availability readable without opening accordions |
| Handoffs | Scheduler, payment page and maps links open in the same context and work inside Instagram and Facebook in-app browsers |
| Click-to-call | `tel:` link with the number visible as text, tracked as an event |

**Tricks most owners miss**

- **Segment by browser + device + payment method.** A "mobile problem" is often one Safari payment bug, one consent layer, one sticky widget or one scheduler embed.
- **Check the in-app browser.** Paid social traffic lands inside Instagram, Facebook or TikTok browsers, where some payment wallets, logins and third-party cookies fail. Complete a purchase inside each one before spending.
- **The compressed hero can still be the slow LCP** if the browser finds it late. Fix priority before shaving bytes.
- **Prerender the next page** (Speculation Rules) for the most common next click, such as listing to product or service to booking. Ray-Ban's conversion doubled on mobile.
