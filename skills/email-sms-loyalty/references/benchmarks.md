# Benchmarks

Read before comparing anything: "conversion", "revenue per recipient", "open" and even "click" are defined differently by each vendor. Postscript EPM, Klaviyo RPR, Omnisend revenue per email and Chatarmin revenue per WhatsApp message never go in one leaderboard. Build a baseline per vendor, then compare channels with your own holdout. "Top 10%" is not a 75th percentile; this file never converts one into the other. All vendor data is a customer cohort with vendor-controlled attribution.

## Email by vertical

| Population | Open | Click | Unsub | Upper benchmark | Source | Year |
|---|---|---|---|---|---|---|
| Ecommerce campaigns (Klaviyo) | 31.0% | 1.69% | n/a | 45.1% / 3.38% top 10% | Klaviyo benchmarks | 2026 |
| Ecommerce flows (Klaviyo) | 32.2% | 5.58% | n/a | 45.8% / 10.48% top 10% | Klaviyo | 2026 |
| Ecommerce campaigns (Mailchimp) | 29.81% | 1.74% | 0.19% | n/a | Mailchimp benchmark page | accessed Nov 2026 |
| Education and training (Mailchimp) | 35.64% | 3.02% | 0.18% | n/a | Mailchimp | accessed Nov 2026 |
| Jobs and education campaigns (Omnisend) | 39.55% | 0.58% CTR | n/a | n/a | Omnisend | 2025 sends, pub. 2026 |
| Food and drink campaigns (Omnisend) | 30.03% | 0.96% CTR | n/a | n/a | Omnisend | 2025 sends |
| Beauty and fitness campaigns (Omnisend) | 29.33% | 0.72% CTR | n/a | n/a | Omnisend | 2025 sends |
| Beauty and wellness campaigns (Phorest users) | 44% | 1.7% | n/a | 4.2% click-to-book | Phorest via PBA, 530+ businesses, 4M emails | 2025 data, pub. 2026 |
| Restaurant (Toast customers) | about 39% | n/a | n/a | n/a | Toast | 2026 |
| Restaurant (third-party benchmark shown by Toast) | 21.7% mean, 17.9% median | 2.1% | n/a | 8.5% CTOR | Toast support | Oct 2026 |
| Home and local services | no sourced benchmark | | | | | |

Public skills quote 43% average open and 2.2% click across industries (AgriciDaniel claude-email, MIT) with no data source. Do not use them as targets. When Apple Mail is over 40% of opens, weight clicks and click-to-open instead (same file, reasonable rule).

## Revenue per recipient and per send

| Flow or campaign | Typical | Upper | Source | Year |
|---|---|---|---|---|
| Campaign, Klaviyo, $1 to $1M revenue, $44 to $83 AOV | $0.11 median | $0.29 p75 | Klaviyo Help (percentiles) | Oct 2026 |
| Cart flow, same band | median not exposed | $2.91 p75 | Klaviyo Help | Oct 2026 |
| Cart flow, $1M to $5M brand, $83 to $112 AOV | $2.39 p25 | $5.86 p75 | Klaviyo Help | Oct 2026 |
| Cart flow, $1M to $5M, $163 to $291 AOV | $6.00 p25 | $16.40 p75 | Klaviyo Help | Oct 2026 |
| Abandoned-cart email, all Klaviyo | $6.77 RPR, 6.0% click | $13.70, 11.3% click (top 10%) | Klaviyo, 110k+ customers | 2026 |
| Welcome email, all Klaviyo | $5.75 RPR, 6.5% click | $13.27, 13.3% click (top 10%) | Klaviyo | 2026 |
| Automated email, Omnisend | 30.21% open, 4.66% CTR, 1.49% conv, $3.41 per email | n/a | Omnisend benchmark report | 2025 data |
| Scheduled campaign, Omnisend | $0.155 per email | n/a | Omnisend benchmark report | 2025 data |
| Automated vs campaign, Omnisend ecommerce report | $2.87 vs $0.18 per send; 2% of sends, 30% of revenue | n/a | Omnisend 2026 Ecommerce Marketing Report, 150k brands | 2025 data |
| Welcome automation, Omnisend | 35.53% open, 3.94% CTR, 2.11% conv, $6.16 per email, 0.87% unsub | n/a | Omnisend | 2025 data |
| Back-in-stock email, Omnisend | 58.80% open, 21.31% CTR, 6.72% conv, $9.14 per email; used by 0.6% of brands | n/a | Omnisend | 2025 data |
| Restaurant welcome vs blast | $1,506 vs $80 per 1,000 delivered | n/a | Bloom Intelligence | Jan 2025 to Aug 2026 |

