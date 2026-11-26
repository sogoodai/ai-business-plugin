# Shopify DTC playbook

For brands selling from their own store (Shopify, WooCommerce and similar). The store wins when the product needs explanation, bundles, subscriptions or a first-party relationship. It loses when it is a fresh store buying cold traffic for a low-AOV product. Offers and the promotion calendar are in [offers-and-calendar.md](offers-and-calendar.md); email and SMS depth in sibling skill `email-sms-loyalty`; ad account mechanics in `paid-ads`.

## Before traffic: the store-ready checklist

- A real test purchase and a real refund, on mobile.
- "Continue selling when out of stock" off unless preorders are intended (one store sold 50 units in 12 minutes, 30 of them oversold).
- Every discount code tested in every market it should and should not work in (a Germany-only 30% code worked in Austria: 400 orders, about €18k lost).
- Every product in a shipping profile, or checkout breaks.
- Shop Pay, Apple Pay, Google Pay and PayPal on. One store had zero sales in two weeks without PayPal and two orders the night it was added (confounded with an ad change, 212-pt thread).
- Purchase tracking verified end to end: Shopify's native Google and Meta channels first (server-side CAPI at Enhanced or Maximum), one sender per platform unless event IDs deduplicate (coreyhaines31 harvest, MIT).
- Category conversion baseline written down: beauty 5.32%, food 4.58%, fashion 2.77%, home 1.29%, jewelry 0.63% (Shopify/Dynamic Yield 2026). Compare to the category, not "2 to 3%".

## Product page levers, with the best evidence available

| Lever | Evidence | Do |
|---|---|---|
| Checkout friction | Cart abandonment 70.22%; checkout UX alone could lift large sites 35.26% (Baymard 2026) | One-page checkout, express wallets above the form, email first, guest checkout, shipping cost shown before checkout |
| Product recommendations on PDP and cart | 10.32% vs 2.43% conversion, $3.91 vs $0.86 per PDP visit with a recommendations app (operator, 160-pt thread; method not described) | 3 to 4 recommendations below Add to Cart; hand-pair new SKUs with bestsellers for 30 days |
| Installment payments | Afterpay added: 2.9% to 6%+ in 2 months (operator, uncontrolled); Klarna reported +30% by one seller, but another lost Shopify Payments on 2 stores and saw chargebacks before returns arrived | Show installments on PDP and cart for AOV $100+; check fees (BNPL 4 to 6% vs ~3% card) and processor terms |
| Subscription framing | +29% subscription opt-ins, +9% sitewide conversion at 99% confidence (Magic Spoon, Shopify case) | State the subscriber benefit plainly near the price, only for real replenishment products |
| Page speed | -1 s mobile load associated with about +3% conversion; pages over 4 s 22% lower (Yottaa 2025, observational) | Real-user tests only; reject "PageSpeed 90+ in 24 h" gigs that inject scripts to fool test tools (operator exposé, 154-pt thread) |
| Photos | Almost every buyer viewed 3+ photos; barely anyone read past paragraph 2 (operator analytics, 271-pt thread) | 3+ images minimum; image 2 = scale in hand; essentials in the first 2 paragraphs |
| Why-copy | Operator recommendation (169-pt) | Replace "Seamless hems for a smooth feeling." with "We decided to use seamless hems on our shorts to avoid chafing on your legs while running." |
| Mobile buy button visible | Session recordings showed it below the fold; moving it up "a few pixels" raised conversion (282-pt thread) | Sticky Add to Cart on mobile when the main button scrolls away |
| Real scarcity | Resetting countdown timers read as fake; real stock counts ("4 products left") and "notify me when back in stock" at zero (169-pt thread) | Timers only for sales that truly end; same-day cutoff timer ("order in the next X hours for same day fulfillment") is honest urgency |
| Returns line | finsilabs harvest (MIT) | "30-day free returns" or "Final sale" right beside Add to Cart |
| Stars placement | Operator UX advice | Rating and count directly under the product name, above the price |

