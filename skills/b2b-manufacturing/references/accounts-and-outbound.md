# Named accounts, triggers and outbound for a small industrial firm

A 1 to 20 person firm does not need an ABM platform. It needs a short list of accounts worth winning, a reason to contact each one now, every person in the buying group mapped, and a seller or owner who follows through. Cold email and calling mechanics (deliverability, inbox setup, sequence tooling, copy testing) live in the `b2b-outbound` skill. This file keeps the industrial angles. Sources in [sources.md](sources.md).

## Why random volume fails here

- Industrial cold email: 38 positive replies from 20,126 first emails, 0.19% (Sales.co, 20 campaigns, Mar to Aug 2026). Operations titles: 1 positive in 2,687. Engineering titles: 0 in 640.
- Cold calls to manufacturers: 7.7% answered (Factur, 439,358 calls, Nov 2025 to Oct 2026). The same program needed about 346 calls and 489 emails per quote and about 1,640 calls and 2,320 emails per PO (our arithmetic on Factur's totals).
- Engineers prefer email first (59%), phone 22%, LinkedIn DM 1% (GlobalSpec 2026).
- Buying groups average 10.2 people and teams that sell to the group, not one lead, report up to 2 to 3x win rates (6sense 2026; Demandbase 2026, enterprise-skewed, directional).
- Only 22% of ABM teams use a dedicated ABM platform; 29% run it in spreadsheets (N.Rich 2025, mostly SaaS).

Rule: shrink the list until each contact has a reason. A list exhausts fast: 10,000 scraped emails at 1,000 a day used up a niche's whole market in three weeks ([r/b2bmarketing 16](https://www.reddit.com/r/b2bmarketing/comments/1m4rfhi/it_took_me_3_years_4_tools_and_thousands_of_cold/)).

## Build the named-account list

**Start from your own wins.** Export 2 to 3 years of invoices. Rank customers by gross profit, not revenue. For the top 10, write down: industry, size, what they buy, why they chose you, who found you, how long to the first PO. That profile is the ICP. Segmenting won and lost deals by firmographics revealed an underserved niche for one seller (complex manufacturers with mixed applications; smaller manufacturers with overworked IT) ([r/salestechniques 74](https://www.reddit.com/r/salestechniques/comments/1t2g6gn/getting_destroyed_in_b2b_sales_dont_know_how_to/)).

**Score every account:**

```
account score = fit (1-5) x value (1-5) x trigger (1-5) x access (1-5)
fit     = capability match: process, material, tolerance, certification, volume, geography
value   = expected annual gross profit if won (1 = under $10k, 5 = over $250k; set bands from your own customers)
trigger = a dated reason to buy now (see list below); 1 = none
access  = a warm path: existing contact, rep, distributor, shared customer, met at a show; 1 = cold
```

Work the top 25 to 100 accounts. Re-score monthly and learn the thresholds from your own won and lost data rather than SaaS ABM models.

**Map the buying group** for each account. Typical roles: design or application engineer (specifies), quality engineer (approves the supplier and the first article), manufacturing or operations (lives with the part), buyer or purchasing (runs the RFQ and terms), supply chain or materials planner (schedules releases), plant manager or VP operations (signs off a new supplier), finance (terms and credit). One logistics seller built relationships with 15+ influencers alongside the key decision maker over a three-month virtual RFQ and won $12M a year without the lowest rate ([r/sales 417](https://www.reddit.com/r/sales/comments/gve5w0/just_landed_the_biggest_deal_of_my_career_12m/)).

## Triggers: reasons to call this account now

| Trigger | Where to find it | Fits |
|---|---|---|
| New plant, line, expansion or acquisition | Press releases, local news, state economic development announcements, building permits | All |
| Reshoring, nearshoring, tariff exposure | Earnings calls, trade press, import records | Contract manufacturers, components |
| Imports of your product category | Bill-of-lading data (ImportYeti searches 70M+ US shipping records free; Panjiva paid) by HS code and volume ([r/supplychain 170](https://www.reddit.com/r/supplychain/comments/kvu5c3/after_150_convos_with_rsupplychain_redditors/)) | Domestic makers selling against imports |
| Hiring for a role tied to your process | Job boards, careers pages (quality engineer, buyer, maintenance, new shift) | All |
| New product launch or certification sought | Trade press, the prospect's own site (Wayback of their certifications page) | Component and process suppliers |
| Supplier disruption | Competitor closures, recalls, fires, strikes, bankruptcies in your sector | Second-source offers |
| Government contract award | USAspending.gov awards, SAM.gov opportunities | Prime contractors need subcontractors |
| Regulatory event | OSHA citations, environmental notices, UCC filings, rezoning in planning-commission minutes ([r/Entrepreneur 651](https://www.reddit.com/r/Entrepreneur/comments/1uckcc4/got_laid_off_33_days_ago_heres_everything_ive/)) | Safety, environmental, equipment, building materials |
| Exhibiting at a show | Exhibitor lists, especially outside their usual industry (same thread) | All |
| Executive priorities | Annual report, 10-K, investor presentations (public companies) | Larger accounts |

Make 10 to 15 hand-picked calls a day, each with a reason (leadership change, new rule, visible need) ([r/sales](https://www.reddit.com/r/sales/comments/1d7aip9/i_spent_a_month_working_in_europe_it_made_me/)), rather than 100 random dials. Emailing only companies that posted a relevant job ad in the last 30 days, 200 prospects, 35-word emails and at most two touches, gave a 4.8% reply rate and 2 deals, beating an agency's 20,000 emails over 4 months ([r/b2bmarketing 30](https://www.reddit.com/r/b2bmarketing/comments/1sqtbwk/a_client_asked_me_why_did_you_only_send_200/)).

## Contact sequence for one named account (operating policy)

1. **Email first** to the person closest to the problem, asking to confirm the problem, not for a meeting ([scripts.md](scripts.md)). Plain text, short, one reason, no attachments except a one-page line card or catalog when the buyer is in purchasing.
2. **Phone** two to three business days later. Avoid Monday 8 to 12 for operations people, who are in production meetings ([r/salestechniques 19](https://www.reddit.com/r/salestechniques/comments/1lqe3uq/the_discovery_call_that_actually_discovered/)). One caller logged 19% connects Tuesday to Thursday 10:00 to 11:30 versus 9% Monday morning and 5% Friday afternoon ([r/Entrepreneur 478](https://www.reddit.com/r/Entrepreneur/comments/1r3ubz0/the_cold_call_opener_that_gets_me_past/)).
3. **Leave no long voicemail; send a LinkedIn connection within 5 minutes that references the call**, then email the next day. In one rep's log LinkedIn got 14.1% responses versus 2.3% voicemail callbacks (same thread, different measures).
4. **Add a second and third person** in the buying group within two weeks: quality and purchasing if you started with engineering.
5. **Send something physical** to high-value accounts: a sample part, a cutaway, a test coupon, a material sample kit. A US brush maker sent free samples, phoned to confirm arrival, spent an hour learning the niche, asked for dimensions and colors by email, delivered a matching custom sample about four weeks later, and won at 50% above the best Chinese option ([r/smallbusiness 529](https://www.reddit.com/r/smallbusiness/comments/16q7k4v/my_kickstarter_is_1000_funded_with_a_week_left/)).
6. **Stop or park** after 6 to 8 touches over 6 to 8 weeks with no reply. Re-enter on the next trigger, not on a timer.

**Tricks most owners miss**

- **Procurement saves catalogs.** A procurement manager who gets 10 cold calls and 15 to 20 cold emails a week said he files cold emails that include a relevant product catalog for future needs, and his team bought from no cold caller ([r/salestechniques 76](https://www.reddit.com/r/salestechniques/comments/1o3rqkk/as_a_procurement_manager_im_genuinely_confused/)). To purchasing, send the line card; to engineering, send the specific capability.
- **Reopen a lost deal for a new offer.** A seller reconnected with an engineer at a pharma plant who had not bought pallets from his old employer; the engineer passed on the maintenance manager's email, which led to his largest customer ([r/LeadGeneration 27](https://www.reddit.com/r/LeadGeneration/comments/1ihi9x5/how_i_landed_my_most_important_customer/)).
- **Prospect by looking.** A lumber rep saw a pile of wood behind a warehouse, stopped and asked; it was a shipping-container builder and became his best customer ([r/sales 426](https://www.reddit.com/r/sales/comments/12mhlva/after_20_years_in_building_materials_here_are_my/)). Drivers, installers and field techs see prospects every day: pay them a small bounty per reported site.
- **Walk the delivery radius with samples.** A wholesale bakery mapped independent cafes within 40 miles, walked in with free samples and a wholesale catalog, and supplies about 20 to 30 of 300+ ([r/Entrepreneur 1,874](https://www.reddit.com/r/Entrepreneur/comments/15yu0h2/i_started_a_business_4_months_ago_and_its_already/)). Food processors, packaging and consumables suppliers can copy this.
- **Lead with the buyer's money problem.** Interviewing customers about what they fear telling their boss surfaced layoffs from low output, compliance problems and facilities overspend; for CFOs, talk repair cost and lost production, not how the machine broke ([r/salestechniques 19](https://www.reddit.com/r/salestechniques/comments/1lqe3uq/the_discovery_call_that_actually_discovered/)).
- **Turn a product into a fix for the buyer's margin problem.** A seller asked a jewelry-store manager "If I had a way for you to give out less discounts would you be interested in hearing me out?" and came back with a gift kit the store could give instead of a discount ([r/Entrepreneur 1,237](https://www.reddit.com/r/Entrepreneur/comments/es5qxv/my_most_successful_business_ever_the_jewelry/)). Same move for a distributor: what do they give away today that your product could replace?
- **Sell the specific use case per buyer type.** Clear janitorial buckets went to prisons as an anti-smuggling measure while standard yellow ones went to fast-food chains ([r/sales 424](https://www.reddit.com/r/sales/comments/1slmxuo/what_does_the_richest_salesperson_you_know_sell/)).
- **Government work.** One owner bid commodity RFQs on SAM.gov across several categories (boxes, jackets), then focused on the one he won (sand and gravel) and reported a roughly $23M levee-repair contract and $10M to 15M a year with 6 employees ([r/Entrepreneur 1,640](https://www.reddit.com/r/Entrepreneur/comments/15284g4/this_guy_does_10m_with_6_employees_by_hauling/)). A county courthouse conference table earned a furniture maker about $10,000 ([r/smallbusiness 710](https://www.reddit.com/r/smallbusiness/comments/17050bx/business_is_failing_struggling_to_get_out_of_this/)).

## Long cycles: stay useful between gates

- **Send account-specific market intelligence.** One seller set news alerts on the prospect's industry, competitors and suppliers, sent a competitor article with a question on day 113 (paragraph-long reply), a monthly report on the sponsor's business on day 125 (used in his C-suite meeting by day 132), and a market brief on day 150 ([r/sales 831](https://www.reddit.com/r/sales/comments/1t4mruq/here_is_every_step_i_took_to_sell_4625m_deals_to/)).
- **Ask how the buyer's team is measured and paid** and tie your deliverables to those goals (same thread, endorsed by an HVAC equipment seller).
- **Phone the silent prospect.** An engineering firm selling to energy companies called after weeks of silence post-demo; the decision maker said his boss had just asked about it and named the first two projects ([r/sales 416](https://www.reddit.com/r/sales/comments/jfgvt7/dont_make_excuses_for_your_clients_pick_up_the/)).
- **Chase everyone who owes an action;** about half had simply forgotten ([r/sales 473](https://www.reddit.com/r/sales/comments/vsx8vg/selling_tips_from_someone_who_has_gone/)).
- **Revive a stalled big deal on paper.** After 97 days of silence, a one-page, signed note couriered to the CFO before a board meeting, listing the three blockers in the buyer's words and asking for a 10-minute no-slides call, closed $1.3M within days ([r/sales 4,270](https://www.reddit.com/r/sales/comments/1n7oou4/got_ghosted_for_97_days_closed_13m_with_a/)). Commenters warned the 90-day opt-out it conceded created cancellation risk.
- **Put engineers in front of the end users on day one** of custom work: less rework, usually within the first budget ([r/Entrepreneur 4,013, 481-upvote comment](https://www.reddit.com/r/Entrepreneur/comments/1mw5yfg/forced_every_engineer_to_take_sales_calls_they/)).
- **Define a paid evaluation with gates and production pricing up front** for big programs: a $75k paid test tied to $500k to 750k a year production on a four-year agreement ([r/sales 831](https://www.reddit.com/r/sales/comments/1t4mruq/here_is_every_step_i_took_to_sell_4625m_deals_to/)). For a job shop the equivalent is a paid first article or pilot lot with the production price and volumes agreed before you cut metal.

## Measure accounts, not leads

- Accounts reached, accounts with a conversation, accounts with an RFQ, accounts with a PO, gross profit per account.
- Positive reply rate per first-contact recipient, not open rate (opens are unreliable and pixels hurt deliverability).
- For ads against the list: share of the list reached (aim 40 to 60%), cost per engaged account, and a 20% holdout of the list to check whether ads moved anything (coreyhaines31 ABM playbook, practitioner thresholds).
- Pay agencies on positive replies, qualified meetings and quotes, never on opens or sends. An agency sending 5,000 emails a month at a "45% open" rate produced 0.6% replies and 3 positives in 4 paid months ([r/b2bmarketing 30](https://www.reddit.com/r/b2bmarketing/comments/1sqtbwk/a_client_asked_me_why_did_you_only_send_200/)); outsourced appointment setting cost £8,000 a month for about 4 qualified meetings a quarter ([r/b2bmarketing](https://www.reddit.com/r/b2bmarketing/comments/1ss4wfs/i_just_quit_my_job_at_a_7figure_b2b_leadgen/)).
