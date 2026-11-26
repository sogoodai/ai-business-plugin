# Benchmarks

Compare only inside the same conversion definition. Unbounce counts a page's configured goal (any form, click or signup), Littledata counts Shopify sessions with a purchase, Contentsquare counts instrumented conversion events across large sites. They are not interchangeable. "Top quartile" appears only where the source publishes it. Sources in [sources.md](sources.md).

## Landing pages by industry (Unbounce)

41,000+ landing pages, 464 million visitors, 57 million conversions, 2024 traffic. Vendor sample; possibly outdated by late 2026 but still the largest public set.

| Industry | Median | Top quartile floor | Notes |
|---|---|---|---|
| All industries | 6.6% | not published overall | |
| Professional services | 6.1% | 14.1% | Repair to consulting; intent varies sharply |
| Ecommerce landing pages | 4.2% | 11.4% | Landing pages, not whole-store purchase rate |
| SaaS | 3.8% | 11.6% | Goal may be trial, demo or form |
| Travel and hospitality | 4.8% | 15.6% | Accommodation 3.7%; transport and travel services 14.8% |

**By traffic source and device, professional services (Unbounce 2024):** email 13.9%, Instagram ads 11.7%, YouTube ads 1.2%, paid social overall about 4.4%; 81% of visits mobile, mobile 8.3% vs desktop 11.6%. **Ecommerce:** email 28.6% median.

**By reading level, professional services (Unbounce 2024):** 5th to 7th grade copy 12.9% median vs 8th to 9th grade 6.6%. All-industry figures in sibling `paid-ads`: 11.1% vs 5.3%. Correlation, but consistent across categories.

## Online stores

| Metric | Median | Top 20% | Top 10% | Source |
|---|---|---|---|---|
| Session to purchase | 1.3% | 2.8% | 3.6% | Littledata, November 2026, 450 Shopify stores (each with 1,000+ sessions and 90+ purchases) |
| Add to cart rate | 6.9% | 13% | 17% | Littledata, November 2026 |
| Checkout completion | 47% | 64% | 73% | Littledata, November 2026 |
| AOV | $111 | $305 | $611 | Littledata, November 2026 |
| Revenue per session | $1.93 | $4.12 | $6.76 | Littledata, November 2026 |
| Cart abandonment | 70.22% average | | | Baymard, October 2026 (50 studies, 2006 to 2025) |

Store conversion by category (Shopify / Dynamic Yield 2026, cited in `ecommerce-brand`): beauty 5.32%, food 4.58%, fashion 2.77%, home 1.29%, jewelry 0.63%. Compare a store with its category, never with "2 to 3%".

## Visitors and channels (Contentsquare 2026)

99 billion sessions, 6,500+ sites, Q4 2024 vs Q4 2025. Enterprise-skewed.

| Metric | Value |
|---|---|
| Returning visitor conversion | 2.9% (52.8% of traffic), down 4% YoY |
| New visitor conversion | 1.7%, down 8% YoY |
| Overall conversion | down 5.1% YoY, with lower traffic and engagement |
| AI-referral conversion (ChatGPT, Perplexity and similar) | 1.3%, up 55% YoY; AI traffic up 632% but still a small share |
| Organic social conversion | 0.7% |

Organic search conversion medians from sibling `seo-content`: 3.3% (SmartSites) and 4.9% average (Ruler), 2026.

## Forms and lead capture

| Metric | Value | Source |
|---|---|---|
| Conversion by number of form fields | 1 field 18.2%, 2 13.0%, 3 11.5%, 4 9.9%, 5 8.1% | NP Digital, 404 pages, 2024 |
| Form starters who finish | 51.7% | Zuko form analytics |
| Shoppers reluctant to give a phone number at checkout | 68% | Baymard 2026 |
| Test users who missed a required field when only optional fields were marked | 32% | Baymard 2026 |
| Demo request form cut from 9 to 3 fields plus hero and CTA changes | +42% leads (lead quality warning) | Optimizely, January 2026 |
| Clearer demo page and form | +18.9% leads | Optimizely, January 2026 |
| Visual preview of a gated asset | +47% submissions at 99% significance | Optimizely, January 2026 |
| Scheduler embedded in the inbound form | Form-to-booking about 50% to 80%+, meetings +71%, time to meeting -63% | Chili Piper / NetSPI case, 2026 (vendor) |
| Same, ChowNow | Speed to lead from about a week to instant; close rate on those meetings 4x | Chili Piper case (vendor, no baselines) |

## Calls and speed to lead (from sibling `paid-ads` research)

