# Mechanics and decision sources

Checked 16 November 2026. These sources inform the modeling choices, not the user's actual fees, outcomes or authorization. Verify the relevant account's current contract before using its figures. No third-party code or prose was adapted.

| Source | Decision it supports |
|---|---|
| [Stripe refund documentation](https://docs.stripe.com/refunds) and [fee explanation](https://support.stripe.com/questions/understanding-fees-for-refunded-payments) | Original processing fees may remain after a refund; refund fees can depend on method and pricing. Enter original fees and actual fee credits separately. Available processor balance and pending refunds also demonstrate why expense economics and spendable cash differ. No Stripe rate is hardcoded. |
| [Shopify Payments refunds](https://help.shopify.com/en/manual/payments/shopify-payments/payouts/refunds) | Shopify Payments does not reimburse the original credit-card fee when refunding. Do not apply that rule blindly to every gateway, marketplace or custom contract. |
| [Shopify third-party transaction fees](https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees) | Platform transaction charges are distinct from payment-processing charges. Enumerate applicable fee lines and credits instead of assuming the processor is the only deduction. |

## Practitioner mechanisms to investigate

The existing historical tactics cache was used only to identify failure mechanisms worth checking. The following public threads were reopened, but their authors' results remain unverified self-reports. No rates, targets or effect sizes are imported.

- [Agency growth and capacity discussion](https://www.reddit.com/r/agency/comments/1902pxa/1_agency_killer_too_much_growth/): reported overload after rapid growth motivates measuring delivery hours, rework and step costs. It does not establish an appropriate universal growth ceiling.
- [Ecommerce cost and tariff discussion](https://www.reddit.com/r/ecommerce/comments/1kb3vs3/how_are_you_folks_handling_the_massive_tarrifs/): reported inventory purchases consuming cash and incomplete shipping-cost effects motivate separating landed replacement cost, current quotes and payment timing. The reported margins are not verified comparables or price recommendations.

## Public skill comparison

[Corey Haines' pricing skill](https://github.com/coreyhaines31/marketingskills/blob/main/skills/pricing/SKILL.md), [MIT license](https://github.com/coreyhaines31/marketingskills/blob/main/LICENSE), was inspected for scope. It emphasizes SaaS price points, packaging and willingness-to-pay research. This skill addresses a different decision: reconciling one fulfilled offer's costs, refunds, acquisition and capacity at a supplied price. No text, code, examples or benchmark rules were copied. No license from a directory listing was assumed to cover a source repository.

The practical advantage is a reproducible bridge from records to contribution, explicit profit/cash/capacity boundaries, and decision reversal tests. Whether the skill improves a model's recommendations requires independent matched evaluations; this source review does not establish uplift.
