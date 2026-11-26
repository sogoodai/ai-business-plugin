# Technical SEO for small sites

For a site under a few thousand URLs, technical SEO is mostly preventing accidental exclusion, duplication and orphaning. It is not a reason to buy a giant crawler or a monthly "technical retainer". Sources in [sources.md](sources.md).

## The eligibility floor (Google, current docs)

Google's minimum technical requirements are three: Googlebot is not blocked, the page returns HTTP 200, and the page has indexable content ([Google technical requirements](https://developers.google.com/search/docs/essentials/technical)). Everything else is quality and efficiency. Check these first on every priority URL.

| Check | How | Fails when |
|---|---|---|
| Crawlable | robots.txt tester, `site:` search, GSC URL Inspection | A staging `Disallow: /` shipped to production; a security plugin or CDN/WAF blocks bots |
| Status 200 | URL Inspection "Page fetch", any header checker | Soft 404s, redirect chains, 302s left from a migration |
| Indexable | View source for `noindex`, check X-Robots-Tag header | Theme or SEO plugin set `noindex` on categories, tags or whole post types |
| Canonical | Rendered HTML `rel=canonical` vs the URL you link to | Canonical points to the homepage, to an http or www variant, or to page 1 of a series |
| Linked | At least one crawlable `<a href>` from an indexed page | Page only reachable through a sitemap, a JS button or site search |
| Rendered content | URL Inspection "View crawled page" | Main text injected by JavaScript after an API call; tabs that load on click |

## Canonicals, duplicates and redirects

- Signal strength (Google): redirects and `rel=canonical` are strong, sitemap inclusion is weak ([canonicalization docs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)). Link internally to the canonical URL, never to the duplicate.
- Google treats canonical as a hint. If GSC says "Duplicate, Google chose different canonical than user", the pages are too similar or your internal links point the other way. Fix the content or the links, not the tag.
- Consolidating two weak pages on one topic: 301 the weaker URL to the stronger, merge the useful sections, update every internal link to the target. Do not just set a canonical and leave both live.
- Ecommerce facets: filtered URLs self-canonical when a single filter has search demand; sort-only parameters canonical to the unfiltered collection; 3+ active filters `noindex, follow`; block `/cart`, `/checkout`, `/account`, `/search?` in robots.txt (claude-seo and finsilabs, MIT).
- Pagination: Google stopped using rel=next/prev in 2019. Use crawlable page links and a self-referencing canonical on each page, never canonical to page 1 (claude-seo seo-technical, MIT).
- Out of stock: keep the URL live at 200 with alternatives. Remove from the sitemap only when the product is gone for good, then 301 to the closest category.

## Sitemaps and indexing

- Sites under about 500 pages with good internal linking may not need a sitemap, per Google ([sitemap overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)). Submit one anyway: it is the cheapest way to see indexed vs submitted counts per page type in GSC.
- Split sitemaps by page type (products, categories, posts, programmatic pages). The Pages report then tells you which template Google is refusing.
- "Crawled, currently not indexed" and "Discovered, currently not indexed" are usually quality or demand verdicts on small sites, not crawl budget. Improve or merge the page, add internal links from pages that already get impressions, then request indexing once. Repeated requests do nothing.
- Bing: verify in Bing Webmaster Tools and import from GSC in two clicks. Bing's index feeds Copilot and is one of the sources behind other assistants. IndexNow pings Bing and Yandex on publish; Google ignores it.

## Speed and Core Web Vitals

