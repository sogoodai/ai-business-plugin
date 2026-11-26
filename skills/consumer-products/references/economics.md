# CPG economics

Every channel decision starts from contribution dollars per unit in that channel. Build the model SKU by SKU and channel by channel; a "50% margin" that compares factory cost to wholesale revenue says nothing about what the brand keeps.

Worked examples marked "illustrative" use assumed terms. Replace each assumption with the owner's real invoices and the buyer's real terms before advising.

## Formulas

```
landed COGS / unit      = ex-factory unit cost + primary and secondary packaging + freight in / unit
                          + duty / unit + QA and lab testing allocation + co-packer setup / run units
                          + warehouse receiving allocation
gross margin %          = (net revenue - landed COGS) / net revenue
contribution / unit     = net realized revenue - landed COGS - freight out - variable fees
                          - commissions - variable trade spend
contribution / order    = net revenue - landed COGS - pick and pack - outbound shipping not paid by buyer
                          - payment and marketplace fees - refunds - creator commission
velocity (UPSPW)        = units sold / active stores / selling weeks
dollar velocity (SPPW)  = dollars sold / active stores / selling weeks
annual contribution / door = UPSPW x 52 x contribution per unit
launch break-even units = fixed launch costs / contribution per unit
DTC max first-order CAC = first-order contribution - required first-order profit
allowable CAC (payback) = cumulative contribution per customer inside the permitted payback window
reorder rate            = buyers with a 2nd purchase in the window / buyers with a 1st purchase
market-day break-even   = (stall fee + labor + travel + permits + sample product + card fees)
                          / contribution per unit at market price
```

Sources for the definitions: SPINS and Circana velocity (store-normalized), Scout repeat-rate definition, deep research synthesis (Nov 2026). Never use gross margin or revenue LTV to set CAC.

## Waterfall 1: through a distributor to grocery

**Eightx model, $4.99 item (June 2026):**

| Step | Who keeps it | Amount | Left |
|---|---|---|---|
| Shelf price | | $4.99 | $4.99 |
| Retailer margin, about 30% | grocer | $1.50 | $3.49 |
| Distributor, about 13% | UNFI or KeHE | $0.45 | $3.04 |
| Trade spend, about 18% | retailer programs | $0.55 | $2.49 |
| COGS | factory | $1.49 | $1.00 gross profit, about 20% of shelf |

**Illustrative $7.99 sauce (deep research, Nov 2026):** retailer 35% leaves $5.19; distributor 20% of its sell price leaves a $4.15 invoice; 18% trade and deductions leaves $3.40 net; $1.85 landed COGS leaves $1.55 contribution, 46% of net realized revenue but 19% of shelf.

**Eightx $5.99 shelf-stable example (June 2026):** retailer about 38%, distributor sell price about $3.71, bill-through to the brand about $2.82. Broker, distributor and trade costs then absorb 40 to 50% of bill-through revenue before COGS.

The conflict on distributor margin: UNFI's reported corporate gross margin is about 13% (Q2 FY2026), which is what the $4.99 model uses. What brands actually pay is higher once fees are stacked. Plan with 20 to 28% of the distributor's sell price plus the fee stack below, then replace with real terms.

### The distributor fee stack (Eightx, June 2026, natural and specialty grocery)

| Line | Range |
|---|---|
| Distributor effective margin | 20 to 28% of its sell price (refrigerated or commodity 18 to 22%; slow or high-service 25 to 30%) |
| Freight or distribution allowance | 7 to 12% on top of margin, plus 1 to 2% fuel surcharge in high-diesel periods |
| MCBs (manufacturer chargebacks for promotions) | 8 to 15% of sales a year; often billed 60 to 90 days after the promotion |
| Marketing or MCB admin fee | 1 to 3% of net sales on every invoice |
| Shrink and reclamation | 1 to 3% combined, more for perishables |
| Cash discount for on-time payment | 1 to 2% of gross invoice |
| New item fee | $250 to $500 per SKU per distributor or distribution center |
| EDI setup | $200 to $1,000 |
| Portal access | $50 to $250 a month |
| Broker | 3 to 5% of net sales conventional; 5 to 7% natural for early brands, settling to 4 to 6% |

Packaged food and beverage gross margins run 30 to 49%, public-company median 33.9%; wholesale compresses margin 20 to 30 points versus DTC (Eightx, 2026). Hold a 35% gross margin floor on retail business.

