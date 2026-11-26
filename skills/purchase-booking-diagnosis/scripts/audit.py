#!/usr/bin/env python3
"""Audit supplied journey evidence. Does not fetch URLs or verify source contents."""

import argparse
import json
import re
import sys
from datetime import datetime, timedelta
from itertools import pairwise
from pathlib import Path


class InvalidEvidence(ValueError):
    pass


def require(condition, path, message):
    if not condition:
        raise InvalidEvidence(f"{path}: {message}")


def obj(value, path):
    require(isinstance(value, dict), path, "expected object")
    return value


def string(value, path):
    require(
        isinstance(value, str) and bool(value.strip()), path, "expected nonempty string"
    )
    return value


def items(value, path):
    require(isinstance(value, list), path, "expected array")
    return value


def count(value, path, unknown=False):
    if unknown and value is None:
        return
    require(type(value) is int and value >= 0, path, "expected nonnegative integer")


def choice(value, choices, path):
    require(value in choices, path, f"expected one of {', '.join(choices)}")


def boolean(value, path):
    require(type(value) is bool, path, "expected boolean")


def timestamp(value, path):
    string(value, path)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidEvidence(f"{path}: expected ISO timestamp") from exc
    require(parsed.tzinfo is not None, path, "timezone offset required")
    return parsed


def indexed(rows, path):
    result = {}
    for i, row in enumerate(items(rows, path)):
        loc = f"{path}[{i}]"
        obj(row, loc)
        key = string(row.get("id"), f"{loc}.id")
        require(key not in result, loc, "duplicate id")
        result[key] = row
    return result


def evidence(value, path, sources, required=True, backend=False):
    refs = items(value, path)
    require(not required or bool(refs), path, "at least one source required")
    for ref in refs:
        string(ref, path)
        require(ref in sources, path, f"unknown source {ref}")
    require(len(refs) == len(set(refs)), path, "duplicate source id")
    if backend:
        require(
            any(sources[ref]["kind"] == "backend" for ref in refs),
            path,
            "persisted-record claim requires a backend source",
        )


