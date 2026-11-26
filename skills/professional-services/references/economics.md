# Economics: formulas with worked examples

Compute these before recommending spend, pricing or channel changes. Every report gives money, not percentages. Inputs come from the practice management system (Clio, TaxDome, Karbon, Canopy, Redtail, Wealthbox, AMS360, HawkSoft), the bank or billing export, and the ad accounts.

## 1. The funnel, by source and by intake person

```
inquiries > contacted > qualified > consult held > proposal/engagement sent > signed > paid
```

Every lead ends in one state: booked, nurturing, disqualified (reason), lost to competitor, unreachable, duplicate, conflict, spam. Without states, cost per lead looks fine while signed cost explodes.

Worked example (law, Pareto Legal 2026 sample): Search CPL $92 vs LSA $192 makes Search look twice as good. After intake, signed-case CAC was $3,812 for Search and $2,354 for LSA. A firm optimizing on CPL would have cut its cheaper channel.

## 2. Signed-client CAC and payback

```
signed CAC = (media + agency + software + intake labor share) / signed clients
first-year gross margin = first-year fees collected x (1 - direct labor % - pass-through costs %)
payback months = signed CAC / (first-year gross margin / 12)
```

Example (family law, operators report r/LawFirm 126): $7,500/month ads + $800 management. If 10 signed clients a month at a $7,000 to $8,000 eventual case value, signed CAC = $830 and each case covers its cost about 9x over its life. If attribution shows only 4 signed, CAC = $2,075; still viable. If 1, kill or fix intake. The owner reported collections without attribution: compute it before raising budget.

## 3. CPL ceiling (insurance, advisors, consumer law)

```
revenue per sale = average premium or fee x commission rate (or first-year fee)
max CPL = revenue per sale x lead-to-sale rate x share of revenue you will spend on acquisition
```

Example (r/InsuranceAgent 37, illustrative): $4,500 annual premium x 230% first-year commission = $10,350 per sale. At 20% lead-to-sale the revenue-only ceiling is $2,070; at 5% it is $517.50. Spend at most a third of that to leave room for chargebacks and overhead: $690 and $172.

## 4. Insurance net commission after chargebacks

```
deposited commission = annual premium x carrier product split x IMO split x upfront advance % x (1 - fallout and chargeback %)
net = deposited commission - lead spend - dialer and admin
```

Example (r/InsuranceAgent 72): $50,000 AP x 85% x 90% x 75% x 75% = $21,516, minus $7,000 leads = $14,516. The same agent sold 30+ policies in two months, deposited about $10,000 and spent $13,000 on leads: about -$3,000 before other costs. A showcased "$1M producer" reportedly spent $250,000 on leads with 30 to 40% fallout and netted $150,000 to $200,000 (r/InsuranceAgent 58). Rule of thumb from operators: budget 25% chargebacks and at least 25% marketing before calling deposits income (r/InsuranceAgent 134).

Internet P&C leads (captive agent, r/InsuranceAgent 42): $4 to $7 per lead, 1.5% close, $265 to $465 per sale, 85% bundled. Viable only because of bundling and renewal; recompute with the agent's own commission and retention.

## 5. Realization-based fee increases (accounting, tax, bookkeeping)

```
realization = fees collected / (all hours incl. unbilled x internal standard rate)
increase % = average target, tilted by realization band
```

Example (operators report, r/taxpros 111): target average 25%. Under 70% realization: +30%. Over 150%: +20%. In between: judgment. Nobody below 20%, including easy, loyal, long-standing clients, so annual increases become expected before they are needed. Internal standard rate $260 while billing new clients $320/hour; revenue doubled in five years with fewer billable hours.

Break-even check before a raise: you can lose `p / (m + p)` of clients and keep the same gross profit, where p = price increase % and m = current margin %. At a 50% margin, a 25% raise survives losing a third of the affected clients. Practitioners report losing 3 of 100 after tripling, and only a handful of 80 after +50% (r/taxpros 155).

## 6. Volume vs minimums

```
revenue = returns x average fee;  workload and liability scale with returns
```

Example (r/taxpros 92): $500,000 = 2,000 returns at $250 or 1,000 at $500. The second firm has half the relationships, half the e-file exposure and room for advisory. One EA with 550 clients for $120,000 in revenue named early underpricing as the root problem (r/taxpros 75).

## 7. Bookkeeping quote

```
monthly fee = hours per month (from 3 months of real data or a books review) x target hourly rate, rounded to a package
sanity check = monthly fee / client monthly revenue (target about 2%, operators report r/Bookkeeping 216)
cleanup = 12 x monthly fee x (1.10 to 1.25)   (r/Bookkeeping 89)
```

Example: a $600 flat fee priced at a $125/hour internal target for a solo service business that rarely needs more than 5 hours (r/Bookkeeping 51). Two owners running about 30 such clients reported $275,000 gross on 45 to 50 combined hours a week.

Scope creep check (r/Bookkeeping 36): quoted $1,700/month at 1.5 hours a week; real work reached 5 hours a week once weekly reconciliations, Slack requests and a 3-day close deadline appeared. Effective rate fell from about $260 to under $80 an hour. Reprice at the 90-day review.

## 8. Adviser economics

```
first-year fee (AUM) = assets x blended fee
household value = annual fee x expected years retained x margin
max CAC = household value / 3 (conservative) ; compare with Kitces medians by client size
```

Example: $1M at 1% = $10,000/year; 10 years at 50% margin = $50,000 value; a $15,447 seminar CAC is defensible, a $48,836 social CAC is not. Kitces 2026 shows CAC rises with client value ($1,720 for clients under $3,000/year, $17,500 for $20,000+/year): a high CAC can be rational.

Seminar class math (operators report, r/CFP 111): 10,000 mailers ($10,000) + room ($2,000) + books ($700) = $12,000 to $15,000 per two-evening class. 10 to 30 households register at $50; about 80% book a lab session; about 40% qualify; about 70% of plan meetings sign. Average class produced $45,000 in annual recurring revenue. Payback in 4 months of fee revenue.

Meta VSL funnel (r/CFP 158): about $3,000 spend for 39 booked appointments ($77 each); 28 appointments in 30 days at $96. Unknown close rate: compute cost per funded household before scaling.

## 9. Buying a book of business

```
price = revenue multiple x recurring revenue retained
real cost per retained dollar = price / revenue still there after 12 months
```

Examples: tax book bought at 75 cents per dollar of revenue, paid over 4 years, grew to $1.2M revenue with 45% margin before owner pay (r/taxpros 99). Advisory books at 2x revenue, seller-financed over 5 years (r/CFP 52, 392). Buyers ask for first-year clawbacks tied to client departures (r/CFP 41, 82 upvotes on the advice). Seller-facilitated intergenerational transitions reported 93% asset retention vs low 80s for outside purchases (operators report, r/CFP 392).

## 10. LSA and Search for lawyers

```
LSA cost per signed matter = LSA charges (after credits) / signed matters from LSA
Search cost per signed matter = (spend + management) / signed matters from Search
```

Report both by practice area monthly. Missed business-hours calls held over 20 seconds can be charged on LSA (Google): an unanswered phone is a direct cost, so compute `answer rate x signed rate` before raising the LSA budget.

## 11. Capacity

```
capacity hours = staff x available hours x (1 - admin share)
committed hours = recurring clients x average monthly hours + seasonal work
headroom = capacity - committed ; throttle acquisition below 10% headroom
```

Advisers: one advisor is often quoted at 150 to 200 relationships (r/CFP 55, 25 upvotes); a reply favored about 70 clients averaging $1.5M. Use the firm's own service model, not the rule of thumb.
