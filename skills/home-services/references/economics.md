# Economics: what to compute before recommending anything

Pull 12 months of leads, quotes, jobs and invoices from the field service software (Jobber, Housecall Pro, ServiceTitan, GorillaDesk) with the original lead source kept on every record. Twelve months covers seasonality. If the owner has no export, use one typical month and label every result as an estimate.

## The funnel, five stages

```
raw lead -> contacted -> qualified -> booked -> completed and collected -> gross profit
```

Minimum fields per lead: source, campaign, service, ZIP/postcode, received time, first-reply time, answered (y/n), qualified (y/n), quote value, won/lost and reason, scheduled date, completed, collected revenue, gross profit, recurring flag, review requested.

```
answer rate      = calls answered live / inbound calls
contact rate     = leads reached / raw leads
qualified rate   = qualified / contacted
book rate        = booked / qualified
show/complete    = completed / booked
```

- Measure time to a human or useful reply, not time to an auto-acknowledgment.
- Split answer rate by staffed hours and after hours. After-hours calls are often the urgent, high-intent ones.
- Marketplace "leads" are not your qualified leads. Keep your own definition.

## Cost per booked job and gross-profit CAC

```
CPL         = spend / raw leads
booked CAC  = spend / booked jobs           = CPL / (contact x qualified x book rate)
completed CAC = spend / completed first jobs
GP CAC      = spend / first-job gross profit  (below 1.0 = first job pays for the lead)
```

Worked (illustrative, from the research pass): a $50 lead that books 20% costs $250 a job; a $90 lead that books 60% costs $150. A $46.99 cleaning lead booking 15% costs $313; a $129 plumbing lead booking 55% costs $235 (LocaliQ 2025 CPLs, Invoca 2026 trade-level call conversion; definitions differ, so this is a sanity check, not a matched comparison; trade split reported by Invoca, not independently checked).

Shared marketplace leads: `effective cost per job = lead price / (P(you reach them first) x close rate)`. A $50 lead shared with four rivals, 20% chance you win the conversation, 30% close once talking = $833 per booked job (agency illustration, 2026). This is why marketplaces lose to fast-answered LSA and referrals for most trades.

## Allowable CAC and LTV

```
first-job GP     = price - labor (wages + payroll burden) - materials - drive time cost - fees
recurring LTV    = GP per visit x visits per year x expected years retained
allowable CAC    = first-job GP + (share who repeat x repeat GP over 12 to 24 months)
```

- Use gross profit, never revenue. No defensible cross-trade LTV benchmark exists; build it from the owner's own retention.
- Retention: count customers with a completed visit in each month after the first; years retained = 1 / annual churn.
- Attribute repeat revenue back to the original source. A channel that looks expensive on the first job can win on cohort value (pest, lawn, cleaning plans).
- Worked: biweekly cleaning at $160 a visit, 1 hour for two cleaners (operators report, r/sweatystartup 197). Say labor and supplies leave $90 GP per visit, 26 visits a year, 1.5 years average stay: LTV = $90 x 26 x 1.5 = $3,510. A $250 booked CAC is fine; the same CAC on a one-off $180 move-out clean is not.
- Trick: lower your target CAC when the calendar is full and raise it when idle capacity is expensive. Same channel, different answer by month.

## Route density

```
route efficiency  = drive minutes / total route minutes
revenue per route-hour = route revenue / (service + drive hours)
stops per route-day; GP per route-mile
cost of an out-of-route stop = extra drive minutes x loaded labor cost per minute + vehicle cost per mile
```

- Worked (operators report, r/smallbusiness 244): a job with a $40 margin, 1 hour on site and 30 minutes driving each way is $20 an hour before mileage. Same job next door to another stop is $40 an hour.
- Dense targets: 25 to 40 fertilization stops per tech per day in dense suburbs (Glacier Lake Partners 2026, advisor data); 39 pet-waste stops in about 9 hours at 2 to 5 minutes apart (r/sweatystartup 431); lawn crews mowing 30 to 40 yards a day in one subdivision with no drive time (r/sweatystartup 445).
- One lawn operator prefers 20 houses in one ZIP over 5 nearby and 15 spread across town (r/sweatystartup 514).
- Map every recurring customer (heat map by ZIP). Stop advertising to clusters under a set density until price covers the drive. Price remote stops separately rather than averaging them in.
- Monthly home-maintenance visits mean 12 drives for maybe 20 minutes of work; quarterly visits with a longer task list keep the revenue and cut the drives (operators report, r/sweatystartup 16).

