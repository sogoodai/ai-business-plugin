---
name: paid-ads
description: Run, audit and scale paid ads for a small business spending $10 to $5,000 a day on Meta (Facebook, Instagram, click-to-WhatsApp and Messenger), Google (Search, Performance Max, AI Max, Demand Gen, YouTube, LSA), TikTok (Smart+, Spark, GMV Max), Pinterest, Reddit, Nextdoor or Microsoft. Use for account structure, budgets, bidding, creative tests, hooks, lead quality, tracking, CAPI, MER, kill or scale calls, policy bans and ad account audits.
---

# Paid ads: buy customers you can afford, prove it, then scale

Built from 539 practitioner threads, about 1,400 extracted tactics (r/FacebookAds, r/PPC, r/GoogleAds, r/DigitalMarketing, r/marketing, r/copywriting, r/socialmedia, r/Emailmarketing, plus ad tactics from r/dropship, r/shopify, r/FulfillmentByAmazon, r/TikTokshop and r/sweatystartup), 2025 to 2026 platform documentation and benchmark studies (Google, Meta, TikTok, Pinterest, Reddit, Nextdoor, WordStream/LocaliQ, Triple Whale, Motion, Unbounce), and the best public ads skills (coreyhaines31, AgriciDaniel, aaron-he-zhu). "Operators report" marks a practitioner claim; everything else carries its source and year. Full list: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

## How paid ads actually work in 2026

