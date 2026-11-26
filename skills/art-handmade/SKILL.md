---
name: art-handmade
description: "Grow an artist or maker business: painters and illustrators selling originals, prints and commissions, candle and soap makers, potters, woodworkers, crochet and fiber artists. Use for pricing from materials, labor and wholesale multipliers, commission terms, craft fair and art festival booths, wholesale, consignment, galleries and licensing, collector lists, limited editions, process videos, and candle, cosmetic and CPSIA labeling."
---

# Art and handmade: price the hours, sell where buyers already spend, own the list

Built from 166 practitioner tactics extracted from 210 threads (r/ArtBusiness, r/candlemaking, r/Etsy, r/woodworking, r/soapmaking, r/crochet), a keyword scan of 2,575 raw threads (r/Pottery, r/handmade, r/crafts, r/crochet, r/soapmaking), 109 handmade tactics from the ecommerce set and 65 from the jewelry set, a November 2026 deep-research report (Crafts Council, Artsy, Art Basel/UBS, Canopy Season, VendorsMap, Art Fair SourceBook, Etsy, Faire, Klaviyo, Littledata, Meta, TikTok, Patreon, AOI, DACS, CPSC, FDA, EU) and targeted checks of Faire terms, CPSC small-batch rules, MoCRA, FDA ceramicware marking and the California print law. "Operators report" marks a Reddit anecdote; everything else carries its source and year. Sources: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

Etsy search, ads and fee mechanics live in `ecommerce-brand`. Jewelry pricing and jewelry consignment live in `jewelry-accessories`. This skill keeps what is different about art and handmade goods.

## How art and maker businesses actually grow

- **Most makers earn little, so channel choice is survival.** 49% of UK makers earn under £10,000 a year from craft, 70% under £20,000, 1.5% over £100,000; 95% employ nobody (Crafts Council Makers Survey 2025, fielded September 2024). Plan a portfolio of channels, not one marketplace.
- **The healthy mix is in person plus direct plus one repeat engine.** Majority sources of in-person sales: fairs and events 34.6%, direct commissions 30.9%, workshops 20.4%, exhibitions 19.2%, someone else's shop 13.5%, gallery representation 12.5% (Crafts Council 2025). One candle maker made 98% of $25,000 in five months at markets (operators report).
- **Labor is the hidden cost.** Underpricing handmade is the default failure: a cutting board at $45 was "far too low for the finishing time" and moved to $75+ (operators report). Time every product before pricing it.
- **Collectors buy from artists directly now.** Among high-net-worth collectors, 43% bought from studios, 37% commissioned work and 35% bought through Instagram links; direct-from-artist was 20% of spend (Art Basel/UBS 2025). 62% of Artsy collectors value private previews; 43% of online buyers were stopped by a hidden price (Artsy 2025).
- **Owned email beats posting.** Klaviyo flows convert at 2.11% placed-order rate versus 0.16% for campaigns (Klaviyo 2026, vendor cohort). A full-time artist at $3,000 to $5,000 a month sends at most two emails a month to her own list (operators report).
- **Process is the content that sells handmade.** 6 to 12 second process clips beat hours-long edits for one full-time artist (operators report); a candle behind-the-scenes video hit 400,000 views and 800 orders in 48 hours (operators report).
- **Repeatable SKUs earn wholesale; one-offs earn collectors.** Candles, soap, mugs, prints and small wood goods can be reordered by shops. Originals and big commissions grow through lists, previews, galleries and price steps.

## Route by sub-model first

| Sub-model | Main engine | First levers | Depth |
|---|---|---|---|
| Fine artist (originals) | Collector list, shows, studio sales, galleries | Visible prices, consistent price per size, private previews, open studio | [collectors-and-content.md](references/collectors-and-content.md), [wholesale-consignment-galleries.md](references/wholesale-consignment-galleries.md) |
| Illustrator, print and commission seller | Commissions, prints at markets and cons, licensing, Patreon | Commission terms, bundle pricing, usage-based quotes | [commissions-and-licensing.md](references/commissions-and-licensing.md) |
| Candle and soap maker | Markets, Etsy, wholesale reorders, refills | 10-SKU range, scent testing, labels that read, compliance | [compliance-and-labeling.md](references/compliance-and-labeling.md), [by-niche.md](references/by-niche.md) |
| Ceramics and woodwork | Markets and festivals, commissions, direct site | Tiered sizes, touch at the booth, shipping quotes, food-safe claims | [fairs-and-markets.md](references/fairs-and-markets.md), [by-niche.md](references/by-niche.md) |
| Fiber (crochet, knit, embroidery, quilting) | Patterns and kits, small finished pieces, commissions, Lives | Hours ceiling, patterns as product, CPSIA for kids items | [by-niche.md](references/by-niche.md), `digital-products` |

