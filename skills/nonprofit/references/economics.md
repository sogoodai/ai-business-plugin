# Economics: formulas with worked examples

Compute from a gift-level export (donor ID, date, amount, source, payment method, recurring flag, campaign). Never from a summary. If the CRM only stores totals, ask for the payment processor export instead.

## 1. Retention, the right way

```
overall retention (year Y) = donors in Y who also gave in Y-1 / donors in Y-1
new-donor retention = donors whose first gift was in Y-1 and who gave in Y / first-time donors in Y-1
repeat-donor retention = donors who gave in Y-2 and Y-1 and gave in Y / donors who gave in Y-2 and Y-1
recapture rate = lapsed donors (gave before Y-1, not in Y-1) who gave in Y / lapsed pool
```

Report new and repeat separately. A blended 45% can hide a 20% new-donor rate behind a loyal core.

**Worked example.** 800 donors last year, 300 of them first-timers. This year 70 of the 300 gave again (23%) and 320 of the 500 repeat donors gave again (64%). Blended: 390 / 800 = 49%. The fix is the first-gift journey, not the loyal core. Each extra 10 points of new-donor retention on 300 first-timers is 30 donors; at $183 a year (M+R 2026 one-time median) that is $5,490 a year, compounding.

**First-to-second gift rate** is the faster signal: first-time donors in a monthly cohort who make a second gift within 90 and 365 days. Use it to judge the first-gift journey within one quarter, not one year.

## 2. Donor value by source

```
first-year value = revenue from cohort in first 12 months / donors in cohort
12-month cohort value (simple) = first-year value + (new-donor retention x average repeat-year revenue)
3-year value = sum of cohort revenue over 36 months / donors in cohort   (use real data once you have it)
monthly donor value = monthly gift x expected months; expected months from M+R curve: 10% gone by month 2, 71% active at 12, then 1 to 2% lost a month, about half active at 24
```

**Worked example, monthly.** $20 a month. Months 1 to 12 average about 82% active: 12 x $20 x 0.82 = $197. Months 13 to 24, starting at 71% and ending near 52%: about 12 x $20 x 0.61 = $146. Two-year value about $343 per sustainer signed, versus about $183 a year from a one-time-only donor (M+R 2026). Use the organization's own curve once 12 months of data exist.

## 3. Cost per donor, not cost per lead

```
cost per new donor = channel spend (media + fees + staff time) / new donors from channel
payback months = cost per new donor / average monthly revenue per new donor
acquisition ROI at 12 months = (12-month cohort revenue - acquisition cost) / acquisition cost
```

**Worked example, Meta.** $3,000 spend, 820 leads at $3.66 (near the M+R $3.64 Meta CPL), 9 donors from those leads in 90 days. Cost per donor $333. If the same $3,000 optimized to donations produces 30 donors at $45 average, cost per donor is $100 and first-gift revenue $1,350. The NextAfter test found a 347% worse cost per donor for lead optimization (2026). Report both lines.

**Acquisition mail.** Prospect mail returns $0.41 per $1 on the first gift (M+R 2026). Do not kill it on that. Kill it when 12 to 24 month cohort value after retention is below cost. With active-donor mail at $4.51 per $1, a prospect cohort that renews at 30% can still be worth buying.

## 4. Event net and net per staff hour

```
direct costs = venue + food + entertainment + printing + platform and card fees + auction items bought
staff cost = staff hours x loaded hourly cost (wage x 1.25 for taxes and benefits if unknown)
event net = gross - direct costs - staff cost
net per staff hour = event net / staff hours
cost to raise $1 (event) = (direct costs + staff cost) / gross
new-donor value = new donors acquired x 12-month cohort value
```

**Worked example.** Gala grosses $320,000, direct costs $145,000, net $175,000 before staff (operators report, 180 upvotes). Two staff for 8 weeks at 50 hours and $40 loaded: 800 hours, $32,000. Event net $143,000, $179 per staff hour, cost to raise $1 = $0.55. Compare: a focused major-gift push with the same 800 hours, 40 meetings, 10 gifts at $10,000 = $100,000 at $125 per hour, with no venue risk and higher next-year retention. The gala wins here only if it also produces new major prospects. Count them.

Event cost to raise $1 of $0.50 or more is common and fine when the event is a cultivation tool, but then it belongs in the acquisition budget, not the net-revenue column.

## 5. Grant expected value and pipeline coverage

```
fit score (0 to 100) = mission fit 30 + funds peers like us 25 + geography and eligibility 15 + amount fit 15 + relationship 15
win probability = cold competitive 0.10 to 0.15; pre-called with positive signal 0.25 to 0.35; invited or renewal 0.5 to 0.8 (internal priors: replace with own history after 20 decisions)
expected value = ask x win probability
hours budget = expected value / target dollars per writing hour
pipeline coverage = sum of expected value of qualified prospects / annual grant target   (aim for 1.0 or more, plus 3x in raw asks)
```

