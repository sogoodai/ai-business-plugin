# Cart and checkout

For stores, checkout is usually the largest addressable leak and the cheapest to fix. Product page structure, Shopify store setup, fraud rules and AOV offers live in sibling `ecommerce-brand`; this file owns the generic cart and checkout depth. Sources in [sources.md](sources.md).

## The numbers that matter

| Metric | Typical | Better | Source, year |
|---|---|---|---|
| Cart abandonment | 70.22% average | No valid "good" line | Baymard, updated 28 October 2026 (unweighted average of 50 studies, 2006 to 2025) |
| Shopify checkout completion (purchase sessions / checkout-start sessions) | 47% median | 64% top 20%, 73% top 10% | Littledata, November 2026, 450 stores |
| Shopify add to cart rate | 6.9% median | 13% top 20%, 17% top 10% | Littledata, November 2026 |
| Shopify session to purchase | 1.3% median | 2.8% top 20%, 3.6% top 10% | Littledata, November 2026 |
| Form elements in an average US checkout | 23.48 | 12 to 14 is achievable | Baymard 2026 |
| Large sites rated "mediocre" or worse on checkout UX | 59% desktop, 59% mobile | 2% desktop rated "good" | Baymard 2026 benchmark, 44,000+ usability scores |
| Modeled conversion gain from fixing checkout UX | 35.26% | n/a | Baymard 2026; a modeled ceiling for large sites, not a test average |

**Why shoppers quit** (Baymard 2026, US survey, reasons after removing "just browsing"): extra costs too high 40%, delivery too slow 20%, did not trust the site with card details 19%, forced account creation 18%, too long or complicated 17%, errors or crashes 17%, unsatisfactory returns policy 13%, could not see or calculate total cost upfront 12%, card declined 10%, not enough payment methods 9%.

**Operator diagnostics** (r/shopify, r/FacebookAds; useful triage lines, not benchmarks): initiated checkouts to purchases under about 50% means checkout friction, check shipping cost surprises and pre-purchase upsells in recordings (81 upvotes); add to cart to checkout 3:1 or better and checkout to purchase 2:1 or better before scaling ads (sibling `paid-ads`).

## Fix order (do not start with trust seals while fees are hidden)

1. **Total cost before checkout.** Shipping cost or a free-shipping threshold on the product page and in the cart; product-specific surcharges (oversize shipping, country VAT or duties) shown beside the price, never first revealed at payment (r/shopify product page guidelines, 66 upvotes). A shipping estimator in the cart for stores with variable rates.
2. **Delivery date, not delivery speed.** "Arrives Tue 18 to Thu 20 Nov" beats "3 to 5 business days". 48% of large sites still show speed instead of date; 83% do not show the order cutoff as a countdown ("Order in the next 3 h 12 min to ship today"), which is honest urgency (Baymard 2026).
3. **Guest checkout, account invite after payment.** 56% of sites still ask for account creation before the confirmation step; Baymard's testing found the post-purchase invite works better. Make the guest option the most prominent choice (47% of sites do not).
4. **Express wallets above the form.** Shop Pay, Apple Pay, Google Pay, PayPal; plus the local methods your market expects (iDEAL in the Netherlands, Bancontact in Belgium, Klarna in Nordics and Germany, Afterpay in Australia). One operator saw zero sales for two weeks without PayPal and two orders the night it was added (confounded, cited in `ecommerce-brand`).
5. **Fewer fields.** Target 12 to 14 elements. Single name field where the platform allows, address autocomplete, Address line 2 behind a link, company field behind a link, billing = shipping by default, no "confirm email".
6. **Phone field honesty.** 68% of shoppers are reluctant to give a phone number; 47% of sites do not explain why it is required. Make it optional, or add "For delivery questions only" under it.
7. **Mark required and optional fields both.** When only optional fields were marked, 32% of test users failed to complete at least one required field (Baymard 2026).
8. **Errors that help.** Inline validation after the field loses focus, message next to the field saying how to fix it, input never cleared. 98% of sites do not adapt error messages to the specific mistake.
9. **Payment trust where card details go.** Encase the card fields in a distinct box or background used nowhere else; put 1 or 2 icons (padlock, a recognized seal) inside that box; reassuring microcopy beside the fields (Baymard perceived-security research). Badges in the footer do nothing for this worry.
10. **Returns line near the decision.** "Free 30-day returns" or "Final sale" beside the add to cart button and in the cart. A poor returns policy is 13% of actionable abandonment.
11. **Coupon field.** Collapse it behind a "Have a code?" link so it does not send shoppers off to search for codes; avoid a separate "Apply" button that users miss (Baymard; 22% of sites still use one).
12. **Card declines.** Look at the processor's decline codes weekly. A spike in "do not honor" on one card type or country is a fixable payment configuration problem, not abandonment.

