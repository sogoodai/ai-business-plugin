# Templates (verbatim)

Swap brackets for real details; never ship an unresolved token. Keep SMS under 160 GSM-7 characters: one emoji or accented character switches to UCS-2 and 70-character segments, so cost can double or triple. Marketing SMS start with the brand and end with an opt-out line where the law or carrier requires it. Source after each template: "research 2026" means the deep-research synthesis; MIT and Apache-2.0 sources are adapted with attribution in [sources.md](sources.md).

## Consent and control messages

**US SMS opt-in disclosure, next to the phone field** (coreyhaines31 sms compliance, MIT; required elements):
> By entering your number you agree to receive recurring marketing texts from [Brand] at this number, up to [4] msgs/month. Consent is not a condition of purchase. Msg & data rates may apply. Reply HELP for help, STOP to cancel. [Terms link] [Privacy link]

**STOP reply** (one confirmation only, MIT):
> You're unsubscribed from [Brand] alerts. No more messages will be sent. Reply HELP for help.

**HELP reply** (MIT):
> [Brand] alerts: For help, visit [URL] or email [support]. Msg & data rates may apply. Reply STOP to cancel.

**UK or EU soft opt-in line at checkout or booking** (wording pattern from ICO and ePrivacy conditions: offer the opt-out at collection):
> We'll send you occasional emails about our own similar [products/services]. Untick if you'd rather not. You can unsubscribe in any email.

**Email footer** (Gmail, Yahoo, CASL, Spam Act all require sender ID and a working unsubscribe):
> You're getting this because you [bought from us / booked with us / joined at the counter] on [date]. [Business legal name], [postal address]. Unsubscribe in one click: [link]

## Welcome

**Ecommerce E1, subject "Your [10%] code is inside"** (NX pattern, MIT):
> Hi [first name or "there"], here's your code: [CODE]. It works on everything except [exclusions] until [date].
> Most people start with [bestseller], because [one concrete reason].
> [Shop now]
> [Owner first name], [Brand]

**SMS welcome** (coreyhaines31, MIT, about 155 characters):
> From [Brand]: Welcome! Here's your 10% off code: WELCOME10. Shop now: [link] Reply STOP to opt out, HELP for help. Msg & data rates may apply.

**Restaurant welcome E1** (ai-restaurant-claude, MIT, adapted):
> Thanks for joining, [first name]. Your first [appetizer] on us next time: just show this email to your server. Good until [date, 60 days].
> [Owner first name], [Restaurant]

Day 10 subject if no visit: "Did your free appetizer expire?"

**In-person signup trade at the counter** (operator suggestions, 11-pt comment, untested):
> "Get a free drink today if you sign up for our anniversary special!"
> "Free jumbo fries upgrade on your meal if you sign up for our birthday club!"

## Cart, browse and quote

**Cart email 1, subject "Still deciding on [product]?"** (no discount):
> You left [product] in your cart. It's still there: [Return to cart]
> If you have a question about [sizing / shipping / how it works], just reply. I read these.

**Cart SMS 1** (coreyhaines31 pattern, MIT, one segment):
> From [Brand]: you left [product] behind. Your cart is saved here: [branded link] Reply STOP to opt out

**Cart email for $100 to $300 carts, objection "will it work for me"** (coleschaffer objection map, MIT):
> Most people who hesitate on [product] ask whether it will work for [their situation]. Here's what [customer name] said after 30 days: "[real review]". If it doesn't, returns are free for [N] days.

**Missed call SMS** (research 2026):
> Hi, this is [Business]. Sorry we missed your call. Are you looking for [service]? Reply with your ZIP/postcode and a one-line description and I'll tell you the next available time.

**Inbound form SMS** (research 2026):
> Hi [Name], [Business] here. I saw your request for [specific service] in [area]. I can help. Two quick questions so I quote it correctly: [question 1]? And [question 2]?

**Quote sent by email, SMS nudge** (wedding photographer, 66-pt thread):
> hey received your inquiry, sending pricing to your email now!

**Quote day 3** (research 2026):
> Hi [Name], wanted to make sure you had everything needed to compare the [service] options. Is the main question price, timing, or what's included? Reply with one and I'll clarify it.

**Quote day 7** (research 2026):
> We currently have [Tuesday AM / Thursday PM] open in [area]. If you want me to hold either slot while you decide, reply TUE or THU.

**Follow-up to a partner or buyer who went silent, 3 days later** (270-pt thread):
> Following up!

## Post-visit, review and rebook

**Review request, same day or next day** (research 2026; no incentive, sent to everyone):
> Thanks for coming in today, [first name]. If everything felt right, would you mind leaving a quick review? It helps people nearby know what to expect: [review link]. If anything wasn't right, just reply here and I'll fix it.

**Review request, home services, sent from the driveway** (operator, 40-pt thread):
> Thank you for your business. You were a pleasure to work with. We genuinely hope you were pleased with our service. As a small, family owned business we rely heavily on Google reviews for future business. Would you kindly take a quick moment of your time to leave me feedback? It would help so much! [link]

**Asking in person while they're happy** (17-pt thread):
> "Would you mind leaving us a quick Google review? It genuinely helps people find us. I'll text you the link right now so you don't have to hunt for it."

**Post-visit rebook** (research 2026):
> Hi [first name], hope you're loving the [service]. You're usually due again around [date]. I've got [slot 1] or [slot 2] open; want either?

