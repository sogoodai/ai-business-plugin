# Measurement: Search Console, GA4 and proving SEO worked

Two layers. Search Console measures what happens before the click (impressions, clicks, CTR, queries, position). GA4 measures what happens after it (sessions, behavior, conversions). Google says the two will not match exactly ([Google](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console)). Sources in [sources.md](sources.md).

## Setup checklist (day 1)

1. GSC **Domain property** (DNS verification) so http, https, www and subdomains are in one view. Add the owner as Owner, never only an agency.
2. Link GSC to GA4 (Admin, Product links). Search Console reports then show landing page plus conversions.
3. One primary conversion, at most three secondary events. Fire on confirmed submission or purchase, not on button click. Use GA4 recommended names (`generate_lead`, `sign_up`, `purchase`).
4. AI channel group in GA4 above Referral (see [ai-answers.md](ai-answers.md)).
5. "How did you hear about us?" field on the form or checkout, with Google search, ChatGPT or AI assistant, YouTube, Reddit, friend, other.
6. Bing Webmaster Tools, imported from GSC.
7. Export GSC data monthly or connect BigQuery bulk export: the UI keeps 16 months and samples long-tail queries. Anonymized queries hide a large share of clicks on small sites.

## Search Console tricks

- **Brand vs non-brand.** Performance, Query filter, Custom (regex), "Doesn't match regex": `(?i)acme|acmé|acme ?co|akme`. Include misspellings and product names. RE2 syntax, case-insensitive by default ([Google Help](https://support.google.com/webmasters/answer/17011165)). Judge SEO work on non-brand clicks only. Brand clicks measure demand created elsewhere.
- **Question queries:** regex `^(who|what|why|how|when|where|which|can|does|is|are|should)\b` shows informational demand and future AI Overview exposure.
- **Commercial queries:** regex `(best|top|vs|versus|alternative|review|pricing|price|cost|cheap|compare)` tracks the money families.
- **Long-tail ideas:** regex `^(\S+\s){5,}\S+$` (6+ words) surfaces conversational queries people type like prompts.
- **Striking distance:** Queries tab, filter position 4 to 20 (export, then filter: GSC position filters are clumsy), sort by impressions. These are the first refresh targets.
- **Impressions without clicks:** pages with 500+ impressions and CTR under 1% at position under 10: rewrite title and meta, check whether the SERP shows an AI Overview or video carousel taking the click.
- **Cannibalization check:** for a query, open Pages. Two or more of your URLs swapping on the same query over time = consolidate or differentiate intent. Two URLs ranking together in top 5 is fine.
- **Compare mode** (last 28 days vs previous 28, or vs same period last year for seasonal businesses) at query and page level. Never read a single week.
- **Average position is not a KPI.** It is an impression-weighted average across queries and surfaces; adding new long-tail impressions makes it "worse" while traffic grows.
- **Measure title tests on a page and query pair,** not the page: select the page, filter to its main query, log CTR as the baseline, ship the new title, compare after a few weeks. Page-level CTR blends dozens of queries (operators report, r/SEO 0 to 200,000 monthly case study, 219 upvotes).
- **Track CTR at a fixed position.** Operators report impressions +66% and clicks -50% on a top-4 query once an AI Overview, videos and People Also Ask sat above it (r/SEO, 174), and traffic down 50%+ with rankings unchanged (r/SEO, 293). Open the live SERP in incognito before blaming the page.
- **Brand vs non-brand on a money page, real example:** 63 branded clicks from 473 impressions vs 8 non-brand clicks from 1,809 impressions in 28 days; the page was only harvesting brand demand after six months of "SEO" (r/bigseo, 2026).
- **Look at the queries a site has, not just indexed pages.** In one collapse, pages with impressions fell 1,953 to 1,450 while queries fell 32,898 to 6,966: the index was intact, the trust was not (r/TechSEO, 2026).
- **See organic results without AI Overviews** for inspection: `https://www.google.com/search?q=%s&udm=14` as a browser search shortcut. Users do not see this view; use it to read the organic order only.
- **Validate commercial terms with a small Google Ads test before writing.** Slidebean confirmed "pitch deck" converted in a few weeks of ads, made it content priority one; its content channel returned $200K on $70K (r/bigseo, 38). Cross-check converting Ads search terms against GSC to find proven terms where you have no organic page.

## The dashboard an owner should see monthly

| Number | Why |
|---|---|
| Non-brand GSC clicks | Did SEO work, net of brand demand |
| Clicks on commercial-query families | Money traffic, not trivia traffic |
| Queries ranking on page one (count) | Leading indicator 2 to 6 months ahead of clicks |
| Organic conversions and organic conversion rate (GA4) | Revenue link |
| Revenue or pipeline from organic landing pages, incl. assisted | Proves value of supporting pages |
| AI-assistant sessions and conversions | New channel, tracked separately |
| Referring domains to money pages | Authority where it pays, not homepage DR |
| Indexed vs submitted priority pages | Health |
| Pages published, refreshed, merged this month | Activity, shown last |

Report three actions with the number behind each. "Nothing material changed" is a valid month.

## Proving a change worked (small-site experiment method)

Most small sites cannot run statistically clean SEO tests. Use controlled before/after:
1. Pick a class of pages and one change (titles, internal links, a section added, refresh).
2. Split similar pages into treatment and control (by template, traffic band, age). Change only the treatment.
3. Wait 4 to 8 weeks; Google needs to recrawl. Note any core update in the window ([Google status dashboard](https://status.search.google.com/summary)) and do not read results during a rollout.
4. Compare clicks and impressions, treatment vs control, vs the prior period. Keep, reverse or scale.

This is how the stronger 2025 to 2026 studies were run (Quattr internal links with control states; Workshop Digital refreshes with untouched controls). "We published 50 pages and traffic rose" is not evidence.

## Diagnosing a traffic drop (in this order)

1. **Tracking or reporting?** GA4 tag removed, consent banner change, GSC property switched. Compare GSC clicks with GA4 organic sessions: if only one fell, it is measurement. Bot spikes inflate GA4 too: one site saw 2,200 "new users" a day that were 95% direct, 100% Windows desktop, hitting one removed 404 (r/SEO, 105).
2. **Google only, or everywhere?** Compare Bing Webmaster Tools, DuckDuckGo and ChatGPT referrals for the same window. Everything fell = technical. Only Google fell = algorithmic or a Google-specific crawl failure (r/TechSEO, 148 and 22; neither found a fix, but the check scopes the problem).
3. **Seasonality?** Same period last year; Google Trends for the head terms.
4. **Technical?** robots.txt, `noindex`, canonical, redirects, site migration date, server errors in GSC Crawl stats.
5. **Which pages and queries?** Compare mode by page. A drop concentrated in one template points to that template; site-wide points to an update or a technical change.
6. **SERP change, not rank change?** Position stable but CTR fell = AI Overview, ads, video or forum results above you.
7. **Core or spam update?** Match dates with the status dashboard. Wait for the rollout to finish before changing anything.
8. **Competitor?** Who took the position, and what does their page have (evidence, freshness, product data, links)?

## Tricks most owners miss

- Filter GSC by country. A sudden "growth" is often impressions from a country you do not sell to.
- Track conversions by landing page group (comparison, product, blog, programmatic), not by single URL. Groups survive URL changes.
- Before paying for rank tracking, use GSC: it is the ground truth for your own site and free. Rank trackers are for competitors and for daily tracking of 20 to 50 money terms.
- When an agency report leads with "keywords ranking" or "estimated traffic value", ask for non-brand clicks and organic conversions over the same 12 months.
