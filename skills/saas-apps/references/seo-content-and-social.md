# Search, AI answers, content and social for small software

This file owns how content connects to a software product's value. Search implementation lives in `seo-content`, platform mechanics and posting cadence in `organic-social`, mobile short video in [mobile-apps.md](mobile-apps.md). Operator numbers are one product each; links in [sources.md](sources.md).

## Why it matters, and when to start

- **It compounds for small teams.** Founders in the MicroConf State of Indie SaaS 2024 survey named SEO and word of mouth as their highest-impact marketing (469 founders, data from late 2023). Organic search and community answers keep working while the founder builds.
- **Start after you know the buyer's words.** Write content in the phrases customers used in interviews, support tickets and cancel reasons, not in your feature names. Before 10 customers, community answers beat articles; after, durable pages start to pay.
- **Measure through to revenue.** Tag organic signups by landing page and compare activation and paid conversion per page after 30 days. Rankings and impressions are inputs, not results.

## The four page types that sell software

1. **Free tool or template around the paid job.** A narrow utility that solves one step of the problem, usable without login, with the paid product as the next step. Operators: a 30-minute ungated subscription-spend treemap posted to r/webdev got 2,000+ upvotes, about 6,000 uniques and about $500 in conversions, link only at the end (r/microsaas 77); utility pages that rank should work without login (r/SaaS 359). Ask for an account only to save, repeat or share the output.
2. **Comparison and alternative pages.** "[Competitor] alternative", "[You] vs [Competitor]", "[Competitor] pricing". Built from real differences: price, migration effort, missing integration, who each is for. Include an import or migration path. Be fair; readers check.
3. **Integration and use-case pages.** One page per tool your users connect ("[Product] for Shopify", "Send [X] to Notion") and per job or role. Marketplace listings on Shopify, Zapier, Notion, Chrome or WordPress are pages too, and they rank with buyer intent ([launches-and-marketplaces.md](launches-and-marketplaces.md)).
4. **Original data and teardown posts.** What you learned from your own product data, a benchmark from your users (aggregated, with consent), a real workflow with screenshots. These earn links and citations that generic "what is X" posts do not.

Programmatic pages are fine only when each page has distinct, useful data. Google's spam policy defines scaled content abuse as "many pages are generated for the primary purpose of manipulating search rankings and not helping users", including AI-generated pages that add nothing new (Google Search Central, 2026). One template filled with a city or job name and no unique data is the pattern to avoid.

## AI answers (ChatGPT, Gemini, Google AI features)

- **Let the search crawlers in.** OpenAI's OAI-SearchBot is the crawler for ChatGPT search; sites that block it are not shown in ChatGPT search answers. GPTBot is separate and only covers model training, so a site can allow OAI-SearchBot and block GPTBot (OpenAI developer docs, 2026). Check robots.txt and any CDN bot blocking before writing anything.
- **Be on the pages assistants cite.** Assistants lean on "best [category] tools" listicles, comparison pages, Reddit threads, review sites and help docs. Tally ($5M ARR) believes AI search became its top channel through Reddit answers, help docs, comparison pages and inclusion in "best form builders" lists (operators report, r/SaaS 689). List the product in the directories and roundups for its category ([launches-and-marketplaces.md](launches-and-marketplaces.md)).
- **Make facts machine-readable.** Prices, plans, limits, integrations and "who it is for" as plain HTML text on the pricing and docs pages, not only inside images or JavaScript widgets.
- **Track it.** Ask new signups "How did you hear about us?" with "ChatGPT or another AI assistant" as an option, and watch referrers from AI assistants in analytics. When the answer is an AI assistant, ask which prompt they typed and track those prompts (Tally's method, [ai-answers.md](../../seo-content/references/ai-answers.md)). No credible public data yet shows which formatting causes more citations; treat "GEO" tactics as experiments.

## Community answers as a channel

- **Answer where buyers ask, not in founder subreddits.** A movie-matching app moved from founder subs to r/movies: about 2,000 upvotes, 27,000 downloads that week, $0 spent (r/EntrepreneurRideAlong 164). Buyers sit in r/marketing, r/PPC, r/shopify, accounting groups, niche Discords.
- **Cadence beats virality.** Three posts a week for about 7 months drove nearly all of one product's 3,556 users, then SEO took over (r/SaaS 336). Ten tailored posts in different subreddits over 2 weeks, each giving something first: about 300,000 views, 3,500 installs, first $1,000 (r/iOSProgramming 107).
- **Help first, product when asked.** Reveal the product when someone asks where the data or the fix comes from (r/indiehackers 96). Six threads agree on 80/20 to 95/5 value to promotion.
- **Alerts on buying phrases.** F5Bot or saved searches on "is there a tool that", "[competitor] alternative", "[competitor] price increase", "[competitor] shutting down". Answer within hours.
- **Read every subreddit's rules** and its top posts of the month before posting; never post the same text in several communities on the same day.

Detail and more cases: [first-users.md](first-users.md).

## Build in public, X and LinkedIn

- **Share numbers and decisions, not hype.** Revenue, failed experiments, pricing changes, what customers said. Story posts work when the story is the product's reason to exist (r/SideProject 846); otherwise lead with what it does and a free way to try it.
- **Reply more than you post.** A quota that worked: 5 posts and 50 replies a day for 2 weeks in X communities, product only in the bio, first 100 users (r/microsaas 129).
- **LinkedIn for B2B:** send a free, product-generated result to anyone who asks (a research tool made LinkedIn about half of all clients this way, r/startups 728). Founder posts with a real result outperform company-page posts.
- **One founder's tracked attribution** put X at about 30% of sales vs about 5% for Product Hunt plus directories (r/indiehackers 84). One product; measure your own.

## Short video for web products

Screen-recorded tutorials (screen, green screen, a cursor or finger guiding clicks) got fewer views but "10x more conversions" than entertainment clips for one SaaS (r/SaaS 564). Show the outcome in the first 2 to 3 seconds and the product for 5 seconds at most. Consumer-app formats (problem carousels, reaction clips, volume rules) are in [mobile-apps.md](mobile-apps.md).

## Built-in distribution

- **Output carries the brand:** a "Made with [product]" mark on free-tier exports or a "Powered by" badge on embeds, removable on paid plans (Calendly and Webflow pattern; coreyhaines31, MIT).
- **Collaboration is the invite:** shared folders, shared links, guest seats. Measure invites sent per active account.
- **Changelog as content:** a public changelog and a monthly "what shipped" email are retention touches and fresh pages for search.

## What to measure per piece of content

```
signups by landing page (30 days) and source
activation and paid conversion of those signups vs site average
assisted conversions: content viewed before the pricing page
AI-assistant mentions: self-reported "how did you hear" + referrers
```

Kill a format after 6 to 8 weeks of steady output with no activated signups; double a format that brings activated signups at any volume.

## Mistakes specific to content

- Writing about features in the founder's vocabulary instead of the buyer's problem phrases.
- Gating the free tool behind signup, which kills sharing and ranking.
- Publishing hundreds of near-identical AI pages; it fits Google's scaled content abuse definition.
- Blocking OAI-SearchBot or other search crawlers by accident through a CDN bot setting.
- Comparison pages that misstate a competitor's price or features; readers and the competitor will notice.
