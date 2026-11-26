# Retention and rebooking

The 42% of guests who visit more than once a year produce 80% of revenue (Zenoti, 2024 data, directional). Most loss happens between visit one and visit two. Messaging depth (flows, deliverability, consent) is in the `email-sms-loyalty` skill; this file covers what is specific to appointment businesses.

## Measure kept rebooks, not calendar entries

Three different numbers:

1. **Prebooked before checkout.**
2. **Future appointment still held after 7 days.**
3. **Future appointment completed.** Only this one is revenue.

- In Zenoti's 2025 salon data, when a client held a single future booking, 72% of those appointments were cancelled; clients holding 2+ future bookings cancelled 4%. Observational, so it partly reflects who books ahead. Still: a pre-book rate alone is a vanity metric, and a bonus paid on calendar entries rewards calendar inflation.
- **Report per provider:** first-to-second completed visit rate, second-to-third, completed rebook rate, days between completed visits, 90 and 180-day retained revenue.
- **Vendor targets for context:** Vagaro calls 60%+ rebooking healthy and under 40% a warning (2026). Med aesthetics 90-day rebooking: 71% median, 76.5% top quartile (CorralData 2026).

## Rebooking at checkout

- **Name the return window, then offer two slots:** "Your color will start shifting around 6 to 8 weeks, that's the best time to come back so it still looks fresh. I can hold Tuesday the 14th at 3:30 or Thursday the 16th at 11, and you can move it later." Stylists report noticeably more rebooking from the window line; two concrete options beat "want to book?".
- **The provider names the interval in the chair,** the front desk offers the slot. Never "call us when you're ready".
- **For cadence clients, book the series** (next 2 or 3 visits) so they hold 2+ future bookings. Pair with the 48-hour reminder and one-tap reschedule so the series stays kept.
- **Tell clients who say you are hard to get to book weeks or months ahead.**
- **Lash fills:** store the refill interval and trigger the rebook before the client crosses into "full set" territory. Flag near-empty fills as full sets before the visit, not in the chair.

## Due-soon and lapse messages by each client's own rhythm

- **Lapse trigger = the client's or service's expected next visit + a grace period.** Not a flat 90 days. The blended average gap is about 63 days (Mangomint 2026), but a barber cut, a lash fill and a facial have very different cycles.
- **Per-client rhythm** (adapted from anthropics/knowledge-work-plugins, Apache-2.0): for clients with 3+ visits, normal interval = median gap between their own visits. Quiet = current gap over 2x normal; gone = over 3x. Under 3 visits, use the service median and label it an estimate.
- **Rank by past value,** then frequency, not by time silent. Fifteen names the owner will actually contact beat two hundred.
- **Top of the list:** a client who left a bad review or complained and then stopped coming. That gets a phone call, not an email.
- **Sequence, no discount first** (research synthesis plus harvest rules):
  1. Due-soon nudge with two real slots from their usual provider.
  2. Overdue: personal note naming their last service, still no offer.
  3. Value add: a low-cost add-on if they come back by a date.
  4. Cash discount only for the residual group, and only if the owner approved it.
- **Stop rules:** any reply stops the sequence; a complaint hands it to the owner at once; at most 3 touches per lapse across 2 channels, then a dormant list.
- **Offer by segment:** high value with a complaint, a personal call and no offer ("the apology is the offer"); high value no complaint, owner note; mid value, a timely reminder; low-value one-timer, one small offer then stop.
- **Recall by reason, not only date** (adapted from mohitagw15856/pm-claude-skills, MIT): drift, cost, bad experience, moved, schedule. One message per reason; measure attended appointments, not sends.
- **Evidence:** a med spa "Miss You" at 10% off rebooked 26% of recipients (Mangomint case, no control). Keep a holdout when the list is big enough before crediting the discount.

## Fill gaps from the list first

