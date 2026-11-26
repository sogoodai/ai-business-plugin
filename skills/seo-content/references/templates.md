# Templates: briefs, page skeletons, checklists, emails, prompts

Fill the brackets with real, owner-approved facts. Never invent prices, features, quotes or numbers. Adapted from coreyhaines31/marketingskills, AgriciDaniel/claude-seo, kostja94/marketing-skills (MIT) and aaron-he-zhu/aaron-marketing-skills (Apache-2.0), plus operator wording where cited; see [sources.md](sources.md).

## 1. Content brief (one per page)

```
Target query: [primary]            Secondary: [3 to 8 close variants, incl. zero-volume ones from GSC or autocomplete]
Page role: sell | decide | do | prove | support      Funnel family: category | comparison | alternative | job | decision detail
Searcher: [who, what they already know, what they want to do next]
SERP read (top 5, ignoring Wikipedia, Reddit, marketplaces): format rewarded [guide | list | comparison | tool | product]; AI Overview [yes/no]; video [yes/no]
What each top result misses: [1 line each]
Information gain (one sentence, mandatory): this page adds [original data | real product example | working tool or template | clearer answer | stronger opinion] that none of them have.
  "More detail" or "better formatting" does not count. No sentence, no page.
Proof we will show: [screenshots, photos, numbers, case result, expert quote, test method]
Outline: H1 / answer paragraph (40 to 60 words, written last) / H2s from buyer sub-questions and GSC queries / decision or comparison table / FAQ from People Also Ask (first sentence answers) / CTA
Fan-out sub-queries to cover: [5 to 10, from "list the searches you would run to answer this"]
Internal links: from [3 existing pages with impressions] to this page; from this page to [money page] with anchor [descriptive]
Title draft: [query] + [reason to click] + [brand if known], about 50 to 60 characters
Length: what the answer needs; reference = top-3 average [n] words, not a target
Done when: facts checked, links click-tested, owner approved, published, URL Inspection requested
```

Website relevance rule: every heading must be something this business can credibly deliver; drop the rest (AgriciDaniel/claude-seo, MIT).

## 2. Comparison page: "[You] vs [Rival]"

```
H1: [You] vs [Rival]: [the deciding difference] ([year])
Last updated [date] · Written by [name, role] · We make [You]; here is how we compared.

TL;DR: [Rival] excels at [strength] but [weakness]. [You] is built for [focus], with [key differentiator].
Choose [Rival] if [their ideal case]. Choose [You] if [your ideal case].

At a glance (table): Best for | Starting price (as of [date]) | Free plan | [3 to 5 deciding features] | Support | Contract
Each cell states the capability or limit, not a bare checkmark. Unknown = "not listed on their pricing page (as of [date])".

Pricing worked example: For a [10-person team / typical order], [Rival] costs about $X a year and [You] $Y, including [add-ons, setup, overages].
Feature sections: 2 to 3 sentences per product, Strengths / Limits, then "Bottom line: choose [Rival] if ..., choose [You] if ...".
Where [Rival] is better: [honest list]
Switching: effort, what transfers, time estimate, migration help.
Proof: switcher quote with name and permission, review-site ratings linked (not marked up as your schema).
CTA: after the table and at the end; none inside the rival's section.
```

Evidence rules (coreyhaines31, MIT): "not observed" is not "doesn't have"; date every competitor fact; state what changed, never why; the page must survive the competitor's own team reading it. Do not mark up third-party ratings in Product schema: Google's review snippet rules disallow ratings aggregated from other sites.

Variants: plural "[Rival] alternatives" (why people leave, criteria, you plus 4 to 7 real options, summary table, recommendation by use case); "[A] vs [B]" where you are the third option (overview, by category, who each suits, then you). Target both word orders.

AI caveat: in 100 B2B "best [category] software" queries (spring 2026), self-promotional listicles earned 323 AI Overview citations, and in 69% of them the answer recommended competitors, not the publisher (Lily Ray study via coreyhaines31). Name the category leader honestly, then show where you go further.

## 3. Single source of truth per competitor (keeps every page current)

```yaml
competitor: [name]
last_verified: [date]
positioning: [one line]
best_for: [...]
not_ideal_for: [...]
pricing:
  - tier: [name]
    price: [number, currency, billing]   # label: measured | user-provided | estimated
    includes: [...]
    hidden_costs: [...]
    source: [url, date]
features:
  - name: [feature]
    status: strong | partial | none | not listed
    note: [...]
    source: [url, date]
common_complaints: [from G2, Capterra, Trustpilot, Reddit, with links]
migration: {difficulty: [low/med/high], exports: [...], time: [...]}
```
Verify prices and major features quarterly and whenever a customer reports a change (coreyhaines31 and aaron-he-zhu).

## 4. Product-led "how to [task] with [product]" page

```
H1: How to [task] [with constraint] (Step by Step)
Answer paragraph: what it takes, how long, what you need.
Before you start: requirements, plan or permission needed.
Steps: numbered, one action each, a real screenshot per step, exact menu names.
Variations: [platform / plan / edge case] sections.
Troubleshooting: [error message]: what it means, fix.
Result: what success looks like (screenshot), next task.
CTA: "Try this in [product]" with a template or deep link to the exact feature.
```

## 5. Refresh checklist (run on a page at positions 4 to 20)

