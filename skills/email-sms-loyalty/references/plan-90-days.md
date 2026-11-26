# 90-day plan

Each block ends with an exit check. Do not start the next block while its exit check fails. The owner approves lists, offers and every first send of a new flow.

## Days 1 to 15: instrument and stop leakage

- Connect POS, booking or store data to the ESP/CRM. One customer record with: `customer_id, email, phone, whatsapp_id, jurisdiction, timezone`, consent per channel (state, source, timestamp, wording version), first and last purchase or visit, order or visit count, lifetime gross margin, last click or reply, favorite product or service, expected next date, acquisition source.
- Audit consent on every existing contact. Tag "no provenance" contacts as transactional-only.
- DNS: SPF, DKIM, DMARC `p=none` with reports, branded sending subdomain, one-click unsubscribe, Postmaster Tools ([deliverability.md](deliverability.md)).
- SMS: STOP/HELP handling, opt-in disclosure, 10DLC registration started if US ([compliance.md](compliance.md)).
- One measurement table: delivered, clicked or replied, purchased or booked, net revenue, gross margin, unsubscribes, complaints.
- Compute: flow share, normal gap per customer, quiet and gone lists, replenishment days by SKU or service.

Exit check: a Gmail test send shows SPF, DKIM and DMARC PASS; every contact has a consent state; the quiet list exists ranked by value.

## Days 16 to 30: the four highest-value automations

- Ecommerce: welcome, checkout/cart, post-purchase, back-in-stock or replenishment.
- Local service and beauty: new-client welcome, missed-call and quote follow-up, post-visit review plus rebook, due-soon.
- Restaurant: signup welcome, first-visit to second-visit, lapse by rhythm, visit-four milestone.
- Educator: lead magnet nurture or mini-course, trial follow-up with summary and worksheet, progress report every 3 to 5 sessions, renewal before the package ends.
- Every flow has an exit on purchase, booking or reply and a 10 to 15% holdout where the list allows.
- Templates from [templates.md](templates.md), rewritten in the owner's voice.

Exit check: no one received a "forgot something?" after buying (check logs); each flow has sent at least 50 messages or two weeks have passed.

## Days 31 to 45: capture

- Baseline signup rate by source: popup, checkout, booking, counter, QR, Wi-Fi.
- One controlled test: delayed vs immediate popup, value exchange vs discount, or single vs multi-step.
- Add four questions after the email field; unique QR per placement; unticked opt-ins in booking and Wi-Fi.
- Keep incentive economics in contribution terms ([capture.md](capture.md)).

Exit check: signup rate per 1,000 visitors and per 100 transactions known by source; duplicate signups measured.

## Days 46 to 60: SMS and WhatsApp, selectively

- SMS into cart (carts over $30 to $50), back-in-stock, rebook, gap fill and expiry. No weekly blast calendar.
- WhatsApp where it is native: utility and service first, then one narrow marketing template with buttons ([whatsapp.md](whatsapp.md)).
- Track reply rate, booked-from-reply, opt-out per send (pause above 2 to 3%), gross margin per message.

Exit check: opt-out per SMS send under 2%; no marketing message sent outside the recipient's window (check logs).

## Days 61 to 75: loyalty or membership experiment

- Choose one behavior: second visit within 30 days, rebook before leaving, second order within the cycle, course or package renewal, maintenance plan signup.
- Smallest reward that could move it; first reward inside one or two normal cycles; pre-stamp if it's a card.
- Holdout or matched comparison group. Judge on 90-day visit or order frequency and margin after rewards, not enrollment ([loyalty-and-referrals.md](loyalty-and-referrals.md)).
- Referral ask wired to a moment (post-visit, anniversary, milestone) and routed to spare capacity; reward on paid conversion.

Exit check: reward cost per incremental visit or order computed; redemption rate over 15% or the threshold is lowered.

## Days 76 to 90: the learning loop

- Per flow with enough volume, test one variable: timing, offer, CTA, proof or framing. Save treatment, audience and result.
- AI drafts the next variants from that history, not from a blank prompt.
- Sunset the unengaged; review complaint and unsubscribe trend before raising campaign frequency.
- Add campaigns only where they are inventory or lifecycle based (openings, drops, events, seasonal peaks).

Exit check at day 90, five questions answered with numbers: which flow makes the most contribution per recipient; what share of email and SMS revenue is automated; how many quiet customers came back and at what cost; is complaint rate under 0.1%; which loyalty or referral mechanic beat its holdout.

## Owner questions to ask along the way

1. Which offers are allowed, and what is the floor margin?
2. Who replies to customer replies, and how fast?
3. Which days, providers or products need demand this month?
4. Who may approve a send when the owner is away?