**Two-way rebook, no sales language** (research 2026):
> Hi [name], this is [person] at [business]. Want me to hold [time] for your next [service]? Reply Y or send a time that works.

**Checkout line for cadence services** (129-pt thread):
> "Your color will start shifting around 6 to 8 weeks, that's the best time to come back so it still looks fresh."

## Due-soon, gap fill and replenishment

**Due-soon** (beauty research 2026):
> Hi [first name], you're coming into your normal [service] window. [Provider] has [Tuesday 3:30] or [Thursday 11:00] available. Want either held for you? [booking link]

**Gap fill to established clients** (research 2026):
> Two openings with [provider] tomorrow: [time] for [service] and [time] for [service]. Existing clients can book here: [direct link]. First booked, first held.

**Openings email, line format** (146-pt comment):
> Openings this week: Jenna 10:30 to 12:00 Tuesday: Cut and Color. Sam 3:00 to 4:00 Thursday: Men's cut. Reply to grab one.

**Replenishment, WhatsApp template with buttons** (coreyhaines31 whatsapp, MIT):
> Your [product] usually runs out around now. Want us to set aside a refill?
> [Yes, reorder] [Not now] [Stop promotions]
"Not now" suppresses 30 days.

## Lapse and win-back

**Touch 1, day 0, no pitch, under 90 words** (anthropics reactivate pattern, Apache-2.0):
> Hi [first name], it's [owner] from [business]. It's been a while since your last [service/order], and I wanted to check in rather than send you another promo. Was there anything about the last [visit/order] that wasn't right? Either way, I'd like to know.

**Touch 2, day 10, what changed, under 80 words:**
> Since you were last in, we've [added Saturday mornings / started [new service] / brought back [product]]. If that's useful, here's the link: [link]. No need to reply.

**Touch 3, day 28, one time-bound reason, under 70 words:**
> [Provider] has two [service] slots open next week and I'd like to hold one for you, with a [low-cost add-on] included. Reply with a day and it's yours until [date].

**Overdue, SMS** (research 2026):
> Hi [first name], it's been [weeks] weeks since your last [service]. Want me to grab you a spot this week? [booking link]

**Founder note to past buyers in a slump** (115-pt thread, plain text):
> Hi [name]! I just wanted to check in and see if you enjoyed the [product]. We're offering 10% off to past customers because we loved them. I'm the founder if you need anything or want to tear apart the product so I can learn.

**Sunset, last email** (NX and aaron-he-zhu patterns, MIT/Apache-2.0):
> Subject: Should we keep writing to you?
> We only want to email people who want to hear from us. If you'd like to stay, click here: [Keep me subscribed]. If not, you don't need to do anything; we'll stop on [date].

## Referrals

**Subscription anniversary, sent personally from the founder's inbox, not automated** (154-pt thread):
> Hi [name],
> I'm a founder, thank you for being a subscriber for a year, if there is anyone you know who would love [Your Company], I would be happy to send them a [Your Product] (on us of course).
Put a 10% subscription coupon insert in the gifted box.

**After a job, with capacity named** (operator, 3-pt comment, learned from experience):
> "I have a couple of openings next week if you have any friends who need [service]. Here's a few cards, most of my best customers come from referrals so pass on my info."

**Education or coaching, outcome-anchored** (research 2026 synthesis):
> You mentioned that [specific measurable result] has improved since we started. If you know one [parent/student/professional] dealing with [same problem], I have two assessment slots before [date]. I'm happy to run the same baseline assessment for them. If they join, I'll add [specific one-off benefit] to your next block.

**When a client tries to tip a no-tip business** (19-pt comment):
> "Only hugs, referrals or reviews accepted."

**Customer who might have an audience** (Mantry founder, 116-pt thread):
> Would you consider sharing a message with your followers? No worries whatsoever if you can't, we're just trying to grow the old-fashioned way.

## Payments and memberships

**Failed payment, day 0** (coreyhaines31 churn-prevention, MIT, tone rule):
> Hi [name], your payment for [membership] didn't go through. Nothing's lost; you can update your card here in under a minute, no login needed: [link]. If something changed, just reply.

**Pause offer instead of cancel:**
> Want to pause instead? You can pause [membership] for 1, 2 or 3 months and it restarts on [date]. We'll remind you a week before.

## SMS campaign shape

**Offer SMS** (research 2026, built against Attentive 2026 findings: concrete benefit, exact offer, deadline, no superlatives or jargon):
> [Brand]: [specific benefit/offer]. [Proof or deadline]: [branded short link] Reply STOP to opt out.

**Restaurant direct-order nudge** (research 2026; inside your own channels, never inside a marketplace bag where terms forbid it):
> Next time, order direct at [short URL]. Direct orders earn [loyalty benefit] and give you access to our online-only [bundle/drop].

## Moving location or leaving a platform

- Tell regulars before you move. A massage therapist who didn't saw clients track her down upset (5-pt comment).
- A stylist used a $0.01 Venmo payment, the channel clients had tipped through, to tell former clients her new location (3-pt comment). Check non-solicit terms with the old employer first; treat this as a one-off notice, not a marketing channel.
- ESL teachers leaving a platform exchanged WeChat QR codes in the final lesson and kept a full schedule for years (25-pt thread). Check the platform's terms; many forbid moving students off-platform.
