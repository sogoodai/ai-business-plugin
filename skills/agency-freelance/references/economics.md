# Economics: what to compute before recommending anything

Compute from the owner's own records (invoices, time tracker, CRM or a spreadsheet of the last 12 to 24 months). Report gaps in money and in founder hours, not percentages.

## The base table

Build one row per client: source (referral, past client, inbound, outbound, marketplace, partner, content), service, industry, start and end date, total billed, hours spent (or estimate), fees paid to platforms, status, churn reason, expansions, referral given (yes or no).

## Formulas

```
effective hourly rate (EHR) = revenue from a client / all hours spent on that client (sales, calls, revisions, reporting, admin)
billable utilization = billable hours / available working hours           (solo: 50 to 65% is realistic; selling and admin eat the rest)
required hourly rate = (target owner pay + overhead + tools + taxes + profit) / realistic billable hours per year
realistic billable hours (solo) = 46 weeks x 40 h x 0.55 = about 1,000 h
client concentration = largest client revenue / total revenue           (over 30 to 40% = one email from a crisis)
gross margin per client = (revenue - contractor and staff delivery cost - client-specific tools) / revenue
channel CAC = (spend + paid tools + platform fees + founder sales hours x EHR) / clients won from that channel
client lifetime value = average monthly gross margin x average tenure in months
LTV / CAC by channel; payback months = CAC / monthly gross margin
proposal win rate by source = proposals accepted / proposals sent, split by source
pipeline needed = monthly new revenue target / (average deal size x win rate)
meetings needed = proposals needed / meeting-to-proposal rate
outbound prospects needed = meetings needed / (positive reply rate x positive-to-meeting rate)
marketplace effective take = (platform fee + Connects or boosts + payment fees) / gross billed
retainer scope check = monthly fee / required hourly rate = hours actually bought per month
```

## Worked examples

**Required rate.** Target pay $90,000, overhead and tools $12,000, taxes about 30% of profit, profit buffer $10,000. Before tax about $160,000 needed. 1,000 billable hours gives $160 per hour. Quoting $75 because "that's what Upwork shows" means working twice as many hours for the same life.

**The $400 retainer trap.** To net $75 an hour you bill about $100 after overhead (operators report). A $400 a month client buys 4 hours of everything: calls, reporting, revisions, posting. If the scope sheet implies 12 hours, the EHR is $33.

**Effective hourly rate by client.** Client A pays $3,000 a month and takes 20 hours: EHR $150. Client B pays $5,000 and takes 60 hours with weekly calls and unlimited revisions: EHR $83. B looks like the better client on revenue and is the worse one. Rank clients by EHR and gross margin, then reprice or replace the bottom fifth.

**Proposal math.** Target $15,000 of new monthly revenue at $3,286 median accepted value (Nusii agency median, 2025 data) is about 5 wins. At the 47.7% agency acceptance rate that is 10 proposals. With a 50% call-to-proposal rate, 20 qualified calls a month. If the owner has 4, the plan must change (deal size, past clients, partners), not just "more outreach".

**Outbound volume.** 20 calls a month from cold email at 0.79% positive reply per prospect (Smarter Outbound median, 2026) and half of positives booking: 20 / (0.0079 x 0.5) = about 5,000 prospects a month. At top-quartile 1.36%: about 2,900. That is why list quality and past clients come first for a solo operator.

**Past clients versus cold.** Past-client proposals accept at 71.8% vs 43.6% for new (Nusii, 2025 data). Ten reactivation conversations that produce 3 proposals yield about 2 wins; matching that cold needs about 5 proposals and the calls behind them.

**Marketplace channel P&L.** $100,000 billed: Fiverr seller fee $20,000; Upwork at 15% $15,000; Upwork Direct Contract $5,000; Contra $0 before processing. Add Connects: 30 proposals a week at an assumed 16 Connects each (the real number varies by job) is 480 Connects, $72 a week, about $3,700 a year, plus proposal-writing hours. Upwork can still be the cheapest channel if it closes; measure it.

**Price raise break-even.** You can lose p / (m + p) of volume before profit falls (m = contribution margin, p = raise). Service work often has 50 to 70% contribution on owner time. A 25% raise at 60% margin survives losing 29% of clients, and the ones who leave are usually the most revision-heavy (see `offers-pricing`).

**Retainer LTV and referral value.** $2,500 a month at 55% margin = $1,375 a month. Twelve months = $16,500. Referral clients stay 1.9x longer (Promethean 2026): about $31,000. A partner who sends 3 a year is worth more than most ad budgets a solo agency can afford.

**Ad-spend fee model.** 10% of $20,000 spend = $2,000; the same client at $5,000 spend pays $500 for the same account work. Add a minimum ($1,500 to $2,000 plus a percentage above a threshold is a common practitioner structure).

## Client health score (0 to 10, review monthly)

- Agreed KPI tied to revenue or pipeline exists and is reported: 2
- Last measurable win within 60 days: 2
- Main stakeholder replies within 2 business days: 1
- No open access or dependency blockers: 1
- Business review held in the last quarter: 1
- Paid on time, last 3 invoices: 1
- Scope used within 10% of what is paid: 1
- Expansion or referral discussed this quarter: 1

7 to 10: ask for referral or case study. 4 to 6: fix the lowest item this month. 0 to 3: owner call this week, with a plan, before the client raises it.

## Weekly dashboard

Qualified opportunities created, positive reply rate, meetings held, meeting to proposal, proposal to win by source, average contract value, gross contribution after channel fees, sales cycle days, founder hours per win, expansion revenue, at-risk clients, referral introductions. Opens, followers and impressions are diagnostics only.
