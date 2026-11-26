# Legal: cold email, LinkedIn and calls by country

Operational guidance, not legal advice. "B2B" is not one global permission. The rule depends on the recipient's country, whether they are a company or an individual (sole trader), the data source, the channel and the content. For programs above a few hundred EU or UK contacts a month, have the setup reviewed by a privacy lawyer once. Sources: [sources.md](sources.md).

## Country rules at a glance

| Recipient | Cold B2B email allowed? | Must include | Opt-out deadline |
|---|---|---|---|
| United States | Yes (CAN-SPAM, no B2B exemption, no consent needed) | Accurate headers and From, non-deceptive subject, identification as an ad, valid postal address, clear opt-out working for 30+ days | 10 business days |
| United Kingdom, limited companies and LLPs ("corporate subscribers") | Yes under PECR, with UK GDPR legitimate interest for the named person | Sender identity, opt-out, privacy information | Promptly |
| United Kingdom, sole traders and some partnerships | No, consent needed (or soft opt-in for existing customers) | | |
| EU | Country by country. GDPR legitimate interest may cover the data processing, but national ePrivacy laws can require consent for the email itself | Source of data (Art. 14), opt-out, privacy notice | Promptly |
| Germany | Effectively no: UWG section 7 requires prior consent for advertising email, B2B included; competitors sue | | |
| Canada | Only with express or implied consent (CASL) | Sender identification, mailing address, unsubscribe | 10 business days |
| Australia | Only with express or inferred consent (Spam Act) | Sender identification, unsubscribe working 30+ days | 5 working days |

## United States: CAN-SPAM (FTC)

- Applies to all commercial email, B2B included.
- Requirements: no false or misleading header information; no deceptive subject lines; identify the message as an advertisement (clearly, not necessarily a label); a valid physical postal address (a registered PO box or private mailbox works); a clear way to opt out, honored within 10 business days and functional for at least 30 days after sending; no charge or extra information to opt out; monitor anyone sending on your behalf.
- Penalty: up to $53,088 per violating email under current FTC guidance. Both the company promoted and the sender can be liable.
- Fake "Re:" or "Fwd:" subjects breach the deceptive-subject rule as well as Google's guidelines.

Footer (compliance-oriented template, not a safe harbor):
> [Legal company name], [postal address]. You're getting this because I believed {{specific business reason}} was relevant to your role. If you don't want further emails from us, reply "unsubscribe" and I'll make sure you don't hear from us again.

Plain-text alternative in the body: "If this isn't relevant, reply 'no' and I won't follow up."

## United Kingdom: PECR plus UK GDPR (ICO)

- **Corporate subscribers** (limited companies, LLPs, public bodies): PECR's consent rule for marketing email does not apply. You must identify yourself and offer an opt-out.
- **Sole traders and some partnerships** are treated like individuals: consent needed unless the soft opt-in applies (existing customers, similar products). Many small agencies, consultancies and trades are sole traders. Check Companies House before sending.
- UK GDPR still applies to the named employee's data: run and record the legitimate-interests test (purpose, necessity, balancing against their reasonable expectations). Public data is not exempt because it is public.
- The Data (Use and Access) Act 2025 raised the PECR maximum fine from GBP 500,000 to GBP 17.5M or 4% of global turnover, and named direct marketing as a recognised legitimate interest (coreyhaines31 compliance reference, MIT). ICO B2B guidance was under review after the Act.
- Marketing calls: screen against the TPS and the Corporate TPS.

## European Union: GDPR plus national ePrivacy

- The dangerous simplification is "GDPR legitimate interest makes B2B cold email legal". The EDPB's final legitimate-interest guidelines (November 2026) say direct marketing can rely on Article 6(1)(f) only after the interest, necessity and balancing tests, and that sector law such as ePrivacy and its national versions can require consent and so rule out legitimate interest for the message itself.
- The CJEU's KNLTB ruling (October 2024) confirmed a purely commercial interest can be a legitimate interest. You still need the written balancing test (a legitimate interests assessment).
- **Article 14:** when the data did not come from the person, tell them the source within a month and at the latest in the first message. One line works: "I found your email on [source]; reply 'remove' and I'll delete it."
- **Public is not free to use:** France's CNIL fined Kaspr EUR 240,000 (December 2024) for collecting LinkedIn contact details that users had chosen to hide.
- **Germany:** exclude from cold email. LinkedIn messages and phone remain, with care: B2B calls need presumed consent (a concrete reason to think they would welcome the call).
- Agent rule: "EU" is never one permission flag. Store a country rule and a lawful-basis record per contact. When uncertain, suppress cold email for that country and use a permitted channel or ask the owner to get legal review.

