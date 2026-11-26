import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "offer_evaluate", ROOT / "scripts/evaluate.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def example():
    return json.loads((ROOT / "examples/discounted-product.json").read_text())


class EconomicsTests(unittest.TestCase):
    def test_sensitivity_includes_displacement_without_fixed_costs(self):
        data = example()
        data.pop("fixed")
        data.update(price=100, shipping_charged=0, tax_collected=0, cac_per_order=0)
        data["costs"] = [{"name": "Delivery", "amount": 60, "kind": "cash"}]
        data["fees"] = []
        data["refunds"] = []
        data["capacity"] = {"max_orders": 200, "displaced_contribution_per_order": 30}
        data["sensitivity"] = [
            {"name": "Higher delivery cost", "overrides": {"/costs/0/amount": 80}}
        ]
        scenario = MODULE.evaluate(data)["sensitivity"][0]
        self.assertEqual((scenario["baseline"], scenario["scenario"]), (10, -10))
        self.assertTrue(scenario["sign_reversal"])

    def test_full_return_reconciles_two_independent_paths(self):
        result = MODULE.evaluate(example())
        unit = result["per_placed_order"]
        self.assertEqual(unit["original_fees"], Decimal("2.85"))
        self.assertEqual(unit["expected_net_revenue"], Decimal("76.5"))
        self.assertEqual(unit["expected_contribution_after_ads"], Decimal("13.95"))
        self.assertEqual(
            result["period"]["modeled_operating_result_before_tax"], Decimal(395)
        )
        self.assertEqual(result["period"]["operating_break_even"]["orders"], 72)
        kept = Decimal(85) - Decimal(36) - Decimal("2.85") - Decimal(25)
        returned = (
            -Decimal(36) - Decimal("2.85") - Decimal(25) - Decimal(7) + Decimal(20)
        )
        self.assertEqual(
            Decimal("0.9") * kept + Decimal("0.1") * returned,
            unit["expected_contribution_after_ads"],
        )
        self.assertEqual(
            unit["cohort_contribution_allocated_per_kept_order"], Decimal("15.5")
        )
        self.assertEqual(result["sensitivity"][0]["scenario"], Decimal(-105))
        self.assertTrue(result["sensitivity"][0]["sign_reversal"])

    def test_multiple_exclusive_outcomes_and_distinct_fee_bases(self):
        data = example()
        data["tax_collected"] = 10
        data["fees"].append(
            {"name": "Marketplace", "rate": 0.1, "fixed": 0, "base": "items"}
        )
        data["fees"][0]["base"] = "charge"
        data["refunds"] = [
            {
                "name": "Partial",
                "probability": 0.2,
                "item_refund_fraction": 0.5,
                "shipping_refund_fraction": 0,
                "fee_credit_fractions": {"Processor": 0, "Marketplace": 0.5},
                "extra_cost": 0,
                "inventory_recovery": 0,
            },
            {
                "name": "Full",
                "probability": 0.1,
                "item_refund_fraction": 1,
                "shipping_refund_fraction": 1,
                "fee_credit_fractions": {"Processor": 0, "Marketplace": 1},
                "extra_cost": 7,
                "inventory_recovery": 20,
            },
        ]
        data.pop("sensitivity")
        unit = MODULE.evaluate(data)["per_placed_order"]
        self.assertEqual(unit["original_fees"], Decimal("11.15"))
        self.assertEqual(unit["expected_fee_credits"], Decimal("1.6"))
        self.assertEqual(unit["expected_refunded_revenue"], Decimal("16.5"))
        self.assertEqual(unit["expected_contribution_after_ads"], Decimal("-0.75"))
        self.assertEqual(unit["kept_order_probability"], Decimal("0.7"))

    def test_all_refunded_has_no_kept_denominator_or_price_solution(self):
        data = example()
        data["refunds"][0]["probability"] = 1
        data.pop("sensitivity")
        result = MODULE.evaluate(data)
        self.assertIsNone(
            result["per_placed_order"]["cohort_contribution_allocated_per_kept_order"]
        )
        self.assertEqual(
            result["thresholds"]["unit_economic_break_even_price"]["status"],
            "higher_price_does_not_improve_result",
        )
        self.assertIsNone(result["period"]["economic_break_even"]["orders"])

    def test_break_even_price_is_actual_boundary(self):
        data = example()
        result = MODULE.evaluate(data)
        threshold = result["thresholds"]["period_economic_break_even_price"][
            "minimum_price"
        ]
        data.pop("sensitivity")
        data["price"] = threshold + Decimal("0.01")
        self.assertGreater(
            MODULE.evaluate(data)["period"]["modeled_operating_result_before_tax"], 0
        )
        data["price"] = threshold - Decimal("0.01")
        self.assertLess(
            MODULE.evaluate(data)["period"]["modeled_operating_result_before_tax"], 0
        )

    def test_capacity_and_owner_time_are_separate_from_operating_profit(self):
        data = json.loads((ROOT / "examples/fixed-scope-service.json").read_text())
        result = MODULE.evaluate(data)
        self.assertEqual(result["capacity"]["max_orders"], 8)
        self.assertEqual(result["assessment"], "requested_volume_exceeds_capacity")
        self.assertEqual(
            result["period"]["modeled_operating_result_before_tax"], Decimal(3300)
        )
        self.assertEqual(
            result["period"]["economic_surplus_after_opportunity_and_displacement"],
            Decimal(1300),
        )
        self.assertEqual(
            result["cash"]["funding_gap_on_supplied_schedule"], Decimal(900)
        )
        self.assertFalse(result["cash"]["liquidity_assessed"])
        self.assertEqual(
            result["sensitivity"][0]["capacity"]["status"], "within_supplied_limit"
        )

    def test_zero_orders_and_zero_unit_margin(self):
        data = example()
        data.pop("sensitivity")
        data["orders"] = 0
        result = MODULE.evaluate(data)
        self.assertEqual(result["period"]["modeled_operating_result_before_tax"], -1000)
        self.assertNotIn(
            "allowable_cac_to_cover_fixed_and_opportunity", result["thresholds"]
        )
        data["cac_per_order"] = MODULE.evaluate(data)["per_placed_order"][
            "expected_contribution_before_ads"
        ]
        result = MODULE.evaluate(data)
        self.assertIsNone(result["period"]["operating_break_even"]["orders"])
        data["fixed"] = {"period": 0, "incremental": 0}
        result = MODULE.evaluate(data)
        self.assertEqual(
            result["period"]["operating_break_even"]["status"],
            "zero_result_at_any_volume",
        )

    def test_missing_is_not_zero_and_optional_is_unassessed(self):
        data = example()
        del data["cac_per_order"]
        result = MODULE.evaluate(data)
        self.assertEqual(result["status"], "missing_data")
        self.assertIn("/cac_per_order", result["missing_data"])
        self.assertNotIn("per_placed_order", result)
        data = example()
        data.pop("fixed")
        data.pop("capacity")
        data.pop("sensitivity")
        result = MODULE.evaluate(data)
        self.assertEqual(result["period"]["status"], "not_assessed")
        self.assertEqual(result["capacity"]["status"], "not_assessed")
        data["costs_complete"] = False
        self.assertEqual(MODULE.evaluate(data)["status"], "missing_data")

    def test_invalid_economics_and_malformed_inputs_are_rejected(self):
        mutations = [
            lambda d: d.update(price=True),
            lambda d: d.update(price=float("nan")),
            lambda d: d.update(price=-1),
            lambda d: d.update(orders=1.5),
            lambda d: d.update(cac_per_order="25"),
            lambda d: d.update(prcie=1),
            lambda d: d["refunds"][0].update(probability=1.01),
            lambda d: d["refunds"][0].update(inventory_recovery=26),
            lambda d: d["refunds"][0]["fee_credit_fractions"].update(Processor=1.1),
            lambda d: d["fees"].append(copy.deepcopy(d["fees"][0])),
            lambda d: d.update(
                capacity={
                    "available_hours": 1,
                    "hours_per_order": 0,
                    "displaced_contribution_per_order": 0,
                }
            ),
            lambda d: d.update(
                sensitivity=[{"name": "Bad", "overrides": {"/unknown": 2}}]
            ),
        ]
        for mutate in mutations:
            data = example()
            mutate(data)
            with self.subTest(data=data), self.assertRaises(MODULE.InputError):
                MODULE.evaluate(data)

    def test_joint_outcomes_cannot_double_count_probability(self):
        data = example()
        second = copy.deepcopy(data["refunds"][0])
        second.update(name="Other", probability=0.95)
        data["refunds"].append(second)
        with self.assertRaises(MODULE.InputError):
            MODULE.evaluate(data)

    def test_same_day_cash_events_are_netted_before_liquidity_test(self):
        data = example()
        data["cash"] = {
            "starting_cash": 10,
            "complete": True,
            "events": [
                {"day": 0, "label": "Out", "amount": -100},
                {"day": 0, "label": "In", "amount": 100},
            ],
        }
        cash = MODULE.evaluate(data)["cash"]
        self.assertEqual(cash["funding_gap_on_supplied_schedule"], 0)
        self.assertEqual(cash["minimum_balance"], 10)

    def test_parent_evidence_labels_cover_numeric_children(self):
        data = example()
        result = MODULE.evaluate(data)
        self.assertEqual(result["evidence"]["unattributed_numeric_inputs"], [])
        data["evidence"] = {"/costs": data["evidence"]["/"]}
        result = MODULE.evaluate(data)
        self.assertIn("/price", result["evidence"]["unattributed_numeric_inputs"])
        self.assertNotIn(
            "/costs/0/amount", result["evidence"]["unattributed_numeric_inputs"]
        )


