# Programmatic SEO: many pages from one template, done right

Programmatic pages work when each URL represents a genuinely different entity, task or decision backed by its own data. They destroy sites when templates swap a keyword. Google's scaled content abuse policy (March 2024) applies whether humans, AI or both made the pages. Decision rule (deep research 2026): if removing the substituted name leaves essentially the same page, do not scale it. Frameworks adapted from coreyhaines31/marketingskills, AgriciDaniel/claude-seo and kostja94/marketing-skills (MIT) and aaron-he-zhu/aaron-marketing-skills (Apache-2.0); see [sources.md](sources.md).

## What worked and what blew up

| Case | Result |
|---|---|
| Polish legal-tech: 1,125 genuinely distinct letter and template pages | 4,863 monthly search clicks (3,591 Google, 1,272 Bing) by November 2025 (SEO Savages case study) |
| 300+ substitution pages ("can I use cottage cheese instead of sour cream in baking") with exact ratios and baking context | Flat for 5 months, then dozens ranked together in month 7; 700,000 impressions over 12 months (r/juststart, 52) |
| About 800-page build | About 60% deindexed by month 4, nearly all near-copies of existing comparison content; every survivor had at least one proprietary data point (r/bigseo, 49) |
| About 120,000 URLs in 10 languages, 86% with zero impressions | Impressions fell from about 8,900 a day to 300 in one hour; noindexing 80,000 brought no recovery (r/TechSEO, 148) |
| About 62,000 city x trade URLs for a field-service software | 97% of clicks but 0.3% CTR and about 33 brand clicks: pages served homeowners, not software buyers; then clicks 207 to 13 overnight (r/TechSEO, 31) |
| Programmatic "x vs y" and "alternatives to x" pages on an affiliate site | Little traffic but a reported 50% conversion rate (r/juststart, 74) |
| Confidential SaaS, programmatic pages | Demo requests +72% in four months (vendor case listing) |

## Playbooks (pattern, URL, value bar)

| Playbook | Query pattern | URL | Minimum to be non-thin |
|---|---|---|---|
| Templates | "[type] template" | `/templates/[type]/` | Actually usable, several variations, near paid quality |
| Curation | "best [category]" | `/best/[category]/` | Real criteria and testing, visible update date, not ranked by commission |
| Conversions and calculators | "[X] to [Y]", "[X] calculator" | `/convert/[from]-to-[to]/` | A working tool plus explanation of the result |
| Comparisons | "[X] vs [Y]", "[X] alternative" | `/compare/[x]-vs-[y]/` | Sourced, dated feature and price data per pair |
| Examples | "[type] examples" | `/examples/[type]/` | Real examples with commentary |
| Locations | "[service] in [location]" | `/[service]/[city]/` | Real local data: providers, prices, regulations, distances. City-swap pages are the classic failure (local depth in `local-seo`) |
| Personas and industries | "[product] for [audience]" | `/for/[persona]/` | Segment-specific workflows, integrations, compliance and proof |
| Integrations | "[A] [B] integration" | `/integrations/[product]/` | A working integration, setup steps, use cases, screenshots |
| Glossary | "what is [term]" | `/glossary/[term]/` | Deeper than a dictionary, examples, linked related terms. Most exposed to AI Overviews |
| Directory and profiles | "[category] tools", "[entity]" | `/directory/[category]/` | Filters, comparisons, data per record (one 350-site operator runs this model with a database rather than an article per entry, r/juststart, 253) |
| Translations | localized pages | `/[lang]/[page]/` | Native review, hreflang, per-market keyword research |

Layer them only when both layers add data ("best coworking spaces in San Diego" = curation x location) (coreyhaines31/marketingskills, MIT).

## Data comes first