## First session: ask, then compute

Ask the owner:

1. What they make, price bands, and which sub-model above. Originals, multiples, or both?
2. For their top five products: materials per unit, hands-on minutes per unit (or agree to time a batch), packaging, and current price.
3. Channels and last 12 months of sales per channel: Etsy (Offsite Ads status), own site, markets and fairs (fee and sales per event), wholesale or consignment accounts and their terms, galleries, commissions, Patreon.
4. Target pay per hour and minimum profit per order. Hours per week available for making versus selling.
5. Email list size, where addresses came from, and consent wording.
6. Countries and states they ship to. Any kids items, cosmetics or food-contact claims.
7. Representation contracts (price parity, exclusivity, discount clauses). Offers they will and will not run.

Then compute ([references/pricing.md](references/pricing.md)):

```
unit cost        = materials + packaging + hands-on minutes / 60 x owner rate + overhead per unit
channel price    = (unit cost + fixed fees per order) / (1 - % fees - target margin)
wholesale        = unit cost / (1 - maker margin on wholesale)      MSRP = wholesale x 2 (keystone)
wholesale-ready  = market retail price >= MSRP the formula requires
event contribution = sales - COGS - booth and application fees - card fees - travel - helper pay
event multiple   = sales / booth fee         (3x to 5x is the floor, 10x is a strong show)
list value per event = consented signups x historic revenue per subscriber
effective hourly = (revenue - all costs except owner labor) / all owner hours incl. selling
```

Report the three biggest gaps in money: underpriced SKUs at today's cost, events below the 3x floor, and the share of buyers never captured to the list.

## Benchmarks to check first

| Metric | Typical | Strong | Source, year |
|---|---|---|---|
| US craft fair booth fee | $75 median (VendorsMap); $165 (Canopy Season) | Top 10% of events start at $475 | VendorsMap Nov 2026; Canopy Season Sep 2026 |
| Sales per booth fee | 3x to 5x | 10x | Fair guides and forums, anecdotal (same rule as `jewelry-accessories`) |
| Elite juried art fair, sales per artist | $14,379 average gross (Saint Louis) | $16,475 average net (Park City Kimball) | Saint Louis Art Fair 2025; Art Fair SourceBook 2025 |
| Open studio trail | 124 visits and about £2,190 sales per reporting studio | n/a | Artmap Argyll 2025 |
| Shopify conversion, home and decor | 1.1% median | 1.8% top 20% | Littledata Nov 2026 |
| Shopify conversion, beauty (soap proxy) | 2.8% median | 3.9% top 20% | Littledata Nov 2026 |
| Email flows, placed-order rate | 2.11% | 4.3% top 10% | Klaviyo 2026 |
| Representing gallery commission | 50% | 25% to 50% range | CAA (pre-2024); BKF Denmark |
| Retail consignment split (maker/shop) | 60/40 | 70/30 | Practitioner norm, see `jewelry-accessories` |

Full table with fees and operator numbers: [references/benchmarks.md](references/benchmarks.md). No robust benchmark exists for craft-fair conversion, commission close rate, wholesale reply rate or art licensing advances. Say so instead of inventing one.

## Decision rules, in order