## Canada: CASL (CRTC)

- Commercial electronic messages need express or qualifying implied consent, sender identification and an unsubscribe mechanism.
- A cold email asking for permission to email is itself a commercial message. You cannot email your way to consent.
- **Conspicuous publication route:** a business address published (for example on the company's own site) without a statement refusing unsolicited messages can give implied consent when the message relates to the recipient's business role. The sender must prove it.
- Existing business relationship: implied consent for 24 months after a purchase or contract.
- Opt-outs honored within 10 business days.
- Record for every Canadian contact: source URL, capture date, whether a "no unsolicited messages" notice was present, role relevance, and the consent basis relied on. "Found in Apollo" is not proof.

## Australia: Spam Act (ACMA)

- Express or inferred consent, accurate sender identification and contact details, an easy unsubscribe working for at least 30 days, honored within 5 working days.
- Inferred consent can come from a conspicuously published business address with no "no unsolicited messages" notice, where the message relates to the person's role. ACMA's October 2026 enforcement report warns that a one-off purchase, enquiry or general contact does not usually create inferred consent.
- You must prove consent even for a purchased list. Address-harvesting software is prohibited.

## LinkedIn and data vendors

- LinkedIn's User Agreement prohibits scraping and automation; see [linkedin.md](linkedin.md). Messages and InMails are still personal-data processing under GDPR and PECR.
- Courts treat scraping public, logged-out pages differently from scraping behind a login or with fake accounts. Neither makes the data lawful to use under GDPR.
- Licensed databases (Apollo, ZoomInfo, Clay providers) carry their own terms: use for your own outreach, no resale, no public sharing. Check how they source LinkedIn-overlap data.
- Google Maps terms forbid bulk extraction and rebuilding listings into your own database. Use the Places API within its terms, keep place IDs, and take retained data from the business's own site.

## Phone and SMS

- **US Do Not Call:** scrub the National DNC Registry and your internal list. Enriched mobile numbers are often personal cells and protected.
- **AI voices are artificial voices** under the TCPA (FCC ruling, February 2024): AI-voiced calls to cell phones need prior express consent, written consent for marketing. $500 to $1,500 per call.
- **Ringless voicemail** is treated as a call under the TCPA.
- Since April 2025, consent can be revoked by any reasonable means and must be honored within 10 business days.
- **Cold SMS to US mobiles** needs consent and 10DLC registration. Use SMS only after the prospect engaged and agreed.
- Call recording: all-party consent in several US states and many countries.

## Gifts and mail

Check company gift policies; regulated industries and government often cap or ban gifts. A themed gift is a marketing message, not a bribe, only when its value is token.

## The contact record an agent must keep

```
source (provider or URL) | collection date | country | entity type (company, sole trader)
lawful basis or consent basis | CASL/Spam Act evidence if CA/AU | verification date and result
suppression status (all channels) | opt-out date and channel | deletion request date
```

## Pre-send audit checklist

- [ ] Every contact has source URL and collection date
- [ ] Country gating applied: Germany excluded from cold email; UK sole traders and partnerships excluded without consent; Canada and Australia only with a recorded consent basis
- [ ] EU/UK first message names where the data came from and how to opt out
- [ ] Postal address and opt-out line in every email
- [ ] One suppression list synced to every sending tool, checked before each touch
- [ ] No scraped LinkedIn data, no harvested personal Gmail addresses
- [ ] Phone numbers scrubbed against DNC; no AI voice or ringless voicemail to US mobiles without consent
- [ ] Legitimate-interest assessment written for EU/UK programs
- [ ] Retention plan: delete prospects who never engaged after a set period

## Tricks most owners miss

- Ask the entity-type question for UK prospects before anything else. A list of "UK small agencies" is often half sole traders.
- "How did you get my email?" is a legal question in the EU and UK. Answer with the actual source and offer deletion.
- Opt-outs on any channel apply to all channels: reply "stop" on LinkedIn means no email either.
- A US-compliant workflow can be unlawful in Canada and Australia. Put the recipient's country on the record before the first send, not after a complaint.
