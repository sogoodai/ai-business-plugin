#!/usr/bin/env python3
"""Reconcile normalized fulfilled-order and variable-cost CSVs without dependencies."""

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import defaultdict
from datetime import date, timedelta
from decimal import ROUND_HALF_EVEN, Decimal, InvalidOperation, localcontext
from pathlib import Path

ORDER_FIELDS = (
    "order_id",
    "offer_id",
    "ordered_at",
    "currency",
    "units",
    "item_revenue",
    "shipping_revenue",
    "tax_collected",
    "costs_complete",
)
LEDGER_FIELDS = (
    "entry_id",
    "order_id",
    "occurred_at",
    "currency",
    "kind",
    "amount",
    "units",
    "reference_id",
)
COST_KINDS = frozenset(
    (
        "inventory_cost",
        "delivery_cost",
        "payment_fee",
        "acquisition_cost",
        "return_cost",
    )
)
REFUND_BASES = {
    "item_refund": "item_revenue",
    "shipping_refund": "shipping_revenue",
    "tax_refund": "tax_collected",
}
CREDIT_BASES = {"fee_credit": "payment_fee", "inventory_recovery": "inventory_cost"}
KINDS = COST_KINDS | REFUND_BASES.keys() | CREDIT_BASES.keys() | {"returned_units"}
ZERO = Decimal(0)


class InputError(ValueError):
    def __init__(self, field, reason):
        self.field = field
        super().__init__(reason)


def issue(row, field, reason):
    return {
        "source": row["source"],
        "line": row["line"],
        "field": field,
        "reason": str(reason),
        "row": row["raw"],
    }


def identifier(raw, field):
    value = raw[field]
    if not value or value != value.strip() or any(ord(c) < 32 for c in value):
        raise InputError(
            field, "expected nonempty text without surrounding whitespace or controls"
        )
    return value


