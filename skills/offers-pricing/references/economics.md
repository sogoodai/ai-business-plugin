# Pricing economics: every formula, with worked examples

Compute these before recommending any price, discount, bundle or plan. Use the owner's real numbers; when a number is missing, say which one and use a labeled assumption. Sources for cited numbers: [sources.md](sources.md).

## 1. Contribution margin: the number every decision runs on

```
contribution per unit = price
                        - cost of goods or materials
                        - direct labor paid per job or per hour of the job
                        - card or processor fee (all-in effective rate, not the headline)
                        - marketplace or platform fee
                        - shipping and packaging you pay
                        - discount, coupon, free item, free shipping
                        - expected refunds, redos and chargebacks per unit
contribution margin (m) = contribution per unit / price
```

- Fixed costs (rent, software, owner salary, insurance) do not belong in m. They belong in the break-even volume.
- Owner-operators who do the work themselves: include their own hours at a target wage, or the "margin" is just unpaid labor.
- Processor fees: get the effective rate from 3 months of statements (total fees / total volume). A gym owner was pitched about 5% of gross and paid close to 10% once all contract fees landed (r/smallbusiness, 1,353 upvotes, top comment 1,089 agreed it was unaffordable).

Worked example, mobile detailer, full detail at $250: products $18, card fee 3% = $7.50, travel fuel $8, 4 hours of a $25/h helper = $100. Contribution $116.50, m = 47%.

## 2. Break-even volume for a price change

The single most useful pricing formula. With contribution margin m before the change:

```
price RISE of p:   you can lose up to   p / (m + p)   of units before contribution falls
price CUT  of d:   you must GAIN at least   d / (m - d)   more units just to stand still
```

| Margin m | +5% price: max unit loss | +10% | +20% | +40% | -10% price: units needed | -15% | -20% | -30% |
|---|---|---|---|---|---|---|---|---|
| 20% | 20% | 33% | 50% | 67% | +100% | +300% | impossible | impossible |
| 30% | 14% | 25% | 40% | 57% | +50% | +100% | +200% | impossible |
| 40% | 11% | 20% | 33% | 50% | +33% | +60% | +100% | +300% |
| 50% | 9% | 17% | 29% | 44% | +25% | +43% | +67% | +150% |
| 60% | 8% | 14% | 25% | 40% | +20% | +33% | +50% | +100% |
| 70% | 7% | 13% | 22% | 36% | +17% | +27% | +40% | +75% |

How to read it:

- Low-margin businesses (restaurants, resellers, dropshippers) are the most sensitive to discounts and the most rewarded by small increases. At 30% margin a 10% raise survives losing a quarter of customers; a 20% discount needs triple the volume.
- A former niche retailer at about 40% gross margin facing online rivals at 20% off MSRP: matching halves gross profit per unit, so twice the units are needed before any extra overhead (r/smallbusiness, operator report).
- Lost customers also free capacity. For a full service business, a raise that loses 10% of clients is a raise plus 10% more time to sell or rest.

Worked example, the 40% raise (r/smallbusiness, 1,239 upvotes): a social media manager raised 22 clients by 40% with three months' notice. Seven left, 15 stayed, monthly revenue rose about 12% and work fell about 35%. At a service margin near 60%, the formula said up to 40% could leave; 32% did.

## 3. Conversion versus profit per visitor or lead

```
revenue per visitor = conversion rate x average order value
profit per visitor  = conversion rate x contribution per order
profit per lead (services) = close rate x contribution per job
```

- A 10% price cut that lifts conversion 10% gives 0.9 x 1.1 = 0.99: revenue per visitor falls 1% and profit falls more (Stripe pricing review framework, 2025, recommends judging revenue, volume, margin, conversion and churn together).
- Card-required trials convert 30% versus 8% median for all free-to-paid models (ChartMogul, 2026, survey of 200 products, observational). Judge trial design on paid customers per visitor, never trial-to-paid alone.
- A higher price that loses 12% of jobs can still win: an importer marked up import duties, lost 12% of win rate and doubled average value and profit on that work (r/smallbusiness, operator report).

## 4. Service price floors

### Required hourly rate

```
billable hours per year = working weeks x hours per week x billable share
required hourly rate = (owner pay target + all overhead + profit target + taxes) / billable hours
```

- Billable share for solo field and appointment businesses is rarely above 60 to 70% once travel, quoting, admin, marketing and cleanup are counted. Use 50% until the owner's calendar proves otherwise.
- Example: $60,000 owner pay + $18,000 overhead + $10,000 profit = $88,000. 46 weeks x 40 h x 55% = 1,012 billable hours. Floor: $87 per billable hour.
- Pressure washers in one thread argued $100 per hour as the floor once travel and equipment are counted (76 upvotes); one operator targets $200 per working hour with a $250 minimum (21 upvotes).

