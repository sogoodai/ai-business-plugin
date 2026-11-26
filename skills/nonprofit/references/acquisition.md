# Acquisition: donation page, Ad Grants, paid, P2P, mail, events, partners

Order of work for a small organization: donation page and fraud defense, then existing-list reactivation, then Google Ad Grants and search pages, then volunteer and peer-to-peer acquisition, then local partnerships, then paid Meta and paid search, then mail. This order is a resource call derived from the channel economics below, not a benchmark.

## 1. The donation page (fix before any traffic)

Why first: median visitor-to-donor is 1.6% and small-org mobile completion is 4% versus 8% for all orgs (M+R 2026). Moving a 4% mobile form to 8% doubles every channel at once.

Checklist:

- **One page, no redirects, no account creation.** Name, email, card or wallet, address only if required for receipts or Gift Aid.
- **Wallets:** Apple Pay, Google Pay, PayPal, Venmo in the US. 79% offer PayPal, 57 to 58% offer Apple and Google Pay (M+R 2026). Check the processor supports them on the embedded form, not only on a hosted page.
- **Headline names the outcome.** A specific-impact headline doubled conversion (17.6% to 36.5%) but cut average gift from $115.69 to $40.72 (NextAfter 2026). Judge every test on revenue per visitor, not conversion.
- **Monthly visible, testable as default.** See [retention-and-recurring.md](retention-and-recurring.md). Never a prechecked hidden box: a political fundraising operation that prechecked recurring and "double" boxes ended up refunding $122 million (thread title, 138 upvotes; reported in 2021 press).
- **Gift array** anchored on the median gift of that audience: middle option near the median, one above, one below, plus "other". Show what each amount does only if program staff can stand behind the unit.
- **Proof near the button:** one line of verified impact, a charity number or EIN, a short "where the money goes" line. 69% of the public in England and Wales say transparency over money raised and spent makes them more likely to support a charity (Charity Commission 2025).
- **Option to cover fees,** unchecked.
- **Static hero, no homepage carousel.** A static treatment lifted featured clicks 1.9% to 3.9% and primary CTA clicks +238% (NextAfter 2026, 40,756 observations).
- **Confirmation page does work:** monthly upgrade offer for one-time donors, share link, "what happens next".

**Card-testing defense** (operators report, 93-upvote thread, top answer 145 upvotes). Bots run stolen cards through $1 to $5 gifts; chargeback fees can turn a $10 fake gift into a $40 loss.

1. Hidden honeypot field; reject any submission that fills it.
2. Reject forms completed faster than a human can (the operator used 10 to 15 seconds; bots finished in 1 to 2).
3. reCAPTCHA v3, threshold around 0.8, accepting that a few real donors get challenged.
4. Processor velocity filter: no more than X attempts per card, IP or email in Y minutes.
5. After 5 consecutive failures, route further attempts to a dead endpoint so they never reach the bank.
6. Alert on bursts of confirmation emails; void suspicious small charges before settlement.
7. Prefer processors whose fraud screening declines before charging (one operator reports Stripe Radar did).

What did not work: raising the minimum to $25 (still 25 to 30 fake charges a day) and strict billing-address matching (stolen datasets include addresses, and it blocked real donors).

## 2. Google Ad Grants

**What it is.** Up to $10,000 a month of Search ads (about $329 a day), no rollover, no required spend, served in a separate auction after paying advertisers, so grant ads often show below paid ads and on long-tail queries (Google 2026). Eligibility runs through Google for Nonprofits; government entities, hospitals and medical groups, and schools and universities are excluded. Organizations without their own validated charity status (many fiscally sponsored projects) generally cannot enroll; confirm with the sponsor.

**What it is good for.** M+R 2026 median: 229 visits per $1,000, $793 of grant per donation, $0.17 returned per grant dollar. So the grant feeds service requests, volunteers, event sign-ups, email sign-ups, petition and resource downloads, and church visits. Donations come later, through the email journey.

