# Flows: trigger, timing, exit, offer

Verbatim copy for each step: [templates.md](templates.md). Benchmarks: [benchmarks.md](benchmarks.md).

Rules for every flow:

- **Exit condition first.** Purchase, booking, reply, unsubscribe or complaint ends the flow. Write the exit before the first message.
- **One CTA per message.** Plain text or light HTML in the owner's voice beats designed newsletters for small senders (operators report 4x conversion from personal founder emails, 115-pt thread; plain-text founder notes "move the needle" in slumps, 61-pt thread).
- **Discount last, and only to the residual group.** Never in message 1 of cart, win-back or replenishment.
- **Channel by urgency.** If it can wait 24 hours, email it; SMS for carts, stock, same-week openings, appointment changes and expiries (coreyhaines31 sms, MIT).
- **Cap per person.** At most one retention touch a week (finsilabs, MIT); restaurants at most one promo email a week and 2 SMS a month (ai-restaurant-claude, MIT); transactional messages do not count.
- **Suppress overlap.** A person in a cart flow is held out of campaigns that day; anyone who bought in the last 60 days is excluded from abandoned-checkout calls and SMS ("significantly fewer complaints", operator with 1,000 carts, 45-pt thread).

## 1. Welcome

| Business | Steps | Notes |
|---|---|---|
| Ecommerce | E1 now: deliver the incentive or promise, one CTA. E2 +2 d: founder story and why. E3 +2 d: reviews, UGC, bestsellers. Split on "has ordered" (yes exits to post-purchase). E4 +3 d: "your code expires soon". Optional E5 +7 d: last chance to non-buyers only | NX builder (MIT). Klaviyo welcome email $5.75 RPR avg, $13.27 top 10% (2026) |
| Local service, salon | E1/SMS1 now: what to expect, how to book, intake or prep guide. +3 d: who you are, before and after. +7 d: proof. +14 d: first-visit offer expiry if not booked | Adapted from AgriciDaniel local-business template (MIT) |
| Restaurant | E1 now: first-return reward ("show this email", valid 60 days). +3 d: story of the signature dish. +10 d: "Did your free appetizer expire?" if no visit | ai-restaurant-claude (MIT). Bloom welcome 7.2% return vs 0.27% blast |
| Coach, course | 5-day email mini-course solving one specific problem; discovery-call link at the end of email 5 | Operator, 20-pt thread |

Tricks:

- **Resend the welcome offer to non-clickers.** One operator calls the non-opener resend "typically the highest-converting email in the flow" (177-pt thread). Use non-clickers, not non-openers, because Apple preloads opens.
- **Founder-story welcome measured by one store:** opens 51, 39, 35, 32, 37%; clicks 16, 10, 8, 7, 8%; conversion 22.3, 4.5, 2.1, 2.7, 0.4% across 5 emails over 14 days (181-pt thread). Most money is in email 1; later emails earn their place only if a test shows it.
- **Separate email and SMS welcome flows** because the permissions differ (Klaviyo Help 2026).
- **Adapt E1 to the signup source:** quiz result, lead magnet, purchase, booking or Wi-Fi each get a different first line (coleschaffer welcome-sequence, MIT).
- **Welcome unsubscribes run high** (0.87% in Omnisend 2025). Five to seven emails must beat three in a holdout to stay.

## 2. Cart, checkout, booking and quote abandonment

Ecommerce (merged from Klaviyo 2026, finsilabs and coleschaffer, MIT):

| Step | Timing | Content | Offer |
|---|---|---|---|
| Email 1 | 1 to 4 h after checkout start (Klaviyo: 2 to 4 h; test 1 h vs 4 h) | Cart image, price, restore-cart link | None |
| SMS 1 (consent only) | 30 to 60 min | "From [Brand]:" + product + link | None |
| Email 2 | +20 to 48 h | Objection by cart value (below), reviews, shipping and returns | None |
| Email 3 or SMS 2 | 24 to 48 h | Scarcity or incentive | New customers 10% single-use, 48 h expiry; repeat customers free shipping only; VIP (6+ orders or $500+) reminder only |
| Stop | purchase, 48 to 72 h, or 4 messages total | | |

Objection by cart value (coleschaffer, MIT): under $30 "do I need this, is shipping worth it"; $30 to $100 "is it cheaper elsewhere"; $100 to $300 "can I justify it, will it work for me"; $300+ "I need to ask someone".

Tricks:

- **Split by buyer status:** past buyers 2 emails over 2 days, never-bought 3 over 2 days (181-pt thread).
- **Do not run SMS cart recovery under $30 to $50 carts**; SMS cost kills it (finsilabs, MIT).
- **Drop anyone who recovered with a discount 3+ times**; if over 30% of recoveries used a code, move the discount later (finsilabs, MIT).
- **Build a dedicated cart flow for the 1 to 3 products taking most ad spend**, with education, customer photos and shipping times (177-pt thread). Browse abandonment sells why this product beats alternatives; cart abandonment resolves buying-experience worries (same thread).
- **Voice + SMS for high-AOV carts:** email only 8 to 12% recovery, SMS only 12 to 18%, voice + SMS 18 to 25% across about 1,000 abandoned checkouts; position the call as support, cap at 3 calls; 15% beat 10% as the late incentive (operator, 45-pt thread, no control group).
- **At under about 10 carts a day, write recovery emails by hand** (operator with about 8 a day, 115-pt thread).
- **Marketplace coupon timing is not yours:** Etsy sends abandoned-cart coupons within an hour, even to shoppers still browsing. Only enable if margin absorbs it (21-pt and 12-pt comments).
- **Audit flat-dollar codes when prices change.** A $5 cart coupon built when everything cost $30+ was used two years later on a $6 item (operators report).

Service businesses: the cart is the unbooked quote or the abandoned booking page.

- **Missed-call text within a minute:** specific, one question, no demand for contact details. First replies naming the job and asking one question got 60.5% 24-hour reply vs 50.3% otherwise (LeadTruffle, 4,699 conversations, 2026).
- **Inquiry received text:** "hey received your inquiry, sending pricing to your email now!" fixed quotes landing in Gmail Promotions; couples texted thanks and searched spam (wedding photographer, 66-pt thread).
- **Quote follow-up cadence:** same-day quote, 24 h confirmation, day 3 objection question, day 7 named slots, day 14 close the loop, day 30 reactivation for high-ticket non-urgent work (research synthesis 2026). ServiceTitan 2025 reports estimate follow-up adds 1 to 15% revenue for many contractors.
- **Cold or partner outreach follow-up:** two words, "Following up!", three days later; credited with half of opportunities (270-pt thread).

## 3. Post-purchase and post-visit

Ecommerce (NX and coleschaffer, MIT): E1 now, thanks plus what happens next; at delivery + 2 days, split first-time (how to use and care, cuts returns) vs repeat (loyalty thanks, early access); +5 to 7 d review request; +14 d cross-sell framed "customers who got results with X found Y". No selling in the first emails. Klaviyo Shopify templates: thank-you at day 1, post-purchase at day 3.

Branch by purchase count (177-pt thread): order 1 appreciation; order 2 "you're one away from VIP"; order 3 VIP recognition and perk; order 4+ more perks, maybe a gift.

Local service, salon, restaurant:

- **Same day or next day:** thanks + review link + "reply here if anything wasn't right". One operator's next-day automated text (Square appointments, personalized, sent by Twilio) produced 88, 58 and 39 reviews for an esthetician, a massage therapist and a nail tech in a few months (37-pt thread).
- **Review request timing by vertical** (AgriciDaniel, MIT): restaurant 24 h, salon or spa same day, home services 24 to 48 h, retail 3 to 5 days, auto 1 to 2 days. Jobber defaults: reminders at day 3 and day 5 if not clicked, no repeat ask to the same client for 6 months (2026).
- **Rebook in the same message for cadence services:** name the date window and two real slots.
- **Physical reminders work too:** a large sticker on the furnace with your number and the next service date (19-pt and 3-pt comments); a lash aftercare guide on every receipt (operators report).

## 4. Due-soon, replenishment and back-in-stock

- **Trigger before depletion, not after.** Klaviyo example: 30-day supply reminded at day 25, or day 20 by SMS when shipping takes time; at most 1 to 2 SMS (2026). Formula: `median reorder interval - shipping days - buffer`. NX examples: dog treats day 25, 60-day skincare day 50, 14-day coffee day 10; follow-up 3 days later with "other customers reorder every X days" and subscribe-and-save.
- **Services:** due-soon = the client's own median gap or the service norm; message just before it with two slots. "Your color will start shifting around 6 to 8 weeks, that's the best time to come back" said at checkout produced "noticeably more" rebooking (129-pt thread).
- **Back-in-stock is the highest-intent, least-used flow:** 6.72% conversion and $9.14 per email, used by 0.6% of brands (Omnisend 2025); p75 SMS 13.80% CVR (Postscript 2026). No discount needed.
- **Wholesale accounts:** reorder prompt before the category's cycle (Faire average about 45 days; 60% of reorders happen when stock is under 25%).

