# Economics and budgets

Compute these before touching a campaign. Every budget, kill and scale decision below is a function of allowable CAC, not of a dollar figure someone read online.

## The core numbers

```
contribution margin rate = (price - COGS - fulfillment - payment fees - refunds) / price
contribution per order = price x contribution margin rate
break-even CPA (first order) = contribution per order
break-even ROAS = 1 / contribution margin rate
customer contribution = first-order contribution + repeat contribution x repeat share
allowable CAC = customer contribution x share you accept
allowable CPL = allowable CAC x lead-to-customer rate
marginal CPA = incremental spend / incremental accepted conversions
MER = total revenue / total paid media spend
blended CAC = total paid spend / new customers counted in the CRM or store
fee-inclusive ROAS = revenue / (spend + agency or management fee)
```

Worked examples:

- **Ecommerce:** $65 AOV, 40% contribution margin. Break-even ROAS 2.5x, break-even CPA $26. Platforms report ROAS on gross revenue before refunds, so compute break-even on the same gross number the platform reports (ecommerce-brand rule). A $79 bundle earns its own CPA target ($30 to 33 vs $25 on the single, operators report r/FacebookAds 329).
- **Local service:** $1,000 average job, 45% gross margin, 30% of customers rebook once a year. Customer contribution about $585. Accept 40%: allowable CAC $234. Leads close at 25%: allowable CPL $58. LocaliQ's plumbing Search CPL is $129 (2025): Search is unaffordable unless close rate or job value rises; LSA at $57 fits.
- **Coaching:** $3,000 program, 80% margin, accept 30%: allowable CAC $720. Calls close at 20%: allowable cost per booked call $144. The r/lifecoaching case ($65 per booked call) clears it.
- **Fee check:** 3.16 ROAS with the agency fee added becomes about 1.5 (operators report, r/googleads).
- **Cheap lead trap:** $20 CPL at 2% close = $1,000 CAC; $60 CPL at 15% close = $400 CAC. The expensive lead is 2.5x cheaper per customer.

Payback for subscriptions (coreyhaines31, MIT): `payback months = CAC / (monthly price x gross margin)`. Same $300 CAC: a $9 plan takes 33 months (do not fund), a $99 plan at 20% margin takes 15 months, a $999 plan under a month. Early churn shifts recovery: identical 12-month retention can recover in month 4 or month 6.

## Budget floors from learning math

```
Google test budget ~ 30 conversions x expected CPA         ($100 CPA -> $3,000, not $300)
Meta daily budget to exit learning ~ target CPA x 50 / 7   ($30 CPA -> about $215/day per ad set)
Meta practical test floor (operators) = 1 to 2 expected conversions a day per test ad set; minimum 1x AOV/day, ideal 3x CPA/day
TikTok Smart+ daily budget >= 10 x CPA (30x with a target)   ($40 CPA -> $400/day)
Pinterest Performance+ daily budget >= 5 x CPA                ($40 CPA -> $200/day)
Lead-gen minimum (operators, r/PPC) = enough for 1 to 3 qualified leads a day
```

When the floor is out of reach:

1. Consolidate: one campaign, one ad set, fewer ads.
2. Optimize a higher-frequency event that still predicts money (initiate checkout, qualified lead, booked call), and keep importing the real outcome.
3. Pick a channel whose floor fits (Search exact match, LSA pay-per-lead, Nextdoor at $5/day).
4. Accept a longer read: judge over 4 to 6 weeks, not days.

Never "test small, scale later" on a budget that cannot produce a readable sample (operators report, 39 upvotes, r/PPC).

## How many ads the budget can carry

```
ad ceiling = daily budget x 14 / (2 x target CPA)
```

Each ad needs about 2x target CPA of spend inside a 14-day read (coreyhaines31, MIT). $1,000/day at $500 target CPL: 14 ads; run 6 to 10. $50/day at $50 CPA: 7. $20/day at $40 CPA: 3. At the ceiling, a new test requires killing an ad first.

Related:

- **Creative supply caps budget:** a proven B2B ad absorbs about $5,000 a month before fatiguing, so proven-ad inventory needed is about monthly budget / $5,000. Never raise budget ahead of creative supply.
- **Test throughput:** tests per month about (monthly budget x 0.20) / (3 x target CPA). Win rates: iterations on winners about 25%, new concepts about 10%, blended about 1 in 6. To find N winners, plan about 6N tests.
- **Split:** about 80% to proven ads (scaling lane), 20% to tests (testing lane). The lane exists to protect test budget, not to segment audiences.

