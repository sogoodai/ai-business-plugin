# By business type: router and angles

This skill is the generic playbook. When a segment skill exists, load it too: it holds the segment's channels, prices and benchmarks. Use this file for the routing, the first-customer angle that differs by type, and the cases that show what the first 100 looked like.

## Router

| Business | Segment skill | Where its first-customer guidance lives |
|---|---|---|
| SaaS, micro-SaaS, web or mobile app, AI tool, browser extension | `saas-apps` | SKILL.md "First users" and "Launches"; `references/first-users.md`, `references/launches-and-marketplaces.md` |
| Physical product brand (Etsy, Amazon, Shopify, TikTok Shop, wholesale) | `ecommerce-brand` | `references/first-100-sales.md` |
| Clothing label | `fashion-apparel` | `references/drops-and-launches.md`, "First 100 customers for a new label" |
| Jewelry or accessories | `jewelry-accessories` | SKILL.md "First 30 days for a new or restarting maker" |
| Agency, freelancer, consultant, studio | `agency-freelance` | SKILL.md "First 30 days"; `references/getting-clients.md` |
| Tutoring, coaching, courses, cohorts, paid community | `education-coaching` | SKILL.md "Launch math"; `references/coaching-sales.md` "First 10 clients" |
| Templates, ebooks, presets, other digital products | `digital-products` | `references/product-selection.md` "Validate before you build"; `references/email-launches-affiliates.md` |
| Creator, newsletter, podcast | `creator` | `references/plan-90-days.md` |
| Salon, barber, lash, nails, massage, med spa | `beauty-business` | SKILL.md "First 30 days for a new or rebuilding practice" |
| Home services and trades | `home-services` | `references/plan-90-days.md` "Brand-new business: the first 30 days" |
| Personal trainer, studio, gym | `fitness` | `references/getting-clients.md` |
| Restaurant, cafe, food truck | `restaurant` | `references/plan-90-days.md` (opening countdown) |
| Independent shop | `local-retail` | SKILL.md "Opening or reopening a shop: first 30 days" |
| Real estate agent or team | `real-estate` | `references/speed-to-lead-and-nurture.md` |
| Indie game | `indie-games` | SKILL.md "Decision rules"; `references/pricing-and-launch.md` |
| Clinic or health practice | `health-practice` | SKILL.md |

Cross-cutting skills for depth this skill does not own: `local-seo` (Google profile, reviews, map rankings), `email-sms-loyalty` (flows, consent, loyalty and referral programs), `paid-ads` (account setup, budgets, learning phases), `organic-social` (content and DM funnels), `offers-pricing` (pricing psychology, tiers, raises), `seo-content` (search content, alternatives pages), `b2b-outbound` (cold email systems and deliverability), `website-conversion` (landing pages). Some of these are still being written; route by name.

## Rules shared across the segment skills (stay consistent)

