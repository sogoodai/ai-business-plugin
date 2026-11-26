# Amazon FBA playbook

For private label and small brands selling through FBA, plus a short note on wholesale resellers. Amazon rewards legitimate review density, conversion and ad-fed rank, and punishes stockouts and policy mistakes harder than any other channel.

## Product selection gates

- **Beatable page one.** One seller entered a niche where the leader had 3,000+ reviews (about $300k a month) but other page-one listings had under 100 reviews and still did $8k to $12k a month; better listings took them to about $50k a month (r/FulfillmentByAmazon, 237-pt thread).
- **Margin gate:** `price x 0.85 - FBA fee - 2 months of storage - landed COGS` should leave comfortably above 45% (r/FulfillmentByAmazon, 124-pt thread, zero to mid-seven figures in 4 years). Room for coupons and rising CPCs is the point.
- **Price floor:** under about $10 historically triggered add-on status and thin profit per unit; a $15 to $90 buy-to-sell spread funds ads and discounts on slow colors (operators report). Wholesale resellers filter for items selling over $30.
- **Supply vs demand growth.** In Product Opportunity Explorer, compare growth in sellers with growth in search volume; walk away where sellers grow faster (operators report).
- **Cap each unproven product at $1,000** until you have your own sales data. One seller split a multipart product between two suppliers and assembled it, cutting test cash from $4,000 to $1,000 (r/FulfillmentByAmazon, 136-pt thread).
- **Variant-friendly niches:** pick products the same factories can vary, so new variants rank for adjacent keywords without another supplier search.
- **Benchmark against unknown brands, not leaders.** A seller projecting 1,000 units a month by month 3 from Jungle Scout got "a few sales per week" (r/ecommerce).
- **Realistic private-label launch budget: $30k+**, once samples, photo and video, packaging, compliance testing, freight, PPC, software and fees are counted (r/FulfillmentByAmazon, 28-pt thread).
- **Buy GS1 barcodes.** Bulk resold UPCs got a whole store removed after another seller proved GS1 ownership (r/Entrepreneur, 553 up).

## Launch