## Cart page

- Quantity with plus and minus buttons (95% of sites in the 2026 benchmark do not offer buttons or buttons plus a text field).
- Cart contents, thumbnail, variant, price, total with shipping estimate, delivery date, returns line, express wallets, one checkout button.
- Cross-sell at the cart or post-purchase, priced under 50% of the main item (r/shopify, 154 upvotes); keep it below the checkout button so it never blocks the path.
- Let shoppers mark an order as a gift in the cart (68% of sites do not).
- Show all fulfillment options, including local pickup, in the shipping selector (53% of sites do not).

## Checkout legal traps

- **Drip pricing.** California's Honest Pricing Law (SB 478, from 1 July 2024) requires the advertised price to include all mandatory fees except government taxes and shipping. The FTC's Rule on Unfair or Deceptive Fees (from 12 May 2025) requires total price display for live-event tickets and short-term lodging. In the EU, the price shown must include VAT for consumers. See [accessibility-and-legal.md](accessibility-and-legal.md).
- **Pre-checked boxes.** Pre-ticked marketing consent is invalid under GDPR; pre-ticked recurring or "double your donation" boxes led one fundraising platform to refund about $122 million (r/userexperience, 138 upvotes). Shopify's "preselect the signup option" is only for stores not selling to the EU or UK.
- **Compare-at prices.** Keep dated records of every original price; a retailer sued over markdown pricing struggled to prove its compare-at prices from a year earlier (r/shopify, 242 upvotes). EU stores must show the lowest price of the previous 30 days when announcing a reduction (Omnibus Directive).

## Monitoring

- **Run a test order weekly** on mobile with a real card, and after every theme, app or payment change. Checkouts break silently: one owner's store-health alert flagged the day checkout actually broke (r/shopify, 43 upvotes).
- **Track checkout completion separately from add to cart.** Littledata's median store converts 6.9% to cart but completes only 47% of checkouts: two different problems.
- **Abandoned checkout email:** send to anyone who entered an email, at 1 hour instead of a 10-hour default (r/shopify agency owner, 78 upvotes). Flow depth lives in `email-sms-loyalty`.
- **Fraud and bot carts:** 500+ fake carts an hour reached one store through the `*.myshopify.com` hostname, bypassing its Cloudflare rules (r/shopify, 125 upvotes). Fraud rules and chargeback scripts live in `ecommerce-brand`.

## Worked example: what a fix is worth

Littledata's median store: 1.3% conversion, $111 AOV. At 10,000 sessions a month that is about 130 orders and $14,430. If checkout completion moves from 47% to 55% with the same checkout starts, orders rise by 55/47 - 1 = 17%: about 22 more orders, $2,450 a month. Compute it with the store's own checkout-start count and AOV before promising anything; Baymard's 35.26% is a ceiling for large sites, not a forecast.

## Tricks most owners miss

- **Fix the reason with the biggest share first.** 40% of actionable abandoners cite extra costs; seals answer only the 19% trust problem.
- **Delivery date + cutoff countdown** is honest urgency that most sites skip.
- **Encase the card fields.** Visual separation raises perceived security at near-zero cost.
- **The coupon field leaks buyers.** Hide it behind a link.
- **Weekly real test order.** The most common catastrophic loss is a checkout that silently broke after an app update.
