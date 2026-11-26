# AI shopping, feeds and product search

"AI optimization" for a store is mostly merchant-data hygiene plus product facts written in text. An assistant cannot recommend "fits a 16-inch laptop", "machine washable at 30°C" or "compatible with model X" if that fact is missing or inconsistent across the page, the feed and the marketplaces. Fixing the catalog improves Google Shopping, Performance Max, free listings, AI Mode and ChatGPT shopping at once.

## What changed in 2026

- **Google:** no special AI markup. Search Central says normal SEO fundamentals apply to AI Overviews and AI Mode, pages must be indexed and snippet-eligible, and Google **does not use llms.txt** (Google Search Central, 2026). Merchant Center added AI-performance insights in May 2026: share of voice on AI surfaces, funnel, product terms and attribute-completeness for AI Mode, AI Overviews and Gemini, rolling out first in the US, Canada and Australia.
- **ChatGPT:** product results are not ads; merchant ranking can weigh availability, price, quality and whether the merchant is the maker or primary seller. Shopify product data flows in through Shopify Catalog; direct product feeds improve freshness and are approval-controlled (OpenAI Help and Developers, 2026).
- **Businesses in ChatGPT (beta, November 10, 2026):** eligible businesses can claim and verify, update details, add product feeds with current price and availability, and see discovery insights; eligible Shopify merchants connect through Shopify. Claiming does not guarantee placement or sales (OpenAI).
- **Universal Commerce Protocol (UCP):** co-developed by Google with Shopify, Etsy, Wayfair, Target and Walmart for agent checkout. Early; a watch item, not a priority for a small store (AgriciDaniel harvest, MIT).

## Actions, in order

1. **Claim and verify** the business in ChatGPT where eligible; connect Shopify; check what the catalog shows for name, variants, price, images and stock.
2. **Merchant Center (Google) and Bing Merchant Center (Microsoft).** One store had zero ChatGPT-sourced visits before listing in Bing Merchant Center and sales from that source after (r/shopify, 26 up; mechanism questioned). Cheap to do.
3. **Clear disapprovals before polishing titles.** Disapproval causes in order: GTIN, price mismatch, availability, image, title or attribute mismatch, policy, unsupported claims (aaron-he-zhu harvest, Apache-2.0).
4. **Price and stock parity.** Feed price must equal the landing page exactly (a one-cent gap disapproves). Keep `price` as the regular price and discounts in `sale_price`; use `preorder` or `backorder` with `availability_date` instead of false in-stock.
5. **GTINs:** valid and unique per product; `identifier_exists: no` plus brand and MPN only for truly exempt items (custom, handmade, some bundles). Missing GTIN is the most common cause of reduced impression share. Never invent a GTIN, price or spec.
6. **Attributes complete:** material, dimensions, fit, compatibility, color, size, gender and age group (required for apparel), `item_group_id` for variants, `product_highlight`, custom labels for margin and season.
7. **Facts in page text, not trapped in images:** spec table, dimensions, care, compatibility, "who it is for", comparison table with real numbers, an FAQ of real objections.
8. **Product structured data server-rendered:** `Product` with `Offer` (not `AggregateOffer`), numeric price, ISO currency, availability URL, `brand`, `sku`, `gtin` or `mpn`, `shippingDetails`, `hasMerchantReturnPolicy`; `ProductGroup` with `variesBy` and `hasVariant` for variants; `aggregateRating` only from real reviews (AgriciDaniel harvest, MIT). Shipping and returns can be set in Search Console without Merchant Center.
9. **Monitor what AI says about the store.** Shopify's Shop AI Highlights blended a product summary with a bundle and told buyers an accessory was free; the seller shipped accessories at their own cost (r/shopify, 52-pt thread). Gemini invented scam claims about one store and stopped about 3 weeks after the owner filed Google feedback (r/ecommerce). Ask ChatGPT, Gemini and Google AI Mode the questions buyers ask each month and log errors.
10. **Use Merchant Center AI-performance reporting** where available; ignore vendors selling llms.txt as a Google ranking factor.

## Feed titles

Lead with what the shopper types. Brand first only if shoppers search the brand; small unknown brands lead with product type (aaron-he-zhu and coreyhaines31 harvests agree).

| Vertical | Title pattern |
|---|---|
| Apparel | Brand + type + key attribute + color + material + size + gender |
| Home | Brand + type + feature + material + dimensions + color |
| Beauty | Brand + type + key attribute + volume + skin or hair type |
| Consumables | Brand + type + flavor + count + size |
| Electronics accessories | Brand + model + type + key spec + capacity + color |

About 150 characters max on Google, Meta and Microsoft; the first ~70 carry matching and clicks; a truthful 60-character title beats a stuffed 150. No promo text, "Free Shipping", "%", ALL CAPS or emoji in titles. Variant words in the title must match the `color` and `size` attributes or the item is disapproved (aaron-he-zhu harvest, Apache-2.0).

Feed refresh: Merchant Center every 6 hours, Meta and TikTok catalogs at least daily; push price changes during promotions through the API rather than waiting for a crawl.

## Marketplaces as AI surfaces

- **Amazon Rufus-style ranking** rewards situational language: when, where and why the product is used, and several use cases in bullets (nexscope harvest, MIT).
- **Consistent entity data** across the site, Amazon, Etsy and Merchant Center (same name, dimensions, materials) helps assistants trust the product.
- **Distinctive product names** let buyers search the exact product on TikTok and Google instead of a generic term that competitors own.

## Content that gets cited

For brands with a content site or blog (operators report, r/juststart 2026, weak evidence): answer the question in the first 2 to 3 sentences under one question per H2; exact specifications instead of adjectives; comparison tables with real numbers; schema that matches visible text; submit new pages to IndexNow and Bing Webmaster on publish day (Bing indexed in 24 h while Google lagged 5+ days in one test). Verify every product link an AI tool writes: one site found 82% of AI-written product links were fake until checked.
