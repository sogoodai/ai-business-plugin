import copy
import csv
import hashlib
import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

SCRIPT = Path(__file__).with_name("reconcile_ledger.py")
EXAMPLE = SCRIPT.parent.parent / "examples" / "ledger"
SPEC = importlib.util.spec_from_file_location("reconcile_ledger", SCRIPT)
ledger = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ledger)


class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.orders = self.read(EXAMPLE / "orders.csv")
        self.entries = self.read(EXAMPLE / "ledger.csv")

    @staticmethod
    def read(path):
        with path.open(newline="", encoding="utf-8") as stream:
            return list(csv.DictReader(stream))

    def write(self, name, rows, fields):
        path = self.directory / name
        with path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        return path

    def run_case(self, orders=None, entries=None, **kwargs):
        order_path = self.write(
            "orders.csv", self.orders if orders is None else orders, ledger.ORDER_FIELDS
        )
        ledger_path = self.write(
            "ledger.csv",
            self.entries if entries is None else entries,
            ledger.LEDGER_FIELDS,
        )
        return ledger.reconcile(
            order_path,
            ledger_path,
            **{
                "offer_id": "PROMO",
                "currency": "USD",
                "start": "2026-10-01",
                "end": "2026-11-01",
                "through": "2026-11-15",
                **kwargs,
            },
        )

    def assert_rejected(self, result, fragment):
        self.assertEqual(result["status"], "rejected")
        self.assertNotIn("totals", result)
        self.assertTrue(
            any(fragment in row["reason"] for row in result["audit"]["rejected_rows"]),
            result,
        )

    def test_independent_four_order_gold_and_audit(self):
        result = self.run_case()
        self.assertEqual(result["status"], "reconciled")
        self.assertEqual(
            result["counts"],
            {
                "orders": 4,
                "fulfilled_units": "5.5",
                "returned_units": "1.5",
                "kept_units": "4",
                "kept_orders": 2,
                "fully_revenue_refunded_orders": 1,
                "partially_revenue_refunded_orders": 1,
            },
        )
        expected = {
            "ORD-A": "35.00",
            "ORD-B": "-27.50",
            "ORD-C": "7.70",
            "ORD-D": "14.00",
        }
        self.assertEqual(
            {
                row["order_id"]: row["actual_variable_contribution_after_acquisition"]
                for row in result["per_order_bridge"]
            },
            expected,
        )
        self.assertEqual(
            result["actual_variable_contribution_after_acquisition"], "29.20"
        )
        totals = result["totals"]
        self.assertEqual(totals["net_revenue_excluding_tax"], "147.00")
        self.assertEqual(totals["net_tax_pass_through"], "29.40")
        self.assertEqual(totals["retained_payment_fees"], "6.80")
        self.assertEqual(totals["inventory_recovery"], "18.00")
        self.assertEqual(
            result["averages"],
            {
                "contribution_per_placed_fulfilled_order": "7.300000",
                "cohort_contribution_allocated_per_kept_order": "14.600000",
                "kept_orders_own_contribution_total": "49.000000",
            },
        )
        self.assertEqual(result["audit"]["accepted_ledger_rows"], 31)
        source = result["audit"]["sources"][0]
        self.assertEqual(
            source["sha256"],
            hashlib.sha256(Path(source["path"]).read_bytes()).hexdigest(),
        )
        self.assertEqual(result["per_order_bridge"][0]["evidence"]["order"]["line"], 2)
        self.assertEqual(result["audit"]["rejected_rows"], [])

    def test_independent_signed_cashless_ledger_identity(self):
        result = self.run_case()
        revenue = sum(
            (
                Decimal(row["item_revenue"]) + Decimal(row["shipping_revenue"])
                for row in self.orders
            ),
            Decimal(0),
        )
        subtract = {
            "inventory_cost",
            "delivery_cost",
            "payment_fee",
            "acquisition_cost",
            "return_cost",
            "item_refund",
            "shipping_refund",
        }
        add = {"fee_credit", "inventory_recovery"}
        expected = revenue + sum(
            (
                Decimal(row["amount"])
                * (-1 if row["kind"] in subtract else 1 if row["kind"] in add else 0)
                for row in self.entries
            ),
            Decimal(0),
        )
        self.assertEqual(
            Decimal(result["actual_variable_contribution_after_acquisition"]), expected
        )
        self.assertEqual(
            sum(
                (
                    Decimal(row["actual_variable_contribution_after_acquisition"])
                    for row in result["per_order_bridge"]
                ),
                Decimal(0),
            ),
            expected,
        )

    def test_row_order_does_not_change_economics(self):
        base = self.run_case()
        random.Random(51).shuffle(self.orders)
        random.Random(71).shuffle(self.entries)
        reordered = self.run_case()
        for field in (
            "totals",
            "counts",
            "averages",
            "actual_variable_contribution_after_acquisition",
        ):
            self.assertEqual(base[field], reordered[field])
        self.assertEqual(
            [row["money"] for row in base["per_order_bridge"]],
            [row["money"] for row in reordered["per_order_bridge"]],
        )

    def test_tax_changes_do_not_change_contribution(self):
        base = self.run_case()
        self.orders[0]["tax_collected"] = "999.00"
        changed = self.run_case()
        self.assertEqual(
            base["actual_variable_contribution_after_acquisition"],
            changed["actual_variable_contribution_after_acquisition"],
        )
        self.assertNotEqual(
            base["totals"]["net_tax_pass_through"],
            changed["totals"]["net_tax_pass_through"],
        )

    def test_splitting_cost_preserves_reconciliation(self):
        base = self.run_case()
        split = copy.deepcopy(self.entries[0])
        split["entry_id"] += "-second"
        split["amount"] = "19.99"
        self.entries[0]["amount"] = "10.01"
        changed = self.run_case(entries=self.entries + [split])
        self.assertEqual(base["totals"], changed["totals"])

    def test_known_cost_increase_decreases_contribution_exactly(self):
        base = self.run_case()
        self.entries[1]["amount"] = "8.23"
        changed = self.run_case()
        self.assertEqual(
            Decimal(base["actual_variable_contribution_after_acquisition"])
            - Decimal(changed["actual_variable_contribution_after_acquisition"]),
            Decimal("1.23"),
        )

    def test_unknown_and_missing_coverage_are_subtotals(self):
        self.entries[1]["amount"] = "unknown"
        result = self.run_case()
        self.assertEqual(result["status"], "scoped_subtotal")
        self.assertIsNone(result["actual_variable_contribution_after_acquisition"])
        self.assertEqual(
            result["totals"]["subtotal_after_known_variable_costs"], "36.20"
        )
        self.assertIn("A-delivery", str(result["unknowns"]))
        missing = self.run_case(
            entries=[row for row in self.entries if row["kind"] != "acquisition_cost"]
        )
        self.assertEqual(missing["status"], "scoped_subtotal")
        self.assertIn(
            "missing explicit acquisition_cost coverage", str(missing["unknowns"])
        )

    def test_incomplete_assertion_blocks_contribution(self):
        self.orders[0]["costs_complete"] = "false"
        result = self.run_case()
        self.assertEqual(result["status"], "scoped_subtotal")
        self.assertIsNone(result["averages"]["contribution_per_placed_fulfilled_order"])
        self.assertEqual(
            result["totals"]["subtotal_after_known_variable_costs"], "29.20"
        )

    def test_duplicate_ids_rejected(self):
        self.assert_rejected(
            self.run_case(orders=self.orders + [self.orders[0]]), "duplicate order"
        )
        self.assert_rejected(
            self.run_case(entries=self.entries + [self.entries[0]]), "duplicate ledger"
        )

    def test_overlapping_and_excess_refunds_rejected(self):
        duplicate = copy.deepcopy(self.entries[10])
        duplicate["entry_id"] = "different-entry-same-refund"
        duplicate["amount"] = "1.00"
        self.assert_rejected(
            self.run_case(entries=self.entries + [duplicate]), "overlapping refund"
        )
        duplicate["reference_id"] = "new-refund"
        self.assert_rejected(
            self.run_case(entries=self.entries + [duplicate]),
            "exceeds original item_revenue",
        )

    def test_fee_credits_sign_and_reference_bounds(self):
        for value, fragment in (
            ("-0.50", "nonnegative"),
            ("2.01", "exceed"),
            ("unknown", "nonnegative"),
        ):
            with self.subTest(value=value):
                changed = copy.deepcopy(self.entries)
                changed[12]["amount"] = value
                self.assert_rejected(self.run_case(entries=changed), fragment)
        changed = copy.deepcopy(self.entries)
        changed[12]["reference_id"] = "A-fee"
        self.assert_rejected(self.run_case(entries=changed), "this order")
        duplicate = copy.deepcopy(self.entries[12])
        duplicate.update(entry_id="B-second-fee-credit", amount="1.51")
        self.assert_rejected(
            self.run_case(entries=self.entries + [duplicate]), "combined credits"
        )

    def test_inventory_recovery_is_not_unbounded_refund_credit(self):
        changed = copy.deepcopy(self.entries)
        changed[14]["amount"] = "20.01"
        self.assert_rejected(
            self.run_case(entries=changed), "combined credits/recovery"
        )
        self.assert_rejected(
            self.run_case(
                entries=[row for row in self.entries if row["entry_id"] != "B-return"]
            ),
            "physical returned_units",
        )
        changed = copy.deepcopy(self.entries)
        changed[13]["units"] = "1.01"
        self.assert_rejected(self.run_case(entries=changed), "returned units exceed")

    def test_wrong_scope_currency_dates_and_unknown_kinds_rejected(self):
        for field, value, fragment in (
            ("offer_id", "OTHER", "selected offer"),
            ("currency", "EUR", "currency"),
            ("ordered_at", "2026-11-01", "outside"),
            ("item_revenue", "unknown", "nonnegative"),
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.orders)
                changed[0][field] = value
                self.assert_rejected(self.run_case(orders=changed), fragment)
        for field, value, fragment in (
            ("occurred_at", "2026-11-16", "cutoff"),
            ("occurred_at", "2026-09-30", "predates"),
            ("currency", "EUR", "currency"),
            ("kind", "refund_net_total", "unmapped"),
            ("order_id", "ORPHAN", "matching"),
        ):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.entries)
                changed[0][field] = value
                result = self.run_case(entries=changed)
                self.assert_rejected(result, fragment)
                if field == "kind":
                    self.assertEqual(len(result["audit"]["unmapped_rows"]), 1)

    def test_fractional_units_and_currency_precision(self):
        self.orders[0]["units"] = "2.125"
        result = self.run_case()
        self.assertEqual(result["counts"]["fulfilled_units"], "5.625")
        self.assertEqual(result["counts"]["kept_units"], "4.125")
        self.entries[0]["amount"] = "30.001"
        self.assert_rejected(self.run_case(), "sub-minor-unit")
        precise = self.run_case(minor_unit=3)
        self.assertEqual(
            precise["actual_variable_contribution_after_acquisition"], "29.199"
        )

    def test_full_refund_does_not_imply_physical_return(self):
        entries = [
            row
            for row in self.entries
            if row["entry_id"] not in {"B-return", "B-recovery"}
        ]
        result = self.run_case(entries=entries)
        self.assertEqual(result["counts"]["kept_orders"], 2)
        self.assertEqual(result["counts"]["kept_units"], "5")
        self.assertEqual(result["totals"]["retained_payment_fees"], "6.80")

    def test_no_kept_orders_has_no_survivor_denominator(self):
        result = self.run_case(
            orders=[row for row in self.orders if row["order_id"] == "ORD-B"],
            entries=[row for row in self.entries if row["order_id"] == "ORD-B"],
        )
        self.assertEqual(result["status"], "reconciled")
        self.assertEqual(result["counts"]["kept_orders"], 0)
        self.assertIsNone(
            result["averages"]["cohort_contribution_allocated_per_kept_order"]
        )
        self.assertEqual(
            result["actual_variable_contribution_after_acquisition"], "-27.50"
        )

    def test_csv_structure_rejections_and_blank_line_evidence(self):
        self.run_case()
        order_path = self.directory / "orders.csv"
        ledger_path = self.directory / "ledger.csv"
        original = ledger_path.read_text()
        prefix, rest = original.split("\n", 1)
        parameters = {
            "offer_id": "PROMO",
            "currency": "USD",
            "start": "2026-10-01",
            "end": "2026-11-01",
            "through": "2026-11-15",
        }
        ledger_path.write_text(prefix + "\n\n" + rest)
        blank = ledger.reconcile(order_path, ledger_path, **parameters)
        self.assertEqual(blank["status"], "reconciled")
        self.assertEqual(
            blank["per_order_bridge"][0]["evidence"]["ledger"][0]["line"], 6
        )
        ledger_path.write_text(
            original.replace("entry_id,order_id", "entry_id,entry_id", 1)
        )
        malformed = ledger.reconcile(order_path, ledger_path, **parameters)
        self.assert_rejected(malformed, "unique columns")
        ledger_path.write_text(original + "extra,wrong,width\n")
        wrong_width = ledger.reconcile(order_path, ledger_path, **parameters)
        self.assert_rejected(wrong_width, "row width")
        self.assertEqual(wrong_width["audit"]["rejected_rows"][0]["line"], 33)

    def test_empty_orders_rejected_and_empty_ledger_is_incomplete(self):
        self.assert_rejected(self.run_case(orders=[]), "no orders")
        result = self.run_case(entries=[])
        self.assertEqual(result["status"], "scoped_subtotal")
        self.assertIsNone(result["actual_variable_contribution_after_acquisition"])
        self.assertEqual(len(result["unknowns"]), 4)

    def test_unknown_cost_fixture_matches_scoped_contract(self):
        result = self.run_case(entries=self.read(EXAMPLE / "ledger-unknown-cost.csv"))
        self.assertEqual(result["status"], "scoped_subtotal")
        self.assertEqual(
            result["totals"]["subtotal_after_known_variable_costs"], "36.20"
        )
        self.assertIsNone(result["actual_variable_contribution_after_acquisition"])

    def test_two_thousand_order_batch_has_exact_linear_totals(self):
        orders, entries = [], []
        for index in range(500):
            suffix = f"-{index}"
            for original in self.orders:
                row = original.copy()
                row["order_id"] += suffix
                orders.append(row)
            for original in self.entries:
                row = original.copy()
                row["order_id"] += suffix
                row["entry_id"] += suffix
                if row["reference_id"]:
                    row["reference_id"] += suffix
                entries.append(row)
        result = self.run_case(orders=orders, entries=entries)
        self.assertEqual(result["status"], "reconciled")
        self.assertEqual(result["counts"]["orders"], 2000)
        self.assertEqual(result["counts"]["kept_units"], "2000")
        self.assertEqual(
            result["actual_variable_contribution_after_acquisition"], "14600.00"
        )

    def test_cli_help_and_exit_contract(self):
        help_run = subprocess.run(
            [sys.executable, SCRIPT, "--help"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(help_run.returncode, 0)
        self.assertIn("--through", help_run.stdout)
        command = [
            sys.executable,
            SCRIPT,
            EXAMPLE / "orders.csv",
            EXAMPLE / "ledger.csv",
            "--offer",
            "PROMO",
            "--currency",
            "USD",
            "--start",
            "2026-10-01",
            "--end",
            "2026-11-01",
            "--through",
            "2026-11-15",
        ]
        success = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(
            json.loads(success.stdout)[
                "actual_variable_contribution_after_acquisition"
            ],
            "29.20",
        )
        command[command.index("PROMO")] = "WRONG"
        failure = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(failure.returncode, 2)
        self.assertEqual(json.loads(failure.stdout)["status"], "rejected")
        self.assertEqual(failure.stderr, "")


if __name__ == "__main__":
    unittest.main()
