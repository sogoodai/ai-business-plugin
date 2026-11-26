#!/usr/bin/env python3
"""Capture an explicitly configured browser journey and identity-scoped readback."""

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit


class CaptureError(ValueError):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise CaptureError(message)


def origin(url):
    require(isinstance(url, str), "HTTP URL must be a string")
    parts = urlsplit(url)
    require(parts.scheme in ("http", "https") and parts.hostname, "HTTP URL required")
    require(
        not parts.username and not parts.password, "URL credentials are unsupported"
    )
    return f"{parts.scheme}://{parts.netloc}"


def safe_url(url):
    parts = urlsplit(url)
    query = urlencode([(key, "[omitted]") for key, _ in parse_qsl(parts.query)])
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, ""))


def locator(page, target):
    if "label" in target:
        return page.get_by_label(target["label"], exact=True)
    options = {"exact": True, "name": target["name"]} if "name" in target else {}
    return page.get_by_role(target["role"], **options)


def validate(config, base_url=None):
    require(isinstance(config, dict), "config must be an object")
    require(config.get("schema_version") == 1, "schema_version must be 1")
    base = base_url or config.get("base_url", "")
    allowed = {origin(base)}
    require(
        isinstance(config.get("allowed_origins", []), list),
        "allowed_origins must be an array",
    )
    for entry in config.get("allowed_origins", []):
        require(entry == origin(entry), "allowed_origins must contain exact origins")
        allowed.add(entry)
    journey = config.get("journey", {})
    require(isinstance(journey, dict), "journey must be an object")
    for field in ("id", "expected_outcome"):
        require(
            isinstance(journey.get(field), str) and journey[field],
            f"journey.{field} required",
        )
    require(journey.get("kind") in ("purchase", "booking"), "invalid journey.kind")
    browser = config.get("browser", {})
    require(isinstance(browser, dict), "browser must be an object")
    viewport = browser.get("viewport", {})
    require(isinstance(viewport, dict), "browser.viewport must be an object")
    require(
        isinstance(browser.get("locale", "en-US"), str),
        "browser.locale must be a string",
    )
    for field in ("is_mobile", "has_touch"):
        require(
            type(browser.get(field, False)) is bool, f"browser.{field} must be boolean"
        )
    for field in ("width", "height"):
        require(
            type(viewport.get(field)) is int and 200 <= viewport[field] <= 4000,
            f"invalid viewport.{field}",
        )
    require(
        isinstance(browser.get("url"), str) and browser["url"], "browser.url required"
    )
    require(
        100 <= config.get("action_timeout_ms", 5000) <= 30000,
        "action_timeout_ms must be 100..30000",
    )
    steps = config.get("steps")
    require(
        isinstance(steps, list) and 0 < len(steps) <= 30,
        "steps must contain 1..30 actions",
    )
    ui = config.get("ui", {})
    require(isinstance(ui, dict), "ui must be an object")
    require(all(isinstance(step, dict) for step in steps), "steps must contain objects")
    targets = [step.get("target", {}) for step in steps] + [ui.get("target", {})]
    for target in targets:
        require(isinstance(target, dict), "target must be an object")
        require(
            ("label" in target) != ("role" in target), "target requires label or role"
        )
        require(set(target) <= {"label", "role", "name"}, "unsupported locator option")
        require(
            all(isinstance(value, str) and value for value in target.values()),
            "locator values must be nonempty strings",
        )
    for step in steps:
        require(
            step.get("action") in ("fill", "click", "check", "select_option"),
            "unsupported action",
        )
        if step["action"] in ("fill", "select_option"):
            require(
                isinstance(step.get("value"), str),
                "fill/select_option requires a string value",
            )
    require(
        ui.get("expected", "success") in ("success", "failure"),
        "ui.expected must be success or failure",
    )
    require(
        100 <= ui.get("timeout_ms", 5000) <= 30000, "ui.timeout_ms must be 100..30000"
    )
    for field in ("success_text", "failure_text", "pending_text"):
        if field in ui:
            require(isinstance(ui[field], str) and ui[field], f"invalid ui.{field}")
    require(
        "success_text" in ui or "failure_text" in ui,
        "provide a success or failure UI marker",
    )
    submission = config.get("submission", {})
    require(isinstance(submission, dict), "submission must be an object")
    require(
        isinstance(submission.get("url"), str) and submission["url"],
        "submission.url required",
    )
    require(
        submission.get("method") in ("POST", "PUT", "PATCH", "DELETE"),
        "submission.method must name the configured mutation",
    )
    readback = config.get("readback")
    if readback is not None:
        require(isinstance(readback, dict), "readback must be an object")
        identity = readback.get("identity", {})
        require(isinstance(identity, dict), "readback.identity must be an object")
        require(
            isinstance(identity.get("value"), str) and identity["value"],
            "readback.identity.value required",
        )
        fields = [identity.get("field"), readback.get("records_field", "records")]
        expected = readback.get("expected")
        require(
            isinstance(expected, dict) and expected,
            "readback.expected must name the expected record fields",
        )
        fields.extend(expected)
        for field in fields:
            require(
                isinstance(field, str) and field,
                "readback fields must be nonempty strings",
            )
            require(
                not any(
                    word in field.lower()
                    for word in (
                        "password",
                        "secret",
                        "token",
                        "cookie",
                        "credential",
                        "authorization",
                    )
                ),
                "secret fields cannot be captured",
            )
        require(
            identity["field"] not in expected, "identity belongs in readback.identity"
        )
        require(
            isinstance(readback.get("url"), str) and readback["url"],
            "readback.url required",
        )
        for field in ("processing_bound_ms", "max_wait_ms"):
            require(
                type(readback.get(field)) is int and 0 <= readback[field] <= 60000,
                f"readback.{field} must be 0..60000",
            )
        require(
            10 <= readback.get("poll_interval_ms", 250) <= 10000,
            "poll_interval_ms must be 10..10000",
        )
    urls = [browser["url"], submission["url"]]
    if readback:
        urls.append(readback["url"])
    for url in urls:
        require(
            origin(urljoin(base, url)) in allowed,
            "target origin must be explicitly configured",
        )
    return base, allowed


