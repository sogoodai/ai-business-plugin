# Quality check: with and without the plugin

Run 24 November 2026. Small test: 3 prompts, so read it as a direction, not a measurement.

## Setup

- Model: Claude Opus 5.5 in Claude Code, print mode, fresh empty folder.
- Clean session: no user settings, no memory, no MCP servers, no web search or fetch, no file writes. The only difference between arms is `--plugin-dir` (this plugin) on or off.
- Prompts: [prompts/](prompts). A house cleaning business, a first template business, an Etsy candle seller.
- Judges: blind and pairwise, order randomized. Claude Opus 5.5 twice per prompt and Codex (gpt-6.1-sol, high effort) once. Each scored specificity, numbers, fit to the founder and insight from 1 to 10, then picked a winner.

## Result

| Prompt | Skill the agent loaded | Verdicts (plugin / without) |
|---|---|---|
| House cleaning, 10 recurring clients, under $1,000 | `home-services` | 3 / 0 |
| Side business selling templates | `digital-products` | 3 / 0 |
| Candles on Etsy: Meta ads or Shopify | `ecommerce-brand` | 2 / 1 |
| **Total** | | **8 / 1** |

Mean scores (1 to 10):

| | Specificity | Numbers | Fit | Insight |
|---|---|---|---|---|
| With plugin | 8.3 | 6.9 | 8.3 | 8.7 |
| Without | 8.3 | 6.4 | 7.3 | 6.9 |

The agent picked the right playbook on its own in all 3 runs.

## What changed in the answers

- **Same level of detail, better judgment.** Both arms wrote concrete week-by-week plans. Specificity scored the same.
- **More risks caught.** With the plugin, answers flagged things the plain model missed: Google's rule against asking only happy clients for reviews, the insurance requirement for Local Services Ads, Etsy's mandatory 12% Offsite Ads above $10,000 a year, fees charged on shipping too, Etsy's rules on promoting your own site in packages, and checking tax formulas before selling a tax template.
- **Numbers with a source.** Every figure the plugin arm cited traced back to a dated source in the skills (for example cleaning Local Services leads at $33.21 in 2026, Meta ecommerce median cost per purchase $38.99, home goods store conversion 1.29%). It also labelled its own guesses as guesses. The plain model gave plausible ranges with no source (for example "$25 to $50 per lead in Austin").
- **The loss.** On the candle prompt, Codex preferred the plain answer: shorter, more proportionate, and it judged that broad benchmarks were applied too precisely to a tiny shop. Both Claude judges went the other way.

## Limits

3 prompts and model judges, no real founders and no business outcomes. An earlier, larger test of short playbooks inside SoGood's own planner (600 plans, 10 November 2026) found a 62% win rate overall, with ecommerce losing. These skills are much longer and loaded by the agent on demand, so the two tests are not comparable, but together they say: useful, not magic.

Full answers: [answers/](answers). Raw verdicts: [verdicts.json](verdicts.json).
