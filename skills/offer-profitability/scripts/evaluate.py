#!/usr/bin/env python3
"""Evaluate one fulfilled, one-time offer. Uses only Python's standard library."""

import argparse
import copy
import json
import sys
from decimal import ROUND_CEILING, Decimal, InvalidOperation
from pathlib import Path

ZERO = Decimal(0)
ONE = Decimal(1)


class InputError(ValueError):
    pass


class Reader:
    def __init__(self):
        self.missing = []

    def required(self, obj, key, path):
        value = obj.get(key)
        if value is None:
            self.missing.append(f"{path}/{key}")
        return value

    def number(self, obj, key, path, *, maximum=None, signed=False, integer=False):
        value = self.required(obj, key, path)
        if value is None:
            return ZERO
        if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
            raise InputError(f"{path}/{key}: expected a JSON number")
        try:
            number = Decimal(str(value))
        except InvalidOperation as exc:
            raise InputError(f"{path}/{key}: invalid number") from exc
        if not number.is_finite():
            raise InputError(f"{path}/{key}: must be finite")
        if not signed and number < 0:
            raise InputError(f"{path}/{key}: must be nonnegative")
        if maximum is not None and number > maximum:
            raise InputError(f"{path}/{key}: must be <= {maximum}")
        if integer and number != number.to_integral_value():
            raise InputError(f"{path}/{key}: must be an integer")
        return number


def object_at(value, path):
    if not isinstance(value, dict):
        raise InputError(f"{path or '/'}: expected an object")
    return value


def keys(obj, allowed, path):
    extra = set(obj) - set(allowed.split())
    if extra:
        raise InputError(f"{path or '/'}: unknown fields: {', '.join(sorted(extra))}")


def text_at(value, path):
    if not isinstance(value, str) or not value.strip():
        raise InputError(f"{path}: expected a nonempty string")
    return value


def rows(reader, data, key):
    value = reader.required(data, key, "")
    if value is None:
        return []
    if not isinstance(value, list):
        raise InputError(f"/{key}: expected an array")
    for i, row in enumerate(value):
        object_at(row, f"/{key}/{i}")
    return value


def named_rows(reader, data, key):
    result = rows(reader, data, key)
    names = []
    for i, row in enumerate(result):
        name = reader.required(row, "name", f"/{key}/{i}")
        if name is not None:
            names.append(text_at(name, f"/{key}/{i}/name"))
    if len(names) != len(set(names)):
        raise InputError(f"/{key}: names must be unique")
    return result


