# Rankings, geogrids and diagnosis

How the local pack decides, how to measure it from a browser, and how to read the result. Sources in [sources.md](sources.md).

## What moves the local pack

Google's stated model: **relevance, distance, prominence**. No weights are published.

| Evidence | What it says | Type |
|---|---|---|
| Whitespark Local Search Ranking Factors 2026 (published 6 Nov 2025, 47 experts) | Top Maps factors: primary category, searcher proximity, keywords in the business name, address in the searched city, open at time of search, rating, visible address vs hidden SAB, secondary categories, review count with text, pin placement, review recency. Spam listing removal #19. Group weights: GBP signals about 32%, reviews about 20% | Expert survey |
| Search Atlas, Aug 2025 (via claude-seo) | Machine-learning model of pack rank: proximity 55.2%, review count 19.2%, domain strength 5.9%, review text relevance 5.3%, everything else under 5% each | Correlation model |
| Localo 2026 (16,098 profiles, 131,000+ keywords) | Top-3 rate: 6 secondary categories 69.1% vs 47.9% with none; complete profile 72.6% vs 58.5% baseline; 201 to 500 reviews 73.0% vs 39.3% at 1 to 5 reviews | Correlation |
| Sterling Sky field tests 2025 to 2026 | Ranking step at about 10 reviews; fresh reviews help; valid niche categories lift their query class; predefined services moved rankings within 24 to 72 hours; posts and photos showed no rank effect (older tests, pre-2024) | Field experiments |

Read together: **distance and category decide who is eligible, reviews decide the order among the eligible.** Content churn (posts, photos, citations) sits far below.

Proximity strength varies by query: "coffee shop" is extremely local, "divorce lawyer" much less (localseoskills, MIT). A competitor with fewer reviews outranking you is usually closer to the searcher, in a more specific category, keyword-named, open when you are closed, or spam.

## Proximity levers (the only ones that move distance)

- **A real second location** where demand is. A junk removal client opened a staffed office about 30 miles away, picked for average competition and no tolls, with its own identity; it ranked within 45 days (r/localseo, 2026). A plumbing company opens shops where rivals neglect SEO and captures leads immediately (r/GoogleMyBusiness, 2025, secondhand).
- **A small office inside the highest-value area.** One operator estimates $500 to $700 a month in rent, paid back by 1 or 2 extra jobs (r/localseo, 2026, estimate only). Must be staffed, signed and genuinely used, or it becomes a suspension risk.
- **Address approval for a service-area business** that really receives customers: permanent signage and a staff-only area are the overlooked requirements. An agency called it one of the biggest contributors to a client's gains two months later (r/localseo, 2026). Another owner called switching from SAB to a physical location their single biggest improvement (r/GoogleMyBusiness, 2026). A Dec 2025 study of 8,186 businesses (attributed to Sterling Sky, unverified) linked hidden addresses to lower pack rank.
- **Never fake it:** virtual offices, UPS boxes, rented-by-the-hour rooms. One owner verified a Regus virtual office with occasional room bookings and a sign; suspended after the third video, putting $150,000 a month of ad spend at risk (r/GoogleMyBusiness, 2024).
- **Service areas do not move you.** Sterling Sky (Mar 2025): the verification address drives rank, not the service-area list. A service area is a display setting.

## Measure: geogrid from a browser

A single rank from the owner's phone is meaningless. Measure from many points.

**Method A, Maps viewport (no tools).** Open an incognito window, logged out. For each grid point, load `https://www.google.com/maps/search/[keyword]/@[lat],[lng],15z` and record the position of the business among organic results (skip "Sponsored"). Maps ranks by the map center at that zoom.

**Method B, Search with a spoofed location.** Chrome DevTools > More tools > Sensors > Location: set the latitude and longitude, reload `google.com/search?q=[keyword]` and read the 3-pack. Closer to what mobile searchers see.

**Method C, a geogrid tool or MCP** (Local Falcon starter about $25 a month covered 6 clients scanned once or twice monthly, r/localseo, 2026; BrightLocal; any local-rank-grid API you have). Always show the cost before running.

Keep the method, keyword, grid size, radius, device and time of day identical between scans. Never mix methods in one comparison.

