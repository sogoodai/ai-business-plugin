# 90-day outbound plan

For a small company starting outbound or restarting a stalled program. The order comes from the research: system before sending, prove one message-market pair, add channels with a job, then scale winners. **First raise expected value per prospect, then raise the number of prospects.** Each phase ends with a short owner report: what changed, the scorecard, what the owner must decide.

## Before day 1: owner questions

1. What do you sell, at what price, and what does one customer's first year earn you?
2. Who bought in the last 12 months (export closed-won and closed-lost)?
3. Which countries, and are buyers companies or sole traders?
4. Which domains and inboxes exist; has anything been sent cold from the main domain?
5. Who can send (founder, rep, agent drafts only)? Who approves claims and offers?
6. Will you take calls? Is LinkedIn the founder's personal asset?
7. Tools and data already paid for (CRM, Apollo, Sales Navigator, dialer)?
8. What will you never do (calls, free work, discounts, guarantees, certain countries)?

## Days 1 to 14: build the system, send nothing cold

**Week 1: ICP and scorecard.**
- Segment past wins and losses; write the ICP as filters plus disqualifiers ([lists-and-signals.md](lists-and-signals.md)).
- Pick 2 to 3 triggers that plausibly cause the problem you solve. Write the "why now" for each.
- Choose one benchmark definition and set up the scorecard: delivered, replies, positive replies, meetings booked, meetings held, opportunities, pipeline, bounce, complaints and opt-outs, cost per held meeting. No open rate.
- Warm list first: message every past client, ex-colleague and lost "not now" deal individually. "5 warm texts beat 50 new cold emails" (r/agency 76).

**Week 1 to 2: infrastructure** ([infrastructure.md](infrastructure.md)).
- 2 to 5 secondary domains, 2 to 3 inboxes each, SPF, DKIM, DMARC, Postmaster and SNDS. Warm 14 to 21 days.
- Opt-out line, postal address, suppression list keyed on email, LinkedIn URL and phone, shared by every tool.
- Cross-channel stop: any reply on any channel pauses all sequences for that person.
- LinkedIn profile rewritten as a landing page.

**Week 2: first cohort.**
- Build 21 to 50 prospects for trigger A. Per record: fit, persona, trigger and date, source URL, verification result, phone if Tier 1, country, entity type, lawful basis, suppression status.
- Write the account brief for Tier 1 names. Draft email 1 to 3 and the LinkedIn note. Human review.

Exit check: domains authenticated and warming, cohort verified with bounce risk under 2%, scorecard live, legal gating applied.

## Days 15 to 30: prove one message-market pair

- Send to the first 21 to 50 at 5 to 10 a day per inbox. 3 emails (day 0, 3, 8), 1 to 2 contacts per company, tracking off.
- One trigger, one problem, one proof point, one soft ask. Offer something smaller than a meeting (permission to send a guide, teardown, sample).
- Call the highest-signal prospects in the cohort with a permission opener; missed call means a LinkedIn note within 5 minutes and an email next day ([cold-calling.md](cold-calling.md)).
- Answer every positive reply within minutes with two times.
- Read every reply. Group the no-reasons.
- Launch cohort 2 (trigger B) in week 4 so you have a comparison.

Exit check, per cohort: delivered with bounces under 2% and no complaints; at least one positive reply per 50 to 100 contacts or a clear reason why not. If replies are under about 1% after 300 delivered, change the list or the offer before the copy.

Owner report: which trigger replied, verbatim objections, meetings held, what to change.

## Days 31 to 60: add channels with a job

- LinkedIn gives recognition and a second route, not a copy of the email: engage, request (note for Tier 1 and 2, blank for network building), 3 messages max ([linkedin.md](linkedin.md)). Benchmark acceptance against about 28% and judge on meetings per invite.
- Phone for Tier 1 and the best Tier 2. Track connect rate, conversation-to-meeting, held rate. Below 5% connect: fix the phone data.
- Split cohorts by trigger (job change, hiring, competitor engager, funding, stack change), 50 to 200 each. Each test teaches something about buying context.
- Start ranking accounts from outcomes: positive replies, meetings and opportunities by trigger, title and segment. "Not interested" and "remove me" are replies; never optimize on raw replies.
- Optional: light account-warming ads on the prospect list (see `paid-ads`).

Exit check: one or two triggers with a repeatable positive-reply rate and held meetings; a dead trigger switched off.

## Days 61 to 90: scale winners, not activity

- Scale a segment only with healthy delivery (bounce under 2%, complaints near zero), a repeatable positive-reply rate and qualified meetings. Against Smartlead, 0.74% reply is median and 1.43% is p75; against Instantly, 3.43% average and 5.5% top quartile. Use the one matching your denominator.
- Add inboxes and domains to add volume. Keep per-inbox sends at 10 to 25.
- Write each winner as a play: ICP + trigger + persona + country rule + channel order + message hypothesis + proof + CTA + stop conditions + benchmark + observed economics.
- Hand low-risk reply types (OOO, unsubscribe, bounce, not now) to the agent; keep positives human.
- Decide buy vs build: only consider an agency or setter now that you know your conversion rates ([ai-and-agencies.md](ai-and-agencies.md)).

Exit check: a small portfolio of proven plays, cost per held meeting known, a forecast of meetings per month from current capacity.

## Weekly rhythm after day 90

| Day | Work |
|---|---|
| Monday | Signal sweep, new cohort research (45 minutes for 20 accounts is enough for a solo owner) |
| Tuesday, Thursday | Sends and calls in protected blocks; callbacks and replies interrupt everything |
| Friday | Scorecard, read every reply, kill or keep each play, domain health check |

A fixed 2 to 3 hour weekly block beats bursts, even when it only produces "5 outreach messages or 3 follow-ups" (r/agency 64). Under 10 customers, outreach is the main job; from 10 to 25, about half the day (r/startups 280).

## Formulas

```
contacts needed per month   = target meetings / meeting rate per contact
meeting rate per contact    = positive reply rate x reply-to-meeting rate
inboxes needed              = (contacts per day x emails per sequence) / 15 to 25
cost per held meeting       = (tools + data + inboxes + people hours x rate) / meetings held
max cost per held meeting   = first-year gross margin per customer x close rate from held meeting / 3   (3:1 rule of thumb, not a benchmark)
payback check               = CAC / monthly gross margin per customer   (months)
```

Example: target 8 held meetings a month, 1.2% of contacts become a meeting, 85% show: 8 / (0.012 x 0.85) = about 785 contacts a month, about 36 a working day, about 108 sends a day on 3 emails, so 5 to 7 inboxes on 3 domains plus a spare.