1. **Price before promotion.** If a SKU does not clear the owner's hourly rate and margin in the worst fee case (Etsy with Offsite Ads at 15%), fix price or cost before buying any traffic. Raise the price of the most labor-heavy bestseller first; Etsy sellers report sales holding or rising after big raises (operators report, uncontrolled).
2. **Test price in steps and record units.** One woodworker sold four boards in a row at $35, raised to $45 and sold none more that weekend; others moved to $75 with engraving. Change one price per event, log units per hour open, decide after two events.
3. **Pick events on contribution, not footfall.** Apply only where conservative sales reach 3x to 5x the fee after travel. A $75 cafe market produced $40 in sales (operators report). Bring a list signup sheet to every event: buyers who meet you buy online later.
4. **Capture every buyer.** Card payments, a QR or sheet for "first look at new work", custom-order notes with contact details. Email at most twice a month for originals; flows for repeatable goods.
5. **Commissions need written terms first:** price by size and complexity, deposit, revisions, timeline at 2x your estimate, shipping quoted before acceptance, rights stated. Use [scripts.md](references/scripts.md).
6. **Wholesale only SKUs built for it.** A SKU is wholesale-ready when keystone pricing still pays labor. Prepay first orders from new accounts. Send self-sourced shops your own Faire link (0% commission) rather than letting the marketplace claim them (15% plus $10 on opening orders, Faire 2026).
7. **Consignment is an entry ticket, not a channel.** Written agreement, 60/40 floor for shops, inventory photos, check the work is actually displayed. Fine-art galleries at 50% are different: they must sell, promote and hold price parity.
8. **Content shows hands and process.** Short process clips, finished piece in hand, maker in frame. Boost only posts that already outperform organically (Donovan Pottery, TikTok case study 2026: over 5x ROAS after boosting proven organic posts; vendor-selected).
9. **Compliance is listing copy.** Candle warnings, soap claims, CPSIA tracking labels and EU GPSR data belong on the product page. Wrong claims change the legal category of a product ([compliance-and-labeling.md](references/compliance-and-labeling.md)).
10. **Ads last.** Paid ads to Redbubble prints ran at a net loss for one artist; $121 of Etsy Ads gave 276 clicks and zero sales for another (operators report). Ads go only to proven listings with margin for a 12% to 15% fee stack.

## First 30 days for a new or restarting maker