### Job price built from cost

```
job price = labor hours x loaded hourly rate
          + materials x (1 + materials markup)
          + travel and setup time x loaded rate
          + disposal, rentals, permits, parking
          + risk allowance (callbacks, warranty, unknowns)
```

- Commercial HVAC replacement planned at a healthy margin cleared 8% after a warranty callback, unpriced refrigerant, underestimated drive time and a forgotten one-day equipment rental (r/sweatystartup, operator report). Put each of those on the estimate template as a line.
- Test-clean, test-cut or test-run one unit before quoting anything large and unfamiliar. A storage-door oxidation job tested at almost $600 of chemical alone and two applications per door; the operator quoted $4,400 and lost to bids of $1,500 and $900. Losing that job was the right outcome.
- Fixed job prices beat hourly for the customer and usually for the operator; keep hourly internally to build the quote.

### Minimum charge

```
minimum charge >= (round-trip travel time + setup + teardown + 30 to 60 min of work) x loaded rate + fixed trip costs
```

Operator minimums reported: $250 per visit even for an inspection-only roof visit; $130 rising to $150 per property for a solo exterior cleaner targeting $100 per field hour; £80 for carpet cleaning; $110 appliance service call covering the first 30 minutes on site (all r/sweatystartup and r/pressurewashing, operator reports). A $1,500 minimum for holiday lighting installs, stated on the first call, filtered estimates to qualified prospects.

## 5. Product price from landed cost

```
landed cost = unit cost + inbound freight + duties and tariffs + inspection + packaging + inserts
contribution per order = price - landed cost - fulfillment - outbound shipping you pay
                         - payment fee - marketplace fee - ad cost per order - returns allowance
markup = (price - cost) / cost        margin = (price - cost) / price = markup / (1 + markup)
```

| Multiplier on landed cost | Gross margin | Typical use |
|---|---|---|
| 1.5x | 33% | Commodity resale, high volume, no ads |
| 2x (keystone) | 50% | Wholesale to retail step |
| 3x | 67% | Retail floor for DTC that buys traffic |
| 4 to 5x | 75 to 80% | DTC with paid acquisition, returns and free shipping |

- A DTC seller who pays for ads needs room for ad cost per order on top of fulfillment. A $10 unit against $16 to $25 competitors leaves no room; a $15 unit sold at $90 funds ads and selective discounts on slow colors (r/FulfillmentByAmazon, operator report).
- Cost increases (tariffs, wholesale flowers, freight): decide between passing through the dollars (keeps profit per unit, margin percentage falls) and re-applying the multiplier (keeps margin percentage, bigger price jump). Pass-through is the safer default for elastic products; re-apply the multiplier when the old price was already too low.
- A florist at 10% margin could not adjust weddings already under contract when wholesale prices rose. For long-lead bookings, add a materials-cost clause or a price valid-until date to every quote.

## 6. Discounts, coupons and free items

```
true cost of a promotion = discount given to customers who would have bought anyway
                         + margin lost on incremental buyers
                         - contribution from genuinely incremental units
incremental units needed = d / (m - d) x baseline units (see table above)
```

- A flat-dollar coupon must be checked against the cheapest item. A $5 abandoned-cart coupon created when everything cost over $30 later turned a $6 item into a $1 order (r/Etsy, operator report). Set a minimum order on every flat coupon.
- Free giveaways attract the wrong buyers. A dealer's free oil change day drew people bringing several cars past the one-per-customer limit and demanding more freebies (operator report). A 50%-off first clean and a 4-free-hours flyer produced 2 leads from 100 flyers and both ghosted at the quote (r/sweatystartup).
- Show the discount as a separate line with its reason so the full price stays the reference (r/smallbusiness, 50 upvotes plus two independent agreements).

## 7. Order expansion: bumps, add-ons, upsells

```
add-on contribution per base order = attach rate x add-on contribution
order-value lift = attach rate x add-on price / base order value
```

- Benchmarks: optional quote line items accepted 25 to 50% of the time in home services (Jobber, 2026, platform data, vendor). Post-purchase upsell take rate median 21.6%, top quartile 30%; session value lift median 18%, top quartile 33% (Funnelish, 2026, 553 US funnels, direct-response skew).
- Track attach rate by base product, not store-wide. If half of one service's buyers take an add-on, make it a default option on that quote.
- Free-shipping threshold: set it one typical add-on above the median order, then check that the add-on's contribution exceeds the shipping you now pay.

