import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "journey_audit", ROOT / "scripts" / "audit.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class EvidenceAuditTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "fixtures" / "synthetic.json").read_text())

    def run_audit(self):
        result = MODULE.audit(self.data)
        self.assertEqual(result["status"], "audited_supplied_evidence", result)
        return result

    def classes(self, result):
        return [item["classification"] for item in result["findings"]]

    def test_mature_label_cannot_override_impossible_capture_time(self):
        scope = self.data["scopes"][0]
        scope.update(
            start="2026-11-16T09:00:00Z",
            end="2026-11-16T10:00:00Z",
            completion_window_seconds=86400,
        )
        result = self.run_audit()
        self.assertEqual(result["metrics"], [])
        self.assertIn(
            "source_capture_precedes_required_followup",
            result["blocked_funnels"][0]["reasons"],
        )

    def test_entry_count_can_be_captured_before_outcome_window_closes(self):
        scope = self.data["scopes"][0]
        scope.update(
            start="2026-11-15T09:00:00Z",
            end="2026-11-15T10:00:00Z",
            completion_window_seconds=86400,
        )
        entry = self.data["sources"][2]
        entry["captured_at"] = "2026-11-15T10:00:00Z"
        result = self.run_audit()
        self.assertEqual(result["metrics"][0]["rate"], 0.2)

    def test_valid_cohort_and_false_success_are_distinct_evidence(self):
        result = self.run_audit()
        metric = result["metrics"][0]
        self.assertEqual(
            (metric["numerator"], metric["denominator"], metric["rate"]), (4, 20, 0.2)
        )
        self.assertEqual(metric["did_not_progress"], 16)
        self.assertTrue(metric["small_denominator"])
        self.assertIn("observed_reproducible_defect", self.classes(result))
        self.assertIn("funnel_symptom", self.classes(result))
        self.assertEqual(result["outcome_checks"][0]["status"], "verified_absent")

    def test_http_200_and_thank_you_without_record_access_are_unknown(self):
        observation = self.data["observations"][0]
        observation["result"] = "unknown"
        observation["outcome"] = {
            "ui": "success",
            "http_status": 200,
            "persisted_record": "unchecked",
        }
        result = self.run_audit()
        self.assertNotIn("observed_reproducible_defect", self.classes(result))
        self.assertIn("missing_instrumentation", self.classes(result))
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")

    def test_declined_payment_negative_test_is_not_false_success(self):
        observation = self.data["observations"][0]
        observation["result"] = "pass"
        observation["outcome"]["ui"] = "failure"
        result = self.run_audit()
        self.assertNotIn("observed_reproducible_defect", self.classes(result))

    def test_record_absence_before_settlement_is_not_proved_failure(self):
        observation = self.data["observations"][0]
        observation["result"] = "unknown"
        observation["outcome"]["verification"]["settled"] = False
        result = self.run_audit()
        self.assertNotIn("observed_reproducible_defect", self.classes(result))
        self.assertEqual(result["outcome_checks"][0]["status"], "pending_verification")
        self.assertNotIn("missing_instrumentation", self.classes(result))

    def test_wrong_record_identity_is_not_verified(self):
        observation = self.data["observations"][0]
        observation["result"] = "unknown"
        observation["outcome"]["verification"]["matched_test_identity"] = False
        result = self.run_audit()
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")

    def test_passing_replay_with_saved_record_has_no_defect(self):
        self.data["observations"][0]["result"] = "pass"
        self.data["observations"][0]["outcome"]["persisted_record"] = "present"
        result = self.run_audit()
        self.assertNotIn("observed_reproducible_defect", self.classes(result))
        self.assertEqual(result["outcome_checks"][0]["status"], "verified_present")

    def test_unreproduced_report_remains_hypothesis(self):
        self.data["observations"][0]["reproduced"] = False
        result = self.run_audit()
        self.assertNotIn("observed_reproducible_defect", self.classes(result))
        self.assertIn("unverified_hypothesis", self.classes(result))

    def test_no_observations_or_funnels_is_an_evidence_gap(self):
        self.data.pop("observations")
        self.data.pop("funnels")
        result = self.run_audit()
        self.assertIn("missing_instrumentation", self.classes(result))
        self.assertEqual(result["metrics"], [])

    def test_browser_check_cannot_stand_in_for_pending_backend_lookup(self):
        observation = self.data["observations"][0]
        observation["result"] = "unknown"
        observation["outcome"]["persisted_record"] = "unchecked"
        observation["outcome"]["verification"]["settled"] = False
        observation["outcome"]["verification_evidence_ids"] = ["replay"]
        result = self.run_audit()
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")

    def test_combined_sources_are_not_duplicated_in_findings(self):
        self.data["observations"][0]["evidence_ids"].append("records")
        result = self.run_audit()
        defect = next(
            finding
            for finding in result["findings"]
            if finding["classification"] == "observed_reproducible_defect"
        )
        self.assertEqual(defect["evidence_ids"], ["replay", "records"])

    def test_mixed_denominators_are_not_divided(self):
        changed = copy.deepcopy(self.data["scopes"][0])
        changed.update(id="other", unit="user", source="organic-search")
        self.data["scopes"].append(changed)
        self.data["funnels"][0]["steps"][1]["scope_id"] = "other"
        result = self.run_audit()
        self.assertEqual(result["metrics"], [])
        self.assertEqual(result["blocked_funnels"][0]["reasons"], ["mixed_scope_ids"])

    def test_open_raw_unordered_immature_and_event_funnels_are_withheld(self):
        cases = [
            ("entry", "open"),
            ("counting", "raw"),
            ("sequence", "unordered"),
            ("maturity", "right_censored"),
            ("maturity", "unknown"),
            ("unit", "event"),
        ]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                data = copy.deepcopy(self.data)
                data["scopes"][0][field] = value
                result = MODULE.audit(data)
                self.assertEqual(result["metrics"], [])
                self.assertEqual(len(result["blocked_funnels"]), 1)

    def test_duplicate_transport_counts_do_not_produce_over_100_percent(self):
        self.data["funnels"][0]["steps"][1]["count"] = 21
        result = self.run_audit()
        self.assertEqual(result["metrics"], [])
        self.assertIn(
            "increasing_counts_in_closed_funnel",
            result["blocked_funnels"][0]["reasons"],
        )

    def test_unknown_count_does_not_become_zero(self):
        self.data["funnels"][0]["steps"][1]["count"] = None
        result = self.run_audit()
        self.assertEqual(result["metrics"], [])
        self.assertIn("unknown_count", result["blocked_funnels"][0]["reasons"])

    def test_empty_cohort_returns_null_rate(self):
        for step in self.data["funnels"][0]["steps"]:
            step["count"] = 0
        result = self.run_audit()
        self.assertIsNone(result["metrics"][0]["rate"])

    def test_standard_and_express_have_independent_denominators(self):
        scope = copy.deepcopy(self.data["scopes"][0])
        scope.update(id="wallet", path="express-wallet")
        self.data["scopes"].append(scope)
        self.data["funnels"].append(
            {
                "id": "wallet",
                "steps": [
                    {
                        "name": "wallet opened",
                        "count": 8,
                        "scope_id": "wallet",
                        "evidence_ids": ["export"],
                    },
                    {
                        "name": "order saved",
                        "count": 7,
                        "scope_id": "wallet",
                        "evidence_ids": ["records"],
                    },
                ],
            }
        )
        result = self.run_audit()
        self.assertEqual([metric["rate"] for metric in result["metrics"]], [0.2, 0.875])
        self.assertEqual(len(result["metrics"]), 2)

    def add_economics(self):
        self.data["sources"].append(
            {
                "id": "cost",
                "kind": "cost_record",
                "captured_at": "2026-11-16T10:00:00Z",
                "locator": "synthetic://invoice",
            }
        )
        self.data["economics"] = [
            {
                "scope_id": "mobile-standard",
                "currency": "EUR",
                "cost": {
                    "amount": 120,
                    "basis": "media_spend",
                    "evidence_ids": ["cost"],
                },
                "realized_value": {
                    "amount": 400,
                    "basis": "gross_revenue",
                    "evidence_ids": ["records"],
                },
                "verified_outcomes": {"count": 4, "evidence_ids": ["records"]},
            }
        ]

    def test_only_actual_supplied_scope_economics_are_computed(self):
        self.add_economics()
        result = self.run_audit()["economics"][0]
        self.assertEqual(result["cost_per_verified_outcome"], 30)
        self.assertAlmostEqual(result["reported_roas"], 400 / 120)
        self.assertNotIn("lost_revenue", result)
        self.assertNotIn("profit", result)

    def test_contribution_ratio_is_not_named_roas(self):
        self.add_economics()
        self.data["economics"][0]["realized_value"]["basis"] = "contribution"
        result = self.run_audit()["economics"][0]
        self.assertIn("realized_value_to_cost_ratio", result)
        self.assertNotIn("reported_roas", result)

    def test_missing_cost_is_withheld(self):
        self.add_economics()
        del self.data["economics"][0]["cost"]
        result = self.run_audit()["economics"][0]
        self.assertIn("withheld", result)

    def test_negative_realized_contribution_is_preserved(self):
        self.add_economics()
        self.data["economics"][0]["realized_value"].update(
            amount=-60, basis="contribution"
        )
        result = self.run_audit()["economics"][0]
        self.assertEqual(result["realized_value_to_cost_ratio"], -0.5)

    def test_immature_economics_are_withheld(self):
        self.add_economics()
        self.data["scopes"][0]["maturity"] = "right_censored"
        result = self.run_audit()["economics"][0]
        self.assertNotIn("reported_roas", result)
        self.assertNotIn("cost_per_verified_outcome", result)
        self.assertIn("withheld", result)

    def test_zero_cost_and_outcomes_do_not_divide_by_zero(self):
        self.add_economics()
        self.data["economics"][0]["cost"]["amount"] = 0
        self.data["economics"][0]["verified_outcomes"]["count"] = 0
        result = self.run_audit()["economics"][0]
        self.assertIsNone(result["cost_per_verified_outcome"])
        self.assertIsNone(result["reported_roas"])

    def test_provenance_and_invalid_numeric_values_fail_closed(self):
        changes = [
            lambda d: d["funnels"][0]["steps"][0].update(count=True),
            lambda d: d["funnels"][0]["steps"][0].update(evidence_ids=["missing"]),
            lambda d: d["sources"][0].update(captured_at="2026-11-16"),
            lambda d: d["scopes"][0].update(end=d["scopes"][0]["start"]),
            lambda d: d["observations"][0]["outcome"].update(
                verification_evidence_ids=["replay"]
            ),
        ]
        for change in changes:
            with self.subTest(change=change):
                data = copy.deepcopy(self.data)
                change(data)
                result = MODULE.audit(data)
                self.assertEqual(result["status"], "invalid_evidence")
                self.assertEqual(result["metrics"], [])

    def test_nonnumeric_economics_fail_without_traceback(self):
        self.add_economics()
        for amount in (float("nan"), float("inf"), -1, True, "120"):
            with self.subTest(amount=amount):
                self.data["economics"][0]["cost"]["amount"] = amount
                self.assertEqual(MODULE.audit(self.data)["status"], "invalid_evidence")

    def test_cli_file_stdin_and_invalid_json_contract(self):
        command = [sys.executable, str(ROOT / "scripts" / "audit.py")]
        from_file = subprocess.run(
            command + [str(ROOT / "fixtures" / "synthetic.json")],
            capture_output=True,
            text=True,
            check=True,
        )
        from_stdin = subprocess.run(
            command,
            input=json.dumps(self.data),
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(json.loads(from_file.stdout), json.loads(from_stdin.stdout))
        for raw in ("{bad", "null", '{"value":NaN}'):
            with self.subTest(raw=raw):
                failed = subprocess.run(
                    command, input=raw, capture_output=True, text=True, check=False
                )
                self.assertEqual(failed.returncode, 2)
                self.assertEqual(
                    json.loads(failed.stdout)["status"], "invalid_evidence"
                )
                self.assertNotIn("Traceback", failed.stderr)


if __name__ == "__main__":
    unittest.main()