1. **Time and price five products.** Launch with 5 to 6 variants, not 20 (a candle maker's first-year advice; perfumer advice caps the whole range at 10 SKUs).
2. **Book three different local events in six weeks:** a flea market that welcomes artists, a studio or atelier market, a holiday market. Log sales per hour open and signups.
3. **Etsy with proof of hands:** real photos with shadows, item in hand at position 1 or 2, a 10-second making clip, a filled About section. Etsy mechanics: `ecommerce-brand`.
4. **Start the list at the first event** with consent wording, and tag every address with its source.
5. **Post finished work where buyers already gather:** a niche or local subreddit, a fandom, a state fair competition. Announce open commission slots occasionally; one artist with 50 followers got a commission from almost every opening post (operators report).
6. **One local partner:** a bakery, honey or produce vendor, cafe or bar where the work can be seen or bundled.
7. **Keep the day job until slow months are covered.** A festival seller reinvested 100% for two years before going full time; another went full time on a $5,000 month and is still paying off debt after a slow summer (operators report).

An existing or stalled business follows [references/plan-90-days.md](references/plan-90-days.md).

## Pricing in one screen

- **Formula, not feeling.** Materials + labor at a stated hourly rate + overhead, then divide by (1 - fees - margin). Convention check: (materials + labor + overhead) x 2 = wholesale, x 2 = retail (handmade pricing convention, Dummies; Etsy handbook cited by Craftybase). If the market will not pay the retail number, the SKU is DTC-only or needs a cheaper construction.
- **Originals:** consistent price per size within a series, raised only after sales. Studio price equals gallery price, always. Common floors from one painter: $150 for an 8x10 watercolor, $200 for an 8x10 oil, 10% off at most (operators report).
- **Prints and small goods:** quantity ladders lift basket size. One artist's second market: 8x10 prints 1 for $20, 2 for $35, 3 for $50; cards 1 for $5, 4 for $15; 562 sales, $6,500 revenue, $5,000 profit over six days (operators report).
- **Premium layers on reproductions:** a 16x20 canvas print hand-embellished with gel medium in 10 minutes sold at $350 against about $50 in materials and shipping (operators report).
- **Size up, not discount down.** Large coin racks sold out at full price while discounted small ones did not (operators report). Show the top size first.
- **Refills and samples lower the barrier** without cutting the hero price: $10 candle refills for a $38 vessel, sample tins as a discovery kit (operators report, planned).

Worked examples for a candle, a mug, a cutting board, an original painting, prints and a crochet piece: [references/pricing.md](references/pricing.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data or platform says | Rule |
|---|---|---|---|
| Price raises | "Double it, sales went up" | Uncontrolled; one board stopped selling after +$10 | Raise in steps, log units per event, keep if contribution per hour rises |
| Etsy renewals | Renew daily for rank | Etsy: small temporary boost only (Oct 2025 disclosure) | Spend effort on first photo and price |
| Reels vs photos | Video always wins | One artist: photos 3,000 to 13,000 likes, Reels 400 to 700 at 10x effort | Test both for a month; keep what sells, not what is liked |
| Consignment | Take any shop that will hang it | 50/50 is wholesale money with consignment risk | 60/40 floor or ask them to buy |
| Galleries | Prestige gallery first | One artist went into debt on commission plus show travel; local low-fee galleries paid better | Model net per piece including travel |
| Faire first-order fee | 25% (older sibling notes and blogs) | 15% plus $10 new-customer fee in North America (Faire pricing update, 2026) | Use the current Faire page at quote time |
| Bigger audience | Followers will buy | Random online followers almost never ordered; con and stream contacts did | Measure buyers from each source |

## Never

- Never price from materials alone, or quote a custom piece before the packed shipping cost is known.
- Never start a commission without a deposit and written terms, or hand over commercial rights at a personal-commission price.
- Never sell the same work cheaper in your studio than through a representing gallery.
- Never call a print "limited" if more can be made; never exceed a stated edition size.
- Never claim soap "treats", "heals" or is "antibacterial", call a candle "non-toxic", or call a glaze "food safe" without testing.
- Never sell children's items without the CPSIA certificate and tracking label; handmade is not exempt.
- Never put another artist's name in titles or tags, including Etsy's AI suggestions (a "Basquiat-style" title cost one seller every listing).
- Never pay an agency for "art fair representation" before checking the fairs' official exhibitor lists.
- Never invent a benchmark, an offer the owner has not approved, or a customer quote.

## Before you write any message

Use [references/scripts.md](references/scripts.md): commission intake and quote, deposit and revision terms, gallery pitch, shop wholesale pitch and follow-up, consignment terms, licensing inquiry reply, collector preview, release and clicker emails, market signup line, booth lines for lurkers and chatters, secrets requests, negative review replies.

## References

- [benchmarks.md](references/benchmarks.md): metric, typical, top quartile, source, year; fees; incomes; operator numbers; what has no benchmark.
- [pricing.md](references/pricing.md): formulas and worked examples by product, channel contribution, wholesale eligibility, price testing, bundles.
- [commissions-and-licensing.md](references/commissions-and-licensing.md): commission pricing, terms, intake, finding commission buyers, licensing, stock, royalties.
- [fairs-and-markets.md](references/fairs-and-markets.md): event selection and scoring, booth economics, display, checkout, booth conversation, unusual venues.
- [wholesale-consignment-galleries.md](references/wholesale-consignment-galleries.md): wholesale terms and Faire math, line sheets, consignment, galleries, open studios, agency scams.
- [collectors-and-content.md](references/collectors-and-content.md): collector list building, releases, limited editions, online channels, process content formats and hooks.
- [compliance-and-labeling.md](references/compliance-and-labeling.md): candles, soap and cosmetics, CPSIA, ceramics, EU GPSR, print disclosure law, Etsy policy traps.
- [scripts.md](references/scripts.md): exact wording.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [by-niche.md](references/by-niche.md): fine art, illustration and prints, candles, soap, ceramics, woodwork, fiber.
- [plan-90-days.md](references/plan-90-days.md): phased plan by sub-model with exit checks and owner questions.
- Sibling skills: `ecommerce-brand` (Etsy search, ads and fees, TikTok Shop, Shopify, wholesale reorder engine), `jewelry-accessories` (jewelry pricing, consignment agreement template), `digital-products` (patterns, printables, tutorials), `local-retail` (a studio shop or gallery storefront), `organic-social` (content systems), `offers-pricing` (pricing psychology, increase notices), `email-sms-loyalty` (flows and consent), `paid-ads` (account setup).
