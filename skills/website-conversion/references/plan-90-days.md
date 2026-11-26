# 90-day conversion plan

For a new or stalled small business site. Order: measure the money funnel, fix catastrophic leaks, remove friction without pretending every change needs a test, then run one big experiment at a time. Sources in [sources.md](sources.md).

## Before day 1: ask the owner

1. What counts as a win: purchase, booked appointment, held appointment, qualified lead, signed job? What is one worth (average order or job value, gross margin)?
2. Where does traffic come from today, roughly how much a month, and which pages get it?
3. Who answers calls, forms and chats, and how fast? After hours?
4. Platforms: site builder, booking tool, payment processor, CRM or spreadsheet. Can you get admin or read access?
5. Any changes you will not accept (prices shown, deposits, removing navigation, chat)?
6. Any legal or regulatory constraints (licensed profession, health, finance, alcohol, EU customers)?
7. Who approves copy, prices and live changes?

## Days 1 to 14: the money funnel and catastrophic leaks

**Instrument the smallest set of events that ties traffic to money:**
- Service and lead businesses: `landing`, `primary_cta`, `form_start`, `form_submit`, `qualified`, `calendar_view`, `booked`, `held`, `won`, `revenue`, plus `call_click` and answered calls.
- Stores: `product_view`, `add_to_cart`, `checkout_start`, `purchase`, `revenue`, `refund`.
- Segment everything by source, device, new vs returning and landing page. UTM tags on every owned link.

**Compute:**
```
conversion by step = next step / previous step, per device and source
value per visitor = revenue (or won value) / sessions
lead-to-held = held appointments / form submits
answer rate = answered calls / inbound calls
checkout completion = purchases / checkout starts
money leak per step = sessions at step x (benchmark rate - your rate) x value per conversion
```

Compare stores with Littledata November 2026 (1.3% median purchase, 47% checkout completion) and their category; lead pages with Unbounce 2024 by industry, source and device. Report the three biggest gaps in money, not percentages.

**Find the catastrophes (all in [page-audit.md](page-audit.md)):**
- Five real-device journeys (iPhone Safari, Android Chrome, desktop, Instagram and Facebook in-app browsers) from the real ad or search result to confirmation.
- Submit every form; confirm the owner receives it and the conversion fires once.
- One real test order or test booking.
- PageSpeed field data on the top 3 money templates; LCP element not lazy-loaded.
- Click every CTA.

**Exit check:** every P1 found is listed with its money estimate; the funnel is visible by device and source.

## Days 15 to 30: no-regret fixes

Ship without testing; compare 4 weeks before and after and label the result "before and after".

**Service and lead businesses:**
- Rewrite the first screen: audience line, outcome headline, subhead with scope, CTA that names the next step, proof line under it ([copy-and-layout.md](copy-and-layout.md)).
- Price, range or price drivers on the page.
- Form field audit; phone optional or explained; success page with the next step and time.
- Calendar immediately after qualification for standard job types; card capture where no-shows hurt.
- Tap-to-call in the header on mobile; missed-call text-back; voicemail pointing to online booking.
- Speed-to-lead target set and tracked (first reply under 5 minutes in business hours).

**Stores:**
- Shipping cost or threshold and delivery date on the product page and cart.
- Guest checkout prominent; express wallets above the form; returns line by add to cart.
- Card fields encased; coupon field collapsed; phone optional.
- Real stock and real cutoffs; remove fake timers.
- Weekly test order on the calendar.

**Both:**
- Fix the LCP image (no lazy load, high priority), defer chat, review and popup scripts.
- Remove navigation and side exits from paid landing pages.
- Accessibility P1s: form labels, keyboard path, CTA contrast, booking and payment widget keyboard test.
- Review request after a neutral completion event, sent to everyone: "Thanks for choosing [Business]. If you have a moment, would you share an honest review of your experience? [link]. We read every review and use the feedback to improve." Depth in `local-seo`.

**Exit check:** P1s closed or explicitly accepted by the owner; before-and-after window started.

## Days 31 to 60: one big experiment, if traffic allows

1. Compute the sample size ([testing.md](testing.md)). If the page cannot reach it in 4 weeks, skip to the qualitative methods and ship the strongest fix as a before and after.
2. If it can, test a whole hypothesis: "specific outcome + visible proof + shorter qualification path" vs the current page, or "instant booking" vs "we'll call you", or "dedicated landing page" vs product page for cold traffic.
3. Primary metric close to the change; guardrails on qualified, held or revenue per visitor.
4. For lead businesses with many repeated questions, test AI chat with a holdout; success = more qualified or held per visitor, not chats.
5. Popups: test timing and placement against purchases and AOV per visitor; dedupe repeat signups.
6. Start monitoring AI-referral traffic separately (Search Console's generative AI performance report, June 2026; referrers like chatgpt.com, perplexity.ai) and make prices, services, areas and policies readable as text. Depth in `seo-content` and `local-seo`.

**Exit check:** one test concluded with a written result and cause-confidence label, or a documented reason why no test was possible.

## Days 61 to 90: compound and find the second bottleneck

- Recompute the full funnel. If page conversion rose but qualified or held fell, add qualification later in the journey or revert. If add to cart rose but purchases did not, move the backlog to checkout. If mobile engagement rose but mobile conversion did not, inspect errors, payment and scheduler handoffs and in-app browsers.
- Roll the winning patterns to the next pages by traffic.
- Rank the backlog:

```
expected value = affected traffic x funnel loss x plausible recoverable fraction x value per conversion x confidence / implementation cost
```

The recoverable fraction never comes straight from a benchmark gap: benchmarks show where the abnormal stage is, not how much of it you can close.

- **Weekly scorecard from now on:** sessions, spend, cost per qualified lead or order, landing conversion, qualified rate, booking rate, held rate, add to cart, checkout start, checkout completion, purchase conversion, AOV, revenue per session, new vs returning conversion, mobile vs desktop conversion, LCP/INP/CLS field status, refunds and cancellations, review count and rating, open accessibility defects, answer rate and median first-reply time.

**Exit check at day 90:** value per visitor up vs day 1 on the same traffic mix, every claimed win labeled by cause confidence, next quarter's top 3 items ranked by expected value.
