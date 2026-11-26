---
name: seo-content
description: "Grow organic search traffic and sales for a small business or online brand. Pick keywords that convert, plan blog, comparison, alternatives, product and programmatic pages that rank, refresh and interlink old posts, earn links and PR, fix technical SEO, read Search Console, recover from Google updates, judge SEO agencies, and get cited in ChatGPT, Perplexity and AI Overviews. For ecommerce, SaaS, B2B services, agencies, content and affiliate sites. Maps and reviews: local-seo."
---

# SEO and content: traffic that turns into customers

For ecommerce stores, SaaS and apps, B2B and professional services, agencies, content and affiliate sites, creators and digital product sellers. Built from 1,157 practitioner tactics across 842 threads (r/juststart, r/SEO, r/TechSEO, r/bigseo, r/blogging, r/content_marketing), 2024 to 2026 research (randomized AI Overview experiments, Google and OpenAI documentation, Ahrefs, SmartSites, Ruler Analytics, BuzzStream datasets, a 468,037-citation AI study) and the best public SEO skills ([sources](references/sources.md)). "Operators report" marks a Reddit anecdote; every other number carries its source and year. The owner's decisions win over this guide.

Local visibility (Google Business Profile, reviews, map pack, city pages, local AI answers) belongs to the `local-seo` skill. This skill covers the website and content layer for any business.

## How organic growth works in 2026

- **Informational clicks are shrinking; commercial clicks are not.** A randomized 2026 field experiment found AI Overviews cut outbound organic clicks 39.8% when they appear; forcing AI Mode cut external CTR 18.8 points in another (N=1,100, March 2026). Pew: 8% of visits with an AI summary click a result vs 15% without, and about 1% click a cited link. Comparison, product, integration, tool and first-party pages keep their economics.
- **Clicks concentrate at the top.** Median CTR is 4.72% at position 1, 1.90% at 2, 0.22% at 10; positions 1 to 3 take 71% of a typical site's clicks (SmartSites, 910 GSC properties, 2025 to 2026).
- **Organic converts like paid search.** Median organic conversion 3.3% vs 3.4% for paid search, and organic brings 29% of conversions from 21.5% of visits (SmartSites 2026). Ruler Analytics averages: software 7.9%, professional services 8.1%, retail 2.0% (2026).
- **It is slow and power-law.** New articles: first impression at a 10-day median, first page-one week at 154 days; 38% reach page one by day 90, 54% by day 180 (murkuz, 633 articles, 2025 to 2026). Only 1.74% of a broad sample of new URLs reached a top 10 within a year (Ahrefs 2025). Median monthly organic clicks: 97 for sites with 10 to 50 indexed pages, 945 for 100 to 200, 2,463 for 200 to 500 (Ahrefs, 344,956 sites, June 2026).
- **Google rewards the company that owns the thing.** March 2024 folded "helpful content" into core ranking and added scaled-content, expired-domain and site-reputation abuse policies; Google reported 45% less low-quality, unoriginal content. March 2026 shifted visibility from aggregators to first-party brands (Amsive, 2,000+ domains, observational).
- **AI answers are retrieval, not decoration.** Retrieval explained 32% of which pages got cited vs 2.8% for page attributes; FAQ blocks and schema barely mattered (158,099 answers, 468,037 citations, October 2026). Google: optimizing for AI features "is still SEO".

## First session: ask, then compute

Ask the owner:
1. What do you sell, to whom, at what price and margin? Which 3 offers make the most profit?
2. Who are the 3 to 5 rivals buyers compare you with? What do buyers ask before buying?
3. Access: Search Console (Owner), GA4, CMS, Bing Webmaster Tools. Who else has admin?
4. What is a conversion (sale, demo, call, signup) and how is it tracked?
5. Any first-hand assets: customer data, tests, photos, case studies with numbers, staff experts?
6. History: migrations, redesigns, traffic drops and their dates, agencies used, links bought.
7. Budget and who writes: owner, staff, freelancers, AI with review?
8. Training crawlers (GPTBot, Google-Extended, ClaudeBot): allow or block? Search crawlers stay allowed.

Then compute ([references/measurement.md](references/measurement.md)):

```
non-brand clicks = GSC clicks excluding a brand regex (trailing 3 and 12 months)
commercial clicks = clicks on queries matching best|vs|alternative|review|pricing|cost|buy
striking distance = queries at positions 4 to 20 with impressions, sorted by impressions x CPC
CTR gap = pages with 500+ impressions, position under 10, CTR under 1%
organic conversion rate = GA4 organic key events / organic sessions, by landing page group
content value = organic conversions x value per conversion, by page role (sell, decide, do, prove, support)
SEO break-even revenue = monthly SEO cost / gross margin
AIO click haircut = informational traffic forecast x 0.4 to 0.6 when the SERP shows an AI Overview
```

Report the three biggest gaps in money, not rankings.

