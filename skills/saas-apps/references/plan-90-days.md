# 90-day plan

For a solo founder or tiny team with a product that is live but not growing, or about to launch. Order matters: measure, fix activation, prove one channel, then build what compounds. Each phase ends with a short founder report: what changed, the scorecard, what the founder must decide. The timeboxes are a working schedule, not a sourced promise.

## No product yet: the first 30 days instead

1. Write the problem in one sentence and the buyer in one line (role, company size or life situation, trigger moment).
2. Find 30 people who had the problem recently: niche communities, competitor reviews (G2, App Store, Chrome Web Store, Shopify App Store), "[competitor] alternative" threads. Interview 15 about the last time it happened ([scripts.md](scripts.md)).
3. Read three competitors' pricing pages and their 1 to 3-star reviews. Note the missing feature and the price band.
4. Sell before building: a landing page with one outcome and a payment link, a pre-sale with a refund promise, or a paid pilot run by hand. Target 5 paying strangers.
5. If nobody pays after 15 interviews and 30 offers, change the buyer or the problem, not the copy.
6. Choose payments and write terms and privacy before the first charge ([payments-tax-and-legal.md](payments-tax-and-legal.md)).
7. Build the smallest version that delivers the first-value event for those buyers. Then join the plan below at day 1.

## Days 1 to 14: measure

Founder supplies: exports of signups, events, payments, refunds and cancellations for 6 to 12 months; costs per user; logins to Stripe or MoR, App Store Connect or Play Console, analytics.

Agent builds one funnel ([economics.md](economics.md)): source, signup date, first-value date, trial start, paid date, plan, MRR, refund, cancel date and reason, failed-payment flag, variable cost.

Fix:
- A source on every signup (UTM, "how did you hear about us", store campaign links).
- One first-value event, defined with the founder, tracked server-side.
- Separate MRR from annual and lifetime cash.
- Failed-payment basics on: card updater, retries, dunning emails, no-login card update link.
- Trial renewal reminder and an easy cancel path.
- Watch 5 real users try the product (screen share or session replays). Write down every hesitation.

Exit check: visitor-to-paid, activation rate, trial-to-paid, logo churn and involuntary share known for the last full month.

## Days 15 to 30: fix activation and pricing

- List every screen, field and permission between signup and first value. Cut, defer, pre-fill or sample-data everything not needed ([activation-and-retention.md](activation-and-retention.md)).
- Behavior-triggered emails: welcome from the founder, first-value nudge, stuck-user offer of a setup call, trial-ending emails for activated and non-activated users.
- B2B: offer a 15-minute setup call to every new signup for two weeks; count how many convert.
- Pricing pass: is the price in the right bucket; is annual visible; does p90 usage cost exceed 40% of the plan; are prices in USD for a global audience.
- If paying users never objected to price and activation is healthy, raise for new signups.

Exit check: activation and trial-to-paid compared with the day-14 baseline on a full cohort.

## Days 31 to 60: prove one acquisition channel

Choose by product type:
- **B2B tool:** founder-led. 20 to 30 targeted messages a day to people who described the problem in public; instant demos; ask every customer which other team has the same problem.
- **Platform app (Shopify, Slack, Notion, Zapier, WordPress, Chrome):** marketplace listing optimized for the host's search, first 10 reviews from real users, integration pages on your site.
- **Consumer mobile app:** store page in the search phrase, localized metadata, 2 to 3 short-video formats posted daily for 4 weeks ([mobile-apps.md](mobile-apps.md)).
- **Developer or technical tool:** Show HN with a no-signup demo, technical posts, GitHub presence.

Then one launch beat if onboarding holds: Product Hunt, a niche directory round, or a community launch post, each source-tagged ([launches-and-marketplaces.md](launches-and-marketplaces.md)).

Decision rule: keep a channel that brings retained payers at a CAC under your ceiling (monthly contribution x payback months you can fund). Kill a channel after 4 weeks of steady effort with no activated signups.

Exit check: retained payers and CAC (founder hours included) by channel.

## Days 61 to 90: build what compounds

- One free tool or template around the paid job, ungated ([seo-content-and-social.md](seo-content-and-social.md)).
- Comparison or alternative pages for the two competitors buyers mention most.
- Referral or affiliate offer if customers already recommend you; output branding on free exports.
- Churn work: read every cancel reason with usage data; fix the top reason; win-back emails to people who left for a reason now fixed.
- Annual push to monthly customers who have been active 3+ months.
- Paid ads only now, and only as a capped test under the computed CAC ceiling (`paid-ads`).

## Day 90 review: eight numbers

1. Visitor-to-paid by source
2. Activation rate (7-day) and time to first value
3. Trial-to-paid or free-to-paid by gate
4. Retained paid at day 60 or 90
5. Monthly logo churn, voluntary and involuntary
6. MRR and net new MRR (annual and lifetime cash shown apart)
7. CAC and payback by channel, founder hours included
8. Contribution margin per account at p90 usage

Then: double the channel with the best retained payers per founder hour, stop the rest, raise price if conversion held, and pick the next single bottleneck.

## Weekly cadence after day 90

- Monday: last week's signups, activations, payers and cancellations by source; failed payments and recoveries.
- Wednesday: read every support ticket and cancel reason; one fix shipped from them.
- Friday: one piece of compounding work (page, tool, integration, listing) and a one-line founder report with the eight numbers.

## Questions to ask the founder at each phase end

- Which customers would you happily clone, and which would you lose?
- What does one more paying customer cost you in hours this month?
- Which price or offer are you willing to test, and who approves it?
- What will you not do (cold outreach, video, ads, lifetime deals)?
- Who may post and send messages in your name?
