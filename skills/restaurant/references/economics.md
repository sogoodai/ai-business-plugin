# Economics: formulas and worked examples

Every marketing decision here answers to contribution, the money left after the variable costs of that sale. Compute these before recommending spend. Label every assumption you had to make.

## 1. Prime cost and the P&L lines

```
food cost % = (opening inventory + purchases - closing inventory) / food sales
beverage cost % = same, on beverage sales (track beer, wine, spirits, non-alc separately)
labor % = (wages + salaries + payroll taxes + benefits + contract labor) / net sales
prime cost % = (food + beverage cost + total labor) / net sales
occupancy % = (rent + CAM + property tax + insurance on premises) / net sales
```

- Invoices alone are not food cost. Without inventory counts, a month with a big stock-up looks terrible and the next one looks great. Ask how it is measured before you compare.
- Compare with the format's NRA medians and the profitable cohort ([benchmarks.md](benchmarks.md)): full-service prime cost about 68.5% median, labor 34.2% in profitable operators vs 42.9% in loss-making ones (2024 data, pub. 2025).
- Small operators carry worse food cost: 33.7% under $2M sales vs 31.0% above (NRA 2025). Scale buys purchasing power; a small place wins on menu focus and waste, not on haggling.

**Trick:** count the owner's own hours and family labor at a market wage. A family truck sold $1,600 against about $1,300 of costs; the $300 left paid 70 to 80 combined hours, about $3.75 to $4.29 an hour (operators report). They closed.

## 2. Channel contribution waterfall

```
contribution = net sales
  - discounts and comps - refunds
  - marketplace commission and in-app marketing fees
  - card or ordering fees
  - food and packaging
  - incremental hourly labor
  - delivery subsidy
```

**Worked example, $40 order** (DoorDash Nov 2026 fees, NRA limited-service food cost 32.4%):

| Line | Marketplace, 30% plan | Marketplace, 15% plan | Direct (Square 2.9% + $0.30) |
|---|---|---|---|
| Commission or processing | -$12.00 | -$6.00 | -$1.46 |
| Food | -$12.96 | -$12.96 | -$12.96 |
| Left before packaging and labor | $15.04 | $21.04 | $25.58 |
| Share of a direct order's value | 59% | 82% | 100% |

A marketplace order is worth 59 to 82% of a direct one before packaging. "20% delivery growth" can lower profit if it is existing direct guests migrating to the app.

**In-app promotions:** compute promo ROAS after commission. One operator saw "2.13 ROAS" on Uber Eats ads plus promos, but the figure ignored the 20% commission and fees; they ended up owing Uber money (operators report). Contribution per promo order = order value x (1 - commission - food% - packaging%) - promo cost - ad cost.

## 3. Markup and break-even formulas

```
app price that keeps proceeds equal = in-store price / (1 - commission)
  15% -> x1.176   20% -> x1.25   25% -> x1.333   30% -> x1.429
proceeds per app order = app price x (1 - commission); compare with the in-store price
contribution after commission = proceeds - food - packaging - incremental labor
direct software break-even (monthly volume) = fixed monthly fee / (commission avoided - processing %)
  $499 / (0.25 - 0.03) = $2,268 of shifted orders a month
```

Operators report: a 10% app markup on a 25% plan took one restaurant's margin from 40% to 15%; another set app prices so proceeds after 25% matched its cash price, with a 4% cash discount at the counter. Check the platform's terms first: DoorDash's 6% pickup rate requires pickup price parity, Uber's 7% pickup rate requires validated in-store pricing, and DoorDash emailed at least one restaurant about higher platform pricing.

## 4. Dine-in capacity

```
RevPASH = revenue in a daypart / (available seats x hours in that daypart)
covers needed to break even (month) = fixed costs / (average check x contribution margin %)
seat displacement cost = covers lost on a peak hour x average check x contribution %
```

