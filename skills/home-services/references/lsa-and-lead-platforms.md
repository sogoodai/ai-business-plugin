# Local Services Ads and lead platforms

Paid lead sources ranked for a typical home-service business: LSA (where eligible) and Google Search for urgent trades; Nextdoor and Meta for visual and recurring services; marketplaces last, as bounded tests. Account structure, bidding and creative depth live in `paid-ads`. This file covers the home-service mechanics.

## Google Local Services Ads (LSA)

### What changed recently

- **Google Verified replaced Google Guaranteed, Google Screened and License Verified** from October 2025 (announced 20 Aug 2025). Google says the badge change does not change ranking. The Google money-back guarantee was phased out; old claims had to concern services booked before 7 Dec 2025 ([Google blog](https://blog.google/products/ads-commerce/google-verified-august-2025/)). Remove "Google Guaranteed" from trucks, sites and scripts.
- **Credits are automated and narrower.** Google no longer credits leads just because the job type or area is not served, and automated credits are unavailable for advertisers in EMEA ([Google help](https://support.google.com/localservices/answer/15100654)). Bad targeting is now your cost, not Google's.
- **Missed calls can be billed.** A missed call during business hours can count as a valid lead if the caller stays on over 20 seconds ([how leads work](https://support.google.com/localservices/answer/7195435); operators saw the policy email for 1 October, r/localseo 25). Repeat contact from the same customer within 15 days is generally not charged again. Charged leads can be reassessed for up to 30 days.
- LSA can now be run alongside Performance Max in the Ads API (`google_local_services_info` on asset groups; country code required for Local Services PMax campaigns, harvest, MIT).

### Eligibility and setup

- Requires business license checks, insurance (amount by category), background checks on the owner and field workers, and a Google Business Profile in good standing. Verification takes about 2 to 6 weeks (harvest: localseoskills, MIT). Requirements differ by country and trade: France, for example, can require liability insurance and licensing checks. Query the country page before launch ([US getting started](https://support.google.com/localservices/answer/6224841)).
- Home categories include plumber, electrician, HVAC, roofer, locksmith, carpet cleaner, garage door, pest control, house cleaner, mover, painter, tree service, handyman; photographers and auto repair exist in some markets.
- A suspended or virtual-office Business Profile blocks LSA. One advertiser spending $150,000 a month lost verification after a Regus virtual office was suspended on the third verification video (r/GoogleMyBusiness 37).
- New business: get 5 to 10 real reviews from full-price jobs first; one new cleaner saw LSA calls begin after 5+ reviews (r/sweatystartup 25).

### How ranking works

Google lists: bid, likelihood of generating a lead, responsiveness, search context, relevance, profile quality, rating and review count, response time, images and completed verification ([ad rankings](https://support.google.com/localservices/answer/7527305)). Google recommends Maximize Leads bidding. Message response time is estimated from the last 90 days once there are at least two message leads.

Operating rules that follow:

- Keep answer rate at 90%+ in listed hours. Return any missed call within 15 minutes and messages within 1 hour (harvest, MIT).
- Pause the campaign during hours you cannot answer rather than collecting slow-response signals and billable missed calls.
- Turn on messaging and booking only if someone replies fast.
- Keep service areas tight and drop unprofitable job types: credits will not rescue them.
- Mark every lead Booked, Completed or Archived. It trains matching and creates your own record.
- Budget cannot overcome poor responsiveness.

### Cost and disputes

- Agency benchmarks: blended $53 per lead, electrical $39, HVAC $51, plumbing $57, booking rate about 44% (SearchLight, Feb 2026); cleaning $33, junk removal $33, landscaping $37, painting $33 (99 Calls, 2026). Cleaning LSA leads rose from $22.94 to $33.21 in a year in the same dataset. Both sell LSA management.
- Dispute window: within 30 days of the lead. Disputable: spam, wrong business, solicitation, duplicate, outside area or job type only where the region still allows it. Credits used to arrive in 1 to 5 business days (harvest, may be dated).
- **Weekly reconciliation (financial control, not marketing):** export LSA leads; for each store lead ID, call or message, charge, duration, disposition and job value; match to the CRM; dispute what qualifies; record credits. Compare billed leads to answered calls: a gap means you are paying for missed calls.
- Test design: set a weekly budget that buys 20 to 30 leads without hurting cash flow, run 4 to 6 weeks, judge on booked and completed CAC against allowable CAC.

### Tricks most owners miss

- Hours on LSA are an auction lever: answer an extra 6 to 9 pm window with an answering service and you compete when rivals show closed.
- Photos and the profile bio count as profile quality. Use real crew and job photos.
- Treat LSA reviews and Google reviews as one ask; never offer anything for them.

## Google Search and Maps ads (home-service notes)

- Search CPL ranges from $46.99 (cleaning) to $228.15 (roofing and gutters) (LocaliQ, Apr 2024 to Mar 2025). Median home-improvement CPC is $8.33 (WordStream 2026), so $25 a day buys about 3 clicks.
- Start with exact and phrase on "[service] + [city]", "near me" and problem terms ("water heater leaking", "no heat"). Send to a service page with click-to-call above the fold, never the homepage.
- Call-only ad creation was removed in Feb 2026 (they stop serving Feb 2027): use responsive search ads with call assets (harvest: claude-ads, MIT).
- Useful headline set: "[Service] in [City]", "Same-Week Appointments", "[4.9 stars / X years / Licensed]", "Upfront Pricing", "Family-Owned", "Book Online", "[Offer]" (research pass, 2026).
- Use dynamic number insertion (CallRail, WhatConverts) on the site and a separate tracked number on ads; keep the canonical number on the Business Profile and citations (r/localseo 26).
- Audit agency call reports by listening. One HVAC/plumbing owner paid a few thousand a month for six months and found two genuine calls among dropped calls with dead callback numbers (r/localseo 27).

## Meta and Nextdoor

- Meta lead-objective CPL averaged $27.66 in 2025, up 21% YoY (WordStream). Lead quality is the issue: Facebook prospects "were not actively seeking" and needed more persuasion than Google leads (knife sharpening, r/sweatystartup 622). Use higher-intent forms, one qualifier question, and judge on booked jobs.
- It works for visual, recurring, local services. A pet-waste operator spends $30 to $50 a day on Facebook and $10 to $15 on Google, takes leads only by text, gets 2 to 5 leads a day and reported $200k first-year revenue; he advises never pausing (r/sweatystartup 529). A new pressure washer spent $500 in month one with zero leads (r/pressurewashing 94). Difference: offer, area and follow-up, not the platform.
- Nextdoor: ads from $5 a day; location-specific copy lifted CTR 17% (Nextdoor 2024). Organic is often better: check neighborhood recommendation requests daily and reply (r/pressurewashing 94); one post produced 3 inquiries and 2 clients, one of whom referred 4 more (r/sweatystartup 158); Nextdoor was 90% of a hyperlocal business's first customers within about 4 miles before Google took over (r/sweatystartup 622). Opportunity Alerts exist for lawn, cleaning, painting, plumbing and pest; Nextdoor's "higher close rate" claims are vendor marketing.

## Lead marketplaces: mechanics and verdicts

No credible cross-trade CPL or close-rate data exists for any of these in 2026. Use only the owner's own numbers.

| Platform | How you pay | What we know | Verdict |
|---|---|---|---|
| Angi | Monthly lead budgets, discounted subscription leads, double opt-in a la carte leads; Contractor+ promo 25% off leads for 30 days, up to 8% quarterly rebates ([Angi filings](https://ir.angi.com/)) | Agency blogs (competitors) claim $15 to $85 per lead, cleaning $15 to $40, HVAC up to $80 to $300, plus a membership fee; leads shared with several pros. A painter "spent thousands" and was left broke (r/sweatystartup 16). | Last resort. Only with sub-5-minute response and a 20 to 30 lead cap. Never sign a long commitment. |
| Thumbtack | Pay when a matching customer contacts or hires you; price set by job size and location; pro controls budget ([Thumbtack](https://www.thumbtack.com/pro/jobs)) | No published price table; your account shows the range. Furniture assemblers report about $1,000 a month part time via TaskRabbit or Angi (r/sweatystartup 18). | Usable for small handyman, cleaning and assembly jobs with instant replies. Track by job. |
| Yelp | Pay per click or ad package; ads in US and Canada | Owners report being charged before promised billing dates ($130 after "free until Nov 1", r/smallbusiness 1,269; $176 after one week, r/smallbusiness 476), keywords and a 15-mile radius re-added, and a $300 credit plus $165 burnt in 16 days. Never solicit Yelp reviews. | Claim the free profile and keep it accurate. Ads only with terms in writing and a weekly check of keywords, categories and radius. |
| Nextdoor | Ads from $5/day; organic posts and recommendations free | See above | Strong for hyperlocal recurring services, especially organic. |
| Bark | Credits, $2.35 each in the US; credits per lead vary by service; credits bought after 1 Nov 2025 expire in 3 months | Paying reveals contact details; follow-ups free. No booking-rate data. | Small test only; buy credits as needed, never in bulk. |
| Houzz | Pro software $199/mo, Teams $399+/mo, ads from $499/mo | Not per-lead pricing | Only for high-ticket visual projects (remodel, landscaping design, painting). |
| Porch | Single leads or budget; "Connection Guaranteed" credit if you meet outreach rules | No public CPL | Same rule as Angi. |
| Care.com | Subscription; solo cleaner paid an $18 background check | One cleaner gets her residential clients there (r/sweatystartup 197) | Fine for solo residential cleaners and sitters. |
| Rover / Wag (pet sitting, walking) | Rover keeps about 20% of the sitter's fee in the US (secondary sources, 2026); owners pay a separate service fee | Marketplace owns the client relationship | Start there for reviews, then move repeat clients to direct booking where the platform terms allow. |
| The Knot / WeddingWire (photographers) | Annual storefront contracts | One photographer had to fight to cancel (r/WeddingPhotography 185) | Read cancellation terms before signing; planners and venues usually beat them. |
| Manufacturer warranty dispatch, Best Buy Geek Squad subcontracts | Lower labor rates paid by the brand ($150 vs $210 appliance labor; $199 to $499 TV installs) | Customers arrive with no marketing cost; leave a brochure (r/smallbusiness 507) | Good for new appliance and AV techs to fill a calendar. |

Marketplace test rules (all platforms):

1. One marketplace at a time, only once answer rate and speed are fixed.
2. Fixed budget for 20 to 30 leads. Log source, lead price, contacted, qualified, appointment, booked, completed, gross profit, and how many competitors also contacted the customer.
3. Measure incremental jobs: a customer who also called you from Google is not a marketplace win.
4. Mark shared vs exclusive leads.
5. Kill rule: after the sample, if the best plausible close rate still cannot reach the GP CAC target, stop.
6. Reply inside 60 seconds to 5 minutes with a message that names the job and asks one question.

## Tricks most owners miss

- A Yelp category error can be fixed fast with a cancellation ultimatum: one owner said "no, change it now or I'm out", got the category restored and $100 credit (r/smallbusiness 476).
- Get every promised credit, billing date and cancellation process in writing before activating any platform ad product.
- AI Mode booking partners are reported to include Angi, Thumbtack, Housecall Pro and Jobber (agency claim, unverified, r/localseo 25). Keep availability and prices current on at least one, and recheck.
- Feed every booked and completed job from every source into one report by gross profit, not leads.