## 8. Recurring revenue

```
monthly churn c = customers lost in month / customers at start of month
expected lifetime (months) = 1 / c
lifetime contribution = monthly contribution / c
paid months in the first year on monthly billing = (1 - (1 - c)^12) / c
break-even annual prepay discount = 1 - paid months in first year / 12
```

| Monthly churn | Paid months in year 1 | Annual discount that breaks even |
|---|---|---|
| 2% | 10.8 | 10% |
| 3.2% (SaaS average, Recurly 2026) | 10.1 | 16% |
| 4.25% (ecommerce subscriptions, Recurly 2026) | 9.6 | 20% |
| 5% | 9.2 | 23% |
| 8% | 7.9 | 34% |

- The median published annual discount in software is 20%, interquartile range 17 to 26% (CostBench, July 2026). That is close to break-even for typical churn, so annual prepay is mainly a cash-flow and commitment tool, not free money.
- Annual buyers self-select: they were less likely to churn anyway. The real gain is smaller than the table says. Offer 2 months free (17%) as the default and only go deeper when cash is the constraint.
- Annual plans still fail on cards: a gym found about 23% of discounted annual members stopped paying within months because their cards would not process (r/smallbusiness, 1,353 upvotes). Card updater, retries and a dunning window are part of the price design.

### Membership math

```
member contribution per month = fee - (expected redemptions x cost per redemption) - card fees
capacity check = members x expected visits per month <= off-peak sellable slots
```

- Price the membership from expected use, not from "unlimited". If peak capacity cannot serve members, sell pay-as-you-go instead: a 9-court facility deliberately avoids memberships so members are not paying for courts they cannot book (r/smallbusiness, 44 upvotes).
- Small group training: set the session price so one occupied spot of four covers labor and costs (gym owner, 50 upvotes).

## 9. Payment plans and BNPL

```
BNPL net gain = incremental orders x contribution
              + average-order-value lift on BNPL orders x margin
              - (BNPL fee - card fee) x all BNPL volume, including orders that would have paid by card
              - extra refunds and disputes
```

- Stripe's randomized test across 150,000+ sessions found up to 14% revenue lift from showing one BNPL method, with more than two-thirds of BNPL volume incremental (June 2024, vendor). Stripe/Affirm report +21% relative conversion on orders above $250 (vendor).
- BNPL merchant fees run several points above card fees; read the processor's current rate card rather than assuming.
- On Shopify, native post-purchase offers do not show for buyers paying with Klarna, Affirm, Afterpay or several wallets (Shopify docs, 2026). Adding BNPL can lower post-purchase upsell exposure. Net the two.

## 10. Guarantees

```
expected guarantee cost = claim rate x (refund amount - recoverable value) + handling cost
guarantee pays when: conversion lift x contribution per order > expected guarantee cost per order
break-even claim rate = conversion lift x contribution / (refund amount - recoverable value)
```

Example: $200 offer, $120 contribution, guarantee lifts conversion from 2.0% to 2.4% (+20%). Per 1,000 visitors that is 4 extra orders, $480 more contribution, on 24 orders. If nothing is recoverable, claims cost 24 x claim rate x $200, so the guarantee breaks even at a 10% claim rate. Specific, conditional guarantees usually run well below that; an unconditional "love it or your money back" on a consumable can exceed it. For services, a redo guarantee costs labor and materials, not the full price, which moves break-even much higher.

## 11. Deposits and prepayment

```
no-show leak = no-shows per month x average ticket
deposit recovers = no-show leak x share that now shows or forfeits
```

- Operators in beauty report near-zero cancellations with a 50% non-refundable deposit; vendors suggest 20 to 50% (see the beauty-business skill). Custom made-to-order goods above a few hundred dollars: collect payment in full or a deposit that covers materials before starting.
- Wholesale and B2B: prepaid trial orders before net terms. A candle maker declined an order that would have tripled monthly revenue because it came with custom labels, net 60 and returns of unsold goods within 30 days; the prepaid smaller trial was refused, which revealed the risk (r/smallbusiness, 925 upvotes).

## 12. Negotiation floors for quoted work

Set three acceptable margins before quoting and start at the top. A painting contractor uses 50%, 47% and 42% target margins: hold 50% when the schedule is full, drop toward 42% only to fill an unsold slot (r/sweatystartup, 222 and 262 upvotes; operator credits the full sales process with over $2 million sold). Any price reduction must remove scope. A pest-control rep who cut the price two or three times for the same work made the buyer distrust the first quote.
