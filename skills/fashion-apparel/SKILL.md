---
name: fashion-apparel
description: "Grow a clothing brand: streetwear labels, independent apparel, print-on-demand and screen-printed tee brands, boutiques selling online. Use for drops, restocks, preorders and waitlists, first 100 customers, creator seeding and try-on content, TikTok Shop for apparel, Meta ads for clothes, size guides and returns, landed cost and margins, MOQs, factories and print shops, wholesale to boutiques, markdowns, Depop or Faire, and green claims."
---

# Fashion and apparel: sell the fit, stock the sizes, drop on purpose

Built from 645 apparel practitioner threads (418 extracted tactics from r/streetwearstartup, r/ClothingStartups, r/printondemand, r/shopify, r/ecommerce, r/Entrepreneur, r/SCREENPRINTING), a manual read of 200 more streetwear, clothing-startup and screen-printing threads, apparel threads from the ecommerce set, 2025 to 2026 research (Loop, Kyra, MHI, Triple Whale, Shogun, Adtribute, McKinsey, Faire, platform fee pages, EU and UK green-claims rules) and the public skills harvest. "Operators report" marks a Reddit anecdote; everything else carries its source and year. Sources: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

General ecommerce (Etsy, Amazon, TikTok Shop mechanics, Shopify conversion, POD math) lives in the `ecommerce-brand` skill. This skill keeps what is different about clothing.

## How small apparel brands actually grow

- **Returns are the hidden tax.** 56% of apparel and footwear brands report 30%+ return rates (Radial 2025) and 56% of apparel returns are fit or size (Loop 2026). Fit work raises conversion and cuts returns at once; ads to a page without fit information pay twice.
- **Margin decides whether paid traffic can ever work.** DTC apparel targets 55% to 65% gross margin (Shopify 2026). The fashion Meta median is a $63.11 purchase CPA at 2.17x first-purchase ROAS (MHI 2026). In the worked example, a $60 tee with free shipping and 20% returns needs about 2.9x to break even.
- **Repeat is modest.** Clothing 365-day repeat is 19.1% (By the Numbers 2025 to 2026); fashion 90-day repeat is 10.91% (Adtribute 2026). Never fund a first-order loss with hoped-for repeat.
- **Distribution is creators plus original content.** 75% of US Instagram recommendations come from original posts (Meta, Jan 2026). Try-ons get about twice the views of other posts for micro creators despite lower engagement (Kyra 2026). 81% of fashion collaborations are repeat partnerships (Flowbox 2025).
- **Drops concentrate attention; stockouts leak buyers.** Only 20% of shoppers wait for a restock and 26% buy a competitor (Podean 2025). Instant sellouts lower repurchase intention (Journal of Retailing 2025). Limited pieces stay limited; the core is replenished.
- **Production is a marketing constraint.** Average production takes 17 to 18 weeks (McKinsey 2026). Drop dates, restocks, preorder promises and ad scaling all wait on it.
- **The cheap winners are owned demand.** Waitlist, size-specific back-in-stock, community, friends' Stories, pop-ups and creators come before cold paid traffic. Operators report a 500+ list producing about 70 launch-day orders and $10.1k at 60% gross margin (r/shopify).

## First session: ask, then compute

Ask the owner:

1. What they sell and how it is made: cut and sew, blanks plus screen print or DTF, POD, upcycled, or a multi-brand boutique. Price range, countries.
2. Landed cost per style and the supplier for each; reorder lead time.
3. Last 12 months: orders by SKU, size, channel and month; refunds and exchanges with reasons; aged stock by size.
4. Drop or always-on; how the last drop sold through by size; list sizes (email, SMS) and consent source.
5. Paid spend by platform and how results are measured; creator deals and usage rights held.
6. Wholesale accounts or plans and their terms; marketplaces in use.
7. Offers they will and will not run; claims in use (sustainable, handmade, made in) and the evidence; who approves prices and messages.

Then compute ([references/economics.md](references/economics.md)):

