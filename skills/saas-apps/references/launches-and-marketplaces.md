# Launches, directories and marketplaces

Treat every launch as a concentrated acquisition experiment with its own cohort, not a contest. No credible 2025 to 2026 dataset gives a median Product Hunt or Hacker News launch-to-paid conversion (research, November 2026). Measure your own: tag signups by source and compare activation, D30 retention and paid conversion ([economics.md](economics.md)). Operator numbers are one launch each; links in [sources.md](sources.md).

## Product Hunt

Platform rules (Product Hunt help center, 2025 to 2026):
- Launches start at 12:01 a.m. Pacific. Ranking uses weighted points since 1 October 2025: comments and engagement count, votes from established active members weigh more than new accounts.
- Asking for upvotes can get a launch disqualified. Ask people to try it and comment: "We launched [product] today. If [problem] is relevant to you, I'd love you to try it and tell me what breaks or feels confusing: [link]."
- You may relaunch after a major update; launches under 2 months apart need a relaunch request.
- Links are nofollow (operators report PH at DR 91). The value is the badge, the newsletter, the people who browse PH, and the scrapers and smaller directories that copy it.

What worked (operators report):
- **Launch only after the first 100 users and weeks of fixes.** Buildpad launched 43 days after MVP: 13 X posts, 91 replies, 22 DMs on the day, live stats all day: #4 Product of the Day, newsletter feature, 475 users and 5 payers in 24 hours, 22 payers in a week (one founder, cross-posted 7 times).
- **Weekend for the badge, weekday for reach.** 979 featured launches (1 May to 14 July): Sunday averaged 4 competing launches and 78.3% finished top five; Tuesday 20 launches and 18.6%. Median votes for #1: 482 Sunday, 700 Tuesday (r/indiehackers, 43; corroborated by a #1 Sunday launch with 646 votes, r/indiehackers, 91). Weekend traffic is lower: this buys the badge and newsletter odds, not visitors.
- **Pitch the newsletter:** editorial@producthunt.co. An app that got the lead slot with the subject "Cure your brainrot" finished #1 with 10,000+ downloads and about $5,000 that day (also pushed to the founder's 200,000 followers, r/SaaS, 408).
- **Reciprocity list, 30 days out:** support other launches daily, then message the makers: "Hey, just upvoted your launch on Product Hunt. We're launching in about a month and would love to send you the link when we go live." Use real, active personal accounts; launch-week accounts carry little weight (r/buildinpublic, 42). Ask 20 to 50 supporters for "feedback, comments, and thoughts", never votes.
- **Day-of waves:** live 12:01 a.m. PT, maker comment immediately (story, not feature list: problem, why you, what's different, what you want feedback on), reply to every comment in the first hour, LinkedIn, X, email and DMs during US morning, a midday update, an evening push. DM line: "We're live, here's the link, a comment would help a ton."
- **Email your existing users** (3 threads agree): one founder remembered 2 hours late, emailed everyone and still finished 11th with a badge.
- **Relaunch with a new angle:** one SaaS launched 9 times varying audience, thumbnail, tagline and day: 3,565 total upvotes and 15 badges (r/indiehackers, 49).
- **Free and open-source positioning** for an extension's first launch, paid version 3 months later (r/SaaS, 835). A $10 lifetime offer on PH got a first payer within an hour (r/microsaas, 185).
- **Counter-evidence:** a #1 daily finish "did not justify the outreach effort" (r/microsaas, 91); one founder's tracked attribution put PH plus all directories at about 5% of sales vs about 30% from X (r/indiehackers, 84); a #6 finish gave 1,000 visitors and no reported signups. Expect a spike, then near zero.

Field specs (kostja94 product-hunt-launch, MIT): tagline 60 characters max, gallery 1270 x 760, demo video under 2 minutes, 3 to 5 topics. Realistic bands from the same skill (uncited): 200 to 400 upvotes is top 10, 800+ is usually Product of the Day.

## Hacker News (Show HN)

Rules (HN guidelines): users must be able to try it, ideally with no signup or email; landing pages and waitlists are not Show HNs; no marketing language; no coordinated voting. Title: `Show HN: [Name]  to  [what it lets you do]`. First comment: the problem, backstory, how it works technically, what's different, and a request for critique. Transparent pricing helps.

What worked:
- A narrow negative promise ("no feed, no likes, just customizable profiles"): #1, 450 points, 17,000+ visitors, 420 signups in 2 days (r/indiehackers, 57).
- Ship basic, build the requests live: 10,000+ visitors in 12 hours, features added the next day from comments (r/SaaS, 507).
- An incident write-up (an attacker deleted data, here is the fix) reached the front page (r/EntrepreneurRideAlong, 199).
- HN brought 2 paid users within hours while same-day Reddit and PH launches brought nothing (r/microsaas, 105).
- Chain: viral launch tweet, HN front page next day, PH #1 the day after: $10K+ MRR in a month (r/SaaS, 305).
- Recycle the coverage: a project reposted to r/SideProject opening with its HN and press links got 2,022 upvotes (r/SideProject, 2,022).
- Dev tools: a short demo of the agent working in a real app, no pitch, asking for feedback: 2,000+ GitHub stars in 48 hours (r/indiehackers, 159).

Temporarily remove the signup wall for HN traffic (the guidelines endorse it), and have server capacity ready.

## Reddit launch posts

Mechanics and first-users rules are in [first-users.md](first-users.md). Launch-specific:
- **Titles that worked (verbatim, r/SideProject):** "I built an alarm clock that won't stop ringing until you go to the toilet to turn it off" with "comment android and I'll send you the link" (1,838); "I built a free tool that turned my 15 PTO days into 56 days off" plus a share template, which users reposted on TikTok and LinkedIn (1,542); "Cluely raised $15M to build this, I just open sourced it and made it completely free" (1,413); an extension post ending "P.S. Yes, it works on this post too." (767).
- **Pattern:** "I built [specific thing] that [concrete outcome]", a real number, a free way to try it, the demo visible in the post.
- **Serialize the story with auditable numbers:** a job-search engine posted numbered updates; update four moved to a buyer subreddit with a 30-second video: 415K views, 1,100+ users, 24 new paid subscribers, MRR $940 to $1,331 in 48 hours (r/SaaS, 333).
- **Subreddit size matters less than buyer presence:** one founder's 95K and 9.5K subreddit posts got nearly equal visits; a 5,000-member sub gave 18,000 views (contradicts a "50K members minimum" rule). Buyers sit in r/marketing, r/PPC, r/shopify, not r/SaaS.
- **Pitch ratio:** 6 threads agree on 80/20 to 95/5 value to promotion. Links: many subs shadowban links in posts; put the link in a comment or profile unless the sub allows it (r/SideProject launches often link directly).
- **Pre-post research:** read the sub's top 20 posts of the month (title patterns, length, link rules, self-promo day), draft 10 titles, post Tuesday or Wednesday US morning, reply to every comment for 2 hours (3 threads).
- **Recycle winners** to other relevant subs 2 weeks later with a new angle.
- **Have email infrastructure ready:** a 1,000-signup waitlist blast got SendGrid locked an hour into launch; AWS SES approval took 48 hours and was rejected (r/EntrepreneurRideAlong, 155). Warm a backup provider.
- **Enable every App Store storefront** before posting: readers in 4 EU countries could not download until it was fixed mid-thread (r/SideProject, 1,484).

## Directories

Use directories as a foundation layer for backlinks, AI-answer citations and a trickle of in-market visitors, never as the strategy. Build the destination pages first: comparison and alternative pages, use-case pages, a pricing page, privacy and terms (coreyhaines31 directory-submissions, MIT).

- **Traffic reality:** BetaList, SaaSHub and niche directories send 5 to 15 visitors a day each, recurring; PH is a spike then near zero (r/EntrepreneurRideAlong, 49; author sells submissions). 30 placements in week one raised traffic, conversions were poor (r/microsaas, 52).
- **Backlink reality:** 60 submissions in 2 weeks gave 43 live listings, 31 dofollow, DR 0 to 12 in 30 days (author sells a service). Skip directories under DR 20 with no traffic. Indie launch sites often have DR 50 to 80 from badge-swap rings and near-zero traffic, and the dofollow link lasts only while you show their badge (coreyhaines31, MIT).
- **Tiers (coreyhaines31 directory list, MIT):** launch week: Product Hunt, Show HN, BetaList (2 to 4 week queue unless expedited), DevHunt (dev tools), Uneed, Fazier, Microlaunch (month-long visibility). Rolling: AlternativeTo, SaaSHub, G2, Capterra, Indie Hackers products, F6S. AI tools: There's An AI For That (other directories copy it, r/microsaas, 128), Futurepedia, Toolify, Future Tools. Open source: Awesome Self-hosted, awesome OSS alternatives lists, Open Alternative, r/selfhosted release posts (Postiz, r/indiehackers, 573). MCP servers and agent tools: publish to the official MCP Registry first; aggregators read from it. Google opened a Connected Apps Platform for Search and the Gemini app on 28 October 2026: register a cloud-hosted MCP server (or Android AppFunctions) in the Google Connected Console and choose Search, Gemini or both. It is a preview with access opened in phases through an interest form ([Google](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/)). Posts calling it an app store that reaches 4.3 billion users (Elliot Garreffa, [X post](https://x.com/elliot_garreffa/status/2116127839967645789)) overstate it: Google has not published how many people use Connected Apps.
- **Vary the description by directory type:** outcome for startup directories, "[competitor] alternative" for SaaS directories, AI angle for AI directories, technical depth for dev directories. Identical copy everywhere adds nothing.
- **Side effect worth having:** listing widely got the product into writers' "Top 10" roundups, which brought links and signups (r/SaaS, 265). AI assistants cite those listicles: Tally ($5M ARR) believes AI search became its #1 channel through Reddit answers, help docs, comparison pages and inclusion in "best form builders" lists (r/SaaS, 689).
- **Agent safety:** never create accounts, accept terms or pay for listings without the owner's approval; use a role email on the product domain; verify the domain is live and not a lookalike before submitting.

## AppSumo and lifetime-deal marketplaces

- **Upside:** Encharge did $990K in one AppSumo month (a top-five launch ever); the founder slept 5 hours that week from support load (r/SaaS, 299). Another founder had AppSumo at 50 to 80% of monthly revenue on the way to $30K a month (r/SaaS, 341). Vendor cases: Pretty Prompt 5,200+ purchases, 170 reviews at 4.86; Mootion from a few thousand monthly subscribers to $100K to $150K MRR after three campaigns (AppSumo, 2026, selected successes). AppSumo claims a 1.3M audience (its own figure).
- **Cost:** lifetime customers need support forever and never pay again. Model net per code against 3 years of serving cost at p90 usage ([economics.md](economics.md)). For AI products, cap usage with monthly credits as Mootion did.
- **Sequence one founder used:** a giveaway in LTD Facebook groups, a private LTD to your list, AppSumo, then one final private LTD (r/SaaS, 463).
- **When to say no:** a subscription product with healthy MRR growth, high variable costs, or no support capacity. LTD buyers also skew to deal hunters who leave many reviews; prepare docs and canned answers before launch.

## Platform marketplaces (often the best channel nobody mentions)

- **Slack App Marketplace:** a thread-only-channels bot made $1.2K MRR with 8% annual churn, 100% from marketplace discovery and zero marketing (r/microsaas, 634).
- **Port a proven add-on to a new marketplace:** a Google Sheets API connector copied into Airtable when Airtable opened its marketplace reached 190 customers and $6,500 MRR (r/SaaS, 298). Watch for platforms opening app stores.
- **Shopify App Store as a market map:** apps making $2M to $3M a year marked a gap; a founder cloned the core in 2 weeks and sold at $500K ARR, mostly via cold outreach (r/microsaas, 102). Shopify, WordPress.org, Chrome, Figma, Notion, Zapier, n8n and HubSpot listings are indexable pages that rank and carry built-in buyer intent.
- **RapidAPI for small APIs:** it handles keys, plans and billing for about 20%: about $50 MRR from a 2-hour API (r/microsaas, 54). Fine for a side bet, not a business.
- **Integration listings as lead sources:** Heroku and DigitalOcean add-on listings (r/SaaS, 250). Prioritize platforms your retained users already use; integration users often churn less (research, November 2026).

## Chrome extensions

- **Free until the Featured badge, then paid:** downloads triggered a Featured review; the badge raised traffic; first sale minutes after the paid launch and $4,500+ in the first month (r/startups, 296). The badge came after 10+ positive reviews in another case (r/microsaas, 60).
- **Chrome Web Store SEO:** an extension seeded in 3 subreddits then grew to 12,000 active users through store search (r/SaaS, 519).
- **Regional social video before launch:** a proof-of-concept on Threads Taiwan framed "Is this worth X hours of my life?" got about 1M views in a week and shaped the product (r/SideProject, 2,345).
- **Monetize with lifetime or BYOK** when monthly fails (r/SaaS, 835; r/SideProject, 1,629). A license key with no account keeps friction low (r/indiehackers, 44).
- **Ship in public the same day:** a GPT-in-any-textbox extension built and launched in one day via an X thread: 52,000 reach, about $400 in 24 hours at $9.99 (r/EntrepreneurRideAlong, 244).

## Tricks most founders miss

- The best launch is a sequence: Reddit and community feedback, then HN if it is technical, then PH once onboarding holds, then directories over 4 to 8 weeks.
- A launch where the cheapest tier sells out first anchors that price as "the deal" ([pricing-and-trials.md](pricing-and-trials.md)).
- Give launch visitors a reason to leave an email even if they do not sign up (template library, waitlist for the next feature); a launch spike without capture is gone in 48 hours.
- Thank-you badge pages ("Featured on X") are free backlinks for the directory, not for you; add them only where the link is reciprocal and the directory has real traffic.
