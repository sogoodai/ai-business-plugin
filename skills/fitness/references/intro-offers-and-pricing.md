# Intro offers and pricing

The intro offer exists to build a routine and reach the recurring price, not to make money or collect signups. Generic pricing psychology, tiers and increase mechanics live in `offers-pricing`; this file holds the fitness-specific angles. Wording: [scripts.md](scripts.md).

## Intro offers by sub-model

| Sub-model | Default intro | Evidence | Measure |
|---|---|---|---|
| Boutique studio (yoga, pilates, cycling, HIIT, barre) | Paid, multi-visit, 14 to 30 days of access at about half the monthly unlimited (Mindbody example: $79 intro vs $159 unlimited) | Intro buyers 54% 90-day retention vs 35% without (Mindbody 2025, association); vendor guidance on price and 15 to 30 day expiry | Intro to recurring within 14 days of expiry; first-month visits |
| Small gym or box | Free consult plus one coached session, or a short coached on-ramp | Two-Brain reports free trials underperform consult-first in its network (not randomized); a training gym combines a free PT session with two free weeks of small group, owner sells from a phone CRM, LTV about $1,800 (r/smallbusiness, 535) | Set, show, close; 90-day retention by intro type |
| PT in a gym | Paid first session at a token price or a coached consult | £10 no-commitment first session, operator claims 90% kept and the rest left good reviews (r/personaltraining, 91); one free session judged too little by a trainer who gives multiple free sessions when starting from zero (81) | Close within 7 days; 90-day retention |
| Independent PT | Consult, then a monthly plan start date | Rates published, consult used to fit schedule and goals | Consult to client rate |
| Online coach | Paid consult or straight to a monthly plan with a 90-day expectation | $80 per 30-min consult on Zoom, $525 a month coaching (r/personaltraining, 89) | Consult to client; month-3 retention |

Rules:

- **One intro per service line.** Several overlapping specials confuse and train people to wait for the next one.
- **Short expiry, multiple visits.** A single free class tests whether they like an instructor; it does not build a habit. A long cheap pack lets them behave like a bargain shopper without meeting the real price.
- **Never stack a voucher or ClassPass rate on the intro.**
- **Book the conversion conversation before the intro ends.** Mindbody's 30-day framework (Aug 2026, vendor playbook): welcome in the first days, follow-up shortly after, offer in the middle of the month, nurture before expiry, close and review at the end.
- **Street signage still works for studios.** A neighbor walking by early in the morning saw a free intro class sign, joined reformer classes and "never missed a class" (r/pilates, 183).
- **Gift intros convert well.** A pilates client came in on an intro package a friend bought for her after surgery; three years later she attends 4 to 6 times a week (r/pilates, 562). Let members buy the intro as a gift.
- **Test free vs paid on retained contribution per lead**, not on signups. Free brings volume; whether it brings members is the question.

## Six-week challenges

No 2025 to 2026 evidence shows that "six weeks" or challenges in general beat a standard intro; most published support comes from companies that sell challenge systems. Run one only with a written business case: expected leads, cost per signup, delivery cost (coach hours, groups, check-ins), recurring conversion rate, 90-day retained revenue. Score it on net members after refunds and discounts and their 90-day retention, not signups. Remote challenge mechanics (daily actions, completion rates): `education-coaching`.

## Packs, memberships and rollovers

- **Packs** monetize genuinely irregular customers. They hurt when regulars use them as a cheap membership. Flag any customer for whom the membership would have been cheaper over the last rolling month and start a membership conversation.
- **Allow one month of rollover** on fixed-count memberships (4 or 8 classes) so travel weeks do not feel like lost money (r/YogaTeachers, 174, customer view).
- **Unlimited memberships need reliable classes.** A $350 unlimited pilates member quit after the studio cancelled classes within the hour three times while charging members $10 for late cancels; another member quit a nearly $200 unlimited (r/pilates, 442; top comments 925 and 614).
- **Do not sell a membership you cannot honour at peak.** A 9-court facility charges per booking instead of memberships so members never pay a fee and then cannot book (r/smallbusiness, 291).
- **Graduation tier:** training clients graduate into an access membership instead of leaving (r/smallbusiness, 535).

## Personal trainer pricing

- **Anchors, not targets.** US single session $75 median, middle half $50 to $110; UK £45 (London £57.50, elsewhere £40); monthly 1:1 plan $460 US, £320 UK (iPT Oct 2026, small samples, mostly stale pages). Operators at $140 to $165 an hour in affluent areas (r/personaltraining, 132 and 89).
- **Place drives price.** Operators recommend building a book in a dense, high-income catchment, moving towns if needed; one AMA trainer charges $80 to $100 an hour where median income is about $120,000 (r/personaltraining, 364). Others report six figures in lower-income markets too (89).
- **Structure choices that work for operators:**
  - Monthly autopay by weekly frequency: card stored in Stripe, charged on the 1st, a flat rate for 2x and another for 3x a week; almost no resistance, no chasing (r/personaltraining, 309, explanation at 58, endorsed at 9 and 10).
  - Billing every 4 weeks with a recurring time slot and a booking window that shows 4 weeks, self-rescheduling inside it, waitlist alerts (same thread, 5).
  - Weekly billing instead of packages made a 6-trainer studio compete less on price (r/personaltraining, 48).
  - Fixed price by length: $75 for 30 min, $95 for 45, $115 for 60, no bulk discount (285).
  - Bundle steps if you must: $99 single, $89 at 12, $79 at 24 (364). A luxury-gym trainer discounts only above 20 sessions (132).
  - Twice-weekly 30-minute sessions spread revenue across 20 to 24 clients (87).
