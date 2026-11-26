# Memberships, subscriptions, payment plans, BNPL and deposits

How customers pay changes what they buy. Sources: [sources.md](sources.md). Formulas: [economics.md](economics.md) sections 8 to 11.

## When recurring billing fits

Use it only to make a naturally recurring need easier. Do not manufacture recurrence.

| Good fit | Poor fit |
|---|---|
| Fixed cadence the customer already follows (lawn, pool, pet waste, cleaning, color, lashes, massage, coffee, supplements, pet food) | One-time events (weddings, moves, a single project) |
| Software or content used every week | Tools needed for a few months. Wedding software switched from monthly to one-time event passes ($69 to $149) and conversions "jumped immediately" (r/Entrepreneur, 558 upvotes) |
| Spare off-peak capacity to absorb member visits | Peak-only demand. A 9-court facility avoids memberships so members are never paying for courts they cannot book (44 upvotes) |
| Consumables with a predictable use rate | Products bought on impulse or as gifts |

## Designing the plan

1. **Define the unit and the limits.** Visits per month, included tasks, items per box, users or usage. "Unlimited" needs a fair-use clause and a capacity check.
2. **Price from expected use.** Member contribution = fee minus expected redemptions times cost per redemption minus card fees. Pilot one cohort before opening to everyone.
3. **Define what the visit includes and quote the rest.** A home maintenance subscription listed inspection plus named tasks; a commenter warned that "leak inspection" otherwise gets read as a free two-hour leak repair. Time a full visit at your own property, add travel, apply the target hourly rate and margin, and cut tasks rather than price if it is too high (r/sweatystartup).
4. **No contract can be a selling point.** Pet waste removal sold "subscription, no contract": weekly $18 to $25, biweekly $25 to $35 per visit (46 upvotes). Another starts at $45 a month weekly, priced by dog count, not yard size; over $2,000 subscription revenue in month three (24 upvotes). A third prices $16 for one dog, $19 for two, $4,000 a month and 8 to 12 new clients a month (117 upvotes).
5. **Annual bundle in monthly installments for seasonal services.** A landscaper bundles the whole year into one flat agreement paid monthly, priced at $100 per labor hour plus materials; year four, $100,000 take-home on just over $300,000 gross (63 upvotes). Cash flow evens out and the customer stops comparing each visit.
6. **Charge for the catch-up visit.** When service pauses in winter, the first spring visit costs more: one yard held 217 piles (12 upvotes).
7. **Expand value before raising the price.** A shaving subscription grew the box from soaps only at $12 a month to a fuller assortment, rebranded, then charged $29; conversion rose (1,754 upvotes, combined changes).
8. **Front-load the starter kit.** The first shaving box held everything a beginner needed at a 10 to 15% margin; later boxes made the margin back.
9. **Starter offer that converts to the plan.** Gym: free personal training session plus two free weeks of small group training, all selling done from a phone CRM; reported client lifetime value about $1,800 (32 upvotes). A gadget brand included 3 free months of content that converts to a small paid monthly plan (129 upvotes).

## Retention mechanics that change lifetime value

- **The first two renewals are where subscriptions die.** About 61% of voluntary churn happens at cycles two and three; first-renewal churn is 28.2% in food and beverage, 27.8% pet, 26.5% health and wellness, 16.1% fashion (Recharge, 2026). Put onboarding, usage guidance, a "too much product?" skip prompt and the save offer before reorder two, not at month six.
- **Pause, skip and change frequency next to cancel.** Pause-before-cancel use grew 337% year over year, and former subscribers are nearly 1 in 4 new sign-ups (Recurly, 2026). Offer pause only after the customer gives a temporary reason.
- **Save flow, in this order:** ask the reason; temporary reason, offer a pause to a date; wrong fit, show the lower tier or another cadence; price, a targeted temporary concession only if margin supports it; otherwise cancel cleanly and schedule a win-back keyed to the stated reason (research report, 2026).
- **Failed payments are a separate churn.** Track voluntary and involuntary churn apart. Recurly's default dunning window is 10 days; it suggests testing 28 days for monthly and up to 60 for annual plans (vendor). A gym lost about 23% of discounted annual members to cards that would not process (1,353 upvotes). Turn on card updater and smart retries before launch.
- **Make payment tokens portable.** A $90,000-a-month supplement subscription had its card tokens locked to one processor; after an account termination every subscriber had to re-enter a card (r/shopify, 39 upvotes). Ask the processor about token export before launch.

