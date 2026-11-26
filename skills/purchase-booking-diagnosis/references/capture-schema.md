# Browser capture

`scripts/capture.py` executes the supplied journey. It can submit the configured form. Use it only against a target and actions the user authorized. The checked-in configuration is for a local synthetic server, with no payment or real booking. No live customer target was tested.

Playwright Python and an existing Chromium installation are optional dependencies. The script installs nothing. `--help` works without them. Use `--executable-path` when the installed Playwright version expects a different browser build.

```sh
python3 scripts/capture.py fixtures/capture-purchase.json /tmp/purchase-evidence \
  --base-url http://127.0.0.1:8765 \
  --executable-path /path/to/existing/chromium
python3 scripts/audit.py /tmp/purchase-evidence/evidence.json
```

The output directory must be new or empty. The fixture config does not start a server. The integration tests start their own loopback server and use the same config with a dynamic port. Run `python3 -m unittest discover -s tests -p test_capture.py -v`. Set `CAPTURE_CHROMIUM_EXECUTABLE` to an existing executable when automatic test discovery cannot find Chromium. Browser tests skip, with a reason, if the optional dependencies are absent.

## Configuration

Use [capture-purchase.json](../fixtures/capture-purchase.json) as the complete example. A config records one path and one test attempt. Use a fresh identity for each replay.

| Field | Meaning |
| --- | --- |
| `schema_version` | `1` |
| `base_url` | HTTP origin of the authorized test environment. `--base-url` overrides it for a dynamic local port. |
| `journey` | Nonempty `id`, `kind` (`purchase` or `booking`), `expected_outcome`, and optional path name. |
| `browser` | Relative or absolute `url`, explicit viewport `width` and `height`, optional `locale`, `is_mobile` and `has_touch`. |
| `allowed_origins` | Optional additional exact HTTP origins. Other browser requests are blocked, including redirects to other origins. These entries describe routing, not authorization. Backend readback does not follow redirects. |
| `steps` | Up to 30 `fill`, `click`, `check` or `select_option` actions. Each target uses an exact `label`, or a `role` with optional exact accessible `name`. Fill and select need a string `value`. No selectors, arbitrary JavaScript or force clicks. |
| `action_timeout_ms` | Locator action timeout, default 5000, maximum 30000. Playwright waits for actionability. Each action is invoked once; a submission is never retried. |
| `ui` | Exact role/label `target`; case-sensitive `success_text`, `failure_text`, optional `pending_text`; `expected` is success or failure; bounded `timeout_ms`. Conflicting markers remain unknown. Pending remains unknown. |
| `submission` | Exact relative/absolute request `url` and mutation `method`, used to identify the observed submission response. HTTP status does not determine success. |
| `readback` | Optional GET-only saved-record check described below. Omit it when unavailable, and the outcome remains unverified. |

Do not put passwords, login codes, access tokens or production identities in the config. Password and authentication-code inputs are unsupported. The browser uses a fresh temporary context. It does not load a login profile or export cookies, storage, request/response headers or bodies. Action logs omit fill/select values, and network URLs omit query values. Screenshots and visible status text can contain test data. Keep them in the approved private location.

## Exact persisted-record check

The normalized JSON readback needs an echoed identity and an array of records. Every returned record must have the same exact identity. For example:

```json
{
  "test_id": "capture-purchase",
  "records": [{
    "test_id": "capture-purchase",
    "status": "confirmed",
    "amount": 1250,
    "currency": "EUR"
  }]
}
```

Configure `identity.field` and `identity.value`, the GET `url`, `records_field` (default `records`), and a nonempty `expected` object. Expected keys are flat record fields. Their JSON values and types must match exactly. Include the actual successful order/booking status. Include amount and currency, quantity, selected slot or other required outcome fields where applicable. State the amount's units in `journey.expected_outcome`. Unlisted fields are neither verified nor exported. More than one matching record is a semantic failure.

Before browser actions, the tool checks that this exact identity has no existing record. An unavailable, incorrectly scoped or nonempty baseline blocks submission. This prevents an older record from proving a fresh replay. The tool makes no cleanup or backend mutation calls.

`processing_bound_ms` is the caller-supplied agreed processing bound, measured conservatively from the end of the last configured action. `max_wait_ms` caps follow-up from that same time. Both are 0 to 60000. `poll_interval_ms` bounds repeated GETs, default 250. Provide a documented bound appropriate to the sandbox. A short arbitrary wait cannot establish real asynchronous failure. If the valid bound exceeds the capture limit, retain pending evidence and arrange a later readback separately.

The tool samples UI, polls readback within the remaining follow-up budget, then samples UI again before the final screenshot. Each GET timeout is capped to that remaining budget. A zero follow-up budget performs no post-action GET and remains unverified. The final `capture.ui` retains its `initial_observation` so a changed message is visible in the evidence. A correct matching record can settle immediately. Absence or wrong fields settle only after the configured processing bound. If follow-up ends sooner, the audit observation stays unknown with `verification.settled: false`. Wrong-identity or malformed records stay unverified. A declining negative control uses `ui.expected: "failure"`; it passes when the failure UI accompanies scoped record absence after the bound.

## Saved evidence and limits

- `evidence.json` is accepted by `audit.py` schema v1. It contains actual timestamps, viewport, browser version, locator actions and screenshot/backend source paths. Reproduction is true only when configured browser actions complete. No cohort counts or conversion rates are invented.
- `initial.png` and `final.png` are screenshots at the exact viewport, not full-page composites. Inspect the final pixels before using them as delivery evidence.
- `network.json` records request method, redacted URL, resource type, request/response times, HTTP status or request failure. It records browser requests, not the separate API GETs.
- `readback.json` records the baseline, timed polling attempts and projected expected fields. It records identity mismatches without exporting another record's contents.
- `capture.backend_semantics` distinguishes `matched`, `absent`, `field_mismatch`, `duplicate_records`, `unverified` and `unchecked`. `capture.mismatched_fields` names a wrong status, amount or slot. Audit v1's `verified_present` means physical record presence only. A wrong-status record produces an observation failure and must not be called a successful purchase or confirmed booking.

The capture does not independently establish backend authority, authorization, actual payment-provider settlement, analytics delivery, other device/path behavior, or customer acceptance. A screenshot, event or HTTP 200 alone proves none of those. Compare the raw readback and browser evidence with the expected customer outcome.