- "Good" = LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less, measured at the 75th percentile of real users ([web.dev](https://web.dev/articles/defining-core-web-vitals-thresholds), updated May 2025).
- Only 48% of mobile sites and 56% of desktop sites pass all three ([HTTP Archive Web Almanac 2025](https://almanac.httparchive.org/en/2025/performance)). Passing is a baseline and a conversion lever, not a ranking shortcut: no study shows a small site jumping positions from a CWV fix alone.
- Use field data (GSC Core Web Vitals report, CrUX) for decisions. A Lighthouse lab score of 60 on a page whose field data passes is not a problem to sell to the owner.
- The usual small-site culprits: uncompressed hero images, page builders loading 20 plugins, chat widgets and popups that shift layout, third-party review widgets. Remove before you optimize.

## Structured data

- Use schema for rich result eligibility and entity clarity: `Product` and `Offer` for products (price, availability, `shippingDetails`, `hasMerchantReturnPolicy`), `Article` with real author pages, `Organization` with `sameAs` to real profiles, `BreadcrumbList`, `SoftwareApplication` for apps.
- Google limited FAQ rich results to well-known government and health sites and dropped HowTo rich results (Google Search Central, August 2023). FAQ markup is not a ranking or AI-citation lever: a 2026 study of 468,037 AI citations found FAQ blocks and structured data explained little of which pages got cited ([Chen and Koudas, arXiv 2610.15033](https://arxiv.org/abs/2610.15033)).
- Product structured data must be in the server-rendered HTML. JS-injected product markup is read late or not at all (claude-seo seo-ecommerce, MIT).
- Never mark up reviews you did not collect, ratings for your own business on your own site (self-serving reviews are ineligible for stars), or prices that differ from the page.

## AI crawler access (check on day one)

| Bot | Used for | If blocked |
|---|---|---|
| `Googlebot` | Google Search, AI Overviews, AI Mode | Gone from all of Google |
| `Google-Extended` | Gemini training and grounding outside Search | No effect on Search or AI Overviews |
| `Bingbot` | Bing, Copilot, DuckDuckGo results | Gone from Bing and Copilot |
| `OAI-SearchBot` | ChatGPT search results and citations | Not shown in ChatGPT search answers except as navigational links ([OpenAI](https://developers.openai.com/api/docs/bots)) |
| `GPTBot` | OpenAI model training | No effect on ChatGPT search |
| `ChatGPT-User` | Fetches a page when a user asks | User-triggered; may not follow robots.txt |
| `PerplexityBot` | Perplexity index and citations | Not cited by Perplexity |
| `Claude-SearchBot` / `ClaudeBot` | Claude search / training | Not cited / no effect on search |
| `Applebot` / `Applebot-Extended` | Siri and Spotlight / Apple training opt-out | Not in Apple surfaces / no effect |

- OpenAI says robots.txt changes take about 24 hours to apply ([OpenAI crawlers](https://developers.openai.com/api/docs/bots)).
- Check the CDN and WAF too: Cloudflare's "Block AI bots" toggle, Wordfence rules and "block AI crawlers" plugins block search bots along with training bots. One WordPress plugin blocked OAI-SearchBot and PerplexityBot by accident (r/smallbusiness, 2026, via `local-seo`). Perplexity publishes its IP ranges for WAF allowlists ([Perplexity community](https://community.perplexity.ai/t/updated-guide-perplexity-crawlers-aws-waf-setup/1022)).
- Blocking training bots is the owner's choice. Blocking search bots removes the site from those answers. Present it that way.
- `llms.txt`: Google says Search ignores it; one log study found 0.1% of AI-bot requests (84 of 62,100) hit it (OtterlyAI via claude-seo, MIT). Ship it only as a 20-minute fact sheet if the owner asks.

## Migrations and redesigns (where small sites lose the most)

1. Crawl and export every URL with clicks or links in the last 16 months (GSC Pages export + backlink tool) before touching anything.
2. Map every old URL to its closest new URL. 301 one to one; never mass-redirect to the homepage (Google treats that as a soft 404).
3. Keep titles, H1s, body copy and internal links on money pages unchanged in the same release. Change one variable at a time.
4. On launch day: check robots.txt, `noindex`, canonicals, sitemap and a sample of 50 redirects. Staging settings shipping to production is the most common disaster.
5. Watch GSC daily for two weeks: 404s, "Page with redirect", impressions by page type.

## Disasters operators report (and the one-line prevention)

| What happened | Cost | Prevention |
|---|---|---|
| Old domain taken offline before redirects were mapped (15-year domain, Oct 2025) | Impressions about 700,000 to 14,000 a month (-98%), organic share of traffic 93% to about 42%, 1,100 redirect rules needed later, no recovery after 4 months (r/TechSEO, 2026) | Keep the old server answering 301s until the full URL map ships |
| Cheap provider swap plus rebrand, new URLs and new content in one go | Ahrefs keywords 3,000+ to 250, revenue down (r/SEO, 136) | One change at a time |
| HTTPS migration changed image URLs on a site where images were 60 to 70% of search traffic | Organic collapse found two weeks later via GSC search type Image (r/bigseo, 40) | Every URL change gets an SEO review; check Web, Image and Video separately |
| Translation plugin (GTranslate) exposed code and admin paths | About 20,000 articles became 7 million URLs; crawl failures 0% to 25%; pageviews 2M to under 100,000 (r/SEO, 102) | Audit which URLs a plugin makes indexable before turning it on |
| robots.txt rules copied without a trailing `$` | Every URL extending those paths blocked; articles vanished (r/bigseo, 40) | Anchor exact-URL rules with `$` |
| robots.txt returning 5xx or timing out | Google can stop crawling for up to 30 days, then uses cached rules (robots.txt RFC summary, r/bigseo, 59) | Monitor robots.txt like the homepage; a 4xx robots.txt means "crawl everything" |
| A canonical template bug pointed thousands of pages to one URL | Near-total deindexing, slow recovery (r/bigseo, 40) | After any canonical deploy, check the rendered canonical on 5 different templates |
| A script closed `<head>` early, pushing canonicals into `<body>` (Home Depot, via Patrick Stox) | Google ignored the canonicals (r/bigseo, 54) | Read canonicals in the rendered DOM; keep them above scripts |
| `<meta name="robots" rel="noindex">` (rel instead of content) | Tag ignored (r/bigseo, 117) | Inspect the live HTML after changing crawl rules |
| CDN subdomain copies of the whole site indexed | Duplicates competing with the main domain (r/bigseo, 117) | Search `site:` for the CDN hostnames |
| Mobile menu links injected only on hamburger click | Googlebot does not click, so links are never found (Martin Splitt, r/TechSEO, 63) | Render nav links in HTML, hide visually |
| Theme change or redesign on the live site | Pageviews 20,729 to 16,621 plus $400 repairs; another 16,621 to 8,974 (r/juststart, 76 and 85) | Stage it, compare speed and templates, then ship |

Crawl logs tell you where Google spends time. On a 400-page site, 90 days of logs showed tags, paginated archives and orphan posts crawled several times a week while the 12 category pages making 80% of revenue were crawled about once every 3 weeks, because nav and sidebars linked to junk (r/TechSEO, 29). Cut sitewide links to junk, add body links to money pages.

Tag archives: one publisher deleted all tag pages (not just noindex) with no dip in traffic (r/SEO, 97). Check tag traffic in GSC first; most get none.

Stop at "good" for speed. Operators who chased lab scores (4 hours to move a score of 80) got nothing; field-data failures in GSC are the only speed work worth billing (r/blogging, 72; r/TechSEO, 36).

## Tricks most owners miss

- Run URL Inspection on the five money pages before any audit tool. It answers "is it indexed, which canonical did Google pick, what did it render" in two minutes.
- A spike of "Alternate page with proper canonical tag" after a theme change usually means the theme added parameterized or `/amp/` URLs. Harmless if the canonical target is right.
- Hreflang and international setups break more small sites than they help. Add a second language only with real translated pages and a separate demand check per market.
- When the owner asks for a "full technical audit", deliver the eligibility table above for priority URLs plus the five worst issues by revenue at risk. A 200-row crawler export is not a deliverable.