## Annual prepay

- Break-even annual discount = 1 minus first-year paid months on monthly billing / 12. At 3.2% monthly churn that is 16%; at 5%, 23% ([economics.md](economics.md)).
- Market reference: 20% median published annual discount, interquartile 17 to 26% (CostBench, July 2026).
- Default: "2 months free" (17%). Show monthly equivalent and the yearly total. Go deeper only for a cash-flow reason.
- Card-required trials convert 30% versus 8% median overall (ChartMogul, 2026, observational). A 7-day trial beat a 3-day trial on adoption but not on immediate conversion in a 680,588-user randomized test (2025). Do not copy "14 days": 62% of products use it because others do.

## Cancellation law in 2026

- **US federal:** the FTC's 2024 "click-to-cancel" amendments were vacated by the Eighth Circuit on July 8, 2025; the FTC restored the prior Negative Option Rule effective February 12, 2026. State auto-renewal laws (California and others) and general deception law still apply. Easy online cancellation remains the safe default.
- **UK:** new subscription-contract duties under the DMCC Act 2024 and the Consumer Subscription Contracts Regulations 2026 (government guidance October 19, 2026): pre-contract information, reminders and easy exit. Update UK flows against that guidance.
- **EU:** check the member state's consumer rules; do not import US defaults.
- Not legal advice. Flag to the owner when the plan auto-renews and sells to consumers.

## Payment plans and BNPL

- **Evidence:** up to 14% revenue lift from showing one BNPL option, over two-thirds of BNPL volume incremental (Stripe randomized tests, 2024). +21% relative conversion above $250 with Affirm via Stripe (vendor). Operators disagree: one reports +30% conversion from Klarna (13 upvotes); another lost Shopify Payments on two stores, got three complaints in a one-week test, and saw chargebacks filed before returns shipped (32 and 7 upvotes, r/shopify).
- **Rule:** offer installments where the ticket is high (above about $250 for products; big-ticket services such as HVAC, roofing, dental, coaching programs), compute net gain after the fee premium on all BNPL volume, and keep a pay-in-full option.
- **Shopify trap:** native post-purchase offers do not render for Klarna, Affirm, Afterpay or several wallet payments (Shopify docs, 2026), so BNPL can cut upsell exposure.
- **Your own installment plan for services and programs:** price the plan higher than pay-in-full ("$3,000 today or 3 x $1,100") so the full-pay option is the visible deal and the financing risk is paid for. Take the first payment before work starts; card on file with written authorization for the rest.
- **Present installments before the price objection,** not after the customer has already said no to the total.

## Deposits, prepayment and payment timing

- **Appointments:** card on file for every booking; deposit for new clients and long or high-value services. Beauty operators report near-zero cancellations at 50% non-refundable; vendors suggest 20 to 50% (see the beauty-business skill for policy wording).
- **Deposit expiry:** a tattoo artist holds deposits as credit for three months, with exceptions; the deposit covers design and setup (r/smallbusiness). Put an expiry on any credit.
- **Prepay to keep the old price:** when raising rates, offer the original price only to clients who prepay or leave a non-refundable deposit (suggestion, 11 upvotes). It turns a price rise into a cash-flow gain.
- **Custom and made-to-order goods:** full payment including shipping before production, with the production window stated. A seller of $800 to $1,000 pieces with 6 to 8 week lead times reports no complaints and all 5-star reviews (69 upvotes; the top comment, 1,025 upvotes, also says full payment up front).
- **Events and weddings:** 50% on booking is the norm practitioners repeat; when a friend's "come as a guest" turns into coverage, send an invoice with 50% due before arrival and do not shoot unpaid (42 and 33 upvotes).
- **Wholesale and B2B:** prepaid first order, then net terms. Ask for a deposit that funds the materials: one maker secured a 50% advance of $50,000 to fulfil a large chain order (1,914 upvotes, unverified). Decline net 60 plus sale-or-return from a buyer you cannot absorb losing (925 upvotes).
- **Import duties:** collect them at checkout. A Canadian seller added a flat 20% prepaid-duty charge on US orders after duties-on-delivery caused complaints and cancellations (31 upvotes); another reported more than 50% of US delivery-duty-unpaid orders refused (98 upvotes).
- **Processor cost:** compute the effective rate from statements. Gym: pitched about 5% of gross, real cost near 10%.