**Compliance list** (Google Ad Grants policy compliance guide, checked November 2026):

| Rule | What to do |
|---|---|
| 5% account CTR each month | Two consecutive months under 5% can deactivate. Filter last 7 days, sort keywords by impressions, pause high-impression low-CTR keywords until the account is back above 5%. |
| No single-word keywords | Exceptions: own brand, recognized medical conditions, some listed terms. Find them with a "keyword text does not contain a space" filter. |
| No overly generic keywords | "free videos", "today's news" style terms must go. A below-average landing page experience is a hint. |
| Quality Score 1 or 2 | Pause or remove. Automate a daily rule (check the rule condition: Google's own example has had it wrong). |
| At least 2 ad groups per campaign | Tightly themed, matching ads and landing pages. |
| At least 2 sitelinks | Account level. |
| Geotargeting | Where you serve. National only if you truly serve nationally. |
| Conversion tracking | Required for accounts created since January 2018 and for Smart Bidding; at least 1 meaningful conversion a month. A conversion rate near 100% is treated as a tracking error. |
| Annual program survey | Sent to the login email; missing it can suspend the account. Turn notifications on. |
| Website | Owned by the org, HTTPS, clear mission, no heavy commercial activity or ads. |

"Two ads per ad group" appears in older guides; it is a performance practice, not a current hard rule (EthicalSaving Ad Grants autopilot, Apache-2.0). The old $2 max CPC cap applied to manual bidding; current guidance points to conversion-based bidding.

**Bidding.** Maximize Clicks only to gather data when there is no conversion history. Switch at about 15 to 30 conversions in the last 30 days to Maximize Conversions, or Maximize Conversion Value if donations are tracked with value (Google 2026). Target CPA or ROAS once volume is stable. Current setup guidance supports Search and Performance Max campaigns; do not apply Search structure rules to Performance Max.

**Conversion hygiene before Smart Bidding** (adapted from EthicalSaving-gUG/google-ad-grants-autopilot, Apache-2.0):

1. List every primary conversion action.
2. Map each to a real mission outcome (donation, volunteer application, service request, call over 60 seconds, newsletter sign-up, event registration).
3. Demote page views, scroll depth, time on site, outbound clicks and legacy imports to secondary.
4. Check custom goals: they can keep a secondary action biddable.
5. Fire a test conversion and confirm it records once.

**Account structure by intent** (one landing page per cluster, never the homepage):

```
Brand: [org name], [org name] donate, [org name] volunteer
Services: "[service] near me", "help with [problem] [city]", "free [service] [city]", "[condition] support group"
Learn: "signs of [condition]", "how to [problem]", "what to do when [situation]"  -> resource page with email capture
Volunteer: "volunteer [city]", "volunteer opportunities [cause]", "volunteer with kids [city]"
Give: "donate [item] [city]", "[cause] charity [city]", "where to donate [item]", "GivingTuesday [cause]" (seasonal)
Church: "church near me" style queries, "[denomination] church [city]", "Christmas Eve service [city]", "Easter service [city]"
```

**Tricks most owners miss**

- Run the "Learn" cluster to a genuinely useful page with an email offer; that is where most grant traffic converts.
- Seasonal campaigns turn on and off: food drives in November, school supplies in August, Christmas Eve and Easter for churches, volunteer queries in late December and January.
- Add exact and phrase variants of the search terms that already convert; mine the Search Terms report weekly and add negatives.
- Underspend is normal on narrow missions. Do not loosen keywords to spend the grant; that kills CTR.
- Use the grant for brand protection; it costs almost nothing and props up account CTR.
- Agencies sell Ad Grants management. Ask for the conversion list and the CTR history before paying; an account counting page views is a red flag.

## 3. Paid Meta and paid search

- M+R 2026: nonprofits spend about $0.10 on ads per $1 of online revenue; 58% of spend is direct fundraising, but small orgs split 38% direct and 37% brand. Paid search returned $2.48 per $1; display $1.11; video $0.56; TikTok $0.04.
- **Optimize Meta to the donation event** whenever there are enough donations to learn. In a controlled test with the same creative, audience and budget, donation optimization converted 0.47% of reached people to donors versus 0.03% for email-sign-up optimization (NextAfter, Dec 2025 to Jan 2026). If donation volume is too low, run lead optimization temporarily and graduate.
- **Report the whole chain:** spend, leads, first donors, cost per first donor, 90-day revenue, second-gift rate, 12-month value.
- Lead-gen ads into an email journey can still pay, but only if the journey converts leads to donors; measure the lead cohort's 90-day donor rate before scaling.
- Paid branded and high-intent search ("donate to [org]", "[cause] charity") can sit beside the grant to win the top slots the grant cannot reach.
- Meta classifies many cause ads as social issue ads in some countries: authorization and "Paid for by" disclaimers apply. Check before launch.
- Account mechanics, creative testing, CAPI and budgets: `paid-ads`.

## 4. Facebook, PayPal Giving Fund, GoFundMe

- Facebook and Instagram donation tools increasingly run through PayPal Giving Fund in the US: no PPGF fee to charity or donor (partner and currency fees can apply), funds paid to the charity's PayPal, donor data only when the donor opts in (PayPal 2026). Availability differs by country; check before planning a birthday-fundraiser push.
- PayPal's standalone "Fundraisers" product stopped accepting new fundraisers on 7 October 2024. Do not plan around it.
- GoFundMe auto-created pages for about 1.4 million nonprofits without consent, then made them opt-in only after backlash (79 upvotes). Check whether a page exists for the org, claim or remove it, and make sure donations land in a channel that gives you donor data.
- Third-party platforms often withhold donor emails. Every platform gift is a donor you cannot thank properly. Push your own page first; use platforms for reach.

## 5. Peer-to-peer

- Activation is the lever, not sign-ups. Raisely's customer base: 76% activation, $159 per activated profile in 2024, down from $202 in 2023.
- **First-hour nudge** after registration (adapted from the research report): "You're in. The fastest way to get your first gift is to ask the three people most likely to say yes. Send this now: 'I'm raising $[goal] for [specific outcome]. I'm starting with people I know will understand why this matters. Would you be one of my first three donors?'"
- Self-donate first: fundraisers who give to their own page first set the anchor; suggest it.
- Default goal low enough to beat ($300 to $500 for a community event); raise it when they hit it.
- Track: registration to activated page, activated to first gift, donors per fundraiser, median dollars per fundraiser, and share of P2P donors who make a direct gift within 365 days. P2P donors give to their friend, not to you, unless the journey moves them.
- Recruit fundraisers from volunteers, board, monthly donors and past participants, in that order.

## 6. Direct mail

- Active-donor mail is a profit center ($4.51 per $1); lapsed mail breaks even ($0.90); prospect mail is an investment ($0.41) (M+R 2026). Average mail gift $120; cost per donation $21 active, $69 lapsed.
- UK: warm charity mail 11.5% response and £10 per £1; cold 0.7% response, £0.20 per £1, £161 per acquisition (JICMAIL 2022 to 2025 via Fretwell).
- Small shops: mail the active and recently lapsed file at year-end and one spring appeal before testing any prospect mail. Hand-addressed envelopes and a real signature for the top 100 donors.
- Kill prospect mail only on 12 to 24 month cohort value, never on first-gift ROI.
- Do not mail gifts nobody asked for: an r/nonprofit thread complaining about personalized address labels hit 162 upvotes. Premiums cost money and teach donors to give for the trinket.

## 7. Events

Classify every event result in four buckets: net cash, first-time donors, new major-gift prospects, new volunteers or ambassadors. Net math in [economics.md](economics.md).

- **Galas.** Operators report $355k against a $500k goal (188 upvotes), $320K gross and $175K net with over a quarter of sponsors leaving seats empty (180), and two galas "basically a wash" (117). Sponsors are shifting from event sponsorship to program funding (same 180-upvote thread). Lock the date with the board and top donors before paying deposits: one board demanded a date change 2.5 months out after deposits and save-the-dates (117).
- **Smaller formats that keep the net:** a luncheon or cocktail hour with a short program and a paddle raise; a host-committee house party (10 to 30 guests, the host asks); a site visit or "open house" where people see the work. Ask sponsors to fund a program instead of a table.
- **Auctions:** average winning bid about $380 across 4,200+ auctions; experiences and wine-and-dine draw bids (GiveSmart via AFP, 2024). Fewer, better items beat a long table of baskets.
- **Paddle raise ("fund-a-need"):** start at the top level with a pre-committed donor raising the first paddle, then step down. Pre-arrange 2 to 3 lead paddles.
- **Ticketing:** compare net per ticket at your real price, including card processing; platforms quoting "no fees" may exclude card fees or ask donors to tip (78 upvotes). Check box-office hardware compatibility before switching. Put waivers in checkout: one team had only 3 of 560 attendees arrive without a signed waiver (446 upvotes).
- **Chargebacks:** a 15,000-person volunteer-run festival lost every disputed chargeback even with signed terms and a scanned ticket (367 upvotes). Price that loss in; do not count on winning disputes.
- **Mission fit:** an addiction-focused charity debating a cash bar is a reminder to check the event against the mission before revenue (69 upvotes).
- **Thank within 48 hours** and send a follow-up within 2 weeks with what the night funded. Event attendees are a cohort: measure their 12-month giving.

## 8. Local businesses and community partners

Businesses are flooded with asks. One owner's fix was a donation form requiring a year's notice, tax ID and a 500-word essay, and requests dropped to zero (1,092 upvotes, posted in several business subs). So pitch value to the business, not need.

- **Give the business something they want:** exposure to a real local audience. The same thread valued a short in-store video posted by a school's social accounts (a few thousand local followers) over a banner, and suggested starting at $25 before a $500 sponsorship.
- **Signature product partnerships:** a youth camp supplied smoked maple syrup and marshmallows for a coffee shop's "Campfire Cappuccino", $2 a drink in November. Stacking local business matches grew it to $12, then $38, then $75 a cup for the 75th anniversary, with matching capped at 1,000 cups so sponsors knew their maximum (152 upvotes). Tie the product to something only you have.
- **Menu-item fundraisers:** a menu item priced $5 higher with the increment going to the cause, named after the school mascot (1,508 upvotes); pancake breakfasts where the group brings supplies and labor and the restaurant turns on the grill (203). Dine-and-donate nights work when the group fills the room.
- **Merch for donations:** a tribute T-shirt sent to people who donated to a food bank raised $2,235 (1,652 upvotes). Let supporters with an audience run these for you.
- **In-kind policy:** a board-approved acceptance policy with current needs, standing needs and partners who take what you cannot. Script: "We can't accept [item] due to our commitment to the health, safety and wellbeing of our clients." Donors received it as evidence of care (82 upvotes). Stop pickups that cost more than the goods are worth: one bookstore spent about $400 collecting unusable books.
- **Corporate asks:** when a company asks what to buy with $1,000, give a specific list (one operator recommended named fragrance-free skin-care brands over dollar-store lotion). Recognize only donations that reach recipients.
- **Cold outreach to corporate giving teams can work:** a $4M org with no name recognition emailed a $100B+ company's giving team found on LinkedIn and was invited to submit a proposal, despite invite-only philanthropy (357 upvotes). Short, specific, local.

## 9. Search and content

Program pages that answer real queries ("free tax help [city]", "food pantry open Saturday [city]") bring service seekers and future volunteers, and they are what Ad Grants landing pages should be. Page depth: `seo-content`. A church, food bank or community center with a physical location needs a complete Google Business Profile: `local-seo`.
