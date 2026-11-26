# 90-day plan

For a new or stalled site. Order matters: measure, then fix eligibility, then build commercial pages, then refresh what already ranks, then earn authority, then scale only what worked. Adapted from the 2026 deep research plan ([sources.md](sources.md)) and the operator patterns in this skill. Each phase ends with a one-page owner report: what changed, the numbers, what they must decide.

A brand-new domain with no pages: days 1 to 15 are setup plus the first 5 money pages; expect impressions in about 10 days and first page-one weeks around month 5 (murkuz 2025 to 2026 median: 154 days). Tell the owner that up front.

## Days 1 to 15: instrument and triage

- GSC Domain property, GA4 with one primary conversion and up to three secondary events, GSC linked to GA4, Bing Webmaster Tools, AI channel group, "How did you hear about us?" field ([measurement.md](measurement.md)).
- Brand vs non-brand regex. Baseline: last 12 months of non-brand clicks, organic conversions, page-one query count.
- Export every indexed URL. Give each one role: **sell** (product, service, pricing, category), **decide** (comparison, alternative, best-for, review), **do** (use case, integration, template, tool, how-to with the product), **prove** (case study, original data, methodology), **support** (informational that feeds a money page), or **remove/merge**.
- Eligibility check on priority URLs: crawlable, 200, indexable, canonical, linked ([technical.md](technical.md)).
- robots.txt and CDN check for Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, Claude-SearchBot. The training-bot decision (GPTBot, Google-Extended, ClaudeBot) is the owner's.
- Owner interview ([SKILL.md](../SKILL.md) first-session questions). Collect proof: customer numbers, screenshots, photos, test results, quotes the owner can approve.

Exit check: dashboard live, URL inventory with roles, list of blocking technical issues fixed or scheduled.

## Days 16 to 30: commercial demand map and first money pages

- Build the demand map around the five families: `[category]`, `[category] for [use case or audience]`, `[brand] vs [competitor]`, `[competitor] alternative`, `[product] + integration / workflow / problem` ([keyword-strategy.md](keyword-strategy.md)). Ecommerce: category + attribute, "best [product] for [need]", gift and occasion terms. Services: service + problem, cost and pricing questions.
- For each target record: current rank, whether the SERP shows an AI Overview, who ranks (big brands, forums, small sites), the conversion path, and "can the searcher get the full answer without visiting a site?" Prioritize where a visit is still needed.
- Ship or overhaul 5 to 10 decide and sell pages, each with selection criteria, first-party evidence, screenshots or photos, and a CTA matched to intent ([templates.md](templates.md)).
- Link each new page from at least 2 relevant existing pages. Google requires one crawlable link; two contextual paths is an operating heuristic.

Exit check: pages live, indexed (URL Inspection), linked.

## Days 31 to 45: refresh and cluster sprint

- Pull queries and pages at positions 4 to 20 and pages with rising impressions but CTR under 1%. Refresh those before writing new informational posts ([content-playbook.md](content-playbook.md)).
- Add sections for the GSC queries a page gets impressions for but does not answer; cut obsolete parts; rewrite titles; add contextual links from informational pages into money pages.
- Merge cannibalizing pairs (301 the weaker, update internal links).
- Map one cluster per money topic: problem, causes, alternatives, selection criteria, implementation, integrations, troubleshooting, cost, comparison, evidence, tool or template. Write the highest-value missing node first.

Exit check: refresh log with date, page, change, and a control group of similar untouched pages.

## Days 46 to 60: one asset worth citing

- Build one link and citation asset from data only this business has: a benchmark from customer data, an original test, a price index, a calculator, a teardown dataset, a small survey. Publish method, sample, dates and limits ([links-and-pr.md](links-and-pr.md)).
- Pitch 30 to 100 relevant journalists, bloggers and newsletter writers with the finding in the subject line.
- Start the off-site list: review and comparison sites in the category, directories that matter, communities where buyers ask, podcasts and YouTube channels that cover the category.

Exit check: asset live, pitches sent, links and mentions logged.

## Days 61 to 75: AI retrieval pass

- For the 10 most important buyer questions, generate fan-out sub-queries and check each maps to a section with a direct answer ([ai-answers.md](ai-answers.md)).
- Add missing facts (prices, limits, compatibility, who it is not for) as text. Not FAQ schema for its own sake.
- Freeze a prompt panel; first monthly run across ChatGPT, Perplexity, Gemini, AI Mode; log mentions, citations, rivals named, cited domains, wrong facts.

Exit check: panel baseline, wrong facts fixed at their source.

## Days 76 to 90: kill, scale or iterate

- Score each new or updated page: impressions, position trend, clicks, conversions, assisted conversions, links or citations.
- Scale a page type (more comparisons, a programmatic set, more integrations) only when the first batch shows indexing plus demand or conversions ([programmatic-seo.md](programmatic-seo.md)).
- Merge, delete or noindex pages with no role. Keep low-traffic pages that assist conversion, support a cluster, earn links or carry first-party evidence.
- Set the ongoing cadence below and the next 90-day priorities.

## Ongoing cadence

| When | What |
|---|---|
| Weekly | GSC check for indexing errors and sudden drops on money pages; ship planned pages; 1 to 2 pitches or community answers |
| Monthly | Owner dashboard; striking-distance list; refresh 2 to 5 pages; AI prompt panel; new rivals in the SERP |
| Quarterly | Content inventory roles; prune and merge; one new citable asset; review the demand map |
| After a core update | Wait for the rollout to finish, then compare by page group vs control before acting |

Operating loop after day 90: observe, find the biggest bottleneck, change one class of pages, wait for evidence, compare with an unchanged group, keep, reverse or scale.