The two Omnisend figures come from two reports on the same year; quote the one matching the dataset you cite. RPR scales with AOV: always use the row for the business's revenue band and AOV.

## Restaurant CRM return rates (Bloom, verified return visits)

| Campaign | Return rate | Caveat |
|---|---|---|
| One-off blast | 0.27% | |
| New-guest welcome | 7.2% | about 27x a blast |
| At-risk win-back | 6.5% | depends on lapse definition |
| Visit milestone | 19.8% | milestone guests already high-propensity |
| Post-visit | 29.9% | Bloom warns selection inflates it |

Source: Bloom Intelligence, Jan 2025 to Aug 2026, US and Canada network, vendor attribution.

## SMS

| Metric | Value | Status | Source | Year |
|---|---|---|---|---|
| Abandoned-cart SMS | 17.28% CTR, 7.84% CVR, $10.95 EPM | p75 | Postscript | 2026 |
| Back-in-stock SMS | 58.70% CTR, 13.80% CVR, $13.34 EPM | p75 | Postscript | 2026 |
| Campaign SMS | 8.01% CTR, 0.54% CVR, $0.55 EPM, 0.88% unsub | p75 | Postscript | 2026 |
| Revenue per message, all | $1.03 median, $2.07 p75 | percentiles | Postscript | 2026 |
| SMS campaigns | 12.39% CTR, 0.12% conv, $0.15 per SMS, 96.6% deliverability | average, 246M+ sends | Omnisend | 2025 data |
| US SMS campaign "good" | 8.9 to 14.5% click, 1.0 to 2.0% CVR | vendor rating | Klaviyo Help | 2025 to 2026 |
| US SMS campaign "great" | 14.6%+ click, 2.1%+ CVR, $2.42+ RPR | vendor rating | Klaviyo Help | 2025 to 2026 |
| Copy effect | components move conversion +19% to -24%; superlatives -11.4%, jargon -7.8% CVR in non-offer sends | model on 25B+ messages | Attentive | May 2026 |
| Healthcare reminders | attendance RR 1.11 (10 RCTs, 8,236 people); adding an automated call to SMS cut no-shows 11.3% to 9.6% (59,994 patients) | randomized | JHMH Policy review; RCT | 2026 |

Operator reports, not benchmarks: SMS revenue grew from under $600 to $18,000 a month with short copy and simple flows (28-pt thread); SMSBump $25.11 spend attributed $152.76 (160-pt thread). Public skills' "SMS 98% open" and "SMS subscribers 1.5 to 3x LTV" are uncited; do not repeat them.

## WhatsApp

| Metric | Value | Source | Year |
|---|---|---|---|
| Campaign open | 72.05% median brand, 79.6% message-weighted | Chatarmin, 382 brands, 49.3M messages | Mar to May 2026 rates, pub. Sep 2026 |
| Campaign click | 12.0% | Chatarmin | 2026 |
| Campaign opt-out | 0.34% | Chatarmin | 2026 |
| Attributed revenue | EUR 1.03 per campaign message (24-hour window, includes view-through) | Chatarmin | 2026 |
| Utility-first then offer, A/B on 20,000 customers | offer conversion 0.17% to 0.37%, click 4.36% to 7.18%, return on messaging spend 1.36x to 2.5x | Spur, Golden Tree case | 2026 |

Costs per message by country: [whatsapp.md](whatsapp.md).

## Capture

| Metric | Value | Status | Source | Year |
|---|---|---|---|---|
| Popup submit rate | 1.30% median, 2.67% p75 | 2,305 popups | Poptin | Jan to Sep 2026 |
| Popup submit rate | 2.3% median; 3%+ recommended | vendor | Klaviyo Help | 2026 |
| Discount / gamified / multi-step popup | 8.62% / 10.15% / 5.64% average | vendor customer base | Wisepops | 2025 to 2026 |
| Delayed popup (20 to 50 s) | +20 to 43% capture, up to 45% lower bounce | vendor A/B compilation | Wisepops | 2025 to 2026 |
| List growth | 1 to 3% a month "healthy" | operating target, weak source | Klaviyo Academy citing AgencyAnalytics | 2026 |
| Restaurant pre-launch signups | 1,200 at about $0.50 each over 45 days | agency case | Debox | 2025 |

