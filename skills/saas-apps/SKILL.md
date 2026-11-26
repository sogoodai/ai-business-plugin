---
name: saas-apps
description: "Grow a small software product built by a solo founder or tiny team: SaaS, micro-SaaS, AI tools, web apps, iOS and Android subscription apps, Chrome extensions, Shopify, Slack, Notion or WordPress apps. Use for validating an idea before code, first 10 and first 100 customers, pricing, free trial vs freemium, card-required trials, annual plans, lifetime deals, onboarding and activation, churn and failed payments, Product Hunt, Hacker News, directories, app stores and marketplaces, Stripe vs merchant of record, sales tax and VAT, terms and privacy basics."
---

# SaaS and apps: prove someone pays, then make them stay

For solo founders and teams of up to about five shipping a SaaS, micro-SaaS, AI tool, mobile subscription app, browser extension or platform app (Shopify, Slack, Notion, Airtable, WordPress), usually under $1M ARR and self-funded. Not for VC-scale sales teams. Built from 1,640 practitioner tactics in 685 usable threads out of 1,350 scraped (r/SaaS, r/microsaas, r/indiehackers, r/buildinpublic, r/AppBusiness, r/startups, r/SideProject, r/EntrepreneurRideAlong, r/iOSProgramming, r/androiddev), a November 2026 research pass (ChartMogul, ProductLed, High Alpha, RevenueCat, Userpilot, Baremetrics, MicroConf, Apple, Google Play, Shopify, Chrome Web Store, Stripe, Paddle, Product Hunt, Hacker News, EU and US regulators) and public skill packs (coreyhaines31 marketingskills, MIT). Platform fees and benchmark figures in this file were rechecked on 26 November 2026. "Operators report" marks a Reddit number with its thread score; everything else carries its source and year. Full list: [references/sources.md](references/sources.md). The founder's decisions win over this guide.

## How small software actually grows

- **Most indie products stay small, so plan for the median.** 28% of 469 surveyed independent SaaS companies made under $1,000 MRR, the largest single group (MicroConf State of Indie SaaS 2024, data from late 2023). On mobile, 17.3% of subscription apps reach $1,000 a month in their first two years and 4.6% reach $10,000 (RevenueCat 2026, 2025 data, 115,000+ apps).
- **Conversion depends on the gate more than the copy.** Free-to-paid within six months: 8% median across 200 products; freemium 3 to 5% good, no-card trial 4 to 6%, card-required trial 25 to 35% (ChartMogul and ProductLed, Feb 2026). Per 1,000 visitors the same survey found 10.5 payers with a card-required trial, 3.6 with a no-card trial and 5 with freemium. Survey, self-selected products: test it on your own funnel.
- **Retention sets the ceiling.** Under $1M ARR, median gross revenue retention is 92% and net 100% (High Alpha 2025, 800+ respondents). Companies above 106% NRR with CAC payback under 10 months grew 71% median vs 30% for NRR under 98% (same report). An AI tool priced under $50 a month kept 23% of revenue gross over a year, median (ChartMogul, Dec 2025). Cheap AI subscriptions churn like consumer apps.
- **Small products win in narrow places.** The repeated pattern in operator threads: one buyer, one recurring job, found where that buyer already asks for help (a niche subreddit, a Slack community, a platform marketplace), sold by the founder by hand until a channel repeats.
- **Marketplaces are distribution most founders skip.** A Slack bot reached $1.2K MRR with 100% marketplace discovery and no marketing (operators report, r/microsaas 634); an add-on ported to Airtable's new marketplace reached 190 customers and $6,500 MRR (r/SaaS 298). Shopify charges 0% revenue share on an app's first $1M of lifetime revenue (Shopify, 2026).
- **Mobile is a different game.** Store search, short video and paywall design matter more than launches. Hard paywalls converted 10.7% of downloads by day 35 vs 2.1% for freemium, median (RevenueCat 2026).

## First session: ask, then compute

Ask the founder:

1. What the product does in one sentence, for whom, and the job it replaces (spreadsheet, agency, competitor, nothing). B2B, consumer, or both.
2. Form: web SaaS, mobile app (iOS, Android), extension, platform app. Country of the business and of most customers.
3. Price, plans, trial or freemium, card required or not, annual option, any lifetime deals sold.
4. Payments stack: Stripe, Paddle, Lemon Squeezy, App Store, Google Play, Shopify billing. Who files sales tax and VAT today.
5. Exports: signups, activation events, payments, cancellations, refunds by source and month (Stripe, RevenueCat, App Store Connect, Play Console, PostHog, Mixpanel or the database). Raw rows, not screenshots.
6. What "first value" is: the event after which a user would miss the product.
7. Where the first 10 paying customers came from, and whether the founder has talked to them.
8. Variable cost per active user (hosting, AI inference, API calls, support) and the heaviest users' cost.
9. Hours per week for marketing and sales; cash for ads; what the founder will not do (cold outreach, video, ads, discounts).
10. Terms of service, privacy policy, refund policy and cancellation path: live, missing or copied.

