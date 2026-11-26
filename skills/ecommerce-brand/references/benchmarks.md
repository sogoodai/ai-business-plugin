# Benchmarks

Use benchmarks as diagnostic priors, never as goals. Match category, AOV, revenue band and attribution method before comparing. A $70 skincare order is not a $600 sofa. Three kinds of numbers, kept apart:

- **Measured:** platform documentation, aggregate merchant datasets, published percentiles. Most are vendor datasets (Klaviyo, Omnisend, Triple Whale, Kolect): large but a customer cohort, not a census, and revenue is vendor-attributed.
- **Agency samples:** small (18 to 38 accounts). Directional.
- **Operators report:** Reddit practitioners. One business, real but anecdotal.

"Year" is the period the data describes. Full links in [sources.md](sources.md). Where a top quartile was never published, the cell says so; do not invent one.

## Store conversion and checkout

| Metric | Typical | Top quartile / strong | Source | Year |
|---|---|---|---|---|
| Conversion, pet care | 5.70% avg | not published | Shopify citing Dynamic Yield | 2026 |
| Conversion, beauty and personal care | 5.32% avg | not published | Shopify / Dynamic Yield | 2026 |
| Conversion, food and beverage | 4.58% avg | not published | Shopify / Dynamic Yield | 2026 |
| Conversion, fashion and apparel | 2.77% avg | not published | Shopify / Dynamic Yield | 2026 |
| Conversion, home and furniture | 1.29% avg | not published | Shopify / Dynamic Yield | 2026 |
| Conversion, luxury and jewelry | 0.63% avg | not published | Shopify / Dynamic Yield | 2026 |
| Cart abandonment | 70.22% avg (50 studies) | no credible "good" line | Baymard | through 2025, pub. 2026 |
| Conversion gain available from checkout UX alone (large sites) | 35.26% potential | n/a | Baymard | 2026 |
| Mobile load time | -1 s associated with about +3% conversion; pages over 4 s convert 22% lower | n/a | Yottaa via Shopify (observational) | 2025, pub. 2026 |
| US online return rate | 19.3% | not published | NRF | 2025 |
| Return rate same product by channel | Shopify <1%, Amazon <3.5%, QVC 6%, Target ~16% | n/a | operators report, r/ecommerce | 2024 |

## Retention and repeat

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Repeat purchase rate, Shopify stores under $1M | 16.3% median | 25.8% p75 | By the Numbers, 1,326 stores | Sep 2025 to Aug 2026 |
| Repeat purchase rate, $1M to $10M | 19.8% median | 29.4% p75 | By the Numbers | 2025 to 2026 |
| 365-day repeat, coffee and tea | 31.7% median | 41.6% p75 | By the Numbers | 2025 to 2026 |
| 365-day repeat by category | skincare 24.9%, cosmetics 22.1%, specialty food 21.7%, clothing 19.1%, jewelry 16.9%, decor 13.0%, bags 12.9%, shoes 12.3% | not published | By the Numbers | 2025 to 2026 |
| Faire wholesale reorders | 70% within 90 days; ~45-day cadence; 60% placed at 25% or less inventory left; 5th order = ~2.5x likelier long-term account | n/a | Faire (marketplace operator, biased) | 2026 |

Rule-based churn windows when predictive tools lack data (finsilabs harvest, MIT, uncited): consumables repurchase 30 to 60 days, at-risk 60+, churned 120+; apparel 60 to 90 / 90+ / 180+; home goods 90 to 180 / 180+ / 365+.

## Email and SMS (depth in sibling skill `email-sms-loyalty`)

| Metric | Typical | Top quartile / top 10% | Source | Year |
|---|---|---|---|---|
| Automated email revenue per send | $2.87 (2% of sends, 30% of email revenue) | not published | Omnisend, 150k brands | 2025 sends, pub. 2026 |
| Scheduled campaign revenue per send | $0.18 | not published | Omnisend | 2025 |
| Klaviyo abandoned cart email RPR, all | $6.77 | $13.70 top 10% | Klaviyo, 110k+ customers | 2026 |
| Klaviyo abandoned cart RPR, $1M to $5M brand, $83 to $112 AOV | $2.39 p25 | $5.86 p75 | Klaviyo Help benchmark | Oct 2026 |
| Same, $163 to $291 AOV | $6.00 p25 | $16.40 p75 | Klaviyo Help | Oct 2026 |
| Klaviyo welcome email RPR | $5.75 | $13.27 top 10% | Klaviyo | 2026 |
| Back-in-stock email | 6.72% conversion, $9.14/email, used by only 0.6% of brands | n/a | Omnisend | 2025 |
| Back-in-stock SMS | n/a | 58.7% CTR, 13.8% CVR, $13.34 EPM (p75) | Postscript | 2026 |
| Abandoned cart SMS | n/a | 17.28% CTR, 7.84% CVR, $10.95 EPM (p75) | Postscript | 2026 |
| Campaign SMS | n/a | 8.01% CTR, 0.54% CVR, $0.55 EPM (p75) | Postscript | 2026 |
| Popup submit rate | 2.3% median (Klaviyo); 1.30% median (Poptin) | 3%+ target (Klaviyo); 2.67% p75 (Poptin) | Klaviyo; Poptin, 2,305 popups | 2026 |
| Popup delayed 20 to 50 s vs instant | +20 to 43% capture in tested cases | n/a | Wisepops A/B compilation (vendor) | 2025 to 2026 |

