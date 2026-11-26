# Channels: DTC, Amazon, TikTok Shop, Faire, retail

Choose channels by contribution dollars per shipment and by where repeat can happen, not by the founder's preferred model. Platform mechanics (Shopify setup, Amazon PPC, Etsy, TikTok Shop operations) live in sibling `ecommerce-brand`; this file keeps the CPG angle.

## Which channel carries which product

| Product shape | Best first channels | Why |
|---|---|---|
| Low-price single unit, heavy or fragile (sauce, jam, drink) | Markets, independents, grocery | Shipping kills single-unit DTC |
| Naturally multi-unit or replenished (coffee, tea, protein, snacks by the case) | DTC subscription, Amazon Subscribe and Save, cafes and offices | Order value and repeat carry shipping |
| Giftable sets (sauce trios, tea samplers, skincare kits) | DTC in Q4, gift guides, corporate gifting, Faire | High AOV, seasonal peaks |
| Visible-result or texture products (skincare, makeup) | TikTok Shop and creators, DTC, then specialty retail | Content sells the result |
| Supplements | DTC subscription, Amazon | Replenishment, search demand; ad policy friction |
| Cottage food | Markets, preorders, local pickup | Law limits shipping and wholesale |

## DTC

- **Paid acquisition benchmarks:** food and beverage median paid CPA $29.66, health and beauty $31.87 (Triple Whale, 55,000+ accounts, Sept 2025 to Aug 2026, vendor). Median Meta ROAS about 1.61 food, 1.54 beauty, 1.44 health (Adwize 40,000-brand dataset, Aug 2025 to Jul 2026). At 50% contribution margin, 1.5x ROAS is below the 2.0x break-even.
- **Conversion and repeat (European DTC panel, adtribute, Sept 2026):** beauty 3.03% conversion, health and nutrition 2.94%; 90-day repeat 15.02% beauty, 12.12% health.
- **Shopify store conversion by category:** beauty 5.32%, food 4.58% (Dynamic Yield via Shopify, 2026; see `ecommerce-brand`).
- **Rule:** raise AOV with 2 to 4 unit starter bundles before buying much paid traffic (deep research, 2026). Test offers with separate ads: "Try 1 on us," "buy 1 box get 1 free," "buy 2, get 4," "a year's supply, save 60%" (suggested by a commenter, untested; pick the ones the margin allows).
- **Gifting is the food DTC season.** Update flows for December with gift positioning; one operator reports Christmas-themed emails beating regular emails by 30% in December across several brands (operators report). Founder thank-you email after BFCM with a free gift on orders for three days beat the Black Friday email "80% of the time" in one operator's experience (operators report, metric unstated).
- **Gift guides and press.** Mantry (food subscription box) attributed $400,000 in sales to press; one Today Show segment drove $24,000 in a day. Find last year's guides by searching "[holiday] gift guide" with a custom date range of the month before that holiday (operators report, 272-pt thread). Script in [scripts.md](scripts.md).

## Subscriptions

**The data:** first-renewal churn is 28.2% for food and beverage, 26.5% health and wellness, 26.3% beauty; mature cycles churn 6.4%, 7.5% and 8.5% (Recharge, renewals July 2025 to March 2026). Across 65.1 million subscriptions at 13,158 Shopify brands, about two-thirds continue after order one and fewer than 40% remain by order three (Recharge, 2026).

**Design rules:**

1. Do not lead with "subscribe and save" before the buyer knows how fast they use the product.
2. Sequence after the first order (deep research, 2026):
   - Day 0: how to use and store it.
   - Day 5 to 10: fix common failure modes; ask a preference question.
   - At 50 to 70% of expected depletion: "Running low?" reorder.
   - After demonstrated use: offer the subscription or a larger cadence.
   - Before the first rebill: reminder with skip and change-frequency options.
3. Report churn by renewal number, not just monthly churn.
4. Make the first box complete even at low margin. A wet-shaving subscription put everything a beginner needed in box one at 10 to 15% margin, with better margins after (operators report).
5. Raise the price by adding visible value. The same box went from $12 soap-only to $29 with a broader assortment, grandfathered early subscribers at $12 with the new contents, and sold annual prepay (operators report, 1,756-pt thread).
6. Keep payment tokens portable. A supplement brand with $90,000 a month in subscriptions on one processor had to ask every subscriber to re-enter cards after the processor terminated it (operators report). Use a subscription app and processor setup that lets you migrate tokens, and keep a backup processor.

**Referral that works for subscriptions:** at the one-year anniversary, the founder emails each subscriber personally and offers to send a free box to someone they know "who would love" it, with a 10% insert in the gift box. App-based "refer a friend, get 15%" got little response for the same food subscription operator (operators report). Script in [scripts.md](scripts.md). Flow mechanics: sibling `email-sms-loyalty`.

## Amazon

