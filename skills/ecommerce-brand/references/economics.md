# Unit economics: the control system

Every growth decision in this skill is checked against contribution, not revenue or platform ROAS. Build this model before recommending any spend. Numbers marked "operators report" come from Reddit practitioners; sources in [sources.md](sources.md).

## The record to keep per SKU and per channel

```
net revenue           = price paid - discounts - refunds and returns allowance
landed COGS           = unit cost + inbound freight + duties and tariffs + inbound prep
contribution / order  = net revenue - landed COGS - pick, pack, packaging - outbound shipping you pay
                        - payment fee - marketplace fees - affiliate or creator commission
                        - per-order app costs - sample cost amortized per order
CM%                   = contribution / net revenue
break-even first-order CAC   = contribution / order
break-even ROAS (platform)   = platform-reported order value / contribution per order
break-even ACoS (Amazon)     = contribution before ads / price
TACoS                 = total ad spend / total sales (ads + organic)
MER                   = total revenue / total paid media spend
new-customer CAC      = paid media spend / new customers (not orders)
```

Rules:

- **Compute break-even ROAS on the same revenue the platform reports.** Meta, Google and TikTok report gross order value before returns. Divide that by contribution, not by net revenue, or the break-even line is too low.
- **Purchase price understates COGS by 15 to 40% for imported goods** once freight, duties and prep are added (finsilabs harvest, MIT; uncited). Ask for the landed number.
- **Returns are SKU and category specific.** NRF put US online returns at 19.3% in 2025; one operator saw the same batch return under 1% on Shopify, under 3.5% on Amazon, 6% on QVC and about 16% at Target. Use the store's own return rate by channel.
- **Recheck quarterly with every cost.** One Amazon seller found all-in costs were 38% of gross, not the 26% they tracked without ads and inbound freight (operators report, r/FulfillmentByAmazon 2026).

## Worked examples by sub-model

**Shopify DTC, $40 product, free shipping**

| Line | Amount |
|---|---|
| Price | $40.00 |
| Average discount (10%) | -$4.00 |
| Returns allowance (6% of $36) | -$2.16 |
| Net revenue | $33.84 |
| Landed COGS | -$9.00 |
| Pick, pack, packaging | -$3.00 |
| Shipping you pay | -$6.00 |
| Payment fee (2.9% + $0.30 on $36) | -$1.34 |
| Apps per order | -$0.50 |
| **Contribution** | **$14.00 (41% CM)** |

Break-even first-order CAC $14. Break-even platform ROAS = $36 / $14 = 2.57. Meta ecommerce median CPA was $38.99 in Aug 2025 to Jul 2026 (Triple Whale), so this SKU cannot buy cold traffic on the first order. The fix is AOV (bundle, threshold, post-purchase offer), price, or a proven repeat rate, not "better targeting".

**Etsy, $28 item + $5 shipping charged**

| Line | Normal order | Offsite Ads order (15%) |
|---|---|---|
| Order total | $33.00 | $33.00 |
| Listing fee | -$0.20 | -$0.20 |
| Transaction fee 6.5% of total incl. shipping | -$2.15 | -$2.15 |
| Processing 3% + $0.25 (US) | -$1.24 | -$1.24 |
| Offsite Ads fee | 0 | -$4.95 |
| Materials | -$6.00 | -$6.00 |
| Packaging | -$1.00 | -$1.00 |
| Postage | -$5.00 | -$5.00 |
| **Contribution before labor** | **$17.41** | **$12.46** |

Fee rates as operators itemize them (r/printondemand 2026); verify the current Etsy fee schedule and the shop's country. Offsite Ads is 15% until the shop crosses $10,000 in a 365-day period, then 12% and mandatory for life, capped at $100 per order, 30-day click window (Etsy Help, 2026). **Price every Etsy SKU so it survives the Offsite Ads case.** Then subtract labor: a $12 rose that takes an hour is a hobby, not a SKU (operators report).

**Amazon FBA, $29.99 private label**

| Line | Amount |
|---|---|
| Price | $29.99 |
| Referral fee (15% most categories) | -$4.50 |
| FBA fulfillment fee (example) | -$5.50 |
| Storage, monthly average | -$0.30 |
| Landed COGS | -$6.00 |
| Inbound placement and freight | -$0.60 |
| Returns allowance (3%) | -$0.90 |
| **Contribution before ads** | **$12.19** |

Break-even ACoS = 12.19 / 29.99 = 41%. Operators use a launch gate: `price x 0.85 - FBA fee - 2 months storage - COGS` should leave "comfortably above 45%" gross margin so there is room for price cuts and CPC rises. This example sits at 45%: borderline. SellerPlex's H1 2026 sample had a 38% median ACoS, which would leave this SKU almost nothing on ad-driven orders.

**TikTok Shop, $25 product, free shipping**

| Line | Amount |
|---|---|
| Price | $25.00 |
| Referral fee (operators report 6%, 2026) | -$1.50 |
| Affiliate commission 15% | -$3.75 |
| Smart Promotion 3.5% (if on) | -$0.88 |
| Free-shipping subsidy (operators report $8+) | -$8.00 |
| Landed COGS | -$5.00 |
| Packaging | -$0.50 |
| **Contribution** | **$5.37 before samples and GMV Max** |

Then amortize samples: 50 samples at $7 landed = $350; if they produce 100 orders, that is -$3.50 per order. Operators who scaled TikTok Shop sell $14 to $19 items mostly through affiliates, but they track net profit per SKU daily against this stack (r/TikTokshop 2026). Verify every fee in Seller Center; they change often.

## LTV, allowable CAC and payback