def validate(data):
    object_at(data, "")
    keys(
        data,
        "schema_version offer_name currency period price list_price shipping_charged "
        "tax_collected costs costs_complete fees refunds cac_per_order orders fixed "
        "capacity cash evidence sensitivity",
        "",
    )
    if data.get("schema_version") != 1 or isinstance(data.get("schema_version"), bool):
        raise InputError("/schema_version: expected 1")
    reader = Reader()
    for key in ("offer_name", "currency", "period"):
        value = reader.required(data, key, "")
        if value is not None:
            text_at(value, f"/{key}")
    values = {
        key: reader.number(data, key, "")
        for key in ("price", "shipping_charged", "tax_collected", "cac_per_order")
    }
    values["orders"] = reader.number(data, "orders", "", integer=True)
    if "list_price" in data:
        reader.number(data, "list_price", "")
    complete = reader.required(data, "costs_complete", "")
    if complete is not None and not isinstance(complete, bool):
        raise InputError("/costs_complete: expected a boolean")
    if complete is False:
        reader.missing.append("/costs_complete: cost list not confirmed complete")

    costs = []
    for i, row in enumerate(named_rows(reader, data, "costs")):
        path = f"/costs/{i}"
        keys(row, "name amount kind", path)
        kind = reader.required(row, "kind", path)
        if kind is not None and kind not in ("inventory", "cash", "opportunity"):
            raise InputError(f"{path}/kind: expected inventory, cash or opportunity")
        costs.append({**row, "amount": reader.number(row, "amount", path)})
    inventory = sum((c["amount"] for c in costs if c.get("kind") == "inventory"), ZERO)

    fees = []
    for i, row in enumerate(named_rows(reader, data, "fees")):
        path = f"/fees/{i}"
        keys(row, "name rate fixed base", path)
        base = reader.required(row, "base", path)
        if base is not None and base not in ("items", "revenue", "charge"):
            raise InputError(f"{path}/base: expected items, revenue or charge")
        fees.append(
            {
                **row,
                "rate": reader.number(row, "rate", path, maximum=ONE),
                "fixed": reader.number(row, "fixed", path),
            }
        )

    refunds = []
    for i, row in enumerate(named_rows(reader, data, "refunds")):
        path = f"/refunds/{i}"
        keys(
            row,
            "name probability item_refund_fraction shipping_refund_fraction "
            "fee_credit_fractions extra_cost inventory_recovery",
            path,
        )
        item = dict(row)
        for key in ("probability", "item_refund_fraction", "shipping_refund_fraction"):
            item[key] = reader.number(row, key, path, maximum=ONE)
        for key in ("extra_cost", "inventory_recovery"):
            item[key] = reader.number(row, key, path)
        if item["inventory_recovery"] > inventory and not reader.missing:
            raise InputError(
                f"{path}/inventory_recovery: exceeds original inventory cost"
            )
        credits = reader.required(row, "fee_credit_fractions", path)
        item["fee_credit_fractions"] = {}
        if credits is not None:
            object_at(credits, f"{path}/fee_credit_fractions")
            fee_names = {f.get("name") for f in fees if f.get("name")}
            if set(credits) - fee_names:
                raise InputError(f"{path}/fee_credit_fractions: unknown fee name")
            for name in sorted(fee_names):
                item["fee_credit_fractions"][name] = reader.number(
                    credits, name, f"{path}/fee_credit_fractions", maximum=ONE
                )
        refunds.append(item)
    if sum((r["probability"] for r in refunds), ZERO) > ONE:
        raise InputError("/refunds: mutually exclusive probabilities sum above 1")

    fixed = None
    if data.get("fixed") is not None:
        block = object_at(data["fixed"], "/fixed")
        keys(block, "period incremental", "/fixed")
        fixed = {
            key: reader.number(block, key, "/fixed")
            for key in ("period", "incremental")
        }
    capacity = None
    if data.get("capacity") is not None:
        block = object_at(data["capacity"], "/capacity")
        keys(
            block,
            "max_orders available_hours hours_per_order displaced_contribution_per_order",
            "/capacity",
        )
        capacity = {}
        if "max_orders" not in block and not (
            {"available_hours", "hours_per_order"} & set(block)
        ):
            raise InputError(
                "/capacity: provide max_orders or available_hours and hours_per_order"
            )
        if "max_orders" in block:
            capacity["max_orders"] = reader.number(
                block, "max_orders", "/capacity", integer=True
            )
        if {"available_hours", "hours_per_order"} & set(block):
            for key in ("available_hours", "hours_per_order"):
                capacity[key] = reader.number(block, key, "/capacity")
            if (
                capacity["hours_per_order"] == 0
                and "/capacity/hours_per_order" not in reader.missing
            ):
                raise InputError("/capacity/hours_per_order: must be positive")
        capacity["displaced_contribution_per_order"] = reader.number(
            block, "displaced_contribution_per_order", "/capacity"
        )

    cash = None
    if data.get("cash") is not None:
        block = object_at(data["cash"], "/cash")
        keys(block, "starting_cash complete events", "/cash")
        cash = {
            "starting_cash": reader.number(block, "starting_cash", "/cash", signed=True)
        }
        cash["complete"] = reader.required(block, "complete", "/cash")
        if cash["complete"] is not None and not isinstance(cash["complete"], bool):
            raise InputError("/cash/complete: expected a boolean")
        events = reader.required(block, "events", "/cash")
        if events is not None and not isinstance(events, list):
            raise InputError("/cash/events: expected an array")
        cash["events"] = []
        for i, row in enumerate(events or []):
            path = f"/cash/events/{i}"
            object_at(row, path)
            keys(row, "day label amount", path)
            label = reader.required(row, "label", path)
            if label is not None:
                text_at(label, f"{path}/label")
            cash["events"].append(
                {
                    "day": reader.number(row, "day", path, integer=True),
                    "amount": reader.number(row, "amount", path, signed=True),
                    "label": label,
                }
            )
    evidence = data.get("evidence", {})
    object_at(evidence, "/evidence")
    for path, entry in evidence.items():
        if not path.startswith("/"):
            raise InputError("/evidence: keys must be JSON pointers beginning with /")
        object_at(entry, f"/evidence/{path}")
        keys(entry, "status source as_of", f"/evidence/{path}")
        if entry.get("status") not in ("observed", "quoted", "assumed", "derived"):
            raise InputError(
                f"/evidence/{path}/status: expected observed, quoted, assumed or derived"
            )
        for key in ("source", "as_of"):
            text_at(entry.get(key), f"/evidence/{path}/{key}")
    return reader.missing, {
        **values,
        "costs": costs,
        "fees": fees,
        "refunds": refunds,
        "fixed": fixed,
        "capacity": capacity,
        "cash": cash,
    }


