# Google Business Profile audit (browser only)

Runs with a browser and the owner's answers. Dashboard access makes it faster but is not required. Source tags point to [sources.md](sources.md).

## Step 0: collect before judging

1. **Find every listing.** Search Google Maps, logged out, for: the business name, name variants and old names, the raw phone number, the street address, old addresses, and (dental, legal, medical) each practitioner's name. Record each Maps URL. More than one result for the same business = duplicate problem, fix first.
2. **Pick 3 money keywords** with the owner: the service that pays most, the most searched service, the most urgent one ("emergency plumber", "nail salon", "pizza delivery"). Not five variants of one word.
3. **Pull the competitor set.** Search each keyword in Maps from the business's own address. Record the top 3 organic results (skip "Sponsored"). For each: name, primary category (shown under the name), rating, review count, date of newest review, distance to the searcher.
4. **Get secondary categories.** They are not shown publicly. Use the free Pleper or GMB Everywhere browser tools, or ask the owner to export theirs. Operators report this whole competitor-category pass takes about 10 minutes (r/localseo, 147 upvotes, 2026).
5. **Note the time.** Rankings change near closing time. A screenshot taken at 10 p.m., when rivals show "Closed", proves nothing (r/GoogleMyBusiness, 2026).

## Pass/fail checklist

Severity: **C** = critical (fix this week), **H** = high, **M** = medium, **L** = low.

| # | Item | Pass rule | If it fails | Sev |
|---|---|---|---|---|
| 1 | Verified and live | No "Own this business?" link on the listing; owner sees no suspension banner | Verification steps in [suspensions-and-spam.md](suspensions-and-spam.md) | C |
| 2 | Duplicates | One listing per real location (practitioner listings allowed if independent, each with own phone) | Merge or remove: keep the listing with the most reviews (Google never moves reviews between listings) | C |
| 3 | Business name | Identical to signage, website header and legal or registered trade name | Remove added keywords and cities. Adding them only works safely after a real rebrand (see "Name" below) | C |
| 4 | Primary category | Passes "This business IS a ___" and is as specific as the category 2 of the top 3 rivals use for the money keyword | Switch to the most specific true category. One change, then wait 2 weeks | C |
| 5 | Secondary categories | Every true "IS a" category added (up to 9 secondary, 10 total in Nov 2026); none for side services; none irrelevant | Add missing true ones; delete wrong ones | H |
| 6 | Services | Every predefined Google service that matches is selected; each real service also added with a description; names match website page names word for word | Add them. Sterling Sky (2026) saw predefined services move rankings within 24 to 72 hours | H |
| 7 | Address vs service area | Storefront: address shown, permanent signage, staffed in posted hours, pin on the real entrance. Pure service-area business (SAB): address hidden, up to 20 named areas, roughly 2 hours' drive from base | Fix the mode. Never a virtual office, UPS box, PO box or unstaffed coworking desk | C |
| 8 | Service area on a pure storefront | None, unless you deliver or travel | Remove it. Auditors of 100+ profiles say it is a frequent finding (r/localseo, 2026; ranking effect unproven) | L |
| 9 | Regular hours | Match the door, the website, Yelp and Facebook | Correct everywhere the same day | H |
| 10 | Special hours | Set for every holiday and closure in the next 60 days | Use special hours, never edit regular hours for a one-day closure | H |
| 11 | More hours | Category hours set where offered (delivery, takeout, kitchen, senior hours, online service) | Add | M |
| 12 | 24/7 claim | Only if a person or answering service picks up 24/7 | Remove. Operators saw fake availability produce 1-star reviews twice (r/localseo, 2026) | H |
| 13 | Phone | Local number answered live during posted hours | If call tracking: tracking number as primary, main number as additional phone, main number on website and directories | H |
| 14 | Website link | Opens on mobile; points to the home page (single location) or that location's page (multi); tagged `?utm_source=google&utm_medium=organic&utm_campaign=gbp` | Fix link and tag. Lowercase UTMs only | H |
| 15 | Landing page match | Page title and H1 name the primary category service and city; page lists the same services as GBP | Rewrite the page headings and service list | H |
| 16 | Action links | Booking, menu, order and reservation links go to this location's own page; preferred provider chosen; each link tested end to end | Fix. Google requires location-specific action links (r/localseo, 2025) | H |
| 17 | Menu (food) | Structured menu with section, dish, description, price; preferred menu source set | Build it. If Google auto-extracted a menu from a photo or PDF, review it before publishing | H |
| 18 | Products | Top services or products listed with price, photo and link to their page (where the category allows) | Add top 5 to 10 | M |
| 19 | Description | Up to 750 characters: what you are, where, top services, proof (years, licenses), no URLs, phone numbers or promo language | Rewrite. Conversion asset, minimal ranking effect | L |
| 20 | Attributes | All true ones set: payments, accessibility, online booking, free estimates, identity | Add. Mostly filters, not rankings (WebFX, Sterling Sky via claude-seo) | L |
| 21 | Photos | Logo, cover, exterior with signage from the street, interior, team, real work; newest owner photo within 30 days; no stock | Add. Conversion and verification evidence, unproven for rank | M |
| 22 | Video | One short real walkthrough (outside sign, parking, entrance, inside, staff working) | Film on a phone, one day max to edit | L |
| 23 | Posts | At least one live post in the last 30 days for the current offer, event or season; no phone numbers, emails or handles in post text | Post with the built-in call or link button instead of typed contact details | L |
| 24 | Reviews | See [reviews.md](reviews.md): newest review 14 days old or less; owner reply on 90%+ of the last 20; every negative answered | Start the review system | C |
| 25 | Pending edits | No unreviewed "Google updates" or wrong data in Edit profile > Collected info | Reject wrong edits. Deleting a Collected info entry does not undo a live change: fix the live field too | H |
| 26 | Access | Primary owner is the business's own account (domain email ideally); agencies and consultants hold Manager, never Owner | Transfer ownership; remove ex-staff | H |
| 27 | Legacy features | No plans built on Q&A, chat or call history | Remove from task lists: chat and call history ended 31 July 2024; the Q&A API was discontinued 3 Nov 2025 and public Q&A is being phased out (claude-seo, 2026) | L |

