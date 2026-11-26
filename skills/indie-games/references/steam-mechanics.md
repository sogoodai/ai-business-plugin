# Steam mechanics

Current Steamworks documentation (2026) unless marked. Valve changes these often: re-read the linked page before quoting a rule to the developer.

## What Steam actually rewards

- **Strong signals:** purchases and players. **Not signals:** page traffic, page conversion, raw wishlist count (outside wishlist-specific surfaces) ([Visibility on Steam](https://partner.steamgames.com/doc/marketing/visibility)).
- **Review score** has little effect above 40% positive; Mostly Negative cuts featuring. Below 10 user reviews the store shows no score summary, which is why operators chase the first 10 (r/gamemarketing 16). Get them from existing community, not incentives.
- **Language:** supported languages count for recommendation relevance. A localized page and game reach players a non-localized one cannot.
- **Implication:** model the funnel as discovery, qualified visit, wishlist or demo, notification, purchase and play, then Steam amplification. Sending cheap clicks "for the algorithm" buys nothing.

## Wishlists and notifications

- Wishlisters get an email at launch (and Early Access launch) and when a discount of 20% or more on the lowest-priced package runs 8+ hours ([Wishlists](https://partner.steamgames.com/doc/marketing/wishlist)).
- **Demo notification button:** when the demo goes live you can notify wishlisters. One developer at about 6,450 wishlists used it and got +2,542 net wishlists and 520 peak players in 38 hours (r/gamemarketing 72). Commenters warned of a cooldown between notifications; nobody had a reliable interval, so do not schedule a demo notification within weeks of launch without checking the current Steamworks text.
- **Failed notifications happen.** Planet Centauri launched to 138,675 wishlists and sold 581 in five days; Steam confirmed a bug that skipped launch emails for under 100 releases since 2015 and offered a Daily Deal (r/gamedev 5,783). Another developer at 2,000 wishlists found no friend had received the email (r/gamemarketing 72). Launch-day check: five real wishlisters confirm the email; if not, file a Steamworks support ticket immediately and ask for a remedy (one studio reportedly got 24 hours of front-page placement).
- **Steam search becomes a traffic source within days of a reveal:** TOWERPUNK's Steam search traffic equaled all external links combined (r/gamemarketing 56). Test the name: "Journey to the Void" forced players to type almost the full title past other "Journey to the" games (r/IndieDev 5,796). Pick a name that is the top result after 4 to 6 typed characters.

## Personal Calendar and Popular Upcoming (2025 to 2026 change)

- Personal Calendar started as a Steam Labs experiment in October 2025 and sits at the top of the refreshed 2026 home page. It recommends upcoming releases using similar players' playtime and wishlists ([Personal Calendar](https://partner.steamgames.com/doc/marketing/visibility/personalcalendar)).
- Eligibility: a specific release date set at least 60 days ahead for the dedicated calendar page, at least 3 weeks ahead for the front page. Inside two weeks of launch, a delay of more than 24 hours removes the game from calendar recommendations until release.
- Operators report games with about 7,000 wishlists receiving 1,000 to 1,300 wishlists a day from calendar impressions after the change, and one developer credits the calendar with growing from about 700 to 22,000 wishlists (r/gamemarketing 26, 48). Treat as reported.
- Popular Upcoming became algorithmic and moved down the home page; the reported entry point went from 6,000 to 7,000 wishlists to about 80,000 (r/gamemarketing 26, summarizing Indie Game Joe, 2026). The "get 7k and release" plan is dead.
- What now matters: accurate tags (Valve added 17 and removed 28 tags shortly before the refresh, per the same summary), and making the first few hundred wishlists come from the exact target audience, because similarity matching starts from them.

## Next Fest

- Three a year: February, June, October. **One per game, ever** ([Next Fest](https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest)).
- Demo must be public when Fest starts. Submit for review 2 weeks before, 4 weeks if you want Press Preview, which starts 11 days before the event.
- Missed registration: one developer explained to Valve that the demo was ready and the Fest mattered for a launch two weeks later, and got an invitation (r/gamemarketing 18). An exception, not a plan.
- Release the demo earlier than Fest: 11 days early gave time to fix bugs and retention issues (r/gamemarketing 72); "months before" allowed balance changes from creator recordings and a 23% Fest conversion (r/gamemarketing 19).
- Front-load: book creators to publish on days one and two. One game's daily demo players still peaked on day 6 (172, 129, 174, 200, 198, 231, 176), so keep posting through the week.
- Screenshot the Next Fest recap report immediately; it is temporary.
- Next Fest magnifies momentum. BOMBANANA opened its page 25 days before Fest, entered with 70,000 wishlists from creator and press work, and left with 230,000 as the most played demo (r/gamemarketing 145). ZOMBUTCHER entered small and still doubled its total (r/gamemarketing 96). Do not launch the full game during Next Fest week.

## Other festivals and showcases

- Find them on the HTMAG festival list (howtomarketagame.com/festivals). Most showcases do not require a demo (r/gamemarketing 350).
- Prefer events with Steam front-page capsules and a matching lineup (story-rich, women-led, turn-based, movement, detective, regional fests like the Ukrainian Games Festival or the Latin American Games Showcase).
- Steam removed event banners from the top of game pages in favor of personalized event recommendations, so joining many third-party events no longer guarantees page-top exposure.
- Announce something new at each: a trailer, a demo window, a playtest date. Midgardr revealed a new trailer and a demo window at TurnBasedThursday and got 3,000+ wishlists in a week without a demo (r/gamemarketing 22).
- Public playtests during festivals count: Superball had 100,000+ players in the 2021 festival (r/gamemarketing 63).
- Steam events can bring publishers: Dawnfolk's developer got inbound publisher interest from Steam events after cold outreach failed (r/godot 3,130).

## Discovery Queue and launch

- DQ supplied 32 to 54% of launch traffic in a 75-game sample (HTMAG, Feb 2025). It responds to early sales and play, so the first 72 hours matter.
- The 2026 home page plays micro-trailers and screenshot previews in discovery modules and shows larger capsules with neighbors' edges visible. Capsule art must survive cropping at the sides (r/gamemarketing 26).

## Discounts

- Launch discount: 10 to 40%, 7 to 14 days; Valve suggests 10 to 15% ([Discounting](https://partner.steamgames.com/doc/marketing/discounts)).
- 30 days between custom discounts; seasonal sales are the exception. A 20%+ discount triggers wishlist email, which is the only proven reason to go deeper.
- No evidence that a deeper launch discount buys algorithmic reach (GameDiscoverCo).
- Successful games commonly start discounting early: in 519 games with 3,000+ reviews, the first post-launch discount came after a median 48 days, usually 20%, and 78% had discounted within three months ([SteamSage, 2026](https://steamsage.io/blog/how-long-until-steam-games-go-on-sale), selected sample).
- **Artwork override trick:** schedule the override 5 minutes before the discount starts so the wishlist email shows the update art ([Overrides](https://partner.steamgames.com/doc/store/assets/overrides)).

## Update Visibility Rounds

Five per game, each up to 30 days or 1M home-page impressions, shared between Early Access and 1.0 ([Update rounds](https://partner.steamgames.com/doc/marketing/visibility/update_rounds)). Spend one only when all four are true: material new content or systems, an announcement post with new art, a creator pitch, and (if economics allow) a discount.

## Store page and build rules that block launches

- Capsules: logo or title readable at the smallest size; no review scores, awards, discount text or other copy on base capsules ([Asset rules](https://partner.steamgames.com/doc/store/assets/rules)).
- The demo banner overlays the capsule. A store page was rejected because the banner covered the title; another developer moved the title off-center (r/IndieDev 4,607, 305-upvote comment). Preview with the banner before submitting.
- 2026 release checklist: at least five minutes of recent Steam-launched playtime before build review, at least five screenshots tagged as gameplay (menu, concept and cinematic images are categorized separately).
- A Coming Soon page must be public at least two weeks before release; plan for months, not weeks.
- Optional AI features can get a build rejected: one game was retired over an optional ChatGPT feature, then reinstated without it (r/gamedev 3,074). Disclose AI content in the Steamworks content survey and keep a non-Steam audience (mailing list, Discord) so a store problem does not strand everyone.

## Reviews and the developer

- Never review your own game, even as a joke; a developer received a Steam warning (r/IndieDev 8,084).
- Do not argue playtime under a negative review. Crashed background processes can log hours without the game working (r/IndieDev 4,283, 104-upvote comment). Ask the reviewer how they got it running so you can fix it for others; that also invites a review update.
- Ask for a review at the moment you fix someone's bug or ship their suggestion in Discord (r/gamemarketing 57).
- Explain misunderstood mechanics in review replies; players will repeat the explanation (an anti-piracy pirate-customer event went viral in China, r/gamedev 1,317).

## Refunds

Steam refunds within 14 days of purchase and under 2 hours of playtime. Refund comments are the best product research you will get: Fantasy World Manager's 19.8% came from automated-sim expectations the marketing set, UI/UX, bugs and Early Access expectations (r/gamedev 823). Fix the expectation in trailer and page first; it is cheaper than code.

## Keys

- Steam keys for creators, press and curators are free. Track every key by recipient.
- Check gg.deals after any key drop; one developer found showcase-distributed beta keys on Kinguin, revoked them, and the listings went out of stock the next day (r/gamedev 1,158).
- Distrust bulk requests ("5 review keys plus 20 giveaway keys"); one requester came back for replacements after keys appeared on resale sites (r/gamemarketing 51).
- Free to Play: set the main genre to Free to Play to appear in the hub (r/IndieDev 3,877).
