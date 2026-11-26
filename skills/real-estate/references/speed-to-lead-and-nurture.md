# Speed to lead and long nurture

Real estate leads are slow to close and fast to go cold. Both clocks matter: the first 5 minutes decide whether you are the agent they talk to (54% of buyers hired the first agent they contacted, Zillow 2026), and the next 6 to 24 months decide whether you are still the one they call when they are ready.

## Diagnose before you fix

```
two-way contact rate = leads with a real reply or conversation / leads
appointment rate = consultations or listing appointments / two-way contacts
agreement rate = signed buyer agreements or listing agreements / appointments
close rate = closings / agreements
median first response = minutes from inquiry to first human reply (staffed hours and off hours separately)
orphan leads = leads with no owner or no next action due
```

- Low two-way contact with fast response: lead quality or form friction (Meta forms, "instant valuation" funnels).
- Low two-way contact with slow response: follow-up problem. Fix first; it is free.
- Healthy contact, weak appointments: offer and script.
- Healthy appointments, weak agreements: the consultation or listing presentation.
- Never merge sources into one conversion rate. Source mix can make a team look better or worse while its sales process is unchanged (research synthesis, 2026).

## Lifecycle states

`NEW > ATTEMPTED > TWO-WAY > QUALIFIED > APPOINTMENT > AGREEMENT > ACTIVE > UNDER CONTRACT > CLOSED > NURTURE > LOST or DO NOT CONTACT`

Each state has an owner, a required next action, a due time and an exit reason. "Not now" becomes NURTURE with a reason and an estimated month. "No response" stays separate from "not now". Run a daily orphan-lead report: any lead without an owner or with an overdue action (research synthesis, 2026).

## The first 5 minutes

1. **Auto-acknowledge in under a minute** by text (where consent exists) and email, from a named person, naming the property or request. No pitch.
2. **Call within 5 minutes.** Redfin requires a 5-minute average connection for partners (2025); Realtor.com attempts contact in about 4 seconds. The industry baseline is 10% within an hour (Pied Piper 2026), so 5 minutes is a moat.
3. **If no answer, text and call again at minute 5.** Text first works where people screen unknown numbers. One marketer found an immediate SMS beat calls for LA clients, with calls working best 11:30 am to 1 pm; the introduction text also helps the phone recognize the next call (unverified claim, r/realtors 1025, 2020). Zapier at about $30 a month automated it (same thread).
4. **Messenger leads:** keep the conversation inside Messenger when the form's email or phone is fake (r/realtors 1025, 2020).
5. **Backup owner:** if the primary does not accept in 5 minutes, the lead goes to the backup automatically. Live transfers (ReadyConnect, Zillow) go to whoever is free, not to a round robin queue.
6. **First call goal:** confirm the request, ask whether they already work with an agent, learn timeline and financing, and book one concrete next step (consultation, call with a lender, or a saved search set up together).

The "Answer every single time, even at dinner" discipline is what one agent credits for a 10:1 return on portal spend and later a $25M team (r/realtors 184, 2022). The old "21x more likely in 5 minutes" multiplier is pre-2024 and not from real estate; do not quote it.

## First 30 days (house cadence, not a benchmark)

| Day | Touch | Content |
|---|---|---|
| 0 | call, text, call | as above |
| 0, +4 h | call | if no two-way contact |
| 1 | call + text | one specific: a similar home, a sold price nearby, the HOA fee they asked about |
| 2 | email | 3 listings that fit, from a saved search you created for them |
| 3 | call | "did any of those fit?" |
| 4 to 7 | one touch a day, alternating text and call | each references something new |
| 10 | text | "Should I keep sending homes like these, or has your plan changed?" |
| 14, 21, 30 | call or text | market fact tied to their search |
| 30 | move to NURTURE with a reason and a month, or LOST with a reason | |

CRE brokers' cadence guidance fits slower seller and investor leads: after a first follow-up at 3 to 5 days, one contact method every 5 to 7 days, not "email Monday, call Wednesday, text Friday, email Monday"; reference the property, deal stage or last conversation instead of "just checking in"; test Tuesday evening or Wednesday morning for people busy in business hours (r/CommercialRealEstate 33, 2026).

