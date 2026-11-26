---
name: website-conversion
description: Turn more small-business website visitors into leads, bookings and sales. Audits landing, service, product, pricing, booking and checkout pages with a browser; fixes headlines, CTAs, proof, price display, forms, calls, chat, popups, speed, mobile, checkout and accessibility; plans low-traffic tests. Use for "why isn't my site converting", page reviews, landing page or checkout fixes, CRO plans, A/B tests, ADA or EAA checks, for service, local, ecommerce, SaaS or creator sites.
---

# Website conversion: more leads, bookings and sales from the same traffic

For one failed or leaking purchase or booking path, use `purchase-booking-diagnosis` first. It separates reproduced defects, comparable funnel symptoms and missing evidence. Use this guide for broader page and conversion improvements after the specific journey is understood.

Built from 270 website-conversion tactics (r/shopify, r/Wordpress, r/web_design, r/webdev) plus about 1,260 conversion tactics from 20 other segment collections (r/sweatystartup, r/PPC, r/FacebookAds, r/ecommerce, r/SaaS, r/juststart and others), 2025 to 2026 research (Baymard, Littledata, Unbounce, Contentsquare, web.dev case studies, Optimizely, WebAIM, UsableNet, platform and legal texts) and the best public CRO skills (coreyhaines31 under MIT). "Operators report" marks a practitioner anecdote; everything else carries its source and year. Sources: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

## How small sites actually gain conversions

- **The defect beats the tweak.** One hidden fee, a lazy-loaded hero, a broken mobile button, a form that clears on error or an unanswered phone can erase a whole ad budget. Find and fix those before any test.
- **Most small sites cannot A/B test copy.** A 20% lift at a 3% baseline needs about 13,900 visitors per variant. Ship mechanism-backed fixes, test only big changes, label every win by cause confidence.
- **Clarity and friction move numbers; aesthetics rarely do.** Optimizely's January 2026 tests: clearer demo page +18.9% leads; hero, CTA and form simplified (9 to 3 fields) +42%; preview of the gated asset +47%.
- **Mobile owns traffic, desktop still converts better.** Professional services: 81% of visits mobile, 8.3% vs 11.6% conversion (Unbounce 2024). Treat mobile as its own funnel.
- **The follow-up is part of the page.** A form that sits unanswered for an hour converts like a broken form. Instant booking after qualification took one B2B firm from about 50% to 80%+ form-to-meeting (Chili Piper 2026, vendor).
- **Returning visitors are worth almost twice new ones** (2.9% vs 1.7%, Contentsquare 2026), and new-visitor conversion is falling faster (-8% vs -4% YoY). Preserve carts, quotes and context.
- **Judge on money per visitor**, never on raw conversion rate: `value per visitor = (conversions / visitors) x qualified or kept rate x value`.

## First session: ask, then compute

Ask the owner:

1. What counts as a conversion (purchase, booked appointment, held appointment, qualified lead) and what one is worth.
2. Monthly sessions by source and device; which pages get paid, organic and email traffic.
3. Platform: site builder, booking tool, checkout and payment processor, CRM or spreadsheet; access you can have.
4. Who answers calls, forms and chats, how fast, and after hours.
5. One real ad and one real search result that bring visitors in.
6. What they will not change (show prices, deposits, remove navigation, add chat) and who approves live changes.
7. Country of customers and business size (drives accessibility and pricing law).

Then compute ([references/plan-90-days.md](references/plan-90-days.md)):

```
step conversion = next step / previous step   (by device and source)
value per visitor = revenue or won value / sessions
lead-to-held = held appointments / form submits
answer rate = answered calls / inbound calls
checkout completion = purchases / checkout starts
money leak = sessions at step x (benchmark rate - your rate) x value per conversion
test feasibility = weekly eligible visitors x 4 weeks >= 2 x required sample per variant
```

Report the three biggest leaks in money, not percentages.

## Benchmarks to check first

Compare only the same conversion definition. Full tables: [references/benchmarks.md](references/benchmarks.md).

| Metric | Median | Better | Source |
|---|---|---|---|
| Landing page, all industries | 6.6% | | Unbounce, 2024 data |
| Professional services landing page | 6.1% | 14.1% top quartile | Unbounce, 2024 |
| SaaS landing page | 3.8% | 11.6% top quartile | Unbounce, 2024 |
| Ecommerce landing page | 4.2% | 11.4% top quartile | Unbounce, 2024 |
| Shopify session to purchase | 1.3% | 2.8% top 20%, 3.6% top 10% | Littledata, Nov 2026 |
| Shopify add to cart | 6.9% | 13% top 20% | Littledata, Nov 2026 |
| Shopify checkout completion | 47% | 64% top 20%, 73% top 10% | Littledata, Nov 2026 |
| Shopify revenue per session | $1.93 | $4.12 top 20% | Littledata, Nov 2026 |
| Cart abandonment | 70.22% | no valid target | Baymard, Oct 2026 |
| Warm email to landing page | 13.9% services, 28.6% ecommerce | | Unbounce, 2024 |
| AI-referral conversion | 1.3% (+55% YoY) | | Contentsquare 2026 |