```
contribution LTV (horizon H)  = first-order contribution
                                + sum over repeat orders within H of (repeat AOV x CM%)
observed repeat rate          = customers with 2+ orders / customers (same cohort, 365 days)
allowable CAC                 = contribution LTV within the owner's payback horizon
first-order payback           = CAC / first-order contribution
monthly payback               = CAC / (AOV x orders per month x CM%)
```

- **No universal 3:1 LTV:CAC or 90-day rule.** Set the ceiling from real contribution and the owner's cash. For a cash-constrained small store, aim to pay back on the first order or within 90 days.
- **Use median AOV** if a few large orders skew the mean; exclude cancelled and refunded orders; say which part is observed and which is modeled when you have under 24 months of data.
- **Compare against category repeat, not a global number:** 365-day repeat in 2025 to 2026 Shopify data was 31.7% median for coffee and tea, 24.9% skincare, 19.1% clothing, 16.9% jewelry, 13.0% decor and furniture (By the Numbers, 1,326 stores). A furniture store at 13% is normal.
- **Klaviyo predicted CLV and churn need roughly 500+ purchasers and 180+ days of orders** (harvest reviewer note). Below that, use rule-based windows from [benchmarks.md](benchmarks.md).
- **Paid social buyers repeat less.** Agency-modeled relative LTV by first-touch channel: direct and referral 1.1 to 1.5x organic, paid social 0.5 to 0.8x, affiliate deal sites 0.4 to 0.7x (indranilbanerjee harvest, MIT; uncited). Segment LTV by first-touch channel from day one and check it.

## Offer and price math

```
units lift needed for a discount d   = d / (m - d)          m = CM% before discount
units you can lose after a raise p   = p / (m + p)
incremental contribution of a promo  = discounted contribution x incremental orders
                                       - full-price contribution cannibalized
                                       - extra ad and fulfillment cost
free-shipping threshold candidate    = median AOV + one sensible add-on   (or AOV x 1.2 to 1.3)
added revenue to cover free shipping = shipping cost / gross margin%      ($8 / 40% = $20)
order bump price                     = 20 to 40% of the front-end price
```

- **20% off at a 50% CM needs 67% more units** just to stand still. At a 40% gross margin, matching "20% off MSRP" halves gross profit per unit (operators report).
- **A 10% raise at a 40% CM survives a 20% unit drop.** Operators report raises working often: an Amazon brand went up 50 to 60% in 10% steps over 8 months with less conversion loss than feared; a $39.99 ASIN at $59.99 did $200k in 5 months against $150k the whole prior year (r/FulfillmentByAmazon 2026). Raise in steps and watch the Buy Box.
- **Build tariffs and cost rises in as dollars, not as a multiplier.** Keep profit per unit, accept a lower margin percent, rise less than competitors. One outdoor brand went up 13% while competitors went up 25% or more (r/ecommerce 2025).
- **Stack AOV before you scale acquisition.** A dropship case went from $0.50 profit per sale at an $11 CPA to about $15 by adding a quantity break, a PDP cross-sell of a higher-margin item, and a thank-you-page offer at 40 to 60% off that 2 in 10 buyers took (r/dropship, 207-pt thread). When CPA later rose to $14, the bare offer would have lost $2.50 a sale.

## Creator and sample economics

```
expected creator contribution = expected orders x contribution/order
                                - sample landed cost - flat fee - commission - incremental ad cost
creator rank score            = expected qualified views x expected CVR x contribution/order
                                - fee - sample - commission
sample funnel                 = requests -> approved -> delivered -> content posted
                                -> qualified views -> orders -> repeat creator orders
```

Followers are a secondary filter. Rank by recent shop sales, relevant views, completion history and reuse rights (research synthesis, 2026).

## Testing math

- **Required sample:** at a 3% baseline, detecting a 20% relative lift needs about 14,000 visitors per variant (Replo, 2026). A store with 10,000 sessions a month cannot A/B test button colors. Make structural changes (offer, bundle, hero content, shipping promise) and read them before/after with the seasonality caveat.
- **Run tests two full weeks minimum.** Replo found 19% of ecommerce tests ended within one day and only 33% ran two weeks (2026).
- **Promotion holdout:** where volume allows, keep a no-discount group so you can see how many would have bought anyway.

## Inventory and cash math

From anthropics/knowledge-work-plugins inventory-planner (Apache-2.0), adapted:

```
velocity            = units sold per day over 7 and over 28 days
stockout date       = on hand / max(7-day, 28-day velocity)
order quantity      = (60 days + lead time) x 28-day velocity - on hand - inbound
safety buffer       = max(7 days, lead time / 2), capped at 30 days
order now if        days of cover < lead time + buffer
```

- Never reorder a zero-velocity item. If 7-day and 28-day rates differ by more than 50%, inspect orders first: one wholesale order fakes a bestseller.
- **Second-order cash rule:** 1,000 units at $12 landed is $12,000. At a $20 price you sell 600 units just to fund the reorder (operators report). Hold at least 2x the first order in cash, or negotiate a deposit (one supplier took 20% down and held 500 units in its US warehouse).
- **Marketplace payout lag is working capital.** TikTok Shop sellers report 31 days plus delivery holds and $20k frozen balances; Shopify holds payouts on new stores until tracking uploads. A viral spike of 300+ orders in a day had to be fulfilled from personal money (r/ecommerce). Cap listed stock at what cash can fulfill.
- **Never 5x a reorder after one good day.** One FBA seller ordered 1,000 more units after a single 7-sale day and lost $10,000 (318-pt thread). But do not cut orders when lead times stretch: stockouts let clones take page one within a month (multiple threads). Ramp proportionally to sustained velocity.
