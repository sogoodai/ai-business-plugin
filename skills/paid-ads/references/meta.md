# Meta (Facebook, Instagram, Messenger, WhatsApp)

## What changed in 2025 to 2026

- **Andromeda** is the retrieval stage that picks which ads enter ranking. The 2024 launch raised retrieval recall 6% and ad quality 8% in selected segments; by October 2026 it scores over one billion eligible ads per second, about 100x 2024, and Meta credits it with +2.4% Facebook conversions since 2025 ([Meta Engineering 2024](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/), [2026](https://engineering.fb.com/2026/10/28/ml-applications/meta-andromeda-next-gen-ads-retrieval-gpu-co-design/)). GEM is the ranking model on top. Practical meaning: the ad itself tells Meta who to show it to.
- **Not first-party (folklore):** fixed "1 to 2 campaigns maximum", the "4x4 creative framework", minimum creative counts, and a precise "60% similarity" suppression threshold (AgriciDaniel, MIT). Use them as practitioner heuristics only.
- **Advantage+ everywhere.** Advantage+ Shopping became Advantage+ Sales in 2025; Advantage+ Leads rolled out globally by Q3 2025 with 14% lower CPL on average vs non-users (Meta, platform-stated). Standalone ASC and Advantage+ App campaigns can no longer be created via the Marketing API (v25.0 Feb 2026, all versions from 19 May 2026); v26.0 (29 July 2026) blocks edits and pauses ASC campaigns using `existing_customer_budget_percentage`. Build with unified Advantage+ on standard campaigns (indranilbanerjee harvest, MIT).
- **Sensitive data restrictions** from 2 September 2025: Meta flags custom audiences and custom conversions that imply health conditions or financial status. Name events `Lead`, `QualifiedLead`, `AppointmentBooked`, `Purchase`, never `DiabetesLead` or `BadCreditApplicant`.
- **Attribution:** view windows were cut in January 2026; a window or attribution update can lift reported CPA 30 to 50% overnight (operators). Look for the banner at the top of Ads Manager before panicking, and never compare across that date.

## Structure by budget

| Daily budget | Structure |
|---|---|
| $10 to 50 | 1 campaign, 1 broad ad set (country or radius, age and gender only if the product demands it), 2 to 4 distinct concepts. Judge on real conversations and deals |
| $50 to 250 | 1 core campaign + 1 testing lane or 1 retargeting exception |
| $250 to 1,000 | Scaling CBO (about 80%) with graduated ads; testing CBO or ABO (about 20%); retargeting only if the pool is large |
| $1,000 to 5,000 | Separate by business question: offer, country, margin tier, new vs existing customers. Consider bid caps or cost caps |

Rules from operators that hold across threads:

- **One campaign per offer.** Bundle, BOGO, 50% sale and Black Friday each get their own campaign (4 threads, up to 329 upvotes). Discount buyers were "less loyal".
- **Separate margin tiers.** Different-margin products in one CBO let Meta overspend on low-margin items: group similar margins or use ABO.
- **Stop duplicating to scale at high spend.** A $4.17M account consolidated prospecting, retargeting and offers into one CBO scaled by budget because duplicates overlapped and raised CPM (r/FacebookAds 307). Commenters: below $100/day there are not enough events for that to work.
- **Diversify near $500/day:** 3 to 5 campaigns so a stockout or one failure does not stop acquisition (r/FacebookAds 157).
- **Destination test when the page is the unknown:** one CBO per persona, one ad set per destination type (product page, advertorial, quiz, demo), identical creatives in each (coreyhaines31, practitioner-reported +30% new reach).

## Learning phase math

- Meta's planning target: about 50 optimization events per 7 days per ad set (directional, app-ad documentation). Daily budget needed about target CPA x 50 / 7.
- Below 50 purchases a month, do not use ROAS goals or cost caps; buy volume first (r/FacebookAds 142, disputed as a hard line).
- Optimize for purchase from day one; no "pixel warm-up". Expect purchase-optimized link clicks around $3 against $0.30 on traffic campaigns, and do not kill a test for a high CPC (r/FacebookAds 157, two agreeing commenters). Lebesgue (vendor) claims 90% lower CAC from purchase vs landing-page-view optimization.
- Event fallback when volume is impossible: Purchase, then InitiateCheckout, then AddToCart. Commenters report AddToCart optimization often brings junk traffic; prefer InitiateCheckout and keep importing purchases.
- New brand-new pixel: you may need lookalike, interest or retargeting audiences to seed events, then go broad (r/PPC 127). A new account does not prove a new pixel; classify account, pixel and conversion history separately (AgriciDaniel cold-start contract).
- Lead gen: keep the real business goal as the optimization event even if it shows "Learning limited"; it was cheaper than switching objectives (r/PPC 127).

## Testing framework

Pick one per account and stick to it for a quarter.

**A. Testing lane plus scaling lane (default for $100+/day).**

1. Testing campaign gets about 20% of budget. Each new concept gets its own ad set, code-named (for example `C14-objection-price`), 3 to 6 executions.
2. Per test ad set, budget for 1 to 2 expected conversions a day (at $50 CPA, $50 to 100/day).
3. Judge after 3 to 7 days and at least 1x to 1.5x target CPA; use the staged stop rules in [economics-and-budgets.md](economics-and-budgets.md).
4. Promote 1 to 3 winners a week into the scaling campaign by post ID (keeps likes and comments). Promotion gates operators use: 4 to 5x target CPA spent at target, or 50 to 100 purchases, or a top-10% ad by CPA. Keep the original running in testing so new tests compete against it.
5. A $400k/month account runs it this way: 4 to 5 concepts a week, 5 to 8 variations each, $100/day per concept ad set, $500 to $1,000 per concept before promotion, a testing cost cap about 10% above the scaling cap, winners promoted as flexible ads of 10 to 25 variations (r/FacebookAds 205).

**B. One CBO, new batch per ad set (default under $100/day).** Each new batch of 3 to 8 ads goes into a new ad set inside the existing CBO, never into an existing ad set. Keep under about 60 ad sets per campaign.

**C. Flexible or dynamic creative for lead gen.** 1 campaign, 1 lightly targeted ad set, up to 10 images or videos, 5 primary texts, 5 headlines (r/FacebookAds 100, a 15-year agency reports "a great couple of months"). Hybrid: run dynamic creative for 3 to 5 days to find winning elements, then build manual variations.

Testing rules that save money:

- **Separate formats when testing** (images with images, videos with videos). Observed spend priority: catalog > video/Reels > carousel > static. Mix formats only when scaling.
- **Unstarve ads.** If 3 of 10 ads take all spend, duplicate the campaign without those 3 so Meta must test the other 7. Operators "repeatedly" found another winner this way (2 threads).
- **Force delivery temporarily** with ad-set spend minimums inside CBO (for example $200 split $50 x 4), removed after a few days.
- **Audience tests use a proven creative as the control;** compare Advantage+ audience, broad, interests and lookalikes on cost per result and CPM. Interests or lookalikes sometimes win with lower CPM.
- **Validate concepts as statics, make video only for winners** (2 sources, including a $20M spender).
- **Judge diverse creative at campaign level.** Five identical ads in one ad set gave "wildly different" results, so aggregate before naming winners (r/FacebookAds 122).
- **Zombie relaunch:** after a CBO run Meta leaves about 80% of variants unspent; relaunch high-conviction dead variants in a separate ad set, about 20% come back as winners (coreyhaines31, practitioner-reported).

## Creative volume and diversity

- **Distinct concepts beat variations.** "20 ads = 20 angles, not 4 angles x 5 versions" cut an ad team by 3 people with a higher hit rate (r/FacebookAds 58). Across 2,000+ ads, the first execution of a concept won about 79% of the time in 3-ad batches, so launch one execution per concept and hold one backup unlaunched (r/FacebookAds 164).
- **Hook-only edits on the same core video stopped working post-Andromeda** (r/FacebookAds 231). Cloned Ad Library concepts get deprioritized; original concepts held up.
- **Volume:** 50 creatives per account per month (2024); at $50/day at least 4 new a week; 5 to 8 a week in prospecting at mid budgets; 20 to 40 a week at $400k/month. A stable small DTC account can run on 1 new creative every 7 to 10 days.
- **Lifespan:** no 2024 creative stayed top for more than 5 months vs about 1 year in 2022 and 2 years in 2018 (r/FacebookAds 229). Profitable ads can still last 6 to 12 months: retire on numbers, not on a calendar.
- **Plan on concept x angle x awareness level x persona.** 8 to 15 ads per batch from persona x desire combinations ("new mom, confidence for date night" vs "busy professional, energy"); on small budgets 4 to 6 concepts (30-upvote commenter).
- **Format mix by price:** high-ticket brand video 90% of performance; agency clients under $100 AOV statics beat video 60/40 (r/FacebookAds 164).
- **Static 1:1 at original size across placements;** skip 1.91:1 versions.
- **Identity trigger:** duplicate a winner with a niche word inserted ("462 leads per week" to "462 dental leads per week"); it works as a viewer trigger and a delivery signal (coreyhaines31). Strong for local ("for salon owners in Lyon").

Creative depth: [creative.md](creative.md).

## Frequency, fatigue and relaunch

- **Fatigue vs saturation:** creative fatigue = CTR falls and frequency rises while reach still grows (rotate creative). Audience saturation = reach plateaus while frequency climbs (widen audience or add creators). Never read decay during learning; confirm against order truth (aaron-he-zhu, Apache-2.0).
- **Signals in urgency order:** CPM up 30%+ over 2 weeks (moves first), CTR down 20%+ vs baseline over 7 days, relevance rankings "below average", CPA up with stable targeting. Retire when CTR is down 30%+ from peak (coreyhaines31).
- **Frequency bands (7-day, estimated):** prospecting 1.5 to 2.5, warm retargeting 4 to 7. B2B cold: 1.0 to 2.5 safe, 2.5 to 4.0 warning, over 4.0 critical. Never add spend at frequency 7 to 8 (r/FacebookAds 80). Never compare 28-day frequency with 7-day bands.
- **Rolling month-over-month reach** is the net-new gauge: falling reach while spend holds means you are recycling a shrinking pool. Track net-new reach and its CPM weekly.
- **Check placements before blaming the creative.** One "fatigued" account had Reels eating budget with zero sales; removing it fixed results "almost immediately" (r/FacebookAds 121, disputed by one commenter). Then try an identical relaunch (same ads, budget, targeting) after about 10 declining days, before paying for a reshoot. Also: duplicate the ad and swap only the thumbnail.
- **Refresh by milestone:** a new variation every $5,000 spent on a creative, keeping core elements (r/FacebookAds 160, $100k+/month accounts). Above $5k/day prepare winner variations weekly before they fatigue.
- **Early relaunch:** judge direction in the first $20 to 50. Example: $4 CPC after $20, stopped and relaunched a duplicate, CPC $1.08 held for a month; cap at 3 relaunches (r/FacebookAds 160). A $500k/month buyer warns this over-intervenes.

## Bid strategies

- **Default:** highest volume (no cap) until you know a stable CPA. An aggressive cost cap suppresses delivery and the learning you need (Meta developer guidance). Example: a $9 cost cap on an account with a $9 to 11 CPA produced $45 to 50 CPA on $700 (r/FacebookAds 123).
- **Cost cap ladder to revive old ads:** 1 CBO, 3 ad sets with cost caps at 1.2x, 1.5x and 2.0x AOV ($100 AOV: $120, $150, $200), filled with previously switched-off ads (r/FacebookAds 109, a $400k/month portfolio).
- **Bid cap discovery** (2 threads, 379 and 155 upvotes): only after 50 to 100 sales; minimum $250/day, start $500 to 1,000. Start the bid $5 to 20 below average CPA ($35 average, bid $25). Wait 24 hours; if no volume raise $5 to 10. If $30 gets nothing and $40 spikes, drop to $35 and climb $1 at a time. Expect 7 to 14 volatile days.
- **Cost cap on broad scaling:** cap at 0.8x break-even cost per purchase, with ad sets split US / top 4 countries / worldwide (r/shopify 260).

## Audiences, exclusions and retargeting

- **Cold/warm split with a 6-month engagement exclusion.** Cold excludes anyone who engaged in 6 months; warm targets only them; same creative pool in both; buyers excluded 7 to 30 days. Managed accounts ($30k to 200k/month) went from 0.5 to 1x to over 2x ROAS; a commenter saw prospecting CPM halve (r/FacebookAds 150). Expect it to look worse until day 7.
- **Existing-customer cap at 0%** in Advantage+ sales campaigns for acquisition, with the customer list built from pixel, Klaviyo, Shopify and other syncs. Define existing customers in Advertising Settings and read Breakdown > Audience Segment for new vs existing. A cold campaign that suddenly spends 40% on engaged users (vs 5% before) has drifted.
- **Clean cold tests:** exclude all customers, email subscribers, 30-day site visitors and 1-day engagers; report those as "engaged", not new (r/FacebookAds 205).
- **Retargeting share:** about 20% of spend on 30 to 90 day visitors, ATC and video viewers with FAQ, objection, testimonial and offer-clarification creative. Catalog retargeting capped at 10% of daily budget. Start 80/20 cold/warm and raise warm only as cold grows the pools.
- **Small accounts: merge warm and hot retargeting;** the pools are too small after iOS 14.5.
- **The 3-minute non-converter:** visitors who spent 3+ minutes on site without converting get their own retargeting at higher bids and are excluded from cold. Reported 2.4x better than regular retargeting and about +20% account ROAS (r/PPC 160, 70-upvote comment).
- **Retarget with a different offer, not the same offer harder:** another product, a free audit, a different lead magnet (coreyhaines31). First retargeting touch can be help, not a discount: "Hey, a quick reminder, if you have some questions or need help, let us know" (r/ecommerce 173).
- **Lookalike seeds** in priority order: high-LTV purchasers 1%, all converters 1 to 3%, add to cart, visitors, video viewers, engagers. Seed minimum 100, 1,000+ recommended. Never seed from traffic or engagement campaigns.
- **Getting the original audience back from Advantage+ audience:** "Further limit the reach of your ads" > "Switch setup", uncheck "Use as a suggestion"; limiting 2+ parameters turns Advantage+ audience off. Exclusions sit under Audience controls.
- **Audience Segments report:** if early sales come from already-engaged users, the campaign has not found cold buyers yet.

## CAPI and event match quality

- Run browser pixel and Conversions API together, with the same `event_id` and identical `event_name` (case-sensitive: "lead" vs "Lead" double counts). A healthy pair shows one "Deduplicated" row in Test Events. Send the server event within seconds, not batched hours later. CAPI rejects `event_time` older than 7 days (physical store events 62 days). The standalone Offline Conversions API shut down 14 May 2025; send offline events through CAPI with `action_source`.
- **EMQ drivers in order:** hashed email, hashed phone (E.164), fbc, fbp, IP + user agent, name and ZIP, external_id; SHA-256 after lowercase and trim. Browser-only Lead events score 3 to 5, full server sends 8 to 10 (practitioner-reported). Changes take 24 to 48 hours to show.
- **EMQ fix in 5 minutes:** Events Manager > Settings > automatic advanced matching on > show customer information parameters > enable all. Purchase EMQ around 9 to 9.6 follows on Shopify (r/FacebookAds 214). Turn off "Track events automatically without code" if it over-reports.
- **One sender per event.** A Shopify app, a separate CAPI setup, site code and checkout code all firing Purchase is triple counting (r/FacebookAds 74). Always ask what already sends server-side (Shopify channel, Zapier, sGTM).
- **Silent failure:** a hosted CAPI plan that hits its event limit with auto-upgrade off just stops. CAC went from $35 to $90 until the plan was fixed (r/FacebookAds 118).
- **CRM to CAPI** for leads: send Qualified and Won stages back; Meta's CRM optimization wants 200+ leads a month, stage reached within 28 days, daily uploads.
- **Bots train the algorithm.** 60 add to carts and 61 checkouts against 2 purchases in a day is a bot signature. Optimize on purchase or offline events, put Cloudflare WAF in front, remove products that attract bot traffic from the catalog.

## Lead ads and lead quality

- **Form type:** Higher Intent (review screen before submit). Require a field that cannot autofill (work email or a short text answer). Add 1 to 3 multiple-choice qualifiers, easiest first; 4+ spikes abandonment (coreyhaines31).
- **Sequences that work** (research report, operator templates): local service "What do you need help with?" then "When do you need it?" then contact details then confirmation "Thanks, call us now for the fastest response." B2B: "What are you trying to improve?" then "Company size?" then work email then "Book a 15-minute fit call."
- **Put the price band on the form** ($6,500 to 9,500) so under-budget leads do not book calls (r/FacebookAds 836). Use the completion screen to tell leads to check their inbox.
- **Form vs landing page:** landing page converting 5%+ use the page; under about 2% use the instant form; demos and trials on a page, content and webinars on a form (coreyhaines31). For call-closed, high-ticket offers, a website Lead event beats instant forms (higher CPM and CPC, better prospects); instant forms gave only 5 to 10% usable leads for one high-ticket B2B offer.
- **Lead quality collapses:** inspect the conversion event and form friction before narrowing the audience. Then tighten geo to the real service area, add a qualifier, and feed `QualifiedLead` back.
- **Proven lead-gen setup** (10th run of the same offer): 1 CBO, 1 ad set, 1 ad at $70/day, website conversion location, Leads event, Audience Network off, Advantage+ creative off, start scheduled at 00:00. 92.31% show rate, 38.46% close rate over 19 days (r/FacebookAds 52).
- **Speed:** every form lead gets an instant SMS and email plus a staff alert; call within 5 minutes; double-dial. A dental clinic booked 35% of 166 form leads with 5 automated touches (r/DigitalMarketing 131). Details: [offers-and-post-click.md](offers-and-post-click.md).
- **Budget direction in lead gen:** raising budget 20 to 40% raised CPL in one account; duplicating worked better (r/FacebookAds 73).

## Messaging ads (WhatsApp, Messenger, Instagram DM)

- **When:** businesses where a conversation is itself high intent: home services, clinics where allowed, tutoring, beauty, auto, travel, and markets where WhatsApp is the default channel. Leads objective supports forms, website, Messenger and calls; Sales can optimize to Messenger or WhatsApp destinations (Meta API docs).
- **Judge the funnel:** message start, then qualified conversation, then booked appointment or sale. Never judge message-start CPA alone. Cross-check reported conversations against the real inbox: one Messenger campaign reported 0 conversation starts in a week that brought several enquiries (r/PPC 121).
- **WhatsApp economics:** per-message pricing since 1 July 2025. A user who replies within 24 hours of a click-to-WhatsApp ad opens a free entry point window of 72 hours in which your messages, including templates, are free (vendor documentation, [SleekFlow](https://help.sleekflow.io/en_US/understanding-click-to-whatsapp-ads-ctwa-and-the-72-hour-free-window)); one vendor reports Meta extended it to up to 7 days from 28 September 2026, unconfirmed in Meta's docs. The ad click itself is billed as usual. Rate card from 1 October 2026, USD per marketing / utility message: India 0.0118 / 0.0014, Brazil 0.0625 / 0.0068, UK 0.0635 / 0.0220, Germany 0.1365 / 0.0550, North America 0.0250 / 0.0034 (WACRM transcription). Misclassifying marketing as utility gets templates reclassified or rejected. Fetch the live rate card before quoting.
- **Script the first reply** within seconds (an auto-greeting with 2 or 3 quick-reply buttons: service, timing, price question), then a human within the business-hours SLA. Welcome scripts and consent rules: `email-sms-loyalty` (whatsapp.md).
- **Comment-triggered DM:** a post engagement campaign whose comments start a Messenger or Instagram automation ("comment GUIDE and I'll send it"); reported 300+ sales in a month from a free-guide-to-$20-guide flow, called comment-farming by others.

## Account and setting traps (check every account, recheck after edits)

- Advertiser Settings > Advantage+ creative > "Test new optimizations" or "Test new enhancements" is on by default and can alter up to 5% of impressions even with ad-level enhancements off.
- AI translations ran for 10 months despite a summary showing "off", sending English-only offers to non-English viewers: high CTR, instant bounce (r/FacebookAds 55). Toggles came back within minutes or after about 5 days in several reports.
- "Test new AI generation features" can generate Meta-hosted landing pages where your pixel does not fire; product browsing defaults can send clicks to Meta-hosted pages (vendor post, Oct 2026). Audit 30 days of change history for image expansion, overlays, music and auto headlines.
- Untick "relevant ads" and multi-advertiser ads on every duplicate. "Add catalog items" can put client A's products in client B's ads when duplicating across accounts.
- Selecting "Instagram only" still sent 43% of a $600 test to Facebook and Threads (r/FacebookAds 90). Check the placement breakdown, not the setting.
- Audience Network red flag: CPC about 20% of normal with 6 to 10x normal CTR and no profit. Placement exclusions may now behave as a "-90% bid" rather than a hard exclusion.
- Opportunity Score recommendations: hover the "i" to see whether it is real-time modelling or an old experiment.
- Ad-level scheduling exists for promotions under "show more options". Dayparting from hourly breakdowns saved 20 to 30% in one account; others warn early impressions assist later purchases. Test it, do not assume it.

## Scaling rules specific to Meta

See [economics-and-budgets.md](economics-and-budgets.md#scale). Meta-specific additions: concentrate on what sells (one watch variant had 70% of sales on under 30% of budget; going exclusive with a new offer and page took ROAS from 63% to 401%, r/FacebookAds 197); keep prospecting even when its own ROAS is below retargeting; do not edit a winning ad set except budget; and halve the budget once as a cheap incrementality check (at about $10k/month a 50% cut left results unchanged, r/FacebookAds 277).