- **Turn time:** Toast measures check open to paid, not literal seat occupancy, so do not compare it with "table turns" from other sources ([Toast support](https://support.toasttab.com/en/article/How-is-turn-time-calculated)).
- **Long-stay regulars:** weigh their weekly spend against the Friday and Saturday business their table displaces. One commenter suggested a reliable $30 to $50 spend a visit to justify extended stays and a stated peak-night limit (operators report).
- **Closing time sets the last hour:** moving close from 9 pm to 10 pm doubled 8 to 9 pm traffic in one restaurant, because guests avoid arriving within an hour of close (operators report). Model the extra hour's labor against that.
- **Open fewer, better hours** when an extra shift cannot cover its labor. Several owners run 4 to 5 days, dinner only (operators report).

## 5. Guest value and acquisition

```
contribution per visit = average check x contribution margin % (after variable costs)
regular value per year = contribution per visit x visits per year
new-guest CAC = channel spend / first-time purchasing guests attributed to that channel
payback visits = CAC / contribution per visit
incremental lift = (visits per guest, treated) - (visits per guest, holdout)   (same period, 10 to 15% holdout)
regular attrition plan: new regulars needed = attrition rate + growth target   (operator: 20% + 5% = 25% a year)
```

**Worked example, regular:** $55 a visit, three visits a week = $8,580 a year in sales (operators report). At 60% contribution that is about $5,150 a year from one guest, more than most monthly ad budgets. A server complaining "he never tips" within earshot cost exactly that.

**Worked example, creator:** fee $500. Average party of 2 spends $60; contribution after food and variable labor 55% = $33. A 25% second-visit rate adds about $8. Value per new party about $41, so the post must bring about 12 new parties you can match to a code or link. If the creator's audience is not local, it cannot.

**Worked example, catering vs walk-in CAC:** never pool them. A $10 private-event inquiry that books a $3,000 party and a $10 reservation for two are different jobs; give each its own conversion event and target.

## 6. Price-change break-even

```
volume you can lose before contribution falls = p / (m + p)
  p = price increase as a fraction, m = current contribution margin as a fraction
```

A 5% raise on an item with 60% contribution survives losing 5 / 65 = 7.7% of its units. The aggregate restaurant elasticity of about -0.76 (SSRN 2026) implies a 5% raise loses about 3.8% of spending on average, inside that limit, but a single item with close substitutes on the same menu can lose far more. Watch units and mix, not just average check.

## 7. Food truck and stand math

```
expected buyers = attendees x purchase rate / comparable food vendors
  purchase rate: 30% (500 attendees -> 150 buyers) to 50-60% (commenter estimates); use the lower without history
expected sales = expected buyers x average ticket
event cost = pitch fee + % of sales fee + event health permit + travel + all labor (prep, travel, service, cleanup) + expected waste
event floor (sales needed) = fixed event cost / contribution margin %
sales per service hour = sales / hours actually serving
labor % per hour = hourly labor / sales per hour
```

- Fees operators report: $200 to $500 flat or about 15% of sales, sometimes both, plus a $200 to $300 single-event health permit; some fairs charge $1,000+ a day and need your own cold storage; local festival fees of 25 to 30% of sales.
- A $1,500 two-day fee needs about $4,500 in sales to break even (implies about 33% contribution). Lollapalooza: $25,000 buy-in, $125,000 sales, $25,000 profit (20%).
- Meal windows, not posted hours: lunch 11 am to 2 pm and dinner 5 to 8 pm sell entrees; 2 to 5 pm is weak. A 12-hour event day may have 6 selling hours.
- Floors operators use: 20 to 30 customers an hour at $15 ($300 to $450 an hour); "$400 to move the truck and generator plus $100 for every hour open, plus $20 an hour per extra staff"; no paid pitch under $1,500 projected; $700 minimum.
- Labor efficiency: two workers at $30 an hour on $1,000 an hour of sales is 6% labor; one at $30 on $300 is 10%.
- Opportunity cost: an event that pulls you off a regular spot doing a couple of thousand dollars in two hours must beat it. One operator lost $180 at a "huge line" free event.

## 8. Bakery and production-constrained math

```
contribution per oven hour = (price - ingredients - packaging) x units per batch / oven hours per batch
contribution per labor hour = same numerator / labor hours per batch (include shaping, proofing handling, packing)
wholesale contribution = wholesale price x units - ingredients - packaging - delivery cost - returns or stales
preorder share = preordered units / units baked; waste % = unsold units / units baked
```

Rank products by contribution per scarce hour, not by gross margin %. A lower-margin wholesale loaf that batches efficiently can beat a high-margin custom cake that eats decorating labor (research synthesis 2026, see [sources.md](sources.md)). A bakery selling pizza dough, ethnic breads and bulk pastry dough to pizzerias, grocers, nursing homes and county jails reached almost 20% profit on $4M sales (bakery plus kitchen, operators report).

**Seasonality check before cutting anything** (gift and treat shops): daily rent + labor + utilities vs average daily sales, and the share of annual revenue earned in November to January. One commenter's illustration: $180 daily costs vs $150 daily sales, 60%+ of revenue in Q4. If the storefront earns its year in the season, bridge summer with preorders or one wholesale account that covers rent rather than slashing staff and ads (operators report).

## 9. What to report

Each month: prime cost %, contribution per order by channel, direct vs marketplace share, first-to-second visit rate at 30, 60 and 90 days (format-dependent), visits per identified guest, loyalty 90-day active rate, review count and rating with last-90-day velocity, event and catering contribution, CAC per new purchasing guest by channel. Never impressions, opens or followers as top-line KPIs when transaction data exists.