def sign(value):
    return "positive" if value > 0 else "negative" if value < 0 else "zero"


def arithmetic(model, price=None):
    price = model["price"] if price is None else price
    revenue = price + model["shipping_charged"]
    bases = {
        "items": price,
        "revenue": revenue,
        "charge": revenue + model["tax_collected"],
    }
    fees = [
        {
            "name": f["name"],
            "base": f["base"],
            "base_amount": bases[f["base"]],
            "original_fee": bases[f["base"]] * f["rate"] + f["fixed"],
        }
        for f in model["fees"]
    ]
    fee_total = sum((f["original_fee"] for f in fees), ZERO)
    outcomes = []
    for r in model["refunds"]:
        refunded_revenue = price * r["item_refund_fraction"] + (
            model["shipping_charged"] * r["shipping_refund_fraction"]
        )
        credit = sum(
            (f["original_fee"] * r["fee_credit_fractions"][f["name"]] for f in fees),
            ZERO,
        )
        loss = refunded_revenue + r["extra_cost"] - r["inventory_recovery"] - credit
        outcomes.append(
            {
                "name": r["name"],
                "probability": r["probability"],
                "refunded_revenue": refunded_revenue,
                "fee_credit": credit,
                "extra_cost": r["extra_cost"],
                "inventory_recovery": r["inventory_recovery"],
                "loss_vs_kept_order": loss,
                "expected_loss": r["probability"] * loss,
            }
        )
    refund_revenue = sum(
        (r["probability"] * r["refunded_revenue"] for r in outcomes), ZERO
    )
    credits = sum((r["probability"] * r["fee_credit"] for r in outcomes), ZERO)
    extra = sum((r["probability"] * r["extra_cost"] for r in outcomes), ZERO)
    recovered = sum(
        (r["probability"] * r["inventory_recovery"] for r in outcomes), ZERO
    )
    costs = sum(
        (c["amount"] for c in model["costs"] if c["kind"] != "opportunity"), ZERO
    )
    opportunity = sum(
        (c["amount"] for c in model["costs"] if c["kind"] == "opportunity"), ZERO
    )
    kept_pre_ad = revenue - costs - fee_total
    pre_ad = kept_pre_ad - sum((r["expected_loss"] for r in outcomes), ZERO)
    kept_probability = ONE - sum((r["probability"] for r in outcomes), ZERO)
    return {
        "collected_revenue_ex_tax": revenue,
        "tax_collected_pass_through": model["tax_collected"],
        "expected_refunded_revenue": refund_revenue,
        "expected_net_revenue": revenue - refund_revenue,
        "original_delivery_cost": costs,
        "original_fees": fee_total,
        "expected_fee_credits": credits,
        "expected_return_cost": extra,
        "expected_inventory_recovery": recovered,
        "expected_contribution_before_ads": pre_ad,
        "cac_per_placed_order": model["cac_per_order"],
        "expected_contribution_after_ads": pre_ad - model["cac_per_order"],
        "opportunity_cost": opportunity,
        "expected_economic_contribution_after_ads": pre_ad
        - model["cac_per_order"]
        - opportunity,
        "kept_order_probability": kept_probability,
        "kept_order_contribution_after_ads": kept_pre_ad - model["cac_per_order"],
        "cohort_contribution_allocated_per_kept_order": (
            (pre_ad - model["cac_per_order"]) / kept_probability
            if kept_probability
            else None
        ),
        "fee_rows": fees,
        "refund_rows": outcomes,
    }