class CliTests(unittest.TestCase):
    def invoke(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(json.dumps(data))
            return subprocess.run(
                [sys.executable, str(ROOT / "scripts/evaluate.py"), str(path)],
                capture_output=True,
                text=True,
                check=False,
            )

    def test_valid_cli_emits_only_json(self):
        process = self.invoke(example())
        self.assertEqual(process.returncode, 0)
        self.assertEqual(process.stderr, "")
        self.assertEqual(
            json.loads(process.stdout)["per_placed_order"][
                "expected_contribution_after_ads"
            ],
            13.95,
        )

    def test_invalid_cli_emits_no_json(self):
        data = example()
        data["price"] = -1
        process = self.invoke(data)
        self.assertEqual(process.returncode, 2)
        self.assertEqual(process.stdout, "")
        self.assertIn("/price", process.stderr)

    def test_help(self):
        process = subprocess.run(
            [sys.executable, str(ROOT / "scripts/evaluate.py"), "--help"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(process.returncode, 0)
        self.assertIn("schema_version 1", process.stdout)

    def test_duplicate_json_fields_are_not_silently_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text('{"schema_version": 1, "price": 80, "price": 90}')
            process = subprocess.run(
                [sys.executable, str(ROOT / "scripts/evaluate.py"), str(path)],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(process.returncode, 2)
        self.assertEqual(process.stdout, "")
        self.assertIn("duplicate JSON field: price", process.stderr)


if __name__ == "__main__":
    unittest.main()