| Metric | Value | Source |
|---|---|---|
| Inbound home-service calls that reach a person | 52% | Invoca 2026 |
| Answered paid-search calls that convert | 48% | Invoca 2026 |
| Home service businesses replying within an hour | 20% | Jobber 2026 |
| Consumers expecting a form reply within an hour / getting one | 57% / 41% | cited in local services research, 2026 |

## Chat

| Case | Result | Grade |
|---|---|---|
| Mindbody AI sales chat, January 2026 | MQL to SQL +10.3% vs control; 4,300+ chats and 130 qualified meetings in Q1 2026 | Controlled A/B, vendor-published (Spara) |
| Body Glove Hawaii boat tours, 2025 | Chat users 6.34% conversion vs 1.9% sitewide; $874,000 "attributed" revenue; 1,600+ conversations | No control: self-selection (TOMIS, vendor) |

## Speed

| Case | Result | Grade |
|---|---|---|
| Rakuten 24 | Revenue per visitor +53.37%, conversion +33.13% after CWV work | A/B test, one month |
| Ray-Ban prerendering | Mobile conversion +101.47%, desktop +156.16% | A/B on supporting browsers, January 2025 |
| Nuvemshop | Mobile organic conversion +8.9% as LCP-good rose 57% to 96% | Same-cohort before and after, June 2026 |
| Yottaa 2025 | 1 s faster about +3%; over 4 s, 22% lower | Vendor observational |

More cases in [speed-and-mobile.md](speed-and-mobile.md).

## Trust and reviews

| Metric | Value | Source |
|---|---|---|
| Consumers trusting online reviews as much as personal recommendations | 42% (79% in 2020) | BrightLocal, January 2025 |
| Shoppers abandoning because they did not trust the site with card details | 19% of actionable abandoners | Baymard 2026 |

## Operator-reported numbers (Reddit; useful lines, not benchmarks)

| Number | Context | Thread |
|---|---|---|
| Popup signup 8% floor, 18% best | Shopify stores $40k to $90k a month | r/shopify, 181 |
| Popup 2.8% to about 7% | 50+ versions over 7 months | r/ecommerce, 29 |
| Spin-to-win 7% to 9% opt-in | Wheelio, exit intent only in one case | r/shopify, 160 and 83 |
| Add to cart to checkout 3:1, checkout to purchase 2:1 | Meta ad triage across 40+ businesses | r/FacebookAds, 180 |
| Initiated checkout to purchase under about 50% | Checkout friction alarm | r/shopify, 81 |
| Landing page view to content views 1:3 | Browsing engagement check | r/shopify, 81 |
| Paid roofing search pages about 21% at about $60 CPC | Dynamic "[term] service in [city]" headlines | r/DigitalMarketing, 114 |
| Coaching single-service page about 17% from paid | 43 booked calls in 3 to 4 weeks | r/lifecoaching, 187 |
| B2B blog modals and demo forms never over 1% | 15-year B2B marketer | r/DigitalMarketing, 222 |
| Contact form to 5-question quiz: 2.5% to 9.3% | B2B, 3 months | r/LeadGeneration, 16 |
| 15-field form to progress-bar quiz: CPL €19 to €4 | Insurance, ads unchanged | r/PPC, 87 |
| Affiliate outbound CTR over 50% | Top pick early plus summary table | r/SEO, 441 |
| Google Play listing visitors to installs under 40% = fix the listing | App store pages | r/androiddev, 335 |

## Numbers to ignore

Several public CRO skills and blogs repeat precise-looking tables with no source: "paid traffic converts 2 to 3x organic", "mobile converts 30 to 50% lower", "the first screen decides whether 60 to 80% stay", "2 to 3 s load costs 7%, 3 to 5 s costs 20%", "6+ fields cost 40 to 80%", "multi-step forms lift 20 to 40%", "email popups convert 2 to 5%, exit intent 3 to 10%". None carries a dataset or a year. Do not quote them to an owner. Use the sourced figures above or say no robust benchmark exists.

Also treat with care: "37% abandon when phone is required", "11 to 4 fields = +120%", "trust badges +16% (new visitors +22%)", "inline validation 22% fewer errors". These circulate as an IvyForms summary of older studies (r/web_design, 85 upvotes), many from 2008 to 2015 tests. Directionally consistent with Baymard; numerically dated.

## Gaps with no robust current benchmark

Booking widget completion rate by industry, click-to-call to booked job rate for small sites, chat-to-booking conversion for local services, the right deposit size, quiz funnel conversion by vertical, AI-referral conversion for local services. Say so instead of inventing one, and build the owner's own baseline in the first two weeks.
