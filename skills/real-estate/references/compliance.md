# Compliance

Compliance controls belong in the content and sending system, not in a PDF. Before an agent publishes or sends anything, it must know the country, state or province, campaign category (housing, credit), consent state of the recipient and DNC status of the number. Operational guidance, not legal advice; brokers, state law and company compliance teams win.

## Fair housing advertising (US)

- **The law:** the Fair Housing Act bans any notice, statement or ad indicating a preference, limitation or discrimination based on race, color, religion, sex, disability, familial status or national origin (42 U.S.C. 3604(c); 24 CFR 100.75). States and cities add classes such as source of income, sexual orientation, gender identity, age, marital status, military status.
- **2025 change:** HUD withdrew a set of FHEO guidance documents on 17 September 2025 and said it will not use disparate impact; reports list its 2024 guidance on advertising through digital platforms among the withdrawals ([NAR](https://www.nar.realtor/washington-report/hud-withdraws-fair-housing-guidance-documents), [Orrick](https://infobytes.orrick.com/2026-04-10/hud-withdraws-eight-fair-housing-guidance-documents-as-part-of-deregulatory-review/)). The statute, regulation, state agencies and private lawsuits are unaffected, and NAR expects state and private enforcement to continue. Keep conservative rules.
- **Copy rule: describe the property, never the people.** Block phrases like "perfect for young couples", "ideal for families", "adults only" (except qualifying 55+ housing), "no kids", "Christian home", "exclusive neighborhood", "safe neighborhood", "great for retirees", "walking distance to [house of worship]" as a selling point about who belongs, "no Section 8" where source of income is protected. Fine: room counts, square footage, named nearby amenities and transit, school names with links to boundary maps, accessibility features stated as features.
- **Neighborhood content:** amenities, commute, parks, dining, named schools; never demographics, crime characterizations or "who it suits" (UnifAPI neighborhood skill guardrail, MIT).
- **Images:** do not show only one kind of person across all ads; use property images or varied, real clients with consent.
- **Steering in conversation:** answer school and safety questions with sources (district maps, public crime data portals) and let the client decide.

## Ad platform targeting for housing

- **Google** (US and Canada): housing ads cannot target by gender, age, parental status, marital status or ZIP code; advertiser-curated audiences are blocked for sensitive categories ([Google](https://support.google.com/adspolicy/answer/143465)). Canada allows the first three postal code characters per Google's policy page (research summary).
- **Meta Special Ad Category Housing:** age fixed at 18 to 65+, no gender, no ZIP targeting, radius at least 15 miles around a point, exclusions removed; lookalikes unavailable (practitioner guides, 2026; Meta's API enforces restrictions with a hard error, [Meta](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category)). Verify current values in Ads Manager. Mortgage ads fall under financial products and services. Depth: `paid-ads`.
- **No backdoor microtargeting:** do not rebuild protected-class proxies through uploaded lists, modeled audiences or narrow geography without a compliance review (research synthesis, 2026).

## RESPA (US, federally related mortgage loans)

- Section 8 and Regulation X 1024.14 prohibit giving or accepting a fee, kickback or anything of value under an agreement or understanding to refer settlement service business (lenders, title, escrow, agents, inspectors in some arrangements) ([CFPB FAQ](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/real-estate-settlement-procedures-act/real-estate-settlement-procedures-act-faqs/), [Reg X 1024.14](https://www.consumerfinance.gov/rules-policy/regulations/1024/14/)).
- Payments for services actually performed are allowed only at fair market value, with the value of referrals excluded. Co-marketing must be split by actual share of use.
- Digital comparison platforms can violate RESPA where paid placement steers non-neutrally and payment relates to referrals ([CFPB advisory](https://www.consumerfinance.gov/rules-policy/final-rules/real-estate-settlement-procedures-act-regulation-x-digital-mortgage-comparison-shopping-platforms-and-related-payments-to-operators/)).
- Agent-to-agent referral fees between licensed brokers are normal; payments to unlicensed people for real estate referrals are restricted by most state license laws. Closing gifts to clients are generally fine; gifts to referral sources tied to referrals are not.
- Affiliated business arrangements need the written disclosure and no required use.

## NAR practice changes (US, from 17 August 2024)

Written buyer agreement before in-person or live virtual tours; compensation objectively ascertainable and not open-ended; no compensation offers on the MLS; open house visitors need no agreement with the hosting listing agent. See [buyers-and-nar-settlement.md](buyers-and-nar-settlement.md). Private listing rules (Clear Cooperation, delayed marketing disclosure, Zillow Listing Access Standards) are in [listings-and-sellers.md](listings-and-sellers.md).

## TCPA, DNC and state telemarketing laws (calling and texting)

**Calling (prospecting expireds, FSBOs, farms, old leads):**
- Scrub every list against the National Do Not Call Registry using a version no older than 31 days (TSR safe harbor, [16 CFR 310.4(b)(3)](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310)) and against your own internal do-not-call list. Honor do-not-call requests fast and permanently.
- Expireds and FSBOs are not exempt. You may not call a registered number to solicit a listing; a buyer's agent with a real buyer may call a FSBO about that buyer ([NAR](https://www.nar.realtor/telemarketing-cold-calling)). Established business relationship: generally 18 months after a transaction, 3 months after an inquiry; for expireds, state summaries say the former listing firm may call for up to 18 months (verify).
- Federal calling hours: 8 am to 9 pm in the called party's time zone. Florida's telephone solicitation act: 8 am to 8 pm and no more than three calls in 24 hours on the same subject to the same person (2021 amendments; [Quarles](https://www.quarles.com/newsroom/publications/hold-the-phone-florida-passes-new-telemarketing-bill)). Other states (Oklahoma, Maryland, Washington and more) have their own rules; check the state before dialing.
- Autodialers, prerecorded and artificial voices need prior express consent, and written consent for marketing. AI-generated voices count as artificial voice (FCC declaratory ruling, February 2024).
- Exposure: private TCPA suits run $500 to $1,500 per call or text; the FTC's maximum civil penalty was $53,088 per violation from January 2025 ([Federal Register](https://www.federalregister.gov/documents/2025/01/17/2025-01361/adjustments-to-civil-penalty-amounts)).

**Texting:**
- Marketing texts sent with automated systems need prior express written consent with the disclosures in `email-sms-loyalty` (compliance.md). Keep the source, timestamp and exact wording.
- An open house sign-in, a portal inquiry or a closed transaction is not marketing consent for automated texts. Put a separate, unticked opt-in on digital sign-in forms and lead forms.
- Consent can be revoked "by any reasonable means" (FCC 2024 order; compliance dates from April 2025, with the "revoke all" piece delayed to April 2026; check current status). Treat "stop", "no thanks", "don't text me" as opt-outs.
- The FCC's one-to-one consent rule for lead generators was vacated by the Eleventh Circuit in January 2025. Portal and lead-vendor consent still carries risk; collect your own consent at first contact.
- A2P 10DLC registration before texting from a local number; see `email-sms-loyalty`.

## Mortgage advertising (US)

Regulation Z trigger terms require full disclosures (12 CFR 1026.24); state licensing rules commonly require the NMLS ID on ads; no rare-exception promises. See [loan-officers.md](loan-officers.md).

## Outside the US

- **UK:** "leading", "number one" and "market leader" imply sales or share superiority and need substantiation; board counts and portal stock alone are inadequate ([ASA](https://www.asa.org.uk/topic/Property_sales_and_lettings.html)). England from 1 May 2026: letting ads state a specific rent and must not imply discrimination against tenants with children or on benefits ([ASA](https://www.asa.org.uk/advice-online/property-letting-agents.html)). PECR for email and texts.
- **EU:** racial and ethnic discrimination in access to housing is banned (Racial Equality Directive 2000/43/EC, older than 2024 but in force); housing and ad rules vary by member state. Bought lists without provable consent are dangerous: France's CNIL fined Solocal EUR 900,000 in 2025 over invalid prospecting consent, with a EUR 10,000-a-day penalty after the compliance period ([EDPB](https://www.edpb.europa.eu/news/the-french-sa-fines-solocal-eu900-000_fr)). Store consent source, timestamp, channel scope, legal basis, country and opt-out on every contact.
- **Canada:** Google's housing targeting limits apply; the Competition Bureau judges the general impression of an ad, not the fine print ([Competition Bureau](https://competition-bureau.canada.ca/en/deceptive-marketing-practices/types-deceptive-marketing-practices/false-or-misleading-representations)); CASL for electronic messages; provincial privacy and human rights rules vary.
- **Australia:** no misleading price representations; state underquoting rules apply ([ACCC](https://www.accc.gov.au/consumers/specific-products-and-activities/real-estate)). Keep rental application data separate from marketing consent; privacy enforcement is active.

## Pre-publish checklist for the agent

1. Country, state or province, and campaign category known?
2. Copy describes property and services only; no people, preferences or protected-class proxies?
3. Platform special ad category set; no forbidden targeting or proxy audiences?
4. Every claim (sold count, "#1", price, "sold in X days") defined and provable?
5. Mortgage terms: trigger terms disclosed, NMLS ID present?
6. Any partner payment or shared cost: RESPA-reviewed, pro rata, not tied to referrals?
7. Calls: DNC scrub under 31 days old, internal DNC, state hours and frequency?
8. Texts and emails: consent for this channel and purpose on record?
