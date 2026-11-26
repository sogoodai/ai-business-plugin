# TikTok and the smaller channels

Rule for every channel here: compute its learning budget before launching. If the platform's own minimum does not fit the owner's budget, skip the channel; a "small test" below the floor produces noise.

## TikTok Ads (Smart+, Spark, lead gen)

**Platform rules** ([TikTok Smart+ best practices, Apr 2025](https://ads.tiktok.com/resources/help/article/best-practices-for-smart-plus-web-campaigns); [learning phase, Jun 2026](https://ads.tiktok.com/resources/help/article/learning-phase)):

- At least 6 creative assets per Smart+ campaign.
- At least 7 days of stable delivery with no disruptive edits.
- Daily budget at least 10x historical CPA; 30x preferred with target CPA or minimum ROAS. Base the target CPA on comparable max-delivery campaigns.
- After day 7: bid edits no more than 15% every 2 days. If the campaign spends 90%+ of its daily budget, try budget increases of up to 30%.
- Volatility generally declines after about 25 results or 7 days.

**What that means:** $50/day with a $30 CPA cannot meet 10x CPA ($300/day); Smart+ is structurally underfunded there. $500/day at a $40 CPA fits. Below the floor, run a manual campaign with 1 ad group and broad targeting, or use TikTok organically to find winners and spend on Meta.

**Creative:**

- Native beats polished: transformations, tutorials, behind the scenes, creator-style talking heads ([TikTok salon guide](https://ads.tiktok.com/business/en/guides/salon-advertising-marketing-guide)). Captions on, first line spoken in the first 1.5 seconds and on screen in 5 to 8 words.
- Test new hooks every 3 to 5 days; do not run the same creative past 7 to 14 days (indranilbanerjee, MIT, unsourced).
- Slideshow hook formula reported to repeatedly reach 50k+ views: someone doubts it, you show them, they change their mind ("my landlord said i can't change anything so i showed her what ai thinks it could look like": 234k views). Secondhand, unverified.
- Ad text 80 characters recommended, 100 max.

**Spark Ads** keep the original post identity and attribute paid views, likes, comments, shares and follows to the post ([TikTok, Jun 2026](https://ads.tiktok.com/resources/help/article/spark-ads)). Default test when an organic or creator post already shows resonance. Authorization codes last 7, 30 or 60 days. Pass `ttclid` server-side through the Events API with a shared `event_id`.

**Placements and fraud:** turn Pangle off, and "triple check it's turned off" (vendor-authored r/FacebookAds thread). In one $1,800 three-channel test, TikTok had 10% invalid sessions vs Meta 92% and Google 1%, and produced 45 sales at $13.33 vs Google 19 at $31.58 and Meta 0 on $600 each (r/FacebookAds 90, single test, event unstated).

**Lead generation objective:** several ad groups, budgets funded to learn, CRM sync ([TikTok](https://ads.tiktok.com/resources/help/article/lead-generation-objective)).

**Local:** US Local Feed from 11 February 2026; Nearby Feed in FR, DE, IT and UK from late 2025. Location cues in the video matter for restaurants and services. A cocktail bar's Spark Ads case: 1.5M views, 700+ bookings at GBP 1.83 per booking (TikTok case study, vendor).

**Policy:** country by country. Example: French prescription-medicine ads are not allowed; some OTC medicines and devices may be with certification and 18+ targeting ([TikTok policy, Oct 2026](https://ads.tiktok.com/resources/help/article/tiktok-ads-policy-other-products-and-services)). Gate on vertical x country x platform before building.

## TikTok Shop and GMV Max

- GMV Max has been the default and only TikTok Shop ads type since July 2025. Product GMV Max attributes all paid and organic orders of promoted products while it runs, even with no ad exposure ([TikTok](https://ads.tiktok.com/help/article/about-attribution-for-gmv-max)). Report it beside a blended or pause-period view; never call it incremental ROAS.
- Feed it an affiliate video library: one seller spent $1,871 in 7 days for 660 orders and $11,255 attributed sales, about 6x (r/TikTokshop 51, attributed, no profit data).
- Settings reported by one seller: Smart Promotion off, GMV Max on, ROI target 20; exclude the video that eats the budget each week so delivery moves to new videos (7 upvotes, uncorroborated).
- Keep a small affiliate commission even on flat-fee creator deals so their videos stay usable in GMV Max.
- Depth (samples, commissions, creator rules): `ecommerce-brand` (tiktok-shop.md).

## Pinterest

- Performance+ wants 50+ conversion events a week, daily budget 5x target CPA, 10+ ads per ad group, about 2 weeks of learning; no more than 2 rounds of changes a week ([Pinterest](https://help.pinterest.com/en/business/article/pinterest-performance-plus)).
- A/B tests need about $825 to $18,000 per test version in the Americas and 14+ days ([Pinterest](https://help.pinterest.com/en/business/article/create-and-manage-ab-tests)). A $100 split test is not a test.
- Fit: products and visually planned services (home, wedding, food, fashion, DIY). Below the conversion floor, optimize for a higher-volume event or skip.
- Scale 20 to 30% at a time.

## Reddit

- Default web attribution: 28-day click + 1-day view; ad groups can overspend the daily budget by 20% ([Reddit](https://business.reddithelp.com/s/article/Web-Attribution-Overview)). Its reported ROAS overlaps other channels heavily.
- Click quality varies: GA4 counted 1 session per 4 to 5 Reddit clicks for one advertiser; $75 bought 10 clicks, 1 tracked visit, 0 leads for another (r/DigitalMarketing 68, r/PPC 35). A vendor claims 80%+ bot or instant-bounce traffic; a practitioner calls Reddit retargeting "one of the highest ROI" with very low CPCs. Measure sessions per click in your own analytics before scaling.
- Cheap clicks with no revenue usually mean an unclear offer: $1,000 bought 5,000 clicks at a best CPC of $0.14 and zero revenue; the fix was offer clarity and ad-to-page match (r/Entrepreneur 265).
- App campaigns: 50x CPI daily for installs, 5x CPA for app events, 1 to 2 weeks of learning.
- Fit: niche hobbies, B2B software, products people research in subreddits. Ads should read like a post from the community.

## Nextdoor

- From $5/day ([Nextdoor](https://business.nextdoor.com/en-us/local/advertise-with-nextdoor-hg-geo)).
- 2024 creative study (platform observational): location-specific copy +17% CTR, real imagery +10%, under 25% text on the image +10%, ads without logos +22%.
- Fit: neighborhood services (cleaning, landscaping, handyman, pet care, pest), visual and recurring services. Claims about higher close rates are vendor marketing.
- Copy pattern: "[Service] for [neighborhood] neighbors" with a real photo of your crew on a local street.

## Microsoft Advertising

See [google.md](google.md#microsoft-advertising): import proven Google Search, constrain budget, verify UET.

## LinkedIn

- Expensive; skip under about $1,000 a month (zubair-trabzada, MIT, unsourced). Meaningful for B2B with high contract values only.
- Exclude the LinkedIn Audience Network: a click-fraud vendor reported 61% invalid clicks, 97% of it on the Audience Network (r/marketing 614, vendor).
- ABM at scale: 100 target accounts, logos and competitors pulled automatically, 100 custom ads in an hour; reported 5 to 6% CTR against a 0.4% benchmark (r/DigitalMarketing 62).
- LinkedIn + Snapchat on the same B2B buyers gave about 25% higher CVR on both (r/PPC 166, one practitioner).
- Warm a prospect list before cold outreach: upload it to Meta and Google, run awareness ads for about 2 weeks, then email or call; open rates rose (r/DigitalMarketing 128, 77 upvotes).

## Native (Taboola, Outbrain)

- Finance and health: CPA up to 25% below Google and Meta on some accounts (r/PPC 166), but others report poor conversion and bounce. Validate mobile numbers on forms; the first 150 to 200 words of an advertorial must name the buyer, the problem and the outcome.

## ChatGPT ads (2026, early)

- Equal-budget angle test on the same page, $500 over 3 weeks: "Replace the Marketing Stack" 2.16% CTR, $3.23 CPC, 6 conversions; "Vibe Marketing at Speed" 1.31% CTR, 4 conversions; "Skip the Tag Manager" 0.43% CTR, 0 (r/PPC 78).
- Use daily, not lifetime, budgets (lifetime pacing was poor, no scheduling at week 3). An education advertiser saw CPL similar to Google across 2 accounts.
- Reporting cannot tell you where to add negatives; do not scale on 1 to 2 conversions. A chatbot on the landing page improved conversion for one advertiser.

## Amazon, Etsy, eBay (marketplace ads)

Owned by `ecommerce-brand` (amazon.md, etsy.md). The rules a generic operator must know:

- **Amazon:** off-Amazon placements are on by default; limit them in campaign settings or in bulk (best seen 70% ACoS). Isolate keywords so each campaign's placement modifier matches that keyword's top-of-search vs other CVR (top of search 10 to 11% vs 6 to 7% implies about +40%, but a keyword converting 2x needs +100%). Store Spotlight on vague keywords with the headline "What type of [keyword] do you need?" and tiles mirroring Amazon's own refinement buttons lifted CTR from 0.6% to 2.2% (r/FulfillmentByAmazon 125). Do not raise bids when search-term impression share is above about 80%. Pause ads when stock or delivery dates slip; one seller spent $300 in a day at zero sales during an FBA transfer.
- **Etsy:** Offsite Ads fee 15% under $10k trailing-year revenue (opt-out allowed), 12% and mandatory above, 30-day click window, $100 cap per order; price every SKU for the attributed case. Etsy Ads about $1/day per 3 listings, judge after 30+ days.
- **eBay Promoted Listings:** any order within 30 days of a click is chargeable; one seller paid $1,300 at a 10% rate for $12,300 of sales (2021).

## Yelp and lead marketplaces

- Yelp ads drift after setup: removed keywords came back, the radius reset to 15 miles and the productive category was removed, burning $300 of credit plus $165 in 16 days (r/smallbusiness 476). Re-audit weekly for the first month.
- Lead marketplaces (Angi, Thumbtack, Bark, Houzz, Porch): one at a time, 20 to 30 lead sample, kill on gross-profit CAC, mark shared vs exclusive leads. Details: `home-services`.

## Offline media as ad creative

- Test billboard ideas on Meta at $5/day first (r/marketing 604). Billboard copy: 2 to 3 words readable in 3 seconds ("No. 1 in 90210", "500 Homes Sold").
- Direct mail suits long, high-ticket buying cycles: one home-services firm mailed 10,000 pieces a month for 3 years and customers kept coupons up to 18 months; 10,000 HVAC door hangers reached 4.5% response by day 60 at a $67 CPA vs $140 on concurrent Google Ads (Think Flyers 2025, seller case).