Never compare RPR across vendors or across AOV bands. Look up the row matching the brand's revenue and AOV.

## Paid acquisition (depth in sibling skill `paid-ads`)

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Meta ecommerce CPA | $38.99 median | not published | Triple Whale, 40k+ brands | Aug 2025 to Jul 2026 |
| Meta ecommerce ROAS | 1.88x median | not published | Triple Whale | Aug 2025 to Jul 2026 |
| Meta ecommerce CPM / CTR / CVR | $15.06 / 2.39% / 1.53% median | not published | Triple Whale | Aug 2025 to Jul 2026 |
| Meta DTC purchase ROAS, agency sample | 2.55 median ($13.40 CPM, 2.65% CTR) | not published | Top Growth Marketing, 19 clients | Oct 2025 to Sep 2026 |
| Health and beauty CPA, cross-channel | $33.44 | $16.77 | Triple Whale, rolling 90 days | Sep 2026 |
| Google PMax ROAS | 2.50 median | ~2.80 p75 | Olifant, 18 accounts | Nov 2025 to Oct 2026 |
| Google PMax CVR | 2.7% | not published | Olifant | 2025 to 2026 |
| Amazon Sponsored Products ACoS | 38% median | 25% (lower quartile is better) | SellerPlex, 38 accounts | H1 2026 |
| Amazon PPC CVR | 8.3% median | 11.1% p75 | SellerPlex | H1 2026 |
| Amazon CPC | $1.07 median | n/a | SellerPlex | H1 2026 |
| Amazon top-of-search vs product page | CPC +56%, CPA -40% | n/a | Perpetua (ad-tech vendor) | Q3 2026 |
| Amazon peer benchmarks in console | p25 and p75 by category: CTR, CPC, purchase rate, NTB | n/a | Amazon Ads benchmark reports | since May 2026, p25/p75 export Oct 2026 |
| Meta creatives that become winners (10x account-median spend) | 5 to 8% | n/a | Motion, 578,750 creatives | 2026 |

Learning-budget floors (platform-stated): Google Smart Bidding judged on 30+ conversions (50 for tROAS); TikTok Smart+ starts at 10x CPA per day, 30x preferred with targets; Pinterest Performance+ 50 conversions a week and 5x CPA daily budget; Google PMax six weeks before judging, experiments 4 to 6 weeks with week 1 discarded.

## Creators and affiliates

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Paid deliverable, nano | $134 median cash | not published | inBeat on OpenSponsorship, 1,527 deliverables | Jan 2025 to Jun 2026 |
| Paid deliverable, micro 10k to 50k | $150 median | not published | inBeat | Jan 2025 to Jun 2026 |
| Paid deliverable, 50k to 250k | $417 median | not published | inBeat | 2025 to 2026 |
| Paid deliverable, macro / mega | $517 / $2,727 median | not published | inBeat | 2025 to 2026 |
| Collaboration cost | half between $300 and $900 | n/a | Kolect, 120k+ collaborations | Aug 2025 to Oct 2026 |
| Cost per 1,000 views | $22.83 overall, $23.11 TikTok, $44.54 YouTube | not published | Kolect | 2025 to 2026 |
| Single-post deals including paid usage, whitelisting or ad code rights | 80% | n/a | Kolect | 2025 to 2026 |
| TikTok Shop affiliate commission allowed | 1% to 80%; Target Collab overrides Open | no robust optimum | TikTok Shop docs | Nov 2026 |
| TikTok free-sample creators | sales in prior 120 days; seller reviews in 7 days, ships in 7 days; content due 14 days after receipt | n/a | TikTok Shop docs | Sep 2026 |
| DTC affiliate commission | 5 to 15% (to 20% high margin) | n/a | OpenClaudia harvest, MIT (uncited) | 2026 |
| Paid shoutout, ~300k-follower niche page | $100, or $75 each for 5 | n/a | operators report, r/ecommerce | pre-2024 |

## Marketplaces

