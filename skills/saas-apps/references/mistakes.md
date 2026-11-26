# Expensive mistakes

Two tables: what the data and platform rules show, and what founders report losing. Sources and dates in [sources.md](sources.md); operator rows carry the thread and its score.

## From the data and platform rules

| Mistake | What it costs | Do instead |
|---|---|---|
| Judging the trial model on trial starts | No-card trials draw more signups but yielded 3.6 payers per 1,000 visitors vs 10.5 for card-required (ChartMogul and ProductLed 2026, survey) | Compare visitor-to-retained-paid at day 60 to 90 |
| Freemium on a mobile app "for retention" | Day-35 conversion 2.1% vs 10.7% with a hard paywall, with the same yearly retention (28% vs 27%) (RevenueCat 2026) | Hard paywall after onboarding unless free users spread the app |
| Planning B2B retention for a cheap AI tool | AI-native products under $50 a month: 23% GRR, 32% NRR median (ChartMogul, Dec 2025) | Annual plans, credits, integrations; plan cash for churn |
| Ignoring failed payments | Revenue lost with no decision by the customer; dunning recovered 29.4% of attempted failed charges, median (Baremetrics, Q3 2026) | Card updater, retries, day 0/3/7 emails, no-login update link |
| Sub-$5 monthly web plans | A $3 plan loses $0.39 (13%) to a US card fee at 2.9% + $0.30 (Stripe 2026) | Higher monthly price or annual only |
| Paying 30% to Apple by default | Small Business Program cuts it to 15% for developers under $1M proceeds; enrolment is not automatic (Apple 2026) | Enrol before launch; recheck each January |
| Starting a new store on a provider that is closing | Lemon Squeezy takes no new sign-ups and shuts down on 31 March 2027 | Paddle, Stripe Managed Payments or Stripe + Tax |
| Charging inside a Chrome extension through the store | Chrome Web Store payments stopped on 1 Feb 2021 | Your own checkout and licence check |
| Asking for upvotes on Product Hunt or Hacker News | Against both platforms' rules; Show HN also excludes landing pages and signup walls | Ask for feedback; let people try it without signup |
| Mass AI-generated SEO pages | Fits Google's scaled content abuse policy | Fewer pages, each with unique data or a working tool |
| Blocking OAI-SearchBot | Site not shown in ChatGPT search answers (OpenAI 2026) | Allow search crawlers; block training crawlers separately if wanted |
| No processor contracts or privacy policy | GDPR requires a contract with each processor (Art. 28); top-tier fines up to EUR 20M or 4% of turnover (Art. 83) | Privacy page listing vendors; sign each vendor DPA |
| Trials that renew silently | US state auto-renewal laws and ROSCA still apply after the FTC rule was vacated (July 2025) | Reminder before the first charge; one-click online cancel |
| Comparing CPLs across sources | B2B Google Ads CPL ranges from $84 to $524 depending on what counts as a lead ([benchmarks.md](benchmarks.md)) | Compare cost per retained payer only |

## What founders report losing

| Mistake | What it cost | Do instead |
|---|---|---|
| Building for months before selling | Months of work with no buyer signal; operators advise a payment button before any build over 2 weeks (r/SaaS 412) and 5 paying strangers first (r/SaaS 1,261) | Pre-sell or run a paid pilot before a long build |
| Free beta as demand proof | OpenPhone's free-for-feedback users mostly lacked the problem (r/EntrepreneurRideAlong 171) | Charge something, even at a deep founding discount |
| Feature-heavy first version | "I couldn't figure out what it does in the first 30 seconds"; return rate near zero until rebuilt around one function, then about 40% (r/indiehackers 57) | One job, one first-value event |
| Free tier that does the core job | 49 downloads, 0 Pro upgrades in 5 months (r/indiehackers 54) | Cap a number most users cross |
| Requiring the user's own API key at signup | 90% lost at that step (r/microsaas 166) | Offer BYOK as a pricing option, never as a setup gate |
| Cutting price to find customers | $59 to $9 "without success"; repeated cuts brought less serious users with higher churn (r/SaaS 250; r/microsaas 63) | Fix activation or audience; raise when people pay without objection |
| Discounted lifetime next to a subscription | 42 lifetime vs 7 subscriptions left $24.40 MRR (r/buildinpublic 53) | One offer at a time; price lifetime at about 12 months of subscription or more |
| Lifetime deal on paid API usage | Each sale adds an open-ended API bill with no new revenue; the lifetime deal that worked was on-device, where "another hour transcribed creates no additional transcription API bill" (r/AppBusiness 353) | Monthly credits, or BYOK lifetime |
| Public price ladder | First 100 at $14.99 sold in 4 days; only 11 at $19.99 in two weeks after (r/indiehackers 36) | One launch price with a real end date |
| Annual plan hidden below the fold | Sold "almost zero" annual (r/AppBusiness 107) | Annual first, framed per month |
| Launch with no email backup | SendGrid locked an hour into a 1,000-signup launch; SES approval rejected after 48 hours (r/EntrepreneurRideAlong 155) | Warm a second provider before launch |
| App not enabled in every storefront | EU readers could not download until fixed mid-thread (r/SideProject 1,484) | Check availability before posting |
| DMs until the platform limit | X spam restrictions on the account (r/SaaS 341) | 20 to 30 targeted DMs a day to people who asked |
| Explaining internals to a platform partner | Platform built the feature free two days later; channel died (r/startups 310) | Show outcomes, not implementation |
| Ignoring a 1-star about price | Repeated "it's not free" 1-stars; the fix was a subtitle stating the trial (r/iOSProgramming 246) | Price and trial on the store page and subtitle |
