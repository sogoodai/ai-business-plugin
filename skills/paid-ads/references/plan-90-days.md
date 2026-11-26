# 90-day plan

For a small business starting or restarting paid ads. Order matters: measurement and economics, then one channel to a baseline, then the biggest bottleneck, then one challenger, then conversion quality, then scale. The plan follows the research report's operating sequence (2026) and the learning floors in [economics-and-budgets.md](economics-and-budgets.md).

Each phase ends with a short owner report: what changed, the scorecard numbers, what you need them to decide.

## Days 1 to 14: economics and measurement

**Week 1: numbers.**

- Compute allowable CAC, break-even ROAS and allowable CPL from real margin, repeat rate and close rate.
- Pull 90 days of spend by channel and the business's new customers in the same period. Compute MER or blended CAC as the baseline.
- Run the [audit-checklist.md](audit-checklist.md) on any existing account; fix every critical FAIL that does not need owner approval (tracking fixes do; budget changes do not).
- Write the policy gate: vertical x country x platform; special ad category if housing, employment, finance or politics.

**Week 2: tracking and post-click.**

- Platform tags, Meta CAPI (or the Shopify channel), Google Enhanced Conversions, UTMs, click IDs into hidden fields, CRM stages `Lead > Qualified > Booked > Won > Revenue`.
- Test: one real submission per platform arrives; `?gclid=test` reaches the CRM; Meta Test Events shows "Deduplicated".
- Speed to lead: instant SMS and email, staff alert, call within 5 minutes; call tracking; answer-rate check.
- Landing page: one page per offer, message match, one CTA, under 3 seconds on mobile, phone visible for local.

**Exit check:** a test conversion visible in every platform and the CRM; allowable CAC written down; answer rate measured.

**Ask the owner:** "What is one customer worth to you after costs, and how much can we spend learning before you need to see customers?"

## Days 15 to 30: one channel to a baseline

- Pick one primary channel by intent and budget: urgent local services start on Search or LSA; visually demonstrable ecommerce on Meta; B2B with search demand on Search; TikTok and Pinterest wait until their CPA multiples fit.
- Build the first inventory, not one idea: about 6 distinct concepts on Meta (validated as statics), or RSAs with 8 to 10 headlines and 5+ genuinely different, on 5 to 15 exact and phrase keywords per theme for Search.
- Settings from [google.md](google.md) or [meta.md](meta.md) applied before launch. Starter negatives labeled as starters.
- Leave it alone: Meta 72 hours before the first decision, TikTok 7 days, Google 2 weeks or 30 conversions.
- Daily: spend sanity check only (pacing, broken links, disapprovals, bots).

**Day 30 table** by campaign and creative: spend, impressions, clicks, landing page views, leads, qualified leads, booked or orders, customers, revenue, gross profit. Do not scale anything whose success disappears when you move from "lead" to "qualified lead" or from platform revenue to blended revenue.

**Ask the owner:** "Of these 20 leads, which became customers or real quotes?" Their answer is the first offline import.

## Days 31 to 45: fix the biggest bottleneck only

| Evidence | Fix |
|---|---|
| CTR weak, post-click fine | New concepts and hooks |
| CTR fine, page CVR weak vs same-vertical benchmark | Message match, speed, proof, form friction (quiz form) |
| Leads plentiful, quality poor | One discriminating question, Higher Intent form, `QualifiedLead` fed back |
| Search spend leaking | Classify search terms, negatives; do not cut bids blindly |
| Leads fine, sales poor | Speed to lead, call answering, follow-up sequence |

Kill and keep using the staged stop rules. Start the weekly creative cadence (at least 3 to 4 new concepts a week from $50/day).

## Days 46 to 60: one meaningful challenger

- Meta: a different concept cluster, an Advantage+ configuration, or a messaging-ad funnel against the incumbent.
- Google: a controlled broad match or AI Max experiment (50/50) once there are 30+ conversions a month, or PMax with brand exclusions and offline quality.
- TikTok Smart+ only if the budget meets 10x expected CPA a day; Pinterest Performance+ only near 50 conversions a week.
- Second channel only if the first is at or under allowable CAC and the budget allows both floors.

**Exit check:** each test has a hypothesis, a decision date and a stop rule written before launch.

## Days 61 to 75: push conversion quality upstream

- Import qualified, booked and won events into Google (Enhanced Conversions for Leads) and Meta (CRM events via CAPI) where policy permits. Keep both click IDs and hashed contact data.
- Add values: margin for ecommerce, job value or stage values for leads. Plan the switch of the new action to primary after the longer of 3 conversion cycles or 4 weeks.
- Move bidding up the ladder only when volume supports it (tCPA at trailing actual at 30+ conversions a month).
- LSA: weekly reconciliation of charged leads vs CRM, disputes filed.

## Days 76 to 90: scale proven economics and test incrementality

- Raise budgets 20% at most every 3 to 4 days where marginal CAC holds; compute ROAS on the added spend only.
- One incrementality check sized to the budget: budget halving on one channel for 2 to 4 weeks, a brand pause if you are the sole bidder, or a geo holdout at higher spend.
- Monthly creative retro; refresh the concept backlog from customer verbatims.

**Day-90 decision for each channel:**

- **Scale** when blended or qualified CAC is inside target and marginal performance survives more spend.
- **Iterate** when the funnel works except one identifiable stage.
- **Change the offer** when traffic and page behavior are reasonable but conversion stays weak across several concepts.
- **Change channel** when the platform's learning economics do not fit the budget.
- **Stop** when spend passed the predetermined evidence threshold without useful lower-funnel signal.

**Ask the owner:** "Do you want the next dollar to go to more of this channel, a second channel, or better follow-up?" Present the marginal CAC of each option.