The 0.10 to 0.15 cold prior comes from Instrumentl's 14% cross-sector rate (2026, vendor); the higher bands are planning assumptions, not benchmarks. Applications under the fit threshold (for example 60) do not get writer time.

**Worked example.** $25,000 ask, fit 72, cold: EV $3,000. If writing takes 20 hours, that is $150 an hour. A $5,000 renewal at 0.8 that takes 4 hours: EV $4,000, $1,000 an hour. Renewals and reports first, always.

## 6. RFM plus engagement score for major-gift prospects

Score every donor 1 to 5 on each, then add engagement points:

```
Recency: last gift <3 months 5, <6 4, <12 3, <24 2, older 1
Frequency: gifts in 3 years: 6+ 5, 4 to 5 4, 3 3, 2 2, 1 1
Monetary: largest single gift by file quintile (top 20% = 5)
Engagement: +2 volunteer, +2 event attendee, +2 board or staff relationship, +1 opened 3+ updates, +3 said "tell me more" or asked a question, +2 DAF or stock gift, +2 business owner or foundation trustee (public info only)
priority = R + F + M + engagement; top 25 (top 50 if a staff member owns it) get a named next step
```

Wealth screening alone produces "high-capacity strangers". One operator's $5 donor screened at $15M to $20M turned out, per the ED, likely to be a vendor fishing for a sale (93 upvotes). Screen only people who already show engagement.

**Ask size.** Common practice: 3 to 5x the largest previous gift, capped by what you know of capacity, tied to one project (wonsukchoi/domain-experts fundraiser skill, MIT). A specific number beats a range: ranges pull to the low end.

## 7. Gift range chart for a campaign

Rule: the lead gift is 10 to 20% of the goal; each tier below doubles the count and halves the size; the top 10 to 15 gifts bring 50 to 60% of the goal; and you need 3 to 5 qualified prospects per gift in the top tiers (gift-table practice; see wonsukchoi/domain-experts, MIT).

**Worked example: $150,000 van and kitchen campaign.**

| Gift | Count | Total | Cumulative | Prospects needed |
|---|---|---|---|---|
| $25,000 | 1 | $25,000 | 17% | 3 to 4 |
| $10,000 | 3 | $30,000 | 37% | 9 to 12 |
| $5,000 | 6 | $30,000 | 57% | 18 to 24 |
| $2,500 | 10 | $25,000 | 73% | 30 |
| $1,000 | 20 | $20,000 | 87% | 60 |
| under $1,000 | about 100 | $20,000 | 100% | the list |

If the file cannot name 3 people for the $25,000 line, the goal is wrong. Do not go public until 50 to 60% is committed; the first public gift anchors every later ask.

## 8. Recurring program math

```
recurring share = active monthly donors / active donors (median org about 4%, GivingTuesday 2025)
monthly revenue run rate = sum of active monthly gifts
net recurring growth = new sustainers - cancelled - failed-and-not-recovered
failed payment recovery rate = recovered failed charges / failed charges
upgrade rate = sustainers who raised their amount in 12 months / sustainers active 12 months
```

**Worked example.** 1,200 active donors, 50 monthly at $18 average (4%). Moving to 10% (120 sustainers) with a monthly-first form and a post-gift upgrade adds 70 x $18 x 12 = $15,120 of annual run rate, about $10,000 to $11,000 of it retained in year 2.

## 9. Google Ad Grants math

```
grant utilization = grant spend / $10,000 (a limit, not a target)
account CTR (monthly) = clicks / impressions, must stay at 5%+
cost per meaningful conversion (grant $) = grant spend / primary conversions
mission value per month = sign-ups x value + volunteer leads x value + service requests x value + donations
```

M+R 2026: 229 visits per $1,000 of grant spend, $793 of grant per donation, $0.17 back per grant dollar. A $10,000 month at those medians is about 2,290 visits and about 13 donations. The win is the 2,000+ other visits: service requests, volunteers, sign-ups that later give. Put a value on each so the account optimizes to something real.

## 10. Card fees and platform choice

```
net per gift = gift - (card % x gift) - fixed fee - platform % - currency fee
net per ticket = price - all fees absorbed by the org   (compare at your real price point)
```

At small amounts fixed fees dominate: a $7 ticket nets $7.00, $6.50 or $5.54 depending on platform (operators report, 78 upvotes, historical fees). "Free" platforms that ask donors to tip the platform shift the cost to the donor and can depress conversion; check the default tip and whether it can be set to zero. Offer donors the option to cover fees, unchecked.
