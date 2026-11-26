---
name: offer-profitability
description: Evaluate one price, discount or ad-funded one-time offer, or reconcile its actual order and cost CSVs. Use delivery costs, refunds, fees, acquisition cost and capacity to compute auditable contribution, identify missing costs and test break-even thresholds. Supports recorded cohorts and conditional proposals, not demand forecasts or subscription lifetime value.
---

# Offer profitability

Answer the owner's decision first: what this offer earns per placed order, what remains after relevant fixed costs, and which unknown could reverse that answer. A low price can be affordable yet a poor use of scarce delivery capacity. Positive contribution can coexist with a cash shortage.

Choose the input mode before loading a reference:

- **Recorded orders and adjustments:** use [the ledger contract](references/ledger-schema.md). When the supplied files match it, run `scripts/reconcile_ledger.py` rather than rewriting its calculations. Use `--help` for the scope arguments. Preserve the source mapping. Redirect its full JSON to an evidence file, then inspect status, counts, totals and unknowns before opening individual bridges. The JSON includes per-order bridges, normalized-source hashes and row-level rejection evidence. Incomplete cost coverage produces a scoped subtotal with unknown contribution. It does not establish profit or settlement.
- **One proposed offer:** use [the calculator contract](references/schema.md) to normalize the actual costs and explicit assumptions, then run:

```sh
python3 scripts/evaluate.py INPUT.json
```

Paths are relative to this skill. The script is standard-library Python, reads one local file, writes JSON to stdout, and changes no accounts. Missing economics produces `missing_data`; invalid inputs produce stderr and exit 2. Synthetic examples: [product](examples/discounted-product.json), [service](examples/fixed-scope-service.json).

Use the relevant CLI contract and example for ordinary execution. Read implementation code only when diagnosing a tool failure or unsupported requirement. Preserve the output and its input evidence so another person can reproduce the conclusion.

## Frame the decision with available evidence

Read supplied invoices, SKU costs, time logs, order/refund exports and ad reports before asking questions. Model one actual basket or fixed service scope, one currency, one acquisition cohort and one delivery/refund period. Ask only for missing facts that could change the recommendation. Do not present the normalized schema as a questionnaire. Derive nonapplicability from explicit facts, such as no shipping for a remote workshop or no processor fee for the stated bank-transfer route, and label that derivation.

Distinguish observed records, current quotes, assumptions and arithmetic derived from them. Attach a source, date, denominator and applicable period. Missing data is an unknown, not zero or proof the offer fails. Check cost coverage before setting `costs_complete: true`.

- Use the actual price after the discount once. Use the complete basket cost for bundles, gifts and buy-one-get-one offers. Marginal discounts can change the SKU mix; do not substitute storewide AOV or gross margin.
- Include landed inventory, fulfillment, merchant-paid outbound shipping, variable paid labor, support, marketplace/payment fees and applicable acquisition costs. Separate shipping charged to the buyer. Keep collected tax outside revenue, while including it in fees if the provider charges on it.
- Put unpaid owner time or displaced alternative contribution in opportunity costs. Put existing fixed costs and costs caused by this offer in their separate fields. Never allocate the same payroll, creative fee or shipping loss twice.
- CAC must match these placed orders. Spend divided by clicks, leads, all historical customers or only kept orders has a different denominator. Platform-attributed orders do not establish incremental acquisition. Hold expected volume constant when finding a price floor; demand at that price remains unknown.

For a discount go/no-go, positive offer profit does not establish improvement over doing nothing. Compare a supplied same-period baseline, including full-price sales displaced by discounted orders. If incremental demand or cannibalization is unknown, show the conditional economics and the test needed to resolve it.

## Reconcile refunds before judging margin

The calculator charges delivery costs and original fees to every fulfilled placed order, then models mutually exclusive refund outcomes. Subtract refunded item and shipping revenue, add extra return/handling costs, and credit only the fee refunds actually available and recoverable inventory at cost. Returned goods are inventory recovery, not another retail sale or immediate cash. Do not also subtract a generic return reserve.

Use mature outcomes from a comparable cohort. For partial refunds, enter the refunded fraction and the fee credit as separate fractions of their respective original amounts. Confirm the exact account, method and fee schedule; retained processing fees are material. Read [mechanics and decision sources](references/decisions-and-sources.md) when resolving these issues. Pre-fulfillment cancellations, exchanges, chargebacks and ongoing service obligations require separate outcome models; do not force them into a delivered-order calculation.

## Test the inputs that control the answer

Run the base case and plausible adverse cases derived from the owner's evidence. Combine risks when they could occur together. Report sign reversals, break-even CAC/price, and the volume needed to cover fixed costs. A negative allowable CAC means even free acquisition cannot meet that modeled target. A price threshold assumes unchanged costs, mix, refunds and volume; it does not prove customers will pay.

Use capacity only when relevant: available delivery hours or stock/slot limits, expected hours including rework, and any contribution displaced. If a hire, overtime or larger batch is needed, model its actual cost and new capacity as a separate case. Do not silently cap orders and leave ad spend unchanged, or sell beyond stated capacity.

Keep cash timing separate. If it matters, supply dated receipts and payments, inventory purchases, processor payout delays/holds, tax remittances and refund payments in the optional cash schedule. Label incomplete schedules as partial. Inventory recovery and accounting profit do not fund bills until cash is available.

## Deliver a decision someone can audit

Keep the answer short, with supporting arithmetic available:

- **Verdict:** conditional on which observed inputs or estimates. Separate computable, unresolved, negative contribution, uncovered fixed costs and infeasible capacity.
- **Bridge:** actual collected revenue excluding tax, refund-adjusted revenue, delivery costs, retained fees, return costs/recovery, CAC, contribution per placed order, then included fixed costs and economic surplus. Link source records to the input paths and output arithmetic.
- **Denominators:** distinguish a kept order's own margin from cohort contribution allocated over surviving kept orders. Credit no repeat contribution, LTV or causal sales lift. If repeat evidence matters, show realized net contribution over a stated mature cohort separately.
- **Reversal and next step:** identify the smallest price/cost/CAC/refund change that flips the result. When unknowns control the decision, propose a bounded test with an owner-chosen loss cap: a few delivered orders with time logs, a shipping quote, a mature refund follow-up, or a capped acquisition cohort. Define which measurement would change the decision. Do not invent universal margin targets, return rates or CAC shares.

Recommend preparation or a test within the user's authorization. Calculating an offer does not authorize changing prices, launching ads, contacting customers or publishing it.