## Price floors

```
required hourly rate = (owner target pay + all annual costs + taxes) / realistic billable hours
job price            >= max(minimum charge, (on-site hours + drive hours) x required hourly rate + materials x markup)
minimum charge       = price that makes a 30-minute job worth getting in the truck
```

- Operators report: $200 per working hour target with a $250 minimum (pressure washing, r/pressurewashing 2,164); $130 minimum rising to $150 for gutters and exterior (r/sweatystartup 200); $250 minimum even to inspect a roof (r/pressurewashing 581); $110 appliance service call covering diagnosis and the first 30 minutes (r/sweatystartup 254).
- A day target works for big jobs: $2,000 per day of 5 to 6 runtime hours means a 3 to 4 hour job quotes at $1,100 to $1,200 (r/pressurewashing 16).
- Labor scaling check: one commenter saw operators reach $50,000 a month in bookings while netting only 15 to 20% after paying techs, fuel and insurance (r/sweatystartup 18). Model tech pay as a percent of job revenue before scaling bookings.

## Negotiation tiers from margin

```
price at margin m = cost / (1 - m)
```

Worked (painter, r/sweatystartup 262): $2,000 labor and materials gives $4,000 at 50%, $3,636 at 45%, $3,333 at 40%. Quote the top, concede one tier only in exchange for booking today, walk at the floor. Choose the floor by how full the schedule is.

## Plans and memberships

```
plan price per month >= (visits per year x (on-site + drive time) x hourly rate + materials + vehicle margin) / 12
plan GP              = plan revenue - visit costs - discounts used on repairs - waived call-out fees
```

- Price from a timed trial visit plus drive time, then cut tasks if the price is too high; do not cut the rate (r/sweatystartup 16).
- Report plan gross margin apart from plan revenue. A plan that waives call-out fees and gives repair discounts can be revenue-positive and margin-negative.
- HVAC worked (operators report, r/smallbusiness 535): 300 agreements x $20 a month = $6,000 a month before service calls; members replace equipment at 3 to 4x the rate of cold leads. Building the base takes 2 to 3 years.

## Offline break-even

```
pieces needed per job = 1 / (response rate x close rate)
cost per job          = cost per piece x pieces needed per job
break-even response   = cost per piece / (close rate x first-job GP)
```

- EDDM postage is $0.260 a piece (USPS 2026); with print, budget about $0.40 to $0.70 delivered (one pest operator paid about $0.70 per address, r/pressurewashing 338).
- Worked: $0.50 per piece, 40% close, $250 first-job GP: break-even response = 0.50 / (0.4 x 250) = 0.5%. A 2,000-piece test costs $1,000 and needs 10 responses (4 jobs) to break even. Mail the same homes 3 to 4 times before judging.
- Door knocking: judge net earnings per door. 16,000 doors for $800 net is $0.05 a door (r/sweatystartup 188); a handyman who only knocks where he sees a specific fixable problem grossed $22,000 in two weeks (r/smallbusiness 1,419).

## Referral budget

```
max combined reward (both sides) = target CAC - other acquisition cost per customer
```

Worked (coreyhaines31/marketingskills, MIT): target CAC $200, other costs $40, so up to $160 combined ($80 each side). Weight rewards by distance to existing stops: next-door neighbor highest, same street next, across town none (operator idea, r/sweatystartup 445).

## Review math

Rating repair, catch-up velocity and prominence scoring live in `local-seo`. Home-service note: Jobber's top performers hold 4.5+ stars and 50+ reviews (vendor cohort, 2026); a new cleaner saw LSA calls start after 5 reviews (r/sweatystartup 25).