def break_even_orders(fixed, contribution):
    if contribution > 0:
        return {
            "status": "finite",
            "orders": int(
                (fixed / contribution).to_integral_value(rounding=ROUND_CEILING)
            ),
        }
    if contribution == 0 and fixed == 0:
        return {"status": "zero_result_at_any_volume", "orders": 0}
    return {"status": "no_positive_volume_covers_costs", "orders": None}


def price_threshold(slope, intercept):
    if slope <= 0:
        return {
            "status": "higher_price_does_not_improve_result",
            "minimum_price": None,
            "slope": slope,
            "intercept": intercept,
        }
    return {
        "status": "finite",
        "minimum_price": max(ZERO, -intercept / slope),
        "slope": slope,
        "intercept": intercept,
    }


def numeric_paths(value, prefix=""):
    if isinstance(value, dict):
        for key, child in value.items():
            if key not in ("evidence", "sensitivity", "schema_version"):
                escaped = key.replace("~", "~0").replace("/", "~1")
                yield from numeric_paths(child, f"{prefix}/{escaped}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            yield from numeric_paths(child, f"{prefix}/{i}")
    elif not isinstance(value, bool) and isinstance(value, (int, float, Decimal)):
        yield prefix


def evidence_for(path, evidence):
    parts = path.split("/")
    while len(parts) > 1:
        candidate = "/".join(parts)
        if candidate in evidence:
            return evidence[candidate]
        parts.pop()
    return evidence.get("/")


def calculate(data, model):
    unit = arithmetic(model)
    cash_after = unit["expected_contribution_after_ads"]
    economic_after = unit["expected_economic_contribution_after_ads"]
    orders = model["orders"]
    capacity = {"status": "not_assessed", "max_orders": None}
    displaced = ZERO
    if model["capacity"] is not None:
        block = model["capacity"]
        limits = []
        if "max_orders" in block:
            limits.append(int(block["max_orders"]))
        if "available_hours" in block:
            limits.append(int(block["available_hours"] // block["hours_per_order"]))
        limit = min(limits)
        displaced = block["displaced_contribution_per_order"]
        capacity = {
            "status": "exceeded" if orders > limit else "within_supplied_limit",
            "max_orders": limit,
            "requested_orders": int(orders),
            "displaced_contribution_per_order": displaced,
        }
    period = {"status": "not_assessed", "reason": "fixed costs not supplied"}
    thresholds = {
        "allowable_cac_for_unit_contribution": unit["expected_contribution_before_ads"],
        "allowable_cac_after_opportunity_cost": (
            unit["expected_contribution_before_ads"]
            - unit["opportunity_cost"]
            - displaced
        ),
    }
    at_zero = arithmetic(model, ZERO)
    at_one = arithmetic(model, ONE)
    slope = (
        at_one["expected_contribution_after_ads"]
        - at_zero["expected_contribution_after_ads"]
    )
    thresholds["unit_economic_break_even_price"] = price_threshold(
        slope, at_zero["expected_economic_contribution_after_ads"] - displaced
    )
    if model["fixed"] is not None:
        fixed = model["fixed"]["period"] + model["fixed"]["incremental"]
        operating = orders * cash_after - fixed
        economic = orders * (economic_after - displaced) - fixed
        period = {
            "status": "calculated",
            "orders": int(orders),
            "existing_fixed_cost": model["fixed"]["period"],
            "incremental_fixed_cost": model["fixed"]["incremental"],
            "contribution_less_incremental_fixed_cost": (
                orders * cash_after - model["fixed"]["incremental"]
            ),
            "modeled_operating_result_before_tax": operating,
            "economic_surplus_after_opportunity_and_displacement": economic,
            "operating_result_sign": sign(operating),
            "economic_surplus_sign": sign(economic),
            "operating_break_even": break_even_orders(fixed, cash_after),
            "economic_break_even": break_even_orders(fixed, economic_after - displaced),
        }
        if capacity["max_orders"] is not None:
            for key in ("operating_break_even", "economic_break_even"):
                threshold = period[key]["orders"]
                period[key]["fits_capacity"] = (
                    threshold is not None and threshold <= capacity["max_orders"]
                )
        if orders > 0:
            thresholds["allowable_cac_to_cover_fixed_and_opportunity"] = (
                thresholds["allowable_cac_after_opportunity_cost"] - fixed / orders
            )
            thresholds["period_economic_break_even_price"] = price_threshold(
                slope,
                at_zero["expected_economic_contribution_after_ads"]
                - displaced
                - fixed / orders,
            )
    cash = {"status": "not_assessed"}
    if model["cash"] is not None:
        block = model["cash"]
        balance = block["starting_cash"]
        minimum = balance
        minimum_day = 0
        daily = {}
        for event in block["events"]:
            day = int(event["day"])
            daily[day] = daily.get(day, ZERO) + event["amount"]
        timeline = []
        for day, amount in sorted(daily.items()):
            balance += amount
            timeline.append(
                {"day": day, "net_movement": amount, "closing_balance": balance}
            )
            if balance < minimum:
                minimum, minimum_day = balance, day
        cash = {
            "status": "supplied_schedule" if block["complete"] else "partial_schedule",
            "minimum_balance": minimum,
            "minimum_day": minimum_day,
            "funding_gap_on_supplied_schedule": max(ZERO, -minimum),
            "ending_balance": balance,
            "timeline": timeline,
            "liquidity_assessed": block["complete"],
        }
    if economic_after - displaced < 0:
        assessment = "negative_unit_economic_contribution"
    elif capacity["status"] == "exceeded":
        assessment = "requested_volume_exceeds_capacity"
    elif (
        period["status"] == "calculated"
        and period["economic_surplus_sign"] == "negative"
    ):
        assessment = "positive_or_zero_unit_contribution_but_fixed_costs_not_covered"
    elif period["status"] == "not_assessed":
        assessment = "unit_contribution_calculated_profit_not_assessed"
    else:
        assessment = "nonnegative_model_conditional_on_inputs"
    evidence = data.get("evidence", {})
    result = {
        "status": "calculated",
        "assessment": assessment,
        "evidence_status": "conditional_model_not_proof_of_demand_or_incrementality",
        "per_placed_order": unit,
        "period": period,
        "capacity": capacity,
        "cash": cash,
        "thresholds": thresholds,
        "evidence": {
            "provided": evidence,
            "unattributed_numeric_inputs": [
                p for p in numeric_paths(data) if evidence_for(p, evidence) is None
            ],
        },
        "audit": {
            "input": data,
            "equations": {
                "refund_loss": "refunded item + refunded shipping + extra cost - inventory recovery - fee credit",
                "expected_contribution_before_ads": "item price + shipping - original delivery cost - original fees - sum(probability * refund loss)",
                "expected_contribution_after_ads": "expected contribution before ads - CAC per placed order",
                "operating_result": "orders * contribution after ads - existing fixed - incremental fixed",
                "economic_surplus": "operating result - orders * (opportunity cost + displaced contribution)",
                "price_threshold": "result per order = slope * item price + intercept; other inputs held constant",
            },
        },
        "limits": [
            "One fulfilled, one-time offer; no repeat purchase or lifetime value credited.",
            "Taxes collected are pass-through, but can be part of a fee base.",
            "Returned inventory recovery is economic cost recovery, not cash or future retail revenue.",
            "Costs apply to every placed order; pre-fulfillment cancellations need a separate model.",
            "Fixed costs, capacity and cash are assessed only when supplied; included-cost profit is not a full financial statement.",
            "Expected arithmetic uses unrounded fees; provider transaction rounding can differ.",
            "Cash events are independently supplied, not generated or reconciled to the contribution model.",
        ],
    }
    if not any(
        evidence_for(p, evidence) and evidence_for(p, evidence)["status"] == "assumed"
        for p in numeric_paths(data)
    ):
        result["limits"].append(
            "Missing assumption labels do not establish certainty or current verification."
        )
    if "list_price" in data:
        reference = Decimal(str(data["list_price"]))
        result["discount"] = {
            "amount": reference - model["price"],
            "fraction": (reference - model["price"]) / reference if reference else None,
            "already_applied_to_price": True,
        }
    return result


def override(data, pointer, value):
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise InputError("/sensitivity/overrides: expected JSON pointers")
    if pointer not in set(numeric_paths(data)):
        raise InputError(
            f"/sensitivity: {pointer} must target an existing numeric input"
        )
    if pointer.startswith("/cash/"):
        raise InputError(
            "/sensitivity: cash timing cannot be inferred from a profitability scenario"
        )
    parts = [
        part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")
    ]
    target = data
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    if isinstance(target, list):
        target[int(parts[-1])] = value
    else:
        target[parts[-1]] = value


def evaluate(data):
    missing, model = validate(data)
    if missing:
        return {
            "status": "missing_data",
            "missing_data": missing,
            "assessment": "not_computable_from_supplied_inputs",
            "audit": {"input": data},
        }
    result = calculate(data, model)
    scenarios = data.get("sensitivity", [])
    if not isinstance(scenarios, list):
        raise InputError("/sensitivity: expected an array")
    result["sensitivity"] = []
    for i, scenario in enumerate(scenarios):
        path = f"/sensitivity/{i}"
        object_at(scenario, path)
        keys(scenario, "name overrides", path)
        name = text_at(scenario.get("name"), f"{path}/name")
        changes = object_at(scenario.get("overrides"), f"{path}/overrides")
        if not changes:
            raise InputError(f"{path}/overrides: must not be empty")
        variant = copy.deepcopy(data)
        variant.pop("sensitivity", None)
        variant.pop("cash", None)
        for pointer, value in changes.items():
            override(variant, pointer, value)
        gaps, alternative = validate(variant)
        if gaps:
            raise InputError(
                f"{path}: override introduced missing data: {', '.join(gaps)}"
            )
        evaluated = calculate(variant, alternative)
        metric = "economic_surplus_after_opportunity_and_displacement"
        if result["period"]["status"] == "calculated":
            baseline, changed = result["period"][metric], evaluated["period"][metric]
        else:
            metric = "expected_economic_contribution_after_ads"
            baseline, changed = (
                result["per_placed_order"][metric]
                - result["capacity"].get("displaced_contribution_per_order", ZERO),
                evaluated["per_placed_order"][metric]
                - evaluated["capacity"].get("displaced_contribution_per_order", ZERO),
            )
            metric = "expected_unit_surplus_after_opportunity_and_displacement"
        result["sensitivity"].append(
            {
                "name": name,
                "overrides": changes,
                "evidence_status": "assumed_scenario",
                "assessment": evaluated["assessment"],
                "metric": metric,
                "baseline": baseline,
                "scenario": changed,
                "sign_reversal": sign(baseline) != sign(changed),
                "per_placed_order": evaluated["per_placed_order"],
                "period": evaluated["period"],
                "capacity": evaluated["capacity"],
            }
        )
    if not scenarios:
        result["limits"].append(
            "No uncertainty scenarios were supplied; thresholds hold all other inputs fixed."
        )
    return result


def json_number(value):
    if isinstance(value, Decimal):
        return float(round(value, 6))
    raise TypeError(f"Cannot serialize {type(value).__name__}")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input",
        type=Path,
        help="UTF-8 JSON input, schema_version 1; see references/schema.md",
    )
    args = parser.parse_args(argv)
    try:
        with args.input.open(encoding="utf-8") as handle:
            data = json.load(
                handle,
                parse_float=Decimal,
                parse_constant=lambda value: Decimal(value),
                object_pairs_hook=unique_object,
            )
        result = evaluate(data)
        print(json.dumps(result, indent=2, default=json_number, allow_nan=False))
    except (InputError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