- **Payment is the only validation.** `saas-apps`: build after 5 strangers pay. `ecommerce-brand`: sell one unit to a stranger. `education-coaching`: 5 to 10 paid seats before recording more than module 1. Free users are for learning and bugs, never proof of demand.
- **Free work only with a reason.** `beauty-business` model calls at product cost, "never free"; `home-services` asks for full-price jobs from friends and neighbors with reviews. Free or at-cost is acceptable only for a portfolio, a reference buyer who can send repeat work, or a time-boxed pilot with a paid next step ([offers.md](offers.md#free-paid-or-in-between)).
- **One primary channel, picked by test.** `ecommerce-brand` (one channel for the first 100 sales) and `education-coaching` (at most two in 30 days) describe the concentration step in [channels.md](channels.md).
- **Founder time:** under 10 customers outreach all day, 10 to 25 half the day (`saas-apps`, same operator source).
- **Product Hunt after the first 100 users;** weekend for the badge, weekday for reach (`saas-apps`, consistent with [launches-and-press.md](launches-and-press.md)).
- **Intro prices carry a written end date** (`beauty-business`, `local-retail`, `offers-pricing`).
- **No review incentives on Google; never gate.** Disclosed incentive programs exist only on some B2B software review sites (`saas-apps`).
- **A waitlist is a launch list, not proof.** `fashion-apparel`, `digital-products` and `restaurant` use waitlists to launch; `saas-apps` refuses them as validation. Both are right: build the list, judge demand by payments.

## B2B SaaS and B2B services

- **First 10 come from conversations:** interviews that turn into sales (first 2 customers and about 50% of a $50k pipeline from validation calls, [r/startups, 377 upvotes](https://www.reddit.com/r/startups/comments/17c7dyl/we_grew_arr_100_from12k_to_24k_grew_pipeline_400/)), trigger outbound, past colleagues.
- **Narrow the wedge:** an AI platform sold one workflow (accounts payable and receivable) to US freight brokers only; first customer $9k ARR, next $30k ARR, and messaging became easy ([r/startups, 242 upvotes](https://www.reddit.com/r/startups/comments/1muqfbw/on_my_4th_startup_raised_money_for_the_first_time/)).
- **Separate user from buyer.** Qualify the budget holder early (edtech failure in [validation.md](validation.md#problem-interviews-that-do-not-lie)).
- **Give the asset, not the login.** Free research reports made with the product turned recipients into demo requests and ambassadors ([r/startups, 733 upvotes](https://www.reddit.com/r/startups/comments/n0hs2l/linkedin_is_a_cringefest_but_it_works_for_b2b/)).
- **Enterprise is slow:** a FOX pilot took 9 months through cold LinkedIn, conferences and warm intros ([r/startups, 940 upvotes](https://www.reddit.com/r/startups/comments/l654ng/how_we_almost_got_acquired_by_facebook_and_failed/)). Price early deals to survive that cycle.
- Cases: Stable's first 100 paying customers served by hand with Drive, Zoom and Stripe ([submit.co 2026](https://submit.co/first-users)); WP Engine's 40 consultant calls and 30 verbal commitments at $50/month before a name.

## Consumer apps

- **Launch where the use case lives,** after testing with makers. r/movies gave 27,000 downloads in a week; a fitness app's second Reddit post brought 5,000 users in two days ([launches-and-press.md](launches-and-press.md#reddit-launches)).
- **Personal network at scale:** 200 to 300 messages per founder reached 400 testers ([r/EntrepreneurRideAlong, 218 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/nu6gp9/we_bootstrapped_to_10000_users_in_6_months_i/)).
- **Ship fast and measure real impressions** instead of long waitlists for cheap-to-build apps (2 to 4 week first release, [r/SideProject, 702 upvotes](https://www.reddit.com/r/SideProject/comments/1dtfhdz/ive_made_over_12_million_from_my_ios_app_side/)).
- **Users are not customers.** A luggage marketplace reached 2,000 users in 1.5 months from WhatsApp groups alone, but few created trips ([r/indiehackers, 46 upvotes](https://www.reddit.com/r/indiehackers/comments/1nmcwro/built_an_app_that_pays_you_for_spare_luggage/)). Measure the activation event and trial-to-paid (RevenueCat 2026: 34.2% median North America).
- Case: Launchli reported 100 users in 30 days from interviews, then Reddit, X and LinkedIn participation and direct conversation ([Fake Mayo, Dec 2025](https://www.fakemayo.com/p/how-sebastian-got-his-first-100-users-from-reddit-x-linkedin-and-manual-outreach)).

## Local services (home, beauty, fitness, health, events)

- **Density first:** one neighborhood, door-to-door with house-specific offers, trucks and signs visible on the job, neighbor names at the door ([manual-acquisition.md](manual-acquisition.md#4-door-to-door-walk-ins-and-local-density)).
- **Google Business Profile on day one,** reviews from every job, 20 to 25 reviews before paid local ads. A free profile produced 2 of a solar-panel cleaner's first 4 jobs plus an installer partnership enquiry ([r/sweatystartup, 114 upvotes](https://www.reddit.com/r/sweatystartup/comments/quksop/update_solar_panel_cleaning_biz_fuck_it_im_in/)). Organic local presence lags: one delivery service got its first two enquiries about 3 months after building site and profile ([r/EntrepreneurRideAlong, 218 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/g2skv2/the_best_88_ive_ever_made_in_my_life_week_two_of/)). Do not wait on it.
- **Lead marketplaces for the first reviews and cash** (Thumbtack, Yelp, Nextdoor), then direct.
- **Presell seasons with deposits** ($90,000 booked in winter at 25% deposits).
- **Partners with repeat demand:** realtors, property managers, builders, adjacent trades.
- Cases: Iztri's first 100 from four buildings; a pet-waste business at 39 properties and $2,000+ monthly subscriptions in three months from vets, shelters, social and word of mouth ([r/sweatystartup, 423 upvotes](https://www.reddit.com/r/sweatystartup/comments/1bxt0rx/yet_another_pet_waste_removal_business_but_its/)); a gym that sold 100 memberships in 14 days from 696 preregistrations (agency case, [Syslo Ventures 2026](https://sysloventures.com/case-study/)).

## Ecommerce and physical products

- **Existing demand first:** a marketplace listing, the hobby community you belong to, one boutique. A product photo posted in the founder's own interest community led to $15,648.74 in 30 days, 30% wholesale ([r/EntrepreneurRideAlong, 140 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/8z7mxo/my_first_ecommerce_store_made_1564874_in_the/)).
- **Presell during production or shipping;** order small batches (AliExpress 100 units, $522, launched in a month vs Alibaba minimums, [r/Entrepreneur, 1,601 upvotes](https://www.reddit.com/r/Entrepreneur/comments/3lltwu/how_i_literally_started_an_amazon_business_in/)).
- **Seed the right people:** Spikeball surveyed every early customer, found three communities, then gave free sets to influential members in exchange for photos ([r/EntrepreneurRideAlong, 253 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/16oik70/from_a_sport_no_one_was_playing_in_the_80s_to_a/)). A backpack brand gifted to niche photography creators and reported 7x revenue over gifting plus payment cost ([r/Entrepreneur, 2,738 upvotes](https://www.reddit.com/r/Entrepreneur/comments/vqr0hm/from_18kmo_to_260kmo_in_5_months_selling_backpacks/)).
- **Empty social profiles sell nothing:** a candle founder's first 5 sales came the day a 20% coupon went into Reddit, Marketplace and Facebook groups.
- Case: IQBAR raised about $74,000 on Kickstarter, half from organic discovery, after alumni outreach seeded momentum ([Shopify 2025](https://www.shopify.com/au/blog/first-customers)).

## Agencies, freelancers, consultants

- **Past clients and network first;** one dormant-account tweet produced a top client in 24 hours.
- **Proof travels:** a published case study sold the same capability to a different industry (law firm to hotels).
- **A one-page audit is the outreach** (18% replies vs 2%); fix one small thing free in person.
- **Never free strategy;** paid entry offer with fixed scope (`agency-freelance`).
- **Avoid long procurement for small deals:** an agency declined an enterprise project cut to a third while meetings, sign-offs and special payment terms stayed ([r/EntrepreneurRideAlong, 158 upvotes](https://www.reddit.com/r/EntrepreneurRideAlong/comments/m5b340/i_fired_a_large_potential_client_this_week_heres/)).

## Coaches, educators, course creators

- **5 personal messages a day,** one community where the buyer asks questions, one free workshop or talk (bookkeeper: one talk, about $30k).
- **Pilot with friends, then a paid cohort,** then the website ([r/smallbusiness, 703 upvotes](https://www.reddit.com/r/smallbusiness/comments/1otuw7c/i_mentally_cannot_do_another_95_desk_job_i_have/)).
- **Demo classes convert when targeted:** UpKraft ran 150+ demos in a few residential clusters, 200+ paying learners in about two months, 31% lead-to-paid ([PedalStart 2026](https://www.pedalstart.com/blog/how-to-get-your-first-customers-a-guide-for-indian-startups), case).

## Creators, newsletters, digital products

- **Audience questions become products:** a creator turned questions too long for a reply into a PDF and a video; each launch made about $40,000 in two weeks with 12,000 and then 24,000 followers ([r/Entrepreneur, 1,539 upvotes](https://www.reddit.com/r/Entrepreneur/comments/iwmzv1/i_made_210822_selling_a_pdf_and_a_video_on_the/)).
- **No audience yet:** launch inside a comment that asked for the exact thing, presell on Carrd plus Gumroad, ship 3 to 5 small products and keep what sells (`digital-products`).
- **Free value at scale:** free automated stock alerts grew 5,000 followers in two weeks before a paid bot.

## Restaurants, shops, venues

- **Opening is the launch:** list building 4 to 6 weeks before, local creators, neighbor partners, a geo-limited push (`restaurant`, `local-retail`).
- **Sell where people already are:** festival and event slots for mobile food and drink; sampling tables; corporate lunches.
- **Do not count on the previous tenant's customers** (`local-retail`); a gym reopening assumed old members would return and reached 400 of a 750 target ([r/smallbusiness, 1,352 upvotes](https://www.reddit.com/r/smallbusiness/comments/1lfs3wn/i_took_over_a_commercial_gym_and_its_been_a/)).

## Marketplaces and communities

- **Hand-recruit the hard side first, where it already sells:** Etsy recruited sellers at craft fairs; Alibaba demonstrated to factories one by one; a photography marketplace was told to narrow to one occasion and recruit photographers locally ([r/Entrepreneur, 3,255 upvotes](https://www.reddit.com/r/Entrepreneur/comments/6d24rb/11_years_ago_i_got_a_428_million_dollar_lesson/)).
- **One spike is not supply:** that marketplace got 100 signups on day one from a friend's Facebook group post, then 3 in the following month.
- **Fill the room yourself** until users do (Quora, Reddit), and keep early activity in one shared space.
- **Bring both sides of one cluster at once** (Tinder: sororities, then the matching fraternities).

## Indie games

- **Player communities, not developer communities;** native Linux builds in r/linux converted better than general gaming subs. Steam page 6 to 12 months before launch (`indie-games`).
