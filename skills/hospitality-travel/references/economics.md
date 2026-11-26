# Economics: formulas with worked examples

Compute these before recommending anything. Numbers in examples are illustrative unless a source is named. Sources in [sources.md](sources.md).

## 1. Airbnb repricing for the host-only fee

Airbnb moved most home hosts to a 15.5% host-only fee in 2026 (PMS-connected hosts not already on it switched on 13 October 2026). Airbnb's own example: a $100 nightly rate paid $97 under the old split fee and pays $84.50 under 15.5%.

```
new listed rate to keep payout = old payout / (1 - 0.155)
$97 / 0.845 = $114.79  -> list at $115
```

Under the split model the guest also paid a separate service fee on top. Under host-only, the listed price is what the guest pays before taxes. So a raise to $115 mostly moves the old guest fee into the price; the guest total barely changes. Check: compare your guest total for five date patterns (midweek near-term, weekend near-term, weekend 30 to 60 days out, event date, peak season) against 10 to 20 true comparables. Airbnb ranks on total price relative to local comps.

Apply the same factor to the cleaning fee and extra-guest fees: the 15.5% is taken on those too.

## 2. Channel net payout, per typical stay

Build one line per channel for the property's most common stay (for example 3 nights, 4 guests).

```
net payout = guest-paid rent + host fees - platform commission - payment processing - taxes remitted
```

Example, 3 nights at $180, $120 cleaning:

| Channel | Gross to host side | Platform take | Net |
|---|---|---|---|
| Airbnb host-only 15.5% | $660 | $102.30 | $557.70 |
| Vrbo pay-per-booking at 12% (standard model per research pass) | $660 | $79.20 | $580.80 |
| Booking.com at a contract rate of 18% (illustrative; read the Extranet contract) | $660 | $118.80 | $541.20 |
| Direct via booking engine, 3% card fee | $660 | $19.80 | $640.20 |

Then adjust for cancellation: Cloudbeds 2025 hotel data shows OTA cancellations at 21.8% vs 10.6% direct. Booking.com ranks on net bookings after cancellations, so a refundable promotion that inflates gross bookings can hurt rank.

## 3. RevPAR beats occupancy

```
RevPAR = revenue / available nights = ADR x occupancy
```

| Calendar | Occupancy | ADR | RevPAR |
|---|---|---|---|
| A, discounted gaps filled | 90% | $140 | $126 |
| B, held rate, some gaps | 75% | $180 | $135 |

B wins and also has fewer turnovers. Add turnover cost to see the real gap:

```
net RevPAR = (revenue - channel fees - cleaning cost not recovered) / available nights
```

PriceLabs (2026) explicitly advises judging gap filling on RevPAR, unbookable-night count and length-of-stay mix, not occupancy.

## 4. Fee load and the cleaning-fee decision

```
fee load = (cleaning fee + mandatory extra fees) / guest total for the most common stay
```

Example: 2 nights at $140, $190 cleaning, $85 service fee: total $555, fee load 50%. That is the r/vrbo guest who "closed the tab entirely" (210 upvotes). Working rule (not a benchmark): flag when the cleaning fee is more than one night's rate on a two-night stay.

Options:

- **Fold into rate:** cost per stay / typical nights added to each night. Good for 1 to 3-night markets. A $45 room with a $4 fee should just be $49 (43-upvote advice).
- **Low fixed fee per booking:** good for long stays, because a nightly increase overcharges 2-week guests (a host charges $10 flat from 1 night to 3 months).
- **Drop it and absorb:** only if margin allows. The cabin case: $200+ fee removed, then every weekend booked for six weeks (r/AirBnB 218, 2024, uncontrolled; owner had no mortgage).

## 5. Minimum stay break-even

Every stay carries fixed costs: cleaning labor, laundry, consumables, restock run, wear, guest-message time.

```
fixed cost per stay F, nightly contribution c (rate minus per-night variable cost)
a k-night stay contributes k x c - F (+ cleaning fee collected)
minimum stay where profit per stay >= target T:  k >= (T + F - cleaning fee) / c
```

Example: F = $110, cleaning fee $60, c = $95, T = $150: k >= (150 + 110 - 60) / 95 = 2.1, so a 3-night minimum. If the same host collects a $150 fee: k >= 1.2, so 2 nights works.

Two operators show both ends are rational:

