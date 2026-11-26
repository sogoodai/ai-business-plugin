# Paid ads for games

Account setup, bidding, pixels and Reddit attribution defaults live in `paid-ads`. This file covers buying wishlists and installs.

## When ads make sense

- Only after organic clips show the hook lands and the page converts tracked visits at a healthy rate. Ads multiply page conversion; a weak page burns budget.
- Only under the max cost per wishlist from [economics.md](economics.md). Typical ceilings for $10 to $20 games come out at $0.40 to $1.00.
- Steam does not reward traffic. Ads pay only through the wishlists and sales they create.

## Reddit ads (the main paid wishlist channel for PC indies)

Operator results, 2026:

| Campaign | Spend | Result | CPW | Thread |
|---|---|---|---|---|
| Visual novel, chasing 7k WL | $3,700 | 2,500 WL | $1.48 | r/gamedev 924 |
| Post-page-launch test with match credit | $3,002 ($1,502 out of pocket) | 657,199 impressions, 14,723 clicks, $0.20 CPC, 2.24% CTR, 2,382 WL | $1.26 | r/gamemarketing 83 |
| Simple post-style ad, comments enabled | $150 | 200 WL | $0.75 | r/gamemarketing 72 |
| Sim, self-managed, US and Europe | not disclosed | 25% of 150,000 launch WL | n/a | r/gamedev 823 |

Tricks:
- **Credits:** Reddit has offered spend-matched credits (spend $500, get $500; another offer matched $1,500). One offer had to be claimed within 30 days of signup and spent within 30 days of claiming; a developer who opened the account five weeks before launch missed it (r/gamemarketing 36). Open the account when you are ready to spend, and read the current offer terms.
- **Start in one region** (US and Canada) to cut variables, then add translated-page geos. Asian impressions were much cheaper but converted so poorly the ad group was cut; Western Europe settled near US levels (r/gamemarketing 83).
- **Check delivery on day two.** A US campaign with a EUR 0.40 cost cap showed 8 impressions and no clicks while the EU lowest-cost twin paid about EUR 0.30 per click (r/gamemarketing 36). Start on lowest cost.
- **Target by thinking style, not just comparable games.** Direct-comparison subs were small; theorycrafting subs like r/PathOfExileBuilds gave scale (r/gamemarketing 36). Research about 30 subreddits.
- **Hold the video constant; vary 4 headlines x 4 thumbnails** across subreddit groups (r/gamemarketing 83).
- **Comments on:** one developer kept comments enabled and ran the ad at minimum budget while it kept producing wishlists (r/gamemarketing 72).
- **Ad wishlists are not automatically weak.** The 150k-wishlist launch with 25% from ads still sold 9,585 in four days; the developer argues audience fit and the expectations you set matter more than the source. Track refunds by source where possible: that launch's 19.8% refund rate came from expectation gaps.
- Reddit reports 28-day click and 1-day view by default; compare against Steamworks UTM wishlists, not Reddit conversions (see `paid-ads`).

## Other channels

- **X and Reddit small tests** to compare wishlist conversion: paid was 5 to 6% of 10,000 wishlists in 21 days for one launch (r/gamemarketing 76).
- **VK:** $530 for 800 wishlists ($0.65), audience exhausted fast (r/gamedev 924).
- **Paid community channel posts:** $340 for about 100 wishlists ($3.40). Ask niche community channels for free posts or a small donation first (r/gamedev 924).
- **Meta and Reddit for Kickstarter followers:** see [publishers-and-funding.md](publishers-and-funding.md).
- **Paid showcases:** $200 for a Best Indie Games slot was "not worth it" (r/gamedev 2,332). Treat any paid showcase as a test with a UTM.
- **Stream overlays** (Word On The Block, CPM, no minimum): no measured results.
- **TikTok creator agencies:** see [creators-and-press.md](creators-and-press.md).

## Ads as a trailer and capsule lab

- **Trailer retention test:** $5 to $10 of YouTube ads per cut, compare retention curves, stop near 1,000 views (r/gamemarketing 83).
- **Capsule test:** two image-only ad cells, same audience and copy; CTR screens, Steam UTM visit-to-wishlist decides.
- **Mobile store pages:** use Google Play store listing experiments and Apple custom product pages instead of guessing (see [mobile-itch-console.md](mobile-itch-console.md)).

## Mobile UA

- Do not scale before retention works in the target genre and geography. 2025 CPIs: $0.56 global, $1.68 North America, $0.53 Europe; action $0.24 to slots $4.47 (Adjust, vendor).
- Keep a cohort matrix: country x OS x network x creative x objective x install date x D1/D7/D30 x payer rate x ARPDAU x ROAS.
- Put 60 to 80% of spend on the one or two proven angles and keep the rest for tests (research operating rule, 2026).
- Kill creatives with poor downstream retention even if CPI is cheap. Match each creative angle to a store page that opens on the same fantasy.

## Kill and keep rules

- Stop any channel above max CPW for two consecutive weeks.
- Stop a trailer test once retention curves separate (about 1,000 views).
- Stop paid creators whose tracked wishlists cost more than ads.
- Stop chasing a placement threshold (Popular Upcoming) with spend. It has moved and was never guaranteed.
- Keep a "stop-doing" ledger beside the calendar with each channel's exit criterion written before launch.
