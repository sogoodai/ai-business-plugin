# Synthetic recorded-order fixtures

All IDs, dates and amounts are invented. No customer data or provider fee benchmarks are used. The [contract](../../references/ledger-schema.md) describes the exact normalization; these are not native Shopify or Stripe exports.

From the skill directory:

```sh
python3 scripts/reconcile_ledger.py examples/ledger/orders.csv examples/ledger/ledger.csv \
  --offer PROMO --currency USD --start 2026-10-01 --end 2026-11-01 --through 2026-11-15
```

There are four orders, 5.5 fulfilled units and 31 cost/event rows. All five cost categories have explicit per-order coverage, including zero return costs for A and D.

| Order | Net revenue without tax | Inventory | Delivery | Original fee less credit | Acquisition | Return cost | Inventory recovery | Contribution |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A, no refund | 85.00 | 30.00 | 7.00 | 3.00 | 10.00 | 0.00 | 0.00 | 35.00 |
| B, full refund | 0.00 | 20.00 | 6.00 | 1.50 | 8.00 | 4.00 | 12.00 | -27.50 |
| C, partial refund/return | 32.00 | 18.00 | 5.00 | 1.30 | 4.00 | 2.00 | 6.00 | 7.70 |
| D, no refund | 30.00 | 10.00 | 2.00 | 1.00 | 3.00 | 0.00 | 0.00 | 14.00 |
| Total | 147.00 | 78.00 | 20.00 | 6.80 | 25.00 | 6.00 | 18.00 | **29.20** |

Original revenue is 213.00, item refunds 65.00, shipping refunds 1.00. Original fees are 7.50 and fee credits 0.70. Pass-through tax net of refunds is 29.40 and excluded from contribution. There are two kept orders, one fully revenue-refunded order, one partly revenue-refunded order, 1.5 physically returned units and four kept units. Complete contribution per placed fulfilled order is 7.30. Entire-cohort contribution allocated per kept order is 14.60; those two orders' own combined contribution is 49.00.

Use `ledger-unknown-cost.csv` with the same orders to see incomplete-cost behavior. Only A's delivery amount changes from `7.00` to `unknown`: the result is `scoped_subtotal`, known-cost subtotal 36.20, and actual contribution null. It must not be interpreted as an improvement.

Run the reconciliation checks with:

```sh
python3 -m unittest discover -s scripts -p test_reconcile_ledger.py -v
```

The batch test generates 2,000 synthetic orders and 15,500 cost/event rows in a temporary directory. Its independently expected contribution is 14,600.00. It also checks exact retained units and order counts. No bulk fixture needs to be hand-read or maintained.
