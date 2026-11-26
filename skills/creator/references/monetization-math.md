# Monetization math

Formulas and worked examples for every creator revenue line. Benchmarks with full sources: [benchmarks.md](benchmarks.md). Pricing psychology for products and memberships: sibling `offers-pricing`; product building: `digital-products` and `education-coaching`.

## The master formula

```
revenue per 1,000 audience members (or per 1,000 views) =
    ad revenue (RPM)
  + sponsorship revenue
  + affiliate: EPC x clicks
  + product: conversion x AOV
  + subscription: conversion x LTV
  + services: leads x close rate x gross margin
```

Optimize the largest marginal term, not the easiest dashboard (research report, 2026). In most reported creator businesses the ad line is the smallest: $1,841 AdSense against $120,000 of offer revenue on a 5,900-subscriber channel; $9,020 ads against $100k+ community sales; under $1,000 AdSense against $20,000+ affiliate (r/PartneredYoutube 185 and 219 pts; r/youtubers 74 pts).

## Pick the primary model by audience intent

| Audience intent | Primary model | Secondary |
|---|---|---|
| Broad entertainment | Platform ads + sponsorships | Merch, memberships |
| High-trust product discovery (reviews, comparisons) | Affiliate | Sponsorships, display |
| Specialist professional knowledge | Services, courses, paid newsletter | Sponsorships (high CPM) |
| Community identity | Membership, live events, merch | Sponsorships |
| Frequent proprietary information (data, deals, alerts) | Paid newsletter or data product | Sponsors |
| Music fandom | Tickets, merch, direct-to-fan | Streaming, sync |

Source: research report's mechanism-to-intent mapping (2026). Creators use 2 to 3 income strategies on average (impact.com, 421 creators, 2025, vendor). A US survey of 1,000 creators put ad revenue at 21.6% of income, platform payouts 13.3%, brand partnerships 12.7%, products, merch and affiliate 21.2% (Influencer Marketing Factory and HypeAuditor, Jan 2026). Do not merge the two surveys. Add a second line only once the first is measurable.

Rule from a 600k-subscriber creator: before quitting a job, build 3 to 4 income sources each at least equal to AdSense (r/PartneredYoutube, 297 pts).

## YouTube ad revenue

```
expected ad revenue = expected views / 1,000 x channel RPM
RPM (creator) = total channel revenue / total views x 1,000   (after YouTube's share)
long-form share to creator: 55% of net ad revenue; Shorts: 45% of the creator pool allocation
Shorts equivalence: 11,000 to 34,000 Shorts views earn what 1,000 long-form views earn (AIR, Sep 2026)
```

Worked example: an education channel at the AIR niche median of $10.22 RPM and 200,000 monthly long-form views makes about $2,044 a month from ads. The same views in gaming at $2.05 make about $410. One sale of a $1,000 course equals the ad revenue of about 98,000 education views or 488,000 gaming views. That ratio is why commercial-topic creators model revenue per qualified viewer, not RPM.

RPM moves with: audience country (US $5.12, UK $4.65, Canada $5.04, Australia $7.08, Germany $1.37, India-heavy channels far lower; Dynamoi, 74 markets, Oct 2026), video length and mid-roll count (11 min $708 vs 23 min $877 at the same views, r/PartneredYoutube, 152 pts), TV share, Q4 seasonality, and Shorts share of views.

## Sponsorship pricing

```
base fee = forecast views / 1,000 x target CPM
forecast views = median 30-day views of the last 10 to 12 comparable posts (never followers)
total quote = base x integration multiplier + paid usage + whitelisting + exclusivity + extras
paid usage per 30 days = base x 15 to 35%          (Aspire 2026)
twelve months of paid usage at 25% per 30 days = base x 3.0
```

Full tables and the worked example: [brand-deals.md](brand-deals.md).

Check the deal against the creator's alternatives: `effective hourly = fee / (scripting + filming + editing + revisions + admin hours)`. A deal under the creator's floor hourly rate is declined or rescoped.

## Affiliate

```
EPC = commissions / clicks
expected monthly affiliate revenue = monthly clicks x EPC
page value = monthly pageviews x link CTR x EPC
break-even CPC for paid traffic = EPC x (1 - target margin)
recurring commission value = monthly commission x expected customer months (cap at program's limit)
```