- **Email or text exact slots and what fits:** "Openings this week: Jenna, Tuesday 10:30 to 12:00, cut and color. Reply to grab it." Recipients book on the spot and add services.
- **One inventory fact, one call to action** (Boulevard's 2026 messaging guidance agrees).
- **Target the gap:** clients of that provider, due within 3 weeks, who have booked that daypart before. Never discount the whole database because tomorrow has two empty slots.
- **Short-notice list** of established clients who accept last-minute slots; they also get first access as a perk.
- **Benchmarks:** Phorest salons average 44% opens, 1.7% clicks, 4.2% click-to-book (2025 campaigns, published 2026). Judge by bookings per 1,000 sends.

## Memberships

- **Only where there is a natural repeat cadence and spare off-peak capacity:** massage, blowouts, waxing, lash fills, facial programs, some med spa maintenance. Not for once-a-year transformations.
- **Data:** membership salons grew sales 8% vs 2% and existing-guest visits 12% vs 3% (Zenoti 2025). Med aesthetics member retention 90.4% vs 50.6% for non-members, member spend 1.70x (CorralData 2026). Both are observational: stronger businesses sell more memberships and loyal clients self-select. Treat the gap as an upper bound.
- **Design:** one service a month at a member rate, member-only add-on pricing, priority booking, rollover capped at one month, peak-time redemptions limited or surcharged. Pause option for life events. Points programs suit high-frequency, variable spend; punch cards win when you can't identify clients reliably.
- **Pilot on one cohort,** then measure member contribution per provider hour after redemptions, entitlement use, freeze and cancel rate, add-on spend, and peak displacement ([economics.md](economics.md)). Prepaid services are a liability; ask the accountant.
- **Membership after a series:** clients finishing a package move into a lower-touch membership.
- **Bundles that create a habit:** "Book four a month and get half off the fourth" (price so the discount still pays). Recurring cleansing-only or blowout appointments for clients who struggle at home.
- **Loyalty card with endowed progress:** 12 spaces with 2 already punched (10 paid visits either way) returns noticeably more clients than a blank 10-space card.
- **Never imply the member's usual choice is wrong.** "If you actually want to feel better instead of sore" ended a membership the same day.

## Make every visit repeatable

- **Write down what they loved:** lash map by zone in mm, color formula (weigh it), pressure level, music, chat or quiet. A client who asks for 10 mm inner and 12 mm middle and outer every time gets the same result every time.
- **Record surcharges in the profile** (long hair, clarifying, dematting) so every stylist charges the same and the client is not surprised.
- **Explain your work while you do it** (why this lash map suits their eye shape, what could change next time). Clients who get this say "I will keep seeing her forever."
- **Transfer the formula and notes** when you refer overflow to a newer colleague.
- **Check in twice on pressure plus once overall,** and treat "it's fine" as a signal to adjust, not satisfaction.

## Recovery

- **Your mistake, your free fix, fast.** Single irritating lash two days later: free. Missed top row: free, never $50 (the client charged $50 left for three years). Refill needed within the first week: free.
- **Ask what recovery they want** before offering one. A refund plus a free session can still fail if it isn't what they wanted.
- **Same-evening follow-up** after a walkout or bad session. Clients who get a sincere apology often say they won't leave a bad review.
- **Ending a session that isn't working:** end it yourself early and don't charge, rather than letting it run to the end and comping it.
- **Junior stylist mistake:** offer a correction with the mentor or senior stylist involved.
- **Unhappy after a week:** compare with the agreed swatch and inspiration, with a second stylist checking. Agreed result and a change of mind = discounted paid change; a real miss = free correction.
- **Discovery questions:** "When did you start getting worried?" and "How does this differ from what you expected?" instead of "What's wrong?"

## Small touches clients mention

- Turn away and tidy up while they use the tip screen. Never question a tip; one tech lost a client and an extra $10 with "that's it?".
- Take-home QR card for tips: clients send digital tips hours or days later.
- Free cleanser with every full lash set; replacement cleanser free on request.
- Aftercare guide attached to every receipt (for lashes: lean back when rinsing conditioner).
- Birthday add-on (aromatherapy, scalp time) at no charge.
- Hot towel neck and shoulder finish, seven-minute scalp massage to close.
- Open early once for a loyal client's pre-vacation emergency fix. They remember and tip more next time.
- Quiet by default for those who want it: "I'm not super chatty, so apart from checking in on pressure, I won't interrupt your zen." Don't push talkers into silence either.

## Moving or leaving a salon

- **Tell regulars before you move.** Clients who track you down unannounced are upset.
- **Expect to keep about a third** of clients when moving 20 to 25 minutes away, 50 to 80% within 5 to 10 minutes. One stylist kept 20 of 65 despite personal outreach.
- **Reach clients you can't find on social:** one stylist sent former tipping clients $0.01 on Venmo with the new address.
- **Sudden closure:** message every client through the old booking app right away; clients usually say they'll follow you. Check your contract's non-solicit terms first.
- **Rebuild with model calls** and post nearly every result; one stylist rebuilt a better clientele within a year.

## Ending a client relationship

Fire clients who cost more than they pay (chronic cancellations, constant correction requests, abuse). Give a specific, service-related reason, never a vague "not a fit", which can be read as discrimination and hurt word of mouth. Handle hygiene one-to-one, never with a newsletter to everyone. Scripts in [scripts.md](scripts.md).
