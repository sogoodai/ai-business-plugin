# Economics: compute before recommending

Pull 12 months from the software: leads with source and timestamps, bookings, attendance per visit, sales, cancellations with reason, freezes, failed payments, refunds. If the owner has nothing, use one typical month and label every result an estimate. Never put acquisition on a screen without churn next to it.

## Churn and retention: get the unit right

```
monthly churn = members who stopped paying in month / active paying members on day 1 of month
monthly retention = 1 - monthly churn
annual retention from monthly = (monthly retention)^12
monthly churn from annual = 1 - (annual retention)^(1/12)
```

- HFA's 66.4% annual retention (2024 data) equals about 3.4% monthly churn. Two-Brain's 92.7% monthly retention equals 40% of a cohort left after 12 months. Big-box and coaching-gym numbers are not comparable; never call a microgym "bad" against HFA.
- **Split churn into four:** voluntary cancel, failed payment (involuntary), freeze that never resumed, and planned completion (a 12-week program that ended as agreed). Only the first three are churn.
- **Early-life vs mature.** Track cohort survival at day 30, 60, 90 separately from churn among members past month 3. Two-Brain's 7.3% monthly loss and 20.7-month median engagement only fit together if early churn is much higher than mature churn. If the first 90 days are poor, no ad fix will repair the economics.
- **Behavioral churn comes first.** Attendance falls before billing stops. Compute a weekly at-risk list from visits, not from cancellation requests ([retention.md](retention.md)).

## LTV: use the survival curve, not 1/churn

```
simple LTV (revenue) = monthly price / monthly churn          (only if churn is flat; it is not)
cohort LTV = sum over months m of (share of cohort still paying in m x average revenue in m)
contribution LTV = cohort LTV x contribution margin
contribution margin = (revenue - coach pay for delivery - card and platform fees - aggregator fees) / revenue
```

- Worked, flat-churn shortcut: $179 a month at 7.3% churn = $2,452 revenue LTV (13.7 months). At 6.3% = $2,841. One point of churn is worth about $390 per member.
- Worked, survival curve: Coachway's online coaching curve (94% M1, 82% M3, 65% M6, 45% M12) implies about 8.5 paid months in year one per client (sum of the month-start survival, interpolated between the published points). At €181 that is about €1,540 of first-year revenue per client. A "median tenure x price" figure of €579 (3.2 x €181) understates it because recent clients are still active. Derived numbers, label them so.
- Operators report a training gym at about $1,800 client LTV with small-group training graduating into access memberships (r/smallbusiness, 535), and a PT with a four-year average client tenure (r/personaltraining, 82).
- Value owner hours. A studio "making 59% margin" while the owner delivers half the sessions is paying the owner nothing for that work (r/personaltraining, 83; a commenter also found a $1,200 a month arithmetic error in the same post).

## The value of one point of retention

```
extra members at month 12 = cohort x (r_new^12 - r_old^12)
12-month revenue gain = simulate month by month: members(m+1) = members(m) x retention + new joins(m); compare total revenue at r_old and r_new
```

- Two-Brain's model: 100 members at $179, monthly retention 92.7% to 93.7%, about 12 more clients kept across the year and about $26,000 of annual revenue (Nov 2026, scenario math).
- On a single cohort of 100: 40.3 left after 12 months at 92.7% vs 45.8 at 93.7%.
- Rule: before approving new ad budget, show the owner the dollar value of 1 point of retention next to the cost of the new members that budget would buy.

## The lead funnel and CAC

```
set rate = booked / leads           show rate = attended / booked
close rate = bought / attended      lead-to-member = set x show x close
member CAC = spend / new paying members      max member CAC = contribution LTV x share you accept (start at 30%)
max CPL = max member CAC x lead-to-member
```

- Worked: Two-Brain medians (33.3% set) x Keepme show (75%) x Two-Brain close (62.5%) = 15.6% lead-to-member. Keepme's paid funnel is 3 to 6% because 57% of leads never get a reply.
- Same $27.11 Meta lead: $174 per member at 15.6%, $452 to $904 at 3 to 6%. Same $67.36 Search lead: $432 at 15.6%, $1,123 to $2,245 at 3 to 6%. Fixing reply speed is cheaper than any ad optimization.
- Worked max CPL: $2,452 revenue LTV x 70% margin = $1,716; accept 30% = $515 max CAC; at 15.6% lead-to-member, max CPL = $80. At 4%, max CPL = $21, below the Meta median. The follow-up decides whether ads are viable at all.
- Measure by source. A campaign with a higher CPL but twice the show and close rate is cheaper per member. Google-sourced in-home PT clients stayed longer than social or word of mouth for one operator (r/personaltraining, 99).