**Grid points.** Center on the business pin (or the SAB's hidden address). `step = 2 x radius_km / (n - 1)`, `mid = (n - 1) / 2`. For row i and column j: `lat = c_lat + ((i - mid) x step) / 111.32`, `lng = c_lng + ((j - mid) x step) / (111.32 x cos(c_lat))` (claude-seo, MIT).

| Business | Grid | Radius |
|---|---|---|
| Cafe, salon, barber, shop in a dense city | 5x5 or 7x7 | 1 to 3 km |
| Dentist, plumber, city-wide service | 7x7 or 9x9 | 3 to 8 km |
| HVAC, roofing, regional trade, rural | 11x11 or 13x13 | 10 to 25 km |

A cafe scanned at 13x13 over 25 km looks terrible by design.

**Metrics.** ARP = average rank across all points (not found = 20). ATRP = average of the found positions only. SoLV = share of points in the top 3. State the definition in every report: some tools count "appears at all", Local Falcon counts top 3. Bands for top-3 SoLV (claude-seo, MIT): 80%+ dominant, 60 to 79 strong, 40 to 59 moderate, 20 to 39 weak, under 20 critical.

**Validate before reading.** Brand name search must be #1 at the center point. Discard a scan with fewer than about 30 results or results from the wrong country (DataForSEO user, r/localseo, 2026; trackers returned poisoned SERPs in late 2026). Cross-check sudden "disappearances" against Search Console average position and a manual search. Rescan after any major GBP edit or after 30 days.

## No geogrid at all: the town-by-town audit

For service-area businesses, search each service from inside each served town (ZIP centroid via Method A or B). Score each cell: pack #1 = 5, pack #2 to 3 = 4, organic positions 4 to 10 = 2, organic only below that = 1, absent = 0. Weight services 1 to 3 by value.

```
area_strength = sum(score x weight) / sum(5 x weight)
  0.70+ strong | 0.30 to 0.69 contested | under 0.30 weak
opportunity = (1 - area_strength) x area_value (1 to 3)
```

Attribute each weak cell to one cause, or write "unattributed": proximity (rival is closer), prominence (review gap such as 480 vs 130), relevance (rival has the exact category or a dedicated town page). Worked example (unifapi, MIT): an Austin HVAC firm scores 0.9 in Austin but 0.28 in Round Rock, where the leader has 480 reviews vs 130, the exact "Air conditioning repair service" category and a Round Rock page. Fix order: Round Rock review velocity, a real Round Rock page, category accuracy.

## Reading the pattern

| Pattern | Meaning | Action |
|---|---|---|
| Strong center, fades outward | Normal proximity | Build prominence (reviews, links) and relevance for the weak side |
| Weak in one direction | A rival owns that zone, or the area is not associated with you | Town page with real local proof, reviews from that area, citations there |
| Weak center, stronger edges | Pin, address or category problem | Check the pin on the real entrance, the category, duplicates near the address |
| Scattered, changes week to week | Volatility or rivals trading places | More data before acting |
| Good where found (low ATRP) but low SoLV | Area association problem | Pages and reviews for those areas |
| ATRP close to ARP and both poor | Relevance problem, not distance | Category, services, landing page match |
| Secondary keyword beats the money keyword | Category or site emphasis misaligned | Re-pick primary category |

**Translate for owners:** SoLV 14% means "86% of nearby people searching for your service don't see you on the map". ARP 6.5 means "when they see you, you're 6th or 7th, and most people look at 3".

## Diagnosis trees

**Not showing at all:** verified? suspended (check the dashboard banner)? hidden by a duplicate? primary category wrong? listing under about 6 months old (new listings often rank poorly)?

**Sudden drop:** in this order:
1. Any GBP edit in the last 2 weeks, including accepted "Google updates" or third-party suggested edits.
2. Address hidden or service area changed. One SAB owner removed her address and set the service area to the whole US; the grid placed her in the ocean and all rankings vanished, then returned the next day when the original verification address was restored (r/localseo, 2026, two changes at once).
3. Reviews lost or a review attack.
4. New competitor or spam listing in the pack.
5. Website change: new theme, noindex, lost service page, broken GBP link.
6. Aggregator pushing old data, or a known Google update.
7. Time of check: closing hour or competitors' hours.

**Outranked by a rival with far fewer reviews:** compare primary category, distance from the searcher, keyword in their name (check their signage on Street View), open hours at search time, their landing page. One "7 reviews beat 150" claim turned out to be checked at night when rivals showed closed and on near-zero search demand (r/GoogleMyBusiness, 2026).

## Website levers that move local rankings

- **GBP landing page alignment.** A dentist's grid score went from 5.66 to 2.68 after matching GBP service descriptions word for word with the website's landing pages and reusing the snippets as posts (r/localseo, 2025, bundled). A coffee shop: completeness 82% to 100%, categories refined, title tags and H1s aligned with GBP; Maps visibility 40% to 70% and top-3 36% to 51% in 12 days (r/localseo, 2026, marketer's self-report).
- **Point the GBP at a city page when the GBP city is not your strongest page's city.** For a Plano profile serving Dallas-Fort Worth, a Plano page with NAP, neighborhoods and local job photos (r/localseo, 2026). Exception: one location with a strong home page.
- **Diversity update (VERIFY):** Sterling Sky (2025) reports it got harder to hold both a pack spot and an organic spot with the same page. Some practitioners avoid linking GBP to their strongest organic page. Single source; test before applying.
- **Backlinks still count** for organic and somewhat for the pack. An HVAC expert roundup (22 contributors via Sourcebottle, 18 published, each emailed the live link) earned 10 free links; pack rank went 5 to 2 a week later (r/localseo, 2025, uncontrolled).
- **Neighborhood pages do not move Maps rank in that neighborhood**, one tester reports after repeated tries (r/localseo, 2025). They help organic and AI answers. Do not sell them as a Maps fix.

## Avoid

- CTR or "engagement boost" services (fake clicks and direction requests). A LocalRank buyer reported rural gains, urban drops and 4 lost high-paying clients (r/localseo, 187 upvotes, 2026).
- Separate profiles per service line at one address. Duplicate profiles at the same address are a top negative factor (Whitespark 2026) and a suspension trigger.