## Budget tiers

| Daily budget | Structure | Read cadence |
|---|---|---|
| $10 to 50 | One channel, one campaign, usually one ad set or ad group theme, 2 to 4 distinct concepts or 5 to 15 exact keywords | Weekly; decisions every 2 weeks |
| $50 to 250 | One core campaign plus one test or remarketing lane; maybe a second channel | Twice a week |
| $250 to 1,000 | Testing lane with protected budget, geo or value splits where conversion density allows, structured creative production | Mon/Wed/Fri cadence |
| $1,000 to 5,000 | Separate business questions (new vs returning, geo, offer, category), bid caps or cost caps, incrementality tests | Daily pacing check, weekly decisions |

Tier rules are a synthesis from platform learning mechanics (research report 2026), not a platform spend table. Operators add: save about $3,000 before starting Meta for ecommerce so you can run $100/day on 3 creatives (r/DigitalMarketing, 411), and treat the first 100 to 200 purchase or lead events as a learning cost, not a profit test (r/FacebookAds, 142).

## Learn: what to leave alone

- Meta: leave a new campaign 48 to 72 hours, first optimization on the morning of day 3, sorted by lifetime spend (r/FacebookAds 174). Cold/warm restructures often look flat or worse for 6 days and improve on day 7 (r/FacebookAds 150).
- TikTok: 7 days with no disruptive edits (platform).
- Pinterest: about 2 weeks; no more than 2 rounds of changes a week, 3 to 5 days to recalibrate after each (platform).
- Google: at most 2 major changes per campaign per month (operators, several threads); target moves take 1 to 2 conversion cycles; never judge the last 3 days (conversions post to click date, up to 72 hours lag).
- What resets learning (estimated, aaron-he-zhu, Apache-2.0): target change over 15 to 20%, budget change over 20%, adding or removing ad groups, changing conversion actions, switching bid strategy. Editing an ad's creative resets it; pausing does not. Add new ads beside winners instead of editing them.

## Kill: staged stop rules

For target CPA T (research report synthesis, agency heuristic):

| Spend on the ad, concept or keyword | Signal | Call |
|---|---|---|
| Under 0.5T | anything | Intervene only for broken tracking, wrong page, policy, or obviously junk traffic |
| About 1T | zero meaningful funnel progress (no add to cart, no form starts, no qualified conversation) | Pause or replace |
| 1T to 2T | healthy intermediate signals (ATC to checkout 3:1 or better, form starts) | Allow more evidence |
| Over 2T | no conversion | Continue only with a written reason |

For lead quality reads on Meta (coreyhaines31 two-stage system, MIT):

- **Stage 1, day 7:** fair-share spend = (campaign daily budget / active ads) x 7 x 0.5. An ad below it was deprioritized by Meta; kill it. Zero spend: kill now. Ongoing: at least 1x target CPL lifetime and under about $10 a day in the last 7 days, kill.
- **Stage 2, weekly on rolling 14 days:** spend under 3x target cost per qualified lead, wait (zero qualified leads at 3x has about 5% probability by chance; at 2x, 13%). Zero leads at 3x+: abandon the concept. Qualified rate under 40%: swap angle; 40 to 60%: monitor; 60%+: proceed. Cost per qualified lead at or under target: candidate; 1 to 1.5x: monitor; over 1.5x: swap.
- **Graduation (all required):** 5+ qualified leads, qualified rate 60%+, cost per qualified lead at or under target, running 14+ days, at least 1 qualified lead in the last 7 days. For appointment businesses the qualified event is "booked and showed".

Concept vs execution: three failed executions kill a concept; one failure kills an execution.

Zero-in-N sanity check for Search (coreyhaines31, MIT): zero conversions in 5 clicks only rules out a CVR of 45% or more; 10 clicks rules out 26%; 30 clicks 10%; 50 clicks 6%; 100 clicks 3%. `break-even CVR = CPC / target CPA`. If break-even CVR is below a plausible CVR for that traffic, the term is unmeasured, not failing.

