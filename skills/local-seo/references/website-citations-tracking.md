# Website pages, citations, Apple and Bing, tracking

Sources in [sources.md](sources.md).

## Service and location pages

**Rule:** one strong page per service that makes money, one genuinely useful page per real market served. Not 200 suburb clones.

- Google's spam policy calls sets of near-identical city pages that funnel to one destination **doorway abuse**. **Swap test** (RicketyRoo, via claude-seo): if you can swap the city name and the page still reads true, it is a doorway. An HVAC company lost 80% of rankings and 63% of traffic in the March 2024 core update for this pattern.
- Practitioners agree one substantial page beats 40 thin ones (r/localseo, 147-upvote thread, 2026, OP conceded the point). Whitespark 2026 ranks dedicated service pages #2 for AI visibility and among top local organic factors.
- **Content vehicle per keyword** (localseoskills, MIT): local transactional term with roughly 50+ searches a month and real local facts = page. Real service variant under about 50 a month = GBP service entry, not a page. Cluster matching a true category = add the category. Cost and problem questions = blog or FAQ. "Near me" = no page; it is won by GBP, proximity and reviews. Under 10 a month or a service you don't sell = nothing.
- **What makes a town page real:** jobs done there with photos, neighborhoods, local building types or climate issues, permits and rules, drive time and response time, local prices, reviews from customers there, local partners. A service-area business never invents an office address or implies a branch.
- **Template** (localseoskills, MIT): title `[Service] in [City, ST] | [Brand]`; H1 `[Service] in [City]`; click-to-call and form above the fold; sections: what we do, why us (proof), service details, local context, reviews from this area, local FAQ, CTA.
- **Scale gates:** 5 to 20 pages hand-written; 20 to 100 template plus required unique sections; 100+ only with a real per-page data source and proven demand. claude-seo stops at 50+ location pages until the owner justifies them.

Operator wins (bundled, self-reported): small suburbs of 5,000 to 10,000 people targeted by a brand-new site with commercial pages: 77 keywords at #1 and 3 form leads in under 30 days (r/localseo, 2025, low competition). A house cleaner's town pages plus reviews, citations and links took organic leads from 0 to 2 a week to 3 to 5 a day over 9 months in NYC (r/localseo, 2025). A junk removal site narrowed from several states to one, then rebuilt city pages under a county > city structure: Maps positions 3 to 4 became 1 to 2 within 18 km in three months (r/localseo, 2026).

**Internal links:** `Home > Service hub > Service > Town proof` and `Home > Areas hub > Town > Services`. Every page you care about gets at least one crawlable `<a href>` link with descriptive anchor text (Google Search Central). One site moved 6 pages from positions 15 to 25 into 4 to 9 in 3 weeks by merging 11 overlapping posts into 5 and pointing internal links at 5 priority pages that had almost none (r/localseo, 2026).

**Content that keeps pulling calls:** turn the questions customers ask on the phone into local cost posts ("how much does it cost to fix a leaking water heater in Austin"); one operator says such posts pull calls for two years (r/localseo, 2026). City-specific problem posts ("slab leaks in [city]") beat generic "what is a slab leak" (r/localseo, 2026). Wedding photographers blogging a venue every Thursday get inquiries within a day or two, including for other venues (r/WeddingPhotography, 2026).

**Search Console quick wins (2 hours, run before writing anything new)** (r/localseo, 2026): Performance > last 3 months > Pages, sort by impressions. Pages at average position 8 to 25 with 200+ impressions and CTR under 3%: rewrite the title around the queries actually showing. Pages at 12 to 18 with CTR 3%+: add depth and internal links. Pages at 15 to 30: strengthen with internal links, FAQs, author credentials and reviews before chasing backlinks.

**Indexing checks:** confirm every location page is indexed. One multi-location client had 40% of location pages missing from Google's index, plus soft 404s and canonicals pointing to another location (r/localseo, 2026). A WordPress "coming soon" page left up for almost a year slowed indexing after launch (r/localseo, 2026).

## Schema

- `LocalBusiness` with the most specific subtype (Plumber, HVACBusiness, HairSalon, DaySpa, Restaurant, CafeOrCoffeeShop, Bakery, Dentist, ChildCare...). Google requires `name` and `address`; recommends `geo`, `openingHoursSpecification`, `telephone`, `url`, `priceRange`, `image`, `menu` and `servesCuisine` for restaurants. One block per real location with its own `@id`.
- Must match the visible page and the GBP exactly. Schema is entity clarity, not a ranking lever.
- **SAB:** omit `address`, list `areaServed` towns; no LocalBusiness rich result without an address, so never invent one.
- **Do not** copy your Google rating into `aggregateRating` on your own page; self-serving review markup earns no stars.
- **FAQPage rich results were retired for all sites on 7 May 2026** (claude-seo). Keep FAQ content for readers and AI; expect no SERP feature.
- Google: AI Overviews and AI Mode need **no special schema, no llms.txt**.

