# Google, local inventory and AI shopping answers

Profile audit, categories, review math, suspensions and spam reporting live in `local-seo`. This file keeps what is specific to shops: products and stock.

## Why stock data is now the lever

- Google ranks local results on relevance, distance and prominence; review count and rating feed prominence (Google Business Profile Help, current). You cannot out-optimize distance, and reviews cannot fix the wrong category.
- Merchants exposing local inventory got 16% more organic Shopping impressions on average (Google, Nov 2023 to May 2024 global data).
- Adding Local Inventory Ads to Shopping ads gave 21% more store visits and 9% more online conversions for in-store items (Google, data through July 2024). Google-measured, vendor bias, 2024 data: directional.
- The Shopping Graph held 45B+ listings in May 2025 and 50B+ in January 2026, with 2B+ refreshed every hour. Google's May 2025 AI Mode examples answered a vintage-shop query with stores, availability and context. Product and inventory now show in AI Mode, Maps and Gemini.
- Google says profile information comes from the owner, the public web, third-party data and users. Stale listings elsewhere (old hours, old address) create conflicts rather than being ignored.

## Setup order

1. **GBP basics** (depth in `local-seo`): primary category that matches what people search ("Florist", "Book store", "Gift shop", "Antique store", "Vintage clothing store", "Women's clothing store", "Thrift store"); exact hours and holiday hours; storefront photo from the street, interior, best sellers; website link with UTM tags; products with price and photo.
2. **Merchant Center account** linked to the GBP.
3. **Free local listings** first. Connect inventory through the POS integration or Google's Local Inventory app (formerly Pointy). Google says compatible POS inventory can appear automatically; stock status can be inferred from scanning or sales activity, and more frequent updates mean better accuracy.
4. **Validate by hand:** search your top 20 SKUs on Google and Maps from a phone near the shop. Fix what is missing or wrong.
5. **Measure** impressions, clicks, calls, direction requests and store-visit or local-action conversions where the account is eligible.
6. **Only then test paid Local Inventory Ads** on high-margin, high-intent SKUs. Separate them from low-margin inventory or ROAS hides poor gross profit (research synthesis 2026). Out-of-stock products fall out of normal local eligibility (Google Merchant Center Help).

Account and country eligibility differ for paid inventory features and store-visit measurement. Check before promising the owner anything. Campaign setup lives in `paid-ads`.

## Product data that gets found

- **Titles shoppers type, not POS shorthand.** "DW-140 NAV" is invisible. "Navy merino cardigan, women's, size M" is found.
- **Keep identifiers.** UPC, EAN, ISBN where they exist. Bookshops get the most out of this: every book has an ISBN.
- **One-of-a-kind items** (antiques, vintage, art) have no identifier. Write unusually descriptive titles (maker, era, material, dimensions, condition) and remove the listing the minute it sells.
- **Price must match the shelf.** Mismatches get items disapproved.
- **Photos:** clean background, window light, every side. A $15 Marketplace buy resold for $45 two days later after rephotographing with window light and a clean, not overly commercial background (r/Flipping, 2,840 points).
- **Do not show items you are not selling.** A reference photo of matching couches next to a table for sale drew repeated requests for the couches (r/Flipping, 1,491 points).

## Reviews for shops

- **Ask everyone, the same way, without reward.** Incentives (discount, gift, entry, points) break Google policy and can restrict the profile's reviews (Google contribution policy). One shop that gave free product for reviews lost 50+ reviews, was suspended and got a 30-day review block; reinstatement did not restore the reviews (r/GoogleMyBusiness, 2026).
- **Bought reviews vanish and hurt:** 20 bought in 2022; 12 gone in three weeks, 8 a month later, ranking below where it started (r/smallbusiness, 10,237 points).
- **QR on the receipt, on a counter card and in the post-purchase email.** Not an in-store tablet or kiosk.
- **Ask for what they bought.** "Would you mind sharing what you bought and how your visit went?" Reviews naming products help shoppers. A contractor whose next customers named the specific service reported ranking for those terms about three weeks later (r/smallbusiness, 323 points, self-promoting OP, not controlled).
- **Ask for a photo.** Photo reviews show the real place (122-upvote comment). No measured rank lift; do it for conversion.
- **Timing for retail:** 3 to 5 days after purchase in the email flow (AgriciDaniel claude-email template, MIT, uncited), plus the counter QR the same day.
- **Walk-in shops cannot claim "no record of you."** Cash and gift purchases leave no trace; readers distrusted that reply (r/smallbusiness, 486 points, replies at 122 upvotes). Reply to the facts you know.

Wording: [scripts.md](scripts.md#review-request).

## AI answers

- AI Mode and Gemini read stock data and the Business Profile. Accurate feeds and hours matter more than blog posts for "where can I buy X near me".
- If the shop sells online, also list products in Bing Merchant Center: ChatGPT search leans on Bing's index (see `local-seo` by-niche, single 2025 report).
- Do not block search crawlers you want answers from. One commenter warns a WordPress "block AI crawlers" plugin also blocked OAI-SearchBot and PerplexityBot; block training bots (GPTBot) if you must and keep search bots and facebookexternalhit allowed (r/smallbusiness, 764 points).

## Tricks most owners miss

- **Holiday hours are a ranking and trust event.** Set special hours for every holiday weeks ahead; "open now" filters drive last-minute footfall.
- **Monitor the chain, not views:** search terms, then calls, directions and website clicks, then store transactions. Profile views are not success.
- **Post-view counts per GBP update** came back in 2026, covering 18 months and combining Search and Maps (r/GoogleMyBusiness, 47 points). Use them to compare which product or event posts get seen, not as sales.
- **A coffee shop that completed every GBP field, refined categories and aligned site titles and H1s with the profile** reported Maps visibility 40% to 70% and direction requests 180 to 240 in 12 days, with no new reviews or ads (r/localseo, 36 points, marketer's own case, bundled changes).