Then compute ([references/economics.md](references/economics.md)):

```
visitor-to-paid = paying accounts / unique visitors (by source, 30-day window)
activation = signups reaching the first-value event within 7 days / signups
trial-to-paid = trials converted / trials ended (card and no-card separately)
retained paid = accounts still paying at day 60 or 90 / accounts that first paid
MRR = monthly subscriptions + annual / 12 (cash from annual and lifetime kept separate)
logo churn = customers lost in month / customers at start of month
involuntary share = churn after failed payment / all churn
contribution per account = price - payment or store fee - variable cost at p90 usage
CAC (fully loaded) = (ads + tools + contractors + founder hours x hourly value) / new payers
CAC payback months = CAC / monthly contribution per account
steady-state customers = new payers per month / monthly logo churn
```

Report the three biggest leaks in money per month, not in percentages. A common first finding: activation is the leak, and more traffic would only make it bigger.

## Benchmarks to check first

| Metric | Typical | Strong | Source, year |
|---|---|---|---|
| Free-to-paid within 6 months, all models | 8% median | top 20% about 10x bottom 20% | ChartMogul and ProductLed, Feb 2026 (200 products) |
| Freemium free-to-paid | 3 to 5% | 8 to 12% | same |
| Free trial, no card | 4 to 6% | 10 to 15% | same |
| Free trial, card required | 25 to 35% | 50 to 60% | same |
| Payers per 1,000 visitors: card trial / no-card trial / freemium | 10.5 / 3.6 / 5 | | same |
| YoY ARR growth, under $1M ARR | 100% | 300% (upper quartile) | High Alpha 2025 |
| CAC payback, under $1M ARR | 5 months | 2 months | High Alpha 2025 |
| GRR / NRR, under $1M ARR | 92% / 100% | 100% / 116% | High Alpha 2025 |
| NRR, B2B SaaS above $250K ARR | 82% | 97% (upper quartile) | ChartMogul, Dec 2025 |
| AI-native GRR / NRR by monthly price | under $50: 23% / 32% | over $250: 70% / 85% | ChartMogul, Dec 2025 |
| Activation rate, B2B SaaS | 37.5% average (62 companies) | | Userpilot 2025 (vendor) |
| Onboarding checklist completion | 19.2% average | | Userpilot 2025 |
| Mobile: download to paid by day 35, hard paywall vs freemium | 10.7% vs 2.1% | | RevenueCat 2026 (2025 data) |
| Mobile: revenue per install by day 60, hard paywall vs freemium | $3.09 vs $0.38 | | RevenueCat 2026 |
| Mobile trial-to-paid by trial length | 25.5% (4 days or less), 37.4% (5 to 9) | 42.5% (17 to 32 days) | RevenueCat 2026 |
| Failed payments recovered by dunning | 29.4% median attempted recovery | | Baremetrics Recovery Index, Q3 2026 (vendor) |

More with sample notes: [references/benchmarks.md](references/benchmarks.md). No credible public dataset gives Product Hunt or Hacker News launch-to-paid conversion, Chrome extension install-to-paid, integration-marketplace CAC or Meta ads CAC for small SaaS. Say so instead of inventing one.

## Decision rules, in order