Rules from the data:

- **Optimize contribution per session, not conversion rate.** A discount or a free-shipping change can lift conversion and lower contribution.
- **Test only big things on small traffic.** At a 3% baseline a 20% lift needs about 14,000 visitors per variant (Replo 2026). Test offer architecture, hero content, shipping promise, bundles, size guidance; never button colors.
- **Turn ad winners into PDP modules.** The message that wins in ads becomes the headline, image 2 and the FAQ.
- **Silent user test:** watch a stranger try to buy without help and note every hesitation (shipping, photos, trust).
- **Distinctive product names.** A Gen Z shopper searched the exact product name on TikTok and watched 10+ videos before buying; generic names hand that search to competitors (601-pt thread).
- **Premium materials need measurable cues and local units** (micron counts for wool, inches for US shoppers).

PDP structure that holds up (coleschaffer and ominou5 harvests, MIT): benefit headline; proof subhead; 3 to 5 images with lifestyle and close-up; price with honest anchor; stars and count; 3 to 5 benefit bullets; full-width Add to Cart; shipping, returns and guarantee line; then problem in the buyer's words, mechanism, proof (2 types minimum), comparison table, size or usage guide, 5 FAQs that are real objections. No paragraph over about 40 words on mobile.

## Landing pages for paid traffic

- Cold traffic to a dedicated landing page beat product pages "9 times out of 10" for one operator with 30+ pages built (129-pt thread; no data). Add one line at the top saying who the page is for.
- The ad's promised discount must be visible on arrival, with a dismiss that turns into a sticky element.
- For Google cold traffic: comparison pages, "us vs them", advertorial, or quiz funnel; the promised offer and hero product above the fold (coreyhaines31 harvest, MIT).

## Email capture and flows (summary; depth in `email-sms-loyalty`)

Build in this order before raising campaign frequency: welcome, checkout and cart abandonment, browse abandonment, post-purchase, back-in-stock, replenishment where the product runs out, win-back on the store's real reorder interval. Automated emails earned $2.87 per send vs $0.18 for campaigns (Omnisend 2025 data).

Ecommerce-specific tricks:

- **Back-in-stock is the most under-used flow:** 6.72% conversion and $9.14 per email, used by only 0.6% of brands (Omnisend 2025).
- **Four questions after the email field, no name or phone:** "What are you interested in?", "What matters most to you in what you're interested in?", "How many do you own?", "When are you looking to purchase?" About 96% completion; timeframe answers split 50% today, 47% in a few weeks (181-pt thread). Feed answers to the ESP for segmentation.
- **Resend the welcome offer to non-openers**, "typically the highest-converting email in the flow" (177-pt thread).
- **Cart flow by objection, not "you forgot something".** Objection by cart value (coleschaffer, MIT): under $30 "do I need this?"; $30 to $100 "cheaper elsewhere?"; $100 to $300 "can I justify it, will it work for me?"; $300+ "need to ask someone". Never discount message 1; new customers 10% after 24 h, repeat customers free shipping only, VIPs reminder only; if over 30% of recoveries used a code, the discount comes too early (finsilabs, MIT).
- **Split abandoned cart by buyer status:** past buyers 2 emails over 2 days, never-bought 3 emails over 2 days.
- **Popup:** test it. One brand ran 50+ versions over 7 months and moved signup from 2.8% to about 7% (28-pt thread). Delayed popups (20 to 50 s) captured 20 to 43% more in Wisepops tests. Dedupe: about 25% of signups can be repeat people re-claiming the discount.
- **Subscriber-for-a-year offer:** a unique code good for 20% off, capped at 6 uses over 12 months, inserted into every email, all other coupons off; faster repeat purchase reported (181-pt thread; margin was about 10x COGS).
- **Collect SMS 3 months before BFCM** and send the first text on sale day.

