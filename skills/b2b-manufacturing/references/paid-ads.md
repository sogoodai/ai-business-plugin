# Google and LinkedIn ads for industrial firms

Account mechanics (bidding ladders, learning floors, match types, PMax, creative testing, audits) live in the `paid-ads` skill. This file keeps what changes for a manufacturer, supplier or distributor: tiny search volumes, long cycles, quotes instead of carts, and a buying committee. Sources in [sources.md](sources.md).

## The budget reality first

| | Google Search, Industrial and Commercial | LinkedIn, B2B |
|---|---|---|
| CTR | 6.57% | 0.67% (spend-weighted) |
| CPC | $5.87 | $9.39 (spend-weighted) |
| Click to lead | 8.20% | 5.9% |
| CPL | $75.19 (average) | $376 median advertiser; under $196 top quartile; over $658 bottom quartile |
| Source | WordStream/LocaliQ, 13,000+ US campaigns, Apr 2025 to Mar 2026 | Metadata, 138 advertisers, $57.6M, 2025 |

Industrial Search CPL improved from $85.63 (2025 edition) to $75.19 while CPC rose from $5.70 to $5.87. Both datasets are vendor aggregates with mixed conversion definitions. Use them to sanity-check, then judge on your own qualified-RFQ and PO economics.

Among 29 Metadata advertisers under 200 employees (broad B2B, not manufacturing), LinkedIn customer acquisition cost was $30,739, ad-sourced opportunity close rate 20.7%, sourced pipeline 4.0x spend, and closed-won ROAS 1.37x at measurement time. LinkedIn works only when one customer is worth tens of thousands in gross profit.

```
allowable cost per qualified RFQ = gross profit per new customer (first 12 to 24 months) x RFQ-to-PO rate x share you accept (start 20 to 30%)
  example: $40,000 GP x 21% quote-to-PO (Factur 2026) x 25% = $2,100 per qualified RFQ
learning budget check (Google): 30 conversions x expected cost per conversion per month at the bidded event
if the bidded event is too rare to reach the floor, bid on the next event up the funnel or stay on manual or Max Clicks with tight keywords
```

