# Reviews, testimonials and healthcare advertising compliance

Operating summary as of November 2026, not legal advice. Rules follow the patient's and the practice's location and the clinician's license. When a question is legal, say so in one line, point the owner to counsel, their malpractice carrier's risk line, or their licensing board, and keep working on the rest.

## 1. Review requests (all countries)

- Ask every eligible patient the same neutral way after a defined event (discharge, completed treatment, or every Nth visit). No NPS gate deciding who gets the Google link. FTC: the Consumer Review Rule (effective October 21, 2024) does not expressly ban asking only happy customers, but review gating may still violate the FTC Act (FTC Q&A 2026). Google prohibits incentives and selective solicitation tools that discourage negative reviews.
- No incentives of any kind for reviews (Google; FTC rule bans buying sentiment-conditioned reviews).
- Separate private feedback from the review ask; never make private feedback a prerequisite for the public link.
- Remind patients not to include medical details in a public review.
- Staff reviews and family reviews: disclose or skip (FTC insider review rules).
- Channel: the review request is a routine operations message; use the same consent basis as appointment messages in your jurisdiction, and keep it free of diagnosis or treatment detail.

**Therapy is stricter.** Professional codes bar soliciting testimonials from current clients and anyone vulnerable to undue influence:
- APA Ethics Code 5.05 (psychologists): no solicitation from current therapy clients or other vulnerable persons.
- ACA Code C.3.b (counselors): no solicitation from current clients, former clients, or others vulnerable to undue influence.
- NBCC: no solicitation from current clients or their families and friends, nor former clients within 5 years of termination.
- CAMFT and many state boards: vulnerability test; "undue influence" is undefined.
Agent rule for therapists: no review requests to clients at all unless the clinician confirms their code and board allow it. Grow reviews from peers (professional endorsements), directory profiles, and patients who post unprompted. Massage and wellness services that automate review texts after each visit (operators report, 37) are not a model for therapy.

**Dental, PT, chiro, optometry, dietitians, acupuncture:** neutral, universal requests are standard practice. Check state board advertising rules; several boards restrict testimonials about clinical outcomes.

## 2. Replying to reviews (US HIPAA, and good practice everywhere)