def validate(data):
    obj(data, "root")
    require(
        type(data.get("schema_version")) is int and data["schema_version"] == 1,
        "schema_version",
        "expected 1",
    )
    journey = obj(data.get("journey"), "journey")
    string(journey.get("id"), "journey.id")
    choice(journey.get("kind"), ("purchase", "booking"), "journey.kind")
    string(journey.get("expected_outcome"), "journey.expected_outcome")
    sources = indexed(data.get("sources", []), "sources")
    for key, source in sources.items():
        loc = f"sources.{key}"
        choice(
            source.get("kind"),
            ("browser", "event_export", "backend", "cost_record", "other"),
            f"{loc}.kind",
        )
        timestamp(source.get("captured_at"), f"{loc}.captured_at")
        string(source.get("locator"), f"{loc}.locator")
    scopes = indexed(data.get("scopes", []), "scopes")
    for key, scope in scopes.items():
        loc = f"scopes.{key}"
        start = timestamp(scope.get("start"), f"{loc}.start")
        end = timestamp(scope.get("end"), f"{loc}.end")
        require(start < end, loc, "start must precede end")
        for field in ("timezone", "population", "identity", "source", "device", "path"):
            string(scope.get(field), f"{loc}.{field}")
        choice(
            scope.get("unit"), ("user", "session", "attempt", "event"), f"{loc}.unit"
        )
        choice(
            scope.get("counting"),
            ("unique_per_step", "raw", "unknown"),
            f"{loc}.counting",
        )
        choice(
            scope.get("sequence"),
            ("ordered", "unordered", "unknown"),
            f"{loc}.sequence",
        )
        choice(scope.get("entry"), ("closed", "open", "unknown"), f"{loc}.entry")
        choice(
            scope.get("maturity"),
            ("mature", "right_censored", "unknown"),
            f"{loc}.maturity",
        )
        count(
            scope.get("completion_window_seconds"), f"{loc}.completion_window_seconds"
        )
        string(scope.get("deduplication"), f"{loc}.deduplication")
    funnels = indexed(data.get("funnels", []), "funnels")
    for key, funnel in funnels.items():
        loc = f"funnels.{key}"
        steps = items(funnel.get("steps"), f"{loc}.steps")
        require(len(steps) >= 2, loc, "at least two steps required")
        names = set()
        for i, step in enumerate(steps):
            path = f"{loc}.steps[{i}]"
            obj(step, path)
            name = string(step.get("name"), f"{path}.name")
            require(name not in names, path, "duplicate step name")
            names.add(name)
            count(step.get("count"), f"{path}.count", unknown=True)
            string(step.get("scope_id"), f"{path}.scope_id")
            require(step["scope_id"] in scopes, path, "unknown scope_id")
            evidence(step.get("evidence_ids"), f"{path}.evidence_ids", sources)
    observations = indexed(data.get("observations", []), "observations")
    for key, observation in observations.items():
        loc = f"observations.{key}"
        for field in ("title", "expected", "actual"):
            string(observation.get(field), f"{loc}.{field}")
        steps = items(observation.get("steps"), f"{loc}.steps")
        require(bool(steps), loc, "replay steps required")
        for step in steps:
            string(step, f"{loc}.steps")
        env = obj(observation.get("environment"), f"{loc}.environment")
        for field in ("url", "device", "browser", "path"):
            string(env.get(field), f"{loc}.environment.{field}")
        boolean(observation.get("reproduced"), f"{loc}.reproduced")
        choice(
            observation.get("result", "unknown"),
            ("pass", "fail", "unknown"),
            f"{loc}.result",
        )
        evidence(observation.get("evidence_ids"), f"{loc}.evidence_ids", sources)
        if observation["reproduced"]:
            require(
                any(
                    sources[ref]["kind"] == "browser"
                    for ref in observation["evidence_ids"]
                ),
                loc,
                "reproduced observation requires a browser source",
            )
        if "outcome" not in observation:
            continue
        outcome = obj(observation["outcome"], f"{loc}.outcome")
        choice(
            outcome.get("ui"), ("success", "failure", "unknown"), f"{loc}.outcome.ui"
        )
        choice(
            outcome.get("persisted_record"),
            ("present", "absent", "unchecked"),
            f"{loc}.outcome.persisted_record",
        )
        if "http_status" in outcome:
            count(outcome["http_status"], f"{loc}.outcome.http_status")
            require(100 <= outcome["http_status"] <= 599, loc, "invalid HTTP status")
        known = outcome["persisted_record"] != "unchecked"
        evidence(
            outcome.get("verification_evidence_ids", []),
            f"{loc}.outcome.verification_evidence_ids",
            sources,
            required=known,
            backend=known,
        )
        if "verification" in outcome:
            verification = obj(outcome["verification"], f"{loc}.outcome.verification")
            string(verification.get("query"), f"{loc}.outcome.verification.query")
            boolean(verification.get("settled"), f"{loc}.outcome.verification.settled")
            boolean(
                verification.get("matched_test_identity"),
                f"{loc}.outcome.verification.matched_test_identity",
            )
    hypotheses = indexed(data.get("hypotheses", []), "hypotheses")
    for key, hypothesis in hypotheses.items():
        for field in ("claim", "test"):
            string(hypothesis.get(field), f"hypotheses.{key}.{field}")
        evidence(
            hypothesis.get("evidence_ids", []),
            f"hypotheses.{key}.evidence_ids",
            sources,
            required=False,
        )
    for i, economic in enumerate(items(data.get("economics", []), "economics")):
        loc = f"economics[{i}]"
        obj(economic, loc)
        string(economic.get("scope_id"), f"{loc}.scope_id")
        require(economic["scope_id"] in scopes, loc, "unknown scope_id")
        require(
            isinstance(economic.get("currency"), str)
            and re.fullmatch(r"[A-Z]{3}", economic["currency"]) is not None,
            loc,
            "currency must be a three-letter uppercase code",
        )
        for field in ("cost", "realized_value"):
            if field not in economic:
                continue
            part = obj(economic[field], f"{loc}.{field}")
            amount = part.get("amount")
            signed = field == "realized_value" and part.get("basis") == "contribution"
            require(
                type(amount) in (int, float)
                and -float("inf") < amount < float("inf")
                and (signed or amount >= 0),
                f"{loc}.{field}.amount",
                "expected finite amount; only contribution may be negative",
            )
            evidence(part.get("evidence_ids"), f"{loc}.{field}.evidence_ids", sources)
            if field == "cost":
                choice(
                    part.get("basis"),
                    ("media_spend", "total_cost"),
                    f"{loc}.{field}.basis",
                )
            else:
                choice(
                    part.get("basis"),
                    ("gross_revenue", "contribution"),
                    f"{loc}.{field}.basis",
                )
        if "verified_outcomes" in economic:
            part = obj(economic["verified_outcomes"], f"{loc}.verified_outcomes")
            count(part.get("count"), f"{loc}.verified_outcomes.count")
            evidence(
                part.get("evidence_ids"),
                f"{loc}.verified_outcomes.evidence_ids",
                sources,
                backend=True,
            )
    return sources, scopes, funnels, observations, hypotheses