## Citations: build where people or AI look

**Decision rule** (deep research, 2026): build or fix a listing only if consumers use it, it ranks for your searches, AI answers cite it, it feeds a major map or data network, or it is the authority in your vertical. Do not buy packages of hundreds.

- **Core set everywhere:** Google, Apple Business Connect, Bing Places, Facebook, Yelp, plus aggregators (Data Axle, Foursquare, Neustar/Localeze, now TransUnion). Data Axle feeds Google, Bing and Apple; Foursquare powers Uber and Nextdoor and is cited by ChatGPT (claude-seo, 2026).
- **US:** add BBB, Yellow Pages, MapQuest, Nextdoor, Thumbtack, Angi (by trade), Houzz (remodel and design).
- **Canada:** YellowPages.ca, Yelp, Foursquare, MapQuest, BBB. **UK:** Yell, The Phone Book (BT) ecosystem, Central Index, Yelp UK, FreeIndex, trade bodies. **Australia:** Yellow Pages AU, TrueLocal, White Pages. **France:** PagesJaunes, 118000.fr, Infobel. Whitespark keeps country lists (whitespark.ca/top-local-citation-sources-by-country).
- **Vertical:** healthcare (Healthgrades, Zocdoc, WebMD, Doctolib in France), legal (Avvo, Justia, FindLaw), restaurants (Tripadvisor, OpenTable, Resy, delivery apps), beauty (Fresha, Treatwell, Booksy, Vagaro, StyleSeat), home services (Thumbtack, Angi, Houzz, Checkatrade in UK), brand "find a provider" locators (Invisalign, Generac, Mitsubishi).
- **Find what AI uses:** BrightLocal (2026) found 415 directories cited in local AI answers. Run the AI audit in [ai-answers.md](ai-answers.md) and add the directories cited for winning competitors.
- **Diminishing returns:** 0 to 50 quality citations matter, 200 to 250 barely (localseoskills, MIT). A one-time cleanup is enough in low to medium competition; one operator pays no ongoing sync fees for 6 clients (r/localseo, 2026).
- **Audit by search:** `"business name" "phone"`, `"business name" "street"`, and old phone and address. Log URL, current data, correct data, action. Fix wrong phones and old addresses first; "St" vs "Street" is not a real conflict (marketingskills, MIT). Fix aggregators, wait 4 to 8 weeks, then fix downstream sites.
- **Home-based SAB:** never publish the private address to satisfy a directory. Skip directories that force a public address.

## Apple and Bing (cheap, often skipped by rivals)

- **Apple Business Connect** (business.apple.com, free): claim, verify by phone, domain email or documents; its own categories; Showcases (Apple's posts) and action links for booking, ordering, reservations. Apple Maps use for local reviews rose to 27% (BrightLocal LCRS, 2026). Apple pulls ratings from partners such as Yelp, so a weak Yelp profile hurts on iPhones. Siri answers from Apple data plus Yelp.
- **Bing Places** (bingplaces.com): "Import from Google" takes minutes; check categories after import. Bing is the main index behind ChatGPT search and Copilot (claude-seo, 2026). Also add Bing Webmaster Tools with the sitemap and IndexNow.

## Tracking (set up before claiming any result)

- **GBP website link:** `https://example.com/location/?utm_source=google&utm_medium=organic&utm_campaign=gbp`. Lowercase, same convention everywhere. Separate tags for the booking and menu links.
- **"Calls" in GBP = clicks on the call button**, not answered calls (Google Help). Call history inside GBP ended 31 July 2024.
- **Call tracking:** tracking number as primary GBP phone, main number as additional phone, main number on the website and directories (r/localseo, 2026; some practitioners keep the main number primary, a dispute). On the website use dynamic number insertion (CallRail, WhatConverts) and a GA4 event on `tel:` link clicks.
- **Audit agency-reported calls.** One owner paid an agency a few thousand dollars a month for 6 months and got 2 real calls; the "calls" were disconnects with dead callback numbers (r/localseo, 2026).
- **Report three things only** (r/localseo, 2026): rankings for target keywords (geogrid), calls from GBP, organic traffic trend. Add bookings and revenue from the CRM.
- **Click-to-call has trended down for two years** across 170+ profiles even where rankings held, as AI answers and layout absorb clicks (localseoskills, MIT). Do not report falling calls as SEO failure when rankings are stable; check website clicks and bookings.
- Benchmarks for GBP actions are in [benchmarks.md](benchmarks.md).
