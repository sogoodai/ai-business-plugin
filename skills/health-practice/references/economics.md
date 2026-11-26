# Economics: formulas with worked examples

Every formula here is a management formula, not a published benchmark. Use the clinic's own numbers; benchmarks in [benchmarks.md](benchmarks.md).

## 1. The revenue identity (NP x PVA x OVA)

```
monthly new-patient revenue = new patients x visits per case (PVA) x collected per visit (OVA)
PVA quick = visits in period / new patients in period   (use 6 to 12 months)
PVA true  = visits in period / unique patients seen in period
OVA = collections / visits   (collections, never charges or UCR)
```

Worked (chiropractor's series, operators report, 52 and 39):
- NP chaser: $5,000 marketing, 30 NP x 4 visits x $30 = $3,600. Paying to work.
- Systems doc: $1,000 marketing, 10 NP x 20 visits x $70 = $14,000.
- Same doctor, 30 NP and $75 OVA: PVA 4 = $9,000; PVA 9 = $20,250. +$11,250 a month, $135,000 a year, no extra spend.

Agent rule: compute all three before recommending any acquisition spend. If PVA sits well below the clinic's own planned visits per case, or OVA is falling while visits hold, fix those first.

Applies by name to chiro; the same identity holds for PT (visits per case x net revenue per visit), acupuncture (visits per course x price), therapy (sessions per client x net per session), dental (production per patient per year x collection rate).

## 2. Contribution per clinical hour by payer

```
contribution per hour = net collected per session x sessions per hour
                        - billing cost (staff time or % fee)
                        - expected denial and write-off
                        - acquisition cost per session (channel CAC / expected sessions per client)
```

Worked (therapy, illustrative inputs):
- Plan A pays $95 for a 53-minute session, billing service 6% ($5.70), 3% write-off ($2.85), CAC near $0 (panel sends referrals): about $86.
- Cash at $160, card fees 3% ($4.80), CAC $300 spread over 12 sessions ($25): about $130.
- Cash at $160 but only 6 sessions per client on average: CAC $50 a session, about $105.
- Conclusion: cash wins only while cash demand fills the hour. If cash leaves 4 hours a week empty, the empty hours cost $0 x 4 against plan A's $344.

Score each plan on net collected rate, days to payment, denial rate, prior-auth burden, referral volume, and retention of those patients. Drop the worst plan only when its hours can be refilled at a higher contribution within the notice period.

## 3. Attended-patient CAC and 90-day contribution

```
attended-patient CAC = channel spend / attended first visits from that channel
90-day contribution ratio = contribution collected from that cohort in its first 90 days / acquisition cost
capacity-adjusted value = contribution per visit x expected completed visits x P(attend) x P(complete)
```

Worked: dental median CPL $84.77 (LocaliQ 2025). 50% attend = $169.54 attended CAC. If a new dental patient produces $600 collected in 90 days at 60% contribution = $360, ratio 2.1. Mental health median CPL $141.17 with 25% becoming attended intakes = $565 per intake; at $100 net per session and 60% contribution it needs 9.4 sessions just to break even.

## 4. Directory payback

```
monthly directory value = attended new clients from directory x contribution per client over expected stay
payback months = listing cost / monthly contribution from directory clients
```

Psychology Today at $29.95 a month: one retained client at 15 sessions x $60 contribution = $900, about 30 months of listing. Track: profile views (diagnostic), inquiries, fit inquiries, consults booked, intakes attended, clients at session 4.

## 5. Zocdoc bid ceiling

```
max sponsored bid = expected contribution per new patient x acceptable marketing share
                    - discovery booking fee - expected no-show loss
expected no-show loss = P(no-show) x (booking fee already paid + value of the empty slot)
```

Worked: PT visit reason with 8 expected visits x $45 contribution = $360. Accept 25% marketing share = $90. Booking fee $60, no-show 10% x ($60 + $45) = $10.50. Ceiling about $19.50 per booking. A one-off visit reason with $45 total contribution has a negative ceiling: do not sponsor it. Zocdoc charges the booking fee even when the patient no-shows (Zocdoc 2026).

## 6. Recall and reactivation value

```
recall value = overdue patients x reactivation rate x visits per year x net per visit
hygiene reappointment gap = (target rate - current rate) x hygiene patients per year x value per hygiene visit
```

Worked: 1,200 active hygiene patients, reappointment 65% vs 80% target. 15 points x 1,200 = 180 extra pre-booked visits a year. At $180 net = $32,400, before any treatment found at those visits.

Dormant list (operators report, 131): 1,000 old leads, email and SMS, 15 booked in 2 weeks (1.5%). Cheap to run; never skip it before new ads.

## 7. Cancellation and no-show leak

```
monthly leak = (no-shows + late cancels not refilled) x average net per visit
recovered cancellation rate = refilled cancelled slots / cancelled slots
```

Worked with Planet DDS 2025 rates on 1,000 scheduled visits: 144 advance cancellations and 62 no-shows. Refill half the cancellations and the leak falls from 206 to 134 visits a month.

## 8. Time-of-service discount check

Keep TOS discounts around 5 to 15% and tied to billing savings (OIG opinion via trade-law commentary). Over about 20% starts to look like a dual fee schedule. Never bill an insurer a higher fee than the cash fee for the same service. Prefer a documented hardship policy or a discount medical plan organization. Confirm with counsel per state.

## 9. Rent and space (PT, chiro, acupuncture, therapy starters)

```
rent per session = monthly rent / sessions per month
```

A PT starter caps one room at about $700 a month and limits percentage-of-revenue rent to the first 3 to 4 months: $15 a session at 15 sessions a week is about $1,000 a month (operators report, 268). Parking and easy access beat a great gym with downtown traffic (same thread). Chiro micro practice opened for $8,000 on a credit card, $4,000 possible without new equipment (operators report, 65).

## 10. Caseload math (therapy)

```
weekly sessions needed = target annual take-home / (net per session x working weeks x (1 - expense ratio) x (1 - tax rate))
```

Worked: $100,000 take-home, $110 net per session, 46 weeks, 25% expenses, 25% tax: 100,000 / (110 x 46 x 0.75 x 0.75) = 35 sessions a week. Matches the recruiter's report that $100,000+ needs 28 to 35 clients a week (operators report, 968). At under 20 sessions, plan on $50,000 to $80,000 unless rates are high: an in-network therapist reports $80,000 net at under 20 sessions billing herself (733); an Alberta psychologist at $220 an hour sees 15 to 25 a week (873).

## 11. Review gap

```
review gap = top-3 competitor median review count - your count
months to close = review gap / (monthly patients x request rate x review rate)
```

Depth and review-rate data: `local-seo`.