Data defensibility ladder, strongest first: 1 proprietary (you created it), 2 product-derived (your users' aggregated data, with minimum cell sizes and "as of [date]"), 3 user-generated (moderated, consented), 4 licensed (exclusive), 5 public or scraped (weakest) (coreyhaines31 and kostja94, MIT). If the only source is public or scraped and the template adds no synthesis, calculator or editorial angle, do not generate the set (aaron-he-zhu, Apache-2.0).

Per-record gate (AgriciDaniel/claude-seo, MIT; thresholds are tool heuristics, not Google numbers):
- Each record needs enough unique attributes for a distinct page. Flag records with over 80% field overlap as near-duplicates.
- Unique % = words unique to this page / total words on page, measured against the rest of the set (count template boilerplate, exclude shared nav). Under 40% = thin; under 30% = stop.
- Metadata counts too: unique strings that share one generated shape ("[Title]. Try it free now.") fail.
- The standalone test, verbatim: "Would this page be worth publishing even if no other similar pages existed?"

Operators add: 12+ data points per page written as full sentences (r/juststart, 335), and "no anchor, no project": at least one data point per page that is not on the open web (r/bigseo, 49).

## Pilot, then scale

1. **Kill test before building:** search 6 target queries (head plus 5 long tails). If 9 of 10 results look alike, especially interchangeable comparison pages, cancel (r/bigseo, 49).
2. **Editorial layer first:** 5 to 10 handwritten pillar pages; every programmatic page gets links from at least 2 editorial pages (r/bigseo, 49; the pattern held for two later clients).
3. **Pilot 5 to 20 pages by hand-check** (deep research 2026) or the 20 to 50 strongest records (coreyhaines31). Verify indexing in URL Inspection, impressions in GSC and at least one conversion path.
4. **Scale in batches of 50 to 100,** wait 2 to 4 weeks between batches, human-review a 5 to 10% sample, never ship 500+ at once without review (AgriciDaniel, uncited heuristics).
5. **Expect a delay:** the substitution site sat flat for 5 months before ranking (r/juststart, 52). Judge at 6 months.

## Template anatomy

- H1 with the target query; a unique intro that uses the record's facts, not swapped variables.
- **Evidence block:** the per-record data (tables, verified stats, real attributes, photos, prices with "as of [date]"). This is what makes the URL non-thin (kostja94, MIT).
- **Decision block:** comparison, recommendation, next step.
- Conditional sections that branch on field values and hide empty fields.
- Related pages by shared attributes (3 to 5 links), breadcrumbs, CTA matched to intent.

## AI in the pipeline

- Pass the record's JSON into the prompt; the data is the source of truth, AI only shapes phrasing, section order and FAQ depth. Forbid invented numbers and citations; block publishing if required fields are empty (kostja94, MIT).
- Vary structure by intent flags, not adjectives. Run n-gram overlap checks before publishing; flag phrases on more than 30% of pages (aaron-he-zhu, Apache-2.0, uncited threshold).
- Fixing homogenized live pages: remove pure filler first, then rewrite formulaic lines with 8 to 15 variants, one category per round, re-scan after each (kostja94, MIT).

## Indexing and architecture

- Hub (category) page links every spoke; spokes cross-link by shared attributes; no orphans; separate XML sitemaps per page type (50,000 URLs or 50 MB per file); `lastmod` = real data update, not generation time; noindexed pages stay out of sitemaps.
- If a programmatic page overlaps a hand-written one, the manual page wins the canonical.
- Build inside the main site's CMS if it can hold the set, so pages inherit authority and links. The platform must render server-side HTML, allow per-item noindex and canonical, and refresh data without a full rebuild (coreyhaines31, MIT).
- "Discovered, currently not indexed" on a programmatic set is usually a value verdict. One operator pushed 94% of 2,500 URLs into the index via the Indexing API vs 8.4% via sitemap (r/TechSEO, 26), but Google limits that API to job posting and livestream pages and retention was not measured. Do not use it as a workaround; improve the pages.
- Cross-post the same template to Bing early: Bing indexed one set in 24 hours and fed Copilot citations by day 5 (r/juststart, 20).

## Cleanup when a set fails

Freeze generation. Keep pages with impressions or conversions; 410 the rest or noindex those users need; 301 only to real replacements. Hold all other site changes so the effect stays readable. Expect slow reprocessing: two postmortems (sitemap 74,876 to 9,311 URLs; 80,000 noindexed) reported no recovery months later (r/TechSEO, 31 and 148).

## Tricks most owners miss

- The best programmatic sets for small businesses are small: 30 to 300 pages built from data the business already has (integrations, templates, product specs, service x industry with real case studies).
- Programmatic "rival vs rival" and "alternatives" pages convert well but need a single source of truth per competitor (one file with dated, sourced prices and features) so one update fixes every page ([templates.md](templates.md)).
- Glossary sets are the most exposed to AI Overviews; integration, template and calculator sets the least.
- Monitor one representative URL per template for changes to titles, robots and canonicals instead of thousands of alerts (r/bigseo, 60).
