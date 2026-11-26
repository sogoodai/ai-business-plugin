# Consent and sending compliance checklist

Operating summary as of November 2026, not legal advice. Law follows the recipient's location. Regulated sectors (health, finance, alcohol, cannabis) and carrier rules add stricter limits. Refresh these sources before relying on them: rules moved in 2024, 2025 and 2026.

## Data model first (every jurisdiction)

Store per contact, per channel: `consent_state, consent_source, timestamp, exact wording/version shown, channel, jurisdiction, timezone, last_opt_out, opt_out_scope`. CASL and the Australian Spam Act put the burden of proving consent on the sender; PECR needs consent or a valid soft opt-in. A record with a phone number and nothing else is not a marketing subscriber. The agent fails closed: no provenance, no marketing send.

Separate:
- **Transactional or service** (booking confirmation, reminder, receipt, shipping, payment failure): sent on the relationship, must not carry promotions.
- **Marketing** (offers, newsletters, win-back, review-plus-offer): needs the consent rules below.

## United States: SMS

- [ ] **Prior express written consent** for marketing texts sent with automated systems (TCPA). Keep timestamped records. Statutory damages $500 to $1,500 per message (coreyhaines31 compliance file, MIT).
- [ ] **Disclosure at opt-in:** program name, frequency ("up to 4 msgs/month"), "Msg & data rates may apply", HELP and STOP, terms and privacy links, and "consent is not a condition of purchase" (wording in [templates.md](templates.md)).
- [ ] **Revocation by any reasonable means.** STOP, QUIT, END, REVOKE, OPT OUT, CANCEL and UNSUBSCRIBE must work; honor within 10 business days (FCC 2024 order). Send one confirmation, nothing after. Also treat "please stop texting me" in plain words as a STOP.
- [ ] **"Revoke all" status:** the FCC waived the rule that an opt-out from one message type must stop all unrelated robotexts until January 31, 2027 (FCC 2026). Safe practice: suppress all marketing on any STOP anyway.
- [ ] **One-to-one consent rule:** vacated by the Eleventh Circuit in January 2025. Lead-generator consent still carries risk; collect your own.
- [ ] **Quiet hours in recipient local time.** Federal window 8 am to 9 pm. Twilio's October 2025 toolkit applies 8 pm ends in Alabama, Florida, Louisiana, Maryland, Mississippi, Oklahoma, Tennessee and Washington; Connecticut and Nevada end at 8 pm with later morning starts; Texas has separate rules. Default for small senders: 9 am to 8 pm local, no Sundays or holidays unless the owner checks state law.
- [ ] **A2P 10DLC registration** before sending from a local 10-digit number. Twilio pass-through fees 2026: $4.50 one-time for sole proprietor or low-volume brand, $46 standard brand, $15 campaign vetting, then $1.50 a month (low-volume mixed) to $10 a month (standard campaign). Approval 1 to 2 weeks; sample messages must match real sends. Provider fees come on top.
- [ ] **Number type by volume** (coreyhaines31, MIT, uncited): under 10k contacts 10DLC; 10k to 100k toll-free (needs verification); 100k+ short code ($500 to $1,000 a month).
- [ ] **No public link shorteners** (bit.ly and similar get filtered); use a branded domain. No ALL CAPS, no "FREE!!!".
- [ ] **Every marketing message identifies the business** and carries an opt-out line on the first message and periodically after.

## United States: email (CAN-SPAM, plus mailbox rules)

- [ ] Accurate From and subject, postal address, working unsubscribe honored within 10 business days (legal floor). Gmail and Yahoo require one-click unsubscribe for bulk marketing and Yahoo expects it honored within 2 days; see [deliverability.md](deliverability.md).
- [ ] Opt-out is the US default for email, but mailbox providers punish unrequested mail; collect opt-in anyway.

## European Union: GDPR plus ePrivacy

- [ ] **Prior consent for marketing by email, SMS and messaging apps** to individuals (ePrivacy Directive art. 13). Unticked boxes, separate per channel, records kept (GDPR art. 7).
- [ ] **Existing-customer exception:** the business's own similar products or services, contact details obtained in a sale, opt-out offered at collection and in every message. National implementations differ; France, Germany and others interpret it narrowly. Keep a country ruleset, not one "GDPR" switch.
- [ ] **Legitimate interest does not replace ePrivacy consent for the send itself** (EDPB Guidelines 1/2024).
- [ ] **Germany:** double opt-in is the established way to prove email consent under German case law (general knowledge, not from the research pass); send the confirmation link before any marketing.
- [ ] **France SMS:** carriers may filter marketing outside 08:00 to 21:30 Monday to Saturday (Twilio France guidelines); avoid Sundays and public holidays; branded domains over shorteners.
- [ ] **Data subject rights:** access, deletion and objection to direct marketing honored without exception.

## United Kingdom: PECR plus UK GDPR

- [ ] **Specific consent for marketing emails and texts to individuals**, unless the soft opt-in applies: details obtained directly in a sale or sale negotiation, marketing for your own similar products or services, opt-out offered at collection, and a simple free opt-out in every message.
- [ ] **ICO updated its electronic mail marketing guidance on 28 April 2026** after the Data (Use and Access) Act 2025. Re-read it before relying on older templates.
- [ ] Business-to-business emails to corporate addresses have lighter rules; sole traders and partnerships count as individuals.

## Canada: CASL

- [ ] Express or valid implied consent, sender identification and a working unsubscribe in every commercial electronic message.
- [ ] Express consent lasts until withdrawn. Implied consent from an existing business relationship has time limits (24 months after a purchase per coreyhaines31 compliance file, MIT; inquiries are shorter, check the CRTC guide).
- [ ] Unsubscribe link valid at least 60 days; process requests within 10 business days (CRTC FAQ).

## Australia: Spam Act

- [ ] Consent (express or inferred), sender identification and a functional unsubscribe.
- [ ] Honor unsubscribes within 5 working days; keep the mechanism working at least 30 days; no login or extra data to unsubscribe (ACMA).
- [ ] ACMA said in 2026 that a one-off purchase or inquiry generally does not by itself justify inferred consent for ongoing marketing.

## WhatsApp (all countries)

- [ ] Explicit WhatsApp opt-in that names WhatsApp and the business, collected before marketing templates. Opt-in can be collected in chat, on a form or at checkout.
- [ ] Utility templates only for genuinely transactional content; Meta reclassifies mixed content as marketing and can pause templates. Details: [whatsapp.md](whatsapp.md).

## Reviews and incentives (all channels)

- [ ] No reward conditioned on a positive review; no review gating (asking only happy customers). Google prohibits incentives, selective solicitation and staff quotas; the US FTC rule effective 21 October 2024 bans fake and sentiment-conditioned reviews. Yelp says do not ask for Yelp reviews.
- [ ] A referral reward for a new paying customer is a different mechanism and is fine; in regulated trades, paying referral fees can raise licensing or anti-kickback issues (research 2026), so default to client benefits or reciprocal introductions.

## Before any send, the agent checks

1. Consent for this channel, this purpose, with provenance?
2. Recipient local time inside the window for their state or country?
3. Opt-out line and sender identity present?
4. Has the goal event already happened (bought, booked)?
5. Is the contact suppressed (unsubscribed, bounced, complained, STOP)?
Any "no" blocks the send and logs the reason.
