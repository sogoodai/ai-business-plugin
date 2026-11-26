# Economics: what to compute before recommending anything

Pull 12 months of appointments and payments from the booking software (covers seasonality). If the owner has no export, ask for one typical week's calendar and the price list, and label every result as an estimate.

## Capacity

```
utilization = completed booked service hours / sellable provider hours
revenue per productive hour = service revenue / completed service hours
revenue per sellable hour = service revenue / sellable hours
```

- Compute by provider x weekday x 2-hour block. The average hides the problem: Saturday at 95% and Tuesday at 20% need opposite actions.
- Sellable hours = hours the provider is on the schedule and bookable, minus fixed breaks. Do not count hours the owner refuses to work.
- Compare with the category median and top quartile in [benchmarks.md](benchmarks.md): 49% and 63% for full-service salons, 47% and 65% for specialty, 56% and 66% for barbers, 38% for waxing and med spas (Zenoti, 2025 data).
- Worked: a specialty salon moving from the 47% median to the 65% top quartile gets 18 points, which is 38% more occupied hours on its current base, at no extra rent. That is usually worth more than any ad budget it could afford.
- Trick: report revenue per sellable hour next to revenue per client. A provider with a high ticket and 30% utilization earns less per sellable hour than a mid-ticket provider at 65%.

## Contribution and lifetime value

```
contribution per visit = price + add-ons + retail margin
                         - provider commission (or the owner's own hourly cost)
                         - product and back-bar
                         - card fees
                         - marketplace fee (first visit only, if any)
                         - discount
contribution LTV = contribution per visit x expected completed visits before churn
```

- Revenue LTV (average spend x visits per year x years, the [Phorest](https://www.phorest.com/blog/how-smart-salons-spas-and-clinics-use-data-to-unlock-hidden-growth/) formula) overstates what you can spend to acquire. Use contribution.
- Expected visits: use the business's own first-to-second and second-to-third completed-visit rates, not a guessed lifetime. Most loss happens before visit two.
- Segment at least: new, second visit, established, lapsing, reactivated. Do not stop at new versus returning.
- Solo owners: price your own time. Required hourly rate = (target take-home + all annual costs + taxes) / realistic billable hours a year. Recompute every year after taxes (operators report this takes emotion out of price talks).

## Acquisition

```
completed new-client CAC = channel spend / completed first visits
90-day payback = 90-day contribution of the acquired cohort / acquisition spend
scale only if: 90-day cohort contribution - acquisition cost > 0
```

- Never use cost per lead. A med spa case at $12.18 per lead was $251 per booked appointment ([MDConsultingNY](https://mdconsultingny.com/our-results/pdo-thread-lift-meta-ads/), 2026).
- Funnel to report weekly: spend, leads, booked, completed first visits, completed second visits, 90-day contribution.
- For consult-led services (color transformations, med spa): inquiry, consult booked, consult attended, treatment booked, treatment completed, 90-day repeat.

## Marketplaces

```
90-day marketplace cohort contribution = service + add-ons + retail + repeat revenue
    - provider pay - consumables - payment fees - marketplace fees - discounts
```

Compare with direct clients of the same service, provider and month. A marketplace that delivers first visits but poor second visits is an inventory liquidator, not an acquisition channel.

First-visit fee on a $150 service (published terms, November 2026): Fresha 20% = $30; Booksy Boost 30% = $45; Treatwell UK 35% = $52.50 + VAT; StyleSeat 30% capped at $50 = $45.

Trick for low tickets: on a $34 barber cut, Booksy Boost takes $10.20 and Fresha $6.80. If the barber earns 50% commission, the shop's $17 margin drops to $6.80 on Booksy before card fees. On a $20 brow wax the minimums bite: Booksy's $10 floor is 50% of gross, Fresha's $6 floor is 30%. Only worth it if the cohort comes back without the marketplace.

Other leak: a returning client who finds you on the marketplace instead of your own link can be charged as "new". Put your direct booking link everywhere the client already looks (Instagram bio, GBP, confirmation emails, receipts).

## Cancellations

```
monthly leak = unfilled cancellations and no-shows x average ticket
value of 1 point = appointments per month x 1% x average ticket
```

- At the specialty median $77 ticket and 1,000 appointments, each point of unfilled loss is $770 of booked revenue (arithmetic on Zenoti's 2025 ticket).
- Waxing at 18% cancellations (Zenoti, 2025) on 1,000 appointments at $34 puts about $6,100 a month in play. The fix is backfill speed, not fees.

## Price changes

```
volume you can lose before contribution falls = p / (m + p)
p = price increase as a fraction, m = current contribution margin as a fraction
```

- Worked: a 10% increase on a 40% contribution margin breaks even if you lose up to 20% of visits (0.10 / 0.50). Most increases lose far less, which is why waitlisted providers should raise.
- Watch 8 to 12 weeks after any change: booking rate, kept rebooks, cancellations, new-client conversion, contribution. Revenue alone lies: [PBA](https://www.probeauty.org/pro-beauty-pulse-october-2026-insights/) 2026 data show ticket growth covering flat visits.

## Discounts

```
cost of a blanket discount = discount % x revenue from clients who would have booked anyway
```

- Worked: 10% off sent to 100 clients who were going to book anyway gives away the value of 10 appointments before any new demand.
- Ladder for any offer: no-discount proof first, then a creditable deposit or consult, then an included low-cost add-on, then cash off. Cash off only for the group the cheaper steps failed on.

## Memberships

Track:

```
member contribution per provider hour = (dues - cost of redeemed services and perks) / provider hours redeemed
entitlement utilization = services redeemed / services included
```

- Plus freeze and cancel rate, add-on spend per member, frequency versus matched non-members, and unused liability (prepaid services owed; accounting treatment is local, ask the accountant).
- A membership that moves full-price Saturday clients onto discounted dues looks good in billing and loses money per hour. Cap peak-time redemptions or price them up.

## Commission versus booth rent

```
commission chair contribution per hour = service price - provider commission - variable cost - payment and acquisition cost
rental chair contribution per hour = rent collected / chair hours supplied - landlord variable costs
```

Commission gives the owner control over price, client data, hours and retention systems but leaves the owner holding utilization risk. Rent stabilizes income and gives up that control. Worker classification is jurisdiction-specific; never change pay or classification as a marketing action, route it to an accountant or lawyer.

## Retail and add-ons

```
retail attach rate = service visits with 1+ retail item / eligible service visits
retail revenue / service revenue, units per 100 visits, gross profit per visit
add-on attach rate = visits with an add-on / visits
```

Units and attach rate catch what dollars hide: in September 2026, average product price rose 7.10% while units fell 7.86% ([PBA](https://www.probeauty.org/pro-beauty-pulse-october-2026-insights/)).

## Review math

Adapted from unifapi-agent/agents (MIT, see [sources.md](sources.md)).

```
5-star reviews needed to reach target rating = ceil(count x (target - rating) / (5 - target))
catch-up target per quarter = (leader count - your count) / 4 + leader's reviews in the last 90 days
```

- Worked: 40 reviews at 4.4 stars to reach 4.7 needs ceil(40 x 0.3 / 0.3) = 40 new five-star reviews. Use your real new-review average instead of 5 if it is lower.
- Below about 4.3 stars, fix the rating (service and recovery) before chasing volume.
- If the catch-up target is over about 3x your current pace, target the nearest beatable competitor instead and call the leader a multi-year goal.
- Velocity beats totals: count reviews dated in the last 90 days and flag a "coasting" profile with a big total and few recent reviews.