1. **Validate with money before code.** Five strangers paying (pre-order, Stripe payment link, paid pilot) beats any number of "I'd use that". Interview about the last time the problem happened, not about the idea. If you cannot reach 20 buyers by hand in two weeks, that is the distribution answer too. Details: [references/first-users.md](references/first-users.md).
2. **Pick one buyer and one place they already ask for help.** Niche communities, competitor review pages, platform marketplaces, "[competitor] alternative" threads. First 10 customers by hand: answer the problem first, DM only people who asked, offer a call and do the setup with them.
3. **Instrument before buying anything.** A source on every signup, one first-value event, paid and retained at day 60 or 90. Judge every channel on retained paid accounts, not signups or upvotes.
4. **Fix activation before traffic.** Write down every screen, field and permission between signup and first value; cut or defer what is not needed. Operators report activation 24% to 61% after deleting features down to the core (r/SaaS 768) and 30% to 54% after renaming one confusing label (r/indiehackers 70). Retest on a later cohort.
5. **Price from the buyer's value, then raise.** Rough buckets: about $10 a month for a prosumer tool, about $100 for a team tool, about $1,000 for sales-assisted (coreyhaines31 pricing, MIT, heuristic). Avoid web plans under $5 a month: at $5, a US card charge at 2.9% + $0.30 (Stripe, 2026) costs 8.9% before billing fees. Offer annual from day one. Raise on new signups first when people pay without objection. Mechanics: [references/pricing-and-trials.md](references/pricing-and-trials.md).
6. **Choose the gate by product type, then test it on visitor-to-retained-paid.** B2B self-serve at $20 to $50: card-required trial of 7 to 14 days (62% of trial products use 14 days, ChartMogul 2026). $100+ a month: demo, trial on request. Consumer mobile: hard paywall after onboarding, trial on the yearly plan. Freemium only when free users spread the product or serving them costs almost nothing.
7. **Set up payments and tax before the first charge.** Selling to consumers in many countries with no finance help: a merchant of record (Paddle 5% + 50 cents; Stripe Managed Payments 3.5% on top of card fees) files VAT and sales tax for you. Mostly B2B in your own country: Stripe plus Stripe Tax is cheaper, but you register and file. Mobile in-app purchases go through the store. See [references/payments-tax-and-legal.md](references/payments-tax-and-legal.md).
8. **Launch as a sequence, not an event.** Community feedback, then Show HN if technical, then Product Hunt once onboarding holds, then directories over 4 to 8 weeks. Each gets its own source tag. Product Hunt: ask for feedback, never for upvotes (Product Hunt rules). Show HN: people must be able to try it, ideally without signup; landing pages do not qualify (HN guidelines).
9. **Use the host's marketplace when the buyer lives in a host product.** Shopify, Slack, Notion, Airtable, Zapier, WordPress, Chrome, Figma listings rank in search and carry intent. Read the revenue share and review rules first ([references/launches-and-marketplaces.md](references/launches-and-marketplaces.md)).
10. **Split churn before fixing it.** Failed payments are an ops problem (card updater, retries, dunning emails); cancellations are a product problem (cancel reason plus usage). Cheap AI and consumer tools need a plan for heavy churn, not a B2B retention target.
11. **Content and SEO after you know the words buyers use.** Free tools, comparison and alternative pages, integration pages, then answers in communities. No mass-generated pages ([references/seo-content-and-social.md](references/seo-content-and-social.md)).
12. **Paid ads only under a computed ceiling.** Allowable CAC = monthly contribution x payback months you can fund (start at 6 to 12). Most tools under $50 ARPA cannot buy non-brand B2B search profitably; test with a capped loss.

## Pricing and trials in one screen

- **Annual plan visible and framed per month,** with the billed amount and period stated (App Review rejects paywalls that hide them). Annual cash funds the next month of work; track it apart from MRR.
- **Raise before you cut.** Nine separate founders report raises with flat or better conversion (r/SaaS 383 and 768, r/AppBusiness 235, r/microsaas 105, r/SideProject 616); repeated cuts brought "less serious users with higher churn" (r/microsaas 63). When nobody pays, price is rarely the bottleneck.
- **Usage costs money, so cap it.** If p90 usage costs more than about 40% of the plan price, add credits, a cap or overage (working rule in [references/economics.md](references/economics.md)). Lifetime deals only when marginal cost is near zero.
- **Trial honesty.** Remind before the first charge; surprise renewals turn into refunds, 1-star reviews and chargebacks. Card-trial conversion includes people who forgot to cancel.
- **Grandfather with an end date.** Move early customers with notice and an "annual at the old price" option.

## Payments, fees and platform rules