def finding(key, classification, summary, refs, action, verification):
    return {
        "id": key,
        "classification": classification,
        "summary": summary,
        "evidence_ids": list(dict.fromkeys(refs)),
        "action": action,
        "verification": verification,
    }


def capture_covers_window(scope, refs, sources, completion=True):
    boundary = timestamp(scope["end"], "scope.end")
    if completion:
        boundary += timedelta(seconds=scope["completion_window_seconds"])
    return any(
        timestamp(sources[ref]["captured_at"], "source.captured_at") >= boundary
        for ref in refs
    )


def funnel_blockers(funnel, scopes, sources):
    steps = funnel["steps"]
    scope_ids = {step["scope_id"] for step in steps}
    if len(scope_ids) != 1:
        return ["mixed_scope_ids"], None
    scope = scopes[steps[0]["scope_id"]]
    blockers = []
    for field, expected in (
        ("counting", "unique_per_step"),
        ("sequence", "ordered"),
        ("entry", "closed"),
        ("maturity", "mature"),
    ):
        if scope[field] != expected:
            blockers.append(f"{field}:{scope[field]}")
    if scope["unit"] == "event":
        blockers.append("raw_event_unit")
    if any(
        not capture_covers_window(
            scope, step["evidence_ids"], sources, completion=i > 0
        )
        for i, step in enumerate(steps)
    ):
        blockers.append("source_capture_precedes_required_followup")
    counts = [step["count"] for step in steps]
    if None in counts:
        blockers.append("unknown_count")
    elif any(b > a for a, b in pairwise(counts)):
        blockers.append("increasing_counts_in_closed_funnel")
    return blockers, scope