def iso_date(value, field):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise InputError(field, "expected YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise InputError(field, "invalid calendar date") from exc


def number(value, field, quantum=None):
    if not re.fullmatch(r"\d{1,18}(?:\.\d{1,12})?", value):
        raise InputError(
            field, "expected a nonnegative decimal without symbols or separators"
        )
    amount = Decimal(value)
    if quantum is not None and amount != amount.quantize(quantum):
        raise InputError(
            field, "amount has sub-minor-unit precision; supply recorded line totals"
        )
    return amount


def read_csv(path, fields, sources, errors):
    name = str(path)
    try:
        contents = path.read_bytes()
    except OSError as exc:
        errors.append(
            {
                "source": name,
                "line": None,
                "field": None,
                "reason": str(exc),
                "row": None,
            }
        )
        return []
    sources.append(
        {
            "path": name,
            "sha256": hashlib.sha256(contents).hexdigest(),
            "bytes": len(contents),
        }
    )
    try:
        reader = csv.reader(
            io.StringIO(contents.decode("utf-8-sig"), newline=""), strict=True
        )
        header = next(reader, None)
        if (
            header is None
            or len(header) != len(set(header))
            or set(header) != set(fields)
        ):
            errors.append(
                {
                    "source": name,
                    "line": 1,
                    "field": "header",
                    "reason": f"expected exactly these unique columns: {','.join(fields)}",
                    "row": header,
                }
            )
            return []
        result = []
        while True:
            line = reader.line_num + 1
            values = next(reader, None)
            if values is None:
                break
            if not values:
                continue
            raw = dict(zip(header, values))
            row = {"source": name, "line": line, "raw": raw}
            if len(values) != len(header):
                row["raw"] = values
                errors.append(issue(row, "columns", "row width differs from header"))
            else:
                result.append(row)
        return result
    except (UnicodeError, csv.Error) as exc:
        errors.append(
            {
                "source": name,
                "line": None,
                "field": None,
                "reason": str(exc),
                "row": None,
            }
        )
        return []


def parse_orders(rows, scope, quantum, errors):
    orders = {}
    for row in rows:
        raw = row["raw"]
        try:
            order_id = identifier(raw, "order_id")
            if order_id in orders:
                raise InputError("order_id", "duplicate order ID")
            if identifier(raw, "offer_id") != scope["offer_id"]:
                raise InputError(
                    "offer_id", "order is outside the explicitly selected offer"
                )
            if raw["currency"] != scope["currency"]:
                raise InputError("currency", "mixed or unexpected currency")
            ordered_at = iso_date(raw["ordered_at"], "ordered_at")
            if not scope["start"] <= ordered_at < scope["end"]:
                raise InputError("ordered_at", "order is outside [start, end)")
            units = number(raw["units"], "units")
            if units <= ZERO:
                raise InputError("units", "fulfilled units must be positive")
            if raw["costs_complete"] not in ("true", "false"):
                raise InputError("costs_complete", "expected true or false")
            orders[order_id] = {
                "order_id": order_id,
                "ordered_at": ordered_at,
                "units": units,
                "costs_complete": raw["costs_complete"] == "true",
                "evidence": row,
                **{
                    field: number(raw[field], field, quantum)
                    for field in (
                        "item_revenue",
                        "shipping_revenue",
                        "tax_collected",
                    )
                },
            }
        except InputError as exc:
            errors.append(issue(row, exc.field, exc))
    if not rows:
        errors.append(
            {
                "source": "orders",
                "line": None,
                "field": "orders",
                "reason": "no orders supplied",
                "row": None,
            }
        )
    return orders


def parse_ledger(rows, orders, scope, quantum, errors):
    entries = {}
    references = set()
    for row in rows:
        raw = row["raw"]
        try:
            entry_id = identifier(raw, "entry_id")
            if entry_id in entries:
                raise InputError("entry_id", "duplicate ledger entry ID")
            order_id = identifier(raw, "order_id")
            if order_id not in orders:
                raise InputError(
                    "order_id", "no matching accepted order in the selected cohort"
                )
            if raw["currency"] != scope["currency"]:
                raise InputError("currency", "mixed or unexpected currency")
            occurred_at = iso_date(raw["occurred_at"], "occurred_at")
            if not orders[order_id]["ordered_at"] <= occurred_at <= scope["through"]:
                raise InputError(
                    "occurred_at",
                    "entry predates its order or exceeds the adjustment cutoff",
                )
            kind = raw["kind"]
            if kind not in KINDS:
                raise InputError("kind", "unmapped ledger kind")
            amount = (
                None
                if raw["amount"] == "unknown" and kind in COST_KINDS
                else number(raw["amount"], "amount", quantum)
            )
            units = number(raw["units"], "units")
            if kind == "returned_units":
                if amount != ZERO or units <= ZERO:
                    raise InputError(
                        "units",
                        "returned_units requires positive units and zero amount",
                    )
            elif units != ZERO:
                raise InputError("units", "only returned_units may carry nonzero units")
            reference = raw["reference_id"]
            if kind in REFUND_BASES or kind in CREDIT_BASES or kind == "returned_units":
                reference = identifier(raw, "reference_id")
                if kind in REFUND_BASES or kind == "returned_units":
                    key = (order_id, kind, reference)
                    if key in references:
                        raise InputError(
                            "reference_id", "overlapping refund/return source event"
                        )
                    references.add(key)
            elif reference:
                raise InputError(
                    "reference_id",
                    "cost rows must leave reference_id empty; entry_id identifies the source line",
                )
            if (kind in REFUND_BASES or kind in CREDIT_BASES) and amount <= ZERO:
                raise InputError(
                    "amount",
                    "refunds and credits require positive amounts; kind sets direction",
                )
            entries[entry_id] = {
                "entry_id": entry_id,
                "order_id": order_id,
                "kind": kind,
                "amount": amount,
                "units": units,
                "reference_id": reference,
                "evidence": row,
            }
        except InputError as exc:
            errors.append(issue(row, exc.field, exc))
    return entries


def validate_links(orders, entries, errors):
    grouped = defaultdict(list)
    credits = defaultdict(list)
    for entry in entries.values():
        grouped[entry["order_id"]].append(entry)
        if entry["kind"] in CREDIT_BASES:
            original = entries.get(entry["reference_id"])
            if (
                original is None
                or original["order_id"] != entry["order_id"]
                or original["kind"] != CREDIT_BASES[entry["kind"]]
            ):
                errors.append(
                    issue(
                        entry["evidence"],
                        "reference_id",
                        "credit/recovery must reference an original fee/inventory entry on this order",
                    )
                )
            elif original["amount"] is None:
                errors.append(
                    issue(
                        entry["evidence"],
                        "reference_id",
                        "cannot validate credit/recovery against an unknown original amount",
                    )
                )
            else:
                credits[entry["reference_id"]].append(entry)
    for reference, rows in credits.items():
        if sum((row["amount"] for row in rows), ZERO) > entries[reference]["amount"]:
            errors.append(
                issue(
                    rows[-1]["evidence"],
                    "amount",
                    "combined credits/recovery exceed the referenced original amount",
                )
            )
    for order_id, order in orders.items():
        rows = grouped[order_id]
        for kind, base in REFUND_BASES.items():
            matching = [row for row in rows if row["kind"] == kind]
            if sum((row["amount"] for row in matching), ZERO) > order[base]:
                errors.append(
                    issue(
                        matching[-1]["evidence"],
                        "amount",
                        f"combined {kind} exceeds original {base}",
                    )
                )
        returns = [row for row in rows if row["kind"] == "returned_units"]
        returned_units = sum((row["units"] for row in returns), ZERO)
        if returned_units > order["units"]:
            errors.append(
                issue(
                    returns[-1]["evidence"],
                    "units",
                    "returned units exceed original fulfilled units",
                )
            )
        recoveries = [row for row in rows if row["kind"] == "inventory_recovery"]
        if recoveries and returned_units == ZERO:
            errors.append(
                issue(
                    recoveries[0]["evidence"],
                    "kind",
                    "inventory recovery requires an explicit physical returned_units entry",
                )
            )
    return grouped


def bridge(order, entries):
    amounts = {
        kind: sum(
            (
                row["amount"]
                for row in entries
                if row["kind"] == kind and row["amount"] is not None
            ),
            ZERO,
        )
        for kind in KINDS
        if kind != "returned_units"
    }
    missing = [
        f"missing explicit {kind} coverage"
        for kind in sorted(COST_KINDS)
        if not any(row["kind"] == kind for row in entries)
    ]
    missing.extend(
        f"unknown amount: {row['entry_id']} ({row['kind']})"
        for row in entries
        if row["amount"] is None
    )
    if not order["costs_complete"]:
        missing.append("order variable-cost list is not confirmed complete")
    values = {
        field: order[field]
        for field in ("item_revenue", "shipping_revenue", "tax_collected")
    }
    values.update(amounts)
    values["net_revenue_excluding_tax"] = (
        order["item_revenue"]
        + order["shipping_revenue"]
        - amounts["item_refund"]
        - amounts["shipping_refund"]
    )
    values["net_tax_pass_through"] = order["tax_collected"] - amounts["tax_refund"]
    values["retained_payment_fees"] = amounts["payment_fee"] - amounts["fee_credit"]
    values["subtotal_after_known_variable_costs"] = (
        values["net_revenue_excluding_tax"]
        - sum((amounts[kind] for kind in COST_KINDS), ZERO)
        + amounts["fee_credit"]
        + amounts["inventory_recovery"]
    )
    revenue_refund = amounts["item_refund"] + amounts["shipping_refund"]
    returned_units = sum((row["units"] for row in entries), ZERO)
    return {
        "order_id": order["order_id"],
        "complete": not missing,
        "unknowns": sorted(missing),
        "counts": {
            "orders": 1,
            "fulfilled_units": order["units"],
            "returned_units": returned_units,
            "kept_units": order["units"] - returned_units,
            "kept_orders": int(revenue_refund == ZERO),
            "fully_revenue_refunded_orders": int(
                revenue_refund > ZERO and values["net_revenue_excluding_tax"] == ZERO
            ),
            "partially_revenue_refunded_orders": int(
                revenue_refund > ZERO and values["net_revenue_excluding_tax"] > ZERO
            ),
        },
        "money": values,
        "actual_variable_contribution_after_acquisition": values[
            "subtotal_after_known_variable_costs"
        ]
        if not missing
        else None,
        "evidence": {
            "order": order["evidence"],
            "ledger": [
                row["evidence"]
                for row in sorted(entries, key=lambda row: row["entry_id"])
            ],
        },
    }


def display(value, quantum):
    if isinstance(value, Decimal):
        return format(value.quantize(quantum, rounding=ROUND_HALF_EVEN), "f")
    if isinstance(value, dict):
        return {key: display(item, quantum) for key, item in value.items()}
    if isinstance(value, list):
        return [display(item, quantum) for item in value]
    return value


def reconcile(
    orders_path, ledger_path, *, offer_id, currency, start, end, through, minor_unit=2
):
    if not re.fullmatch(r"[A-Z]{3}", currency):
        raise InputError("currency", "expected a three-letter uppercase currency label")
    if not offer_id or offer_id != offer_id.strip():
        raise InputError("offer_id", "expected a nonempty offer identifier")
    if (
        isinstance(minor_unit, bool)
        or not isinstance(minor_unit, int)
        or minor_unit not in range(5)
    ):
        raise InputError("minor_unit", "expected an integer from 0 to 4")
    scope = {
        "offer_id": offer_id,
        "currency": currency,
        "start": iso_date(start, "start"),
        "end": iso_date(end, "end"),
        "through": iso_date(through, "through"),
    }
    if scope["start"] >= scope["end"] or scope["through"] < scope["end"] - timedelta(
        days=1
    ):
        raise InputError(
            "scope", "require start < end and through >= end minus one day"
        )
    quantum = Decimal(1).scaleb(-minor_unit)
    sources, errors = [], []
    with localcontext() as ctx:
        ctx.prec = 50
        order_rows = read_csv(Path(orders_path), ORDER_FIELDS, sources, errors)
        ledger_rows = read_csv(Path(ledger_path), LEDGER_FIELDS, sources, errors)
        orders = parse_orders(order_rows, scope, quantum, errors)
        entries = parse_ledger(ledger_rows, orders, scope, quantum, errors)
        grouped = validate_links(orders, entries, errors) if not errors else {}
        audit = {
            "sources": sources,
            "unmapped_rows": [
                row for row in errors if row["reason"] == "unmapped ledger kind"
            ],
            "rejected_rows": errors,
        }
        result_scope = {
            "offer_id": offer_id,
            "currency": currency,
            "order_start_inclusive": start,
            "order_end_exclusive": end,
            "adjustments_complete_through_inclusive": through,
            "minor_unit_decimal_places": minor_unit,
            "orders_are_fully_fulfilled": True,
            "basis": "original pre-refund receipts and recorded variable-cost events; not cash settlement",
        }
        if errors:
            return {
                "schema_version": 1,
                "status": "rejected",
                "scope": result_scope,
                "audit": audit,
            }
        rows = [bridge(orders[key], grouped[key]) for key in sorted(orders)]
        complete = all(row["complete"] for row in rows)
        counts = {
            key: sum((row["counts"][key] for row in rows), ZERO)
            for key in rows[0]["counts"]
        }
        counts = {
            key: int(value)
            if key.endswith("orders")
            else format(value.normalize(), "f")
            for key, value in counts.items()
        }
        totals = {
            key: sum((row["money"][key] for row in rows), ZERO)
            for key in rows[0]["money"]
        }
        contribution = (
            totals["subtotal_after_known_variable_costs"] if complete else None
        )
        averages = {
            "contribution_per_placed_fulfilled_order": contribution / len(rows)
            if complete
            else None,
            "cohort_contribution_allocated_per_kept_order": contribution
            / counts["kept_orders"]
            if complete and counts["kept_orders"]
            else None,
            "kept_orders_own_contribution_total": sum(
                (
                    row["actual_variable_contribution_after_acquisition"]
                    for row in rows
                    if row["counts"]["kept_orders"]
                ),
                ZERO,
            )
            if complete
            else None,
        }
        audit.update(
            {
                "accepted_order_rows": len(order_rows),
                "accepted_ledger_rows": len(ledger_rows),
            }
        )
        for row in rows:
            row["counts"] = {
                key: format(value.normalize(), "f")
                if isinstance(value, Decimal)
                else value
                for key, value in row["counts"].items()
            }
        return {
            "schema_version": 1,
            "status": "reconciled" if complete else "scoped_subtotal",
            "scope": result_scope,
            "counts": counts,
            "totals": display(totals, quantum),
            "actual_variable_contribution_after_acquisition": display(
                contribution, quantum
            ),
            "averages": display(averages, Decimal("0.000001")),
            "unknowns": [
                {"order_id": row["order_id"], "items": row["unknowns"]}
                for row in rows
                if row["unknowns"]
            ],
            "per_order_bridge": display(rows, quantum),
            "audit": audit,
            "limits": [
                "Coverage, original pre-refund receipt semantics and cutoff completeness are supplied assertions, not independently verified.",
                "Kept orders have no item/shipping refund. Kept units are fulfilled units minus physical returns, independent of money refunds.",
                "Inventory recovery is recorded recoverable cost, not cash, future revenue or a reversal of the customer's refund.",
                "Variable contribution excludes fixed overhead, owner opportunity cost and settlement timing; this is not profit, available cash, incremental lift, a forecast or LTV.",
            ],
        }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Contract: ../references/ledger-schema.md. Rejects rows outside scope; never silently filters. JSON goes to stdout; no files or accounts are changed.",
    )
    parser.add_argument("orders", type=Path, help="normalized original-order CSV")
    parser.add_argument(
        "ledger", type=Path, help="normalized variable-cost/refund event CSV"
    )
    parser.add_argument(
        "--offer", required=True, help="exact offer_id shared by all orders"
    )
    parser.add_argument(
        "--currency", required=True, help="exact uppercase currency label, e.g. USD"
    )
    parser.add_argument(
        "--start", required=True, help="inclusive placed-order date, YYYY-MM-DD"
    )
    parser.add_argument(
        "--end", required=True, help="exclusive placed-order date, YYYY-MM-DD"
    )
    parser.add_argument(
        "--through",
        required=True,
        help="inclusive date through which all adjustment events were exported",
    )
    parser.add_argument(
        "--minor-unit",
        type=int,
        choices=range(5),
        default=2,
        help="recorded currency decimal places, default 2; no automatic currency lookup or rounding",
    )
    args = parser.parse_args(argv)
    try:
        result = reconcile(
            args.orders,
            args.ledger,
            offer_id=args.offer,
            currency=args.currency,
            start=args.start,
            end=args.end,
            through=args.through,
            minor_unit=args.minor_unit,
        )
    except (InputError, InvalidOperation) as exc:
        print(
            json.dumps(
                {
                    "schema_version": 1,
                    "status": "rejected",
                    "error": str(exc),
                    "field": getattr(exc, "field", None),
                }
            )
        )
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 2 if result["status"] == "rejected" else 0


if __name__ == "__main__":
    sys.exit(main())
