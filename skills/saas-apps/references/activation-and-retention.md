# Activation, onboarding, churn and dunning

Retention decides whether acquisition compounds. High Alpha 2025: companies with NRR above 106% and CAC payback under 10 months grew 71% median; under 98% NRR with the same payback, 30%. Fix this file's problems before buying traffic. Email flow mechanics and deliverability: `email-sms-loyalty`.

## Define activation from data, not from the onboarding checklist

Method (coreyhaines31 onboarding, MIT, citing Amplitude Compass docs):
1. Signup is time zero. Pick an early window (first 7 days for weekly-use tools, first session for consumer apps) and a separate later outcome (week-4 return, or paid at day 30).
2. Include every eligible signup with full follow-up; show immature cohorts separately.
3. Compare actions done inside the early window between retained and churned users. Candidate events are hypotheses.
4. Confirm on a later cohort, then test an intervention that pushes users to the event.

Good activation events represent value, not setup. "Invited a teammate" beats "finished onboarding" for collaborative tools; for an AI writing tool "exported or used an output" beats "generated an output" (research, November 2026). For multi-user products, measure activation per workspace, not per person.

Benchmarks to sanity-check only (vendor, do not average them): Userpilot 2025 37.5% average activation, 1 day 12 hours average time to value, 19.2% checklist completion; Appcues 2025 32% activation. Vendor claim, uncited: 40 to 60% of free-trial signups never return after the first session, 75 to 80% of trial abandonment happens in the first day (coreyhaines31 Minimum Path to Value).

## Cut the path to value

The strongest operator numbers in the whole dataset are cuts:
- Deleting analytics, team seats and custom branding to leave the core widget: activation 24% to 61% (r/SaaS, 768).
- Renaming "Workspaces" to "Projects" after about 10 support questions a day: activation 30% to 54% in a week. The founder previewed the label by editing it in the browser console first (r/indiehackers, 70).
- Rebuilding an 11-feature MVP around one function after a churned user said "I couldn't figure out what it does in the first 30 seconds": next-week return from near zero to about 40% (r/indiehackers, 57).
- 15 onboarding screens to 4: users reaching pricing went from 28% to 66%. Revenue stayed $0, so reaching the paywall is necessary, not sufficient (r/AppBusiness, 79).
- Two steps removed on mobile closed a weeks-long mobile vs desktop activation gap "overnight" (r/AppBusiness, 55).
- Requiring the user's own API key lost 90% at that step (r/microsaas, 166).

Procedure (Minimum Path to Value, coreyhaines31, MIT): list every screen, field, click, permission prompt and empty state between signup and value; cut, defer, pre-fill or make skippable everything not needed for first value; rebuild in value-first order; re-measure.

Value before account: let people use the tool before signup and ask for an account only to save. Duolingo delaying signup until after the first lesson is reported at +20% DAU (secondhand, r/EntrepreneurRideAlong, 194). Utility pages that rank in search should work with no login (r/SaaS, 359).

**Long onboarding is not always wrong.** One app lengthened onboarding after copying the top apps in its niche and conversion "improved significantly" (r/AppBusiness, 164); quiz-style apps add an animation every 4 to 5 questions (r/indiehackers, 70). Rule: cut screens that explain; keep screens that ask the user about their goal and build a personal result shown right before the paywall.

Endowed progress: a 12-box coffee card with 2 boxes pre-stamped beat a blank 10-box card, 34% vs 19% completion, same purchases needed (classic study, cited in r/startups, 378). Start checklists partly complete (signup counts as step 1).

First screen = the outcome. After a day watching a 120-vehicle fleet customer, the first screen became "which vehicles are not earning and why"; the admin dropped a 20-minute daily spreadsheet within a week (r/EntrepreneurRideAlong, 48).

## Lifecycle messages that move activation and paid conversion

Fire on behavior, not elapsed time. Research synthesis (November 2026), wording to adapt:
- After the first value event: "You just completed [outcome]. The next step that usually makes this useful every week is [specific second action]."
- Before trial end, activated: "You've already [value event X times]. Keep [artifact, history, integration] active after [date] by choosing a plan."
- Before trial end, not activated: "You haven't reached [specific outcome] yet. Reply with what blocked you and I'll point you to the shortest path."

Operator tricks:
- **Plain text from a real person's name:** opens "almost doubled" for one founder and rose for another (r/microsaas, 250 and 160). Welcome line: "Thanks for signing up. Even though this is an automated email… I just wanted to say hey and let you know I'm a real person." (r/EntrepreneurRideAlong, 148).
- **Welcome, tips, then a setup-review offer a few days in** (r/buildinpublic, 38).
- **Free 15-minute setup call for every signup** in B2B; at $20 to $50 a month it pays back if it lifts paid conversion by a few points ([economics.md](economics.md)).
- Activation emails should drive back into one specific in-app action, never duplicate the tour (coreyhaines31, MIT).

## Churn: measure, then cut

```
monthly logo churn, revenue churn, GRR and NRR by signup cohort, plan, source and country
voluntary vs involuntary share (failed payment then canceled = involuntary)
```

