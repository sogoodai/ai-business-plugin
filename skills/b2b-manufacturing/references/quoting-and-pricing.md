# Quoting speed, win rates and pricing

The quote is the product demo of a job shop, contract manufacturer or distributor. How fast it arrives, how clearly it states assumptions and what it leaves out decide the win more often than the price line. Pricing psychology, packaging and price-increase rollout in general live in `offers-pricing`. Sources in [sources.md](sources.md).

## What the data says

- 87% of job shops say customers demanded faster quote turnaround and more order visibility than a year earlier (Paperless Parts Supplier Readiness 2026; quoting-software vendor).
- Quote to PO: 21.1% (268 of 1,271 US manufacturing quotes, Factur, Nov 2025 to Oct 2026, outbound-sourced). Median quote $12,000, mean $137,000.
- "Most job shops win 20 to 30% of quotes" is Paperless Parts' long-running heuristic from customer conversations, not a sampled benchmark.
- 26% of technical buyers first contact a vendor because of pricing or inventory questions (GlobalSpec 2026): the site should give price and stock guidance where it can.
- No public study proves a specific hour target moves win rate. Speed is treated here as operating policy backed by buyer demand, not as a measured lift.

## Quote SLA by complexity (operating policy)

| Class | Work | Target | Message |
|---|---|---|---|
| A | Repeat parts, catalog items, standard work | Same business day | Quote, lead time, validity date |
| B | Normal custom work with a complete package | Named date, usually 2 to 3 business days | Acknowledge with the date, then quote |
| C | Engineering-heavy, new process, large program | Acknowledge within hours; fit check within 2 business days; quote date agreed with the buyer | "We'll confirm fit first, then price" |

Every RFQ gets an automatic acknowledgement within minutes and a human decision (quote, question or decline) the same business day. Wording in [scripts.md](scripts.md).

## Triage before estimating

Estimator time is the scarce resource. Score each RFQ in two minutes:

```
quote priority = fit (in capability?) x value (annual GP band) x win odds (new or incumbent, relationship, source) x strategic (new industry, anchor customer)
expected gross profit per quoting hour = (quote value x expected gross margin x win probability) / estimator hours
```

- Decline fast and politely when the work is outside capability, below minimum, or a price check for an incumbent. Say why, and name what you would quote. A clean decline earns the next RFQ.
- Ask "Is this a new part, or are you looking at a second source for a current one?" A price check for an incumbent rarely converts.
- Ask for the annual volume and the release pattern, not just the first quantity. Setup cost spread over the real annual volume changes the price.

## Questions that change the price (ask before you quote)

The best practitioner threads in this segment are about tolerances that did not need to be tight:

- **What does the part do?** A tight bore along a 2 to 3 foot tube only needed bearing fits at the ends. For a 3.5 m tube drawn at 0.13 mm concentricity, the call script was: "It's not 0.13 per m. It's per the whole length. If you pick it up, it'll fall out of spec" (339-upvote comment, [r/Machinists 1,128](https://www.reddit.com/r/Machinists/comments/1qwhw3b/customer_wants_35m_tube_to_be_concentric_within/)). Default title-block tolerances are common.
- **Slip fit or press fit, and what hardware goes through it?** A shop reamed a .484 ID to .5115 at about $9 a piece, batches of 500, for about 20 years. When the drawing changed to .505 to .520, the engineer said it was a clearance hole for a 1/2-13 bolt and could have been drilled (255-upvote comment, [r/Machinists 1,734](https://www.reddit.com/r/Machinists/comments/17wsijp/ive_been_killing_myself_to_hold_this_only_to_find/)).
- **How will you inspect it?** ±0.002 mm callouts checked with a handheld digital mic; a 0.40 mm hole rejected because a 0.40 mm gauge pin would not enter. Agree the inspection method before accepting the order (207 and 117-upvote comments, [r/Machinists 1,128](https://www.reddit.com/r/Machinists/comments/1qwhw3b/customer_wants_35m_tube_to_be_concentric_within/)).
- **Which spec drives cost?** 1 kV vs 5 kV isolation is a huge cost difference; a ballpark without it gets held against you ([r/manufacturing 48](https://www.reddit.com/r/manufacturing/comments/ob25am/do_you_think_b2b_pricing_or_lack_thereof_on/)).
- **What documentation is required?** FAIR (AS9102), PPAP level, CoC, material certs, CMM reports, portal uploads, labeling and packaging specs.

Offering a cheaper alternative (drill instead of ream, relaxed tolerance, standard material) as a second line on the quote shows engineering value and often wins the job.

## Price the paperwork and the portal

- A contract shop saw first-article preparation rise from 1 to 2 hours to 6 to 8 hours per lot under a customer's new portal and file rules, with 2 to 3 years left on fixed pricing. The customer refused to reprice and returned shipments submitted the old way at the supplier's expense ([r/manufacturing 94](https://www.reddit.com/r/manufacturing/comments/1kbhwgr/anyone_else_getting_tired_of_customers_pawning/)).
- Practitioner fixes from the same thread: standard PDFs as the included baseline and about $55 an hour for customer-specific portal uploads and formatting; one supplier doubled the product price after three months of nonstop paperwork.
- Quote terms to add: "Documentation included: CoC and material certs. FAIR, PPAP and customer-portal submissions quoted separately. Changes to documentation requirements after award are re-quoted." Put a price-review clause in every long-term agreement (annual, or on documented requirement change).

## Win rate: read it, do not chase it

- **A very high win rate is a warning.** If most quotes are accepted without pushback, you are probably underpriced, quoting only captive repeat work, or not quoting enough new opportunities.
- **A low win rate can be healthy** if estimating is cheap and you only chase high-margin work.
- Track win rate by count and by quoted dollars, by source, by customer type, by process and by estimator. The meaningful number is expected gross profit per quoting hour.
- Log a loss reason for every lost quote: price, lead time, technical fit, incumbent kept, project cancelled, other. Ask the buyer with one short email ([scripts.md](scripts.md)). "Lost" without a reason teaches nothing.
- Follow up every open quote once: 3 to 5 business days after sending for class A and B, and on the buyer's decision date for class C.

Quote dashboard fields: RFQs received, declined, quoted, median turnaround, quote value, expected margin, POs won, win rate by count and by dollars, gross profit won, loss reason, source, new or existing customer, estimator hours.

## Setting and changing prices

- **Complete jobs pay more than leftovers.** A grinding shop reported about $125 an hour quoting the complete job versus about $75 an hour as a grinding-only subcontractor taking finishing work (historical rates, [r/Machinists 3,652](https://www.reddit.com/r/Machinists/comments/12jwve8/fun_job_this_is_an_experimental_connecting_rodhad/)). Quote the whole part where you can.
- **Raise prices while the queue proves demand.** A custom trailer maker moved base price from about $2,500 to $4,000 in steps every two weeks and kept a three-week queue ([r/manufacturing 75](https://www.reddit.com/r/manufacturing/comments/1ipvsim/small_manufacturing_business/)). A full backlog is a pricing signal.
- **Narrow before you discount.** The same maker escaped price-only competition by moving from general utility trailers to custom UTV and ATV trailers.
- **Commodity-linked goods:** price at the higher of what the stock cost and what it costs to replace; keep prices steady through temporary cost dips, because up, down and up again upsets customers more than holding ([r/smallbusiness 2,120](https://www.reddit.com/r/smallbusiness/comments/1io528v/our_aluminum_suppliers_are_saying_prices_arent/)). A steel supplier raised 30% on a roughly 10% raw-cost rise and held it after costs fell (same thread). Better: index clauses tied to a published metal or resin price, with a review date, so increases are mechanical.
- **Tariffs reopen accounts.** A Canadian buyer spending millions a year on US parts moved to a European supplier on a three-year commitment when that supplier matched the US price ([r/sales 2,517](https://www.reddit.com/r/sales/comments/1k5iczf/just_lost_millions_in_sales_due_to_tariffs/)). Watch your customers' and competitors' tariff exposure: it is both a threat and a trigger.
- **Usage-based pricing from the real duty cycle.** Removing overtime charges on equipment used across three shifts needed a 20% higher rental rate, $2M a year, on a $45M deal where purchases earned about 2% and rentals about 35% ([r/sales 501](https://www.reddit.com/r/sales/comments/1krokou/wish_me_luck_45m_deal_im_presenting_tomorrow/)).
- **Cost with paid labor, not the owner's.** A $1,670 job looked like 92% margin with unpaid owner labor and about 60% once two employees were costed ([r/Entrepreneur](https://www.reddit.com/r/Entrepreneur/comments/5sss8m/about_two_weeks_ago_i_posted_here_about_losing_my/)).
- **Label introductory prices as introductory** ("this is our new-customer pricing for the first order") so a launch price does not become the permanent anchor ([r/smallbusiness](https://www.reddit.com/r/smallbusiness/comments/igcp2o/today_i_had_my_first_customer/)).

**Price objections:** cut scope, not rate. Offer the relaxed-tolerance or alternate-material version, a larger batch, a longer lead time, or fewer documents, each with its price. Ask what the cheaper quote includes (material certs, inspection, packaging, freight, lead time). Scripts in [scripts.md](scripts.md).

## Lead times you can beat

- Quote a lead time with room for the real backlog. A repair shop changed its quote from 6 to 8 days to 16 to 18 days, delivered in 8 to 9, and customers went from angry to thrilled (63-upvote comment, [r/smallbusiness](https://www.reddit.com/r/smallbusiness/comments/igcp2o/today_i_had_my_first_customer/)).
- A building-materials veteran overestimates delivery windows and answers pushback with "let me see if I can pull some strings" ([r/sales 426](https://www.reddit.com/r/sales/comments/12mhlva/after_20_years_in_building_materials_here_are_my/)).
- Domestic speed is worth money: a buyer said they would pay 20% more for 5-day delivery, and listings claiming local stock but shipping from overseas in 5 weeks earned refunds and bad reviews ([r/smallbusiness 1,278, 192-upvote comment](https://www.reddit.com/r/smallbusiness/comments/16mdptb/unpopular_opinion_opening_a_shopify_store_just_to/)).
- Offer an expedite tier with a price, rather than expediting for free.

## Deposits, terms and credit

- Custom, customer-specific work: take a deposit or progress payments covering at least material and tooling, and state who owns tooling, fixtures and programs.
- One supplier funded the capacity a large buyer required by first selling that buyer a complementary product against a 50% advance ($50,000) ([r/Entrepreneur 1,904](https://www.reddit.com/r/Entrepreneur/comments/ygnko2/i_became_a_self_made_millionaire_at_25_in_a_third/)). Big buyers will advance money when the alternative is no supplier.
- Set a credit limit for every account, including old ones, and review it when order size jumps (bad-debt case in [accounts-and-retention.md](accounts-and-retention.md)).
- Hard prepayment has a conversion cost: a strict pay-within-one-hour rule stopped no-shows but ended phone bookings for one business ([r/smallbusiness 608](https://www.reddit.com/r/smallbusiness/comments/134ubhg/i_need_to_stop_wasting_my_time_on_people/)). Match the term to the risk, not to a blanket rule.
- If a mandatory fee was left out of a verbal quote, absorb it as an approved discount before the buyer finds out ([r/sales 890](https://www.reddit.com/r/sales/comments/1fjyurm/the_day_i_sold_7_cars/)). Your credibility is worth more than the fee.