- 3-night maximum, 4 houses, about 95% occupancy, one-night stays the core business, $50 fee ($25 per bed) collected per stay, host cleans: more fees, more profit (r/airbnb_hosts 434).
- 25-night minimum, also listed on 2 mid-term platforms, fully booked, higher payout after fewer turnovers, stolen linens and supply runs (r/airbnb_hosts 288).

Pick from the owner's cost structure and labor, not from a rule of thumb.

## 6. Orphan nights and gap pricing

```
orphan nights (next 60 days) = sum of open gaps shorter than the minimum stay that applies to them
lost revenue = orphan nights x expected gap rate
```

Fix with gap-length minimums (a 2-night gap gets a 2-night minimum), check-in and check-out day rules, and adjacent-day rules that stop a new booking from creating a one-night remainder (PriceLabs 2026). Price the gap nights, not the whole week. Screen gap requests from locals (see [pricing-and-stays.md](pricing-and-stays.md)).

## 7. Extra-guest pricing for big homes

A 6 to 8-sleeper in a market with few big groups: set the base for 2 to 3 guests and add a per-guest fee above that (r/airbnb_hosts 589). Check the quote from search with 6 guests: if the total jumps at checkout, conversion and reviews suffer (r/vrbo, $25 per guest surcharge, 8 upvotes, in a 3,071-upvote thread).

## 8. Repeat and direct value

```
commission saved per converted guest = commission rate x average booking x expected future stays
max acceptable direct incentive        = commission saved on the next stay - card fees
```

Example: 15.5% x $900 x 1.5 expected stays = $209. A $50 welcome credit or free late checkout on the next direct stay is easily paid for.

## 9. Tours: contribution after commission

```
contribution per booking = price x (1 - commission) - guide cost per head - variable cost per head
departure contribution    = sum of bookings' contribution - fixed cost per departure (guide minimum, vehicle, permits)
break-even pax per departure = fixed cost per departure / contribution per head
```

Viator Accelerate (commission-funded ads):

```
incremental contribution = incremental bookings x (price x (1 - new commission) - variable)
                           - organic bookings x price x (new commission - old commission)
```

Run it on a subset of products or dates and compare to the rest (research pass 2026). Viator says even a 1-point commission increase can lift exposure, but booking recency and review credibility still weigh.

GetYourGuide launch offer (20% for 30 days): treat as acquisition cost.

```
launch cost = bookings during launch x price x 0.20
cost per review = launch cost / reviews gained
```

Accept if the cost per review is below what the product earns from the lift that 3+ reviews bring (platform research: 3 reviews = 3x booking likelihood vs 0).

## 10. Advisor economics

```
annual net = gross supplier commission x split - host annual fee - transaction and tech fees + planning fees
```

Compare host agencies on net, not split. Example on $60,000 gross commission:

| Host | Split | Fees | Net |
|---|---|---|---|
| A | 90/10 | $1,800 tech + $150 a month | $50,400 |
| B | 80/20 | $500 annual | $47,500 |

A wins here, but if B's supplier rates add 1 point of commission across $600,000 in sales, B adds $6,000 x 0.8 = $4,800 and ends at $52,300, ahead of A. Model it with the owner's mix (research pass 2026; host averages 80% split, about $500 fee, Travel Market Report 2025).

Quoting time value:

```
cost of an unpaid quote = hours x owner's target hourly rate
quote-to-book rate needed without fee = cost of quote / commission per booking
```

If a quote takes 4 hours at $50 and commission is $400, you need 50%+ close on quotes to break even on time. That is why fees or deposits before research work (r/travelagents, 56 and 68 upvotes).

## 11. Paid leads test (advisors, tours)

```
break-even bookings = lead spend / commission or contribution per booking
```

Example from r/travelagents (44): 50 leads for $1,575; two bookings broke even. Run one small batch, track replies and bookings for 60 days, buy volume only if the batch beats break-even. Demand the originating ad and exact inquiry; the buyer of those leads could not tell prospects which Facebook offer they had seen.

## 12. Refund-if-rebooked math

When a guest leaves early or cancels outside policy:

```
refund = nights rebooked by a completed, paid replacement stay x original nightly rate (minus taxes and fees already paid out)
```

Pay after the replacement stay completes, and only at equal or higher value (r/airbnb_hosts 1,005 thread, 6 and 3-upvote safeguards). Never refund the whole stay to prevent a review; one host did and still got 2 stars (r/airbnb_hosts 905).
