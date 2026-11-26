# Mobile apps: store pages, paywalls, short video and app ads

Mobile subscription apps have richer measured data than web SaaS. Key frame (RevenueCat 2026, 2025 data): new subscription apps rose from about 2,000 to almost 15,000 launches a month in three years, so discovery is harder and monetization design matters more. Fee details and the revenue-per-install formula live in [economics.md](economics.md).

## Paywall design

- **Hard paywall vs freemium:** median D35 conversion 10.7% vs 2.1%, D60 revenue per install $3.09 vs $0.38, one-year retention of yearly subscribers 27% vs 28% (RevenueCat 2026). Observational, but freemium does not buy better retention. Keep freemium only if free users spread the app.
- **Placement: onboarding, then a personal result, then the paywall** while the result is on screen (coreyhaines31 paywalls, MIT). Operators: explain three useful functions in three sentences, then the paywall (r/iOSProgramming, 622); put it at the end of a flow where the user already committed to an output (r/buildinpublic, 88).
- **Teaser, not blur:** showing the count of critical issues while locking the details tripled conversion vs blurring everything (r/AppBusiness, 163). Gate Pro features with a preview on the user's own data (their muscle map with the breakdown blurred, r/AppBusiness, 219).
- **Yearly first:** lead with yearly, per-week or per-month equivalent as supporting text, at most one shorter plan. "$3.33/mo billed yearly" lifted trial starts per paywall view from 24.1% to 30.1% (r/AppBusiness, 219, not yet significant). Annual below the fold sold almost nothing (r/AppBusiness, 107).
- **Paid download vs hard paywall:** commenters (88 upvotes) told a founder to drop a $4.99 upfront price for a free download with in-app purchase; the founder agreed (r/iOSProgramming, 373). Exception: a $4.99 one-time iPad browser made $3,185 net in 9 days (r/buildinpublic, 271). Rule: free download plus paywall by default; paid upfront only for a clear, one-time utility with strong search demand.
- **Trial on yearly only, with a reminder before it ends.** Surprise renewals cause refunds, 1-stars and chargebacks. If most trials cancel on day 1, test no trial plus a cheap weekly plan ([pricing-and-trials.md](pricing-and-trials.md)).
- **One abandon offer:** when a user closes the paywall without starting, show one discounted yearly offer once, not on every close (coreyhaines31, MIT).
- **Expect regression:** one studio's paywall went from 0.8% direct purchase to a 4% peak and settled at 1 to 1.5% (r/AppBusiness, 79).
- **Test remotely** (RevenueCat Paywalls, Superwall, Adapty) so price, plan mix and copy change without a release. Judge on revenue per paywall view and D60 revenue per install.
- **Localize paywall copy by screen, not key by key:** "Lifetime" translated alone became "Durée de vie" (lifespan) in French (r/iOSProgramming, 230).
- **App Review checklist:** price, billing period, trial length and "auto-renews until cancelled" on the paywall; Terms (EULA) and Privacy links; Restore Purchases; visible close button; events `paywall_viewed`, `trial_started`, `subscription_started` with variant ID (coreyhaines31, MIT).
- **Kill the "not free" 1-star:** subtitle "THIS IS NOT A FREE APP - 7 DAY FREE TRIAL INCLUDED" (r/iOSProgramming, 246).

## App Store and Google Play optimization (ASO)

Apple fields (Apple docs via coreyhaines31 ASO, MIT, March 2026): name 30 characters, subtitle 30, keyword field 100 bytes (non-Latin scripts use 2 to 3 bytes per character), all indexed; description and promotional text (170) are not indexed. Promotional text changes without a release. Product Page Optimization tests icons, screenshots and previews only (up to 3 treatments, 90% confidence, one test at a time). Custom product pages: up to 70, each with its own keywords and deep links, and they appear in organic search since July 2025. Apple reports +2.5 points of conversion for custom pages vs a 1.6% default-page rate (2026).

Google Play: title and short description carry the keywords; custom store listings (up to 50) can target countries, search keywords, Google Ads campaigns, pre-registration and churned users (Google Play Console help, 2026).

