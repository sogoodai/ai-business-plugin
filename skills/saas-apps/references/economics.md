# Economics: the numbers to compute before any recommendation

Every formula here takes inputs the owner can export from Stripe, RevenueCat, App Store Connect, Google Play Console, PostHog, Mixpanel or their database. Ask for raw exports, not dashboard screenshots. When an input is missing, say which recommendation it blocks.

## The core set

```
MRR = sum of active subscriptions normalized to a month (annual / 12, weekly x 4.33)
logo churn (monthly) = customers lost in month / customers at start of month
revenue churn (monthly) = MRR lost to cancels and downgrades / MRR at start of month
GRR = (start MRR - churned MRR - contraction MRR) / start MRR          (12-month or monthly)
NRR = (start MRR - churned - contraction + expansion) / start MRR
ARPA = MRR / paying accounts
gross margin = (revenue - hosting - inference/API - payment fees - store fees - support) / revenue
LTV (simple) = ARPA x gross margin / monthly revenue churn
CAC (fully loaded) = (ad spend + tools + contractor + founder sales hours x hourly value) / new paying customers
CAC payback (months) = CAC / (ARPA x gross margin)
```

High Alpha's 2025 benchmark warns early founders understate CAC because they leave out founder sales time, support and onboarding ([sources](sources.md)). Always add founder hours at a stated hourly value, even if the owner objects; show both numbers.

Simple LTV breaks when churn is under about 2% a month (it projects decades). Cap the lifetime at 36 months for B2B and 24 for consumer, and say so.

## Whole-funnel conversion, not one step

```
visitor -> signup -> activated -> paid -> retained at day 60/90

visitor-to-paid = signup rate x trial-to-paid
revenue per visitor = visitor-to-paid x first-year revenue per payer x gross margin
```

Worked example (illustrative inputs, adapted from coreyhaines31/marketingskills, MIT): 10% signup x 10% trial-to-paid = 1.0% visitor-to-paid. 3% signup x 25% trial-to-paid (card required) = 0.75%. In this illustration the card gate "wins" the last step and loses the funnel. Real data can point the other way: ChartMogul and ProductLed's February 2026 survey of 200 products counted 10.5 payers per 1,000 visitors with a card-required trial vs 3.6 with a no-card trial (self-selected products, not an experiment). Decide on your own visitor-to-paid and retained paid at day 60 or 90.

Value of one point of free-to-paid: ChartMogul (2026) models a one-percentage-point absolute increase as roughly 15% more new revenue per trial around typical levels. Use this to rank onboarding work against traffic work.

## Mobile subscription app unit economics

```
revenue per install (RPI, D60) = trial start rate x trial-to-paid x first-period price x (1 - store fee) + direct purchases
allowable cost per install = RPI (D60) x payback share you accept (start at 1.0 for bootstrapped)
first-year LTV per payer = yearly price x (1 - store fee) + renewals for monthly/weekly
```

Benchmarks to sanity-check against (RevenueCat 2026, 2025 data): D60 RPI median $0.42 iOS, $0.16 Google Play; hard paywall $3.09 vs freemium $0.38. One founder's working assumption (30% of downloads start a trial, 30% of trials pay, about $30 a year) gives about $2.70 per download before fees (coreyhaines31 paywalls reference, MIT). Treat it as a placeholder to replace with real data after 2 to 4 weeks.

Store fees (check current terms before modeling, they changed in 2025 and 2026):
- Apple: 15% in the App Store Small Business Program (up to $1M proceeds in the prior calendar year); otherwise auto-renewable subscriptions pay 30% in a subscriber's first year and 15% after one year of paid service (Apple Developer, 2026).
- Google Play: in most markets 15% on the first $1M earned each year and on auto-renewing subscriptions. In the EEA, UK and US from 30 June 2026 (Australia and Japan from 30 September 2026): subscriptions on the first $1M pay 10% plus a 5% billing fee (Google Play Console Help, 2026).
- Link-outs from an app to web checkout: rules and any commission differ by storefront and are still moving in court. Model web checkout as several scenarios (for example 0%, 12% and 27%) and check the current guideline before relying on it.
- Stripe on web: 2.9% + $0.30 per US card charge (Stripe Support example, 2026), plus 0.7% for Stripe Billing pay-as-you-go and 0.5% per transaction for Stripe Tax (Stripe price list, 2026). Merchant of record: Paddle 5% + $0.50 per checkout transaction; Stripe Managed Payments 3.5% on the full amount on top of card fees; both file sales tax and VAT for you. Lemon Squeezy takes no new sign-ups and shuts down on 31 March 2027. A $5 monthly plan loses about 9% to the card fee alone: avoid sub-$5 monthly prices on web. Detail: [payments-tax-and-legal.md](payments-tax-and-legal.md).