Operator kill rules worth knowing (all self-reported): product tests under $30 change something after $40 with no purchase (r/dropship); set a hard cap per product test before launch, because "one more day" pushed failed tests from $100 to $800 (r/dropship); stop a $50 to 150/day product test not at break-even after 2 to 3 days (r/FacebookAds 133).

## Scale

| Method | Rule | Source |
|---|---|---|
| Vertical, Meta | +20% every 3 to 4 days once the trailing 3-day average holds target; 5 to 10% steps above $500/day | operators, several threads (205, 257, 555) |
| Vertical, Meta, symmetric | +20% after 3 to 7 good days; -20% after 2+ bad days; if not recovered 24 h later, stop and relaunch | r/FacebookAds 160 |
| Horizontal, Meta | duplicate the winning ad set or post ID into a new campaign at full budget; $250/day duplicates launched 5 to 7 days apart beat $300 | r/FacebookAds 555, 133 |
| TikTok | up to +30% when the campaign spends 90%+ of budget; bids no more than 15% every 2 days | TikTok 2025 |
| Pinterest | +20 to 30% gradually once Performance+ performs | Pinterest 2026 |
| Google budget | 5 to 20% steps; do not raise just because "limited by budget"; pull winners out of shared budgets | operators r/googleads 205, 101 |
| Google targets | move tCPA or tROAS 10 to 15% per step, never over 30%; wait 1 to 2 conversion cycles | Google, operators |
| Microsoft | if CPA beats Google by over 20%, +25% a month | indranilbanerjee, MIT |

Rules that keep scaling honest:

- **Measure the incremental spend, not the blend.** Raise budget 20 to 30%, compute ROAS on the extra spend only, stop when marginal ROAS reaches break-even (r/PPC).
- **Scale on net cash, not ROAS.** ROAS falling from 10 to 5 while spend goes $10k to $100k can mean far more profit (coreyhaines31).
- **Pausing a big-spend CBO ad set is a scaling event** for the survivors (losers spent $130, survivors $35, $30 and $5): check yesterday's spend before pausing.
- **Prospecting below break-even can be correct** when blended MER is healthy: TOF ROAS 2 against a break-even of 3 inside an overall 8 (r/FacebookAds 156).
- **High-ticket gate:** raise spend only when daily cash flow is positive and MER stays above target; expect a 20-day decision lag at $5,000 AOV (r/FacebookAds 74).
- **Seasonality:** Q4 CPMs run 60 to 80% higher and Q1 lowest (practitioner-reported, coreyhaines31); some brands break even Q1 to Q3 and cash in during Q4 (r/DigitalMarketing 411).
- **Ceiling check:** when more spend brings the same number of real leads, cut back. A plumber and an eight-figure advertiser both recovered efficiency by spending less (r/googleads 205).

## Allocate across channels

- Reserve commitments and measurement costs; protect campaigns with strong evidence of positive marginal contribution; fund bounded experiments with a hypothesis, decision date and stop condition; reallocate from the weakest marginal opportunity, not the worst average CPA (AgriciDaniel, MIT). Fixed splits like 70/20/10 are optional heuristics.
- Channel concentration over 80% of revenue from one paid platform is fragile even while growing (coreyhaines31 growth pulse).
- One beauty brand moved Google from 75% to 35% of budget (Meta 25%, TikTok 20%, community 20%) over 6 months: CAC -27%, revenue +40% (operators report, r/PPC 283). Treat as a case, not a rule.

## Sample size for A/B tests

Per variant, alpha 0.05, power 0.80, relative lift (aaron-he-zhu, Apache-2.0):

| Baseline CVR | 10% lift | 20% lift | 50% lift |
|---|---|---|---|
| 1% | about 150,000 | about 39,000 | about 6,000 |
| 3% | about 47,000 | about 12,000 | about 2,000 |
| 5% | about 27,000 | about 7,000 | about 1,200 |
| 10% | about 12,000 | about 3,000 | about 550 |

Add 20 to 30% for A/B/n; cap at 4 variants; run at least one full business cycle (1 to 2 weeks); no peeking. Most small accounts cannot run statistically clean landing page tests: run big swings (new offer, new page type) instead of button colors. A public table that uses n = Z^2 p(1-p)/E^2 with no power term understates samples about 10x; do not copy it.