def read_record(request, config, base, timeout):
    from playwright.sync_api import Error as PlaywrightError

    identity = config["identity"]
    result = {
        "captured_at": now(),
        "matched_test_identity": False,
        "semantic_status": "unverified",
    }
    try:
        response = request.get(
            urljoin(base, config["url"]), timeout=timeout, max_redirects=0
        )
        result["http_status"] = response.status
        if not response.ok:
            result["error"] = "readback_http_error"
            return result
        payload = response.json()
        if not isinstance(payload, dict):
            result["error"] = "readback_invalid_json_shape"
            return result
        rows = payload.get(config.get("records_field", "records"))
        if payload.get(identity["field"]) != identity["value"] or not isinstance(
            rows, list
        ):
            result["error"] = "readback_scope_mismatch"
            return result
        if any(
            not isinstance(row, dict) or row.get(identity["field"]) != identity["value"]
            for row in rows
        ):
            result["error"] = "readback_record_identity_mismatch"
            return result
        result["matched_test_identity"] = True
        result["matching_record_count"] = len(rows)
        fields = [identity["field"], *config["expected"]]
        result["records"] = [{key: row.get(key) for key in fields} for row in rows]
        mismatches = [
            key
            for key, value in config["expected"].items()
            if len(rows) == 1
            and (
                key not in rows[0]
                or type(rows[0][key]) is not type(value)
                or rows[0][key] != value
            )
        ]
        result["mismatched_fields"] = mismatches
        result["semantic_status"] = (
            "absent"
            if not rows
            else "duplicate_records"
            if len(rows) != 1
            else "field_mismatch"
            if mismatches
            else "matched"
        )
    except (ValueError, PlaywrightError) as exc:
        result["error"] = f"readback_{type(exc).__name__}"
    return result