def audit(data):
    try:
        sources, scopes, funnels, observations, hypotheses = validate(data)
    except InvalidEvidence as exc:
        return {
            "status": "invalid_evidence",
            "errors": [str(exc)],
            "metrics": [],
            "findings": [],
        }
    findings, metrics, blocked, outcome_checks, economic_metrics = [], [], [], [], []
    if not observations and not funnels:
        findings.append(
            finding(
                "journey:evidence",
                "missing_instrumentation",
                "No replay observations or funnel evidence supplied.",
                [],
                "Replay the reported transition and capture its expected and actual result.",
                "Correlate the test with an authoritative saved outcome when submission is reached.",
            )
        )
    for key, funnel in funnels.items():
        blockers, scope = funnel_blockers(funnel, scopes, sources)
        refs = sorted({ref for step in funnel["steps"] for ref in step["evidence_ids"]})
        if blockers:
            blocked.append({"funnel_id": key, "reasons": blockers})
            findings.append(
                finding(
                    key,
                    "missing_instrumentation",
                    "Funnel rates withheld: " + ", ".join(blockers),
                    refs,
                    "Re-export one cohort with a single identity, path, time window and deduplication rule.",
                    "Reconcile step membership, order and observation maturity before dividing counts.",
                )
            )
            continue
        for previous, following in pairwise(funnel["steps"]):
            denominator, numerator = previous["count"], following["count"]
            metric = {
                "funnel_id": key,
                "scope_id": scope["id"],
                "from": previous["name"],
                "to": following["name"],
                "numerator": numerator,
                "denominator": denominator,
                "rate": numerator / denominator if denominator else None,
                "did_not_progress": denominator - numerator,
                "meaning": "observed cohort progression, not proven failure or causal loss",
                "small_denominator": denominator < 100,
            }
            metrics.append(metric)
            if denominator > numerator:
                findings.append(
                    finding(
                        f"{key}:{previous['name']}->{following['name']}",
                        "funnel_symptom",
                        f"{denominator - numerator} {scope['unit']} entities did not progress within the supplied window.",
                        refs,
                        "Replay this transition in the affected source, device and checkout path.",
                        "Confirm persisted outcomes and event delivery separately; measure the same cohort after repair.",
                    )
                )
    for key, observation in observations.items():
        refs = observation["evidence_ids"]
        failed = observation.get("result") == "fail"
        outcome = observation.get("outcome")
        false_success = False
        if outcome:
            check = outcome.get("verification", {})
            verified = (
                outcome["persisted_record"] != "unchecked"
                and check.get("settled") is True
                and check.get("matched_test_identity") is True
            )
            pending = (
                not verified
                and check.get("settled") is False
                and check.get("matched_test_identity") is True
                and any(
                    sources[ref]["kind"] == "backend"
                    for ref in outcome.get("verification_evidence_ids", [])
                )
            )
            state = (
                f"verified_{outcome['persisted_record']}"
                if verified
                else ("pending_verification" if pending else "unverified")
            )
            outcome_checks.append(
                {
                    "observation_id": key,
                    "status": state,
                    "evidence_ids": outcome.get("verification_evidence_ids", []),
                }
            )
            false_success = (
                verified
                and outcome["persisted_record"] == "absent"
                and outcome["ui"] == "success"
            )
            if not verified and not pending:
                findings.append(
                    finding(
                        f"{key}:outcome",
                        "missing_instrumentation",
                        "Order or booking persistence has not been verified for this test identity after settlement.",
                        refs + outcome.get("verification_evidence_ids", []),
                        "Read the authoritative order or booking record with the test identifier after its agreed processing bound.",
                        "Check status, amount or slot, quantity and identity. A success page or HTTP 2xx is insufficient.",
                    )
                )
        if failed or false_success:
            classification = (
                "observed_reproducible_defect"
                if observation["reproduced"]
                else "unverified_hypothesis"
            )
            summary = (
                "Success signal without a persisted order or booking."
                if false_success
                else observation["title"]
            )
            findings.append(
                finding(
                    key,
                    classification,
                    summary,
                    refs
                    + (outcome.get("verification_evidence_ids", []) if outcome else []),
                    "Repair the demonstrated transition; preserve other checkout and wallet paths.",
                    "Repeat the supplied steps and a working adjacent path; verify saved outcome and analytics once each.",
                )
            )
    for key, hypothesis in hypotheses.items():
        findings.append(
            finding(
                key,
                "unverified_hypothesis",
                hypothesis["claim"],
                hypothesis.get("evidence_ids", []),
                hypothesis["test"],
                "State what result would disprove this explanation before testing.",
            )
        )
    for economic in data.get("economics", []):
        scope = scopes[economic["scope_id"]]
        result = {
            "scope_id": scope["id"],
            "currency": economic["currency"],
            "meaning": "descriptive supplied-scope economics, not incrementality or recoverable revenue",
        }
        cost, value = economic.get("cost"), economic.get("realized_value")
        outcomes = economic.get("verified_outcomes")
        if scope["maturity"] != "mature":
            result["withheld"] = "outcomes have incomplete or unknown follow-up"
        elif any(
            not capture_covers_window(scope, part["evidence_ids"], sources)
            for part in (value, outcomes)
            if part
        ):
            result["withheld"] = "source capture precedes required outcome follow-up"
        else:
            if cost and outcomes:
                result["cost_per_verified_outcome"] = (
                    cost["amount"] / outcomes["count"] if outcomes["count"] else None
                )
            if cost and value:
                label = (
                    "reported_roas"
                    if cost["basis"] == "media_spend"
                    and value["basis"] == "gross_revenue"
                    else "realized_value_to_cost_ratio"
                )
                result[label] = (
                    value["amount"] / cost["amount"] if cost["amount"] else None
                )
            if not cost:
                result["withheld"] = "actual cost not supplied"
        economic_metrics.append(result)
    priority = {
        "observed_reproducible_defect": 0,
        "missing_instrumentation": 1,
        "funnel_symptom": 2,
        "unverified_hypothesis": 3,
    }
    findings.sort(key=lambda row: priority[row["classification"]])
    return {
        "status": "audited_supplied_evidence",
        "journey_id": data["journey"]["id"],
        "metrics": metrics,
        "blocked_funnels": blocked,
        "outcome_checks": outcome_checks,
        "economics": economic_metrics,
        "findings": findings,
        "limits": [
            "Source contents, browser actions and cohort membership were not independently verified by this script.",
            "A small_denominator flag (n < 100) is a review prompt, not a significance test or traffic requirement.",
            "No causal loss, recovery forecast, benchmark uplift or repair success is inferred.",
        ],
    }


def reject_constant(value):
    raise ValueError(f"nonfinite JSON constant {value}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input", nargs="?", default="-", help="JSON file, or - for stdin"
    )
    args = parser.parse_args()
    try:
        raw = (
            sys.stdin.read()
            if args.input == "-"
            else Path(args.input).read_text(encoding="utf-8")
        )
        result = audit(json.loads(raw, parse_constant=reject_constant))
    except (OSError, ValueError) as exc:
        result = {
            "status": "invalid_evidence",
            "errors": [str(exc)],
            "metrics": [],
            "findings": [],
        }
    print(json.dumps(result, indent=2, allow_nan=False))
    return 2 if result["status"] == "invalid_evidence" else 0


if __name__ == "__main__":
    sys.exit(main())
