# Validation before building

The question is never "do people like it?". It is "will a specific person give up money, time, data or reputation for it, now?". Build only as much as the strongest signal you have earned.

Why it matters: in CB Insights' March 2026 analysis of 431 VC-backed shutdowns since 2023, 43% cited poor product-market fit; running out of cash (70%) was usually the symptom, not the cause ([CB Insights 2026](https://www.cbinsights.com/research/report/startup-failure-reasons-top/)). A 2024 peer-reviewed study of 50 failure accounts found weak information-seeking in 35 of them ([Frontiers 2024](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1299135/full), possibly outdated). Operators report the same thing in money: one founder asked friends "Would you pay for this?" for weeks, everyone said yes, and 18 months and $47k later the product had 12 paying customers and $340 total revenue ([r/Entrepreneur, 1,862 upvotes](https://www.reddit.com/r/Entrepreneur/comments/1mj1olw/i_spent_47k_and_18_months_building_an_ai_startup/)).

## The evidence ladder

Score every signal on this ladder. Report the highest rung reached, not the volume on the lowest one.

| Rung | Signal | What it proves | Weight |
|---|---|---|---|
| 0 | Compliments, "I'd use that", likes, survey enthusiasm | Nothing | 0 |
| 1 | Page view, follow, waitlist email | Attention | Low |
| 2 | Booked call, filled qualification question, replied to a follow-up | Problem is real for this person | Medium |
| 3 | Introduces you to a colleague, gives data access, agrees to a pilot with a date | Willing to spend reputation or time | High |
| 4 | Deposit, preorder, paid pilot, letter of intent with a price | Willing to pay | Very high |
| 5 | Paid, used it, came back or renewed | Demand | Proof |

Rules:

- Survey enthusiasm and verbal "yes" are rung 0. Treat "Let me know when you launch" and "I would definitely buy that" as unconfirmed ([r/startups, 278 upvotes](https://www.reddit.com/r/startups/comments/mq2lfu/3_mistakes_founders_make_when_talking_to/)). The real tests: a follow-up meeting, a trial request, a preorder question, an intro to their team.
- A waitlist is rung 1. A Product Hunt launch in September 2026 produced about 290 signups and zero paid conversions ([Nimply 2026](https://nimply.io/blog/product-hunt-launch-case-study)).
- Record what the prospect pays for today instead. An existing paid workaround or competitor is stronger evidence than enthusiasm.
- Before spending on the build, require rung 4 from at least a few buyers of the same type, or repeated rung 3 from one tight segment.

## Test the riskiest assumption first

Adapted from the "cheapest test" canon in alirezarezvani/claude-skills (MIT, built on Ries, Blank, Fitzpatrick's *The Mom Test* and Traction's Bullseye; see [sources.md](sources.md#public-skill-frameworks-adapted-rewritten-in-our-words)). Name the one assumption that kills the business if wrong, then run the cheapest test for that risk, with a pass rule written first. Its principle: a real charge beats a survey, a stranger beats a friend, behavior beats opinion.

| Riskiest assumption | Cheapest test | Pass looks like |
|---|---|---|
| People want it | Smoke-test page plus a little targeted traffic | Signup rate at or above the median for the page type (below) and cost per signup under your target cost per customer |
| They will pay this price | Pre-sale or deposit | At least one prepayment or signed commitment from a stranger; `saas-apps` asks for 5 before building |
| We can deliver it | Concierge or manual delivery | The promised outcome delivered by hand, on time, at a margin |
| It beats what they use now | 5 interviews with people who switched or tried to | They name a specific reason the current option fails |
| We can reach them | One channel spike (100 contacts, one community, one street) | Meaningful conversations at a rate you can afford |
| They come back | One-week concierge probe | Unprompted return or reorder |

Rate the pain you hear: **burning** (they already spent money or time on a fix), **nagging** (they complain but have not acted), **imagined** (only appears when you ask). Build only for burning.

## Problem interviews that do not lie

Run 20 to 30 conversations with one segment before rewriting anything. Operators who did this report the first customers came out of the interviews themselves (below).

Rules for the agent preparing interview guides:

1. **Keep the idea out of the first half.** Ask about past behavior, not hypotheticals. Replace "How much would you pay for an app that splits the bill?" with "When you go to a restaurant with friends, how do you usually pay?" then "Can you walk me through the last time?" ([r/startups, 278 upvotes](https://www.reddit.com/r/startups/comments/mq2lfu/3_mistakes_founders_make_when_talking_to/)).
2. **Ask for last week, not in general.** One YC founder sourced 20 construction conversations through his network and asked: "What does your day-to-day look like?", "What was something that frustrated you last week, last month?", "Why did that process frustrate you?", "What tools and processes do you use to get around those frustrations?" Repeated stories across roles revealed the product ([r/startups, 745 upvotes](https://www.reddit.com/r/startups/comments/hlsj2t/how_i_got_into_yc_twice_with_2_different_ideas_in/)).
3. **Make them rank it.** Ask the prospect to stack-rank their problems before you name yours. Talking about one annoyance inflates it (the focusing illusion).
4. **Separate the user from the buyer.** An edtech founder had teachers confirm the pain, but purchasing sat with deans and directors who never used the tool; the startup closed ([r/indiehackers, 252 upvotes](https://www.reddit.com/r/indiehackers/comments/1kwxwyg/5_brutal_lessons_i_learned_after_my_failed_edtech/)).
5. **End with a commitment ask.** "If we build X, would you pay for it and how much?" is weak alone, but one B2B founder found interviews "naturally became sales opportunities": his first two customers and about 50% of a $50k pipeline came from the validation phase ([r/startups, 377 upvotes](https://www.reddit.com/r/startups/comments/17c7dyl/we_grew_arr_100_from12k_to_24k_grew_pipeline_400/)).
6. **Log five fields per conversation:** trigger, current workaround, quantified pain, objection, exact buyer wording. After 20 to 30, rewrite the page and outreach in the phrases that repeat (research recommendation, [report 2026](sources.md#research-benchmarks-and-platform-data)).

Where to find interviewees, with numbers:

- LinkedIn research request: about 250 executives contacted, about 20 conversations (8%). Script in [scripts.md](scripts.md#problem-interview-request) ([r/startups, 377 upvotes](https://www.reddit.com/r/startups/comments/17c7dyl/we_grew_arr_100_from12k_to_24k_grew_pipeline_400/)).
- Niche community DM: about 20 people messaged, about 50% replied; the fourth idea tested got buying interest and some interviewees became paying customers ([r/sweatystartup, 581 upvotes](https://www.reddit.com/r/sweatystartup/comments/ilubcf/after_failing_for_years_i_did_it_my_store_is_9/)).
- Paid-for-your-time email: Jason Cohen emailed 40 WordPress consultants offering to pay for an hour; all 40 took the call, none asked for payment, 30 said they would pay $50/month before WP Engine had a name or a server (reported commitments) ([r/sweatystartup, 229 upvotes](https://www.reddit.com/r/sweatystartup/comments/m5mh23/the_cold_email_that_started_a_100m_yr_company/)).
- Existing list survey: 1,500 contacts, about 180 responses (12%), with a final question offering a private walkthrough; the walkthroughs later sold over $20,000 before the MVP existed ([r/EntrepreneurRideAlong, 237 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/13ooetz/how_we_made_20k_in_sales_without_an_mvp_to_fund/)).
- Complaint mining: read 40 to 50 high-engagement posts in one subreddit with comments, tally complaints, shortlist 5 to 7 problems ([r/startups, 265 upvotes](https://www.reddit.com/r/startups/comments/1kks4n3/you_are_not_building_a_startup_you_are_just/)). Low-upvote, high-comment threads flag controversy and pain. Cross-check competitors' 1-star Yelp, G2 and App Store reviews ([r/Entrepreneur, 4,377 upvotes](https://www.reddit.com/r/Entrepreneur/comments/5lfy6n/4_years_ago_i_wrote_a_case_study_on_reddit_on_my/)).
- DIY workaround videos: hundreds of thousands of views on YouTube hacks with spare parts and glue means unserved demand; one product built on this reached about $5,000/week profit in 10 months ([r/Entrepreneur, 2,406 upvotes](https://www.reddit.com/r/Entrepreneur/comments/9n8xyj/inventrepreneurship_i_took_an_idea_to_mass/)).

**Tricks:** Call every waitlist signup you can before trusting a winning signup rate. Four calls with roofing signups turned a vague "estimating" idea into a specific underpricing problem ([r/EntrepreneurRideAlong, 47 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1qhu4ud/heres_my_insight_on_how_to_validate_your_startup/)). Prefer markets with competitors: two indie SaaS founders screen for at least 3 established competitors making roughly $20k to $80k a month and reject empty markets ([r/indiehackers, 69 upvotes](https://www.reddit.com/r/indiehackers/comments/1s8wz28/my_saas_journey_so_far_numbers_wins_mistakes_and/)).

## Smoke tests and waitlists

A one-page test is a rejection tool, not proof. Structure (adapted from the research report):

- **Headline:** "Get [measurable outcome] without [painful current method]."
- **Mechanism:** "We do it by [specific mechanism], built for [specific buyer]."
- **Low CTA:** "Join the first-customer list."
- **Strong CTA:** "Reserve a founding slot, $50 refundable deposit."
- **Qualification question:** "What are you doing today instead?"

Benchmarks to judge it (targeted traffic only):

| Page type | Median | Top quartile | Source |
|---|---|---|---|
| Prelaunch waitlist signup | 7.7% | 17.1% (top 10%: 28.4%) | [Waitlister 2026](https://waitlister.me/tools/conversion-rate-checker), vendor aggregate |
| All landing pages | 6.6% | about 11.4%+ | [Unbounce, Jul 2023 to Jul 2024 data](https://unbounce.com/conversion-benchmark-report/), possibly outdated |
| SaaS landing pages | 3.8% | 11.6% | Unbounce 2024 |
| Ecommerce landing pages | 4.2% | 11.4% (food 7.1%, fashion and beauty 1.3%) | Unbounce 2024 |

Set the kill rule before the traffic arrives. Example operating rule (not an industry benchmark): "If 500 qualified visitors give fewer than 20 signups and fewer than 3 interviews where people describe an urgent workaround, change the offer, not the button."

Paid smoke test economics: a 2026 validation project got 128 cold signups from 36,000 impressions on a $2,000 budget (about $15.60 per signup), and picked the winning page at 95% confidence on 1,400 views ([Evil Martians 2026](https://evilmartians.com/chronicles/from-0-signal-to-128-cold-signups-product-validation-on-2k-budget), agency case). Budget at least that per segment you test, or skip paid tests and use communities.

Operator tests with deadlines:

- **7-day test:** one-page description, landing page in under a day, one full week of marketing and sales, kill on zero signups or demo requests; give 2 weeks to build if it moves. The founder tested 39 ideas this way and killed 37 ([r/indiehackers, 494 upvotes](https://www.reddit.com/r/indiehackers/comments/1lsidt7/i_launched_39_startups_until_one_made_me_millions/)). Several commenters objected to taking payment for an unbuilt product; see the honesty rule below.
- **60-day test:** landing page with Stripe checkout or a Calendly link, marketing almost daily across Facebook groups, DMs, LinkedIn, Reddit, X, TikTok and Shorts; pivot if no money after about 60 days ([r/EntrepreneurRideAlong, 553 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1ojcn6a/so_ive_launched_18_startups_if_i_could_start_over/)).
- **One product a week:** Tweet Hunter's founders ran 11 "request access" landing pages in four months against the same buyer and backend; the 11th got its first paying user ([r/EntrepreneurRideAlong, 91 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1xmwe5n/quitting_with_250k_of_debt_and_sold_for_8_million/)).
- **One-sentence filter:** write the landing page before any code; if you cannot say who it is for in one sentence, it is not ready. One founder cut about 80% of their idea list this way ([r/indiehackers, 60 upvotes](https://www.reddit.com/r/indiehackers/comments/1rkl0n6/i_had_17_business_ideas_in_my_notes_app_never/)).
- **App exception:** an iOS founder with $1.2M+ in app revenue says pre-product validation gave reassuring answers, not evidence; ship a 2 to 4 week version and measure real App Store impressions instead ([r/SideProject, 702 upvotes](https://www.reddit.com/r/SideProject/comments/1dtfhdz/ive_made_over_12_million_from_my_ios_app_side/)). For cheap-to-build consumer apps, a fast real release can beat a waitlist.

## Pre-sales

Pre-sales turn rung 1 into rung 4 and often fund the build. Evidence:

| Case | Mechanism | Result | Source |
|---|---|---|---|
| Software, B2B pain | Sketch prototype in one week, $500 to $700 discounted lifetime access, working product promised in 3 months, full refund if not | 10+ customers before a working product | [r/startups, 597 upvotes](https://www.reddit.com/r/startups/comments/1l9jeza/we_almost_killed_our_startup_by_raising_too_much/) |
| Digital product | Carrd page plus Gumroad, $49 early access, shared in Facebook groups and subreddits | $1,000 in a couple of days | [r/Entrepreneur, 1,377 upvotes](https://www.reddit.com/r/Entrepreneur/comments/poeihp/12_months_ago_i_was_unemployed_last_week_my_side/) |
| B2B | Cohorts by role; "we think you have this problem... we're going to charge X, would you pay it?"; payment conditional on delivery | First sale closed before development | [r/startups, 313 upvotes](https://www.reddit.com/r/startups/comments/h0tl8t/if_you_build_it_they_do_not_come_what_almost/) |
| Dev starter kit | Preorders to people asking for early access on X, delivery in 3 days | 5 preorders, €700; €4,548 in 2.5 months | [r/indiehackers, 63 upvotes](https://www.reddit.com/r/indiehackers/comments/1h92ect/i_finally_built_something_that_makes_sales_it/) |
| Bounce house rental | Marketplace listing with photos of units not yet owned, availability 2 weeks out | About 15 rentals with deposits before buying 3 units for $1,700 | [r/EntrepreneurRideAlong, 410 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/ma28l6/1500_a_day_renting_out_bounce_houses_at_20_years/) |
| Seasonal home services | Winter door knocking, estimates next weekend, 25% deposit by cheque | About $90,000 booked before spring; deposits covered most startup costs | [r/sweatystartup, 449 upvotes](https://www.reddit.com/r/sweatystartup/comments/1bsnned/i_started_a_home_service_biz_in_a_new_city_6/) |
| Imported product | Ads, samples and presales during a 4-month ocean shipment | Entire first batch sold before arrival | [r/Entrepreneur, 2,590 upvotes](https://www.reddit.com/r/Entrepreneur/comments/10mxbuk/made_200k_last_year_while_still_in_college/) |
| B2B supplier | Asked a McDonald's buyer for a 50% advance on a side product | $50,000 advance funded the first order | [r/Entrepreneur, 1,912 upvotes](https://www.reddit.com/r/Entrepreneur/comments/ygnko2/i_became_a_self_made_millionaire_at_25_in_a_third/) |
| Crowdfunding | Kickstarter as validation and production finance plus alumni outreach | About $74,000, half from organic Kickstarter discovery | [Shopify 2025, IQBAR](https://www.shopify.com/au/blog/first-customers) |

Honesty rule: say the product is not finished. Taking payment for something presented as live, then refunding, cost one founder's critics their trust; commenters reported prospects refusing MVPs after earlier "smoke and mirrors" ([r/indiehackers, 494 upvotes](https://www.reddit.com/r/indiehackers/comments/1lsidt7/i_launched_39_startups_until_one_made_me_millions/)). Use "founding access, ships [date], full refund if we miss it" wording. Never take deposits for a physical delivery date you cannot hit; check the owner's local consumer rules for preorders.

## Concierge and manual delivery

Deliver the outcome by hand before you automate it.

- Stable reportedly served its first 100 paying customers with Google Drive, Zoom and a Stripe link before automating ([submit.co 2026](https://submit.co/first-users), founder case).
- A personal-shopping business ran from spreadsheets, charged the planned online price in person, and only built the website after funding ([r/startups, 313 upvotes](https://www.reddit.com/r/startups/comments/h0tl8t/if_you_build_it_they_do_not_come_what_almost/)).
- A cleaning-marketplace founder asked his own house cleaner to take the jobs he generated: first job on launch day, about 40 cleaners later ([r/sweatystartup, 1,011 upvotes](https://www.reddit.com/r/sweatystartup/comments/1asegdq/from_an_idea_to_replacing_my_fulltime_salary_in_4/)).
- A Craigslist request for graduation-party valet parking was sold at $3,000 and subcontracted for $1,000 ([r/Entrepreneur, 3,305 upvotes](https://www.reddit.com/r/Entrepreneur/comments/aylx5g/how_i_made_2k_in_a_day_pretending_to_own_a_valet/)). Commenters objected to the founder pretending to own the valet company: broker openly.
- Software founders: run the setup yourself and send the prospect the finished asset instead of a login ([r/Entrepreneur, 202 upvotes](https://www.reddit.com/r/Entrepreneur/comments/1v3la4h/building_is_too_easy_now_heres_how_to_actually/)). A B2B search tool offered "free research reports" on LinkedIn made with its own product; recipients asked for demos and referred decision makers ([r/startups, 733 upvotes](https://www.reddit.com/r/startups/comments/n0hs2l/linkedin_is_a_cringefest_but_it_works_for_b2b/)).
- Narrow pilot inside one team: a 3-hour script saved 20 seconds after each of 300 to 400 daily calls; within days the test user out-dialed 95% of about 100 coworkers, which justified building the product ([r/Entrepreneur, 1,712 upvotes](https://www.reddit.com/r/Entrepreneur/comments/yopjb9/how_i_made_47k_selling_an_unsexy_product_i_built/)).
- Services and coaching: pilot a two-week program with friends, revise, run a second cohort, then build the website ([r/smallbusiness, 703 upvotes](https://www.reddit.com/r/smallbusiness/comments/1otuw7c/i_mentally_cannot_do_another_95_desk_job_i_have/)).

## Physical demand tests

- **Rent before you buy:** $45 of flyers in good neighborhoods, book every job for one Saturday, rent the pressure washer that morning ([r/Entrepreneur, 1,354 upvotes](https://www.reddit.com/r/Entrepreneur/comments/ajpc5k/a_low_risk_way_to_turn_100_into_a_lot_more/), projection). A tent rental owner books and takes a deposit on the first graduation-season job before buying the $800 tent ([r/sweatystartup, 106 upvotes](https://www.reddit.com/r/sweatystartup/comments/10q7ih8/a_stepbystep_guide_to_starting_a_tent_rental/)).
- **Ugly listing first:** a garage-built WiFi school bell sold on eBay before any branding ([r/SideProject, 634 upvotes](https://www.reddit.com/r/SideProject/comments/1sbr7sm/i_built_a_wifi_bell_system_in_my_garage_because_a/)). Native launched on Product Hunt in 12 days with $1,000 and placed its first supplier order only after seeing demand ([r/Entrepreneur, 1,392 upvotes](https://www.reddit.com/r/Entrepreneur/comments/yv9aqk/from_1k_initial_investment_to_100_m_exit_in_25/)).
- **Boutique consignment:** 400 bracelets bought for $200; one Malibu boutique sold out in under a week ([r/EntrepreneurRideAlong, 89 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1wllhu5/helping_homeless_costa_ricans_turned_into_1037m/)).
- **Interest is not payment:** free watches given to bartenders at a brunch had people lining up to buy within 15 minutes, but no money changed hands, so it proved interest only ([r/EntrepreneurRideAlong, 207 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/arzplw/250kmonth_selling_wooden_sunglasses_1_employee/)). Always carry a way to take payment.

## What to tell the owner at the end of validation

One of four verdicts (research report framing):

1. **Validated:** rung 4 or 5 from several buyers of one type. Build the minimum that delivers the paid promise; move to the first-channel tournament ([channels.md](channels.md)).
2. **Problem real, offer wrong:** many rung 2 and 3 signals, no payment. Change price, packaging, or buyer (user vs budget holder) and rerun.
3. **Attention without pain:** signups and likes, no calls or workarounds. Change the segment or the problem.
4. **No signal:** stop or pick the next idea. More content or ads will not fix it.