def poll_record(request, config, base, timeout, action_finished):
    attempts = []
    deadline = action_finished + config["max_wait_ms"] / 1000
    bound = action_finished + config["processing_bound_ms"] / 1000
    state = {
        "captured_at": now(),
        "matched_test_identity": False,
        "semantic_status": "unverified",
        "settled": False,
        "error": "observation_budget_exhausted",
    }
    while True:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return state, attempts
        state = read_record(
            request, config, base, min(timeout, max(1, int(remaining * 1000)))
        )
        attempts.append(state)
        elapsed = time.monotonic()
        state["elapsed_after_actions_ms"] = round((elapsed - action_finished) * 1000)
        state["settled"] = state["semantic_status"] == "matched" or (
            state["matched_test_identity"] and elapsed >= bound
        )
        if state["semantic_status"] == "matched" or elapsed >= min(bound, deadline):
            return state, attempts
        time.sleep(
            min(
                config.get("poll_interval_ms", 250) / 1000,
                min(bound, deadline) - elapsed,
            )
        )


def observe_ui(page, config, wait=True):
    deadline = time.monotonic() + config.get("timeout_ms", 5000) / 1000
    state = {"state": "unknown", "text": "", "signal_observed": False}
    target = locator(page, config["target"])
    while True:
        if target.count() == 1 and target.is_visible():
            text = target.inner_text(timeout=500)
            matches = [
                name
                for name in ("success", "failure", "pending")
                if config.get(f"{name}_text") and config[f"{name}_text"] in text
            ]
            state.update(
                state=matches[0] if len(matches) == 1 else "unknown",
                text=text[:1000],
                signal_observed=len(matches) == 1,
            )
            if state["state"] in ("success", "failure"):
                break
        if not wait or time.monotonic() >= deadline:
            break
        page.wait_for_timeout(50)
    state["captured_at"] = now()
    return state