```
landed COGS            = garment + decoration + labels/packaging + freight + duty + handling + QC loss
contribution / order   = net x (1 - refund rate) - COGS x (1 - f + (f + e) x u) - pick/pack - fees
                         - shipping subsidy - return labels and handling - commission   (returns in, always)
break-even ROAS        = platform-reported order value / contribution before ads
allowable CAC          = first-order contribution + measured 90-day repeat x repeat contribution
wholesale check        = landed <= MSRP / 4   (retailer ~50%, brand ~50%)
discount unit lift     = gross margin / (gross margin - discount) - 1
days of cover (size)   = units on hand in size / 28-day daily sales of that size
return rate grain      = SKU x size x reason x production batch
```

Report the three biggest gaps in money against [references/benchmarks.md](references/benchmarks.md).

## Route by model

| Model | First channel | Lever that matters most | Depth |
|---|---|---|---|
| Streetwear drop label | Community, friends' Stories, pop-ups, creators | Waitlist and drop calendar; graphics before logo pieces | [drops-and-launches.md](references/drops-and-launches.md), [by-niche.md](references/by-niche.md) |
| Screen-printed tee brand | Local markets, events, Instagram, causes | Designs a place or group adopts; setup vs run economics | [production-and-sourcing.md](references/production-and-sourcing.md) |
| POD tee brand | Etsy, then own store | $8+ profit per sale, wash-tested quality, move winners to bulk | `ecommerce-brand` pod-handmade.md, [by-niche.md](references/by-niche.md) |
| Independent label, cut and sew | DTC with creators, boutiques once sell-through is proven | Fit and size curve; landed cost that allows wholesale | [fit-returns-pdp.md](references/fit-returns-pdp.md), [pricing-and-channels.md](references/pricing-and-channels.md) |
| Boutique selling online | Existing customers, Instagram, local search | Fit information, new-arrival drops, leftover-size events | [by-niche.md](references/by-niche.md), `local-seo` |

## Benchmarks to check first

| Metric | Typical | Better quartile | Source, year |
|---|---|---|---|
| Apparel store conversion | 1.76% median (803 Shopify stores); 2.77% broader average | not published | Shogun 2026; Shopify 2026 |
| Meta purchase CPA, fashion | $63.11 | $52.62 or lower | MHI, 14 brands, 2026 |
| Meta first-purchase ROAS, fashion | 2.17x (apparel 2.24x, Triple Whale) | 2.51x or higher | MHI 2026 |
| Meta CPM / CTR, fashion | $21.37 / 1.67% | $13.68 / 1.88% | MHI 2026 |
| Blended CAC, fashion | €41.96 | not published | Adtribute 2026 |
| Repeat: 90-day fashion / 365-day clothing | 10.91% / 19.1% | not published | Adtribute 2026; By the Numbers 2025 to 2026 |
| Fit or size share of apparel returns | 56% | n/a | Loop 2026 |
| Merchants with exchanges / with return fees | 73.6% / 65.2% (average fee $9.04) | n/a | Loop 2026 |
| TikTok fashion creator engagement by views | 9.3% (IG 2.8% by plays) | n/a | Kyra Q3 2026 |
| Clothing email order rate, campaign / flow | 0.97% / 1.62% | not published | Klaviyo 2026 |

No robust public benchmark exists for sell-through targets, size-curve splits, waitlist conversion, minimum ad budgets, boutique reply rates or screen-print prices. Say so; use the brand's own drops.

## Decision rules, in order