| Metric | Value | Source | Year |
|---|---|---|---|
| Etsy active buyers / sellers / items | 86.5M / 5.6M / 100M+; ~30% of GMS custom or made-to-order | Etsy 10-K | 2025 |
| Etsy Offsite Ads fee | 15% under $10k trailing-365 sales (opt-out allowed), 12% above (mandatory for life), $100 cap, 30-day click | Etsy Help | 2026 |
| Etsy search priority for US domestic shipping | under $6 (with exceptions) | Etsy Seller Handbook | since Oct 2024 |
| Etsy tags | 13 per listing, 20 characters each; title up to 140 | Etsy; nexscope harvest | 2025 to 2026 |
| Amazon Vine (US) | $0 for up to 2 units, $75 for 3 to 10, $200 for 11 to 30; under 30 reviews to enroll; inventory 3 weeks before launch | Sell on Amazon | 2026 |
| Amazon Vine claimed lift | +30% sales (Amazon internal, vendor-biased) | Sell on Amazon | 2026 |
| Amazon referral fee | 15% most categories; jewelry 20%, apparel 17%, electronics 8% (simplified, tiered in reality) | nexscope harvest, MIT | verify |
| TikTok GMV Max | default and only Shop Ads campaign type since Jul 2025; counts paid and organic orders of promoted products | TikTok Ads Help | 2025 to 2026 |

## Pricing and promotions

| Metric | Value | Source | Year |
|---|---|---|---|
| BFCM consumer spend vs discount depth | spend +11% YoY while discounts fell 10%; repeat-buyer revenue +13.5% | Klaviyo BFCM report (SEC filing) | 2025 |
| Gross-profit growth by BFCM discount depth | ~2.05x around 15% off vs ~1.75x around 40% off | Lebesgue, 500+ stores (stores at 30% off started with 72% vs 66% gross margin) | 2025 |
| Retailers using a free-shipping minimum | 56%; 94% of shoppers say free shipping influences purchase | Shopify (consumer survey) | 2026 |
| Post-purchase upsell case lifts | MaryRuth +27% AOV, Feals +18.93% AOV | Rebuy case studies (vendor-selected) | 2025 to 2026 |
| Subscription-benefit PDP treatment | +29% subscription opt-ins, +9% sitewide conversion at 99% confidence | Shopify, Magic Spoon case | 2025 to 2026 |
| A/B sample needed, 3% baseline, 20% lift | ~14,000 visitors per variant | Replo | 2026 |

## Operator-reported numbers worth knowing

Real but single-business. Use to frame expectations, not as targets.

| Number | Context | Source |
|---|---|---|
| 90% of sales from ~20% of listings | Etsy: 5 subniches x 5 listings, then expand the winner | r/EtsySellers, 232-pt thread |
| 43 to 57% of POD designs ever sell | 208 designs (42.8% sold), 242 designs (56.6% sold) | r/printondemand, 44 and 78-pt threads |
| Shops with 500 to 5,000 sales price at $26 to $32 median vs $17.99 for abandoned shops | Etsy POD, 50 shops reviewed | r/printondemand, 173-pt thread |
| PDP recommendation block: 10.32% vs 2.43% conversion, $3.91 vs $0.86 per visit | Shopify app, method not described | r/shopify, 160-pt thread |
| Afterpay added: conversion 2.9% to 6%+ in 2 months | uncontrolled | r/dropship, 146-pt thread |
| Popup tested 50+ times: signup 2.8% to ~7% | 7-figure apparel | r/ecommerce, 28-pt thread |
| Store Spotlight ads CTR 0.6% to ~2% | Amazon, vague keywords | r/FulfillmentByAmazon, 125-pt thread |
| Best off-Amazon ad placement ACoS seen across audits: 70% | default opt-in | r/FulfillmentByAmazon, 20-pt thread |
| Shop-button video 50 to 100 sales/day vs bio link ~5/day | TikTok Shop, one seller | r/TikTokshop |
| GMV Max week: $1,871 spend, 660 orders, $11,255 attributed | revenue only, no profit | r/TikTokshop, 51-pt thread |
| Gift-guide press: one Today Show mention = $24k in a day | DTC gift product | r/ecommerce, 270-pt thread |
| Niche Facebook group post: 800+ visitors, 50+ orders | rabbit hay, 14k-member group | r/ecommerce, 226-pt thread |
| Abandoned checkout recovery: email 8 to 12%, SMS 12 to 18%, voice + SMS 18 to 25% | ~1,000 carts, uncontrolled | r/dropship, 45-pt thread |

## No robust benchmark exists for

Top-quartile store conversion by category, an optimal TikTok affiliate commission, a "minimum viable" Meta daily budget, cold-email reply rates for wholesale, Etsy Ads ROAS, and contribution LTV by sub-model. Say so instead of inventing one.