**Trick: the deductions arrive after the cash.** MCBs land 60 to 90 days after the promotion. Model cash, not just margin: a profitable promo month can show up as a negative remittance in month three.

## Waterfall 2: direct to independents and local grocers

Retailer margin bands are practitioner guidance, not audited data: 25 to 40% conventional grocery, 35 to 45% natural and specialty (Vice CPG, 2026); Eightx uses 25 to 30% for national-brand center store. Many independents and gift shops expect about 50% (keystone); one candle maker planned wholesale at about 50% of online retail (operators report).

Illustrative, $7.99 MSRP sold direct to a natural independent at 40% margin:

| Line | Per unit |
|---|---|
| Wholesale price | $4.79 |
| Self-delivery (route cost / units on route) | $0.30 |
| Samples and free fill, amortized over year one | $0.15 |
| Landed COGS | $1.85 |
| Contribution | $2.49 |

That is 60% more per unit than the distributor route ($1.55). Direct-to-retail saves 30 to 40 points combined versus a distributor (Eightx, 2026). The trade-off is delivery labor and route density. Use direct for the first 10 to 40 local doors and for accounts a distributor will not serve.

## Velocity to dollars: the number buyers and owners both need

```
annual contribution per door = UPSPW x 52 x contribution per unit
```

At 2 UPSPW (near the Kroger-panel median of 1.99, Scout 2026) and $1.55 contribution: 2 x 52 x 1.55 = **$161 per store per year**. Fifty stores earn $8,060 a year. A $20,000 launch package for those 50 stores takes 2.5 years to recover. At 3.57 UPSPW (p75) the same stores earn $288 each and pay back in 1.4 years.

**Trick:** show the owner this table before they accept a chain. It turns "we got into 200 stores" into "we need 3 UPSPW for 16 months to break even."

## Trade spend, slotting and launch costs

**Trade spend (planning numbers):**

- 44% of surveyed CPG companies spent 11 to 15% of revenue on trade promotion; 16% spent 20 to 27%; 7% over 27% (POI 2024 benchmark, possibly outdated).
- Model 15 to 25% of gross wholesale sales until real terms exist; grocery-heavy brands cluster at 18 to 20%, club-heavy 22 to 24% (Eightx, 2026).
- Leading "10X" natural brands sold 36 to 43% of department volume on promotion versus 19 to 28% department averages (SPINS, 2025). Sales on promo is not the same as trade spend percentage, but it shows how promotion-dependent scale becomes.

**Slotting and launch package (planning ranges, not syndicated data):**

| Line | Range | Source |
|---|---|---|
| Slotting per item per store | $250 to $1,000 | Eightx citing NielsenIQ, 2026 |
| Slotting per SKU across a chain or region | $5,000 to $20,000+ | same |
| Regional launch, 150 to 400 stores: direct slotting | $0 to $25,000 | spring.ai, 2026 |
| Free fills | $3,000 to $12,000 | spring.ai, 2026 |
| Distributor setup | $1,500 to $6,000 | spring.ai, 2026 |
| First-year promotions | $8,000 to $30,000 | spring.ai, 2026 |
| Demos | $2,000 to $15,000 | spring.ai, 2026 |
| FTC study average slotting, per product, retailer and metro | $2,313 to $21,768, median $6,500 | FTC 1998 to 2001 data, outdated |

**Free fill math (illustrative):** 2 SKUs x 50 stores x one 12-unit case x $1.85 COGS = $2,220 of product, plus freight, before a single sale.

**Trick: ask what replaces slotting.** "No slotting" deals often carry free fills, mandatory ad buys, reset fees or introductory allowances that cost the same (deep research, 2026). Most slotting is negotiable for emerging brands; ask to redirect it into demos (FoodBevy).

## Launch break-even (worked)

Illustrative: $20,000 regional launch package, $1.55 contribution per unit.

```
break-even units = 20,000 / 1.55 = 12,903 units
weeks to break even = 12,903 / (UPSPW x stores)
  at 2 UPSPW in 150 stores = 43 weeks
  at 1 UPSPW in 150 stores = 86 weeks (the item is usually cut before then)
```

## Waterfall 3: DTC, why single jars do not work

Illustrative food bundles against a $29.66 median paid CPA (Triple Whale, 2025 to 2026):

| Order | Price | Landed COGS | Packaging | Pick and pack | Shipping | Payment 3% | Contribution |
|---|---|---|---|---|---|---|---|
| 1 jar | $9.99 | $1.85 | $1.00 | $2.50 | $9.00 | $0.30 | -$4.66 |
| 3-pack | $29.00 | $5.55 | $2.00 | $3.00 | $10.00 | $0.87 | $7.58 |
| 6-pack | $54.00 | $11.10 | $3.00 | $3.50 | $13.00 | $1.62 | $21.78 |

