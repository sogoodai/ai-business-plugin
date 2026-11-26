---
name: purchase-booking-diagnosis
description: "My checkout or booking is broken, or people visit but don't buy. Find where one purchase or booking journey fails and how to fix it. Use when a founder says: customers can't pay, the checkout errors, orders or bookings are missing, the booking form doesn't save, people add to cart then leave, traffic but no sales, or sales dropped on mobile or from one ad. Replays the journey in a browser, reads funnel data, gives the fix and how to check it worked."
---

# Purchase or booking diagnosis

Find the failing transition in one journey and show how to verify its repair. Read the existing evidence before asking for missing inputs. A URL alone permits an initial visible inspection; it does not provide funnel data, lost revenue or permission to place a real order.

## Establish what success means

Identify the entry URL and acquisition promise, expected order or booking state, platform, affected period, source/campaign, device/browser and standard versus express-wallet path. For booking, establish service timezone, availability and capacity. A request, payment authorization, confirmed booking and attended appointment are different outcomes. Record the exact outcome being diagnosed.

Use authorized read-only records and exports where available. Replay in a local fixture, sandbox or test mode. A real charge, reservation that consumes capacity, customer edit or live repair needs the corresponding user authorization. Keep identifying customer data in private evidence, outside this distributable skill.

## Replay the affected path

Start with the reported source and device, then a working adjacent path. Inspect the rendered page at its actual viewport after it settles. Follow the CTA through validation, totals, payment or slot selection and confirmation. Capture the URL, viewport/browser, timestamp, exact steps, expected/actual behavior, screenshot or trace and request/response evidence at the failure.

Choose checks that discriminate between explanations:

- **Interaction:** click or tap normally, without forced clicks. Check overlays, disabled controls, invalid fields, keyboard and errors that erase entered data. A DOM element existing does not show that a customer can use it.
- **Purchase:** compare standard checkout with the affected wallet, account or off-site return path. Confirm total, currency, quantity and shipping destination. A skipped cart or checkout step may be a legitimate express path.
- **Booking:** inspect the selected date in the service timezone, slot availability, duration and resource capacity. Test a known available slot and a full/unavailable slot in a sandbox. Capacity exhaustion can explain no bookings without a broken button. Do not prescribe more demand when there is no capacity.
- **Outcome:** correlate the test identifier with an authoritative saved record after the agreed processing window. Check the final state, amount or slot, quantity and identity. A thank-you page, HTTP 200, analytics hit or outbound email alone does not prove persistence. A record missing before asynchronous processing settles does not prove failure.
- **Measurement:** compare one test action with the emitted event, received event and saved record. Re-entry, refresh, duplicate senders, consent, blockers and cross-domain identity can change counts without changing purchases. Do not disable customer privacy controls to improve reported conversion.

Use an available browser connector or Playwright; this skill does not require a new browser dependency. For Playwright, use user-facing locators and retrying assertions on the settled UI, then separately poll an authorized record lookup with the test identifier and bounded timeout. Capture failure pixels. Browser emulation does not prove wallet behavior on a physical phone or an in-app browser; mark that gap.

For a repeatable authorized sandbox path, read [the capture contract](references/capture-schema.md). When the supplied configuration matches it and Playwright is available, run the collector first. Write custom browser code only for an unsupported requirement or diagnosed collector failure:

```sh
python3 scripts/capture.py journey-config.json /private/path/evidence
python3 scripts/audit.py /private/path/evidence/evidence.json
```

It records actual screenshots, viewport, action and network-status evidence, then performs an identity-scoped GET readback. A preexisting record cannot prove a new replay succeeded. It distinguishes pending processing, missing records and wrong status/amount/slot. The collector uses a fresh browser context and existing Playwright; it does not authenticate to production systems. Inspect its final pixels and raw readback. A blocked origin, unavailable browser or unavailable record API is a capture limitation, not proof of a site defect. Use the documented contract for execution; source inspection is needed only for a tool failure or unsupported requirement.

## Reconcile the funnel before dividing

Read [the evidence schema](references/evidence-schema.md) when assembling the JSON input. Export the entrant cohort with one identity/counting unit, ordered step membership, completion window, timezone and mature follow-up. Keep source/campaign, device and checkout path separate when they change eligibility or instrumentation. Inspect duplicate event IDs and repeated legitimate attempts before deduplicating. Do not divide sessions by users, raw hits by unique people, open-funnel totals, unrelated daily totals, or this week's starts by this week's completions from earlier cohorts.

Run the offline auditor, which validates supplied evidence and computes comparable descriptive rates:

```sh
python3 scripts/audit.py /private/path/journey-evidence.json
python3 scripts/audit.py < /private/path/journey-evidence.json
python3 scripts/audit.py fixtures/synthetic.json
```

Paths above are relative to this skill's directory. Inspect `blocked_funnels` and source contents before treating output as evidence. The script neither visits URLs nor independently confirms that a source's declared cohort, counts or records are true. Its `small_denominator` flag is a review prompt, not a significance test. With sparse traffic, reproduce the defect and validate the outcome; do not invent an A/B win.

Use actual supplied costs and realized values only for descriptive cohort economics. Name the basis: media spend versus total cost, gross revenue versus contribution, booked versus collected value. Missing costs stay unknown. Do not multiply drop-offs by order value, a benchmark gap or an assumed recovery percentage and call it lost or recoverable revenue. Even a reproduced defect does not establish how many historical abandonments it caused.

## Deliver the decision

Lead with the affected transition and evidence status. Give at most five ranked findings. Separate:

| Status | What supports it | Next action |
|---|---|---|
| Observed reproducible defect | Replay steps and captured failure, with saved-record check when relevant | Repair that transition and repeat the affected and working adjacent paths |
| Funnel symptom | Comparable cohort counts and their period | Replay the transition; distinguish real failures from event loss |
| Unverified hypothesis | Plausible explanation without a discriminating result | One test with a result that would disprove it |
| Missing instrumentation | Unknown identity, scope, event delivery or authoritative outcome | Obtain the smallest missing export or record lookup |

For each finding include the source locator, exact environment/steps, observed result, practical change or test, and verification condition. Include counts and denominator beside any rate. State actual economics only when supplied and comparable. Do not rank by invented financial loss.

After an authorized repair, replay at the same viewport and entry path, inspect the saved record and rendered result, and check that one action produces one intended event or record. Include negative validation and an unaffected standard or wallet path where relevant. Report repair verification separately from customer acceptance and production release.

Read [sources and counterexamples](references/sources.md) only for the relevant mechanism or platform caveat. Prefer the current platform documentation over an anecdote. This procedure diagnoses a journey; it does not call for a sitewide redesign or a generic CRO checklist.