## 5. Lapse and win-back by each customer's own rhythm

From anthropics small-business reactivate and churn-signals (Apache-2.0), adapted:

1. Normal gap = median of that customer's own gaps (needs 3+ orders or visits). Fewer: use the business or service median, label it an estimate.
2. Quiet at over 2x normal; gone at over 3x. At-risk at 1.5x is a softer variant (finsilabs, MIT).
3. Rank by past value (lifetime spend, then frequency, then last order size), not by length of silence. "Fifteen names the owner will actually work beat two hundred."
4. A customer who left a bad review and then went quiet gets a phone call, no offer up front ("the apology is the offer").
5. Sequence: day 0 acknowledge the gap, ask what happened, no pitch, under 90 words; +10 days what changed (new service, hours, product), under 80; +28 days one specific, time-bound reason to return, under 70. Any reply stops it; a complaint hands it to the owner.
6. Offer by value tier (finsilabs, MIT): VIP = founder note and early access, no discount; high value = free shipping or included add-on; standard = 10% at the final step only; one-time buyer = 10% off a second order around day 45. LTV over $1,000 and high risk = a human calls.

Category windows when the store has no history (finsilabs, MIT): consumables repurchase 30 to 60 days (at-risk 60+, churned 120+); apparel 60 to 90 (90+, 180+); home goods 90 to 180 (180+, 365+).

Tricks:

- **Value-add before discount.** A salon "Miss You" campaign at 10% off rebooked 26% with no control group (Mangomint 2026); test a low-cost included add-on first.
- **Ask why, with a gift.** Offer a free product to six-month-lapsed buyers for a 10-minute call on why they stopped (25-pt comment). The answer decides whether email can fix it.
- **Owner-signed plain note to past buyers** with a timely hook, a personal detail and "tear apart the product so I can learn" (115-pt thread).
- **Sunset after the ladder:** "should we keep sending?" then suppress, never delete.

## 6. Gap fill and same-week openings (services)

- **Email or text exact openings with what fits:** "Jenna 10:30 to 12:00 Tuesday: Cut and Color." A client booked at once and added color for the first time in years (146-pt comment).
- **Short-notice slots only to established clients**, keeping a 36-hour advance rule for new ones (massage therapist, operators report).
- **One inventory fact and one CTA**, never a discount to the whole list for two empty slots (research 2026). Route to the providers below target utilization.
- **Lull-timed referral thank-yous:** one 20-year owner sends referral thank-you cards only when he sees a lull, to get a controlled bump (operators report).

## 7. Payment, membership and subscription upkeep

- **Failed payments are a flow, not bad luck.** A gym lost about 23% of annual-plan members to cards that stopped processing within four months (1,353-pt thread).
- **Dunning stack** (coreyhaines31 churn-prevention, MIT): card-expiry emails at 30, 15 and 7 days; retries on soft declines at 24 h, day 3, 5, 7 on the day of month that worked before; emails day 0 friendly, day 3 reminder, day 7 "paused in 3 days", day 10 final; one-click update link with no login; "your payment didn't go through", never "you failed to pay".
- **Pause before cancel:** 1 to 3 months, defaulting to 1, auto-resume with emails at day -7, -1 and 0 (same source).
- **Renewal reminder 14 or 30 days before annual charges**; trial-ending email 3 days before conversion.

## 8. Campaigns that earn a place

Only after the triggers run:

- **Inventory and lifecycle campaigns** (openings, back in stock, new drop for past buyers of the category, event with limited seats: 21, 7 and 1 day before, "8 seats left").
- **BFCM** (finsilabs, MIT): T-21 teaser, T-14 preview, T-7 VIP early access, T-3 countdown, T-0 morning launch plus evening reminder, T+3 Cyber Monday to non-buyers only; cap 4 to 5 emails per person that week. Collect SMS three months ahead and send the first text on sale day (193-pt thread). Early access to all buyers if the list is under 15,000, to 2+ order customers above that (181-pt thread).
- **Cadence is earned.** One clothing brand went from 56,000 to 460,000 monthly campaign sends with segmentation, and campaign revenue from $6,800 to $55,000, alongside offer changes (28-pt thread, confounded). Raise frequency only while unsubscribes stay under about 0.3% per send and complaints under 0.1%.
- **Educational drip for considered purchases:** two emails a week for four months, 90% education and 10% pitch, still converting leads five months after opt-in (skincare, 129-pt thread).
