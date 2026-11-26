# Benchmarks

Treat these as priors, not targets. Three kinds of numbers, kept apart:

- **Measured:** randomized experiments, platform documentation, large GSC or analytics datasets. Most SEO datasets come from tool vendors or agencies analyzing their own customers: big samples, selection bias. Flagged "vendor".
- **Case study:** one program, one site. Shows what is possible, not what to forecast.
- **Operators report:** Reddit practitioner numbers. Real, anecdotal.

"Year" is the year the data describes; publication year follows when different. Where no credible top-quartile number exists, the table says so. Never invent one. URLs in [sources.md](sources.md).

## Clicks and CTR

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Google organic CTR, position 1 | 4.72% median | not published | SmartSites, 910 GSC properties (vendor) | Oct 2025 to Sep 2026 |
| CTR, position 2 | 1.90% median | not published | SmartSites (vendor) | 2025 to 2026 |
| CTR, position 10 | 0.22% median | not published | SmartSites (vendor) | 2025 to 2026 |
| Share of a site's Google clicks from positions 1 to 3 | 71% median | n/a | SmartSites (vendor) | 2025 to 2026 |
| Outbound organic clicks when an AI Overview appears | -39.8% | n/a | Agarwal and Sen, randomized field experiment | 2026 |
| Zero-click searches when an AI Overview appears | +34.5% | n/a | Agarwal and Sen | 2026 |
| External CTR, AI Mode forced vs normal | -18.8 points | n/a | Wang et al., preregistered experiment, N=1,100 | Mar 2026 |
| External CTR, AI features hidden vs normal | +8.8 points (underestimate: only about half of AIOs were hidden) | n/a | Wang et al. | Mar 2026 |
| Result clicks, visits with vs without AI summary | 8% vs 15% | n/a | Pew, 900 US adults (observational) | Mar 2025, pub. Jul 2025 |
| Clicks on a citation inside the AI summary | about 1% of visits with one | n/a | Pew | Mar 2025 |
| Searches showing an AI summary in Pew's panel | 18% | n/a | Pew | Mar 2025 |
| Position-1 CTR when an AIO shows vs modeled counterfactual | -58% | n/a | Ahrefs (vendor, observational) | Dec 2025 data, pub. Feb 2026 |
| Same metric, earlier run | -34.5% | n/a | Ahrefs (vendor) | Mar 2025 data, pub. Apr 2025 |
| CTR on queries with an AIO | 1.76% to 0.61% | n/a | Seer Interactive clients (vendor; queries already had lower CTR before AIOs) | Jun 2024 to Sep 2025 |
| Growth in Google searching for query types showing AIOs | more than +10% (US, India) | n/a | Google (platform's own figure) | May 2025 |

Rule: forecast informational traffic at 40 to 60% of historical CTR curves when the query shows an AI Overview. Commercial and navigational queries hold up better.

## Conversion from organic

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Google organic conversion rate, cross-industry | 3.3% median | not published | SmartSites, 1,159 client sites (vendor) | Oct 2025 to Sep 2026 |
| Paid search conversion rate, same dataset | 3.4% median | not published | SmartSites | 2025 to 2026 |
| Organic share of conversions vs share of visits | 29% of conversions from 21.5% of visits (medians) | n/a | SmartSites | 2025 to 2026 |
| Organic conversion rate, all industries | 4.9% average | not published | Ruler Analytics, 5M+ conversions (vendor; conversion definitions vary) | pub. 2026 |
| Organic conversion, software | 7.9% average | not published | Ruler Analytics | 2026 |
| Organic conversion, professional services | 8.1% average | not published | Ruler Analytics | 2026 |
| Organic conversion, retail and ecommerce | 2.0% average | not published | Ruler Analytics | 2026 |
| Comparison pages vs category blog posts | 3.8x conversion | n/a | Cemafor, one SaaS (case study) | 2025 |
| Share of content conversions from 3 product-led hubs | 97% | n/a | Minuttia, Meilisearch (case study) | Jan 2025 to Jul 2026 |

Ruler counts leads (forms, calls) as conversions; SmartSites counts each client's key events. Compare a business only with its own definition over time.

## Time to rank and traffic per site size

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| New software articles, time to first Google impression | 10 days median | n/a | murkuz, 633 articles on 9 sites (observational GSC cohort) | Jul 2025 to Sep 2026 |
| Time to first page-one week | 154 days median | n/a | murkuz (includes long-tail queries) | to Oct 2026 |
| New articles with a page-one week | 38% by day 90; 54% by day 180 | n/a | murkuz | 2025 to 2026 |
| New URLs reaching a tracked top 10 within a year | 1.74% broad sample; 6.11% filtered English content | n/a | Ahrefs, 1M URLs (vendor) | pub. May 2025 |
| Of pages that ranked top 10, share that did so within a month | 40.82% | n/a | Ahrefs (vendor) | pub. May 2025 |
| Monthly organic clicks, sites with 10 to 50 indexed pages | 97 median | not published | Ahrefs, 344,956 sites with GSC data (vendor) | Jun 2026 |
| 50 to 100 indexed pages | 400 median | not published | Ahrefs | Jun 2026 |
| 100 to 200 indexed pages | 945 median | not published | Ahrefs | Jun 2026 |
| 200 to 500 indexed pages | 2,463 median | not published | Ahrefs | Jun 2026 |
| Sites at Ahrefs DR 20 to 30 | 133 median monthly clicks | not published | Ahrefs (DR is Ahrefs' metric, not Google's) | Jun 2026 |
| Pages with zero estimated Google traffic | 96.55% | n/a | Ahrefs, 14B pages, modeled traffic (Dec 2023: possibly outdated) | 2023 |

Rule: judge a new page at 90 and 180 days, not at 30. If it has no impressions after 6 months, intervene (rewrite, merge, relink or drop), per Ahrefs' own advice.

## Technical

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Sites with good Core Web Vitals | 48% mobile, 56% desktop | n/a | HTTP Archive Web Almanac | 2025 |
| "Good" thresholds (p75 of real users) | LCP 2.5 s, INP 200 ms, CLS 0.1 | n/a | web.dev | updated May 2025 |
| Sitemap optional below | about 500 pages with good internal links | n/a | Google docs | current |
| OpenAI crawler policy change propagation | about 24 hours | n/a | OpenAI docs | current |

## Links and digital PR

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Links per digital PR practitioner per month | 15.58 weighted average | about a third report 31+ | BuzzStream survey (self-report) | 2025 |
| Practitioners who never pay for placements | 87.3% | n/a | BuzzStream | 2025 |
| Cost per digital PR link | mostly $300 to $750 (over half do not know their own) | no reliable quartile | BuzzStream | 2025 |
| Practitioners rating digital PR the most effective tactic | 48.6% | n/a | Editorial.Link, 518 practitioners (opinion) | 2026 |
| Prefer unique opportunities over copying competitor links | 66.6% | n/a | Editorial.Link | 2026 |
| Link-earning by format vs page share (B2B) | stat roundups 4.25x, glossaries 1.47x, calculators 1.38x, how-tos 1.36x, original research 0.80x, ultimate guides 0.77x | n/a | Foundation Inc., single vendor (via coreyhaines31/marketingskills, MIT) | Mar 2026 |

## Content operations

| Metric | Typical | Top quartile | Source | Year |
|---|---|---|---|---|
| Refreshed pages vs untouched controls, 90 days | 610 to 3,341 sessions (95 pages) vs controls -20.2% | n/a | Workshop Digital (agency, selected cohort; do not forecast from it) | pub. May 2026 |
| Internal-link uplift, 10 links added per page | +15.1% daily clicks vs untreated, +19.4% vs control states | n/a | Quattr, about 50,000 pages, controlled (vendor, large legal site) | 2025 |
| Pruning: removed 198 of 600 URLs (3.1% of clicks) | GSC clicks +37%, sessions +55% four months later | n/a | Search Engine Land case study (uncontrolled) | 2024 to 2025 |
| Topical depth, deepest vs shallowest quartile | average position 9.5 vs 13.5; top-3 reach 20% vs 4% | n/a | 510 sites, 41 commercial SERPs (observational) | 2026 |
| Correlation of topical depth with position | 0.329, or 0.277 controlling for links and size | n/a | same | 2026 |
| Contextual blog-to-pricing or demo links on the typical site | zero | n/a | same crawl | 2026 |
| Programmatic: 1,125 distinct template pages | 4,863 monthly search clicks (3,591 Google, 1,272 Bing) after 7 months | n/a | SEO Savages, Prawomat (case study) | 2025 |

## Operators report (Reddit, anecdotal)

See the operator numbers inside each playbook file, each with its thread, and the full thread list with upvotes in [sources.md](sources.md).