## What to check first, in order

1. **Eligibility.** robots.txt, `noindex`, canonicals, HTTP 200, rendered HTML on 5 money pages (GSC URL Inspection). Then OAI-SearchBot, PerplexityBot, Bingbot and Claude-SearchBot in robots.txt and CDN bot settings. [technical.md](references/technical.md)
2. **Brand vs non-brand.** If non-brand clicks are near zero, SEO has not started, whatever the agency report says.
3. **Money pages exist?** Category, product or service pages, pricing, one comparison and one alternatives page per main rival, integration or use-case pages. Missing ones beat any blog post.
4. **Striking distance and CTR gaps.** Cheapest wins: refresh and relink before writing new posts.
5. **Internal links into money pages.** The typical site has zero contextual blog-to-pricing or demo links (510-site crawl, 2026).
6. **Thin or duplicate inventory.** Give every URL a role; merge or remove pages with none.
7. **Off-site gaps.** Review sites, comparison lists, communities and videos cited for rivals in AI answers. [ai-answers.md](references/ai-answers.md)

## Decision rules

- **Every URL gets one job: sell, decide, do, prove or support.** If an informational page does none and its answer fits a six-line AI summary, skip it.
- **Commercial before informational.** Build the five demand families first: category, comparison, alternative, job or integration, decision details. [keyword-strategy.md](references/keyword-strategy.md)
- **Refresh before publish.** Pages at positions 4 to 20 and high-impression low-CTR pages come first. Five threads agree this is the best queue; one operator tripled clicks in 2 weeks by retitling pages with 8,000 to 9,000 impressions and no clicks.
- **Information gain or no page.** Write one sentence on what the page adds that the top results lack: data, a test, screenshots, a decision rule, a price. No sentence, no page.
- **Answer first.** Direct answer in the first 2 to 3 sentences under each heading (eight threads agree), exact facts over adjectives.
- **Link to money pages.** Adding 10 internal links per page lifted daily clicks 15.1% to 19.4% vs controls (Quattr, about 50,000 pages, 2025).
- **Programmatic only with a distinct data payload per URL.** Pilot 5 to 20 pages, scale after indexing plus demand. [programmatic-seo.md](references/programmatic-seo.md)
- **Judge a page at 90 and 180 days.** No impressions at 6 months: rewrite, merge, relink or drop.
- **Change one class of pages at a time, with a control group.** Never read results during a core update rollout.
- **Earn links to the pages that make money;** never buy links that pass ranking credit. [links-and-pr.md](references/links-and-pr.md)

## Benchmarks to check first

| Metric | Typical | Source, year |
|---|---|---|
| Organic CTR, position 1 / 2 / 10 | 4.72% / 1.90% / 0.22% median | SmartSites 2025 to 2026 |
| Organic conversion rate | 3.3% median (SmartSites); 4.9% average (Ruler) | 2026 |
| Organic conversion: software / services / retail | 7.9% / 8.1% / 2.0% | Ruler Analytics 2026 |
| Outbound clicks when an AI Overview shows | -39.8% | Randomized experiment, 2026 |
| New article: first impression / page-one week | 10 days / 154 days median | murkuz 2025 to 2026 |
| Monthly organic clicks, 100 to 200 indexed pages | 945 median | Ahrefs June 2026 |
| Sites passing Core Web Vitals, mobile | 48% | HTTP Archive 2025 |
| Digital PR links per practitioner per month | 15.58 weighted average | BuzzStream 2025 |

Vendor and agency datasets dominate SEO benchmarks; no credible top-quartile figures exist for most metrics. Say so instead of inventing one. Full tables: [benchmarks.md](references/benchmarks.md).

## After a traffic drop or a core update

1. **Measurement or real?** Compare GSC clicks with GA4 organic sessions; check the tag, consent banner and property.
2. **Google only?** Compare Bing, DuckDuckGo and ChatGPT referrals over the same window. Everything fell = technical (robots.txt, `noindex`, canonicals, redirects, server errors). Only Google = algorithmic.
3. **Wait for the rollout to finish** (status.search.google.com). Moves within about 5% are noise.
4. **Find the shape:** which page groups, query families and search types (Web, Image, Video) lost; did position fall or only CTR (an AI Overview or video block above you)?
5. **Pair each losing page with the page that beat it** and name the reason: intent, first-hand evidence, freshness, format, product ownership.
6. **Fix 5 former top pages at a time** with original material, measure against untouched pages, then the next 5. Title tweaks, bulk pruning by word count and routine disavows did not bring recoveries in operator reports.

Full diagnosis order: [measurement.md](references/measurement.md). Recovery tactics: [content-playbook.md](references/content-playbook.md).

## When practitioners and the data disagree