1. Record baseline: position, impressions, clicks, CTR for its top 5 queries (28 days).
2. Name why each of the 3 results above wins: intent, a missing section, freshness, format, links. No reason found = authority gap, build links instead of rewriting (coreyhaines31).
3. Answer in the first two sentences.
4. Add a short section for each GSC query the page gets impressions for but does not answer; answer in its first sentence.
5. Update facts, prices, screenshots, year references; remove obsolete sections.
6. Add internal links from the 3 strongest related pages; link out to the money page.
7. Title: change only if CTR is the problem, and then change only title and description so the result is attributable.
8. Date: over 50% new = new published date; 20 to 50% = "Last updated"; under 20% = keep (aaron-he-zhu, Apache-2.0). Update `dateModified` and sitemap `lastmod`. Never change dates without changing content.
9. Request indexing once; re-check after 3 to 4 weeks. Two rounds without movement: stop editing; it is intent or authority.

## 6. Title patterns by page type (coreyhaines31, MIT)

| Page | Pattern |
|---|---|
| Category or product | [Category] for [Audience] \| [Brand] |
| Pricing | [Brand] Pricing: Plans and Costs |
| Comparison | [A] vs [B]: [the deciding difference] |
| Alternatives | [N] Best [Rival] Alternatives ([Year]) |
| Listicle | [N] Best [Things] for [Audience] in [Year] |
| How-to | How to [Task] Without [Obstacle] |
| Definition | What Is [Term]? [Short payoff] |
| Tool | Free [Thing] [Template or Calculator] ([Format]) |
| Troubleshooting | [Error]: What It Means and How to Fix It |

Low-CTR rewrites: "Home" to "Invoicing Software for Freelancers | Acme"; "Plans That Grow With You" to "Acme Pricing: Plans and Costs"; "Free CRM Templates" (only one is free) to "CRM Template for Small Teams (Google Sheets)". Swap test: if the title could move unchanged to a sibling page, add a page-specific fact (kostja94, MIT). Present bulk changes as a table: Page | Current title | Proposed title | Reason.

## 7. Digital PR pitch (data story)

```
Subject: New data: [single surprising number and what it means]

Hi [first name],

You covered [their specific recent piece] on [date]. We analyzed [sample, source, period] and found [one counterintuitive result].
The biggest gap was [number]; [second useful number].

Method and full table: [URL]. Charts are free to embed with a link.
Happy to send the raw breakdown for [their beat] or a short quote from [name, role] on [specific implication].

[Name], [role], [company], [phone]
```
Plain text, no attachments, one follow-up after 3 to 5 days with one new data point. Skip anyone who has not covered the beat in 6 months.

## 8. Resource or broken-link replacement email

```
Subject: [Their page title]: a broken link and a replacement

Hi [name], your [page] still sends readers to [dead or outdated resource] in the section on [topic].
We published [your resource], which covers [what theirs covered] and adds [what is new: data, tool, updated year].
If it helps your readers, here it is: [URL]. Either way, the old link returns a 404 now.
```

## 9. Journalist request reply (Qwoted, Featured, Help a B2B Writer, Source of Sources)

```
Subject: [Your role] at [Company] for "[their request title]"

Hi [name],
[One sentence restating their question.]
[Direct answer in 1 to 2 sentences.]
[Selection criteria or the reason, 2 to 3 sentences, with one specific number or example.]
[Specific picks or steps if asked, each with a reason.]

[Name], [role], [company], [site]. Happy to answer follow-ups by phone: [number].
```
Answer within the hour, stay inside word limits, give 2 to 3 quotable passages (r/juststart, 94).

## 10. Expert quote request (before publishing)

```
Subject: Quick quote for a piece on [topic]?

Hi [name], I'm writing [title] for [site], publishing [date]. Your [post or talk] on [specific point] is the best take I've seen.
Would you answer one question in 2 to 3 sentences: [question]?
We'll credit you with a link to [their site or LinkedIn]. No worries if timing does not work.
```

## 11. Prompts

**Internal links (r/SEO, 736 upvotes, adapted):**
"Here is my site [URL] and a target page [URL] about [topic]. Find at least 20 places in the body text of other pages on my site where a link to the target page would help a reader. Exclude navigation, footers, sidebars and pages that already link to it in the body. Return a table: source URL, natural anchor text, the sentence with the link inserted, and where in the page it goes."

**Fan-out sub-queries:**
"A buyer asks: '[full question with constraints]'. List the 15 to 30 searches you would run to answer it well, covering definitions, alternatives, comparisons, price, compatibility, setup, risks and evidence. Group them by the page that should answer each."

**Reader critique (r/blogging, 126, verbatim opening):**
"Imagine you've just landed on this blog post after typing [query] into Google. Please read through this post and share your thoughts and reactions..." Then ask: how long it took and where attention drifted, what stood out, whether you would share, buy or subscribe, what was missing, whether you would read another post.

**Research, not prose:**
"List every type of [concept] used in practice, with a one-line definition and a real example for each. Mark which ones the top Google results for '[query]' do not cover." (the taxonomy expansion that held #1 above Forbes, r/content_marketing, 26)

## 12. AI prompt panel log (monthly)

| Date | Engine | Prompt | Named? (Y/N, position) | Cited our URL? | Rivals named | Cited domains | Wrong facts about us |
|---|---|---|---|---|---|---|---|

Per engine: mention rate = answers naming you / answers collected; citation rate = answers linking you / answers collected; share of voice = your mentions / all brand mentions. Same prompts, same engines, each run 3 times; failed runs are missing data.
