---
name: home-services
description: "Grow a home or local service business: house and office cleaning, lawn care, landscaping, pressure and window washing, auto detailing, pest control, handyman, painting, junk removal, grooming, dog walking and training, photography, plumbing, HVAC, electrical. Use for cost per booked job, Local Services Ads, Angi, Thumbtack, Yelp, Nextdoor, door hangers, yard signs, EDDM, speed to lead, quotes and follow-up, recurring plans, pricing, commercial accounts, seasonality."
---

# Home services: answer fast, quote well, fill the route

For owner-operators up to about 20 staff in cleaning (residential and commercial), lawn and landscaping, pressure washing, window cleaning, auto detailing, pest control, handyman, painting, junk removal, pet services, photographers and small trades (plumbing, HVAC, electrical). Built from 286 practitioner threads out of 817 scanned (r/sweatystartup, r/smallbusiness, r/pressurewashing, r/AutoDetailing, r/WeddingPhotography, r/localseo, r/GoogleMyBusiness), 2025 to 2026 data (Invoca, Jobber, ServiceTitan, Housecall Pro, LocaliQ, LSA agency datasets, USPS, Google's own LSA and Business Profile help) and the best public skills, mainly anthropics small-business (Apache-2.0). "Operators report" marks a Reddit anecdote with its thread score; everything else carries its source and year. Full list: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

## How these businesses actually grow

- **The biggest leak is unanswered demand, not traffic.** Only 52% of inbound home-service calls reached a person; of answered marketing calls, 38% were real leads and 45% of those booked on the call (Invoca, 2026). Jobber's December 2025 survey: 20% of pros reply within an hour, while over half of customers expect it. One pressure washer tracked it for a month: texting back within about 5 minutes won roughly 70% of jobs, and overall close rate went from 40% to 75% once replies were instant (operators report, r/pressurewashing).
- **Referrals and repeat work carry the business; paid sources fill gaps.** 59% of owners name referrals and 59% name repeat work as a top source; Facebook 32%, Google Search 20%, LSA 19%, lead sites 16%, door-to-door, postcards and yard signs about 8% each. Jobber's top performers run 3 to 5 sources (Jobber, 2026, vendor survey).
- **Google is the main free channel once reviews build.** Owners attribute 90 to 95% of new customers to the Google profile (operators report, r/sweatystartup 477, r/pressurewashing 338). GBP depth lives in `local-seo`; this skill only adds the home-service angles.
- **Two kinds of businesses.** Demand capture (plumbing, HVAC, electrical, pest, urgent junk removal) wins on answer rate and LSA. Considered purchases (painting, landscaping projects, photography, training) win on portfolio, quoting and follow-up. Recurring routes (cleaning, lawn, pest, pool, pet waste, grooming, windows) win on lifetime value and route density.
- **Route density is margin.** 39 pet-waste properties in about 9 hours with 2 to 5 minutes between stops (operators report, r/sweatystartup 431). A tech doing 35 stops instead of 20 produces 75% more stops for the same day (Glacier Lake Partners, 2026, M&A advisor data). Out-of-route customers are a more expensive product.
- **Offline works around jobs, not citywide.** Neighbor offers and signs near active jobs convert; blanket door hangers often return zero (300 hangers, 0 leads; 150 hangers, 0 calls; r/pressurewashing 338).
- **Lead marketplaces are rented, shared demand.** Judge them on cost per completed job and gross profit, never on lead price.

## First session: ask, then compute

Ask the owner:

1. Trade, services and which 3 make the most profit; solo or crew; country and towns served (and which towns are worth the drive).
2. Field service software (Jobber, Housecall Pro, ServiceTitan, GorillaDesk, spreadsheet) and whether you can export 12 months of leads, quotes, jobs and invoices with lead source.
3. Who answers the phone, when, and what happens to missed calls and after-hours forms.
4. Current lead sources and monthly spend per source, including LSA, Angi, Thumbtack, Yelp, Nextdoor, mail, signs.
5. Average ticket, minimum charge, gross margin per job (labor, materials, drive time), crew capacity per week.
6. Quote process: how fast quotes go out, by text or email, whether unsold quotes get any follow-up.
7. Share of revenue that is recurring; plans or memberships offered; churn reasons if known.
8. Google rating and count vs the local top 3 (hand to `local-seo` for the full audit).
9. Seasonal peaks and dead months; what the crew does in the off-season.
10. Offers they will and will not run; who may change prices; licenses and insurance (needed for LSA).

Then compute ([references/economics.md](references/economics.md)):

```
answer rate = calls answered live / inbound calls (staffed hours and after hours separately)
speed to lead = median minutes from inquiry to first human or useful reply
booked CAC = channel spend / booked jobs          completed CAC = spend / completed first jobs
GP CAC = channel spend / first-job gross profit   (the number to compare across channels)
quote win rate = quotes won / quotes sent (by service, by tier, by source)
recurring LTV = gross profit per visit x visits per year x expected years
route efficiency = drive minutes / total route minutes; revenue per route-hour
allowable CAC = first-job gross profit + (expected repeat gross profit x share who repeat)
unsold quote pool = value of quotes with no decision in the last 90 days
```

Report the three biggest leaks in money. A typical first finding: missed calls and unworked quotes are worth more than any new channel.

## Benchmarks to check first

| Metric | Typical | Strong | Source |
|---|---|---|---|
| Calls answered by a person | 52% | 90%+ is the LSA operating target | Invoca 2026; harvest (localseoskills, MIT) |
| Leads converting on the call | 45% (plumbing 55, pest 55, lawn/tree 54, HVAC 43) | paid search 48% | Invoca 2026 |
| Reply within 1 hour | 20% of pros | top businesses average under 60 min | Jobber 2026 |
| Quote win rate | 69% of owners win over half | Jobber top performers over 60%; near 100% = underpriced | Jobber 2026 |
| Google Search CPL | $90.92 all home services; cleaning $46.99, plumbing $129.02, painting $138.38 | | LocaliQ 2025 (Apr 2024 to Mar 2025) |
| LSA CPL | $53 blended; electrical $39, HVAC $51, plumbing $57; cleaning $33, junk $33 | book rate 43.9% | SearchLight Feb 2026; 99 Calls 2026 (agency data) |
| Direct mail response, home services | 3.75% | | Postalytics 2025 (vendor) |
| EDDM postage | $0.260 per piece | | USPS 2026 |
| Owners who raised prices last year | 65% (cleaning 55%, HVAC 83%) | 80% of $500K+ businesses | Jobber 2026 |

More, with denominators and bias notes: [references/benchmarks.md](references/benchmarks.md). No robust benchmark exists for Angi, Thumbtack, Yelp or Nextdoor cost per lead, yard-sign conversion, or cross-trade LTV. Say so instead of inventing one.

## Decision rules, in order

1. **Fix answering before buying anything.** Missed-call text back, a trained answering service or AI receptionist answering in the business name, and a 5-minute reply target in staffed hours. If a channel produces leads faster than the team answers, cut spend: unanswered paid leads still cost money (LSA bills an in-hours missed call held over 20 seconds).
2. **Work the unsold quote pool before new leads.** Follow up every quote on a fixed cadence (see below). ServiceTitan's 2025 survey: among $10M+ contractors, 47% say estimate follow-up produces 11 to 15% of revenue (self-reported).
3. **Neighbor saturation around every job.** Cards on every job, a doorstep offer to the 20 to 100 homes nearby while the crew is there, a yard sign where allowed, a readable truck. Cheapest acquisition there is.
4. **Google profile and reviews next** (hand to `local-seo`): every completed job gets the same neutral review request; no gating, no incentives, never ask for Yelp reviews.
5. **Then one paid channel at a time.** Urgent trades: LSA first, then Search. Visual and recurring services: Nextdoor and Meta with real before/after work. Lead marketplaces last, as a bounded test of 20 to 30 leads with a kill rule on GP CAC.
6. **Sell recurrence at the relief moment.** Every eligible one-off job ends with a plan offer. Price per visit lower for higher frequency; never let a member discount eat the route margin.
7. **Densify before expanding.** Stop marketing to remote micro-clusters until pricing covers the drive or the cluster fills. Referral rewards weighted by distance to existing stops.
8. **Raise prices when the calendar is full and win rate is high.** Test 5 to 10% on new quotes first; move early customers off legacy rates.

## Speed to lead in one screen

- **First reply:** name the specific job, ask one question, do not demand contact details first. That pattern got a 60.5% 24-hour reply rate vs 50.3% across 4,699 Yelp, Thumbtack and LSA conversations (LeadTruffle, Sept 2026, vendor data).
- **Missed-call text:** "Hi, this is [Business]. Sorry we missed your call. Are you looking for [service]? Reply with your ZIP and a one-line description and I'll tell you the next available time."
- **Quotes:** send within 30 minutes of the call from templates; give a range by phone for size-based work ("most houses your size land between X and Y, I confirm when I measure"); qualify on price per foot or minimum before driving out (a fence installer and a Christmas-light installer cut wasted estimates this way, operators report).
- **Follow-up:** same-day quote, 24 hours, day 3 (price, timing or scope question), day 7 (two named slots), day 14 close the loop, day 30 for big projects. One cleaner followed up at 1 hour, then days 1, 2, 3 and 4 because rivals sent one quote and stopped (r/sweatystartup 252).
- **After hours:** list hours you actually answer. Listing 24/7 without coverage produced 1-star reviews (operators report, r/localseo 95).

Triage, reply templates and the full cadence: [references/speed-to-lead-and-quoting.md](references/speed-to-lead-and-quoting.md).

## Quoting and pricing in one screen

- **Price from the target day, not the competitor.** Target revenue per hour (operators report $100 to $200 per working hour for exterior cleaning) plus a minimum job charge ($130 to $250 is common in pressure washing and gutters) so a short job still pays for the drive.
- **Three prices before you quote:** the painter's method is 50%, 45% and 40% margin tiers; open at the top, concede only in exchange for booking today, walk at the floor (r/sweatystartup 262, credited with scaling to $1M).
- **Good-better-best on real scope differences** (repair, repair plus prevention, replacement). 54% of thriving contractors offer three options on at least half of jobs vs under 10% for struggling ones (ServiceTitan 2025, correlation).
- **Budget objection = smaller scope, same rate.** "What budget range are you working with? Sometimes I can adjust the scope to fit."
- **Show discounts as a separate line** with the reason and an end date; never zero out line items.
- **Write the scope surface by surface** (driveway, walkway, patio, pool deck) and get it signed. The classic loss: agreeing $100 for three hours, then a demanded extra patio and $60 paid.
- **Financing on $500+ jobs:** 62% of homeowners say financing makes them more likely to proceed; 75% would hire rather than DIY at $1,000+ (Housecall Pro, 2026 survey).

Methods by trade, raises and add-ons: [references/pricing.md](references/pricing.md).

## Recurring revenue

- **Plan structure:** Basic (scheduled visits plus reminder), Priority (plus priority scheduling and waived call-out fee), Protection (plus consumables or inspection and a defined credit). For HVAC, operators report 200 to 400 agreements at $15 to $25 a month, and maintenance customers converting to replacements at 3 to 4x cold leads (r/smallbusiness 535).
- **Targets to aim at, not averages:** ServiceTitan's playbook uses 30% service-call-to-membership and 80% tune-up-to-agreement for techs (partly pre-2024).
- **Cleaning and lawn:** sell frequency as the price lever. Biweekly is the largest recurring cohort for one affluent-area cleaner; refuse less-than-monthly clients who expect a full reset each visit.
- **Pet waste:** $16 one dog, $19 two dogs weekly, or $45 a month entry, no contract (r/sweatystartup 431).
- **Win-back by each customer's rhythm:** quiet = gap over 2x their own median interval, gone = over 3x (an annual tune-up at 13 months is normal). First message never pitches.

Plans, cross-sells and churn: [references/recurring-and-retention.md](references/recurring-and-retention.md).

## Seasonality

Build next year's budget calendar from last year's booked jobs, not leads. Pre-sell before the peak (one window cleaner booked about $90,000 of spring work by knocking doors at minus 30 C in winter with 25% deposits, r/sweatystartup 453). In the peak, shift spend to high-intent capture and protect answer rate; in the trough, sell interior work, maintenance plans and commercial contracts. Weather is the top scaling constraint for 34% of owners (Jobber 2026). Calendar by trade: [references/by-trade.md](references/by-trade.md).

## When practitioners and the data disagree

| Topic | Operators say | Data says | Rule |
|---|---|---|---|
| Door hangers | Zero calls from 150 to 300 | Vendor case: 1.8% by day 14, 4.5% by day 60 | Only around jobs or dense routes, with a tracked number; judge at 60 days |
| EDDM | $200 mailing returned $0 | 3.75% vendor response; postcards kept 18 months | Mail the same 400 to 2,000 homes 3 to 4 times or not at all |
| Five-minute rule | 5-minute replies win about 70% | The famous 21x stat is from 2007-era studies | Target 5 minutes; measure your own win rate by reply time |
| Discount to start | 20% intro for reviews worked for one cleaner | Deep discounts drew leads that ghosted at quote (2 of 2) | Name it "intro pricing", with an end date; never free |
| LSA disputes | "Dispute every bad lead" | Credits no longer granted for wrong job type or area; none in EMEA | Fix targeting; reconcile weekly |
| Yard signs | Main source for a gutter and a junk business | 100 signs, no calls for another | Busy stops, readable number, tracked line; reorder only on calls |

## Never

- Never gate, incentivize or set staff quotas for Google reviews; never solicit Yelp reviews. Never buy reviews: one buyer lost all 20 within two months and dropped below the starting rank.
- Never use "Google Guaranteed" wording: the badge became Google Verified in October 2025 and the money-back guarantee ended.
- Never claim a neighbor is a customer unless true and permitted ("I'm taking care of your neighbor Linda tomorrow" only if Linda agreed).
- Never verify a Google profile on a virtual office or show a home address on a service-area profile; one advertiser spending $150,000 a month lost LSA access this way.
- Never scale a channel on cost per lead, or add a marketplace while calls are going unanswered.
- Never send promotional texts without consent; a reply to the customer's own call is service, a promo blast is marketing (see `email-sms-loyalty`).
- Never invent a benchmark, an offer the owner has not approved, a license, or a customer quote.

## Before writing any customer message

Use [references/scripts.md](references/scripts.md): missed-call text, first replies, quote follow-ups, objection and negotiation lines, neighbor and door-knock openers, commercial walk-ins, plan offers, price increase notice, scope and expectation disclaimers, refusal and referral-out lines.

## References

- [benchmarks.md](references/benchmarks.md): metric, typical, strong, source, year; CPL by trade and channel; operator-reported numbers kept separate.
- [economics.md](references/economics.md): every formula with worked examples (funnel, GP CAC, LTV, route density, minimums, plan math, offline break-even, referral budget).
- [lsa-and-lead-platforms.md](references/lsa-and-lead-platforms.md): LSA ranking, billing, disputes, Google Verified; Angi, Thumbtack, Yelp, Nextdoor, Bark, Houzz, Porch, Rover and others with verdicts; Search and Meta notes.
- [offline-and-neighbor.md](references/offline-and-neighbor.md): door hangers, yard signs, mail, EDDM, door knocking, vehicles, neighbor saturation, with response data and tests.
- [speed-to-lead-and-quoting.md](references/speed-to-lead-and-quoting.md): triage, response system, quote building, negotiation, unsold-quote cadence.
- [recurring-and-retention.md](references/recurring-and-retention.md): plans by trade, conversion moments, cross-sells, service recovery, win-back.
- [pricing.md](references/pricing.md): methods, minimums, operator price points, good-better-best, raises, discounts.
- [commercial-and-partnerships.md](references/commercial-and-partnerships.md): commercial cleaning sales, property managers, realtors, builders, HOAs, venues and planners, referral programs.
- [by-trade.md](references/by-trade.md): notes per trade and the seasonality calendar.
- [scripts.md](references/scripts.md): verbatim wording.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan with exit checks.
- Sibling skills: `local-seo` (Google profile, reviews, map pack, suspensions, AI answers), `email-sms-loyalty` (flows, consent, SMS compliance, loyalty), `paid-ads` (Google, Meta and account depth).