Rules that come from operator results:
- **Rename to the literal local search phrase and align every asset.** A weight tracker renamed "몸무게 기록" (Weight Tracker) in Korea and "Weight Loss Tracker Pro" in the US, then aligned subtitle, keywords, screenshots, icon and featured features: Korea downloads +283% over 90 days, store conversion 35.3% (App Store Connect screenshot, r/AppBusiness, 55). "AI for kids - Askie" ranked #1 for its phrase in US and UK; MRR $3,361 to about $5,900 in 3 months, 90% organic, after starting with long-tail keywords in the UK and Israel (r/AppBusiness, 147).
- **Contradiction:** branded names (ShutEye ranks top three for "sleep") and branded queries can get richer cards on Play. Rule: new apps with no brand demand put the search phrase in the name; brands with search volume keep the brand plus one keyword.
- **Localize metadata at launch** (3 threads): a 20-app portfolio in EN, FR, DE, IT, ES, PT made about 50,000 organic installs and $35,000 in 30 days (r/iOSProgramming, 992). Localize metadata before UI, mirror en-US screenshots to UK and AU, es-ES to MX (r/AppBusiness, 219). Add UK and Australian English metadata to gain an extra keyword field each (r/AppBusiness, 57). Prioritize rich markets (DE, FR); have a native speaker check only paywall and onboarding.
- **Keyword selection:** feed a category leader into an ASO tool (AppTweak, MobileAction, Astro, AppRadar); shortlist 6 to 10 keywords with popularity around 30+, low competition and buying intent; prefer keywords where the top 10 apps have hundreds of ratings, not thousands, and lack the term in their titles (r/AppBusiness, 134). Skip a keyword if you cannot say why your app is more relevant (r/androiddev, 335). Do not repeat words across title, subtitle and keyword field.
- **Niche screen:** skip if the top app makes under $5,000 a month (r/iOSProgramming, 992). Copycat play: an incumbent at about $10K a month with strong keywords, no trademark, a stale design and a weak page; the best of 5 such apps made $60K in year one (r/startups, 291).
- **Screenshots:** 90% of users never pass screenshot 3; the first screenshot carries the decision (ASO vendor aggregates, 2024 to 2025). Benefit headline on each, real UI, full battery in the status bar (a 34-upvote tip).
- **Play conversion floor:** below 40% store-listing visitors to installs, rework icon, screenshots and feature graphic (r/androiddev, 335).
- **Ratings:** see the review section of [first-users.md](first-users.md). Below 4.0 stars, fix before buying installs.
- **Rejections:** two months of Guideline 4.3 spam rejections came from an icon bought from an icon service that matched another app; ask until a reviewer names the conflict (r/EntrepreneurRideAlong, 263). Google Play closed testing for new personal accounts: recruit 70+ testers (r/AndroidClosedTesting), ship 2 to 3 updates in the 14 days, write detailed production-access answers (commenter advice, r/androiddev, 287).
- **Play account termination:** a 46-day appeal failed; a detailed public r/androiddev post got reinstatement within 8 hours (r/androiddev, 400).
- **ASO alone is a weak launch plan for a new app:** two ASO-only apps made under $100 in 10 months while the same founder's content-driven app made $1,000+ in 3 weeks (r/AppBusiness, 94).
- **Trend apps:** a game named after that day's trending video got 24,000 downloads in 12 hours and 260,000 in a month, then collapsed (r/androiddev, 430). Treat trend launches as short windows; harvest emails or cross-promote before the drop.

## Short video for consumer apps (TikTok, Reels, Shorts, Threads)

The channel that most often makes a small consumer app work. Volume and repeatable formats beat polish. Platform mechanics and posting rules: `organic-social`.

