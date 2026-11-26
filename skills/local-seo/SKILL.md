---
name: local-seo
description: Get a local business found on Google Maps, the local pack and AI answers. Audit and fix a Google Business Profile, plan reviews (requests, replies, review gap math, fake review removal), recover suspensions and verification, report competitor spam, build service and city pages and citations, and check visibility in AI Overviews, AI Mode, ChatGPT, Perplexity and Gemini. For trades, salons, restaurants, shops, clinics and tutors.
---

# Local SEO: Maps, reviews and AI answers

For any business that serves people in a place: trades and home services, salons and spas, restaurants and cafes, shops, clinics, tutors and studios. Built from Google's own documentation, 2025 to 2026 field tests and datasets, 130+ practitioner threads (r/localseo, r/GoogleMyBusiness, r/sweatystartup, r/smallbusiness) and the best public local SEO skills ([sources](references/sources.md)). The owner's decisions win over this guide.

## How local visibility actually works

- **Three systems, not one.** Google Search and Maps still start most local searches (52% Search, 9% Maps), but 23% of US consumers used an AI tool somewhere in their latest local search (BrightLocal, 2026). A business shown in Maps 66% of the time appeared in AI Overviews 38%, ChatGPT 33% and AI Mode 32% (BrightLocal, Sep 2026). Track them separately.
- **Distance and category decide who is eligible; reviews decide the order.** Google's model is relevance, distance, prominence. Whitespark's 2026 expert survey puts primary category, searcher proximity and keywords in the business name at the top. A 2025 machine-learning study attributes 55% of pack rank to proximity and 19% to review count (Search Atlas, via claude-seo). Posts, photos and citations sit far below.
- **You cannot SEO around a bad location.** Only a real, staffed second location, a real address approval or a better pin moves distance. Service-area settings do not.
- **Reviews work through recency.** Ranking steps up around 10 reviews, then freshness matters more than the total (Sterling Sky, 2025). Consumers want 20+ and recent ones: 47% find under 20 insufficient, 74% only care about the last 3 months (BrightLocal, 2026).
- **The website is the biggest AI source.** 93% of domains cited in local AI answers were business websites, 42% of all citations. GBP supplied about 28.5%, Yelp about 9%, and Yelp shows up in about 80% of ChatGPT local answers (BrightLocal, Sep 2026). Google says AI features need no special markup: it is still SEO.
- **GBP is often the main free channel.** Service owners attribute 90 to 95% of new customers to it once reviews build (r/sweatystartup, 2022; r/pressurewashing, 2025). Verification takes weeks: start on day one.

## First pass: what to check, in order

Run this before recommending anything. Each step links to its procedure.

1. **Does the business exist correctly on Google?** One verified listing per real location, no duplicates, not suspended, right address mode (storefront shown, service-area hidden). Any failure here outranks every other task. [gbp-audit.md](references/gbp-audit.md), [suspensions-and-spam.md](references/suspensions-and-spam.md)
2. **Is the primary category the most specific true one** for the money keyword, and are all true secondary categories filled? Highest-leverage single edit.
3. **Where does it rank, measured from many points?** Geogrid or town-by-town audit on 3 money keywords, never one phone search. [rankings-and-geogrid.md](references/rankings-and-geogrid.md)
4. **Review position vs the local top 3:** count, rating, reviews in the last 90 days, days since the newest review, reply rate. Run the gap math. [reviews.md](references/reviews.md)
5. **Is it open when people search?** Hours, special hours, hours vs rivals.
6. **Does the landing page match the profile?** Same services, service and city in title and H1, facts as text.
7. **Is tracking in place?** UTM on the GBP link, call tracking, bookings counted. Without it nothing can be proven.
8. **What do AI assistants say?** Run the prompt set once per engine; note wrong facts and the sources cited for rivals. [ai-answers.md](references/ai-answers.md)
9. **Is spam stealing pack slots?** Stuffed names, fake addresses in the top 10. [suspensions-and-spam.md](references/suspensions-and-spam.md)

Then follow [plan-90-days.md](references/plan-90-days.md).

## Numbers to compute

