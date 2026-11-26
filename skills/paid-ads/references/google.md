# Google Ads (Search, Performance Max, AI Max, Demand Gen, YouTube, LSA) and Microsoft

## Settings to fix before any spend

Seven or more threads agree on each of these; most are defaults that cost money.

| Setting | Set to | Why |
|---|---|---|
| Location option | "Presence: people in or regularly in your included locations" | "Presence or interest" lets "USA plumbing" searched from abroad qualify; one B2B account got 10x clicks from an excluded country until fixed (r/googleads 54) |
| Networks on Search | Search Partners off, Display expansion off | Partners off: ROAS +15 to 25% (r/googleads 101); partner spend jumped 200 to 1,000% mid-year in one agency's accounts with sales flat |
| Account-level channel controls | Search Partners and Display at Low priority and 0% budget, including PMax; screenshot the saved settings | Settings revert silently; ask your rep for the "3P Inventory Control" beta (r/PPC 138) |
| Auto-apply recommendations | Off, then search change history for "Google Ads Team [with user permission]" | "Upgrade your keywords to broad" replaces exact and phrase with broad (63 upvotes) |
| Account-level automated assets | Assets > More > Account-level automated assets > Advanced settings: all off | An old opt-out did not cover the new Location option; one sitelink read "Smoked Dog Bones" |
| Location Manager | Tools > Shared library > Location manager > Settings: "Google Owned Location Data" off | On by default even in manual CPC campaigns (r/PPC 103) |
| PMax asset optimization | "Sourced videos" off | Can pull up to 10 of your videos from social or site onto a Google-owned channel under your name (r/googleads 24) |
| Conversion goals | One primary per campaign goal, fired on the thank-you state; everything else secondary | Accounts often run 4 to 5 primaries including page views |
| Budget on invoiced accounts | Account-level budget, reset on the 1st | Prevents the $104k and EUR 50k overspend stories ([operations](operations-and-agency-tricks.md)) |
| Language targeting | Know it keys off the user's interface language, not the query | Manual language criterion unsupported for Search and AI Max from Sept 2026 |

## Account structure

- **Minimum viable split, each with its own budget:** Brand, Non-brand high intent, Competitor (with comparison pages), Remarketing. Never share a budget with brand: the cheap brand campaign starves the campaigns you need data from (coreyhaines31, MIT).
- **Intent ladder:** brand, then high-intent non-brand (the profit center), then competitor, then problem-aware, then Demand Gen, YouTube and Display last. Do not open a rung until the one below converts to pipeline. If category search volume is near zero, Search cannot create demand: say so and move budget to social.
- **Themed ad groups, not single-keyword groups:** 5 to 15 closely related keywords one promise can answer; split when two keywords need different pages; 2 to 3 RSAs per ad group. Consolidate any campaign that cannot reach about 15 to 30 conversions a month.
- **Local templates:** single location = Core services (radius), Emergency (radius, 24/7, urgent page), Brand, optional Competitor. Multi-market = one campaign per service x market, plus brand.
- **Under $2,000 a month in ecommerce, consolidate:** $1,948.89 spend gave 20 conversions, 19 from PMax (r/googleads 35). Keep PMax plus a small brand campaign; do not split by margin yet.
- **Keyword cleanup works:** one account went from 18,000 keywords (built on strategist advice) to 50, with 10x revenue at half the spend (r/PPC 142, 49-upvote comment).

## Match types now