1. **Contribution after returns below the owner's floor** (operators use 40% to 50% after ads): fix price, landed cost, AOV or returns before any traffic.
2. **Return rate high or rising:** fix fit information on the top return SKUs, check grading by batch, switch to free exchanges with a fee only on refunds. Measure page tests on net revenue after returns.
3. **No proven product yet:** validate the sample on TikTok and Reels, with 20 community DMs and a waitlist that asks for size. Run 25 to 100 units per style or preorders, never bulk.
4. **Stock cover on the top two sizes shorter than lead time:** no ad scaling and no creator push on that SKU; open size-specific back-in-stock or preorders.
5. **Conversion under about 1.5% with decent traffic:** product page first (measurements, model stats, fit note, video near the buy box, back view).
6. **Flows missing:** welcome, cart, back-in-stock by size, post-purchase care and fit, drop alerts. Depth: `email-sms-loyalty`.
7. **Drops:** true limits only on limited pieces; replenish the core; exact time and timezone; early access to the list; sold-out sizes to a restock list; leftovers to a recurring bundle event.
8. **Creators before cold ads:** seed 20 to 50 matched nano and micro creators with no posting obligation, ask size first, buy paid usage separately, rebook the ones who sold.
9. **Paid ads** only when the gate in [paid-ads.md](references/paid-ads.md) passes. Diagnose by CPM, CTR and conversion before killing; never scale on ROAS alone.
10. **Discounts:** depth at events and on aged sizes only; never on the hero. A 40% discount at 60% margin needs 3x the units.
11. **Wholesale** only for SKUs that pass the 4x check, prepaid first orders, brand-sourced retailers on Faire to avoid the first-order fee (25% outside North America, 15% plus $10 in North America).
12. **Claims:** no "eco", "sustainable", "carbon neutral" or "good for the planet" without a specific certified attribute; EU rules apply since 27 September 2026.

## Drops in one screen

- Hybrid wins: always-stocked core plus "3-4 shirts every couple months" (operators report) or weekly limited drops with a monthly clear-out.
- Sequence: build in public, waitlist with size question, exact time and timezone, early access, public, sold-out to restock list or preorder, post-drop "missed it" flow, leftovers to a bundle event. An agency case reports 18% to 24% extra revenue from post-drop flows (vendor, ceiling).
- Preorders fund production ($39.99 preorder, $50 at stock, operators report) and destroy trust when late. Proactive delay emails with a refund option.
- Load-test checkout before a hyped drop. Close outerwear preorders early enough for the season.

Depth: [references/drops-and-launches.md](references/drops-and-launches.md).

## Fit, returns and the product page in one screen

- Garment measurements (flat, pit to pit), model height and size worn, intended silhouette, between-sizes advice, inches and cm. Wording in [scripts.md](references/scripts.md).
- Keep clean on-model and back views; video near the buy box (Foot Locker blueprint: sizing, materials, history, styling, rotate the product; +6% conversion, vendor case). Lifestyle shots replacing model shots cost 7.2% conversion in one test (not significant).
- Fit tools only behind a randomized test: +29.9% conversion in one vendor case, +0.65% returns among size-finder users in a peer-reviewed study.
- Ask every reviewer usual size, size bought and fit; show the distribution.

Depth: [references/fit-returns-pdp.md](references/fit-returns-pdp.md).

## Content and creators in one screen

- Judge content on views, add to cart and contribution, not engagement rate: try-ons and ad-labelled posts look weak on engagement and still sell.
- Original footage only; Instagram Trial Reels as the hook lab; promote proven hooks into ads.
- TikTok Shop mass apparel winners sat at $25 to $36 in one operator's tracking of 1.2M listings; TikTok's own checklist wants 500+ units and 100+ samples a month for a hero SKU, so check stock per size before joining that race.

Depth: [references/creators-and-content.md](references/creators-and-content.md), [references/paid-ads.md](references/paid-ads.md).

## Production and channels in one screen

- Ask factories the eight questions and sign tolerances (plus or minus 1.5 cm) before the deposit; samples should cost $30 to $40 for basics (operators report).
- Brief print shops with exact sizes, placements, colors and date; "bulk order, it's gonna blow up" gets ignored.
- Wash-test POD and DTF before premium pricing; sample every color.
- Fees to load per SKU: Etsy 6.5% plus Offsite Ads, Amazon apparel 17% above $20, Depop processing plus 12% on boosts, Faire 25% first order outside North America (15% plus $10 in North America).