| Topic | Operators say | Data says | Rule |
|---|---|---|---|
| Content length | Sub-500-word answers rank top 3; skyscrapers win links | Word count uncorrelated with rank in 6,824 pages (p = 0.603) | As long as the answer needs; expand pages that reach page two |
| Links needed? | Seven threads ranked new sites with zero links on KD 0 terms (mostly 2018 to 2022) | Top-1 pages had 168% more linking domains than #5 (1M URLs, older); AI visibility tracks mentions | No links for long-tail; links to money pages for competitive terms |
| AI content | Scaled AI sites reached 216,000 visits | 72 of 208 AI pages deindexed vs 3 of 141 rewritten; Google: scaled content is spam regardless of author | AI drafts, human facts and first-hand detail, never unreviewed volume |
| Pruning | Seven threads pair pruning with recoveries | Never isolated; word-count pruning showed no recovery; one case +37% clicks uncontrolled | Merge and remove by role and demand, not word count |
| FAQ schema and llms.txt for AI | "ChatGPT cited us after adding FAQ schema" | Schema: AI Overviews -4.6% vs controls (Ahrefs diff-in-diff); 97% of llms.txt files got no bot visits | Skip as AI levers; write passages that answer sub-queries |
| Disavow | Routine "toxic link" cleanup | No measured effect without a manual action | Disavow only with a manual action |
| Programmatic indexing | "1,151 pages indexed in 2 days" | 60% of an 800-page build deindexed by month 4; 86% of 120,000 pages had zero impressions before a collapse | Unique data per page, pilot first |

## Never

- Never buy links that pass ranking credit, run PBNs, or hide keyword anchors in embeds.
- Never publish unreviewed AI text at scale, fake first-hand experience, invent statistics, or create near-duplicate pages that only swap a keyword.
- Never place content on another site to exploit its authority (site reputation abuse).
- Never block search crawlers (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot) without the owner choosing to.
- Never use hidden text, cloaking or prompt-injection copy aimed at AI, or post undisclosed sockpuppet reviews and Reddit answers.
- Never change URLs, migrate a domain or switch themes without a redirect map and a before/after crawl.
- Never promise rankings, traffic or AI recommendations.
- Never publish, change live pages, send outreach or alter robots.txt without the owner's approval. Draft first.

## Working rules for the agent

- Read-only by default. Draft pages, briefs, title changes, outreach and redirect maps; the owner approves before anything ships or is sent.
- Label every claim: platform rule, experiment, dataset (vendor or not), case study, or operator report.
- Keep a dated change log per page group and a control group; re-measure before claiming a result.
- Use GSC and GA4 as ground truth; third-party traffic estimates undercount and misread.

## References

| File | Use it for |
|---|---|
| [keyword-strategy.md](references/keyword-strategy.md) | Demand families, scoring formula, SERP difficulty reads, finding queries tools miss, intent and audience checks, clustering |
| [content-playbook.md](references/content-playbook.md) | Page types by priority, writing that wins, titles, AI drafting rules, internal linking, refresh and pruning, writers, distribution |
| [templates.md](references/templates.md) | Verbatim briefs, comparison and alternatives page skeletons, refresh checklist, outreach and PR emails, prompts |
| [programmatic-seo.md](references/programmatic-seo.md) | Playbooks, quality gates, pilot sequence, indexing, failure postmortems |
| [ai-answers.md](references/ai-answers.md) | AI Overview and ChatGPT evidence, retrieval-first procedure, platform table, measurement, GEO tactics that failed |
| [links-and-pr.md](references/links-and-pr.md) | Link policy, tactics by cost, digital PR procedure, outreach yields, what not to buy |
| [technical.md](references/technical.md) | Eligibility checks, canonicals, sitemaps, Core Web Vitals, AI crawler table, migrations, disaster table |
| [measurement.md](references/measurement.md) | GSC regex and tricks, dashboard, experiment method, traffic-drop diagnosis |
| [buying-seo.md](references/buying-seo.md) | Break-even math, what owners pay, agency questions and red flags, hiring writers, minimal tool stack |
| [benchmarks.md](references/benchmarks.md) | Metric tables with source and year |
| [mistakes.md](references/mistakes.md) | Mistake, what it cost, do instead |
| [plan-90-days.md](references/plan-90-days.md) | Phase plan with exit checks and the ongoing cadence |
| [by-niche.md](references/by-niche.md) | Ecommerce, SaaS, B2B services and agencies, local content, content and affiliate sites, digital products, multi-market |
| [sources.md](references/sources.md) | Research sources, harvested skills with licenses, Reddit threads with upvotes |

Sibling skills: `local-seo` (GBP, reviews, map pack, local AI answers), `website-conversion` (turning visits into leads and sales), `organic-social` (social distribution), `paid-ads` (Google Ads tests and Shopping), `email-sms-loyalty` (capturing and nurturing readers), `ecommerce-brand` (marketplace SEO and feeds), `b2b-outbound` (when the market is too small for search).
