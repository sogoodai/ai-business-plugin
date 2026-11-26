# Evidence input, version 1

The auditor uses Python 3.10+ standard library only. Run `python3 scripts/audit.py INPUT.json`, omit the filename for stdin, or pass `-`. It writes JSON to stdout, returns 0 for an audited document and 2 for invalid evidence. No network access, browser action or file output occurs. A valid document can still contain insufficient evidence; withheld rates appear in `blocked_funnels`.

Start with [the small synthetic fixture](../fixtures/synthetic.json). It is invented test data, not a benchmark or customer result. Optional arrays default to empty. Omit unavailable optional sections rather than fabricating values. Unknown step counts use JSON `null`, never zero.

## Required root and provenance

```json
{
  "schema_version": 1,
  "journey": {
    "id": "one-journey",
    "kind": "booking",
    "expected_outcome": "One confirmed booking for the chosen service and slot"
  },
  "sources": [
    {"id": "replay", "kind": "browser", "captured_at": "2026-11-16T10:00:00Z", "locator": "/private/evidence/replay.png"},
    {"id": "records", "kind": "backend", "captured_at": "2026-11-16T10:00:05Z", "locator": "/private/evidence/test-booking-query.json"}
  ]
}
```

`kind` is `purchase` or `booking`. Source kind is `browser`, `event_export`, `backend`, `cost_record` or `other`. Each source requires a unique nonempty `id`, ISO timestamp with timezone and nonempty `locator` (file, URL or exact query reference). Sources are supplied provenance, not proof that the auditor has read them. Keep full query, export settings, capture and redacted raw evidence at the locator.

## Observations: useful without analytics

Optional `observations` is an array. Each observation requires unique `id`, `title`, `expected`, `actual`, nonempty replay `steps` strings, `environment` with nonempty `url`, `device`, `browser`, `path`, `evidence_ids` and boolean `reproduced`. A reproduced claim requires a browser source. `result` is `pass`, `fail` or `unknown` (default). Set `fail` only for behavior conflicting with the expected contract. `reproduced: true` does not itself mean a defect.

Optional `outcome`:

```json
{
  "ui": "success",
  "http_status": 200,
  "persisted_record": "absent",
  "verification_evidence_ids": ["records"],
  "verification": {
    "query": "Lookup test_id=fixture-1 after the agreed 5-second processing bound",
    "settled": true,
    "matched_test_identity": true
  }
}
```

`ui`: `success`, `failure`, `unknown`. `persisted_record`: `present`, `absent`, `unchecked`. A present/absent assertion needs backend provenance. The auditor treats it as verified only with both verification booleans true and a query. The caller must actually inspect the identity, final status and correct amount/slot, and establish a sufficient processing window. An empty query at the wrong account, stale replica or before settlement is not verified absence. A card-decline negative test can validly return HTTP 200 and no order. HTTP status alone proves neither success nor failure.

Do not attach an outcome check to a blocked earlier step that never attempted submission. For a completed submission with unavailable record access use `persisted_record: "unchecked"`.

## Optional cohort scopes and funnels

Every `scopes` item requires:

| Field | Meaning / allowed values |
|---|---|
| `id` | Unique scope identifier. Every funnel step uses the same identifier to be comparable. |
| `start`, `end`, `timezone` | ISO timestamps with offsets for entrant window, plus business timezone name. End is exclusive. |
| `population` | Eligibility, geography, product/service, consent, test/bot exclusions and filters; explicitly state unknowns. |
| `source`, `device`, `path` | Exact channel/source/campaign dimension basis, device/browser segment and standard/express-wallet path. Use an explicit all/unknown string when appropriate. |
| `unit`, `identity` | `user`, `session`, `attempt` or `event`; exact entity key, identity stitching and cross-domain rule. |
| `counting`, `deduplication` | `unique_per_step`, `raw`, `unknown`; rule and key used to remove transport duplicates while preserving real attempts. |
| `sequence`, `entry` | `ordered` / `unordered` / `unknown`; `closed` / `open` / `unknown`. |
| `completion_window_seconds` | Nonnegative integer, maximum allowed time from entrant to completion. Do not use 0 to mean unknown. |
| `maturity` | `mature`, `right_censored`, `unknown`. Mature means even the last entrant has had the full follow-up and ingestion lag. |

