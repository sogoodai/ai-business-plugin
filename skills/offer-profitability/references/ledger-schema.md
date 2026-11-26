# Actual order reconciliation, version 1

Use `scripts/reconcile_ledger.py` for a supplied batch of recorded one-time, fully fulfilled orders. It joins two local CSV files, validates every row, and returns an auditable variable-contribution bridge. It does not estimate demand, infer missing costs, calculate LTV, or prove profit or available cash.

```sh
python3 scripts/reconcile_ledger.py examples/ledger/orders.csv examples/ledger/ledger.csv \
  --offer PROMO --currency USD --start 2026-10-01 --end 2026-11-01 --through 2026-11-15
```

Run from this skill's directory. `--help` describes the stable CLI. Python standard library only. Reads files and prints JSON; no network, writes or account access. Save stdout outside the repository if a saved result is needed.

## Normalize existing records, not a questionnaire

The two CSVs below are an explicit normalization contract, not a claim to import an arbitrary provider's native export. Read the actual supplied headers and row semantics first. Aggregate SKU lines to their original order only after verifying the join and line-total semantics. Preserve original transaction IDs as `entry_id` and refund event IDs as `reference_id`. A repeated refund total on several item rows is one event, not several refunds. Original item/shipping/tax amounts must be **before refunds**, already after discounts. Never feed an export's refund-adjusted sales total and also subtract its refund records.

Map amounts from invoices, fee records, delivery/time records and acquisition reports where available. Put landed inventory at cost, variable fulfillment/shipping/paid labor/support in delivery, and allocated cohort acquisition expense in acquisition. Allocation is supplied evidence, not proof of incremental acquisition. Keep a mapping note with the original filenames/hashes, exact source columns, allocation basis, excluded records and source-versus-normalized row/amount controls. The script hashes the normalized files it actually reads, not unseen originals. Unknown provider columns or unexplained control differences require investigation before a complete result is claimed. Do not guess a mapping or ask the owner to manually fill every field when files already contain it.

Supply only the selected offer and currency. All orders must be fully fulfilled; units can be fractional for measured goods. Pre-fulfillment cancellations, exchanges, chargebacks, mixed offers, subscriptions and ongoing obligations need a different reconciliation. A fulfilled subset is not the entire offer cohort if excluded orders incurred losses. Do not hide those losses by dropping their rows. Dates use the same explicitly chosen accounting timezone, normalized to `YYYY-MM-DD`.

`--start` is inclusive and `--end` exclusive for placed orders. `--through` is an inclusive adjustment cutoff, at least the final cohort date. Every event must fall between its order date and the cutoff. The cutoff asserts that all relevant events through that date were included. It does not establish refund maturity or include later refunds. Scope mismatches are rejected, never silently filtered. Use a later cutoff once more outcomes are recorded, and retain the earlier snapshot separately.

## Orders CSV

Exactly these headers, in any order. UTF-8, optional BOM, ordinary CSV quoting. One row per order. No customer names, email addresses or payment details are needed.

```csv
order_id,offer_id,ordered_at,currency,units,item_revenue,shipping_revenue,tax_collected,costs_complete
```

| Column | Contract |
|---|---|
| `order_id` | Unique, stable source order ID. Never use one row per SKU here. |
| `offer_id` | Exact `--offer` identifier. One actual basket/offer scope. |
| `ordered_at` | Placed-order date in `[start, end)`. |
| `currency` | Exact uppercase three-letter `--currency` label. No conversion. |
| `units` | Positive fulfilled quantity, including all bundle/gift units under one consistent unit definition. Fractional quantities allowed. Order count is still one. |
| `item_revenue` | Original actual item/service total after discounts, before refunds, excluding shipping and collected tax. |
| `shipping_revenue` | Original customer-paid shipping excluding tax, before refunds. Explicit zero if none. |
| `tax_collected` | Original pass-through collected tax. Not revenue. Explicit zero if none. |
| `costs_complete` | `true` only when all relevant variable costs for this order and its recorded adjustments through the cutoff have been covered. `false` means incomplete, even if every named bucket has a value. This is a source assertion, not a fact the script can verify. |

## Cost and event CSV

Exactly these headers. A unique `entry_id` for each source line, including explicit zero or unknown coverage records.

```csv
entry_id,order_id,occurred_at,currency,kind,amount,units,reference_id
```

`order_id` must join an accepted order. `occurred_at` is the recognition/event date for that order's variable contribution, not an earlier inventory purchase or later bank payout date. `currency` must match. Amounts are recorded line totals, never unit prices, percentages or quantities to multiply again. The allowed kinds determine their sign. Negative numbers are invalid, including negative refunds or fee credits.

Every order needs explicit coverage for **all five cost kinds** below. Multiple source lines per kind are allowed. A zero row confirms that the category is known to be zero for this scope. The literal `unknown` is allowed only for these cost kinds. A missing category or any unknown amount produces a subtotal with unknowns, never complete contribution.