## AI products: margin per account

```
inference cost per active account = total model/API spend / monthly active accounts
cost per paid account at p90 usage = p90 usage x unit cost
plan margin = plan price - p90 cost - payment fees
credit price floor = unit cost / (1 - target gross margin)      (target 70 to 80%)
```

Rules:
- If p90 usage cost exceeds 40% of the plan price, the plan needs a cap, credits or overage. Stripe (April 2026) recommends base plus usage or credits when compute scales with use.
- Track free-credit exhaustion rate and time to first billable usage (ChartMogul usage-billing guide, October 2026): both lead conversion.
- ChartMogul (December 2025): median NRR 48% and GRR 40% for AI-native products above $250K ARR, versus 82% NRR for B2B SaaS. Plan cash for heavy churn; do not project B2B retention on an AI wrapper.

## Lifetime deal (AppSumo and similar) math

```
net per code = deal price x (1 - marketplace share) - refunds
lifetime cost per code = monthly cost to serve x expected active months (use 36 for B2B tools, plus AI usage at p90)
LTD margin = net per code - lifetime cost per code
```

Operators report AppSumo keeps about 70% of first-week sales from its own audience and less on sales you drive; check the current partner terms before modeling. Price the deal so the code covers at least 3 years of cost to serve at p90 usage, and cap AI usage with monthly credits (the Mootion case in [launches-and-marketplaces.md](launches-and-marketplaces.md)). An LTD that is underwater per code gets worse with every sale.

## Price change break-even

```
customers you can lose on a raise of p% at gross margin m before gross profit falls = p / (m + p)
```

At an 80% gross margin, a 30% raise survives losing 27% of customers. Software margins make raises safer than in services. Grandfather or not: [pricing-and-trials.md](pricing-and-trials.md).

## Dunning and involuntary churn value

```
monthly failed-payment MRR = failed charges x average charge
recoverable MRR = failed MRR x expected recovery (29.4% median attempted recovery, Baremetrics Recovery Index Q3 2026; soft declines recover far better than hard)
annual value = recoverable MRR x 12 x average remaining lifetime months / 12
```

Paddle (vendor) estimates involuntary churn at 20 to 40% of all SaaS churn. Compute the real share from Stripe (failed then canceled) before quoting it.

## Ad math for apps and SaaS

```
allowable CAC (B2B self-serve) = ARPA x gross margin x target payback months (start at 6 to 12)
allowable CPI (mobile) = D60 RPI x 1.0 (bootstrapped) or D180 RPI if cash allows
breakeven CPC = visitor-to-paid x allowable CAC
```

Example: visitor-to-paid 1.5%, allowable CAC $120, breakeven CPC $1.80. PipeRocket's 2026 B2B SaaS Google Ads median CPC was $6.81 (non-brand $13.75). Most sub-$50 ARPA tools cannot buy non-brand B2B search profitably; say so before anyone spends.

LinkedIn: Kiin's 2026 panel puts a demo at $350 median. A product earning $500 a year per account cannot support it.

## Launch cohort comparison

Give every source its own signup field value (ph, hn, appsumo, reddit-<sub>, outreach, directory-<name>). Then per source:

```
activation rate, D30 retention, paid conversion, refund rate, support tickets per account
value per signup = paid conversion x first-year net revenue - support cost
```

A source with 500 signups can be worth less than one with 30. Report value per signup, never signup counts alone.

## Revenue math sanity checks

- **$10K MRR target:** at $20 ARPA that is 500 paying customers; at 5% monthly churn the business must win 25 new payers a month just to stay flat. Show this when an owner picks a low price.
- **Churn ceiling:** steady-state customers = monthly new customers / monthly churn. At 40 new a month and 8% churn, the product plateaus at 500 customers. Fix churn before buying traffic.
- **Annual mix:** cash collected up front = annual subscribers x annual price. Annual plans lower churn by design; compare cohorts by renewal, not by month-2 churn.