Even the 6-pack does not cover a median paid CPA on order one. Food DTC works through organic acquisition, gifting, subscriptions and repeat, not cold paid traffic. One founder found a $10 sauce bottle had $12 cheapest shipping and 28 to 84 days delivery to international buyers before buying traffic there (operators report).

Illustrative beauty serum: $48 price, $6 landed COGS, $3 pick and pack, $6 shipping, $1.44 payment = $31.56 contribution against a €47.16 median blended CAC (adtribute, 2026). The first order loses money; the second order decides the business. That is why minis, discovery sets and subscriptions exist.

**Trick: price for the paid channel or skip it.** A $90 cosmetic with $10 product and $10 shipping leaves $70 to compete for traffic; a $30 product with the same costs leaves $10 (operators report, 103-pt thread).

## Waterfall 4: Amazon

US referral fees (Amazon, Nov 2026): Grocery and Gourmet 8% when the total sales price is $15 or less, 15% above; Beauty, Health and Personal Care 8% at $10 or less, 15% above. FBA fulfillment for standard sizes adds about $2.43 to $5+ per unit in 2026, before storage and inbound placement.

Illustrative $12 grocery item: referral $0.96, FBA $3.50, landed COGS $1.85, inbound $0.40, ads at 10% TACoS $1.20 = **$4.09 contribution**.

**Trick: the fee cliff.** The rate applies to the whole price. A grocery item at $14.99 pays $1.20; at $15.49 it pays $2.32. Raising price 50 cents loses 62 cents. Same at $10 for beauty and health: $9.99 pays $0.80, $10.49 pays $1.57. Price just under the threshold or well above it (a multipack).

## Waterfall 5: Faire

North America (Faire, Nov 2026): marketplace-discovered retailer orders pay 15% commission plus $10 on the opening order; Faire Direct orders (retailers you bring) pay 0% commission. Payment processing 1.9% + $0.30 at 60-day payout up to 3.5% + $0.30 next-day. Outside North America the first marketplace order can carry 25% commission.

Illustrative opening order, one case of 12 at $8 wholesale = $96:

- Marketplace: $14.40 + $10 = **$24.40 (25% of the order)**
- Faire Direct with next-day payout: 3.5% + $0.30 = **$3.66**

**Trick:** put your Faire Direct link on every sample card, sell sheet and trade-show follow-up so the stores you find yourself never come through as marketplace orders.

## Waterfall 6: TikTok Shop

Fee stack: 6% referral (US, 2026), creator commission you set from 1 to 80%, sample product and shipping, discounts, refunds, GMV Max spend.

Illustrative $24 skincare duo: referral $1.44, creator commission 20% $4.80, landed COGS $5, pick, pack and ship $6, payment included in referral = $6.76 before ad spend and samples. At 50 samples a week costing $8 each ($400), the brand needs 59 commissioned orders a week just to cover samples.

**Trick:** separate creator commission from paid-media budget in the books so GMV Max cannot hide an unprofitable combined CAC (deep research, 2026).

## Waterfall 7: market day

Illustrative: stall $40, two people for 7 hours at $18 = $252, travel $25, sample product $20, card fees 3% → $337 plus card fees. At a $10 price and $1.85 COGS, contribution per unit after a 3% card fee is $7.85. Break-even: about 43 units. The research model: $350 a day at $5 contribution needs 70 units.

Do not credit the market with hypothetical LTV from contacts captured. Value contacts only after measuring their later purchases.

## Setting the shelf price

1. Find the category's price per ounce or per serving on the shelf where it will sit; position against the 2 or 3 nearest items.
2. Work the waterfall backward to the brand invoice for the intended channel.
3. Check landed COGS at or under about 25% of shelf for distributed SKUs. If it is 30%+, change pack size, format or ingredients before pitching.
4. Report penny profit as well as margin percentage: a buyer may prefer a slower premium SKU that produces more gross profit per facing (deep research, 2026).
5. Keep the price per ounce honest across sizes. A 6 oz bottle at $15 replaced by a 4 oz at $10 advertised as "$5 less" is the same $2.50 per ounce; customers called it deceptive (operators report, 485-pt thread).

Pricing psychology, discount math and promo design: sibling `offers-pricing`.
