# Apparel economics: formulas and worked examples

Numbers in the worked examples are illustrative inputs, not benchmarks. Replace them with the brand's own orders, quotes and payouts. General ecommerce formulas (MER, LTV, Etsy and TikTok Shop fee stacks, inventory cash) live in the `ecommerce-brand` skill, references/economics.md. This file keeps what is different about clothing: returns, sizes, MOQs, decoration methods, wholesale and markdowns.

## 1. Landed cost, not factory cost

```
landed COGS per unit = garment (or blank) + decoration + labels, tags, hangtags
                     + packaging + inbound freight + duty and tariff + inbound handling
                     + QC loss (defect rate x unit cost) + sample and tooling cost / units in run
```

Rules:
- A quote "per piece" from a factory or print shop is never landed cost. Ask what it includes (trims, labels, grading, packaging, freight) before comparing quotes.
- Spread sample, screen and pattern costs over the units actually sold, not the units ordered.
- Recompute landed cost every run. Freight, duties and blank prices move; one Reddit seller found a $4 product landing at over $10 after a tariff change (r/shopify, 147-pt thread).

## 2. Return-adjusted first-order contribution

Apparel loses money in returns before it loses it in ads. 56% of apparel returns are fit or size (Loop 2026) and 56% of apparel and footwear brands report 30%+ return rates (Radial 2025).

```
f = share of orders refunded            e = share of orders exchanged
u = share of returned units unsellable  L = return label + handling per return
S = outbound shipping per shipment      net = price after discount

contribution = net x (1 - f)
             - COGS x (1 - f + (f + e) x u)
             - pick/pack x (1 + e)
             - payment fees - marketplace fees - creator commission
             - shipping subsidy - e x S
             - (f + e) x L
```

Worked example, a $60 heavyweight tee sold DTC with free shipping:
- Net after an average 10% discount: $54. COGS $18, pick/pack $3, payment fees $1.92, shipping subsidy $6.
- Without returns: 54 - 18 - 3 - 1.92 - 6 = **$25.08**.
- With 10% refunds, 10% exchanges, 10% of returned units unsellable, $8 per return label and handling, $6 outbound on exchanges:
  - revenue 54 x 0.9 = 48.60
  - COGS 18 x (1 - 0.1 + 0.2 x 0.1) = 16.56
  - pick/pack 3 x 1.1 = 3.30; fees 1.92; shipping 6 + 0.6 = 6.60; labels 0.2 x 8 = 1.60
  - contribution = **$18.62**. Returns cost $6.46 an order, about a quarter of contribution.

Agent rule: never report contribution, CAC headroom or ROAS targets without the return line. Use the brand's own refund and exchange rates by SKU; if missing, use the last 90 days of return records, not a category average.

## 3. What CAC the brand can afford

```
break-even first-order CAC = return-adjusted contribution per first order
break-even ROAS            = platform-reported order value / contribution before ads
allowable CAC              = first-order contribution
                           + (measured 90-day repeat rate x contribution of a repeat order)
```

Worked example, continued: break-even ROAS = 54 / 18.62 = **2.9x**. The median apparel Meta ROAS is 2.24x (Triple Whale 2025 to 2026) and the fashion median 2.17x (MHI 2026). A one-tee order at median performance loses money on the first purchase.

Fixes, in order: raise AOV (second item, bundle, threshold), cut returns (fit information, exchange-first policy), raise price, lower landed cost. Count repeat only from measured cohorts. The fashion 90-day repeat median is 10.91% (Adtribute 2026), so with a $25 repeat contribution the repeat adds about $2.73, not a second full order.

## 4. Discount break-even: how many more units a discount must sell

```
required unit lift = gross margin / (gross margin - discount) - 1
```

| Gross margin | 15% off | 20% off | 30% off | 40% off |
|---|---|---|---|---|
| 60% | +33% units | +50% | +100% | +200% |
| 50% | +43% | +67% | +150% | +300% |

Shoppers expect about 40% off for a "good deal" on clothing at Black Friday (BCG France, 2025). At a 60% margin that needs three times the units to earn the same gross profit. Leading apparel brands concentrate depth at peak events (22.43% at Black Friday 2024) and run at 5.48% the rest of the year (Triple Whale 2025). Depth goes to events and to aged sizes, never to the hero.

## 5. Wholesale viability: the 4x check

Retailers need about 50% margin, so MSRP is about 2x wholesale (Faire 2026). If the brand also wants about 50% gross margin on its wholesale price:

```
max landed cost for wholesale = MSRP / 4
brand wholesale margin        = (wholesale price - landed - rep or platform commission) / wholesale price
```

| MSRP | Wholesale | Landed | Brand margin direct | After Faire 25% first order | After Faire 15% reorder |
|---|---|---|---|---|---|
| $60 | $30 | $15 | 50% | 25% | 35% |
| $60 | $30 | $24 | 20% | -5% | 5% |

The 25% column is Faire's first-order fee outside North America; in North America the opening order pays 15% plus a $10 new-customer fee (Faire North America pricing update 2026).

The $24 landed tee works at a 60% DTC margin but has no wholesale future. Decide wholesale before the run is cut, because landed cost is fixed at the factory. Retailers the brand recruits itself can be commission-free on Faire (Faire brand terms 2026), so send boutiques the brand's own Faire link.

## 6. Decoration method breakpoint

Screen printing has fixed costs (screens or setup per color and per location) and a low run cost. DTG, DTF and POD are flat per unit. Get both quotes on the same brief, then:

