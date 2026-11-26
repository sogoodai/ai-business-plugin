# Paid ads for apparel

Account structure, bidding, CAPI, learning budgets, Advantage+, Smart+ and GMV Max mechanics are in the `paid-ads` skill. This file is the apparel layer: when a clothing brand should pay for traffic, what the numbers look like, which creative angles work for clothes, and how stock and returns change the decisions.

## Gate: three checks before any spend

1. **Return-adjusted contribution covers a realistic CPA.** Fashion Meta purchase CPA median is $63.11 (MHI, 14 brands, Oct 2025 to Oct 2026) and all-channel apparel CPA $31.64 (Triple Whale 2025 to 2026). Compute break-even ROAS with returns ([economics.md](economics.md) section 3). A $60 one-tee order with free shipping and 20% returns needs about 2.9x; the apparel median is 2.24x.
2. **The product page answers fit.** 56% of apparel returns are fit or size (Loop 2026). Traffic to a page without garment measurements, model stats and a fit note pays twice: once for the click, once for the return.
3. **Stock cover on the two best sizes** lasts longer than the test plus the reorder lead time. An agency's apparel client ran out of stock four months into scaling and September ROAS fell to 2.6 (r/shopify, 96-pt thread).

If any check fails, fix it before buying traffic. "Refuse to scale spend from ROAS alone" (research report, 2026).

## What apparel Meta numbers look like

| Metric | Median | Better quartile | Source |
|---|---|---|---|
| Purchase CPA | $63.11 | $52.62 or lower | MHI 2026 |
| First-purchase ROAS | 2.17x | 2.51x or higher | MHI 2026 |
| Link CTR | 1.67% | 1.88% or higher | MHI 2026 |
| Link CPC | $1.29 | $0.94 or lower | MHI 2026 |
| CPM | $21.37 | $13.68 or lower | MHI 2026 |
| Link click to purchase | 2.51% | n/a | MHI 2026 |
| ROAS, apparel (Triple Whale cohort) | 2.24x | n/a | Triple Whale 2025 to 2026 |

The folklore "3x or kill it" sits above the median of real apparel accounts. Whether 2x is good depends on the brand's own break-even ROAS, not on a rule of thumb.

## Diagnose before killing

From the research report (2026):

| Symptom | Problem | Fix |
|---|---|---|
| CPM normal, CTR well below the account baseline | Creative | New hook, first frame, product shown sooner |
| CTR healthy, click-to-purchase weak | Product, offer, page or fit | PDP fit info, price display, shipping, size availability |
| CTR and conversion healthy, CPA too high | Economics: CPM or AOV | Raise AOV, bundle, threshold; do not touch creative |
| Meta ROAS poor, blended CAC and MER healthy | Attribution overlap | Do not cut Meta automatically; check new-customer share and blended numbers |

Kill and scale policy (research report, 2026):
- **Scale** when contribution after expected returns is positive, creative is at or above the account benchmark, the hero sizes have stock cover, and the 7 to 14 day trend is stable.
- **Fix PDP or offer** when CTR is healthy but purchase rate is weak.
- **Fix creative** when CPM is normal but CTR is weak.
- **Fix economics** when CTR and conversion are healthy but allowable CAC is below actual CAC.
- **Stop** when a SKU needs permanent discounting, generates abnormal fit returns, or cannot be replenished before stockout without destroying margin.

Do not judge an individual ad before it has spent about 2x AOV (operator rule, r/ecommerce, 146-pt thread). Judge the month on profit, not sales: one brand had €31,914 in sales and a €3,872 loss in a month of Google and Meta ads, then barely broke even for the year (r/ecommerce, 57-pt thread).

## Creative angles that work for clothing

Give the delivery system several genuinely different messages inside few ad sets instead of fragmenting audiences (research report, 2026):

1. Founder or problem story ("I couldn't find a heavyweight tee that didn't shrink").
2. Fit demonstration: the same piece on two bodies, model height and size on screen.
3. Three ways to wear.
4. Comparison with the obvious alternative (fabric weight, cut, price per wear).
5. Customer review read aloud or shown on screen.
6. Price and value: what goes into it, honestly.
7. Construction close-up: stitching, print, GSM, hardware.
8. Scarcity or restock with real numbers.
9. Creator proof: try-on or fit check from a creator with usage rights.
10. Catalog retargeting that names the product.