Unbounce data is the largest public set but is 2024 traffic: possibly outdated. Never compare warm email traffic with cold social. Several popular CRO tables ("mobile converts 30 to 50% lower", "each second costs 7%", "popups convert 2 to 5%") have no source: do not quote them.

## Decision rules, in order

1. **Broken before better.** Run the browser audit ([references/page-audit.md](references/page-audit.md)): click every CTA, submit every form and confirm the owner receives it, place a test order or booking, open the real ad on a phone. $50k+ of ad spend once went to buttons pointing off-site (operators report).
2. **Message match.** The first screen repeats the promise of the ad or search result that sent the visitor. No match: fix the page or stop the ad.
3. **First screen answers five questions:** what, for whom, what result, why trust you, what happens on click. Five-second test with 5 people; if 2 fail, rewrite before anything else.
4. **Price before the ask.** Show a price, an honest range or what drives it. Stores: shipping cost or threshold and delivery date on the product page. Extra costs are 40% of actionable checkout abandonment (Baymard 2026).
5. **Path by value per visitor.** Urgent local: call first. Standard-scope service: online booking with instant price. Variable or high-ticket: short qualifying form then the calendar immediately. Stores: express wallets. Details: [references/lead-capture.md](references/lead-capture.md).
6. **Every field earns its place** (routing, quoting, eligibility, compliance, sales prep), but judge cuts on qualified and held leads, not submits.
7. **Proof next to the objection it answers,** verifiable and specific. Only 42% of consumers now trust reviews like a recommendation, down from 79% in 2020 (BrightLocal 2025).
8. **Speed: fix priority before bytes.** Field LCP 2.5 s or less, INP 200 ms, CLS 0.1. A lazy-loaded or script-revealed hero is the usual culprit (Nuvemshop 2026). Details: [references/speed-and-mobile.md](references/speed-and-mobile.md).
9. **Checkout in Baymard's order:** total cost, delivery date, guest checkout, express wallets, fields, phone optional, errors, encased card fields, returns line. Details: [references/checkout.md](references/checkout.md).
10. **Test only what the traffic can support,** one whole hypothesis at a time, no peeking. Otherwise ship and label "before and after". Details: [references/testing.md](references/testing.md).
11. **Chat and popups get a holdout,** judged on qualified or purchase value per visitor, not engagement.
12. **Accessibility on the money path is both conversion and legal risk.** Fix labels, keyboard, contrast and third-party widgets; never sell an overlay as compliance. Details: [references/accessibility-and-legal.md](references/accessibility-and-legal.md).

## Fixes that carry evidence

- **Instant scheduling after the form:** form-to-booking about 50% to 80%+, meetings +71%, time to meeting -63% (NetSPI, Chili Piper 2026, vendor).
- **Quiz instead of a long form:** insurance CPL €19 to €4 with a progress-bar quiz, "see your options in 60 seconds" (operators report); B2B contact form to a 5-question recommendation quiz, 2.5% to 9.3% (operators report).
- **Outcome headline instead of technology:** "Publish on 13 platforms from one chat." 40 signups in 2 weeks; a tech rewrite got 0 in a week (operators report); roofing tool 0.3% to 1.4% after dropping AI copy.
- **CTA repeats the headline keyword:** 58 to 59% click-through vs 42 to 45% for an unrelated message (Kutzner et al. 2024, cleaning site).
- **Speed with a control:** Rakuten 24 revenue per visitor +53.37%, conversion +33.13% (A/B, web.dev); Ray-Ban prerendering doubled mobile conversion (A/B, January 2025).
- **Encased card fields and 1 to 2 icons inside them** raise perceived payment security (Baymard); 19% of actionable abandoners distrust card entry.
- **No exits on paid pages:** removing social and WhatsApp links took a page from 0 to 5 sales a month to about 150 a week (operators report).
- **Speed to lead:** replying within about 5 minutes won about 70% of jobs for one pressure washer; close rate 40% to 75% (operators report; 9 threads agree).
- **AI chat, controlled:** MQL to SQL +10.3% vs control (Mindbody, January 2026). Uncontrolled "chatters convert 3x" claims are self-selection.
- **Show the locked value:** a scanner showing the count of critical issues with details locked tripled conversion (operators report).

## Tricks most owners miss