1. **Inventory live at least 3 weeks before launch** (Amazon's Vine guidance).
2. **Vine:** eligible FBA products with under 30 reviews; US cost $0 for up to 2 units, $75 for 3 to 10, $200 for 11 to 30 (Sell on Amazon, 2026). Amazon claims +30% sales for Vine products (its own data). One $33M seller's most successful launch was Vine reviews first with no PPC: 20 to 30 sales on launch day (r/FulfillmentByAmazon, 2026).
3. **Request a Review button** on every eligible order, plus the neutral insert in [scripts.md](scripts.md). Never incentivize, never ask only happy buyers, never ask anyone to change a review. One brand put $10 to $20 gift cards for 5 stars and $40 to remove negatives in its inserts; a buyer published the offer in a review (284-pt thread).
4. **Small first order, funded reorder.** A huge first run to cut COGS took over a year to sell and blocked the next launch. A bulky product needed the second order ($55k after a $30k first batch) within a month; underfunding forced the seller to throttle sales to avoid stocking out (r/FulfillmentByAmazon, 151-pt thread).
5. **Plan receiving at 3 to 30 days.** A 30-day receive caused a 2 to 4 week stockout that needed higher bids and price cuts to recover rank.
6. **Stockouts invite clones.** A differentiated product sold out for a month and came back to 5 exact copies on page one using its own images.
7. **Discount-driven rank is temporary.** 250+ units given away through deep-discount Facebook traffic reached the bottom of page one, then fell back to page three at the same sales rate (lost about $4,000). Ranking giveaways also carry policy risk.

## PPC structure for a small catalog

Amazon recommends checking a new Sponsored Products campaign at least twice a week in week one and driving decisions from search-term, targeting and placement reports.

```
Auto (discovery)            -> harvest converting search terms weekly
Broad / phrase (discovery)  -> same
Exact (proven terms)        -> single keyword or tight intent group per campaign
Product targeting           -> competitor ASINs where your price and rating win
Branded defense             -> separate, only if competitors bid on your brand
Store Spotlight             -> vague head terms (see below)
```

- **Single-keyword or tight-intent campaigns.** Placement multipliers apply to every target in a campaign, so mixing targets with different placement economics wastes money. In one account Sponsored Brands Top of Search converted at 10 to 11% vs 6 to 7% for Other: +40% bid is right for the average, but a keyword converting 2x at top deserves +100% (r/FulfillmentByAmazon, 209-pt thread). Separate branded from generic; never mix match types; put negatives per keyword group.
- **Turn off off-Amazon placements.** They are opted in by default. Pull the placement report, then set "Limit off-Amazon spend" in campaign settings or in bulk. The best off-Amazon ACoS one auditor saw across accounts was 70% (2026).
- **Store Spotlight for vague keywords.** Headline "What type of [keyword] do you need?", three tiles linking to Store category pages chosen from Amazon's grey refinement buttons, Other Placements at -99%. CTR went from about 0.6% to about 2% and two weak keywords produced $425k in 6 months (r/FulfillmentByAmazon, 125-pt thread).
- **Judge launches on TACoS and the organic-to-ad sales ratio**, not break-even ACoS. Keep a small high-ACoS budget for rank defense on "strike zone" keywords.
- **Seasonal front-loading:** bid high when nobody else is bidding, low when everyone piles in. One seller pushed Valentine's keywords from February 1 at 100%+ ACoS to build organic rank before the peak (157-pt thread; unverified).
- **Check search-term impression share before raising bids.** Above about 80% on the main term, more bid buys nothing; compare share before and after changes.
- **Measure total revenue lift, not attributed ad sales.** Spending more on terms you already own organically just moves sales from organic to ad. But cutting ads 40% in one account dropped organic sessions about 22% in 5 weeks and lost two page-one keywords (2026; authenticity questioned). Rule: cut cannibalizing terms, keep rank-defense spend.
- **Pool TACoS across products whose keywords overlap 80%+;** ads for A sold B up to 80% of the time in one agency's data, so judge on blended margin.
- **Kill ads on undeliverable offers:** inventory transfers pushing delivery a month out burned $300 in a day with zero sales.
- **Use Amazon's own peer benchmarks** (p25 and p75 by category for CTR, CPC, purchase rate, new-to-brand) before any internet ACoS target (Amazon Ads, May and Oct 2026). A 38% median ACoS (SellerPlex 2026) can be fine or fatal depending on margin.
- **Optimize CPA, not CPC.** Top-of-search CPCs ran 56% higher than product pages but CPAs 40% lower (Perpetua Q3 2026).
- **Audit any automation tool against your own baseline.** One trial raised spend from $10k to $15k a month and ACoS from 20 to 30% to 40 to 45%; back on manual: $8k at 20 to 25%.

## Listing conversion

- **Mine competitor reviews for copy.** Export reviews and ask an LLM: "Analyze the following list of product reviews. Create a list summarizing: Top 5 phrases people used to describe the product / Top 5 things people like about the product / Top 5 things people dislike about the product / Top 5 desired improvements / Add any other insights that may be valuable. Summarize the customer avatar." (r/FulfillmentByAmazon, 154-pt thread).
- **Title:** brand + primary keyword + 2 attributes + secondary keyword; bullets as a CAPS header plus one benefit sentence; situational language (when, where, why) and several use cases for Rufus-style ranking (nexscope harvest, MIT). Field limits drift; verify in Seller Central.
- **No "money back guarantee" text in images.** A competitor reported it and the top two products were removed for days.
- **Flat-dollar coupons with a minimum** "nearly doubled conversion" on struggling products and beat percentage coupons (operator, $6.5M wholesale seller).
- **Frame one bundle component as free** ("boat with a free trailer") rather than a bundle price.
- **Keep color variants together; give functionally different products separate pages.** One seller lost about 60% of sales when reviews split across near-identical variations.
- **Prime can carry a premium:** one seller won the Buy Box at 15% above the next free-shipping offer.

## Fees, inbound and cash

- **Quarterly all-in SKU audit** with referral, fulfillment, storage, surcharges, ads, inbound freight, returns and removals. Prices needed to rise 50 to 60% in one brand's audit; they cut 40% of SKUs (r/FulfillmentByAmazon, 136-pt thread).
- **Watch recorded dimensions.** Wrong dimensions cost one seller over $1,500 four times and another over $50k a year. Track and open a case immediately.
- **Reconcile inbound shipments weekly** (claims close after 9 months); claim unreimbursed adjustment-report entries. One seller recovered about $5k in a year.
- **Stranded stock check:** if ACoS spikes and Prime vanishes while you hold stock, see which fulfillment centers hold it. 2,000 of 3,000 units sat in a facility that does not ship orders.
- **AWD for multi-unit case packs** came out 30 to 40% cheaper than a 3PL plus placement fees for one brand; poor for heavy or single-unit packs.
- **Shrink size tiers** where packaging allows and ship pallets LTL.

## Account health and protection

- **Alerts on top listings** for "adult" flags (one seller lost 4 days and $30k+), inserted banned terms, and suppressed Buy Boxes.
- **Buy Box suppression for "competitive pricing":** audit your price per ounce and per pack on Walmart, Target, eBay, Costco, Shopify and Google Shopping. Use separate SKUs, packaging or GS1 barcodes per channel: one Target Labor Day discount removed the Amazon Buy Box and cost "six figures" in a weekend (r/ecommerce, 115-pt thread).
- **Screen wholesale accounts and enforce MAP.** About 10 rogue sellers dropped a $79.99 item to about $65 and Buy Box share tanked.
- **Keep some stock and fulfillment outside Amazon.** One suspension froze inventory that also fed eBay and Shopify through MCF.
- **Escalation ladder:** Seller Support case with order-level evidence, then a public Seller Central forum post with a dated timeline, then your account rep if you have one.

## Off-Amazon traffic and brand

- **Brand test:** does your brand name appear as a search term in Brand Analytics? A trademark is not a brand.
- **External traffic** (creators, PR, email) to Amazon lifts organic rank; one KDP seller saw ads raise organic sales 20 to 30% through rank.
- **Inserts that push buyers off Amazon** (website coupons, "join our list for 15% off") breach Amazon's communication rules. Operators do it and regret not building a list sooner, but it risks the account. Build the list from your own site, social and creators instead.
- **Moving from Amazon to DTC works with existing brand demand.** One brand spent $650k rebuilding its site plus $65k a month in ads before winding Amazon down: $18.3M at 17% net on its site vs 7.3% net on $43M on Amazon (306-pt thread). A new brand without demand reported about 1% site conversion and Google working only on branded terms.

## 90-day plan: Amazon

**Days 1 to 14: economics and listing.**
- All-in contribution per SKU, break-even ACoS, the 45% gate; GS1 barcodes; dimensions verified.
- Review-mined title, bullets and images; Vine enrolled if under 30 reviews; inventory live 3 weeks before push.

**Days 15 to 45: discovery.**
- Auto plus broad discovery campaigns; check twice a week in week one; harvest converting terms weekly into single-keyword exact campaigns; off-Amazon placements limited.
- Request a Review on every order; neutral insert.
- Reorder decision from 28-day velocity, not one good day.

**Days 46 to 75: control.**
- Placement multipliers set per keyword from the placement report; Store Spotlight for vague head terms; product targeting where you win on price and rating.
- Compare CTR, CPC and purchase rate with Amazon's p25/p75 peer report; fix the weakest one.
- Test a flat-dollar coupon with a minimum on any ASIN converting below peer median.

**Days 76 to 90: compound.**
- TACoS trend and organic share by keyword; cut cannibalizing spend, keep rank defense.
- 10% price step on the strongest ASIN, Buy Box watched daily.
- Reorder funded for 60 days plus lead time; claims reconciled; alerts set.
- Exit check: TACoS falling while total sales hold or grow, review count and rating rising, cover above lead time plus buffer.