| Kind | Meaning | `reference_id` | `units` |
|---|---|---|---|
| `inventory_cost` | Original landed cost of fulfilled goods, including gifts. Zero for a service without inventory. | Empty | `0` |
| `delivery_cost` | Original variable fulfillment, merchant-paid shipping, paid labor and support. Do not put return extras here too. | Empty | `0` |
| `payment_fee` | Original processor/marketplace fees. Positive expense; no assumed fee schedule. | Empty | `0` |
| `acquisition_cost` | Actual acquisition expense attributed/allocated to this order, including later-refunded orders. Allocation must reconcile to the supplied cohort spend. | Empty | `0` |
| `return_cost` | Additional recorded return labels, handling, refund fees and other variable return expense. Explicit zero if none through cutoff. | Empty | `0` |
| `item_refund` | Positive refunded item/service money, excluding tax. | Stable source refund event ID | `0` |
| `shipping_refund` | Positive refunded shipping money, excluding tax. | Stable source refund event ID | `0` |
| `tax_refund` | Positive refunded pass-through tax. Excluded from contribution. | Stable source refund event ID | `0` |
| `fee_credit` | Positive actual credit of an original payment fee. Separate from customer refund money. | Original `payment_fee` entry ID on the same order | `0` |
| `returned_units` | Physically returned fulfilled quantity. Amount must be `0`. A monetary refund does not imply a return. | Stable physical-return event ID | Positive quantity |
| `inventory_recovery` | Positive recoverable inventory value at original cost. Not retail resale value, cash, or customer refund money. Requires physical returned units. | Original `inventory_cost` entry ID on the same order | `0` |

A refund event may have one item, one shipping and one tax row. Duplicate `(order_id, kind, reference_id)` refund/physical-return events are rejected even with different entry IDs. If a native refund has several item lines, aggregate them once into its item-refund component and preserve the underlying mapping evidence. Refund components may not cumulatively exceed their matching original revenue/tax amount. Multiple fee credits or inventory recoveries against one original line may not cumulatively exceed it. An unknown original cannot validate a credit/recovery cap. Returned quantity may not exceed fulfilled quantity. Unmapped kinds, orphan joins, duplicate order/entry IDs and wrong scope/date/currency are rejected.

These checks cannot discover the same source transaction deliberately assigned different IDs below the caps. They cannot verify that a returned mixed basket's recovery valuation is correct. Preserve source identifiers and validate the normalization controls.

All numeric fields use nonnegative ordinary decimals, no symbols, thousands separators, exponent notation or missing values. Required original money and refund/credit amounts cannot be unknown. Zero is explicit. The default monetary precision is two decimal places; set `--minor-unit 0`, `3` or `4` only when supported by the recorded currency. There is no currency precision lookup. Sub-minor-unit line totals are rejected instead of silently rounded. Fractional units are preserved independently, up to twelve decimal places. Aggregates use Decimal and are exact at the declared minor unit. Only divided averages are rounded, to six decimals with half-even rounding.

## Read the result

- `status: reconciled` means the supplied rows pass validation and their variable-cost coverage is asserted complete. `actual_variable_contribution_after_acquisition` is available. It does not independently verify source completeness.
- `status: scoped_subtotal` means validated records exist but variable cost coverage is incomplete. Actual contribution and complete-contribution averages are `null`. `unknowns` identifies affected orders/entries. `totals.subtotal_after_known_variable_costs` subtracts only known expenses; it is not the completed contribution or a loss verdict. Known fee/cost subtotals can also omit unknown amounts.
- `status: rejected` returns source/line/field/reason/raw-row evidence in `audit.rejected_rows`, plus `audit.unmapped_rows` for kind errors. No monetary totals are returned. Exit code `2`; successes and scoped subtotals exit `0`. CLI argument errors use argparse's stderr and exit `2`.
- `audit.sources` contains filename, byte count and SHA-256 of each supplied file. Success adds accepted row counts. `per_order_bridge` contains every order's counts, monetary components, completeness, contribution or null, and source rows with line numbers. Totals sum those bridges.

The bridge is:

```text
net revenue = original item + original shipping - item refunds - shipping refunds
retained payment fees = original fees - fee credits
variable contribution = net revenue - original inventory - delivery - return cost
                        - retained payment fees - acquisition + inventory recovery
```

Tax is reported separately as net pass-through. Original fulfillment and fees stay charged even after a full refund; only explicit credits and recovery reverse their respective amounts. Inventory recovery affects contribution without becoming a cash receipt.

`counts.orders` counts these placed, fully fulfilled orders. `fulfilled_units` sums their quantities. `kept_units = fulfilled_units - returned_units` measures physical retention, not money retained. `kept_orders` have no item/shipping refund, so any partial revenue refund removes an order from that denominator; a tax-only correction does not. Fully/partially revenue-refunded order counts are separate. A full refund without a physical return leaves kept units unchanged. `averages.kept_orders_own_contribution_total` is the no-revenue-refund orders' own contribution. `cohort_contribution_allocated_per_kept_order` allocates the entire cohort result across that denominator; it is not each survivor's margin. It is null when there are no kept orders.

This is recorded variable contribution for the stated scope. Fixed overhead, unpaid owner time, financing, settlement timing and any missing obligations remain outside it. It does not establish operating profit, cash balance, causal lift, future sales, or LTV. Use the separate scenario calculator only for explicitly supplied future assumptions; do not turn this actual cohort into a forecast automatically.

## What the tool adds

The useful edge is a deterministic join and accounting control over many source rows: every order stays visible, unknowns block a complete total, refunds cannot overlap silently, retained fees and recovered inventory remain separate, and quantities never become order denominators. Row order cannot change the result. Source hashes and line evidence make a challenged number traceable. This is reproducible reconciliation, not a claim that a model cannot do small-batch arithmetic.

The [synthetic fixtures](../examples/ledger/README.md) have independently stated gold totals. The tests include independent signed-ledger reconciliation, row-order and cost-split invariance, exact cost-change effects, fractional units, currency precision, failure cases and a 2,000-order / 15,500-entry batch.