- Never confirm or deny a care relationship, never mention treatment, visits, attendance, insurance or outcome. HHS OCR settlements: Manasa Health Center $30,000 (2023) and New Vision Dental $23,000 (2022) over review replies; older but still the enforcement standard.
- Safe reply template: [scripts.md](scripts.md#review-replies). Same text structure for good and bad reviews.
- Do not write: "We're sorry your treatment didn't work," "You missed three appointments," "You were never our patient," "Glad your back feels better."
- Take it offline with a phone number or secure channel, not by name.
- Fake or abusive reviews: flag through Google's process; do not argue in public. Removal mechanics: `local-seo`.

## 3. Testimonials, photos and case stories

- US HIPAA: using a patient's name, image, voice, condition or recognizable story in your marketing is a use of PHI that needs a signed HIPAA marketing authorization. Complete P.T. paid $25,000 for posting patient testimonials and images without valid authorizations (HHS OCR). A public Google review is not an authorization; reposting it on your site or ads needs one.
- Authorization form: specific use (website, social, ads), duration, right to revoke, and a statement if any third party pays you (45 CFR 164.508).
- Filmed sessions for ads (a chiro micro practice's growth engine, operators report, 65) need written authorization from every patient on camera, plus a release covering ads specifically.
- Outcome claims inside testimonials need substantiation (FTC; ASA CAP September 21, 2026 guidance in the UK requires evidence the testimonial is genuine and contact details on file).
- Australia (AHPRA): advertising a regulated health service must not use testimonials about clinical aspects (symptoms, diagnosis, treatment, outcomes, practitioner skill). Patient reviews on independent sites are fine; republishing a clinical one on your website or ads can breach the law.
- Before and after photos (dental cosmetic, some PT): consent, no retouching, typical-result context, and board rules.

## 4. Pixels, analytics and tracking

**US (HHS OCR tracking guidance, current 2026):**
- Authenticated pages (portal), scheduling flows, intake forms, symptom checkers and pages tied to a booking can send PHI to tracking vendors. That needs a HIPAA permission and, where the vendor acts as a business associate, a BAA. Most ad pixels' vendors do not sign BAAs.
- After the June 20, 2024 court ruling, HHS accepts that an IP address on a public condition page is not automatically PHI, but booking and intake flows remain red zones.
- A cookie banner is not HIPAA authorization.
- Red zones to audit: booking confirmation pages, thank-you URLs with condition or clinician parameters, intake form fields, portal pages, chat widgets, call-tracking recordings, event names like `AnxietyConsultBooked`.

**Audit procedure (agent):**
1. List every tag in GTM and hard-coded scripts; open the booking and intake flow with browser dev tools and record every third-party request and its payload.
2. Check URLs and query strings for condition, clinician-specialty or appointment identifiers.
3. Remove ad pixels from booking, intake and portal pages; keep public marketing pages only with neutral events.
4. If conversion signals are needed, use a HIPAA-compliant server-side tool under a BAA that strips identifiers and sends a neutral event (`QualifiedLead`, `AppointmentBooked`).
5. Never upload patient lists to Meta or Google, even hashed, without legal sign-off.

**Platforms:**
- Meta: from September 2, 2025 proactively restricts custom audiences and conversions implying health conditions. Since January 2025 many health and wellness advertisers see lower-funnel events and URL parameters restricted, with severity by business category (agency reports; check Events Manager). Optimize to neutral upper or custom events plus offline-qualified leads.
- Google Ads: health conditions are sensitive interests; no Customer Match, remarketing or first-party segments targeting them. The May 29, 2025 update clarified healthcare-professional audiences; consumer condition targeting stays prohibited. Healthcare and medicines policy requires certification for some services (addiction, online pharmacy, some telehealth).

**UK and EU:** health data is special category; tracking pixels and cookies need consent under PECR, and special-category data for ads needs explicit consent (ICO, updated April 2026). The EU Digital Services Act bars platforms from profiling-based ads using health data (EDPB).

**Canada:** medical information is highly sensitive; online behavioral ads involving health data need express consent (OPC). Provincial health-information laws add duties.

**Australia:** OAIC determinations against Medmate and Monash IVF (June 24, 2026) found that tracking health-site visitors for social ads collected sensitive information requiring consent.

## 5. Inducements, free services and discounts (US)

- Beneficiary inducements: gifts to Medicare or Medicaid beneficiaries are limited to nominal value, $15 per item and $75 a year, never cash or equivalents (OIG policy statement, December 2016). A "free exam" or "free first visit" advertised to everyone reaches federal beneficiaries: either exclude them explicitly or do not run it.
- Routine copay or deductible waivers are risky for federal and commercial plans; use a documented financial-hardship policy.
- Time-of-service discounts: about 5 to 15% tied to billing savings is the defensible range; routine 40 to 50% discounts read as a dual fee schedule (trade-law commentary on an OIG opinion). Never charge insurers more than cash patients for the same service.
- Discount medical plan organizations and in-house memberships: check state rules; Medicare patients cannot buy a membership for Medicare-covered services.
- Anti-kickback: no payment or free rent tied to referral volume between referral partners.
- Chiropractic Medicare: maintenance care is not covered; use the ABN when providing services Medicare will not cover.

## 6. Pricing disclosures (US)

- No Surprises Act: uninsured or self-pay patients scheduling 3+ business days ahead get a written Good Faith Estimate; patients may dispute a bill $400+ over the estimate; post the notice on the website and where scheduling happens (CMS 2026).
- Superbills: never promise reimbursement; the plan decides.

## 7. Claims in ads and content

- No promises of cure, outcome or "pain-free"; no claims the clinician cannot substantiate.
- Specialist titles: many boards restrict "specialist" or "expert" unless board-certified; dentists especially.
- Chiropractic: avoid immunity, vaccination or systemic disease claims; boards and regulators act on them, and trade press keeps the profession under scrutiny.
- Australia: no time-limited offers that encourage indiscriminate use of a regulated service; no misleading comparisons (AHPRA).
- UK: CAP Code health claims and ASA rulings apply to clinic sites and social posts.

## 8. Messaging channels

- First outbound messages and reminders carry no diagnosis or symptom detail.
- Patients may request unencrypted email or text after being warned of the risk (HIPAA right of access practice); record that preference.
- Marketing consent is separate from appointment communication consent. SMS marketing in the US needs prior express written consent (TCPA); depth in `email-sms-loyalty`.
