---
name: indie-games
description: Market indie games for solo developers and small studios on Steam, mobile and itch.io. Use for Steam pages, wishlists, Next Fest, demos, festivals, trailers, streamer outreach, pricing, discounts, launch plans and mobile acquisition economics.
---

# Indie games: build intent, then spend it in one window

Built from 277 practitioner tactics in 118 threads (r/gamemarketing, r/gamedev, r/IndieDev, r/Unity3D, r/godot, r/indiegames) out of 1,889 scraped posts, a November 2026 research pass (Steamworks documentation, How To Market A Game, GameDiscoverCo, Voyer Law publishing report, Adjust, GameAnalytics, AppsFlyer, Apple, Google Play, Microsoft, Kickstarter, creator agencies) and the public game-marketing skill packs (coreyhaines31 marketingskills, MIT). "Operators report" marks a Reddit number with its thread upvotes; everything else carries its source and year. Sources: [references/sources.md](references/sources.md). The developer's decisions win over this guide.

## How indie games actually sell

- **Steam rewards purchases and play, not traffic.** Valve says page visits, wishlist count and page conversion are not direct visibility signals; sales and playtime are ([Steamworks visibility, 2026](https://partner.steamgames.com/doc/marketing/visibility)). Wishlists matter because they trigger launch and 20%+ discount emails, feed the Personal Calendar and predict week one.
- **Launch week is one coordinated spike.** Discovery Queue supplied 32 to 54% of launch traffic in a 75-game sample; median DQ impressions ran from about 21k (games under $30k lifetime) to 664,835 ($1M+) (HTMAG, Feb 2025). Concentrate creators, wishlist mail, discount, community and ads into the same days.
- **Growth is lumpy and concentrated.** Among about 1,200 unreleased demo games, the top 10% took 74% of new followers in a week; the median game had 12 followers and 85% had under 100 (operators report, r/gamemarketing 339, Nov 2026). Most wishlists arrive in 2 to 5 spikes: reveal, a creator video, a festival, the demo, Next Fest.
- **The hook is the marketing.** Every breakout in the data had a premise readable in one to three seconds: "platformer where you are the bad guy" (17,445 upvotes), "8-player pong, the arena shrinks and the dead come back as saboteurs" (7,603), three blind, deaf and mute monkeys defusing a bomb (70k wishlists before Next Fest). If the clip needs explaining, fix the clip or the game before buying reach.
- **Creators and trailer channels beat owned social for most games.** One 180k-subscriber genre creator moved more wishlists than dozens of small ones (r/gamemarketing 44); 5% of coverage drove about 80% of impact in a 1,000-creator campaign (r/gamemarketing 37). IGN's GameTrailers channel took one email and produced about 2,300 wishlists (r/gamemarketing 38).
- **Wishlists are inflating.** First-month units per launch wishlist in 2023 to 2025 were roughly half the 2020 to 2022 level (HTMAG, Oct 2026, 160 games). Median week-one sales are about 0.15x launch wishlists for games over 25k, with a 10 to 20x spread (GameDiscoverCo, 2024 to 2025 data).
- **Mobile is the opposite game.** Retention and LTV first, paid UA second. Premium Steam logic (wishlists, festivals) does not transfer.

## First session: ask, then compute

Ask the developer:

1. Platform(s), engine, genre and two or three comparable games ("X meets Y"), price, solo or team, country (tax treaty, VAT).
2. Steam page live? Date, current wishlists, followers, daily wishlist baseline (last 28 days), demo or playtest status.
3. Steamworks access: UTM link stats, traffic breakdown, wishlist report by country, demo players and median playtime.
4. Target release date and whether it is fixed; which Next Fest (one per game, ever) they plan to use.
5. Budget in money and hours per week for marketing; any publisher offer or contract.
6. Assets: trailer(s), raw 60 fps footage, capsule variants, press kit, Discord, mailing list, social accounts and their numbers.
7. Past campaigns with spend and results (ads, creators, festivals, showcases).
8. AI use in the game or art (some creators and festivals refuse AI-assisted games).
9. What they will not do (paid creators, ads, discounts below a floor, Early Access).

Then compute ([references/economics.md](references/economics.md)):

```
daily wishlist baseline = median net wishlists/day over 28 days with no event
event lift = wishlists during event - baseline x event days
follower ratio = wishlists / Steam followers (about 10 is typical, operators report)
page conversion = wishlists / unique Steam visits (by UTM source)
demo conversion = players who played and wishlisted / demo players
non-player share = 1 - (played and wishlisted / total wishlists in the window)
launch forecast = launch wishlists x 0.05 (weak) / 0.15 (central) / 0.30 (strong)
net per sale = price x (1 - launch discount) x 0.70 Steam x (1 - refund rate) x (1 - tax/VAT share)
value per wishlist = net per sale x first-year conversion (use 0.10 to 0.20)
max cost per wishlist = value per wishlist x 0.5
publisher hurdle = 1 / developer share - 1   (67.9% share needs +47% sales to break even)
mobile: LTV(D180) / CPI by country x OS x creative, after store fees
```

Report the three biggest gaps in wishlists or money, not in percentages.

## Benchmarks to check first

| Metric | Typical | Strong | Source, year |
|---|---|---|---|
| Week-one sales / launch wishlists (25k+ WL) | 0.15x | 0.30x+ (spread 10 to 20x) | GameDiscoverCo, 2024 to 2025 |
| Next Fest demo player to wishlist | 16.33% median | 20% (p70); about 32% for breakouts (operators) | HTMAG, 2025; r/gamemarketing 19, 2026 |
| Next Fest wishlists added | 618 median | 1,490 (p70) | HTMAG, June 2024, 40 games |
| Next Fest gain entering with 1k to 10k WL | about 1,000 | 1,700+ (top 30%) | operators quoting HTMAG surveys, 2026 |
| Fest wishlists from people who never played the demo | 68 to 88% | | operators report, 2026 |
| Launch discount | 10 to 15% (Valve suggests) | 10 to 40% allowed, 7 to 14 days | Steamworks, 2026 |
| Paid cost per wishlist (Reddit ads) | $0.75 to $1.48 | $0.15 to $0.24 (agency case, vendor) | operators 2026; Trapster 2026 |
| Creator outreach: key activation / reply / coverage | 7% / 3% / 1.2% | 13.8% reply | operators report, 500 and 2,232 emails, 2026 |
| Steam refund rate | 10 to 15% | 22% China-heavy, 19.8% expectation mismatch | operators report, 2026 |
| Mobile gaming CPI | $0.56 global, $1.68 NA, $0.53 EU | | Adjust, 2025 data |
| Mobile retention D1 / D7 / D30 | 27 / 13 / 5% (Adjust); 22 / under 4 / 0.7% (GameAnalytics median) | top 1%: 64 to 68% D1, 13 to 15% D30 | Adjust and GameAnalytics, 2025 data |

Full tables with sample definitions: [references/benchmarks.md](references/benchmarks.md). No defensible public benchmark exists for console wishlist conversion, Epic or GOG sales, or itch.io conversion. Say so instead of inventing one.

## Decision rules, in order

1. **Hook test before anything else.** Post three 10 to 20 second raw clips to player-facing communities. If none earns comments like "where can I wishlist", fix the premise, camera or first minute. Ads and creators amplify a hook; they cannot create one.
2. **Steam page live as soon as one clip lands.** "Sir, We Have an Orc Problem" launched its page with concept-art capsules and editor screenshots and got 900 wishlists on day one (r/gamedev 2,332). Pages opened one month or two weeks before launch sold 30 and "barely any" copies (r/gamemarketing 47, 26). Target 6 to 12 months of Coming Soon for a first game; high converters averaged 214 days on Steam pre-launch vs 411 for under-converters (GameDiscoverCo, correlation).
3. **Instrument before spending.** Every link gets a Steamworks UTM (utm_source, utm_campaign, utm_content per post or creator). Visits without wishlists means a page problem; no visits means a traffic problem. Report wishlists, never views or upvotes.
4. **Page conversion under 10% of tracked visits or demo conversion under 12%:** fix capsule, first five tags, short description, trailer opening and the demo's first ten minutes before buying traffic.
5. **Demo:** release it ahead of Next Fest (11 days to months), patch from creator recordings, then enter Fest with a known conversion. Put a wishlist button on the main menu and the end screen.
6. **Next Fest only with momentum.** One per game, February, June and October. Submit the demo 2 weeks before (4 weeks for Press Preview, which opens 11 days before). Book creators to post during Fest days one and two.
7. **Festivals and showcases in between.** Use the HTMAG festival list; most do not need a demo. Prefer ones with Steam front-page capsules and a matching audience. Genre fests gave 500, 800, 3,000 and 8,500 wishlists in operator reports.
8. **Creators before ads.** 100 to 300 genre-matched creators, key in the first email, 20 to 50 personal pitches, one follow-up after 5 to 7 days, trailer to IGN/GameTrailers and Indie Games Hub. Paid creators only after free keys prove the game converts creator audiences.
9. **Ads only under the ceiling.** Compute max cost per wishlist; stop the day a channel runs above it. Never chase a Popular Upcoming threshold with ads.
10. **Release date:** a specific date at least 60 days ahead (Personal Calendar dedicated page; 3 weeks for front-page eligibility). Avoid seasonal sales, Next Fest week and big-showcase weeks. Inside two weeks, never slip more than 24 hours.
11. **Launch:** 10 to 15% discount, every channel in the first 72 hours, notification check with real wishlisters. Save the 20% wishlist-email discount for a later beat.
12. **After launch:** fix refund reasons first, then spend Update Visibility Rounds (five per game, shared by Early Access and 1.0) only on real updates paired with a discount and creator push.

## Steam mechanics an agent must know

- **Notifications:** wishlisters get email at launch and at 20%+ discounts on the lowest-priced package running 8+ hours. A 2024 bug sent no launch emails for Planet Centauri (138,675 wishlists, 581 units in five days; Steam offered a Daily Deal) (r/gamedev 5,783). On launch day ask five wishlisting friends if they got the email; if not, open a Steam support ticket the same day.
- **Popular Upcoming is no longer the goal.** The old 6,000 to 7,000 wishlist entry point is reported to have moved to about 80,000 after the 2026 home-page refresh, while the Personal Calendar matches upcoming games to players with similar playtime in the genre (operators report summarizing Indie Game Joe, 2026). Valve says there is no minimum wishlist threshold. Tags and a targeted first audience now decide who sees the game.
- **Artwork overrides:** schedule them 5 minutes before a discount starts so wishlist emails pick up the new art; localize them; run one month at most.
- **Discount rules:** 30 days between custom discounts (seasonal sales excepted); launch discount 10 to 40% for 7 to 14 days.
- **2026 release checklist:** at least five minutes of recent Steam-launched playtime before build review and at least five screenshots tagged as gameplay.
- **Free to Play hub:** set the main genre to "Free to Play" for free games; a developer whose free games fund the paid one made 85% of $100k from the paid title (r/IndieDev 3,877).

More: [references/steam-mechanics.md](references/steam-mechanics.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| 7,000 wishlists = visibility | Hit 7k for Popular Upcoming | Valve: no threshold; PU now reported near 80k | Chase qualified wishlists and tags, not a number |
| Wishlist conversion | 20 to 25% (old HTMAG) | 0.15x median, halved since 2023 | Forecast at 0.05 / 0.15 / 0.30 |
| Release-date notice | 5 weeks keeps hype (Eastshade, 2019) | Personal Calendar needs 60 days | Set the exact date 60+ days out |
| Action-first trailer | Open on the most intense action | A $10 YouTube test showed an action-first cut dropping at 5 to 6 s vs a loop-first cut | Open on the core loop or fantasy, test retention |
| Ad wishlists are weak | Organic wishlists convert better | 25% of 150k launch wishlists came from Reddit ads and the launch sold 9,585 in 4 days | Judge by source cohort, not origin |
| Next Fest from zero | "Enter anyway" | Fest magnifies existing momentum; top-10% growth threshold fell 26% from Feb 2024 to Feb 2025 | Enter with a tested demo and booked creators |
| Low price sells | $3 to $5 for simple games | Chris Zukowski argues indies underprice | Price to comparables and hours; test with the wishlist cohort |

## Never

- Never review your own game, even as a disclosed joke: a developer got a Steam warning (r/IndieDev 8,084). Never offer anything for reviews.
- Never send bulk keys to showcases or "curators" you have not verified; check gg.deals and Kinguin after any key drop and revoke leaked keys.
- Never show a non-playable camera, mode or feature in a trailer as if it were the game.
- Never put "probably a flop" or self-deprecation in a launch title (659-upvote warning).
- Never burn an Update Visibility Round on a patch.
- Never sign a publisher deal without a written minimum marketing commitment, territory limits and audit rights.
- Never run paid creators or ads on cost per view; judge on tracked wishlists and sales.
- Never scale mobile UA before D1/D7/D30 clear your own genre and geo band.
- Never invent a benchmark, a quote or a review.

## Before you write any message

Use [references/scripts.md](references/scripts.md): creator and streamer pitch, IGN/GameTrailers premiere email and follow-up, press pitch, snowball pitch, Reddit post titles, short description template, Instagram Reel format, Steam review replies, Discord review ask, price-objection reply, publisher diligence questions, live-stream ask.

## References

- [benchmarks.md](references/benchmarks.md): Steam, festival, creator, ads, refund, publisher, Kickstarter and mobile numbers with source, year and sample.
- [economics.md](references/economics.md): wishlist value, cost-per-wishlist ceiling, revenue waterfall ($560k gross to $73k take-home), forecasts, publisher hurdle.
- [steam-mechanics.md](references/steam-mechanics.md): wishlists, notifications, Next Fest, festivals, Personal Calendar, DQ, visibility rounds, discounts, keys, reviews, refunds.
- [store-page-trailer-demo.md](references/store-page-trailer-demo.md): capsule, tags, descriptions, screenshots, WebM, trailer structure and tests, demo design and instrumentation.
- [creators-and-press.md](references/creators-and-press.md): creator list building, outreach maths, trailer channels, snowballing, China and Japan, paid creator platforms, key safety.
- [social-and-communities.md](references/social-and-communities.md): short-form clip primitives, platform splits, Reddit, X, Facebook groups, Discord, devlogs, stunts.
- [paid-ads.md](references/paid-ads.md): Reddit and other ads for wishlists, trailer tests, geos, credits, kill rules.
- [pricing-and-launch.md](references/pricing-and-launch.md): price, launch discount, date selection, Early Access, sales cadence, post-launch.
- [publishers-and-funding.md](references/publishers-and-funding.md): publisher deal terms and red flags, Kickstarter, grants, console.
- [mobile-itch-console.md](references/mobile-itch-console.md): mobile soft launch, CPI, store tests, clones; itch.io; Xbox, PlayStation, Switch.
- [scripts.md](references/scripts.md): exact wording for every recurring message.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [by-niche.md](references/by-niche.md): roguelikes, co-op, cozy and sims, horror, visual novels, strategy, adult, kids mobile, tools and assets.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan for a new, pre-launch or stalled game.
- Sibling skills: `organic-social` for platform mechanics, Trial Reels and cadence; `paid-ads` for account setup, Reddit attribution and creative testing; `creator` when the client is a gaming YouTuber or streamer; `offers-pricing` and `email-sms-loyalty` for pricing psychology and mailing lists.
