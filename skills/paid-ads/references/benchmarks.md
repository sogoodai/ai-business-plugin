# Benchmarks

Benchmark against the business's own last 6 to 8 periods first, then its own experiments, then CRM cohorts, then a peer cohort, and a broad benchmark last (comparison order from AgriciDaniel/claude-ads, MIT). Keep three kinds of numbers apart:

- **Measured:** platform documentation, platform experiments, large aggregated datasets. Vendor datasets are customer cohorts, not a census: Triple Whale skews to Shopify DTC, WordStream to US lead-gen Search.
- **Platform-stated:** what Google, Meta or TikTok say about their own product. Often averages from their own tests, with selection effects.
- **Operators report:** Reddit practitioner numbers. Real accounts, self-reported, no control group.

Definitions differ. WordStream "CPL" is any configured lead conversion; Triple Whale "CPA" is spend per purchase; Meta lead CVR is a lead-event rate; Meta traffic-objective CPCs ($0.70 in WordStream 2025) are not comparable with sales-campaign CPAs. Before you quote a benchmark, record source, population, date range, metric definition and fit.

## Google Search (measured, US)

| Metric | Typical (median or mean) | Top quartile | Source | Year |
|---|---|---|---|---|
| CTR, all industries | 6.64% | not published | [WordStream/LocaliQ 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks), 13,000+ campaigns | Apr 2025 to Mar 2026 |
| CPC, all industries | $5.42 | not published | same | same |
| CVR, all industries | 8.18% | not published | same | same |
| CPL, all industries | $66.69 | not published | same | same |
| CPC, attorneys and legal | $9.87 | not published | same | same |
| CPC, home improvement | $8.33 | not published | same | same |
| CPC, travel | $2.14 | not published | same | same |
| CPC / CVR, restaurants and food | $2.05 / 8.05% | not published | same | same |
| CVR, business services | 4.85% | not published | same | same |
| CVR, automotive repair and service | 15.51% | not published | same | same |
| CPC / CVR / CPL, education and instruction | $6.23 / 11.38% / $90.02 | not published | [WordStream 2025](https://www.wordstream.com/blog/2025-google-ads-benchmarks) | Apr 2024 to Mar 2025 |

What $5.42 means: $25 a day buys 4 to 5 average clicks. A $25/day home improvement account buys 3. Exploratory query sprawl is unaffordable at that size.

### Home services Search CPL by trade ([LocaliQ 2025](https://localiq.com/blog/home-services-search-advertising-benchmarks/), 3,211 US campaigns, Apr 2024 to Mar 2025)

| Trade | CPL |
|---|---|
| All home services | $90.92 |
| Cleaning | $46.99 |
| Handyman | $54.05 |
| Window cleaning | $66.69 |
| Electrical | $93.69 |
| Landscaping | $117.92 |
| Plumbing | $129.02 |
| Painting | $138.38 |
| General contractor | $165.67 |
| Roofing and gutters | $228.15 |

### Local Services Ads CPL (summary; full table in `home-services`)

| Population | CPL | Source | Year |
|---|---|---|---|
| Blended, 888 contractors, 126,650 leads | $53; book rate 43.9% | [SearchLight](https://searchlightdigital.io/google-local-service-ads-cost-per-lead/) | Feb 2026 |
| Electrical / HVAC / plumbing | $39 / $51 / $57 | same | Feb 2026 |
| Cleaning / junk removal / landscaping / painting | $33.21 / $33.14 / $37.29 / $33.06 | [99 Calls](https://99calls.com/blog/lsa-cost-per-lead-by-industry) | 2026 |
| Handyman median / p75 | $35 / $44 | AdGenius, 24 accounts | 2025 |

## Meta (measured)

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Lead-objective CPC, US | $1.92 | not published | [WordStream 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025) | data to Jun 2025 |
| Lead-objective CVR, US | 7.72% | not published | same | same |
| Lead-objective CPL, US | $27.66 (+20.94% YoY) | not published | same | same |
| Traffic-objective CPC, US | $0.70 | not published | same | same |
| Education lead CPC / CVR / CPL | $1.65 / 10.08% / $28.22 | not published | same | same |
| Restaurants traffic CTR / CPC | 2.68% / $0.45 | not published | [LocaliQ](https://localiq.com/blog/facebook-advertising-benchmarks/) | 2026 |
| Ecommerce CPM | $15.06 | not published | [Triple Whale](https://www.triplewhale.com/blog/facebook-ads-benchmarks), 40,000+ brands | Aug 2025 to Jul 2026 |
| Ecommerce CTR | 2.39% | not published | same | same |
| Ecommerce CVR (purchase) | 1.53% | not published | same | same |
| Ecommerce CPA | $38.99 | not published | same | same |
| Ecommerce ROAS | 1.88x | not published | same | same |
| DTC CPM / CPC / CTR / ROAS | $13.40 / $0.59 / 2.65% / 2.55x | not published | [Top Growth Marketing](https://topgrowthmarketing.com/dtc-ecommerce-benchmarks/meta-ads-benchmarks/), 19 clients, $2.88M spend (agency) | Oct 2025 to Sep 2026 |
| Advantage+ leads vs not | 14% lower CPL | n/a | [Meta Q3 2025](https://s21.q4cdn.com/399680738/files/doc_financials/2025/q3/META-Q3-2025-Earnings-Call-Transcript.pdf) (platform-stated) | 2025 |
| Advantage+ leads, 20 tests | 10% lower cost per qualified lead, 83% confidence | n/a | [Meta](https://about.fb.com/br/news/2025/02/impulsione-o-desempenho-da-sua-campanha-com-os-novos-recursos-de-ia-do-advantage-e-recomendacoes-testadas-e-comprovadas/) | Nov 2024 to Jan 2025 |
| Incremental attribution model vs standard | +24% incremental conversions | n/a | [Meta](https://about.fb.com/news/2026/01/2026-ai-drives-performance/) | Q4 2025 |

The two ecommerce ROAS figures (1.88x and 2.55x) are different samples, not a contradiction. `ecommerce-brand` uses the Triple Whale row.

### Cross-channel ecommerce cohorts with a top quartile ([Triple Whale live benchmarks](https://benchmark.triplewhalelabs.com/), rolling 90 days, updated Sep 2026)

| Vertical, metric | Median | Top quartile |
|---|---|---|
| Health and beauty CPA (extra-large cohort) | $33.44 | $16.77 |
| Gaming and apps CTR | 2.12% | 3.08% |
| Gaming and apps CVR | 1.82% | 5.50% |
| Gaming and apps CPA | $30.41 | $13.42 |
| Healthcare providers ROAS | 2.03x | 4.29x |
| Gaming and apps CPM / pets CPM / pharma CPM | $13.47 / $19.63 / $13.41 | not published |
| Pharmaceuticals and biotech ROAS | 0.75x | not published |

## Performance Max, Amazon, creators (measured, agency or vendor cohorts)

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| PMax ecommerce ROAS | 2.50x | about 2.80x | [Olifant](https://olifantdigital.com/blog/google-ads-benchmarks-ecommerce), 18 accounts US/EU/UK/CA | Nov 2025 to Oct 2026 |
| PMax ecommerce CVR | 2.7% | n/a | same | same |
| Amazon Sponsored Products ACoS | 38% | 25% (lower quartile) | [SellerPlex](https://sellerplex.com/amazon-ppc-benchmarks-2026/), 38 accounts | H1 2026 |
| Amazon CVR / CPC | 8.3% / $1.07 | 11.1% | same | same |
| Creator CPM (all / TikTok / YouTube) | $22.83 / $23.11 / $44.54 | n/a | [Kolect](https://www.kolect.ai/guides/influencer-rates), 120k+ collaborations | Aug 2025 to Oct 2026 |

## TikTok, Pinterest, Reddit, Nextdoor (platform-stated)

| Item | Value | Source | Year |
|---|---|---|---|
| TikTok Smart+ minimums | 6+ creatives, 7 days no disruptive edits, daily budget 10x CPA (30x with target CPA or min ROAS) | [TikTok](https://ads.tiktok.com/resources/help/article/best-practices-for-smart-plus-web-campaigns) | Apr 2025 |
| TikTok edits after learning | bids no more than 15% every 2 days; budget +30% if spending 90%+ | same | 2025 |
| TikTok learning | volatility falls after about 25 results or 7 days | [TikTok](https://ads.tiktok.com/resources/help/article/learning-phase) | Jun 2026 |
| Pinterest Performance+ | 50 conversions/week, daily budget 5x CPA, 10+ ads per ad group, about 2 weeks learning | [Pinterest](https://help.pinterest.com/en/business/article/pinterest-performance-plus) | 2026 |
| Pinterest A/B test budget (Americas) | about $825 to $18,000 per test version, 14+ days | [Pinterest](https://help.pinterest.com/en/business/article/create-and-manage-ab-tests) | 2026 |
| Reddit attribution default | 28-day click + 1-day view; ad group can overspend 20% | [Reddit](https://business.reddithelp.com/s/article/Web-Attribution-Overview) | 2026 |
| Reddit app budgets | 50x CPI for installs, 5x CPA for app events, 1 to 2 weeks learning | [Reddit](https://business.reddithelp.com/s/article/app-event-optimization) | 2026 |
| Nextdoor creative study | location copy +17% CTR, real imagery +10%, under 25% text +10%, no logo +22% | [Nextdoor](https://business.nextdoor.com/en-us/blog/creative-best-practices-for-maximizing-ad-effectiveness-on-nextdoor) | 2024, possibly dated |
| Nextdoor minimum | $5/day | [Nextdoor](https://business.nextdoor.com/en-us/local/advertise-with-nextdoor-hg-geo) | 2026 |

## Learning floors (planning numbers)

| Platform | Floor | Source |
|---|---|---|
| Google Smart Bidding | judge over 30 conversions, 50 for tROAS | [Google](https://support.google.com/google-ads/answer/7065882), 2026 |
| Google target changes | 1 to 2 conversion cycles to settle | Google Ads Help, 2026 |
| Google migrating offline to Enhanced Conversions | wait the longer of 3 conversion cycles or 4 weeks before making it primary | [Google](https://support.google.com/google-ads/answer/15479791), 2026 |
| Meta | about 50 optimization events per 7 days per ad set (app-ad guidance, directional) | [Meta](https://developers.meta.com/vr/resources/launch-ad-campaign/) |
| Meta CRM conversion optimization | 200+ leads a month, stage reached within 28 days, daily uploads | coreyhaines31 harvest, MIT |
| TikTok Smart+ | 10x CPA/day, 30x with targets | TikTok, 2025 |
| Pinterest Performance+ | 50/week, 5x CPA/day | Pinterest, 2026 |
| Microsoft Ads | tCPA 30+/month, Max Conversions 15+, tROAS 50+ | indranilbanerjee harvest, MIT, unverified |

## Creative (measured, observational)

| Metric | Value | Source | Year |
|---|---|---|---|
| Share of Meta creatives that become winners (10x account-median spend) | 5 to 8% | [Motion](https://go.motionapp.com/benchmarks-paid), 578,750 creatives, 6,015 accounts, $1.29B (reported by Motion, not independently checked) | 2026 |
| Hit rate by asset type | text-only 11.60%, product image with text 8.75%, UGC 7.56%, high production 6.97%, animation 4.57% | [Motion](https://runneth.com/thumbstop-pulse/creative-benchmarks-2026) (reported by Motion, not independently checked) | 2026 |
| Hit rate by visual structure | unboxing 9.83%, offer-first banner 8.68%, behind the scenes 8.64%, founder 8.57%, POV 8.28%, demo 8.11%, testimonial 6.57% | [Motion](https://runneth.com/library/formats/) (reported by Motion, not independently checked) | 2026 |
| Meta image generation tools | about +7% conversions (Meta aggregate) | Meta Engineering, Dec 2024, possibly dated | 2024 |
| RSA: second RSA in an ad group | +6.6% conversions at similar CPA; third RSA +3.7% | [Google](https://support.google.com/google-ads/answer/6167115) (platform observational) | 2026 |
| RSA Ad Strength | "Excellent" $28.68 CPA, 4.97% CVR vs "Average" $12.43 CPA, 12.65% CVR | Optmyzr, about 20,000 accounts, via r/PPC | 2026 |
| RSA pinning | 1 to 3 pins: $13.68 CPA, 365% ROAS; full pinning $32.57 CPA | Optmyzr via r/PPC | 2026 |
| AI Max full suite vs search-term matching only | +7% conversions or value at similar CPA/ROAS | [Google](https://support.google.com/google-ads/answer/15910187) | Apr 2026 |
| Enhanced Conversions for Leads vs standard offline import | median +10% recorded conversions (partly measurement recovery) | [Google](https://support.google.com/google-ads/answer/2998031) | 2026 |

## Landing pages, forms and calls (measured, observational)

| Metric | Value | Source | Year |
|---|---|---|---|
| Landing page CVR, median | 6.6% (industry medians 3.8 to 12.3%) | [Unbounce](https://unbounce.com/conversion-benchmark-report/), 41,000 pages, 464M visitors | Jul 2023 to Jul 2024, possibly dated |
| Reading level | 5th to 7th grade pages 11.1% vs professional-level 5.3% | same | same |
| Form CVR by field count | 1 field 18.2%, 2 13.0%, 3 11.5%, 4 9.9%, 5 8.1% | [NP Digital](https://neilpatel.com/marketing-stats/conversion-rate-by-form-fields/), 404 pages | Dec 2024 |
| Form starters who finish | 51.7% | [Zuko](https://www.zuko.io/form-statistics), 93M form views | Jan 2022 to Apr 2025 |
| Mobile load time | -1 s about +3% conversion; pages over 4 s 22% lower | Yottaa 2025 via [Shopify](https://www.shopify.com/blog/website-load-time-statistics) (vendor) | 2025 |
| Slow vs fast pages in Google Ads audits | 1.28% vs 3.65% CVR | operators report, r/DigitalMarketing | 2026 |
| Home services calls answered by a person | 52% (73% for calls over 30 s) | [Invoca](https://www.invoca.com/reports/the-invoca-call-conversion-benchmarks-report-home-services-2025) | 2026 |
| Answered paid-search calls that convert | 48% | same | 2026 |
| Store CVR by category | F&B 4.58%, beauty 5.32%, fashion 2.77%, home 1.29%, luxury and jewelry 0.63% | Dynamic Yield via Shopify | 2026 |

## Operators report (Reddit, self-reported, use as color, not targets)

| Number | Context | Thread |
|---|---|---|
| Meta CPM $9.71, 4.14x ROAS on $19.8k in 13 days, 4 campaigns | Canada ecommerce | r/FacebookAds, 59 upvotes |
| TOF ROAS just under 2, MOF 6, BOF 26, overall 8, break-even 3 | luxury decor, $300 to $1,000/day | r/FacebookAds, 156 |
| Purchase-optimized link click about $3 vs $0.30 on traffic campaigns | ecommerce | r/FacebookAds, 157 |
| Search Partners off: ROAS +15 to 25% | $50k to $150k/month accounts | r/googleads, 101 |
| Exact only + 500 negatives, no PMax: cost -60 to 70% | client accounts | r/googleads, 33 |
| Auto-created assets "often 40% worse" | Google | r/googleads, 101 |
| Hook rate (3-s views / impressions) over 30% is strong | Meta video | r/FacebookAds, 130 |
| CTR above 10% or a 40 to 50% gap between link clicks and landing page views = bot traffic | Meta | r/FacebookAds, 70 |
| Invalid sessions in one $1,800 test: Meta 92%, TikTok 10%, Google 1% | single product test | r/FacebookAds, 90 |
| Meta overreports conversions 15 to 30% vs server-verified results | Meta | r/FacebookAds, 337 |
| Purchase EMQ 9.3 good, under 6.0 investigate | Shopify | r/FacebookAds, 118 |
| Instant forms: 5 to 10% usable leads | high-ticket B2B | r/FacebookAds, 836 |
| Dental FB forms: $3,800, 166 leads, 58 booked (about $65 per booking) with a 5-touch follow-up | Switzerland dental | r/DigitalMarketing, 131 |
| Coaching Search $150/day: 43 booked calls at about $65, 7 clients worth $17.5k | executive coaching | r/lifecoaching, 187 |
| Pet waste removal: Facebook $30 to 50/day + Google $10 to 15/day = 2 to 5 leads/day | local service | r/sweatystartup, 529 |
| Roofing Search: about $60 CPC, about 21% landing page CVR | roofing to $2.2M revenue | r/DigitalMarketing, 114 |
| TikTok Shop GMV Max: $1,871 spend, 660 orders, $11,255 attributed (about 6x) in 7 days | TikTok Shop | r/TikTokshop, 51 |
| Ecommerce funnel ratios: add to cart to checkout 3:1 or better, checkout to purchase 2:1 or better; fix the site under 1% CVR | ecommerce | r/FacebookAds, 180 |

## What does not exist

No robust public benchmark for: Meta CPL by local trade, Nextdoor or Yelp CPL, TikTok lead CPL for local services, YouTube CPV for small advertisers, frequency thresholds by vertical, or a universal minimum daily budget. Say so instead of filling the gap. Unsourced tables in public skills (Meta CTR "0.8 to 1.2% average", "ROAS > 3x", "CPA < LTV/3") are directional at best.