**Scoring.** Count C fails first. Any C fail outranks every other recommendation. If you need one number: 2 points per item passed and optimized, 1 if present but weak, 0 if missing, normalized to 100. Bands: 90+ excellent, 75 to 89 good, 50 to 74 needs work, under 50 poor. Weight hours and service areas higher for trades, menu and photos higher for restaurants (adapted from claude-seo's 25-field score, MIT).

## Categories: the highest-leverage edit

- **Rule: category first, service second, webpage third.** A category says what the business is. Services say which jobs it does. The website proves both (deep research, 2026).
- **Specific beats generic.** "Air conditioning repair service" over "HVAC contractor" when AC repair is the money keyword (r/localseo, 2026). "Cosmetic dentist" over "Dentist" when that is the core. Across 1.8 million profiles, specific categories showed a 12.5% vs 9.2% top-10 rate (2026 analysis, correlation).
- **Fill the secondary slots.** Localo (2026, 16,098 profiles): 6 secondary categories ranked top 3 in 69.1% of checks vs 47.9% with none. Sterling Sky (Aug 2025) added "Landscape designer", "Landscape architect" and "Retaining wall supplier" to a landscaper and saw lifts for each query class. Google's own text still says "as few as necessary". Agent rule: add every category the business truly is; never one for an occasional service.
- **Junk removal case:** 3 extra categories plus 10 to 15 services per category, with a new site and blog, gained rankings within 45 days (r/localseo, 2026, bundled changes).
- **Re-check every 3 months.** Google adds categories, and anyone can suggest a category change on your listing (r/localseo, 2026).

## Name: the rule and the gray zone

- Keywords in the name still rank (top 3 in Whitespark's 2026 survey). That is why spammers do it and why you report them (see [suspensions-and-spam.md](suspensions-and-spam.md)).
- **Never add words only on Google.** Google requires the name to match real-world signage and branding, and big name edits can trigger re-verification.
- **The legitimate version, operators report:** register a trade name (DBA) such as "[Brand] Drain & Sewer" (filing $25 to $100, 1 to 3 weeks in the US), then change invoices, vehicle lettering, signage, cards, website footer and bank account, and only then the GBP name and citations. Keep the filing and photos for verification (r/localseo, 72 upvotes, 2026). A 17-upvote reply warns signage and vehicle changes cost far more than the filing. This is an owner decision with real rebrand cost. Present it, do not push it.
- **Rebrand order:** build the new name on a staging site, switch site, GBP and citations within the same few weeks. Announcing early on the live site with half the citations updated cost one client weeks of cleanup (r/localseo, 2026).

## Hours as a ranking input

- "Open at the time of search" ranked #5 for Maps in Whitespark 2026; Google says hours match businesses to "open now" queries.
- **Trick:** compare your hours with the top 3. Opening 7 a.m. when rivals open at 9 gives two hours where you are one of few open options (r/localseo audits of 100+ profiles, 2026). Only extend hours you staff.
- Trades: after-hours emergency searches at 9 p.m. go to whoever shows "Open". If an answering service or AI receptionist truly covers it, list the hours (r/localseo, 2026).

## Photos, posts and videos: what the evidence says

| Activity | Measured evidence | Operator reports | Agent rule |
|---|---|---|---|
| Photo uploads | Sterling Sky (pre-2024, possibly outdated): no measurable rank lift across 4 businesses. WebFX: some vs none may help, more does not. EXIF geotags: no effect | Tire shop: 50+ real photos plus video in batches, grid average 20+ to 6.6 in 90 days, calls 96 to 401 a month, bundled with other work (r/localseo, 2026) | Upload real photos for conversion and verification evidence. Never sell geotagging or "7 photos a week for rankings" |
| Posts | Sterling Sky (pre-2024): no rank effect across 441 keywords per location. Posts can trigger "post justifications" in the pack | Calls rose in weeks posts went live (r/GoogleMyBusiness, 2026, 3 upvotes) | One post a week for offers, events and seasons. Merchandising, not ranking fuel |
| Videos | None | Walkthrough video plus 20 to 30 photos is called "the highest-return few hours" (r/localseo, 2026, impact not isolated) | One real walkthrough is enough |

Per-post view counts (Search plus Maps, 18 months, no API) returned in Sept 2026 per r/GoogleMyBusiness: use them to compare Offer vs Update vs Event posts, not as sales.

## Change discipline

- One sensitive change at a time: never name, address and category together.
- Before any name or address edit, build the evidence pack in [suspensions-and-spam.md](suspensions-and-spam.md).
- Log every change with date. Run a geogrid before and 14 days after ([rankings-and-geogrid.md](rankings-and-geogrid.md)). Without a log you cannot tell what worked.
- Monthly 2-minute check: search the business name plus city and confirm phone, hours, name, category and "Open" status. Operators report about half of the profiles they check show wrong data (r/GoogleMyBusiness, 38 upvotes, 2026).
