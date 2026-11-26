# Economics

Digital products have near-zero marginal cost, so the money questions are fees, price, traffic, conversion and support time. Every formula below has a worked example. Fees are November 2026 published rates; processing for Gumroad, Stan, Shopify and Payhip is modeled at 2.9% + $0.30 (check the live rate). Sources in [benchmarks.md](benchmarks.md).

## 1. Net per order

```
Etsy:             net = P - 0.20 - 0.065P - (0.03P + 0.25)          (US processing)
Etsy Offsite:     subtract another 0.15P (shop under $10k/yr) or 0.12P, max $100
Gumroad direct:   net = P - 0.10P - 0.50 - processing
Gumroad Discover: net = 0.70P
Lemon Squeezy:    net = P - 0.05P - 0.50       (+0.05P on recovered carts, +0.03P on affiliate orders)
Payhip Free:      net = P - 0.05P - processing
Stan, Shopify, Payhip Pro: net = P - processing, minus the monthly plan
Creative Market:  net = 0.50P
```

Worked examples (our math):

| Price | Etsy | Etsy + Offsite 15% | Gumroad direct | Discover | Lemon Squeezy | Payhip Free | Card only | Creative Market |
|---|---|---|---|---|---|---|---|---|
| $5 | $4.08 | $3.33 | $3.55 | $3.50 | $4.25 | $4.30 | $4.55 | $2.50 |
| $9 | $7.70 | $6.35 | $7.04 | $6.30 | $8.05 | $7.99 | $8.44 | $4.50 |
| $15 | $13.12 | $10.88 | $12.27 | $10.50 | $13.75 | $13.52 | $14.27 | $7.50 |
| $29 | $25.80 | $21.45 | $24.46 | $20.30 | $27.05 | $26.41 | $27.86 | $14.50 |
| $49 | $43.89 | $36.55 | $41.88 | $34.30 | $46.05 | $44.83 | $47.28 | $24.50 |

Agent rule: always model the Etsy Offsite case. One seller paid a $50 Offsite fee when a buyer clicked an ad for a small item and bought a big one (r/Etsy, 391 pts). Never cancel an attributed order to avoid the fee; a buyer reported the shop and bought elsewhere (r/Etsy, 1,484 pts). Price so the attributed order still clears your margin.

## 2. Orders and visitors to a goal

```
orders needed = (goal + monthly fixed costs) / net per order
visitors needed = orders needed / conversion        or   goal / revenue per visitor
```

Orders for $1,000 net a month (our math, no tool costs except where noted):

| Setup | Net per order | Orders a month | Per day |
|---|---|---|---|
| $5 printable on Etsy | $4.08 | 245 | 8.2 |
| $9 template on Etsy | $7.70 | 130 (157 if all Offsite) | 4.3 |
| $15 template on Etsy | $13.12 | 76 | 2.5 |
| $15 on Gumroad direct | $12.27 | 82 | 2.7 |
| $29 bundle on Lemon Squeezy | $27.05 | 37 | 1.2 |
| $29 bundle on Stan Creator ($29 a month) | $27.86 | 37 | 1.2 |
| $97 mini-course on Stan | about $93.9 | 11 | 0.4 |

The ladder lesson: moving the average order from $9 to $29 cuts the orders you need by about 70%. That is why bundles and bumps come before more traffic.

Revenue per visitor (RPV) from operator reports: $2,143 / 3,400 visitors = $0.63 (planner shop); $1,518 / 2,647 Discover views = $0.57; $6,831 / 15,247 Pinterest visitors = $0.45 (course). At $0.45 to $0.63, $1,000 a month needs about 1,600 to 2,200 qualified visitors a month. If your RPV is under $0.20 after 1,000 visitors, the problem is offer or traffic fit, not volume.

## 3. Platform plan break-evens

- **Payhip Free to Plus:** saves 3 points for $29: break-even $29 / 0.03 = **$967 a month** in sales. Plus to Pro: $70 / 0.02 = **$3,500** (Payhip pricing, our math).
- **Gumroad direct vs Payhip Plus at $15:** Gumroad keeps $12.27, Payhip Plus keeps about $14.00 minus $29 a month. Above about 17 sales a month, Payhip Plus wins on fees; then weigh Gumroad Discover reach and Merchant of Record coverage (Payhip also remits EU and UK VAT).
- **Stan Creator ($29) vs Gumroad direct:** Gumroad's percentage on a $29 product is about $3.40 more per order than card-only. Stan pays off above about 9 orders a month at $29; above about 15 at $15. Tax handling: the research confirmed Merchant of Record or tax remittance only for Gumroad, Lemon Squeezy and Payhip; check Stan's current terms before assuming it files VAT for you.
- **Gumroad high-volume discount:** direct sales above $20,000 in a calendar month drop to 5% + $0.50 for the rest of that month. Launch months benefit; do not plan around it.
- **Lemon Squeezy add-ons:** cart recovery costs +5% only on recovered orders, which you would not have had; affiliate orders +3% on top of the commission.