| Channel | Fee or rule | Source, year |
|---|---|---|
| Apple App Store | 15% in the Small Business Program (up to $1M proceeds in the prior year); otherwise subscriptions pay 30% in a subscriber's first year, 15% after | Apple Developer, 2026 |
| Google Play | 15% on the first $1M a year and on subscriptions in most markets; EEA, UK and US from 30 June 2026: subscriptions 10% + 5% billing fee on the first $1M | Google Play Console Help, 2026 |
| Google Play, new personal accounts | Closed test with 12+ testers opted in for 14 days before production | Google Play Console Help, 2026 |
| Shopify App Store | 0% on the first $1M of lifetime app revenue (counted from 1 Jan 2025), 15% above; $19 one-time registration | Shopify Dev Docs, 2026 |
| Chrome Web Store | No built-in payments since 1 Feb 2021: use your own checkout and licence check. Featured nominations require core features to work without payment | Chromium Extensions group, 2020; Chrome docs, 2026 |
| Stripe | 2.9% + $0.30 per US card for a US merchant; Billing 0.7% of billed volume and Tax 0.5% per transaction on pay-as-you-go (Stripe's price list; card rates differ by country) | Stripe, 2026 |
| Stripe Managed Payments | Merchant of record for digital products, 3.5% on the full amount incl. tax, on top of card fees | Stripe Support, 2026 |
| Paddle | Merchant of record, 5% + 50 cents per checkout transaction | Paddle, 2026 |
| Lemon Squeezy | No new sign-ups; shuts down 31 March 2027. Do not start a new product on it | Lemon Squeezy, 2026 |

Check every fee on the live page before modeling; these changed in 2025 and 2026. Not legal or tax advice.

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| Card-required trial | "Fewer starts, so it loses the funnel" | 10.5 payers per 1,000 visitors vs 3.6 without a card (ChartMogul 2026, survey) | Test both on visitor-to-retained-paid at day 60 to 90, not trial starts |
| Freemium builds loyalty | Free users stay and upgrade later | Yearly subscriber retention 27% hard paywall vs 28% freemium, conversion 5x higher with a hard paywall (RevenueCat 2026) | Freemium only when free users spread the product |
| Short trials convert better | 3-day trials cut cancel-forgetting | Mobile trial-to-paid rises with length: 25.5% at 4 days or less, 42.5% at 17 to 32 (RevenueCat 2026, correlation) | Match trial length to time-to-value; judge revenue per install |
| AI wrapper retention | "Same as SaaS" | Under $50 a month, AI-native GRR 23% vs B2B NRR 82% (ChartMogul 2025) | Price for churn: annual plans, credits, workflow lock-in |
| Product Hunt makes the business | #1 finishes and badges | One founder's tracked PH plus directories: about 5% of sales vs 30% from X (r/indiehackers 84); no public launch-to-paid data exists | Launch for a cohort and backlinks; judge on retained payers |
| Price low to get traction | $9 removes friction | 28% of indie SaaS sit under $1K MRR (MicroConf 2024); raises held conversion in nine operator reports | Start in the right bucket, raise on evidence |

## Never

- Never ask for upvotes, coordinate votes or buy reviews; Product Hunt and Hacker News forbid it and store reviews get removed.
- Never let free trials renew without a clear reminder, or hide the cancel path. The FTC click-to-cancel rule was vacated on 8 July 2025, but ROSCA, FTC Act section 5 and state auto-renewal laws still apply (Greenberg Traurig, 2025).
- Never sell lifetime access to something that costs you money per use without a cap.
- Never quote MRR that includes annual or lifetime cash, or call trial starts revenue.
- Never put personal data in a vendor you have not listed in the privacy policy; under GDPR a processor needs a contract (Art. 28).
- Never mass-generate near-identical pages for SEO; Google calls it scaled content abuse.
- Never scrape and mass-DM a competitor's community or run accounts that pretend to be users.
- Never invent a benchmark, a testimonial, a customer count or a "users love it" claim.

## Before writing any message

Use [references/scripts.md](references/scripts.md): validation interview, problem-first DM, demo and setup call, welcome and activation emails, trial-ending emails, failed-payment emails, cancel survey, win-back, price increase notice, review ask, Product Hunt maker comment, Show HN post, affiliate and sponsorship pitches.

## References

- [benchmarks.md](references/benchmarks.md): conversion, retention, growth, mobile, paid, outbound numbers with source, year and sample.
- [economics.md](references/economics.md): every formula with worked examples (funnel, CAC, payback, mobile revenue per install, AI margin, lifetime deals, price-raise break-even, dunning value).
- [first-users.md](references/first-users.md): validation with money, Reddit, intent mining, communities, founder-led sales, creators, affiliates, referral loops, reviews.
- [pricing-and-trials.md](references/pricing-and-trials.md): first price, tiers, trial vs freemium vs card, annual and lifetime, launch pricing.
- [activation-and-retention.md](references/activation-and-retention.md): activation events, path to value, lifecycle messages, churn, cancel flow, dunning, win-back.
- [launches-and-marketplaces.md](references/launches-and-marketplaces.md): Product Hunt, Show HN, Reddit launches, directories, AppSumo, platform marketplaces, Chrome extensions.
- [mobile-apps.md](references/mobile-apps.md): paywalls, ASO, short video, install ads.
- [seo-content-and-social.md](references/seo-content-and-social.md): free tools, comparison and integration pages, AI answers, community answers, build in public.
- [payments-tax-and-legal.md](references/payments-tax-and-legal.md): Stripe vs merchant of record, store billing, VAT and sales tax, terms, privacy, GDPR basics, refunds and cancellation.
- [scripts.md](references/scripts.md): exact wording for every recurring message.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan for a new, launched or stalled product.
- Sibling skills: `offers-pricing` (price psychology, raise notices), `website-conversion` (landing and pricing pages), `seo-content` (search implementation), `organic-social` (platform mechanics), `paid-ads` (account setup and creative tests), `email-sms-loyalty` (lifecycle flows and consent), `b2b-outbound` (cold email infrastructure), `launch-first-customers` (generic first-customer playbook), `digital-products` (one-time digital goods).