## Long nurture (months 2 to 24)

Bucket by stated timeline and refresh it every touch.

| Bucket | Engine | Personal touch | Exit trigger |
|---|---|---|---|
| 0 to 3 months | saved search, instant alerts | weekly | consultation booked |
| 3 to 6 months | saved search, daily digest | every 2 weeks | preapproval, lease end date |
| 6 to 12 months | weekly digest, monthly market note | monthly | a home saved 3+ times, a valuation request |
| 12 to 24 months | monthly market note | quarterly | life event, rate move, re-engagement with alerts |
| Seller leads | quarterly home value update, sales on their street | quarterly call | asks for a CMA, lists a home they would buy |

- **Behavior beats calendar.** A lead who saves three homes in a ZIP, reopens alerts after silence, or requests a valuation goes back to a human the same day.
- **Short messages, one open question, then take over by hand when they reply.** One agent automated Facebook Messenger and email nurture with ManyChat and took every reply manually: 22 deals in 12 months (r/realtors 1025, 2020).
- **Meta lead forms need more chasing than portal leads** and a qualifying step before the offer (r/realtors 1200, 2021). Accept a higher CPL to get more commitment.
- **Lead magnets that worked for one agent:** "Hot List of Homes Under $X", "Free Home Seller Guide", "Free Home Buyer Guide", with beds, baths, area and timeline asked before email and phone (r/realtors 1025, 2020). A marketer working with agents found home valuation ads converted best for seller leads, with guides kept for retargeting and nurture (same thread).
- **Seller long nurture:** the research-preferred offer is information an automated estimate will not give, such as likely buyer search bracket, competing inventory, and the price-reduction risk zone (research template, 2026).

## Past clients (forever nurture)

- Closing day: review request, referral ask in group-text form ([scripts.md](scripts.md)).
- Day 30: "How is the house treating you?" plus a vendor list.
- Home anniversary each year: estimated equity change, one sold comp on their street.
- Twice a year: something useful and local, in person where possible (pop-by, event invitation).
- Event triggers: refinance opportunity (pass to a lender without anything of value in return), a listing near them, kids changing schools, lease end for tenants they rented to.
- Keep separate consent for automated texts; a past client's phone number is not marketing consent.

## CRM fields that pay for themselves

`source, sub_source, assigned_to, backup_owner, stage, next_action, next_action_due, timeline_bucket, financing_status, preapproval_lender, has_agent, property_owned, likely_next_event, relationship_type, last_transaction_date, referral_given, review_status, landlord_status, consent_sms (source, timestamp, wording), consent_email, dnc_status, country, state, loss_reason`

Feed expired and FSBO data straight into the CRM and dialer so prospects and clients live in one system (one team used MyPlusLeads into Chime; affiliate link disclosed, r/realtors 184, 2022). Scrub every call list against the National DNC Registry within 31 days and against your internal do-not-call list ([compliance.md](compliance.md)).

## Leverage: ISA, VA, AI

- **Outsource the first call, not the relationship.** The Facebook-ads agent moved first calls to a third party but kept replies personal (r/realtors 1025, 2020). The $25M team used VAs in the Philippines at about $3 an hour for admin and prospecting support (r/realtors 184, 2022).
- **AI drafts, humans send cold outreach.** A multifamily broker found AI-written prospecting emails underperformed his personal emails because the wording read generic (r/CommercialRealEstate 135, 2025). Use AI for listing screening and underwriting drafts (one broker cut first-pass underwriting from 2 to 3 hours to about 10 minutes, 80% complete; same thread), not for the voice of the first contact.
- **AI voice agents count as artificial voice under the TCPA** (FCC, Feb 2024): no outbound AI voice calls without prior express consent. Inbound AI answering for your own number is a different case; still disclose it is an assistant.
- **SLA for the team:** first human reply within 5 minutes in staffed hours, every lead with a next action, daily orphan report, weekly review of response distribution. Improve against your own baseline.