## 4. Contribution after support and refunds

```
contribution per order = net - (support minutes per order x hourly value / 60) - refund rate x price - payment disputes cost
```

Worked example: a $6 crochet pattern nets about $5.10 on Etsy. If almost every sale triggers a message (operators report this for patterns sold beside finished items, r/EtsySellers 239 pts) and each takes 5 minutes at $30 an hour, support costs $2.50 and contribution halves. Add an 8% refund rate (operators report for static PDF trackers) and it drops again. Fix: delivery design ([delivery-refunds-ip.md](delivery-refunds-ip.md)), or raise price and bundle.

## 5. Ladder math

```
net revenue per checkout = core conversion x (core net + attach rate x bump net + upgrade rate x upgrade net)
```

Keep a bump only if net revenue per checkout rises and core conversion does not fall materially. Example: 100 checkouts at $15 core, 25% take a $7 bump: +$175 gross, about +$166 net on Lemon Squeezy. If core conversion fell from 3.0% to 2.7% on the same traffic, you lost 10 core sales ($137 net) and gained about $150 of bumps on the remaining 90: barely positive. Judge on net revenue per visitor, not attach rate.

## 6. License tier math

Creative Market's minimums put a commercial template at 1.56x personal ($14 vs $9) and extended at 4x ($36). If 15% of buyers choose commercial at 1.6x, AOV rises 9% with no new product. Extended tiers should carry a real right (resale in client work above the 5,000 end-product cap, merchandise, templates for client deliverables), not a label.

## 7. Pay what you want

Studies (2024): higher suggested prices raise payments, and payments land below the anchor. Treat PWYW as list building:

```
value of a PWYW lead = average payment + email value per subscriber
email value per subscriber = 90-day email revenue / list size     (compute from your own data)
```

Use PWYW only when the email value is the point (entry product, open-source tool, community goodwill). Use a minimum ($0 or a floor) plus a suggested price; on Gumroad any positive payment must be at least $0.99.

## 8. Affiliate commission ceiling

```
max commission % = (net per order - target contribution per order) / price
```

Example: $49 template bundle on Lemon Squeezy nets $46.05, minus 3% LS affiliate fee ($1.47) = $44.58 before commission. If you want $20 contribution per affiliate order, the ceiling is ($44.58 - $20) / $49 = **50%**. On a $9 Etsy item there is no affiliate program to run; affiliates belong on direct checkout. Pay only after the refund window closes (coreyhaines31/marketingskills affiliate operations, MIT).

## 9. Paid traffic break-even

```
break-even CPA = net per order x (1 + expected repeat and upsell orders in 90 days)
break-even CPC = break-even CPA x landing conversion
```

Example: $29 product nets $27; 20% of buyers take a $19 upsell within 90 days (+$3.60): break-even CPA about $30.60. At a 2% landing conversion, break-even CPC is $0.61. Operators report $500 of Facebook ads bought 3 signups for a $297 course (about $167 each) and the seller moved to Pinterest (r/juststart, 152 pts). Etsy Ads on a new shop: about $20 for one $4.99 sale (r/EtsySellers, 341 pts). Expect paid to fail below a $25 average order unless the buyer stays for more products.

## 10. Catalog economics

- **Concentration check:** if the top 20% of SKUs carry under 60% of revenue after 6 months, you have not found the winner yet; keep testing subniches. One POD seller with 8,000 designs reports 10-plus bestsellers carry 90% of sales (r/passive_income, 474 pts).
- **Production rule:** validate cheaply first, then invest in the winners. KDP operators publish decent books first (most sell under 10 copies), then 2 to 5-day books in niches that sold, then outsource high-quality versions of confirmed winners, which made most of the revenue (r/sidehustle, 159 pts).
- **Focus rule:** operators report staying on one project until it makes $1,000 a month before starting another (r/passive_income, 1,148 pts).
