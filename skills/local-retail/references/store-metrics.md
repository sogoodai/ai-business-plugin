# Store metrics: formulas, counting and the weekly scorecard

The shop's money comes through one chain. Measure every link, then work on the weakest one.

```
passersby -> entries -> transactions -> sales -> identified customers -> repeat customers
```

## Counting the door

- **Best:** an overhead counter (infrared beam or camera). Many POS systems import counts. Exclude staff and children if the device allows.
- **Free:** a hand tally by hour for two weeks. Staff tap a clicker app at each entry group. Count groups, not people, if couples and families shop together: a couple buying once is one buying unit.
- **Passersby:** a staff member counts relevant passersby (people on your side of the street, walking past the window) for 15 minutes in each daypart on three days, then multiply to the hour. Rough is fine; you compare treatments, not absolute numbers.
- **Match dayparts.** Compare Tuesday 2 to 4 pm with Tuesday 2 to 4 pm. Weather, school holidays and events move traffic more than any window.

## Core formulas

```
attraction rate      = entries / passersby
conversion           = transactions / entries            (or buying units / groups)
ATV (avg transaction)= net sales / transactions
UPT (units per txn)  = units sold / transactions
AUR (avg unit retail)= net sales / units sold
ATV                  = UPT x AUR
sales per hour open  = net sales / opening hours
sales per labor hour = net sales / staff hours
attach rate (cat X)  = transactions containing an X companion / transactions containing X
identified rate      = transactions with a customer ID / transactions
regular rate         = identified customers with 4+ purchase days in 12 months / identified customers   (Square definition, 2026)
second-purchase rate = first-time identified buyers who buy again within 90 days / first-time identified buyers
gross margin %       = (net sales - cost of goods) / net sales
GMROI                = gross margin $ / average inventory at cost
sell-through %       = units sold / (opening units + units received)   (per period, per category)
weeks of supply      = units on hand / average weekly units sold
markdown %           = markdown $ / original retail $ of units sold
```

## Worked example: where is the money?

Gift shop, one week: 6,000 relevant passersby, 900 entries, 207 transactions, $9,315 net sales, 414 units.

- Attraction 900 / 6,000 = 15% (bottom of Flame's 15 to 35% range).
- Conversion 207 / 900 = 23%.
- ATV $9,315 / 207 = $45. UPT 414 / 207 = 2.0. AUR $22.50.

Three levers, each moved modestly:

| Change | New weekly sales | Gain |
|---|---|---|
| Attraction 15% to 18% (window test) | 1,080 entries x 23% x $45 = $11,178 | +$1,863 |
| Conversion 23% to 26% (staff at peaks, greeting) | 900 x 26% x $45 = $10,530 | +$1,215 |
| UPT 2.0 to 2.2 (attach lines) | 207 x 2.2 x $22.50 = $10,247 | +$932 |

Here the window is worth the most. In another shop it will be conversion. Compute, then decide. This is arithmetic on the shop's own numbers, not a benchmark.

## Discount break-even

```
required unit lift = d / (m - d)        d = discount as fraction of price, m = gross margin before discount
```

| Margin before discount | 10% off | 20% off | 30% off |
|---|---|---|---|
| 40% | +33% units | +100% | +300% |
| 50% | +25% | +66.7% | +150% |
| 60% | +20% | +50% | +100% |

Before any sale, show the owner this row. Incremental labor and ad spend come on top. A gift with purchase that costs $3 at cost on a $60 threshold is 5% of price, not 20%.

## Event lift

```
baseline        = average sales of the same weekday and hours over the prior 4 comparable weeks (exclude holidays)
event lift      = event sales - baseline
event margin    = event lift x gross margin % - event costs (partner fee, food, staff overtime, print)
new identified  = new customer records tagged to the event code
90-day value    = later purchases by event-tagged new customers within 90 days x gross margin %
```

An event is worth repeating when event margin + 90-day value > 0 and new identified buyers clear the target set before the event.

## Partner attribution

Give each partner their own link with UTM tags, QR code or spoken code ("say BAKERY at the till"). Tag new customer records with the code. Rank partners by new identified buyers and their 90-day value, not by RSVPs.

## Inventory health for marketing

- **Dead stock:** units older than 180 days with no sale. Move them with bundles, a window of "last ones", a wholesale lot or a marketplace, before they absorb the best shelf.
- **Hero stock:** the 20 to 40 SKUs with the highest gross profit and steady sell-through. These get the window, Google inventory, social and paid budget.
- **Out-of-stock on heroes** kills conversion silently. Track a weekly in-stock rate on the hero list.
- **One-of-a-kind stock** (antiques, vintage, art): sell-through per category per month and days to sell. Price by sold comparables in matching condition, not by the highest sale ever recorded (r/Flipping, 1,114 points: a $3,000 ask became $50 after sold comps showed $8 to $12 per album).

## Weekly scorecard (one screen for the owner)

| Line | This week | Same week last year | 4-week average |
|---|---|---|---|
| Entries | | | |
| Attraction rate | | | |
| Conversion | | | |
| ATV / UPT / AUR | | | |
| Net sales / gross margin $ | | | |
| Identified rate | | | |
| New identified customers | | | |
| Second purchases from last month's new customers | | | |
| Email/SMS flow orders / campaign orders | | | |
| Google: calls, directions, website clicks; reviews this week | | | |
| Online orders, fulfilled on time %, inventory mismatches | | | |
| Hero SKU in-stock rate | | | |

At day 90 the agent should answer five questions with numbers: where do new customers discover the shop, what share of passersby enter, what share of entrants buy, what share of buyers become identifiable, what share come back (research synthesis, 2026).

## Tricks

- **Split conversion by staffed vs understaffed hours.** A "quiet" hour by transactions may be a busy hour where people walked out unserved (RetailNext case logic).
- **Measure a broken zone, not the store.** Fitting-room-to-sale, counter-engagement-to-sale and category attach rate find the one place that leaks.
- **Credit the store for online saves.** If staff place a web order for a missing size, attribute it to the store so staff keep doing it.
- **The best-day diagnostic** (r/smallbusiness, 399 points): pull the best day of the last 90 and name its cause before buying any marketing. Repeat the cause.