Operator reports: 2.8% to about 7% signup (best 8.2%) after 50+ popup versions in 7 months (28-pt thread); 9% with a spin wheel (160-pt); about 10% instant popup (3-pt comment); 96% completion of four questions after the email field (181-pt); about 25% of discount signups are repeat people (13-pt comment, brands with 10k+ signups a day).

## Loyalty, memberships and repeat

| Metric | Value | Caveat | Source | Year |
|---|---|---|---|---|
| Restaurant return, loyalty vs baseline | near 30% vs 7% | self-selected | Toast Regulars Report | Q1 2026 data |
| Casual dining cashback 90-day retention | 24 to 26% | observational | Toast | 2026 |
| Fine dining item reward vs cashback | 20% vs 13% retention | observational | Toast | 2026 |
| Loyalty 90-day active rate | strongest segments 66 to 72%; casual dining under 50%; bar and grill down 13% YoY | 800+ brands, 225M profiles | Paytronix | 2025 data, 2026 report |
| QSR members vs non-members | +40% spend per visit, +64% frequency | survey of 450+ decision-makers | Square | 2025 |
| Square Loyalty sellers | +40% visit frequency | vendor association | Square | 2025 to 2026 |
| Salon membership businesses | sales +8% vs +2%; existing-guest visits +12% vs +3% | observational | Zenoti | 2025 data |
| Med aesthetics members | retention 90.4% vs 50.6%; spend 1.70x; penetration 26.6% median | authors call it an upper bound | CorralData | Q3 2026 |
| Salon rebooking target | 60%+ healthy, under 40% warning | vendor guidance | Vagaro | 2026 |
| Beauty average inter-visit gap | about 63 days | blended | Mangomint | 2026 |
| Endowed progress punch card | 34% vs 19% completion (10-stamp card with 2 pre-stamped vs 8-stamp blank, both needing 8 purchases; 300 cards) | field experiment, car wash, 2004 | Nunes and Dreze, Journal of Consumer Research | 2006 |
| Shopify repeat purchase rate, under $1M | 16.3% median, 25.8% p75 | 1,326 stores | By the Numbers | Sep 2025 to Aug 2026 |
| 365-day repeat by category | coffee/tea 31.7% (p75 41.6%), skincare 24.9%, cosmetics 22.1%, specialty food 21.7%, clothing 19.1%, jewelry 16.9%, decor 13.0%, shoes 12.3% | cohort | By the Numbers | 2025 to 2026 |
| Wholesale reorders | 70% within 90 days; 5th order = about 2.5x long-term loyalty; cadence about 45 days | marketplace operator | Faire | 2026 |
| Trades maintenance agreements | 30% service-call-to-agreement target; 80% tune-up-to-agreement | vendor targets, partly pre-2024 | ServiceTitan | legacy |
| Homeowners expecting a service plan | 51%; 43% appreciate reminders | stated preference | Housecall Pro | 2025 |
| Music school students still studying after a year | 47%; only 6% of cancellations cite cost | vendor cohort | Opus1 | 2026 |

## Referrals

| Metric | Value | Caveat | Source | Year |
|---|---|---|---|---|
| Referrals as top lead source, home services | 59% of owners (repeat work also 59%) | survey | Jobber | 2026 |
| Contractor referral rate | 2 to 10%, 4 to 6% conversion | third-party quotes, weak | Housecall Pro | 2026 |
| Capacity-targeted salon referral certificates ($50 off $250+ for stylists under 70% productivity) | +10% new clients | single operator | Salon Today 200 | 2025 |
| Structured salon referral launch | 172 referrals in month one | vendor case | Zenoti, Willo Salons | 2025 to 2026 |

Public skills' referral numbers (referred customers 16 to 25% higher LTV, K-factor 0.3 to 0.5 "strong", share rate over 5%) are uncited. Use them as hypotheses only.

## Measurement fields to store

`delivered, unique_clickers, replies, orders_or_bookings, net_revenue, discount_cost, message_cost, unsubs, spam_complaints, new_subscribers, signup_source, attribution_window`. Vendor dashboards are not truth: Chatarmin attributes via coupon, click, UTM or chat within 24 hours, which includes view-through.
