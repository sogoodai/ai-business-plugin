# Intake: from inquiry to attended first visit

The cheapest growth in most clinics. Invoca 2026: 54% of calls answered live, 45% of qualified phone leads booked, 43% of organizations never asked to book. Zencare 2025: average therapist reply 28 hours.

## Stage taxonomy (set up on day 1)

Every inquiry gets a record: source (captured before staff overwrite it), timestamp, channel, first two-way human reply time, qualification, insurance status, booking status, appointment date, attended or not, first collection, and later plan-of-care status.

Allowed states: `new` > `replied` > `qualified` > one of `booked`, `booked later + waitlist`, `pending insurance or referral`, `lost`. "Will call back" is not a state.

Lost reasons (fixed list): no response, out of network and declined cost, no availability soon enough, wrong service or level of care, location or parking, schedule, price, chose another provider, needs referral, not ready, other.

## Response SLA

| Situation | Target | Mechanism |
|---|---|---|
| Phone, business hours | answered live; under 3 rings | overflow to second phone or answering service under BAA |
| Missed call | text-back within 1 minute, human callback within 15 | missed-call text automation |
| Web form, directory message, text | first two-way human reply under 5 minutes in hours | alert to two phones, round-robin owner |
| After hours | instant reply with self-booking or callback time | scheduler link, AI or service limited to non-clinical answers |
| Voicemail | callback within 15 minutes in hours, first thing next day otherwise | voicemail-to-text, queue |

Evidence: human reply under 5 minutes booked at more than 3x the rate of over 24 hours (9 practices, 2026). A dental clinic that alerted staff and bridged a call on every Meta lead form reports 30 to 40% more bookings (operators report, 131). Autoresponders do not count as a reply (Invoca excluded them).

Solo clinicians without a front desk: block two 10-minute inquiry windows a day minimum (between sessions), use a scheduler with intake built in, and put "I reply to all messages by [time]" in the autoresponder. An Alberta solo psychologist budgets 5 hours a week as "own secretary" (operators report, 873).

## The first reply

Goal: one message that answers the two deterministic questions (insurance and soonest time) and offers a booking.

- Ask for plan name only, never member ID, diagnosis or symptoms by SMS or ordinary email.
- Offer two times or a self-book link.
- Move clinical detail into the secure intake form.

Script in [scripts.md](scripts.md#first-reply-to-an-inquiry).

## Therapy: consult or straight to intake

- A bookable consult converts better than messaging: 73.7% vs 40.4% completion (Zencare 2025, platform data).
- Keep the consult 15 minutes, free, by phone or video, with three goals: fit (issue, level of care, risk screen per the clinician's protocol), logistics (insurance or fee, schedule, telehealth or office), next step (book intake on the call).
- Phone screening still matters for safety and fit: a 19-year therapist screens every caller before offering openings after a hostile caller (operators report, 1,514). Screen on the booked consult, not in a long message chain.
- Close on the call: "It sounds like a good fit. I have Tuesday at 6 or Thursday at 11 for your first full session. Which works?" ([scripts.md](scripts.md#therapy-consult-call))
- Not a fit: give two named referrals with openings. Keep a peer list of who has space; they return the favor.

## Chiro, PT, acupuncture: exam and report

- First visit = history, exam, a clear explanation, and treatment the same day if appropriate. Patients who leave untreated rarely return.
- Do not give free evaluations by default. A first-year DC examined and advised for free, the patient declined treatment despite €500 a year coverage, no money changed hands (operators report, 25). Price the exam; reduce it for cash patients if you want a low barrier, never for federal beneficiaries ([reviews-and-compliance.md](reviews-and-compliance.md#5-inducements-free-services-and-discounts-us)).
- Report of findings: diagnosis in plain words, what care looks like, how progress is measured, total cost, when you re-examine. A DC presenting 12 to 18 visit plans with financials heard "this all feels very sales and not very medical" (operators report, 25). Fix: lead with the patient's goal, show the measure (pain scale, range of motion, outcome questionnaire), offer a short first block with a re-exam date, not a full contract.
- PT: book the expected visits for the first 2 to 3 weeks before the patient leaves visit 1.

## Dental: phones and treatment acceptance

- New-patient calls get a scripted answer to insurance in the first minute; insurance was a barrier 11x as often as price (Patient Prism 2025).
- Ask for the appointment on every call; offer two times inside 7 days.
- Same-day emergency slots convert and seed treatment; keep two a day.
- Treatment acceptance: phase the plan, show photos, give the cost after insurance estimate and financing in writing, and schedule phase 1 before the patient leaves. Planet DDS 2025: 56% accepted but 46% completed: schedule every phase, not just the first.
- Corporate-style quotas on CareCredit applications and Google reviews hurt staff and trust (operators report, 226). Offer financing, do not push it.

## Insurance verification

- Verify eligibility before visit 1 and tell the patient the expected cost in writing. Surprise bills kill plans of care.
- Out of network: give the superbill script and the questions to ask their plan ([scripts.md](scripts.md#out-of-network-and-superbill)).
- US self-pay: Good Faith Estimate when booking 3+ business days ahead (CMS).

## Booking path

- Online booking for new patients wherever the clinician allows it. About 30% of online bookings happen outside 8 a.m. to 5 p.m. (DexCare 2026).
- Count taps from Google to a confirmed booking on a phone; fix anything over about 6.
- New-patient slots protected weekly so lead time stays under 7 days.
- Intake forms sent at booking, completed before arrival. Patients who arrive to a clipboard and a 20-minute wait start the relationship in a hole (operators report, 39).
- Clear location page: parking, entrance, accessibility. A PT practice inside a great gym struggled because of parking and downtown traffic (operators report, 268).

## Waitlist and "book later"

When the first slot is too far: "I can add you to our cancellation list and also hold [later slot] so you have something confirmed. Would you like both?" Text waitlisted patients first-confirmed-wins when a slot opens.

## Weekly intake review (agent routine)

1. Inquiries by source, answered rate, median reply time.
2. Qualified to booked, booked to attended, by source and by clinician.
3. Open inquiries older than 24 hours with no state: work them today.
4. Lost reasons count: if "no availability soon enough" leads, the problem is capacity, not marketing.
5. New-patient lead time per clinician.
