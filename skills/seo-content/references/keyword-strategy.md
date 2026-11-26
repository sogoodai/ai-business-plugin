# Keyword strategy: what to target, in what order

The 2026 rule: pick queries where a visit is still needed and the searcher can buy. Informational queries increasingly end inside an AI Overview (outbound clicks -39.8% when one appears, randomized 2026 experiment); commercial, comparison, product, integration, tool and first-party queries keep their value. Thread URLs and research links in [sources.md](sources.md).

## Step 1: start from money, not volume

Ask the owner for the 3 offers that make the most profit, the customer's words for the problem, the rivals buyers compare them with, and the questions sales or support hear every week. Then build the demand map in five families (deep research 2026):

| Family | Pattern | Examples |
|---|---|---|
| Category | `[category]`, `[category] for [audience or use]` | "invoicing software for freelancers", "linen bedding for hot sleepers" |
| Comparison | `[brand] vs [rival]`, `[rival A] vs [rival B]` | "Asana vs Todoist" written by a tool that is neither |
| Alternative | `[rival] alternative(s)`, `cheaper than [rival]`, `switch from [rival]` | "Mailchimp alternatives for Shopify" |
| Job or integration | `[product] + [integration / workflow / problem]`, `how to [task] with [tool]` | "sync Stripe to Xero", "send invoices from Notion" |
| Decision details | pricing, cost, review, "is it worth it", "best [product] for [need]" | "how much does a website redesign cost", "best standing desk for small spaces" |

Ecommerce: category + attribute ("long narrow couch good for sleeping"), "best [product] for [need]", gift and occasion terms, care and sizing questions. Services and B2B: service + problem, cost and pricing questions, "[service] for [industry]", compliance and template queries.

Operator evidence that the comparison family works: a workflow tool ranking "Asana vs Todoist" and "Basecamp vs Asana" grew 0 to 200,000+ monthly visits in under 2 years with no active link building (r/SEO, 219). A UK small business with a £0 SEO budget targeted "compare" and "switch" queries after Google Ads CPCs nearly quadrupled in September 2021: #1 for 10 high-converting terms by March 2022 and 162 organic leads in a month (r/content_marketing, 118). Brian Dean's order for bottom-funnel work: "tools for X", then "X alternatives", then "X pricing" (via r/blogging, 31).

## Step 2: score each candidate

Record per keyword: monthly volume, CPC, current rank (GSC), who ranks (brands, forums, small sites), AI Overview present (Y/N), intent (buy, compare, learn), the page that would answer it, and "can the searcher get the full answer without visiting?" Then:

```
value score = volume x CPC x intent weight x (1 - AIO click loss)
  intent weight: buy 1.0, compare 0.8, problem-aware 0.4, trivia 0.1
  AIO click loss: 0.4 if an AI Overview shows and the answer fits in it, else 0
winnability = can we beat the weakest page in the top 5? (see step 3)
priority = value score, filtered to winnable, sorted
```

CPC is the cheapest commercial-value proxy. Two operator formulas: `(volume / KD) x CPC` with Ahrefs data (r/bigseo, 54) and `volume x advertiser competition x CPC` from Keyword Planner, where 1,000 x 0.8 x $1.00 = 800 beats 1,500 x 0.8 x $0.50 = 600 (r/bigseo, 39). Neither is a difficulty measure.

Buyer-intent content earns $80 to $100 per 1,000 visits on affiliate sites vs about $23 to $42 RPM for display ads (r/juststart, 87): intent beats volume even on content sites.

## Step 3: judge difficulty from the SERP, not the tool

- Keyword difficulty scores are a link hint, not a forecast. Ahrefs KD is roughly the referring domains of the top pages (Ahrefs-affiliated poster, r/bigseo, 86). Tools undercount: one operator's real traffic was more than double Ahrefs' estimate (r/juststart, 84).
- **Manual SERP read, 2 minutes:** page one has forums, Reddit, Quora, thin listicles, mismatched pages or tiny sites = winnable. Nine of ten results near-identical from big brands = skip for now.
- **Loose-match gap:** a rival ranks with a page built for a different query (ranking for "top homes in [city]" with a "homes for sale" page). Build the exact-intent page (r/SEO, 114).
- **Format beats authority:** a site with Authority Score 10 and no links to the page outranked a stronger site for "airdrop for windows" (2,400/month) because it had the format the SERP wanted, "10 alternatives, tested" (r/TechSEO, 2026). Match the dominant format first.
- **DR as a rough KD ceiling:** a DR 20 site starts with KD 20 or below (r/SEO, 114; arbitrary but useful). Move to harder terms only after similar-difficulty pages on the site already rank (r/juststart, 155).
- **Manual competition count:** pursue topics with only 3 or 4 truly relevant quality pages in the top results; defer those with 50+ while the site is new (r/SEO, 128).

## Step 4: find the queries tools miss

