<p align="center"><img src="assets/wordmark.svg" alt="SoGood AI" width="220"></p>

# SoGood AI plugin

Business playbooks for AI agents, plus the [SoGood AI](https://sogood.ai/?utm_source=github&utm_medium=readme&utm_campaign=ai-business-plugin) MCP server.

- **33 business playbooks**: 24 business types (ecommerce, local services, education, creators, B2B, simple "boring" online businesses and more) and 9 channels and jobs (ads, SEO, pricing, first customers...). Measured numbers cite their source; practitioner reports are labelled as such.
- **2 executable tools**: an offer profitability calculator and ledger reconciler, and a purchase or booking journey diagnosis, each with tests.
- **The SoGood MCP**: let your agent read and run your SoGood AI business (sales, products, site, ads, tasks). OAuth sign-in, no API key.

Works with Claude Code, Codex, Cursor, Gemini CLI, Claude Desktop and any MCP client. Skills follow the open [Agent Skills](https://agentskills.io) format.

## Install

**Claude Code**

```bash
claude plugin marketplace add sogoodai/ai-business-plugin
claude plugin install sogood@sogood
```

Then run `/mcp`, pick `plugin:sogood:sogood` and sign in (only needed for the SoGood tools; the playbooks work without it).

**Codex**

```bash
codex plugin marketplace add sogoodai/ai-business-plugin
codex plugin add sogood@sogood
```

**Cursor**: Settings, Plugins, add this repository. Or MCP only, in `~/.cursor/mcp.json`:

```json
{ "mcpServers": { "sogood": { "url": "https://mcp.sogood.ai/mcp" } } }
```

**Gemini CLI**

```bash
gemini extensions install https://github.com/sogoodai/ai-business-plugin
```

**Claude.ai and Claude Desktop**: Settings, Connectors, Add custom connector, `https://mcp.sogood.ai/mcp`.

**Any MCP client**: use [`mcp.json`](mcp.json), or add `https://mcp.sogood.ai/mcp` as a remote Streamable HTTP server. Stdio-only clients: `npx mcp-remote https://mcp.sogood.ai/mcp`.

**Skills only** (any agent that reads `SKILL.md`): copy the folders in [`skills/`](skills) into `~/.claude/skills/`, `~/.agents/skills/` or your agent's skills directory.

## What's inside

**Use SoGood**

| Skill | For |
|---|---|
| [`sogood`](skills/sogood/SKILL.md) | Connect the SoGood MCP, its 5 tools, approval rules, worked flows (start a business, check sales, draft an ad, business case, edit the site), what SoGood does and costs |

**Start with the job**

| Skill | For |
|---|---|
| [`offer-profitability`](skills/offer-profitability/SKILL.md) | Whether one price, discount or ad-funded offer makes money, or what recorded orders actually earned (calculator and CSV reconciler) |
| [`purchase-booking-diagnosis`](skills/purchase-booking-diagnosis/SKILL.md) | One broken or leaking checkout or booking journey (browser replay and funnel audit) |

**By business type**

| Skill | For |
|---|---|
| [`ecommerce-brand`](skills/ecommerce-brand/SKILL.md) | Etsy, Amazon, TikTok Shop, Shopify, print on demand, wholesale |
| [`consumer-products`](skills/consumer-products/SKILL.md) | Food, drinks, skincare, supplements, retail placement |
| [`fashion-apparel`](skills/fashion-apparel/SKILL.md) | Clothing brands, drops, POD tees, boutiques |
| [`jewelry-accessories`](skills/jewelry-accessories/SKILL.md) | Handmade and fine jewelry, accessories |
| [`art-handmade`](skills/art-handmade/SKILL.md) | Artists and makers, prints, commissions, craft fairs |
| [`digital-products`](skills/digital-products/SKILL.md) | Templates, printables, ebooks, presets, platforms and fees |
| [`boring-businesses`](skills/boring-businesses/SKILL.md) | 11 simple online business models: fees, sizing maths, launch checklists |
| [`home-services`](skills/home-services/SKILL.md) | Cleaning, lawn, trades, detailing, pest, junk removal |
| [`beauty-business`](skills/beauty-business/SKILL.md) | Salons, barbers, lashes, nails, med spas |
| [`restaurant`](skills/restaurant/SKILL.md) | Restaurants, cafes, bakeries, food trucks, catering |
| [`fitness`](skills/fitness/SKILL.md) | Trainers, studios, gyms, online coaching |
| [`health-practice`](skills/health-practice/SKILL.md) | Therapists, chiropractors, dentists, dietitians |
| [`events-weddings`](skills/events-weddings/SKILL.md) | Photographers, DJs, florists, planners, venues |
| [`hospitality-travel`](skills/hospitality-travel/SKILL.md) | Short-term rentals, B&Bs, tours, travel agents |
| [`local-retail`](skills/local-retail/SKILL.md) | Independent shops, florists, bookshops, vintage |
| [`real-estate`](skills/real-estate/SKILL.md) | Agents, property managers, loan officers |
| [`professional-services`](skills/professional-services/SKILL.md) | Accounting, law, insurance, financial advice |
| [`education-coaching`](skills/education-coaching/SKILL.md) | Tutoring, courses, cohorts, coaching, communities |
| [`creator`](skills/creator/SKILL.md) | Creators, newsletters, podcasts, sponsorships |
| [`agency-freelance`](skills/agency-freelance/SKILL.md) | Agencies, freelancers, consultants, studios |
| [`b2b-manufacturing`](skills/b2b-manufacturing/SKILL.md) | Manufacturers, suppliers, distributors |
| [`saas-apps`](skills/saas-apps/SKILL.md) | Micro-SaaS, apps, AI tools, extensions |
| [`indie-games`](skills/indie-games/SKILL.md) | Steam, mobile and itch.io games |
| [`nonprofit`](skills/nonprofit/SKILL.md) | Nonprofits, charities, churches |

**By channel or job**

| Skill | For |
|---|---|
| [`launch-first-customers`](skills/launch-first-customers/SKILL.md) | The first 10 to 100 customers |
| [`offers-pricing`](skills/offers-pricing/SKILL.md) | Prices, packages, discounts, price rises |
| [`paid-ads`](skills/paid-ads/SKILL.md) | Meta, Google, TikTok and other ads at $10 to $5,000 a day |
| [`organic-social`](skills/organic-social/SKILL.md) | Instagram, TikTok, YouTube, LinkedIn, Pinterest without ads |
| [`seo-content`](skills/seo-content/SKILL.md) | Organic search and AI answers |
| [`local-seo`](skills/local-seo/SKILL.md) | Google Maps, reviews, local pack |
| [`website-conversion`](skills/website-conversion/SKILL.md) | Turning visitors into leads, bookings and sales |
| [`email-sms-loyalty`](skills/email-sms-loyalty/SKILL.md) | Email, SMS, WhatsApp, loyalty, referrals |
| [`b2b-outbound`](skills/b2b-outbound/SKILL.md) | Cold email, LinkedIn, lists, deliverability |

Each playbook has a short `SKILL.md` (how the business grows, the first questions, the math) and `references/` with the detail (benchmarks, scripts, pricing, common mistakes, launch plans; contents vary by playbook) and its sources.

## How the playbooks were made

For each business type: hundreds of practitioner threads from the relevant subreddits (sorted by score, with the numbers people reported), deep research reports with dated sources (2025 to 2026 benchmarks, platform rules and fees), and the best public skills under MIT or Apache-2.0 (credited in each skill's `references/sources.md` and in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)). Practitioner reports are labelled as such. Measured data carries its source.

They are written as instructions for an agent: what to ask, what to compute, what to recommend, what never to do.

What we measured: in a small blind test (3 founder questions, 9 judge verdicts), answers with the plugin won 8 of 9, mainly by catching risks and citing sourced numbers; detail was the same. See [evals/README.md](evals/README.md). We do not claim the playbooks make a business succeed.

## Updating the playbooks

Issues and pull requests are welcome here. SoGood keeps the playbooks' master copy internally and syncs it into `skills/` with `scripts/sync-playbooks.sh` (maintainers only); [PLAYBOOKS_SOURCE](PLAYBOOKS_SOURCE) records the last sync.

## The SoGood MCP

`https://mcp.sogood.ai/mcp`. Five tools (`search_actions`, `describe_action`, `read_action`, `call_action`, `call_sensitive_action`) over SoGood's business API: products, orders, site, blog, ads, social, inbox, CRM, tasks. Sends, publishes, deletes and spend go through `call_sensitive_action` and need the founder's yes. Details: [skills/sogood](skills/sogood/SKILL.md).

[SoGood AI](https://sogood.ai/?utm_source=github&utm_medium=readme&utm_campaign=ai-business-plugin) is an AI cofounder: describe a business idea and a team of AI agents builds the brand, website, store and first customers, then keeps running it with you. [Privacy](https://sogood.ai/privacy) · [Terms](https://sogood.ai/terms)

## License

Code, scripts and configuration: [MIT](LICENSE). Text, including the skills and playbooks: [CC BY 4.0](LICENSE-CONTENT); reuse it freely, crediting SoGoodAI Inc with a link to [sogood.ai](https://sogood.ai/?utm_source=github&utm_medium=license&utm_campaign=ai-business-plugin). Adapted third-party material keeps its own license, see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