Copy rule: explain the design choice and the problem it solves. "Seamless hems for a smooth feeling" becomes "We decided to use seamless hems on our shorts to avoid chafing on your legs while running" (r/shopify, 170-pt thread). Cut unsupported superlatives ("best", "comfiest") and replace them with one construction fact (r/ecommerce, 79-pt thread).

Identity callouts in the first line work for niche apparel ("Yogis everywhere are raving about...", r/shopify, 136-pt thread) as long as they stay inside Meta's personal-attributes policy (`paid-ads`).

## Apparel-specific tactics with reported results

- **Thank-you ad to recent buyers.** A humorous thank-you creative shown only to purchasers from the last 14 days, on a very low budget, returned 3.25x for an apparel DTC client and made repeat purchases profitable (r/shopify, 71-pt thread; agency-reported, no incrementality test).
- **Agency apparel scale-up case:** a store at $20k to $25k a month, 2% conversion and $45 AOV went to $97k in month 3 and $190k in month 9 ($110k in Black Friday week) with purchase-optimized Meta at about $500 then $1k+ a day, about 70% prospecting and 30% remarketing, ROAS 3.40 in month 1 to 5.56 in month 3 (r/shopify, 96-pt thread; self-reported, holiday-inflated).
- **POD catalog test, then product ads.** A new POD store advertised its whole roughly 100-design catalog, then switched to single-product ads once purchases revealed demand: 1% to 2% of designs became winners and one ad drove about 99% of purchases. The month still lost money: €1,021 revenue, €714 goods, €367 ads (r/printondemand, 28-pt thread). A simple shirt on a high-contrast yellow background was the winning creative and fatigued after about three weeks.
- **$5 engagement screen before a POD design gets a sales budget:** see `ecommerce-brand` references/pod-handmade.md.
- **Gift buyers are a separate audience.** For niche shirts (aviation, engineering), the wearer rarely buys; commenters suggested Facebook ads to older relatives around Christmas and geotargeting towns with air bases or aviation employers (r/printondemand, 17-pt thread). Check purchases by age before trusting the assumed buyer: one store targeting 25 to 35 found 45 to 65+ converted far better and drove 42% of revenue (r/ecommerce, 61-pt thread).
- **Help-first retargeting copy:** "Hey, a quick reminder, if you have some questions or need help, let us know" as the first retargeting message instead of a discount (r/ecommerce, 173-pt thread; figures disputed by commenters).

## Catalog and Shopping feeds for apparel

- **Required apparel attributes:** color, size, gender and age group, plus `item_group_id` to group variants (Google Merchant Center; aaron-he-zhu harvest, Apache-2.0). Google requires these for apparel, so items missing them can be limited or disapproved.
- **Title formula:** Brand + product type + key attribute + color + material + size + gender ("Northside Heavyweight Tee Boxy Fit Washed Black 100% Cotton L Unisex"). One key attribute, not three (aaron-he-zhu harvest, Apache-2.0).
- **Feed only in-stock sizes** to prospecting catalog ads; a click on a sold-out size wastes the click and annoys the shopper.
- **Start Google with Shopping on niche-specific titles** rather than broad Search (r/shopify, 274-pt thread, comment).
- **Warm audiences:** catalog creative that names the product, with reviews (r/shopify, 136-pt thread). Several 2021 operators reported catalog sales beating standard conversion campaigns for viewers and carters (r/ecommerce, 59-pt thread; older, retest).

## Money lost, so the agent does not repeat it

| What happened | Cost | Source |
|---|---|---|
| Custom apparel ads chosen by engagement, then optimized for View Content and Add to Cart | About $3,000 spent, $200 in sales in month one | r/shopify, 82-pt thread |
| Kept advertising a $20 product that never sold | $3,000, zero units | r/shopify, 302-pt thread |
| Media buyer relaunched winners without their post IDs, mismatched copy and product pages | About $1,400 at 0.2 ROAS vs a normal 1.9+ | r/ecommerce, 93-pt thread |
| TikTok agency test with 20+ creatives and no testing plan | $2,000, zero sales | r/shopify, 67-pt thread |
| Influencer and ad spend scaled hard | Revenue +100% in a year, no profit | r/ecommerce, 101-pt thread |
| Ad created in the Meta mobile app with the wrong objective ("Message me") | About $100 before noticed | r/printondemand, 28-pt thread |