```
screen cost per unit = (screen and setup fees per color x colors x locations + other setup) / quantity
                     + print price per piece at that quantity
breakpoint quantity  = total screen setup / (flat per-unit price - screen print price per piece)
```

Below the breakpoint use DTG, DTF or POD; above it use screen print. More colors push the breakpoint up; one-color designs make screen print cheap early. Shops price differently by quantity bracket, garment and ink, so recompute per design; no public price list is reliable.

POD to inventory: test designs on POD, then move steady sellers to bulk. One operator compared an $8 to $10 wholesale Gildan heavy blend hoodie blank with about $40 landed through Printful after printing, shipping and tax, at only 10% to 15% profit per sale (r/printondemand, 43-pt thread). Another tested on Printful and Printify, killed every first-round design, and only bought stock from a local printer after consistent sales; 80% of their first-year $12k came in the last five months (r/printondemand, 32-pt thread).

Size upcharges: 4XL and 5XL cost about $5 more to print on POD (r/printondemand, 28-pt thread). Either price sizes separately (`size premium = extra unit cost / (1 - fee rate)`) or cap the flat-priced range at 3XL.

## 7. MOQ decision: the saving is real only if it sells

```
expected loss from a bigger run = (units ordered - units expected to sell at full price)
                                 x (landed cost - liquidation value per unit)
MOQ worth taking only if: unit saving x units expected to sell > expected loss
```

A factory that saves $3 a unit at a 1,000-piece MOQ saves $3,000 only if the units sell (research report, 2026). The cautionary case: 1,200 heavyweight hoodies at $80 retail, 456 sold, 744 left after price cuts, bigger discounts and free delivery (r/ClothingStartups, 27-pt thread). First orders of 25, 50 or 100 units per style limit the damage from a wrong sample, wrong measurements or a bulk run that differs from the sample (r/ClothingStartups, 41-pt thread).

Negotiate MOQ before paying more per unit: accepting the factory's standard packaging cut one quote from about 500 to about 200 units per product (r/ClothingStartups, 15-pt thread). UK factories run test-and-react orders in the 1 to 500 and 500 to 1,000 brackets (UKFT 2025).

## 8. Stock by size, not by style

```
days of cover (size)  = units on hand in that size / average daily sales of that size (last 28 days)
reorder point (size)  = daily sales of that size x (lead time days + buffer days)
size share            = units sold in size / units sold of the style (by drop, by channel)
```

- 100 units of XL do not cover zero M. Any paid or creator push must check days of cover on the two best-selling sizes, not total units.
- Lead time is the whole calendar: McKinsey measured an average 17 to 18 week production process (2026). With three weeks of stock and a three-month reorder, do not scale ads on that SKU without preorders or a local quick-turn supplier.
- Seed the first size curve from waitlist size choices, preorder sizes, or a POD test, not from a generic chart. Size demand differs by product and audience; no public benchmark is reliable.
- When a size sells out, keep the page live and capture size-specific back-in-stock signups.

## 9. Drop sizing

```
expected drop units = waitlist (opted in for this drop) x expected buy rate x units per order
size buy            = expected drop units x size share
```

Use the brand's own previous drop buy rate. Agency cases report 22% waitlist-to-buyer on an 8,400 list (Sphyx) and a 4,200 list with average 4-hour sellouts (beavaro); treat them as ceilings. A Journal of Retailing study (2025) found immediate sellouts of limited editions lower brand value and repurchase intention and recommends stocking to cover initial demand, so size the core sizes to sell through over days, not minutes. Only 20% of shoppers wait for a restock and 26% buy from a competitor (Podean 2025).

## 10. Markdowns and leftover sizes

```
markdown gross profit = units sold at markdown x (net markdown price - landed)
hold gross profit     = probability of selling at full price before next season x units x (full price - landed)
                        - carrying cost (storage, cash tied up)
```

Mark down by size and age: full price while size availability is healthy and sell-through is on plan; light promotion when aged sizes pass the owner's age threshold; deeper markdown only when replenishment is no longer rational (research report, 2026). Bundle scattered leftover sizes into a recurring event: one brand's first-Monday "Mystery Bundle" shipped 916 orders and 2,378 units in one day and recycled the cash into new drops (r/ClothingStartups, 23-pt thread).

## 11. Creator seeding cost

```
cost per seeded creator = product cost + shipping + fee + commission paid + usage rights fee
cost per usable asset   = total seeding cost / pieces of content cleared for paid use
creator value           = code or link contribution + assisted orders + (paid ad contribution from their footage)
```

Fashion campaigns ask for 2.7 content pieces per influencer on average and 81% of collaborations are repeat partnerships (Flowbox, Nov 2024 to Nov 2025). Judge creators as a portfolio over 60 to 90 days, not on last-click code revenue from one post.

## 12. Channel contribution after its own fee stack

Every channel gets its own contribution line per SKU. Fees to load (2026, verify in each seller center):
- Etsy: $0.20 listing, 6.5% on item plus shipping, processing, 15% or 12% Offsite Ads when charged.
- Amazon US apparel: 17% referral above $20 (5% at $15 or less, 10% over $15 to $20), plus FBA or self-ship costs and returns. A $35 tee pays $5.95 in referral alone.
- Depop: processing only in UK, US and AU, plus 12% on boosted sales of new UK and US listings.
- Faire: 25% first order outside North America (15% plus $10 in North America), 15% reorders, 0% on retailers the brand brings itself.

A channel stays only if its contribution per order after its fees and its return rate clears the owner's minimum. Revenue alone is not a reason to keep it.