def save(path, value):
    path.write_text(
        json.dumps(value, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )


def capture(config, output_dir, executable_path=None, base_url=None):
    base, allowed = validate(config, base_url)
    config = {**config, "base_url": base}
    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise CaptureError(
            "Playwright Python is optional and unavailable. Use an environment with Playwright and an existing Chromium installation."
        ) from exc
    output_dir = Path(output_dir)
    require(
        not output_dir.exists() or not any(output_dir.iterdir()),
        "output directory must be empty to preserve earlier evidence",
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    network, steps, screenshots, blocked_urls = [], [], [], []
    ui = {"state": "unknown", "text": "", "signal_observed": False}
    backend = {
        "semantic_status": "unchecked",
        "matched_test_identity": False,
        "settled": False,
    }
    baseline, attempts = None, []
    status, error = "captured", None
    timeout = config.get("action_timeout_ms", 5000)
    browser_config = config["browser"]
    url = urljoin(base, browser_config["url"])
    submission_url = urljoin(base, config["submission"]["url"])
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(executable_path=executable_path)
        except PlaywrightError as exc:
            raise CaptureError(
                "Chromium could not launch. Supply --executable-path for an existing compatible browser."
            ) from exc
        try:
            context = browser.new_context(
                viewport=browser_config["viewport"],
                locale=browser_config.get("locale", "en-US"),
                is_mobile=browser_config.get("is_mobile", False),
                has_touch=browser_config.get("has_touch", False),
                service_workers="block",
            )
            context.set_default_timeout(timeout)

            def route_request(route):
                if (
                    urlsplit(route.request.url).scheme in ("http", "https")
                    and origin(route.request.url) in allowed
                ):
                    route.continue_()
                else:
                    blocked_urls.append(safe_url(route.request.url))
                    route.abort()

            context.route("**/*", route_request)
            page = context.new_page()
            requests = {}

            def on_request(request):
                row = {
                    "method": request.method,
                    "url": safe_url(request.url),
                    "resource_type": request.resource_type,
                    "started_at": now(),
                    "status": None,
                }
                requests[request] = row
                network.append(row)

            def on_response(response):
                if response.request in requests:
                    requests[response.request].update(
                        status=response.status, responded_at=now()
                    )

            def on_failed(request):
                if request in requests:
                    requests[request].update(failed=True, finished_at=now())

            page.on("request", on_request)
            page.on("response", on_response)
            page.on("requestfailed", on_failed)
            if config.get("readback"):
                baseline = read_record(
                    context.request, config["readback"], base, timeout
                )
                if (
                    not baseline["matched_test_identity"]
                    or baseline.get("matching_record_count") != 0
                ):
                    status = "blocked_baseline"
                    error = "Use a fresh test identity and a working identity-scoped readback before submission."
            if status == "captured":
                try:
                    page.goto(url, wait_until="domcontentloaded", timeout=timeout)
                    page.screenshot(
                        path=str(output_dir / "initial.png"), full_page=False
                    )
                    screenshots.append(
                        {
                            "file": "initial.png",
                            "captured_at": now(),
                            "viewport": page.viewport_size,
                        }
                    )
                    for step in config["steps"]:
                        row = {
                            "action": step["action"],
                            "target": step["target"],
                            "started_at": now(),
                        }
                        steps.append(row)
                        target = locator(page, step["target"])
                        if step["action"] == "fill":
                            require(
                                target.get_attribute("type") != "password"
                                and target.get_attribute("autocomplete")
                                not in (
                                    "current-password",
                                    "new-password",
                                    "one-time-code",
                                ),
                                "Authentication fields are unsupported",
                            )
                            target.fill(step["value"])
                        elif step["action"] == "select_option":
                            target.select_option(step["value"])
                        elif step["action"] == "check":
                            target.check()
                        else:
                            target.click()
                        row["completed_at"] = now()
                    action_finished = time.monotonic()
                    ui = observe_ui(page, config["ui"], wait=not config.get("readback"))
                    if config.get("readback"):
                        backend, attempts = poll_record(
                            context.request,
                            config["readback"],
                            base,
                            timeout,
                            action_finished,
                        )
                    initial_ui = ui
                    remaining_ms = (
                        config["readback"]["max_wait_ms"]
                        - (time.monotonic() - action_finished) * 1000
                        if config.get("readback")
                        else 0
                    )
                    final_ui_config = {
                        **config["ui"],
                        "timeout_ms": min(
                            config["ui"].get("timeout_ms", 5000), max(0, remaining_ms)
                        ),
                    }
                    ui = observe_ui(page, final_ui_config, wait=remaining_ms > 0)
                    ui["initial_observation"] = initial_ui
                except (CaptureError, PlaywrightError) as exc:
                    status, error = (
                        "incomplete",
                        f"Browser step did not finish ({type(exc).__name__}); no submit retry was attempted.",
                    )
                try:
                    page.screenshot(path=str(output_dir / "final.png"), full_page=False)
                    screenshots.append(
                        {
                            "file": "final.png",
                            "captured_at": now(),
                            "viewport": page.viewport_size,
                        }
                    )
                except PlaywrightError:
                    status, error = (
                        "incomplete",
                        "Final screenshot unavailable; inspect partial evidence.",
                    )
            version, final_url = browser.version, safe_url(page.url)
            submission_rows = [
                requests[request]
                for request in requests
                if request.url == submission_url
                and request.method == config["submission"]["method"]
            ]
            context.close()
        finally:
            browser.close()
    save(
        output_dir / "network.json", {"requests": network, "blocked_urls": blocked_urls}
    )
    save(
        output_dir / "readback.json",
        {"baseline": baseline, "attempts": attempts, "final": backend},
    )
    evidence = build_evidence(
        config,
        output_dir,
        status,
        error,
        steps,
        screenshots,
        ui,
        backend,
        version,
        final_url,
        submission_rows,
    )
    save(output_dir / "evidence.json", evidence)
    return evidence


def build_evidence(
    config,
    output_dir,
    status,
    error,
    steps,
    screenshots,
    ui,
    backend,
    version,
    final_url,
    submission_rows,
):
    captured_at = now()
    sources = [
        {
            "id": "network",
            "kind": "browser",
            "captured_at": captured_at,
            "locator": str((output_dir / "network.json").resolve()),
        }
    ]
    for screenshot in screenshots:
        sources.append(
            {
                "id": screenshot["file"].removesuffix(".png"),
                "kind": "browser",
                "captured_at": screenshot["captured_at"],
                "locator": str((output_dir / screenshot["file"]).resolve()),
            }
        )
    if config.get("readback"):
        sources.append(
            {
                "id": "readback",
                "kind": "backend",
                "captured_at": backend.get("captured_at", captured_at),
                "locator": str((output_dir / "readback.json").resolve()),
            }
        )
    known = backend["matched_test_identity"]
    persisted = (
        "unchecked"
        if not known
        else "present"
        if backend.get("matching_record_count")
        else "absent"
    )
    outcome = {
        "ui": ui["state"] if ui["state"] in ("success", "failure") else "unknown",
        "persisted_record": persisted,
        "verification_evidence_ids": ["readback"] if config.get("readback") else [],
    }
    if submission_rows and submission_rows[-1]["status"] is not None:
        outcome["http_status"] = submission_rows[-1]["status"]
    if config.get("readback"):
        outcome["verification"] = {
            "query": f"GET {safe_url(urljoin(config['base_url'], config['readback']['url']))}; exact {config['readback']['identity']['field']}={config['readback']['identity']['value']}",
            "settled": backend["settled"],
            "matched_test_identity": known,
        }
    result = "unknown"
    if status == "captured" and submission_rows and known and backend["settled"]:
        expected_ui = config["ui"].get("expected", "success")
        expected_backend = "matched" if expected_ui == "success" else "absent"
        result = (
            "pass"
            if ui["state"] == expected_ui
            and backend["semantic_status"] == expected_backend
            else "fail"
            if ui["state"] in ("success", "failure")
            else "unknown"
        )
    replay = [f"Open {safe_url(urljoin(config['base_url'], config['browser']['url']))}"]
    replay.extend(
        f"{step['action']} {json.dumps(step['target'], ensure_ascii=True)} (configured value omitted)"
        if step["action"] in ("fill", "select_option")
        else f"{step['action']} {json.dumps(step['target'], ensure_ascii=True)}"
        for step in steps
    )
    evidence = {
        "schema_version": 1,
        "journey": config["journey"],
        "sources": sources,
        "observations": [
            {
                "id": "browser-capture",
                "title": "Browser confirmation and exact persisted outcome",
                "expected": config["journey"]["expected_outcome"],
                "actual": f"UI={ui['state']}; record semantics={backend['semantic_status']}; capture={status}",
                "steps": replay,
                "environment": {
                    "url": final_url,
                    "device": json.dumps(config["browser"]["viewport"], sort_keys=True),
                    "browser": f"Chromium {version}",
                    "path": config["journey"].get("path", config["journey"]["kind"]),
                },
                "reproduced": status == "captured",
                "result": result,
                "evidence_ids": [source["id"] for source in sources],
                "outcome": outcome,
            }
        ],
        "capture": {
            "status": status,
            "error": error,
            "config_sha256": hashlib.sha256(
                json.dumps(config, sort_keys=True).encode()
            ).hexdigest(),
            "steps": steps,
            "screenshots": screenshots,
            "ui": ui,
            "backend_semantics": backend["semantic_status"],
            "mismatched_fields": backend.get("mismatched_fields", []),
            "submission_response_count": len(submission_rows),
            "locale": config["browser"].get("locale", "en-US"),
            "is_mobile": config["browser"].get("is_mobile", False),
            "has_touch": config["browser"].get("has_touch", False),
        },
        "capture_limits": [
            "Only the explicitly configured path, viewport, UI markers and backend fields were checked; no funnel or causal inference.",
            "The caller supplies the target, sandbox authorization and agreed processing bound; this capture does not establish them.",
            "HTTP status and visible confirmation are independent signals, never proof of a persisted successful outcome.",
            "Audit v1 reports physical record presence. Check capture.backend_semantics and the observation result for status, amount, slot or duplicate-record failures.",
            "Request and response bodies, headers, storage and cookies are not exported. Query values and form values are omitted; screenshots and visible UI text may contain test data.",
        ],
    }
    return evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "config",
        type=Path,
        help="Explicit journey JSON; use only on an authorized target",
    )
    parser.add_argument("output_dir", type=Path, help="New or empty evidence directory")
    parser.add_argument(
        "--executable-path",
        help="Existing Chromium executable; no browser is installed by this script",
    )
    parser.add_argument(
        "--base-url",
        help="Override the configured origin, for a local fixture's dynamic port",
    )
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text(encoding="utf-8"))
        evidence = capture(config, args.output_dir, args.executable_path, args.base_url)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "capture_error", "error": str(exc)}))
        return 2
    print(
        json.dumps(
            {
                "status": evidence["capture"]["status"],
                "evidence": str((args.output_dir / "evidence.json").resolve()),
                "result": evidence["observations"][0]["result"],
            }
        )
    )
    return 0 if evidence["capture"]["status"] == "captured" else 1


if __name__ == "__main__":
    sys.exit(main())