- **The algorithm does the targeting; you supply signal and creative.** Meta's Andromeda retrieval now scores over one billion eligible ads per second, about 100x its 2024 system, and Meta credits it with +2.4% Facebook conversions since 2025 ([Meta Engineering, Oct 2026](https://engineering.fb.com/2026/10/28/ml-applications/meta-andromeda-next-gen-ads-retrieval-gpu-co-design/)). Interest stacks and 15 small ad sets lose to broad delivery fed by many distinct concepts.
- **Most creatives fail, so volume of distinct ideas wins.** Only 5 to 8% of Meta creatives become winners (10x account-median spend) across 578,750 creatives and $1.29B of spend ([Motion 2026](https://go.motionapp.com/benchmarks-paid), reported by Motion, not independently checked). A 20% hit rate on 5 ads gives 1 winner; 10% on 50 gives 5.
- **The platform optimizes whatever event you feed it.** Feed it raw form fills and it buys form fillers. A $20 lead closing at 2% costs $1,000 per customer; a $60 lead closing at 15% costs $400 (illustrative arithmetic). Send qualified, booked and won events back.
- **Every platform has a learning floor in conversions.** Google judges Smart Bidding on 30 conversions (50 for tROAS); Meta's guidance is about 50 events per 7 days per ad set; TikTok Smart+ wants 10x CPA a day (30x with a target); Pinterest wants 50 conversions a week and 5x CPA a day. Below the floor, consolidate or pick another channel; never fragment.
- **Search harvests demand, social creates it.** Google wins where people already search (urgent services, named products, "near me"). Meta and TikTok win where the product can be shown and the buyer did not know to look.
- **Platform ROAS is not profit.** Platforms overlap, count view-throughs and ignore refunds. Business truth is MER, blended CAC and contribution, checked with holdouts.
- **Post-click usually beats more spend.** Answering 95% of calls instead of 65% and booking 80% instead of 70% moved a plumber from about 2.4x to 4x ROAS at the same ad cost (operators report, r/PPC). A quiz form cut insurance CPL from EUR 19 to EUR 4 with nothing else changed (operators report).

## First session: ask, then compute

Ask the owner:

1. Business type, country, service area, and what one customer is worth: price, gross margin, repeat rate, refund rate.
2. Monthly budget they can lose while learning, and the CAC they can afford.
3. Current channels, last 90 days of spend by channel, and who manages them (agency, rep, self).
4. Read access to every ad account, GA4, the CRM or store backend, and the call tracking.
5. What counts as a real customer: booked job, paid order, showed appointment, signed contract.
6. Who answers leads and how fast; hours covered; capacity for more work.
7. Offers they will and will not run; claims they can prove; regulated category (health, finance, housing, employment, alcohol, legal, gambling, weight loss).
8. Past bans, disapprovals or account restrictions.

Then compute ([references/economics-and-budgets.md](references/economics-and-budgets.md)):

```
contribution per customer = first-order gross profit + expected repeat gross profit x repeat share
allowable CAC = contribution per customer x share you accept (start 30 to 50% for services, payback-based for subscriptions)
break-even ROAS = 1 / contribution margin rate      (40% margin -> 2.5x)
allowable CPL = allowable CAC x lead-to-customer rate
learning budget = conversions the platform needs x expected CPA     (Google 30 x CPA; TikTok 10x CPA/day; Pinterest 5x CPA/day)
ad ceiling = daily budget x 14 / (2 x target CPA)      (each ad gets 2x CPA over a 14-day read)
MER = total revenue / total paid media spend
blended CAC = total ad spend / new customers (from the CRM or store, not the platform)
```

If the learning budget for a channel exceeds what the owner can lose, that channel is out, whatever the benchmarks say.

## Benchmarks to check first

US data unless noted. Compare inside the same conversion definition: a Search "CPL" is any configured lead; a Meta ecommerce CVR is purchases.

| Metric | Typical | Source, year |
|---|---|---|
| Google Search CTR / CPC / CVR / CPL, all industries | 6.64% / $5.42 / 8.18% / $66.69 | WordStream/LocaliQ, 13,000+ campaigns, Apr 2025 to Mar 2026 |
| Search CPC: legal / home improvement / travel / restaurants | $9.87 / $8.33 / $2.14 / $2.05 | same |
| Meta lead campaigns CPC / CVR / CPL | $1.92 / 7.72% / $27.66 (+20.94% YoY) | WordStream 2025 |
| Meta ecommerce CPM / CTR / CVR / CPA / ROAS (median) | $15.06 / 2.39% / 1.53% / $38.99 / 1.88x | Triple Whale, Aug 2025 to Jul 2026 |
| Performance Max ecommerce ROAS median / p75 | 2.50x / 2.80x | Olifant, 18 accounts, 2025 to 2026 (agency) |
| Home services Search CPL / LSA CPL | $90.92 / $53 | LocaliQ 2025; SearchLight Feb 2026 |
| Landing page CVR median (industry range) | 6.6% (3.8 to 12.3%) | Unbounce, 41,000 pages, 2023 to 2024 |

Full tables by vertical, top-quartile figures, learning floors and operator numbers: [references/benchmarks.md](references/benchmarks.md). No credible universal "minimum daily budget" exists; derive it from CPA.

## Pick the channel by intent and budget

| Daily budget | Local lead gen | Ecommerce | B2B and coaching |
|---|---|---|---|
| $10 to 50 | Google exact/phrase Search or LSA; Nextdoor for very local | One Meta campaign, or Shopping/feed-only PMax | High-intent Search only |
| $50 to 250 | Search + LSA, or Search + Meta leads; one second channel | Meta core + brand and non-brand Google | Search + Meta or LinkedIn retargeting |
| $250 to 1,000 | Add PMax with CRM feedback; TikTok only if 10x CPA fits | Meta + Shopping/PMax; structured creative volume; TikTok or Pinterest by fit | Search + Meta, YouTube or Demand Gen tests; CRM values mandatory |
| $1,000 to 5,000 | Geo, offer and value splits; geo holdouts | Portfolio, new-customer bidding, incrementality tests | Pipeline-value bidding, holdouts |

Synthesis from platform learning floors (research report, 2026). One paid channel at a time until it is profitable; under $2,000 a month, never more than two.

## Decision rules, in order

1. **Tracking before spend.** One primary conversion per goal, fired on confirmed success, deduplicated (pixel + CAPI share `event_id`), tested with a real submission. Test GCLID capture free with `yoursite.com/?gclid=test` and check the CRM.
2. **Post-click before traffic.** Answer rate 90%+, first reply within 5 minutes, landing page matches the ad, one CTA, under 3 seconds on mobile.
3. **Consolidate to the learning floor.** On Meta at $10 to 250 a day: one prospecting campaign, usually one broad ad set, distinct concepts. On Google: brand, non-brand and competitor campaigns with separate budgets, nothing else until each converts.
4. **Optimize the deepest event that still reaches the floor.** Purchase or qualified lead first; step up the funnel only if volume is impossible, and import offline outcomes as soon as you can.
5. **Test concepts, not tweaks.** Hold offer and event constant, launch 3 to 6 materially different angles, judge at concept level. Iterate only on winners.
6. **Kill by staged spend, not by feel.** Target CPA T: under 0.5T fix only broken things; at 1T to 1.5T with no lower-funnel signal, stop; 1T to 2T with good add-to-cart or qualified signals, continue; past 2T with no conversion, require a written reason.
7. **Scale what holds on marginal CAC.** Meta: +20% at most every 3 to 4 days while the trailing 3-day CPA is at target; 5 to 10% steps above $500 a day; or duplicate the winner into a new campaign. Google: budget steps of 5 to 20%, target moves of 10 to 15%, never over 30%.
8. **Judge on blended numbers weekly.** Platform ROAS for in-platform choices, MER and blended CAC for budget, a holdout before you call anything incremental.

## Meta in one screen

- **Structure:** one CBO/Advantage+ campaign; testing lane about 20% of budget, scaling about 80% (coreyhaines31). Separate campaigns only for a real business split: offer, country, margin tier, special ad category.
- **Creative is targeting:** 20 ads should be 20 angles, not 4 angles in 5 versions. Hook-only edits of one video now count as one concept.
- **Volume:** at $50 a day, at least 3 to 4 new concepts a week; at $500+, 10 to 20. No 2024 creative stayed top for more than 5 months versus about a year in 2022 (operators report).
- **Kill switches:** turn off Advantage+ creative enhancements, "test new optimizations", AI translations and auto music at account level; recheck after every duplicate. They re-enable themselves.
- **CAPI:** purchase EMQ 8+ (9.3 good, under 6 investigate). Automatic advanced matching on.
- **Leads:** Higher Intent form, 1 to 3 multiple-choice qualifiers, a field that cannot autofill, a confirmation screen that says "call us now". Then speed to lead.
- **Messaging ads:** judge message start, qualified conversation, booked; never message-start CPA alone.

Depth: [references/meta.md](references/meta.md).

## Google in one screen

- **Settings first:** Presence (not "presence or interest"), Search Partners and Display off, auto-apply recommendations off, account-level automated assets off, PMax "Sourced videos" off.
- **Match types:** start exact + phrase on high-intent themes with a starter negative list; add broad with smart bidding only after 30+ conversions a month and clean tracking.
- **Bidding ladder:** under 15 conversions a month Max Clicks with a CPC cap or Max Conversions; 15 to 30 Max Conversions; 30+ tCPA at trailing actual; values flowing, tROAS. Since 17 August 2026 budget-limited target campaigns aim to hit, not beat, the target (five practitioner threads): reset targets to actual results.
- **PMax:** never the first campaign for local lead gen; brand exclusions on; CRM quality checked against Search leads. For ecommerce under about $2,000 a month, feed-only PMax plus a brand campaign.
- **AI Max:** experiment only, 50/50, watch the search terms weekly for 3 months.
- **Calls:** call tracking with DNI, count calls over 60 seconds or booked, not button taps.
- **LSA:** pay per lead, answer every call, dispute junk weekly. Mechanics live in `home-services` (lsa-and-lead-platforms.md).

Depth: [references/google.md](references/google.md).

## TikTok and smaller channels

- **TikTok Smart+:** at least 6 creatives, 7 days untouched, 10x CPA a day minimum. A $50/day account with a $30 CPA cannot meet it. Spark Ads keep the post's social proof.
- **GMV Max** counts organic orders of promoted products: report it next to a blended view, never as incremental ROAS.
- **Pinterest:** 50 conversions a week, 5x CPA a day, 10 ads per ad group; a $100 split test means nothing (Pinterest suggests $825+ per test arm).
- **Reddit:** default attribution 28-day click + 1-day view, ad groups can overspend 20%. Check GA4 sessions per click before believing it.
- **Nextdoor:** from $5 a day; location in the copy +17% CTR, real photos +10%, no logo +22% (Nextdoor 2024 study).
- **Microsoft:** import the proven Google Search build, constrain budget, verify UET.

Depth: [references/tiktok-and-other-channels.md](references/tiktok-and-other-channels.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data or platforms say | Rule |
|---|---|---|---|
| Broad match | Exact only, broad burns money (6+ threads) | Google: broad + Smart Bidding (its 25% uplift claim is 2020 data) | Exact/phrase until 30 conversions a month and clean tracking, then a broad experiment |
| Meta test structure | ABO per concept vs one CBO for all | Meta: consolidate to reach event density | Testing CBO with ad-set minimums, or ABO at 1 to 2 expected conversions a day per ad set; graduate winners |
| Kill threshold | $20, 2x AOV, 3x CPA | Statistics: zero conversions at 3x target is still about 5% likely by chance | Staged stop rule above; concept dies after 3 failed executions |
| Scaling step | 5% to 50% | TikTok up to 30% at 90% budget use; Pinterest 20 to 30% | +20% every 3 to 4 days, smaller above $500/day, or horizontal duplication |
| UGC vs statics | UGC always wins | Motion 2026 (reported by Motion, not independently checked): text-only 11.6% hit rate, UGC 7.6%, high production 7.0% | Run a low-fi static lane and a video lane; validate concepts as statics first |
| PMax | Junk for local leads | Google: PMax with offline quality feedback | Search first; PMax only with brand exclusions and CRM-graded leads |
| Platform ROAS | "Ads Manager says 4x" | Meta overreports 15 to 30% vs server truth (operators); windows overlap | Decide budgets on MER and blended CAC |

## Never

- Never scale on CPL, CTR, cheap CPMs or platform ROAS alone; never celebrate PMax or brand-inflated ROAS before splitting brand out.
- Never let a Google rep, auto-apply or an AI agent change the account without an approved written diff.
- Never name audiences or custom conversions after health conditions or financial status, or run housing, employment or financial offers outside their special ad category.
- Never recreate a disabled account's campaign for the same Page in the same Business Manager; never fund Meta with a credit line you cannot watch.
- Never invent negatives without a search-terms report, invent a benchmark, or present an operator anecdote as measured data.
- Never fabricate reviews, testimonials, before/after images or scarcity in ads.
- Never sum conversions across platforms.

## References

- [benchmarks.md](references/benchmarks.md): CPM, CTR, CPC, CPL, CVR, ROAS by platform and vertical, top quartiles, learning floors, creative hit rates, operator numbers.
- [economics-and-budgets.md](references/economics-and-budgets.md): every formula with worked examples, budget tiers, learn/scale/kill rules, test throughput, sample sizes.
- [meta.md](references/meta.md): Andromeda, Advantage+, structure by budget, learning math, testing framework, fatigue, bids, CAPI, lead forms, messaging ads, retargeting, settings traps.
- [google.md](references/google.md): match types, negatives, RSAs, bidding ladder, the August 2026 target change, PMax, brand, AI Max, Demand Gen, YouTube, offline import, calls, LSA summary, Microsoft.
- [tiktok-and-other-channels.md](references/tiktok-and-other-channels.md): Smart+, Spark, GMV Max, Pinterest, Reddit, Nextdoor, LinkedIn, Amazon, Etsy, ChatGPT ads, Yelp.
- [creative.md](references/creative.md): hook formulas with data, formats ranked, angle taxonomy, VoC research, brief template, iteration and fatigue fixes.
- [offers-and-post-click.md](references/offers-and-post-click.md): offer toolkit, landing page levers with numbers, forms, quizzes, speed to lead, call handling, messaging funnels.
- [measurement.md](references/measurement.md): tracking stack, UTMs, dedup, EMQ, offline conversions, windows, MER, blended CAC, holdouts and geo tests on small budgets, reporting.
- [policy-and-accounts.md](references/policy-and-accounts.md): special ad categories, restricted verticals, bans, prevention and recovery, billing safety, agent write rules.
- [audit-checklist.md](references/audit-checklist.md): pass/fail rules for Meta, Google, TikTok and tracking, with scoring.
- [operations-and-agency-tricks.md](references/operations-and-agency-tricks.md): weekly cadence, change logs, rep handling scripts, competitor research, reporting templates.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan with exit checks and owner questions.
- Sibling skills hold the segment angles and win on their own KPIs: `home-services` (LSA mechanics, GP CAC, answer rate), `beauty-business` (completed first-visit CAC, med spa rules), `education-coaching` (max CPL, 1.25x kill rule), `ecommerce-brand` (break-even ROAS, Amazon, Etsy, TikTok Shop), `restaurant` (new-guest CAC, delivery fees), `local-seo` (GBP, call tracking on GBP), `email-sms-loyalty` (flows to build before spending, WhatsApp windows).