Segment before comparing: ChartMogul December 2025 medians above $250K ARR were NRR 82% B2B SaaS, 49% B2C SaaS, 48% AI-native (AI-native GRR 40%). An AI consumer tool losing half its revenue a year is median, not broken; it still needs a plan.

Operator evidence:
- **Two months spent only on churn took it from 34% to 11.6% and doubled MRR on the same traffic** (r/AppBusiness, 129).
- **Required cancel reason** that accepts anything ("no" or ".."): at least 50% still give an honest reason (r/buildinpublic, 38).
- **Save offer only for real customers:** 50% off the next 3 months, only for subscribers with at least one paid month (r/indiehackers, 47, planned).
- **Sit in on one unfiltered cancellation call:** a churned customer said being the only user on their team, with no Slack or CRM integration, made it "easy to forget" (r/SaaS, 370). Integrations and team invites are retention features.
- **Refund early, before a dispute:** 90% of support requests came from customers who spent under $5; $20+ spenders barely wrote in (r/SaaS, 569). Fast refunds protect your Stripe dispute rate and reviews.
- **Recurring triggers built into the product:** a notification the day before a tracked subscription bills, budgets that reset on the user's payday instead of the 1st, a Lock Screen widget so logging takes 2 seconds (r/buildinpublic, 70; r/AppBusiness, 67).
- **Fix the paying user's problem twice:** a failed webhook on a $49.99 upgrade; the founder enabled Pro manually, fixed it, and sent a second email confirming activation; the customer stayed (r/buildinpublic, 46).
- **Weekly proof for B2B accounts:** a 2-minute Loom every Friday covering what happened, what the data says and next week's step, after a €2,000-a-month client left over three silent weeks (r/EntrepreneurRideAlong, 340).

Cancel flow (coreyhaines31 churn-prevention, MIT; numbers uncited): one-question exit survey with 5 to 8 reasons plus free text, then one offer matched to the reason and one fallback. Too expensive: discount 20 to 30% for 2 to 3 months or downgrade. Not using it: pause 1 to 3 months or a free setup session. Missing feature: roadmap or workaround. Switching to a competitor: comparison plus offer. Business closed: no offer. Keep "continue cancelling" visible and confirm the end date. Check applicable cancellation requirements for the customer jurisdiction; design cancellation to be as easy as signup; never hide the cancel path (`offers-pricing` holds cancellation law).

Churn warning signals (coreyhaines31, MIT): logins down 50%+ over 2 weeks, key feature stopped, billing page visits, seats removed, data export started. Triggers: usage down 50% for 2 weeks sends a "need help?" note; export started on a high-value account gets a personal email the same day.

## Dunning and involuntary churn

Baremetrics Recovery Index (Q3 2026, all Baremetrics Recover customers, vendor): the typical company recovered 29.4% of the failed charges its dunning attempted; 203,756 failed payments attempted, 34,252 recovered. Its May 2026 edition reported 12.7% on a smaller cohort; use the latest and your own number. Paddle (vendor) estimates involuntary churn at 20 to 40% of SaaS churn. Compute your own share first.

Stack (coreyhaines31 churn-prevention, MIT):
- Card-expiry emails at 30, 15 and 7 days; Stripe's card updater and Smart Retries on; a pre-billing notice 3 to 5 days before annual renewals.
- Retry soft declines over about a week; do not retry hard declines.
- Emails on day 0, 3, 7 and a final notice, plain text, with a no-login update link. Wording (research, November 2026): subject "Payment issue: your [product] account is still active"; body "We couldn't process the payment for [plan]. Nothing has been deleted. Update your card here: [billing link]." Follow-up: "Your [specific asset or workflow] is still available, but billing needs to be fixed by [date] to keep service uninterrupted."
- Say "your payment didn't go through", never "you failed to pay".
- On mobile the stores run billing retries and grace periods; turn on Apple's billing grace period and Google Play's grace period and account hold in the consoles.

## Win-back

ChartMogul (2026): 45% of returning customers come back within 30 days, 66% within 90. Front-load win-back.
- Day 7: one question on why they left. Day 30: what's new. Day 60: their specific reason, if fixed. Day 90: one final offer (coreyhaines31, MIT).
- Lapsed-customer calls work at scale: a 100-contact AI-voice pilot fixed the wording live, then about 3,000 contacts in a week; about 100 called back and 50 said they would renew (gym, r/indiehackers, 146). Check calling and consent rules before copying.
- Never discount the whole churned list; offer only to the reasons a discount fixes.

## Tricks most owners miss

- Separate "paid conversion" from "retained paid conversion" so discounts and card traps do not look like wins.
- Track free-credit exhaustion and time to first billable usage for AI tools (ChartMogul usage-billing guide, October 2026).
- A changelog email of what shipped is a retention touch; tier announcements by size: major gets every channel, medium gets the affected segment, minor goes in the changelog only (coreyhaines31 launch, MIT).
- Turn a public critic into a fan: "Hey, I actually implemented your suggestion!" the next day (r/microsaas, 51).
