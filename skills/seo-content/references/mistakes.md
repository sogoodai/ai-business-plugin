# Expensive mistakes

Two tables: what the research shows, and what operators report losing. Thread URLs in [sources.md](sources.md).

## From the research (2024 to 2026)

| Mistake | What it costs | Do instead |
|---|---|---|
| Forecasting informational traffic on old CTR curves | AI Overviews cut outbound clicks 39.8% when shown (randomized, 2026); Ahrefs puts the position-1 CTR loss at 58% (Dec 2025 data) | Forecast informational pages at 40 to 60% of old CTR when an AIO shows; shift the mix to commercial pages |
| "20 articles a month" as the KPI | Only 1.74% of a broad 1M-URL sample reached a top 10 within a year (6.11% for filtered English content) (Ahrefs 2025) | KPI = non-brand clicks, commercial-query clicks and organic conversions |
| Counting articles as topical authority | Topic share barely correlated with rank; coverage depth did (510 sites, 2026) | Map buyer questions and fill missing nodes; stop when pages would paraphrase |
| Buying links because rivals have them | Google link spam policy; 87.3% of digital PR practitioners never pay (BuzzStream 2025) | Earned assets, partners, journalist requests |
| Scaling programmatic pages before proving one template | Scaled content abuse policy multiplies one mistake across thousands of URLs (Google, March 2024) | 5 to 20 hand-checked pages, verify indexing and value, then scale |
| Judging SEO on sessions only | Organic produced 29% of conversions from 21.5% of visits (median, SmartSites 2026) | Report conversions and revenue by landing page group |
| Treating GSC average position as a KPI | It is an average over queries and surfaces; new long-tail impressions make it "worse" | CTR and conversions by query family |
| Mass "keyword + generic explanation" libraries, near-duplicate template pages, parasite placements | Directly targeted by 2024 spam policies; site-reputation abuse tightened November 2024 | One page per real intent, with distinct value |
| Reacting during a core update rollout | Rankings swing both ways mid-rollout (November 2026 update started November 10) | Wait for "complete" on the status dashboard, then compare page groups |
| Blocking AI search crawlers by accident | Not shown in ChatGPT search if OAI-SearchBot is blocked (OpenAI) | Check robots.txt and CDN bot settings on day one |

## From operators

| Mistake | What it cost | Do instead |
|---|---|---|
| Spending on SEO without break-even math | $60,000 in a year with no return; at a 20% margin it needed $300,000 of extra revenue, doubling a $300,000 business (r/SEO, 164) | Compute required revenue before signing ([buying-seo.md](buying-seo.md)) |
| Contract promising "page one in a month" | Delivered rankings for phrases nobody searches (r/SEO, 164) | Name the exact keywords and conversions in the contract |
| Not auditing month-one deliverables | $500 for 10 hours: one 200-word article on a link farm, 3 nofollow forum links (r/SEO, 184) | List every placement and hour after month one |
| Agency holding the CMS, GA or GSC | Lawyers to regain WordPress access; a client paying $13,000 a month got no reporting (r/SEO, 195) | Owner keeps admin on every account |
| Cheap provider swap plus rebrand and new URLs at once | Ranking keywords 3,000+ to 250, revenue down (r/SEO, 136) | One change at a time; pay for migration work |
| Old domain switched off before redirects | Impressions 700,000 to 14,000 a month, no recovery after 4 months (r/TechSEO, 2026) | Old server keeps serving 301s until the full map ships |
| Translation plugin without an indexing audit | 20,000 articles became 7M URLs; pageviews 2M to under 100,000 (r/SEO, 102) | Audit what a plugin makes indexable |
| Ranking for the wrong audience | 9,500 of 10,000 sessions were students; every demo came from word of mouth (r/SEO, 106) | Check who searches before writing |
| Programmatic pages with no demand | About 120,000 URLs in 10 languages, 86% with zero impressions; impressions fell 8,900 a day to 300 and noindexing 80,000 brought no recovery (r/TechSEO, 148) | Gate each programmatic URL on demand and unique data |
| Pure AI pages on a specialist topic | 72 of 208 AI pages deindexed vs 3 of 141 hand-rewritten; rewritten pages got 6.7x the impressions (r/blogging, 57) | AI drafts, expert rewrites |
| Outsourcing writing without trials | $800 to $1,000 lost on articles that missed; every top page was self-written (r/juststart, 73 and 131) | Brief, paid trial, compare performance |
| Bulk pruning by word count | Thousands of sub-200-word articles removed, no recovery (r/SEO, 97) | Prune by role and demand, test a sample |
| Shortening titles by cutting synonyms | -27% organic traffic in a controlled test (r/TechSEO, 225) | Keep synonyms |
| Retitling to fix a core-update loss | 5 to 10 articles retitled, none recovered (r/SEO, 1,399) | Fix page quality and evidence, not snippets |
| Major keyword page on the homepage | Peaked at #6; moving it to a dedicated URL later cost 4 months off page one (r/juststart, 258) | Dedicated URL from day one |
| Routine disavow | No measurable effect without a manual action; 1,200 domains disavowed, no recovery (r/TechSEO, 225 and 51) | Disavow only with a manual action |
| Redesign or theme change on the live site | Pageviews 20,729 to 16,621 plus $400 repairs; another site halved (r/juststart, 76 and 85) | Staging, speed and template checks first |
| Chasing PageSpeed lab scores | Hours for a few points, no revenue (r/blogging, 72) | Fix field-data failures only |
| Third-party traffic estimates as truth | Ahrefs showed under half of a site's real traffic (r/juststart, 84); an $85,000 a year tool showed 0 keywords where Ahrefs showed 1,300 (r/bigseo, 78) | GSC and GA4 are ground truth; test tools on your own domain |
| Paying for SEO tools year-round | 90% of the value comes in one month for a small business (r/bigseo, 38); $211 charged after a missed cancel confirmation (r/SEO, 151) | One month or a trial, export, cancel with screenshots |
| Low-intent traffic chased for volume | Six-figure traffic sites earning $200 to $300 a month (r/SEO, 285); a viral spike lifted pageviews 50% with flat income (r/juststart, 79) | Score keywords by intent and CPC |
| AI-generated affiliate or product links unchecked | 82% of AI product links fake in one audit (r/juststart, 64) | Click-test every link; one broken button was worth $812 a month (r/juststart, 76) |
| Leaving a winning site on autopilot | $5,000 to $6,000 a month fell to about $2,500 (r/juststart, 69) | Monthly refresh and link checks |
| One traffic source or one affiliate program | Amazon's April 2020 cut: about $7,000 lost in a month; another site lost 60% of commissions (r/juststart, 140 and 107) | Diversify: email list, second program, direct products |