- **Problem carousels with no CTA:** about 10 a day. Slide 1 "I added up everything I still owe", slides 2 to 8 one item each, last slide the total; the app is never mentioned. A 220K-view carousel; 15K to 40K-view posts still drove downloads; $1.6K MRR in 23 days, 87% of revenue from App Store search as viewers searched the name (r/AppBusiness, 235).
- **Five-slide tool lists** on an unbranded account, about 15 minutes each: one hit 1M views and sent signups for weeks (r/AppBusiness, 163).
- **App on the last slide of 1 in 3 carousels only;** more frequent appearances cut reach. Myth-bust hooks worked best ("WILL CARDIO KILL YOUR GAINS?"). Render slide text in code (Pillow), not with an image model, to stop drift; about $0.04 a slide (r/AppBusiness, 219).
- **Volume:** 10 to 12 posts a day on one account beat waiting for one viral post; adding CTAs cut views but improved conversion: 100 to 200 downloads a day (r/AppBusiness, 85).
- **UGC reaction farm:** 3 to 5-second reaction clips at about $2 each, stitched to 1 to 10-second app demos with a text hook ("This website feels ILLEGAL"); warm a new account 3 to 4 days, post 1 to 2 a day at US peak; when a post passes about 1,000 views, make 10 to 20 variants of hook, reaction and demo; judge on profile visits, signups and payers (r/AppBusiness, 98 and 62). Tutorials (screen recording, green screen, a finger guiding clicks) get fewer views and "10x more conversions" (r/SaaS, 564).
- **AI UGC:** $150 to $15 per ad and hours instead of days at the same cost per lead (r/EntrepreneurRideAlong, 300). Label AI content where platforms require it and never fake testimonials.
- **Comment, don't only post:** useful replies under TikToks about the problem (budgeting, debt) brought 140 customers in 30 days from a 3-installs-a-day base, $0 (r/AppBusiness, 190).
- **Reels rules for a viral app:** a 2.5 to 3-second text hook over a real-life scene, the app on screen 5 seconds max, one easy feature, cuts synced to music: 360 to 27,000+ users in about 40 days (r/SaaS, 258).
- **Patience per creator:** an in-house creator stuck under 6,000 views for 2 weeks hit 1M+ by month end (r/AppBusiness, 82). Carousels from 6 months ago still bring installs (r/AppBusiness, 79).
- **Threads:** "pov: my app got acquired by apple" got about 115,000 views and 35 sales in 2 days (r/AppBusiness, 183).
- **Reverse-engineer winners, do not copy them:** prompt used by one studio: "analyze the supplied tiktok creative's exact text and slide order to identify its hook mechanics, audience, psychological flow, emotional arc, and payoff. turn those mechanics into a reusable writing prompt that selects one supplied hook verbatim and creates fresh, credible details without copying the source's specific events or titles." (r/AppBusiness, 178).
- **Account farms** (several accounts on cloud phones, run by a VA) appear in operator reports. They can break platform rules on inauthentic behavior; tell the owner the risk before recommending more than 2 to 3 accounts.

## App install ads

- **Map every ad concept to its own store page:** Apple custom product pages and Google custom store listings, each with matching screenshots and keywords (research, November 2026). Only 31% of apps use custom product pages (AppTweak, 2025).
- **Allowable cost per install = D60 revenue per install** for a bootstrapped app ([economics.md](economics.md)). Medians: $0.42 iOS, $0.16 Google Play (RevenueCat 2026). Most freemium apps cannot buy installs profitably.
- **Apple Search Ads:** start with exact-match brand and category terms; turn off Search Match at first; read Apple's acquisition analytics by custom page.
- **Ads as a review and data engine:** one founder kept loss-making ads on to reach thousands of real users for reviews and bug reports instead of 20 organic downloads a month (r/SaaS, 438). Cap the loss in advance.
- **Web-to-app funnel:** ad, web quiz, web paywall, then download. Moves payment off the store and lets you test onboarding without releases; check each storefront's link-out rules and model Apple's commission at several rates.
- Ad account mechanics, creative testing and kill rules: `paid-ads`.

## Tricks most owners miss

- iOS monetizes faster (D60 RPI $0.42 vs $0.16) but one-year payer LTV is close ($23.38 vs $21.62, RevenueCat 2026). Launching on Android with the same paywall doubled daily subscriptions for one TikTok-driven app (r/AppBusiness, 107).
- Widgets, notifications tied to the user's own dates (payday, bill dates) and a 2-second logging path are retention features ([activation-and-retention.md](activation-and-retention.md)).
- Apple's in-app events (up to several a month) earn browse placements; the lift ends when the event ends (vendor data via coreyhaines31 ASO, MIT). Use them around real content drops.
- Check Play Console search terms monthly: a competitor's large search card cost one app half its new installs, then another 60% (r/androiddev, 264).
- **Apps with user content need moderation before review.** Apple guideline 1.2 requires apps where users post or generate content (social, UGC, AI content creation) to filter objectionable material, let users report content with timely responses, block abusive users and publish contact details ([Apple](https://developer.apple.com/app-store/review/guidelines/#user-generated-content)). Telegram's founder says Apple briefly removed Telegram after an extortionist planted illegal content by editing an old message in a public group and reported it, before Apple contacted the company (reported by Pavel Durov, [X post](https://x.com/durov/status/2084686326540996625), not independently checked). Moderate edits as well as new posts, and keep a takedown contact Apple can reach.
