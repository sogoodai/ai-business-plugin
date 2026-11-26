# Retention, loyalty and regulars

Restaurant-specific design only. Flow builders, consent law (TCPA, PECR, CASL), deliverability and SMS rules: `email-sms-loyalty`.

## 1. Capture identity at the moments guests already give it

Online orders, reservations, Wi-Fi, loyalty signup, receipts, catering forms, event tickets. A QR needs a job: table tent "join and get dessert next visit", receipt "loyalty signup" (research 2026). Generic "scan for our newsletter" converts poorly.

- **In-person trade for signup** (suggested scripts, untested): "Get a free drink today if you sign up for our anniversary special!" or "Free jumbo fries upgrade if you join our birthday club!" Birthday only with a reliable date and consent.
- **List growth math:** 5,000 subscribers in 12 months needs about 14 opt-ins a day (ai-restaurant-claude, MIT).
- **Separate the launch crowd from the trade area:** tag signups by postcode and intent (dine-in, coffee, catering, private events) so the first post-opening campaign does not go to hundreds of party guests who will never return (research report 2026).

## 2. Four triggers before any newsletter

Blasts returned 0.27% of recipients against 7.2% for welcome and 6.5% for at-risk win-back (Bloom 2025 to 2026). Build in this order, each with an exit condition (visit or order) and a 10 to 15% holdout where the list allows:

1. **First visit, within hours:** thanks plus one specific high-contribution item to try next time and the direct link.
2. **Second-visit nudge at the format's return window:** coffee and bakery days, QSR one to two weeks, casual dining weeks, fine dining months, catering buyers on their own meeting cycle. Measure each format's real gap from POS data.
3. **Lapse by each guest's own rhythm:** normal gap = median of that guest's own gaps (3+ visits); quiet at over 2x, gone at over 3x; with fewer than 3 visits use the business median and label it an estimate. Rank by past value. A guest who left a bad review then went quiet gets a call, not a coupon (anthropics small-business, Apache-2.0).
4. **Milestone at visit 4 (and 10):** recognition plus a reward. Paytronix's 2026 data shows behavior shifting sharply at four visits; its 95% retention figure for four-visit members carries heavy survivorship bias.

The welcome offer ladder from ai-restaurant-claude (MIT): free appetizer on first return, valid 60 days; day 3 the signature dish's story; day 10 "Did your free appetizer expire?" if no visit. Win-back at days 60, 75 and 90 (adjust to the format): what changed and a comped starter; a 3-question survey; a last note with permission to unsubscribe. No discount on the first touch for high-value regulars; recognition first.

Frequency caps (ai-restaurant-claude): at most one promotional email a week and 2 SMS a month. US marketing texts need prior express written consent, quiet hours 8 am to 9 pm local, opt-out honored within 10 business days (digital-marketing-pro compliance file, checked Oct 2026). Details: `email-sms-loyalty`.

## 3. Loyalty program design

**Benchmarks (vendor, self-selected members):** return near 30% for members vs 7% baseline (Toast Q1 2026); 90-day active 66 to 72% in the best segments, under 50% in casual dining, bar and grill down 13% with nearly 3 in 4 new members not returning (Paytronix 2026); QSR members +40% spend and +64% frequency (Square 2025); Square loyalty sellers +40% visit frequency.

**Design rules:**

- **Measure activation, not enrollment.** The KPI is 90-day active rate and visits per member against a holdout, with redemption cost netted out.
- **Time to first reward under one normal visit cycle.** More than half of diners left a program because rewards were too hard to earn (Toast 2026).
- **Reward type by format:** casual and QSR, simple cashback or a common item (cashback 24 to 26% 90-day retention, Toast); fine dining, an item or experience (appetizer or dessert 20% vs cashback 13%); coffee and bakery, a punch card or app stamp when identity capture is weak.
- **Redeem the usual order.** Excluding the extra protein at first redemption lost a guest spending $25 to $30 four times a week (operators report).
- **Know when it won't work:** a boba shop living on passersby tried stamp cards and points without building regulars (105 upvotes). Loyalty needs a plausible repeat; for tourist or transit trade, invest in reviews and location instead.
- **VIP touches** (ai-restaurant-claude): a one-year anniversary gift waiting at the host stand, early access to events and drops instead of permanent discounts.

## 4. Recognize regulars in person

- **Names with a description in phone notes:** "Bob, very tall, weird mustache" (operators report). Train staff to greet known regulars without overdoing it.
- **Personal touches cost nothing:** latte art made for what the guest is doing (heart, spade and clover for a table learning card tricks), the regular's drink started when they walk in.
- **Teach the order:** "I know all the barista speak can be really confusing if you aren't used to it. Do you want me to tell you exactly what to ask for next time so that it's easier for you to get what you want and I don't have to bug you with all my questions?" Most guests were happy (former barista).
- **Never complain about a guest within earshot.** A regular spending about $55 three times a week (about $8,580 a year) heard "he never tips" and left. Fix the staff problem instead: a manager serves the habitual non-tipper and his sales come out of the server's tip-out; a small perk for whoever serves him; one owner offers to double any tip he ever leaves, which turned it into a game (operators report).
- **Long-stay regulars:** let them linger when tables are free; when demand builds, move them ("we have a few families waiting, any chance we can move you to the bar for a while?") or give a time ("we'll need this table in two hours for the dinner rush"). A 38-seat cafe reclaims tables from bottomless-coffee laptop guests as soon as it gets busy; a 120-minute limit at the bottom of the menu covers busy shifts.
- **Protect what regulars come for:** new owners who replaced a scratch tomato soup and half the menu with frozen equivalents emptied the room; an LA vintage venue sees atmosphere in 80% of its reviews and keeps it. Reliable hours matter more than any campaign.

## 5. Complaint recovery

- **Frontline staff can fix it on the spot.** A weekly burger guest was told twice to "call the manager", got no callback after three tries, and posted a negative Google review that also got no reply (operators report).
- **Answer documented complaints, even without a refund request.** A years-long delivery regular emailed a photo of mold in a cake, got no reply and never ordered again; an apology would have kept them.
- **Don't promise a callback you can't make.** The broken "I'll call you in half an hour" escalated a dispute more than the food did.
- **Good regular, first incident:** refund and offer the next meal; if the same claim repeats, stop. For hair-in-food claims, comp the dish and record the name and phone to spot repeats.
- **Serial comp-seekers:** check the meal midway and note the answer; a finished meal is not comped. Tell repeat send-back guests before they order that remakes are no longer available ([scripts.md](scripts.md)). A habitual complainer told he had "used up our goodwill" stopped complaining and became a promoter (operators report).
- **Fix your own process errors generously:** the four double-pineapple pizzas were replaced in full for a group that orders 2 to 3 times a year; cheaper than the review.