## Paid traffic (summary; depth in `paid-ads`)

- **Ads come after the store converts and the economics allow.** Break-even first-order CAC from [economics.md](economics.md) vs a $38.99 Meta ecommerce median CPA (Triple Whale 2025 to 2026). If contribution per order is under the likely CPA, fix AOV first.
- **Visually demonstrable products start on Meta; search-demand products start on Google Shopping** with a clean Merchant Center feed. One operator ran $200k then $300k a year at 35% margin with Google Shopping as the main channel and Meta only for retargeting.
- **Consolidate.** At $10 to $50 a day: one campaign, normally one ad set, a few genuinely different concepts (research synthesis 2026). Only 5 to 8% of creatives become winners (Motion 2026), so concept breadth beats polish.
- **Do not judge an ad before it has spent about 2x AOV;** kill a $25 product that spent $250 with zero sales. One operator spent $3,000 on a $20 product with no sale.
- **Gate cold spend on retargeting:** if retargeting is unprofitable, cold will be too.
- **Always have the next creative in production.** One store at $10k a day revenue went to zero when its last of three creatives burned out (2,332-pt thread).
- **MER and new-customer CAC are the business truth;** platform ROAS is for in-platform decisions only.

## Fraud and chargebacks

- **Statement-descriptor code:** add a rotating 4-digit code to the billing descriptor ("SP * Store 8426"); for medium and high-risk orders, ask the buyer for the code on their statement before fulfilling, cancel if they cannot confirm (179-pt thread; "saved thousands" over a year).
- **Manual capture plus Shopify Flow auto-capture for low-risk orders,** so fraud is cancelled before capture and fees are not lost. During card-testing attacks (hundreds of orders seconds apart), require customer accounts temporarily.
- **Auto-cancel rules:** high risk score, IP far from shipping, first-time buyer choosing express, order over 2x AOV, identical quantities to one address under different names (one store owed $3,013 after shipping those).
- **Amazon "Buy For Me" orders** (emails ending buyforme.amazon) showed a 28% chargeback rate for one store; cancel with a Flow rule and opt out via branddirect@amazon.com.
- **Dispute file:** full journey (ad referral, pages viewed, delivery proof, emails and calls attempted) before the deadline; lead with the fact that answers the reason code.
- **"Delivered but missing" script** in [scripts.md](scripts.md); the package turns up about 75% of the time for one operator. Never ship an exchange before the original return arrives.
- **Keep a backup payment processor;** a $90k-a-month subscription brand was terminated and every subscriber had to re-enter a card.

## 90-day plan: Shopify DTC

**Days 1 to 14: economics and plumbing.**
- Contribution and break-even ROAS per hero SKU; category conversion baseline; store-ready checklist done; tracking verified.
- Welcome, cart and checkout abandonment, post-purchase and back-in-stock flows live.

**Days 15 to 45: demand from existing intent.**
- Communities, gift-guide press, creators seeded (see [first-100-sales.md](first-100-sales.md)); Google Shopping feed clean ([ai-shopping.md](ai-shopping.md)); Pinterest if the product is planned and visual.
- PDP rebuilt around the objections and words that sold; recommendations block; installments if AOV $100+.
- One AOV lever live: bundle, threshold or post-purchase offer ([offers-and-calendar.md](offers-and-calendar.md)).

**Days 46 to 75: paid, only on proven loops.**
- Meta or Google at a learning budget sized from CPA; 4 to 6 distinct concepts; creator footage with usage rights.
- Fraud rules on; statement-descriptor code; dispute template.

**Days 76 to 90: compounding.**
- Cohort repeat rate vs category benchmark; replenishment trigger at median reorder interval minus shipping days; win-back on the real interval.
- Promotion calendar built from contribution ([offers-and-calendar.md](offers-and-calendar.md)).
- Exit check: new-customer CAC under the ceiling, MER stable as spend rises, contribution per session up since day 1.