- **Minimums.** Weekly training minimum, no ad hoc sessions, payment by subscription or card machine (r/personaltraining, 97).
- **Auto-renew until cancelled.** "Do you want to renew?" is never asked; the agreement renews until cancelled (20-year trainer, 82). Follow auto-renewal law ([retention.md](retention.md#freeze-and-cancel)).
- **Vacations:** billing stays the same; with 6 weeks' notice for a 1 to 2 week trip, sessions are front-loaded or made up after (309, reply at 4).
- **Price the relationship, not the hour.** Put programming, messaging, nutrition accountability, testing and progress reviews in the package description. Otherwise prospects compare coaching with a commodity hour.
- **Sell transfers when you are full.** A trainer raising his new-client minimum to $150 an hour handed lower-rate clients to colleagues for a 25% sell-and-service commission: $4,000 sold, $1,000 earned in a month (r/personaltraining, 232).

## Semi-private and small group

- **The equation:** price per person x average occupied seats - extra delivery cost > revenue of the 1:1 hour it displaces.
- **Divide your hourly target across up to four people,** explain the shared format before purchase, bill monthly (r/personaltraining, 309 thread; another commenter says semi-private is 75% of their business).
- **Individual programs inside the group** (each client on a personal Trainerize plan, logging their own work) keeps it from feeling like a class (r/personaltraining, 83).
- **Semi-private is not small-group training.** A 15-year studio owner switched from small group to semi-private as part of competing less on price (r/personaltraining, 48).
- **Price the break-even into the format:** 4 spots, past break-even with one person (r/smallbusiness, 535).
- **Counterpoint:** a studio grossing $191,000 is phasing out groups because 1:1 at $79 to $99 is stickier and higher margin (364, 88-upvote reply, a 16-upvote commenter agreed some clients want 1:1). Run the equation with real seat counts before choosing.
- **Specialist group class:** a trainer teaching only HIIT group classes brings in about $250 a class (secondhand, 285).

## Online coaching pricing and tiers

- **Monthly, never per session.** $200+ a month is reasonable depending on what is included (operator, 98); $150 to $300 starting range (10+ year online coach, 50). Medians: $199.50 US, £99.50 UK, €181 Nordic (iPT, Coachway 2026).
- **Two tiers by accountability:** entry = custom programming, one weekly text or form check-in, progress review and adjustments, replies within 12 hours on weekdays; higher = the same plus a weekly 15 to 30 minute call. No add-on fees for nutrition, extra check-ins or messaging within the stated limits (r/personaltraining, 184). A third premium or hybrid tier adds live or in-person touchpoints.
- **Do the workload math first.** $50 a month x 15 clients took 20 hours a week and ended in burnout (95). A $19 a month info program for seniors sold one copy in month one; personalized coaching at a higher price brought retention and referrals (91).
- **Bound the deliverables in writing:** weekday reply window (12 to 24 h), what is excluded (daily meal reviews, form checks on every set), and whether the promise survives 15 to 20 clients (98).

## Price increases

- **Trigger:** near capacity, waitlist, or confidence you can replace leavers (operator, 82). Not your costs.
- **New clients first,** then existing clients with a month's notice.
- **Small, regular, unceremonious.** "I'm raising my prices by 5 dollars next month to cover my expenses", no big announcement (52-year-old trainer, 191). Operators mention roughly annual raises around 10% (56).
- **Explain through their goals, never your life.** A trainer justified a raise with diapers, food and his girlfriend's support and said the client's degree made it affordable; she left for a trainer $25 an hour more expensive whose sessions felt built around her goals (r/personaltraining, 156).
- **Raises can be a capacity tool.** 28 clients cut to 19 regulars at the new rate, near-equal take-home, restored quality (56).
- **Keep rates when moving clients to autopay.** Change one thing at a time (309).

## Discounts

- Gyms without discounts earn about $2,900 more a month at the median (Two-Brain Nov 2026, confounded). Permanent discounts reset the anchor.
- For a dry spell: "20 to 35% off this week only", not free classes or a lower standard rate (r/YogaTeachers, 57).
- Teen and kids discounts can open a family market (r/crossfit, 1,846-upvote thread, comment at 12).
- Staff discounts are a referral channel: a UK trainer charged gym staff £10 a session so they recommend him (r/personaltraining, 76).
- Use real deadlines (a price rise on a date, a cohort start), never fake countdowns.
