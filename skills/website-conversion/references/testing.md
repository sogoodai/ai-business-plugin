# Testing on small traffic: sample sizes, what to do instead, how to report a win

Most small business sites cannot run a valid A/B test on a copy tweak. This file decides when a test is possible, what to run when it is not, and how to label a result so nobody mistakes a lucky week for a win. Sources in [sources.md](sources.md).

## Step 1: can this page support a test at all?

Visitors needed **per variant**, two-sided alpha 0.05, 80% power, standard two-proportion formula (computed November 2026; matches the research pass and Optimizely's December 2025 method note):

| Baseline conversion | +10% relative | +20% relative | +30% relative | +50% relative | +100% (doubling) |
|---|---|---|---|---|---|
| 1% | 163,000 | 42,700 | 19,800 | 7,750 | 2,320 |
| 2% | 80,700 | 21,100 | 9,800 | 3,830 | 1,140 |
| 3% | 53,200 | 13,900 | 6,460 | 2,520 | 750 |
| 5% | 31,200 | 8,160 | 3,780 | 1,470 | 435 |
| 10% | 14,800 | 3,840 | 1,770 | 690 | 200 |
| 20% | 6,510 | 1,680 | 770 | 290 | 82 |

Replo's 2026 ecommerce report gives the same order of magnitude: about 14,000 visitors per variant for a 20% lift at a 3% baseline.

**Decision rule.** Take the page's eligible weekly visitors (one device class if the change is device-specific). If two variants cannot reach the required sample within 4 weeks of stable traffic (no sale, no launch, no seasonal spike), do not run a split test of that change. Make a bigger change or use a method from Step 3.

**Quick read for a typical small business:** a lead page converting at 5% with 1,000 visitors a month needs about 8 months to detect a 20% lift. Only changes that could plausibly move conversion 50% or more (new offer, instant booking, visible price, form cut from 11 to 4 fields) are testable at that volume, and only on the page's primary metric.

## Step 2: choose the metric before you start

- **Primary metric close enough to the change to have power, far enough down to matter.** For a form change: submits as the sensitive metric, qualified leads and booked appointments as guardrails. For a PDP change: add to cart as sensitive, purchase and revenue per session as guardrails (research synthesis 2026).
- **Lead businesses:** report `lead`, `qualified_lead`, `booked`, `held`, `won`. A form test that adds submits and loses held appointments is a loss. Optimizely's January 2026 B2B test that cut a form from 9 to 3 fields (+42% leads) carried an explicit lead-quality warning from Optimizely itself.
- **Stores:** revenue per session beats conversion rate whenever the change can move AOV (discounts, free-shipping thresholds, bundles, upsells).
- **Write the stop rule in advance:** sample size, minimum full weeks (at least one, ideally two full business cycles so weekday mix is balanced), primary metric, guardrails.

## Step 3: what to do instead of a split test

Ranked by value per hour for sites under about 10,000 monthly visitors.

1. **Ship "no-regret" fixes without testing.** Mechanism-backed defects: broken buttons, hidden fees, forced account creation, lazy-loaded hero image, phone field required for no reason, no price signal, mobile CTA below the fold, form errors that clear inputs. Baymard's usability corpus and Google's CWV mechanics are the evidence. Testing a broken checkout against a working one wastes weeks.
2. **Five real-device journeys.** iPhone Safari, Android Chrome, desktop, plus the in-app browsers your traffic actually uses (Instagram, Facebook, TikTok). Complete the full money path to confirmation. Log every hesitation, error and covered CTA. This finds most of the money on a small site.
3. **Silent user test.** Ask 3 to 5 people who match the buyer (not friends in the trade) to complete the purchase or booking while you watch and say nothing. Note every pause. Operators on r/shopify recommend this as the highest-yield test for small stores.
4. **Five-second test.** Show the above-the-fold screen for 5 seconds, then ask: what is offered, for whom, what would you click? If 2 of 5 cannot answer, rewrite the hero before anything else.
5. **Session recordings and funnel steps.** Microsoft Clarity (free) or Hotjar. Watch 20 recordings of non-converting sessions from the main paid or organic landing page. Look for rage clicks, dead clicks, form field re-entry, scroll to the footer looking for price or contact.
6. **Ask the visitors.** One-question exit or post-purchase survey: "What almost stopped you from buying today?" or "What nearly stopped you from booking?" On the lead side, ask "How did you hear about us, and what made you get in touch?" on the thank-you page.
7. **Interrupted time series with a comparison.** Change one page; keep a similar page or traffic source unchanged as a comparison. Compare 4 weeks before and after on both. Label the result "observational before and after", never "test winner".
8. **Holdout for big systems.** For chat, popups and personalization apps, switch the tool off for a random 10 to 20% of sessions (most tools support it) or alternate weeks on and off. This is the only honest way to measure incremental effect on a small site.

## Step 4: running a real test

- **Never stop a fixed-horizon test when it first crosses p < 0.05.** Repeated peeking inflates false positives; if you need to look early, use a tool with sequential testing that adjusts for interim looks (Statsig docs, 2026).
- **One big hypothesis per test, tested as a whole page:** "specific outcome + visible proof + shorter qualification path" vs the current page. Accept that you will not know which element caused the lift (Optimizely 2026's +42% variant changed hero, image, CTA and form at once).
- **Split by device in analysis,** but only if each segment was powered.
- **Re-check after rollout.** A winner that fails to hold for 4 weeks after full rollout was noise or novelty.
- **Tools:** Shopify stores can use theme-level testing apps; WordPress sites can use server-side split URL tests; Google Optimize no longer exists (sunset September 2023), so any guide that tells the owner to "use Google Optimize" is outdated.

## Step 5: report with cause confidence

Every claimed win in a report carries one of these labels (research pass 2026):

| Label | Means |
|---|---|
| Randomized test | Split traffic, pre-registered stop rule, powered sample |
| Controlled comparison | Holdout or comparison page over the same period |
| Before and after | Same page, different periods, no comparison group |
| Correlation | Two numbers moved together; nothing more |

And always: affected traffic, primary metric change, guardrail change, money impact per month.

## What operators report about testing

- 30+ completely different landing pages over 4 months beat the product page "9 times out of 10" for paid traffic (r/shopify, 127 upvotes; no test data published). Treat as a hypothesis worth one big test, not a rule.
- A popup rebuilt 50+ times over 7 months moved signup from 2.8% to about 7% (cited in sibling `ecommerce-brand`). Iteration on a high-traffic element works; on a low-traffic page it does not.
- "Revenue per visitor with vs without" figures published by app users (10.32% vs 2.43% conversion for a recommendations app, r/shopify 160 upvotes) compare self-selected visitors. Ask for a holdout before believing them.

## Tricks most owners miss

- **Test the offer, not the button.** At small-business volume, only offer, price display, booking path, form length and proof changes clear the sample-size bar.
- **Power the test on the sensitive metric, then veto on the economic one.** A form test powered on submits can still be rejected on held appointments.
- **Benchmarks diagnose, they do not forecast.** Use them to find the abnormal stage, never as the expected lift.
- **Chat and popup "conversion of engagers" is self-selection.** Body Glove Hawaii's chatbot users converted at 6.34% vs 1.9% sitewide (TOMIS, 2025, no control). That gap says who chats, not what chat adds.