## Intro offer economics

```
intro conversion = intro buyers starting a recurring plan within 14 days of intro expiry / intro buyers
intro yield = (intro revenue + recurring revenue from converters over 90 days) / intro buyers
90-day retained intro customers = converters still active at day 90 / intro buyers
```

- The KPI is not intro revenue. Track intro purchase, first visit, second visit, target visit frequency, recurring purchase, 90-day retained (Mindbody added Intro Offer analytics in July 2026 for this reason).
- Compare free vs paid intros on retained contribution per lead, not on signups.

## Studio capacity and class economics

```
class fill = attendees / capacity, per class-hour (day x time x instructor)
contribution per class-hour = class revenue attributed - instructor pay - variable cost (heat, towels, consumables)
revenue per visit = membership revenue / member visits + drop-in and pack revenue / their visits
```

- Average studio sells under 36% of listed capacity through its own channels (ClassPass data, vendor). Median by class-hour hides the problem: 6 pm Tuesday full and 4 pm empty need opposite actions.
- Operators report 4 pm yoga slots "desolate" while 5:30 and 7 pm fill, and 4:30 drawing a third of morning attendance (r/YogaTeachers, 60). Move or cut weak slots at the next schedule change, not by cancelling booked classes.
- Membership revenue per visit falls as a member attends more. That is the goal (attendance retains), so watch revenue per member and contribution per class-hour, not revenue per visit alone.

## Packs vs memberships

```
effective price per visit (pack) = pack price / visits actually used before expiry
membership breakeven visits = monthly membership / drop-in or pack per-visit price
```

- Flag any customer whose pack use makes the membership cheaper over the same rolling month, and trigger a membership conversation. Leave genuinely irregular customers on packs.
- Unused pack visits are revenue now and resentment later. Trainers dropped packs because clients hoarded sessions, rushed before expiry or felt awkward renewing (r/personaltraining, 309).

## Personal trainer capacity

```
required hourly rate = (target take-home + annual costs + taxes) / realistic billable hours a year
coach-hour contribution = session revenue - gym rent or cut per hour - travel time valued - card fees
roster risk = share of monthly revenue from the top 3 clients
semi-private wins if: price per person x average occupied seats - extra delivery cost > displaced 1:1 hour revenue
```

- Rent: one LA studio charges $20 an hour capped at $1,500 a month; another trainer paid $42,000 a year ($3,500 a month) at his gym (r/personaltraining, 285). Negotiate a monthly cap before you build volume.
- Thirty-minute sessions twice a week let a YMCA trainer carry 20 to 24 clients instead of 10 to 12, so losing 1 to 3 clients no longer removes a quarter of income (r/personaltraining, 87).
- Overload costs money too: at 28 clients service slipped and clients left about 3 months later; after a raise the roster settled at 19 with slightly lower take-home and a sustainable week (r/personaltraining, 56).

## Online coaching workload

```
effective hourly = monthly price x clients / hours spent per month
check-in load = clients x minutes per check-in x check-ins per month
```

- $50 a month x 15 clients at 20 hours a week is about $8.70 an hour (r/personaltraining, 95). Raise the price or cut the deliverables before taking more clients.
- Weekly check-ins run 10 to 15 minutes per client once the process is set (operators, 184 and 50). At 30 clients that is 5 to 7.5 hours a week before programming and messages.
- Onboarding is front-loaded: about 3 hours in a client's first week, then little (operator at $525 a month, 89).

## Fees, failed payments and contracts

- Get the effective processor rate from 3 months of statements: total fees / total volume. A gym was pitched about 5% of gross and paid close to 10% once all contract fees landed (r/smallbusiness, 1,353; top comment 1,089 agreed).
- Discounted annual plans hide involuntary churn: about 23% of one gym's annual members stopped paying within 4 months on failed cards (same thread). Card updater, retries and dunning before launch; flows in `email-sms-loyalty`.
- An independent trainer absorbs 2.9% + $0.30 card fees rather than passing them on; the time saved chasing payments outweighed them (r/personaltraining, 309).
- Taking over a gym: forecast without the old members. A 20-year-old gym's members had joined elsewhere; the reopening reached 400 of a 750 target (r/smallbusiness, 1,353).