Depth: [references/production-and-sourcing.md](references/production-and-sourcing.md), [references/pricing-and-channels.md](references/pricing-and-channels.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| Scarcity | "Never coming back" sells out | Instant sellouts cut repurchase; 20% wait for restock | Limited means limited; core sizes restocked; restock lists by size |
| Ads vs community first | "Most orders should come from ads" vs "skip ads, do meetups" | Apparel Meta medians sit near break-even for low AOV | Community and creators until creative and contribution prove out, then ads |
| ROAS target | "3x or kill it" | Apparel medians 2.17x to 2.24x | Compute break-even ROAS with returns; kill on that |
| Photos | "Don't blow the budget on shoots" vs "photos make or break conversion" | Lifestyle replacing model shots -7.2%; video +4% to +6% in A/Bs | Clean on-model and video first, editorial last |
| Free returns | Free returns sell | 82% of shoppers care; 65.2% of merchants charge some fee | Free exchanges and credit; fee on refunds where law allows |
| Size tools | Fit quizzes fix returns | +29.9% conversion in one case; +0.65% returns in another study | Randomized test on net revenue after returns |
| Back vs front print | Back prints sell better | No test; back art hides under jackets | Small front plus big back; test placement; shoot both sides |
| Tech packs | "Factories walk you through" vs "never cut corners" | No data | Full tech pack for cut and sew; print spec for blanks |

## Never

- Never scale ads or creators on a SKU without return-adjusted contribution and size-level stock cover.
- Never fake scarcity, quantities, countdowns, reviews, sell-through numbers or customer photos.
- Never write green, ethical, handmade or origin claims the owner cannot prove, and never generic "eco" or "sustainable" copy in the EU or UK.
- Never put brand names, characters or artist names in designs, titles or tags without the owner's informed decision on the IP risk.
- Never pay or discount for positive reviews, or present paid creators as unpaid customers.
- Never send marketing email or SMS without recorded consent, or copy US return-fee language into EU or UK policies without checking local law.
- Never invent a benchmark, an offer the owner has not approved, or a quote attributed to a real customer.

## Before you write any message

Use [references/scripts.md](references/scripts.md): creator gift DMs, size questions, usage-rights asks, try-on brief, drop teasers, waitlist email, drop SMS, sold-out and preorder copy, delay emails, boutique pitch and follow-up, opening terms, factory inquiry, sample questions, tolerance confirmation, print-shop quote request, defect claim, fit note, return policy, fit review request, care card, founder notes, ad hooks.

## References

- [benchmarks.md](references/benchmarks.md): metric, typical, top quartile, source, year; returns, tests, creators, TikTok Shop, fees, production; operator numbers; what has no benchmark.
- [economics.md](references/economics.md): landed cost, return-adjusted contribution, CAC, discount lift, 4x wholesale check, decoration breakpoint, MOQ risk, size cover, drop sizing, markdowns, creator cost.
- [drops-and-launches.md](references/drops-and-launches.md): drop vs always-on, the drop sequence, preorders, first 100 customers, stunts with results, collabs.
- [creators-and-content.md](references/creators-and-content.md): content matrix, Instagram 2026 mechanics, seeding rules, TikTok and TikTok Shop for apparel, UGC and fit reviews.
- [paid-ads.md](references/paid-ads.md): the gate, apparel Meta numbers, diagnosis and kill rules, creative angles, feeds, money lost.
- [fit-returns-pdp.md](references/fit-returns-pdp.md): size guide spec, fit tools, photos and video, copy, returns policy, tracking returns.
- [production-and-sourcing.md](references/production-and-sourcing.md): lead time, MOQs, vetting factories, tolerances, decoration methods and blanks, print-shop briefs, POD quality, in-house printing, green claims, IP.
- [pricing-and-channels.md](references/pricing-and-channels.md): setting prices, discount cadence, markdowns, wholesale to boutiques, marketplaces.
- [scripts.md](references/scripts.md): exact wording for creators, drops, wholesale, manufacturers and customers.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [by-niche.md](references/by-niche.md): streetwear, screen-printed tees, POD, cut and sew, boutiques, swim and activewear, one-of-ones, merch.
- [plan-90-days.md](references/plan-90-days.md): a new label from samples to the second drop, and a stalled label; owner questions.
- Sibling skills: `ecommerce-brand` (Etsy, Amazon, TikTok Shop, POD, wholesale reorders, creator rates), `paid-ads` (account structure, budgets, measurement), `email-sms-loyalty` (flows, consent, SMS), `offers-pricing` (pricing psychology, increases), `organic-social` (cadence and craft), `website-conversion` (pages), `local-seo` and `local-retail` (physical shops).