- **Audit from the ad, inside the app.** Open the real Instagram or Facebook ad on a phone and buy or book inside the in-app browser. Wallets, logins and schedulers fail there first.
- **Delivery date plus cutoff countdown** ("Order in the next 3 h 12 min, arrives Thu") is honest urgency; 48% of large sites show speed instead of date and 83% skip the countdown (Baymard 2026).
- **Mark required and optional fields.** When only optional ones were marked, 32% of test users missed a required field (Baymard 2026).
- **Phone field with a reason** ("So the technician can call when 30 minutes away"); 68% of shoppers resist giving a number.
- **Collapse the coupon field** behind "Have a code?" so buyers do not leave to hunt for codes.
- **Prerender the next likely page** (Speculation Rules) from listing to product or service to booking.
- **Four questions after the email field, no name or phone**, and read the "when are you buying?" split: 50% today, 47% in weeks for one store (operators report).
- **Cap the calendar at 7 days out** and propose a specific time in live conversations.
- **Submit the form and wait for the email.** Thank-you pages that count conversions while nothing arrives are common.
- **Keep dated price records.** They defend compare-at prices in lawsuits and satisfy the EU 30-day rule.
- **Prices as HTML text, not images or PDFs,** so phones, screen readers and AI answers can read them; one plain price paragraph won an AI Overview citation over complex tables (operators report).

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| Fewer fields | Cut everything | 9 to 3 fields +42% leads, with a quality warning (Optimizely 2026) | Cut fields with no job; guard on qualified and held |
| Multi-step forms | Always better | A plain two-step split raised total abandonment in one test; quizzes with a payoff won | Multi-step only when each step is a meaningful question with a result |
| Popups | Instant 10% popup works / popups hurt AOV | No controlled purchase data | Device-specific, holdout, judge on purchases and AOV per visitor |
| Countdown timers | Urgency sells | Fake timers read as scams; EU law blacklists false limited-time claims | Real cutoffs and real stock only |
| Speed scores | Chase 90+ | Field CWV and conversion matter; score gigs fake results | Fix real slowness (4 s+, lazy hero); ignore lab score polishing |
| Landing page vs product page | Dedicated pages win "9 of 10" | No published test data | One big test if traffic allows |
| Guarantees | Strong refunds drive sales | Uncapped results guarantees bankrupted an agency; Amazon delists "money back" images | Specific, capped, honored, platform-compliant |
| Show prices | Hide to force calls | Hidden costs top abandonment; published prices bring warmer leads | Price or honest range on the page |

## Never

- Never invent ratings, review counts, customer numbers, credentials, response times, guarantees, scarcity or quotes.
- Never ship fake timers, fake stock counts, fabricated "someone just bought" notices or pre-ticked consent, recurring or upsell boxes.
- Never gate or incentivize reviews, or hide negative reviews while implying all are shown.
- Never recommend an accessibility overlay as compliance.
- Never stop a test on the first significant reading, or report a win without its cause-confidence label.
- Never place real orders, bookings or charges on a live business without the owner's go-ahead; use test modes.
- Never change live prices, checkout, payment settings or legal pages without the owner's approval, and test the full path after any change.

## References

- [page-audit.md](references/page-audit.md): browser-runnable pass/fail checklist with console scripts (CTA above the fold, lazy hero, labels, keyboards, tap targets, LCP and CLS), priorities and report format.
- [copy-and-layout.md](references/copy-and-layout.md): first screen, verbatim headline and CTA patterns, microcopy, proof by objection, price display, page length by awareness.
- [lead-capture.md](references/lead-capture.md): forms, quizzes, calls, booking widgets, speed to lead, AI chat, popups and email capture.
- [speed-and-mobile.md](references/speed-and-mobile.md): CWV targets, case studies, LCP procedure, WordPress and Shopify tricks, mobile checks.
- [checkout.md](references/checkout.md): Baymard data, fix order, cart page, legal traps, monitoring, worked example.
- [testing.md](references/testing.md): sample-size table, what to do instead of A/B tests, metric choice, reporting labels.
- [accessibility-and-legal.md](references/accessibility-and-legal.md): ADA, EAA, UK, Canada, Australia, lawsuits, overlay risk, money-path accessibility pass, review, pricing, urgency and consent rules.
- [templates-by-business.md](references/templates-by-business.md): section-by-section pages for service, local storefront, ecommerce, SaaS, creator and B2B.
- [benchmarks.md](references/benchmarks.md): metric, typical, top quartile, source, year; operator numbers; numbers to ignore; gaps.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead (data and practitioners).
- [plan-90-days.md](references/plan-90-days.md): owner questions, instrumentation, fixes, one big test, scorecard, exit checks.
- Sibling skills: `paid-ads` for ad accounts, speed-to-lead systems and call handling; `ecommerce-brand` for product pages, Shopify setup, fraud and AOV offers; `local-seo` for Google profile, reviews and local pages; `offers-pricing` for pricing psychology and tiers; `seo-content` for organic traffic and AI answers; `email-sms-loyalty` for flows after capture; segment skills (`home-services`, `beauty-business`, `restaurant`, `saas-apps`, `creator` and others) for niche offers and policies.