A Google rep called $50 per conversion "too expensive" for a custom-forklift maker whose single sales reach five figures ([r/PPC 107](https://www.reddit.com/r/PPC/comments/cjhjwa/anyone_else_just_about_had_it_with_google_reps/)). Judge cost per lead against deal value and close rate, never against an all-industry average.

## Google Search: capture the buyer who already knows what to search

Industrial search volume is small and specific, which is an advantage: the right 50 terms can carry the account.

**Phase plan** (research synthesis):

1. **Phase A:** tightly grouped Search campaigns on explicit process or product terms plus a qualifier: material, tolerance, certification, industry, geography, "quote", "manufacturer", "supplier", part numbers. Exact and phrase match. Manual CPC or Maximize Clicks with a cap while data is thin.
2. **Phase B:** capture the GCLID in a hidden form field and the CRM. Upload qualified RFQ and won PO outcomes with Enhanced Conversions for Leads. Make "qualified RFQ" the primary conversion; RFQ submitted secondary.
3. **Phase C:** add values (expected gross profit band or quote value) where data is reliable.
4. **Phase D:** test AI Max for Search against the control as an experiment. Google reports +14% conversions at similar CPA for advertisers who enabled it, +27% for accounts heavy in exact and phrase (Google's own 2025 rollout figures, not industrial).
5. **Phase E:** review the search terms it adds and the qualified-opportunity cost, never Google's aggregate "conversions".

**Conversion taxonomy**

- Primary: qualified RFQ, accepted quote, PO.
- Secondary: RFQ submitted, phone call over a set length (90 seconds or more), distributor enquiry.
- Observation only: datasheet or CAD download, generic contact, careers form, newsletter.

Never let Smart Bidding optimize all of these as equal "conversions": it will buy students, job seekers and competitors who download PDFs.

**Mechanics that matter for long cycles**

- Google moved Enhanced Conversions settings into one place in April 2026 and made Data Manager the preferred upload route from 15 June 2026. Adding hashed email or phone to GCLID import gave a median +10% measured conversions (Google). Upload windows are limited (the `paid-ads` skill tracks the current window), so a PO that lands 6 to 10 months after the click cannot be uploaded. Upload the earliest stage that predicts revenue, usually qualified RFQ or quote sent, and judge POs in the CRM.
- Keep careers, students and DIY away: negatives such as jobs, careers, salary, hiring, internship, course, training, school, degree, DIY, "how to", homemade, free, used (unless you sell used), plus each wrong material, wrong process and wrong industry you see in search terms. Review search terms weekly for the first month.
- Use location targeting by "presence" and match the service radius you can actually ship or serve. For national suppliers, segment campaigns by region only if you have regional capacity or pricing.
- Schedule ads to business hours in the buyer's time zone if calls matter; plant buyers start early.
- Brand campaign on your own name is cheap insurance when competitors or directories bid on it.

**Ad copy: concrete and literally true**

Research synthesis hooks (each claim must appear on the landing page):

> ISO 9001 CNC Machining | ±[actual tolerance] | Quote From Your Drawing
> [Material] Fabrication for [industry] | [Certification] | Upload CAD for Review
> Replacement [component or service] | [Service radius] | Emergency or Planned Shutdown Support

Angle ideas from practitioners (cross-border forged, cast and fabricated parts; proposed, untested, [r/b2bmarketing 22](https://www.reddit.com/r/b2bmarketing/comments/1jnhbs8/i_write_scrollstopping_b2b_ad_ideas_want_3/)):

> "You don't buy parts. You buy certainty. Wrong spec? Late shipment? Customs delay? That's not just a headache… it's lost money."
> "It's not just metal. It's margin. Bad parts stall production. Late deliveries kill trust."
> "Your next supplier should speak fluent paperwork. Export docs. Compliance certs. Customs red tape."

The pattern: name the failure the buyer is punished for (line stoppage, rejected lot, missed audit), then the proof you prevent it.

**Tricks most owners miss**

- Bid on what the buyer is trying to do, not only on your process name. A party business won by bidding on the event, not its activity ([r/Entrepreneur 1,725](https://www.reddit.com/r/Entrepreneur/comments/m0n5x6/if_you_live_in_a_boring_midsized_town_you_could/)); the industrial version is "replacement bushing for [machine]", "reshoring [part]" or "second source for [component]".
- Do not let a rep or a new agency replace a working manual setup wholesale. One advertiser lost thousands switching a strong manual campaign to an automated strategy on a rep's advice and took longer to recover ([r/PPC 107](https://www.reddit.com/r/PPC/comments/cjhjwa/anyone_else_just_about_had_it_with_google_reps/)); another saw CPC triple after an agency rebuilt the account around 3 keywords ([r/googleads 17](https://www.reddit.com/r/googleads/comments/1x0sy9m/help_please/)). Test changes as experiments.
- When sales says "the leads are fake", audit spend on search partners, Display, PMax and audience networks first ([r/sales 539](https://www.reddit.com/r/sales/comments/1rfa3bv/you_need_to_audit_your_marketing_department/)).
- Test Microsoft Ads once Google is profitable: import the Google campaigns, keep the same negatives, and judge on the same qualified-RFQ metric. Office and plant desktops run Edge with Bing by default unless IT changed it, so check your own share of Bing traffic in analytics before deciding.

## LinkedIn: coverage of named people at named accounts

LinkedIn is where you reach the buying committee by company, function and seniority. Only 11% of engineers use it as a routine research source (GlobalSpec 2026) and 1% want a LinkedIn DM as first contact, so it is for coverage and proof, not discovery.

**When to run it**

- One new customer is worth at least about $30,000 in gross profit over two years, the sales cycle is long, and the target market has enough companies to build audiences.
- Budget at least $1,000 to $3,000 a month for three months; below that, use organic founder posts and outbound instead.

**Mechanics that limit small industrial ABM**

- Matched Audiences need at least 300 matched members to serve; LinkedIn recommends company lists of 1,000+ organizations, and supplying company page URLs or websites improves matching (LinkedIn Help 2026). A list of 20 target plants cannot run as its own campaign. Options: pad with lookalike companies of the same type, target by company list plus function across a whole segment, or retarget website visitors.
- Mixed lists get over-served to the largest companies; split enterprise, mid-market and small into separate campaigns (coreyhaines31 ABM playbook, practitioner).
- Narrow audiences to roughly 65,000 to 95,000 people, start bids at about half LinkedIn's suggested CPC, and turn off Audience Expansion and the LinkedIn Audience Network ([r/b2bmarketing](https://www.reddit.com/r/b2bmarketing/comments/1rjyamu/i_spent_2000_on_reddit_ads_im_embarrassed/), practitioner). The `paid-ads` skill records a vendor finding of heavy invalid-click rates on the Audience Network.
- Cap frequency at about 3 impressions per person per week in priority accounts; one method is an engagement audience of accounts with 500+ impressions in 7 days used as an exclusion (coreyhaines31 ABM playbook, practitioner thresholds).

**What tends to work**

- **Native Lead Gen Forms before landing pages:** $193 vs $346 CPL in Metadata's 2025 data (observational). Compare qualified-lead rate and pipeline per dollar, not CPL, before choosing.
- **Document ads** had the lowest lead-gen CPL by format ($142 vs image $200, video $265, conversation $362; Metadata 2025). A spec guide, design guide or material selection chart fits this format naturally.
- **Thought Leader Ads:** promote a founder's or engineer's real post. LinkedIn's internal 2025 data shows up to 2.4x CTR versus other single-image ads. One seller ran thought-leader ads against 200 to 300 target companies at $3,000 a month for three months and claimed $6.4M in deals, attribution unclear; hooks named the ICP and its pain, and people who clicked "see more" were retargeted with the same post plus a link ([r/b2bmarketing 53](https://www.reddit.com/r/b2bmarketing/comments/1xm8g4i/we_spent_3000_a_month_and_got_over_64m_in_deals/)).
- **Cold-audience order:** ungated point of view on the problem, then a customer story with numbers, then the offer (drawing review, sample, plant visit).
- **Optimize toward qualified leads.** LinkedIn added Qualified Leads Optimization, Conversion Value Optimization, appointment booking in Lead Gen Forms and Conversion Lift tests in September 2025, plus Conversions API to send CRM outcomes. Send "qualified RFQ" back, not every form fill.
- **Open-pipeline acceleration:** run reach-objective ads with proof and case studies to accounts that already have an open quote, refreshed weekly. The goal is keeping you in front of the rest of the committee (coreyhaines31 ABM playbook, practitioner).

**Tricks most owners miss**

- Retarget validated LinkedIn clickers on Meta with a website audience of "URL contains utm_source=linkedin": LinkedIn-grade audience at Meta prices (coreyhaines31 ABM playbook, practitioner). Needs enough LinkedIn traffic to reach minimum audience sizes.
- Exclude existing customers, employees, competitors and irrelevant countries from prospecting.
- A retail buyer found a supplier through her personal Facebook feed ([r/b2bmarketing 46](https://www.reddit.com/r/b2bmarketing/comments/1rjq6nl/our_best_b2b_marketing_strategy_in_2026/)): buyers are people on every platform. Meta was the second-best inbound channel for one seller of $50k+ contracts when ads named specific problems ([r/b2bmarketing 39](https://www.reddit.com/r/b2bmarketing/comments/1q3qfnd/5214587_pipeline_generated_for_a_software_dev/)). Test Meta with retargeting and problem-led video before calling it irrelevant.
- Do not trust engagement you bought. $150 for six paid LinkedIn posts gave about 3,500 likes, 500 comments, 0 referral visits and 0 replies ([r/smallbusiness](https://www.reddit.com/r/smallbusiness/comments/1qfie00/buying_posts_on_linkedin_pages_just_opened_my/)).

## Read the results like an owner

```
cost per qualified RFQ = spend / qualified RFQs (from CRM)
cost per PO = spend / POs from the cohort, read over the full sales cycle
channel score at day 90 = (gross profit won + probability-weighted qualified pipeline - channel cost) / channel cost
```

Same closer across sources when comparing, because who closes moves cost per close: one test moved from $192 to $274 per close by closer alone, and a variant with 2.4x the opt-in cost had 4.4 to 6.3x the cost per close ([r/b2bmarketing 46](https://www.reddit.com/r/b2bmarketing/comments/1rjq6nl/our_best_b2b_marketing_strategy_in_2026/)). Cheap leads are often the expensive ones.