Measured EPC benchmarks are network data (Aragon Premium, Sep 2026, banded, the network sells traffic): refinance $8 to $10; personal finance $2 to $3; debt about $1; loans $0.50 to $0.75; insurance about $0.50. Operator-reported site economics: $80 to $100 per 1,000 visits on buyer-intent posts; site RPM $19 to $44 after adding comparison tables (r/Affiliatemarketing, 28 and 122 pts). Depth: [affiliate.md](affiliate.md).

Worked example: a review channel gets 3,000 link clicks a month on a camera kit at 4% conversion and a $1,200 average order at 3% commission. EPC = 0.04 x 1,200 x 0.03 = $1.44; monthly = $4,320. Moving the same clicks to a direct program at 8% raises EPC to $3.84. Compare with an operator rule: pick products paying $5 to $10 net per sale or more (r/PartneredYoutube, 528 pts).

## Newsletter

```
paid subs = engaged free list x conversion             (beehiiv median 0.62%, top quartile about 2 to 5%)
paid LTV  = monthly price / monthly churn              (beehiiv median LTV $83 to $230 by vertical)
free subscriber value per year = conversion x paid LTV x margin + sponsor revenue per subscriber per year
max CPA = free subscriber value x payback share        (e.g. 50%)
sponsor revenue per issue = active subs / 1,000 x CPM  (or median clicks x CPC)
```

Worked example: a finance letter with 10,000 engaged free readers, 1.5% conversion, $20 a month, 8% monthly churn: 150 paid; LTV = 20 / 0.08 = $250; free subscriber value = 0.015 x 250 = $3.75 from paid alone, plus sponsors at $40 CPM weekly (10 x $40 x 52 / 10,000 = $2.08 per subscriber per year). Value about $5.80 per subscriber; at 50% payback, buy subscribers up to about $2.90. SparkLoop's $1 to $5 range and operators' $0.31 to $0.65 Meta lead forms fit; $5 placements do not. The research report's rule is the same: `maximum CPA = gross-margin LTV x desired payback fraction`, computed by source, never blended.

## Podcast

```
direct sponsorship per episode = 30-day downloads / 1,000 x CPM x number of reads
Spotify Partner Program = 50% of recognized revenue on Spotify-sold ads (+ Premium video payouts)
niche value check = listeners in sponsor ICP x sponsor's value per qualified prospect
```

Worked example: 2,000 downloads at 30 days, two host reads at $25 CPM: 2 x 2 x 25 = $100 an episode. The same 2,000 listeners as founders of B2B software companies can justify a flat $500 to $1,000 to a vendor whose customer is worth thousands, if a listener survey proves the audience.

## Music

```
streaming revenue = streams x effective per-stream rate (from the artist's own statements, by platform and country)
ad payback = (streaming revenue + follower value + email value + attributed tickets and merch) / ad spend
cost per real listener = spend / new Spotify listeners (not platform conversions)
```

Return per $1 of ads by offer, one marketer across $5M: tours about $10, appearances about $6, merch about $5, recorded music about $0.50 (r/musicmarketing, 521 pts). Build the campaign around the high-return offer, use streams as the funnel.

## Products and the value ladder

Across 101M Kajabi transactions ($11.7B, to Aug 2026): $97 is the most common price; products under $25 are 14.8% of listings but 3.5% of earnings; offers at $1,000+ are 15% of listings and 40% of earnings; business and finance one-time products median $275 vs $89 for lifestyle and hobby; subscriptions $131 vs $47 per payment (Kajabi, vendor, correlation only). Operator ladder from Instagram: $19 template plus $150 coaching session made about $4,200 plus $2,400 a month at 40K followers (r/InstagramMarketing, 99 pts).

```
product revenue per 1,000 engaged followers = click-through x conversion x AOV x 1,000
second-purchase value matters: design the next offer before scaling the first (education-coaching sibling)
```

## Weekly prioritization

```
priority = expected incremental gross profit x confidence / implementation cost
confidence: platform rule or randomized test = high; vendor aggregate benchmark = medium; single case or operator anecdote = low
```

Research report, 2026. Scale a tactic when the median outcome over repeated executions moves the money metric, never on one viral post.