- **Fees:** grocery 8% at $15 or less, 15% above; beauty, health and personal care 8% at $10 or less, 15% above; FBA about $2.43 to $5+ per standard unit in 2026, before storage and inbound placement (Amazon, Nov 2026). Price off the cliff: see [economics.md](economics.md#waterfall-4-amazon).
- **Subscribe and Save:** sellers fund 0, 5, 10, 15 or 20% base discounts; Amazon may add 5% when shoppers combine five or more subscriptions; Amazon claims 10 to 15% discounts have driven up to 1.8x conversion (self-reported).
- **Shelf life:** at check-in, products must have enough remaining shelf life to be consumed in full plus 90 more days; a 240-day supplement supply needs 330 days left (Amazon help page). Third-party guides cite 90 to 105 days for food; check the live page. Short-dated items near expiry are removed or disposed.
- **Stranded units:** one seller with 3,000 units of each top product found 2,000 sitting in a supplemental storage facility that did not fulfill orders; Prime badges dropped and ACoS spiked while PPC ran over $150,000 a month until support moved them (operators report).
- **Reviews:** use Amazon's Request a Review button; no inserts offering anything for reviews. Amazon bans incentives even where the FTC would allow a neutral one.
- **Supplements:** operators report automatic campaigns working when target terms are expensive, with TACoS around 20% (r/FulfillmentByAmazon). Expect category approval and documentation requests.
- **Amazon versus your site:** one seller paid about 30% on Google Ads versus about 15% Amazon fees, but about 40% of site customers repeated within 12 months, so considered reserving scarce stock for the site (operators report). Compare repeat-adjusted contribution, not fee percentages.
- **Plan for freezes.** An account deactivated for three months into Christmas held funds while storage fees continued (operators report). Do not depend on one marketplace for peak-season cash.

## TikTok Shop and creators

- **Mechanics (TikTok, 2025 to 2026):** 6% referral fee per sale (US); affiliate commissions you set from 1 to 80%, calculated net of refunds; 30-day commission protection for creators already promoting when you cut a rate; GMV Max is the only new Shop sales campaign type since July 2025 and can use official, affiliate and approved creatives.
- **Start:** about five different videos per new GMV Max campaign; pick 3 to 7 best sellers for a new shop; TikTok suggests scaling products with more than $1,500 GMV in the prior seven days (platform guidance, not neutral).
- **Loop:** seed product to many category-matched creators on commission, find the videos with strong click and order economics, authorize them, let GMV Max scale, keep adding creative (deep research, 2026).
- **Cases (platform-selected, directional only):** French skincare brand Mela'Aura sent about 50 creator samples a week and reported 4,600+ Q1 2026 orders, €233,000+ revenue and 3x ROI. Love and Pebble reported 3.2x ROAS after leaning into affiliate content.
- **Operators report:** a candle video at 400,000 views brought 800 orders in 48 hours; packing ran to 2 am, messages went unanswered, reviews turned negative. Set a maximum daily order count or pause listings before ops break. A seller doing $95,000 GMV a month hired two livestream hosts and credited live demos (r/TikTokshop).
- **Category traps:** a supplement listed under Pet Supplies but promoted as a supplement triggered regulated-goods violations, a ban and over $20,000 of frozen affiliate commissions (operators report). List in the right category and keep claims inside the approved bank.
- **Distinct names:** shoppers search TikTok for the exact product name they saw; generic names surface competitors (operators report, 606-pt thread). Give each hero SKU a searchable name.
- **Original content wins reach:** 75% of US Instagram recommendations came from original posts in Q4 2025 (Meta). Use creator and founder footage, not reposts.
- **Creator rates and briefs:** sibling `ecommerce-brand` (creators reference) and the claims-safe brief in [scripts.md](scripts.md).

## Faire and wholesale marketplaces

- Fees: 15% + $10 on opening orders from marketplace-discovered North American retailers; 0% on Faire Direct; processing 1.9% + $0.30 to 3.5% + $0.30; outside North America the first marketplace order can carry 25% (Faire, Nov 2026). Check the live fee table before pricing.
- Use marketplace discovery only where its acquisition fee is acceptable; route every store you find yourself through Faire Direct. Never move an existing marketplace account off-platform against Faire's terms; choose the path before the first order (deep research, 2026).
- Reorder behavior and the reorder timer: sibling `ecommerce-brand` wholesale playbook.

## Subscription boxes

Search Cratejoy for niche boxes and pitch the operators directly. One brand got a 5,000-piece order to produce in 30 days at a deep discount; the founders worked out to about $2 to $3 an hour (operators report, 151-pt thread). Price the labor and treat exposure as a separate, unproven benefit.

## AI shopping and product data

- Google AI Mode draws on the Shopping Graph (50+ billion listings, 2 billion+ refreshed hourly, Google 2025). Merchant Center's AI performance insights show share of voice across AI Mode, AI Overviews and Gemini in the US, Canada and Australia (2026).
- Merchants adopting Google's core feed best practices saw an average 5% conversion increase the following month (Google, Sept 2026, platform-reported).
- **Do:** exact GTIN and brand, price and availability identical on site and feed, flavor, size, heat level, dietary flags (vegan, gluten-free where true), skin type, ingredients, shipping and returns, reviews, real images; Product and Offer schema matching the visible page.
- One operator reports $15,000 revenue from free Google listings for a friend's beauty brand after connecting Merchant Center (operators report).
- ChatGPT shopping and Merchant Center steps: sibling `ecommerce-brand` (AI shopping reference).

## Channel conflict rules

1. Separate SKUs, pack sizes or bundles between big retail and Amazon. Price matching works per ounce, so a different size alone may not protect you.
2. Screen wholesale accounts that also sell online; set and enforce a MAP policy.
3. Keep DTC prices at or above shelf price unless the DTC offer is a different pack.
4. When a reseller marks you up online, raise your own retail price (see `ecommerce-brand`).