Scope is a declaration that must match the underlying export. GA4's user-once funnel and an attempt-level checkout funnel have different semantics even with identical timestamps. `unique_per_step` means each entity is counted once at each attained step and later-step membership is a subset of earlier ordered membership. For open funnels or aggregate event counts, re-export a closed cohort or do entity-level reconstruction first. The auditor does not reconstruct raw event streams.

Optional `funnels` contains `{id, steps}`. Steps are ordered objects `{name, count, scope_id, evidence_ids}` with unique names and nonnegative integer or null counts. At least two steps are required. Example:

```json
{"id":"mobile-standard", "steps":[
  {"name":"checkout started","count":20,"scope_id":"cohort-1","evidence_ids":["export"]},
  {"name":"order saved","count":4,"scope_id":"cohort-1","evidence_ids":["records"]}
]}
```

Rates require one scope ID, unique entity counts, ordered closed membership, mature follow-up and nonincreasing known counts. Mixed scopes, duplicate-prone raw events, event units, open/unordered funnels, immature windows, increasing counts or unknown counts withhold the entire funnel. This is deliberately conservative: merge semantically identical scope declarations before running rather than guessing equivalence. A zero denominator returns a null rate.

Capture timestamps must be consistent with maturity. Entry-count evidence must be captured after the entrant window closes; later-step evidence must cover that end plus the completion window. If every supporting source for a step predates that boundary, rates are withheld even when `maturity` says mature. A later capture is necessary, not proof that the exported data actually include the complete window. Outcome-derived economics use the same check.

Each computed transition reports numerator, denominator, rate (fraction), `did_not_progress` and `small_denominator` (denominator below 100). Nonprogress is a symptom, not a count of errors or causal abandonments. Counts taken only from client events remain event-derived even if the step is called "purchase". Verify records separately. Do not add symptoms across overlapping funnels, people, devices or paths.

## Optional economics and hypotheses

`economics` is an array of `{scope_id, currency, cost?, realized_value?, verified_outcomes?}`. Every amount is finite; only realized contribution may be negative. Currency is a three-letter uppercase code. Each component needs `evidence_ids`. Components inherit the same scope; assemble them only after reconciling period, population, currency, attribution and refunds. Do not put last month's collected revenue in this week's entrant cohort.

- `cost`: `{amount, basis: "media_spend" | "total_cost", evidence_ids}`.
- `realized_value`: `{amount, basis: "gross_revenue" | "contribution", evidence_ids}`. Booked or forecast value is not realized value; keep it outside this section until realized. State refund/discount/tax treatment in source evidence.
- `verified_outcomes`: `{count, evidence_ids}`. Distinct final orders/bookings from backend provenance, not client events or all-time totals. The caller must reconcile the final status and deduplication.

For mature scopes, the script computes actual cost per supplied verified outcome and realized value/cost ratio. Media spend with gross revenue is labelled `reported_roas`, describing the supplied attribution, not incrementality. Zero denominators return null. Missing cost withholds economics. It does not calculate profit, causal loss, future value or recoverable revenue. Capacity remains an operating constraint to inspect in the diagnosis; it cannot be inferred from counts or dollar values.

`hypotheses` is an array of `{id, claim, test, evidence_ids?}`. These remain `unverified_hypothesis`, even with many citations. Include the observable result that could disprove each claim.

## Output limits

`findings` contains evidence classifications, an action and a verification condition. Observed defects sort before instrumentation gaps, funnel symptoms and hypotheses. `outcome_checks` distinguishes verified present/absent from unverified. A matching record lookup with `settled: false` is `pending_verification`; waiting for the agreed processing bound does not itself produce an instrumentation finding. An all-pass replay can legitimately produce no defect findings. No finding means no supported defect in the supplied evidence, not proof that the business works. The auditor validates structure and declared semantics; it does not authenticate evidence, prove causal impact, read record contents or choose a live repair.