- Exact and phrase no longer mean literal. Close variants leak: an exact-only account had 53% of spend under "Other search terms", none of it converting (r/PPC 41); a B2B account saw CPA rise from $120 to 250 to $400 to 600 as "exact (close variant)" pulled consumer intent.
- **Small and new accounts:** exact + phrase on the highest-intent themes, starter negatives on day one, Max Clicks with a CPC cap or Max Conversions. Six threads agree; exact only plus 500 negatives cut cost 60 to 70% in client accounts.
- **Broad match:** Google says broad works with Smart Bidding and match-type segmentation is unnecessary ([Google](https://support.google.com/google-ads/answer/10195720)); its "25% more conversions" figure is 2020 data. Gate it: 30+ conversions a month, smart bidding live, clean primary conversion, tight negatives. Then add broad versions of proven exact winners, or run broad as an experiment arm with 20 to 25% of budget, same ads and negatives, and a portfolio max CPC cap so you do not buy $100 clicks against a $6 to 10 average.
- **Where broad works:** non-brand ecommerce with Max Conversion Value (brand added as negatives) improved ROAS "with minimal management" for a 10-year practitioner (r/PPC 179). Where it fails: niche B2B, one keyword went from $4.01 manual to $31.76 automated (r/PPC 117).
- **Cut informational queries:** research-phase traffic converted 12x worse than purchase intent ("[product] pricing", "buy [solution] for [use case]") in a high-six-figure account (r/PPC 95).

## Negatives hygiene

- **No invented negatives:** without a search-terms report, name zero candidates. Starter lists for net-new local builds are allowed if labelled: jobs, salary, hiring, career, intern, indeed, free (unless free estimates), DIY, how to, tutorial, youtube, reddit, wiki, pdf, template, reviews, complaints, same-name cities you do not serve, your own brand in non-brand campaigns.
- **Classify every new term:** relevant high intent, relevant low intent, irrelevant, competitor, existing customer, job/research/support. Negate only intents the business does not want; do not negate every non-converting phrase after a few clicks (break-even CVR check in [economics-and-budgets.md](economics-and-budgets.md)).
- **Weekly three passes:** waste (3+ clicks, zero conversions, irrelevant: negative), winners (converting terms not yet keywords: add exact or phrase), drift (adjacent wrong meanings: tighten).
- **Search terms are a sample:** on low-volume accounts 50 to 65% of clicks have no disclosed term; always say "N disclosed of M clicks".
- **Broad negatives with misspellings:** for an unwanted "smith's physio", add smith, smiths, smit, smits as broad negatives (r/PPC 33). Negative broad "free trial" needs all words, so it does not block "free".
- **Rule-based exact negatives by script, hourly:** each ad group gets AND/OR word rules ("discount" AND "auto" AND "parts"); any query failing the rule becomes an exact negative. Also protects brand campaigns from look-alike names (r/PPC 179, 109-upvote comment). A simpler public script checks TODAY and LAST_7_DAYS search terms against enabled keywords, allows plural variants, and has a `DRY_RUN` flag (r/googleads 32).
- **Shared lists at MCC or account level:** jobs, free, DIY, employment (one account wasted $5,000 on job seekers).
- **Google Ads Editor** reviews 1,000+ daily terms in 15 to 30 minutes vs an hour in the browser.

## RSAs and assets

- Google recommends 8 to 10 headlines with at least 5 genuinely unique, 2 keyword-bearing, 3 that do not repeat keywords, and at least 2 unique descriptions ([Google](https://support.google.com/google-ads/answer/10530456)). A second RSA in an ad group: +6.6% conversions at similar CPA; a third: +3.7% (Google averages).
- **Spec:** 15 headlines of 30 characters, 4 descriptions of 90, 2 paths of 15. Mix for 15: 3 to 4 keyword, 3 to 4 benefit, 2 to 3 proof, 2 to 3 CTA, 1 to 2 differentiators, 1 brand. LLMs return 4 to 6 headlines and miscount characters: ask for the full set and count.
- **Service-business headline set:** "[Service] in [City]", "Get a Quote Today", "Same-Week Appointments", "4.9 Stars, [X] Reviews" or "Licensed and Insured Since 2005", "Upfront Pricing", "No Long-Term Contract", "Family-Owned", "Book Online", "Call [Business]", "[Offer]".
- **Ignore Ad Strength:** "Excellent" RSAs averaged $28.68 CPA vs $12.43 for "Average" across about 20,000 accounts (Optmyzr via r/PPC 33); Google's liaison says it is not used in the auction.
- **Pin sparingly:** 1 to 3 pinned assets averaged $13.68 CPA vs $32.57 fully pinned (Optmyzr). Sentence case beat Title Case ($7.46 vs $27.47 CPA, correlational). AI Max with URL expansion can ignore pins, so pin only regulatory text there. A practitioner pattern: 5 keyword headlines pinned to position 1 and 5 offer headlines to position 2; position 3 rarely shows.
- **Auto-created assets:** reported "often 40% worse"; audits found "We're Hiring" as a grocery chain's top combination for 4 months. Review and pause losers.
- **Ad-group-level sitelinks** matched to each category theme lifted ecommerce sales enough to become an SOP (r/PPC 160).
- **Show the price** in ecommerce ads to pre-qualify clicks (r/dropship 387).
- **Call-only ads:** creation removed February 2026, serving stops February 2027; use RSAs with call assets (AgriciDaniel, dated 2026-10-12).

## Bidding ladder

| Conversions per campaign per 30 days | Strategy |
|---|---|
| 0 to 15 | Max Clicks with a max CPC cap ($1 on a fresh account; uncapped clicks hit $50 to 100) or Max Conversions without target, or manual CPC |
| 15 to 30 | Max Conversions; check spend daily the first week (a $12.50/day budget spent about $25/day for 3 days) |
| 30+ stable | tCPA at the trailing 30-day actual (or within 10% of it) |
| 30+ with real values (50 for tROAS evaluation) | tROAS at 0.9 to 1.0x trailing ROAS |

Sources: coreyhaines31 and aaron-he-zhu (MIT, Apache-2.0), Google guidance. Move targets 10 to 15% per step, never over 30%; wait 1 to 2 conversion cycles. Starting formula from practitioners: tCPA = 30-day cost per conversion minus 10 to 15% for efficiency or plus 10 to 15% for volume.

- **Max Clicks to tCPA:** run Max Clicks for one conversion cycle (15 to 30 days), then Max Conversions with tCPA (r/PPC 107).
- **No target in the first 45 to 60 days of a new campaign** (r/googleads 34); threshold opinions range from 20 to 60 conversions a month.
- **Manual CPC is not dead** for B2B exact match, or when manual clicks come out 300 to 400% cheaper than Smart Bidding. Manual CPC disables AI Max search-term matching.
- **Portfolio caps:** a portfolio Max Conversions or tCPA with a max CPC ceiling set from margin stops $50 to 75 clicks.
- **Never a target plus a binding budget cap.** Either a target with budget about 15% above actual spend (effectively uncapped), or a capped budget with no target (r/PPC 45).
- **Control spend with the budget, not the target.** Raising tROAS to slow PMax raised CPCs; lowering it from 11 to 9.5 also raised CPC (EUR 0.55 to 0.75). Direction is unreliable.
- **Value-based bidding fixes day-of-week skew:** an event business got all inquiries on Saturdays under conversion bidding; assign Saturday bookings $10 and other days $50 via offline values or the event date chosen in the form (r/PPC 107).
- **Classify auto-created conversion-based audience lists by customer type yourself** in Audience Manager (change of 18 August 2026) to protect new vs returning bidding.

### The 17 August 2026 target change

Budget-limited tCPA and tROAS campaigns now aim to hit the target rather than beat it, and targets do not update automatically (five threads, plus the Bid Target Adjustment Tool reported from 6 July 2026).

- **Fix:** reset targets to actual performance. A $10 tCPA campaign delivering $5 gets a $5 target. One practitioner did this across $5 to 9k/day accounts and held 4.3x tROAS.
- **Audit rule:** window = the longest of 14 days, 2 conversion cycles, or 30 conversions (tCPA) / 60 (tROAS). Overperforming = actual CPA under 0.8x tCPA, or actual ROAS above 1.2x tROAS. Move the target between the current setting and actual (r/PPC 53).
- **Restarting volume on Shopping** where target was 300% and history 3,000 to 4,000%: uncap the budget first, then step tROAS 3,000%, 2,000%, 1,500%, 3 to 4 weeks per step. Jumping straight to 300% uncapped delivers about 300%.
- **Diagnosis:** compare absolute-top impression share, impression share lost to rank, and a no-target control (brand on Target Impression Share saw CPC fall 53% while target campaigns rose: CPC EUR 0.22 to 0.67, ROAS 33x to 9.1x, r/googleads 17).
- **Budget only where marginal economics allow:** at $70 actual vs $100 tCPA, extra customers at $95 suit one business and not one with a $75 margin ceiling.

## Brand campaigns

- **Run brand on Target Impression Share,** absolute top, a cap (start at $1 max CPC), aiming for about 90%, not 100% (pushing to 100% inflates CPC). 8 of 31 audited accounts ran brand on Max Conversions or tCPA; one branded click cost $103 vs a usual $2.50 (r/PPC 212).
- **Do not kill brand when competitors bid on your name.** An education SaaS paused brand and stopped after 2.5 weeks because leads dropped, estimating 58% more leads if it had stayed on; another pause cut branded impressions 60% in 3 days (r/googleads 58, 34).
- **Brand pause test, done right:** only if you are the sole bidder and own the organic results. Watch total brand conversions (paid + organic). If the total holds, you were cannibalizing.
- **Exclude existing customers from brand:** track the "Log In" button click in GTM, build "Customers: clicked Log In" in GA4 and exclude it from brand campaigns; or exclude visitors to logged-in URLs. Reported to save "thousands per quarter" (r/googleads 119).
- **Search Console overlap:** join 90 days of paid terms with organic queries; buckets: double-paying (organic position 3 or better, no competing bidders), defensible (competitors bid), paid-only winners (SEO roadmap), organic-only converters (scale candidates) (Ryze, MIT).

## Performance Max

- **Not the first campaign** for local lead gen, weak tracking or tiny budgets. Fencing: $6,900 for 50 Google-reported leads, 0 real (r/googleads 39). Plumbing: a PMax test showed $11 CPL on 9 leads, but only 1 was non-brand, against a $35 historical CPL (r/PPC 121).
- **Lead gen setup:** brand exclusions (they also block misspellings and foreign-script versions, [Google](https://support.google.com/google-ads/answer/14587068)), campaign-level negatives, Presence location, Final URL expansion off or URL exclusions, placement report reviewed, CRM-graded lead quality vs Search leads, offline conversions as the bidding goal ([Google lead gen guidance](https://support.google.com/google-ads/answer/13775965)). Check its search terms every week for the first 3 weeks: a plumbing PMax matched electrician, DIY, handyman and competitor names.
- **Ecommerce at small budgets:** feed-only PMax (no text, image or video assets) until EUR 200 to 300/day, then one general PMax plus one per important category. EUR 100/day did EUR 10 to 12k at 10x ROAS in month 1 (r/googleads 34, self-report). At $2M+/month, 85 to 95% of PMax cost still went to Shopping ads (r/PPC 158).
- **Feed:** buyer-intent words in titles via a Merchant Center supplemental feed; first ~70 characters of titles matter; GTINs, price match with the page, margin custom labels (grouped by item group ID so variants do not get conflicting labels); feed refresh at least daily, ideally every 6 hours; products whose spend exceeds the cost per purchase go to a low-bid "graveyard" campaign; a product taking over 50% of budget gets its own campaign.
- **Signals:** customer lists as signals and exclusions (10 of 31 audited accounts had none), converting search terms as a custom segment.
- **Video:** supply your own; auto-generated slideshows made one agency stop running PMax for clients without video.
- **Placements:** PMax honors account and MCC placement exclusions. An LLM classified a PMax placement list into spam, gaming junk and off-topic with 95 to 98% accuracy on obvious junk (r/PPC 34).
- **Diagnose drops** by Shopping vs non-Shopping click share (Mike Rhodes's PMax script) and by query mix: generic share rising from 23% to 30% while brand fell 61% to 53% preceded a 28% order drop.
- **Overlap:** 91% of 503 accounts had exact keyword overlap between Search and PMax (Optmyzr, Feb 2025, prevalence only).
- **Evaluate over at least 6 weeks;** experiments run 4 to 6 weeks and discard the first 7 days; upload seasonal assets 2+ weeks ahead.

## AI Max

- **What it is:** search-term matching (keywordless), text customization and Final URL expansion on Search. Google reports +7% conversions at similar CPA/ROAS for the full suite vs search-term matching alone (April 2026, platform-stated, not vs classic Search).
- **Auto-upgrade:** campaigns with campaign-level broad match plus automatically created assets began auto-upgrading in September 2026; DSA migrates from February 2027. To opt out, turn off campaign-level broad, auto-created assets and auto-apply. Add exact-match copies of key broad keywords; they do not inherit history.
- **Field results:** a CNC software reseller saw 955 distinct queries and 72% of visible spend irrelevant with AI Max on, versus 30 queries the next week with it off (r/PPC 32). On $500k to 1M/year accounts already on broad, the visible vs "other search terms" conversion split moved from 60/40 to 35/65. Gains appeared mainly in phrase-and-exact-only campaigns; at about $15k/month it matched addresses and needed thousands of negatives. One test was up early and below account average by month 3.
- **Rule:** experiment only, 50/50, brand and location controls on, weekly search terms for 3 months, judge on CRM quality. Skip on budget-limited or small accounts (Google itself notes it may be ineffective when budget-limited).
- **Disapproval trap:** AI Max wrote descriptions containing phone numbers, which were disapproved and silently stopped serving. Pull the disapproval list on a schedule.
- **AI Overviews:** ad inventory there needs AI Max, broad or PMax; exact and phrase show only when the query itself is commercial (unverified practitioner claim).

## Demand Gen and YouTube

- Demand Gen is not "PMax lite": it runs on YouTube, Discover and Gmail with more control over placements, audiences and creative. Video Action Campaigns were all upgraded to Demand Gen by April 2026; Demand Gen has an enforced minimum daily budget since 1 April 2026.
- Under about $250/day, running Search, PMax and Demand Gen together fragments data (operator heuristic).
- Use it for remarketing with creative matched to where people dropped off, and as a feeder for retargeting pools. Display only to past search clickers; Search clicks converted 3 to 5x better than Display in seven-figure accounts (r/PPC 162).
- Placement hygiene: export placements, filter 0 conversions, sort by spend, exclude; keep mobile-app placements out.
- Research: VidTao shows competitors' YouTube ad spend over time.

## Offline conversions and Enhanced Conversions for Leads

- **The single highest-impact Google move for lead gen** (coreyhaines31): import qualified, booked and won stages with values.
- Google now recommends Enhanced Conversions for Leads over legacy GCLID-only import; advertisers combining hashed email or phone with GCLID saw a median +10% recorded conversions. Settings unified in April 2026; Data Manager is the preferred upload route from 15 June 2026; uploads within 63 days of the click ([Google](https://support.google.com/google-ads/answer/2998031)). Keep both identifiers. When migrating, wait the longer of 3 conversion cycles or 4 weeks before making the new action primary.
- **Value ladder:** low value for on-site behavior, medium for calls and forms, higher for contacted or qualified, actual deal value at close.
- **Capture:** GCLID, gbraid and wbraid written to hidden form fields at first touch (Safari caps JS cookies at 7 days, 24 hours with a click ID in the URL). Third-party booking or thank-you pages on another domain lose `_gcl_aw`, conversions vanish, tCPA lowers bids, impressions fall next.
- **Test free:** visit `yoursite.com/?gclid=test`, submit the form, confirm the CRM stored it.
- **Refunds:** conversion adjustments need gclid or gbraid and usually order_id, within 54 days (7 days to affect bidding).

## Calls

- Calls are the primary local conversion. Use dynamic number insertion (CallRail, CallTrackingMetrics), a tracking number on the call asset, the canonical number on GBP (see `local-seo`).
- Count calls over a duration you choose (60 seconds is common) or booked calls, not phone-button taps. Call asset "Clicks" counts every ad click while the asset showed, not taps: segment by click type.
- Report Editor's call details show time, duration and caller number; use them when staff say "no calls from ads".
- Google-hosted lead forms produce false conversions for phone-driven firms (r/googleads 19).
- Emergency trades: send "emergency plumber" type terms to call-focused ads with no landing page step. One rebuild went from $1,300 for 3 poor leads to 4 good leads on $1,100, then scaled to $5k/month (r/googleads 21).

## Local Services Ads (summary)

Pay per valid lead, shown above Search ads. Ranking inputs include bid, responsiveness, proximity, reviews, profile quality and hours; Google recommends Maximize Leads ([Google](https://support.google.com/localservices/answer/7527305)). A missed business-hours call held over 20 seconds can be chargeable; leads are evaluated for automatic credits over 30 days, but EEA advertisers do not get credits; Google Guaranteed, Screened and License Verified merged into Google Verified from October 2025. Operating rules: 90%+ answer rate, pause hours you cannot answer, mark every lead, reconcile charges against CRM weekly, use LSA as the baseline lead source (inventory is capped) and Search for growth. Category mismatch is deadly: a specialist roofer listed as "roofing contractor" got 95% irrelevant leads (r/PPC 114). Full mechanics, disputes, CPL by trade and test design: `home-services` (lsa-and-lead-platforms.md).

## Microsoft Advertising

- Most efficient as a second deployment of a proven Google Search build: import, constrain budget, verify UET, add negatives, then consider Microsoft PMax (research report).
- A copied PMax and Shopping setup got 0 conversions in 30 days at similar CPCs (r/PPC 34): import Search first, not PMax.
- Bidding minimums (unverified): tCPA 30+ a month, Max Conversions 15+, tROAS 50+. Audiences need 300 users to activate. LinkedIn profile targeting is the unique lever for B2B.
- Coaching example: Google + Microsoft on direct-demand terms ("confidence coaching") at $150/day (r/lifecoaching 187).

## Click fraud and invalid traffic

- **Check the network first:** about $3,000 over 6 months for 2,500 clicks and 1 lead was Search Partners (r/googleads 102).
- **Clarity recordings:** repeated IPs, no scroll, no mouse movement, instant exits. "Click fraud" is often a slow page: 4G users leaving during an 8-second load look like bots.
- **Bot honeypot on forms:** a question with a default answer; default-answer submissions go to a separate thank-you page that is not a conversion. "Filters out most spam" (r/googleads 119).
- **Click-fraud tools** did nothing in one account; Google found 1 invalid click of 2,500 and refunded $0.54. Fix setup before buying tools. Attach Clarity recordings to refund claims.
- **Google rep clicks:** one advertiser traced repeated calls to an outsourced Google contractor's area code and excluded that location; rep clicks stopped (r/googleads 58).