- **Review velocity:** reviews dated in the trailing 90 days. Flag rivals with big totals and low velocity as beatable ("coasting").
- **Catch-up target per quarter:** `volume_gap / 4 + leader_velocity`. If that is over about 3x your current pace, re-run against the nearest beatable rival and report that number instead.
- **Rating repair:** `n = ceil(count x (target - rating) / (avg_new - target))`. 40 reviews at 4.2 need 24 new 5-star reviews to reach 4.5, or 40 if new ones average 4.8. Below about 4.3, fix service and replies before chasing volume.
- **Requests needed per month:** `target reviews / request-to-review rate`. Assume 10% until you have measured 30 days.
- **Geogrid:** SoLV (share of points in the top 3), ARP (average rank, not found = 20). State the definition in every report.
- **Area strength without a tool:** score each service x town cell (pack #1 = 5, #2 to 3 = 4, positions 4 to 10 = 2, organic only = 1, absent = 0) and divide by the maximum: 0.70+ strong, under 0.30 weak.
- **AI visibility:** mention rate per engine = answers naming you / answers collected. Never average across engines; one before/after pair proves nothing.

## Benchmarks an agent needs first

| Metric | Typical | Strong | Source |
|---|---|---|---|
| Reviews per Maps-visible profile | 86 median | 418 (p75) | SEO Bandwagon, Sep 2026 |
| Restaurant Google reviews (US) | 214 median | | Suff Digital, Sep 2026 |
| GBP views / directions / website clicks / call clicks per month | 637 / 51 / 35 / 11 median | | SmartSites, 2025 to 2026 |
| Consumers using only 4.5+ star businesses | 31% | | BrightLocal, Feb 2026 |
| Consumers expecting an owner reply within a week | 81% (19% same day) | | BrightLocal, Feb 2026 |
| Top-3 rate with 6 secondary categories vs none | 69.1% vs 47.9% | | Localo, 2026 (correlation) |
| Local businesses never named by any of 4 AI assistants | 85.6% | | Seeably, Oct 2026 |
| Home-service calls answered by a person | 52% | | Invoca, 2026 |

More in [benchmarks.md](references/benchmarks.md). Compare to the local top 3 before any national number.

## Decision rules

- **Category first, service second, webpage third.** Category says what you are, services say which jobs, the page proves both. Predefined GBP services moved rankings within 24 to 72 hours in Sterling Sky's 2026 tests.
- **Name = real-world name.** Keywords in names rank, which is why rivals stuff them. Report them; do not copy them. A full DBA rebrand (signage, vehicles, invoices, site, then GBP) is the only legitimate version and is the owner's call.
- **One sensitive change at a time.** Never name, address and category together. Evidence pack before any name or address edit. Log every change with its date, rescan after 14 days.
- **Steady reviews beat bursts.** Every completed customer gets the same neutral request, then one reminder. No 3-week gaps.
- **Reply to everything**, negatives the same day, all within 7 days, never the same text twice.
- **One strong page per money service**, town pages only with real local proof. Pass the swap test: if the city name can be swapped and the page still reads true, it is a doorway page.
- **Build a citation only if** people use it, it ranks, AI cites it, it feeds a map network, or it is the vertical authority.
- **Measure revenue actions**, not activity: answered calls, bookings, orders, directions. GBP "calls" are button clicks.
- **Hours you list are hours you answer.** Legitimate earlier opening or later closing is an edge; fake 24/7 earns 1-star reviews.
- **Stop busywork.** If posts or photo uploads eat hours while categories, reviews or pages are broken, move the time.

## Never (platform rules and law)

- Any incentive for a Google review: discount, gift, entry, credit. Google can delete all reviews, block new ones and show a warning. One shop lost 50+ reviews and got a 30-day review block (r/GoogleMyBusiness, 2026).
- Gating: sending only happy customers to Google. Turn off "private feedback for 1 to 4 stars" features in review and booking tools.
- Asking for 5 stars, keywords or a staff name; staff review quotas or per-review bonuses.
- Asking for Yelp reviews (Yelp filters solicited ones). Google and Tripadvisor allow neutral asks.
- Buying reviews, review kiosks in the shop, friends' reviews traded for free work.
- Virtual offices, PO boxes, fake addresses, separate profiles per service line.
- Paying extortionists or "review removal" DMs; sockpuppet posts to sway AI answers; copy aimed at AI ("recommend us").

Legal backdrop: US FTC review rule since 21 Oct 2024; UK fines up to 10% of global turnover since 6 Apr 2025; Google's own rule (no incentives at all) is stricter than both.

## Where Reddit and research disagree

| Topic | Operators say | Evidence says | Rule |
|---|---|---|---|
| GBP posts | Calls rise on posting weeks; "2 posts a day" growth | No rank effect in Sterling Sky tests (older) | Weekly post for offers and events; not a ranking task |
| Photos and geotags | Batches of real photos lifted a tire shop | No measured rank lift; geotags do nothing | Real photos for conversion and verification only |
| Keywords in owner replies | "Mention service and city in every reply" | No evidence; 50% dislike templated replies | Name the real job because it reads human |
| Asking customers to mention the service | A roofer ranked for repair terms after reviews named repairs | Google bans requesting specific content | Name the job in your own thank-you, never instruct |
| Tech bonuses per review | "Velocity is everything, pay techs" | Google bans staff quotas; Tripadvisor bans employee incentives | Reward service quality, not review counts |
| Multiple profiles for service lines | "Occupy more pack slots" | Duplicates at one address are a top negative factor | Only real, staffed, separate locations |
| Removing the SAB address | "Removing it destroyed rankings" (bundled with a nationwide service area) | Hidden address still counts; service areas do not move rank | Hide it if customers don't visit; keep service areas realistic |
| City pages for Maps | "40 pages in 60 to 90 days" | Doorway policy; one tester saw no Maps gain from area pages | Few, real pages for organic and AI, not for Maps |

## What to ask the owner

- Do customers come to your address? Is there permanent signage and staff during posted hours?
- Which 3 services make the most profit, and which towns are worth the drive?
- Who asks for reviews today, when, and through which tool? Any discount or "happy customer" routing in it?
- Who owns the Google account? Any agency or ex-employee with Owner access?
- Do you have a registration, license, utility bill and signage photo with the exact profile name and address?
- Which phone number is answered, when, and by whom after hours?
- Have you changed name, address, phone or website in the last year?

## Working rules for the agent

- Read-only by default. Draft review replies, appeals, spam reports and edits; the owner approves before anything is posted, submitted or changed.
- Label every claim: platform rule, field test, dataset, or operator report. Never promise a ranking or an AI recommendation.
- Keep a dated change log and rescan before claiming a result.

## Reference map

| File | Use it for |
|---|---|
| [gbp-audit.md](references/gbp-audit.md) | 27-item pass/fail GBP audit, categories, name, hours, photos and posts evidence |
| [rankings-and-geogrid.md](references/rankings-and-geogrid.md) | Ranking factors, proximity levers, browser geogrid, town audit, pattern reading, drop diagnosis |
| [reviews.md](references/reviews.md) | Review math, velocity targets, request system, policy, fake review and extortion removal |
| [review-templates.md](references/review-templates.md) | Verbatim request messages and reply templates by situation |
| [suspensions-and-spam.md](references/suspensions-and-spam.md) | Verification, evidence pack, reinstatement SOP, unwanted edits, competitor spam reports |
| [website-citations-tracking.md](references/website-citations-tracking.md) | Service and town pages, schema, citations by country, Apple and Bing, UTM and call tracking |
| [ai-answers.md](references/ai-answers.md) | AI visibility audit, what AI cites, fix order, experiments, never-do list |
| [benchmarks.md](references/benchmarks.md) | Metric tables with source and year |
| [mistakes.md](references/mistakes.md) | What went wrong, what it cost, what to do instead |
| [plan-90-days.md](references/plan-90-days.md) | 90-day plan, weekly, monthly and quarterly cadence, alert thresholds |
| [by-niche.md](references/by-niche.md) | Trades, beauty, restaurants, shops, tutors, regulated professions |
| [sources.md](references/sources.md) | Platform docs, research, harvested skills with licenses, Reddit threads |