- **GSC first.** Queries already getting impressions at positions 9 to 20 are the best shortlist: Google already associates you with them (r/SEO, 339 and 269).
- **Zero-volume keywords are real.** Five threads agree: one zero-volume article drove about half of an 82-article site's 3,204 monthly users (r/juststart, 70); zero-volume buyer-intent articles average about 50 visits a month each (r/juststart, 87). Put them in every brief because competitors skip them.
- **Alphabet-soup autocomplete:** "best shoes for" + a to z and 0 to 9 = 36 requests gave 679 keywords; aa to zz = 676 requests gave 3,948. Run word orders separately, set country and language variant, and try Images, Shopping and YouTube surfaces (r/juststart, 182). Longer stems ("which [kw] for", "how [kw] can") beat bare modifiers capped at about 25 suggestions (r/bigseo, 102).
- **Question stems with forum SERPs:** a stem like "can you camp in" + variants, keep those where page one is forums and no dedicated article; nearly every post indexed near the top of page two by month 7 without links (r/juststart, 186).
- **Content Explorer "weak site, big traffic":** pages with high traffic on sites with DR up to about 10, or pages with 1,000+ traffic and under 5 referring domains. Found two 40,000+/month keywords where a DR 7 site with under 10 pages ranked; a site built for under $2,000 then reached about $950/month (r/juststart, 695; one commenter found nothing).
- **Competitor gap:** rival domain, non-branded keywords, lowest DR in top 5 up to 39, KD up to 25 (r/SEO, 122). Rival `sitemap_index.xml` lists every topic they cover (r/blogging, 109).
- **Support inbox, sales calls, site search, Reddit threads in the niche.** These hold the exact buyer wording. Misdirected support emails revealed buyers searching for a similarly named brand in one case (r/juststart, 224).
- **Buy and use the product** (about $50) to find 10 to 20 article ideas tools missed; map a niche into brands, problems and accessories (r/juststart, 206).
- **Country wording:** Japanese users searched "ipad usbメモリ" (2,900/month) vs "iPad ファイル 転送" (260); Indonesians "dari HP ke laptop" (3,600) vs 20 for the PC wording (r/TechSEO, 2026). Research each market in its own words.
- **Emerging topics** in fast-moving industries are invisible to lagging tools and beat incumbents (r/juststart, 202).

## Step 5: check intent and audience before writing

- **Search the query logged out and ask: who is this searcher?** One B2B SaaS got 9,500 of 10,000 monthly sessions from students searching "models of xyz" for quiz answers; every demo came from word of mouth (r/SEO, 106). A programmatic section of about 62,000 URLs targeted homeowners for a field-service software (r/TechSEO, 31). Traffic without the buyer is a cost.
- Hundreds of sites with six-figure traffic earn $200 to $300 a month because the queries have no purchase intent ("Madagascar character names" vs "hormone balance supplement") (r/SEO, 285).
- **Prefer queries that need more than one sentence to answer.** One operator won many featured snippets on one-line answers under 500/month and got few clicks; one long-answer page drove 70% of traffic (r/juststart, 258). AI Overviews make this rule stronger.
- **AI Overview exposure rises with query length.** In a 2025 analysis of 100,000+ keywords, one-word queries triggered AIOs 12.78% of the time vs 69.21% for ten-word queries; 100,000+ volume heads triggered only 9 to 12% (r/content_marketing, 29). Long informational questions are the most exposed; long commercial constraints still convert.

## Step 6: cluster and map, one page per intent

- **SERP-overlap rule:** if 3+ page-one results rank for both queries, one page; fewer than 3, separate pages (r/juststart, 162).
- **Cluster template** (deep research 2026): problem, causes, alternatives, selection criteria, implementation, integrations, troubleshooting, cost, comparison, evidence, tool or template. Write the highest-value missing node first; stop when new pages would paraphrase old ones.
- Coverage depth correlates with rank (deepest quartile average position 9.5 vs 13.5 for shallowest, 510 sites, 2026); share of the site devoted to the topic barely does. Cover buyer questions fully, do not count articles.
- Category gate used by one affiliate operator: approve a category only if it has at least 10 keywords with volume over 100 and KD under 10 (r/juststart, 364).
- **Keyword map sheet:** keyword, family, volume, CPC, KD, AIO (Y/N), intent, target URL (one per keyword, existing or new), status, date published, GSC position at 90 and 180 days. No keyword gets two target URLs.

## Tricks most owners miss

- Validate a money keyword with $100 to $300 of Google Ads before writing a long page: if the paid click does not convert, the organic one will not either.
- "Rival vs rival" pages where you are neither earn trust and traffic; end with "when neither fits" and your option.
- A query where no credible page exists to cite is an underserved niche (r/juststart, 77). So is a SERP where the top results answer a different question.
- Review cheaper popular products first in product content: brands send premium units to big publishers, so competition clusters there (r/juststart, 100).
- Seasonal money pages need to be live 6 to 8 weeks early: finance "best X" pages published in November and December ranked for January demand and doubled revenue ($3,773 to $7,589) (r/juststart, 75); a niche Black Friday page on a 54-article site held #2 most of November (affiliate £317 to £3,865) (r/juststart, 76).
