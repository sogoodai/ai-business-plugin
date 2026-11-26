# 90-day plan and recurring cadence

Order: eligibility and category, then measurement, then the review engine, then pages, then distribution, then spam. Stop low-evidence busywork that eats the time. Sources in [sources.md](sources.md).

## Days 1 to 14: truth and instrumentation

- [ ] Find every listing and duplicate ([gbp-audit.md](gbp-audit.md) step 0). Fix duplicates and critical fails first.
- [ ] Owner answers: real address mode (customers visit or not), services ranked by profit, towns served ranked by value, capacity by weekday, current review ask process, booking tool, phone answering.
- [ ] Save a baseline: GBP Performance export (views, searches, calls, directions, website clicks, bookings), review count, rating, newest review date, reply rate, screenshot of every profile field.
- [ ] UTM on the GBP link; GA4 event on `tel:` clicks; call tracking set up if calls matter.
- [ ] Geogrid (or town-by-town audit) for 3 money keywords ([rankings-and-geogrid.md](rankings-and-geogrid.md)).
- [ ] AI prompt set run once on each engine ([ai-answers.md](ai-answers.md)).
- [ ] Competitor sheet: top 3 per keyword with category, rating, count, 90-day velocity, distance.
- [ ] Evidence pack folder built ([suspensions-and-spam.md](suspensions-and-spam.md)).
- [ ] Category fix: primary first, then true secondary categories. Predefined services added. Hours, special hours, more hours. Pin checked. Never name and address in the same week.

## Days 15 to 30: review and reply engine

- [ ] Review link and QR generated and tested on a phone.
- [ ] Trigger wired to job completion, checkout or payment ([reviews.md](reviews.md)). Same request to everyone. One reminder.
- [ ] Gating and incentives removed from every tool and script.
- [ ] Review math run: catch-up target per quarter, rating repair count, requests per month.
- [ ] Every unanswered review replied to, negatives first ([review-templates.md](review-templates.md)).
- [ ] Reply SLA set: negatives same day, all within 7 days.
- [ ] Last 20 customers asked individually if the profile has been quiet.
- [ ] Target for a new business: reach 10 reviews, then 20, with no 3-week gaps.

## Days 31 to 50: website

- [ ] One strong page per money service, words matching GBP services.
- [ ] GBP link points to the matching home or location page; title and H1 name service and city.
- [ ] Town pages only where real local proof exists; merge thin duplicates.
- [ ] Internal links: hubs to services to towns; each priority page linked from relevant pages.
- [ ] LocalBusiness schema matching GBP. No self-serving rating markup.
- [ ] Facts as text: towns, hours, starting prices, licenses, warranty, booking, insurance.
- [ ] Search Console: indexing check of every service and location page; quick-win title rewrites.
- [ ] robots.txt allows OAI-SearchBot, PerplexityBot, Claude-SearchBot, Googlebot, Bingbot.

## Days 51 to 65: distribute the entity

- [ ] Bing Places (import from Google), Apple Business Connect, Facebook, Yelp claimed and complete.
- [ ] Aggregators and the country's core directories; vertical directories.
- [ ] Citation audit by search; wrong phones and old addresses fixed first.
- [ ] Source-gap list from the AI audit: get onto the directories, lists and associations cited for competitors.
- [ ] One local link or mention effort: chamber, association, supplier locator, sponsor page, local press angle, expert roundup.

## Days 66 to 75: spam

- [ ] Top 10 in each money keyword checked for stuffed names, fake addresses, lead-gen listings.
- [ ] Evidence log, Suggest an edit, Redressal form for clusters ([suspensions-and-spam.md](suspensions-and-spam.md)).
- [ ] Rankings recorded before and after.

## Days 76 to 90: measure and reallocate

- [ ] Rescan the same grids, same settings. Rerun the AI prompt set.
- [ ] Compare to day 1: SoLV and ARP per keyword, GBP actions, organic clicks, qualified calls, bookings, review velocity, reply time, rating, citation coverage, AI mention rate per engine.
- [ ] Keep what moved booked jobs. Drop what did not: posts that take 3 hours a week, citations that never rank or get cited, pages nobody visits.
- [ ] Next quarter's priorities: the 3 biggest gaps by value.

## Recurring cadence

**Weekly (30 to 60 minutes)**
- Reply to all new reviews; negatives same day.
- Review velocity check: alert if no review in 14 days or pace down 40%+.
- One GBP post for the current offer, event or season (optional, conversion only).
- Check "Google updates" and suggested edits on the profile.

**Monthly**
- 2-minute public check: name, phone, hours, category, open status as shown in Search.
- Geogrid on 3 money keywords, same settings.
- AI prompt set on each engine; log wrong facts.
- Upload a few real photos from recent work.
- Special hours for the next 60 days.
- Report: calls and bookings from Google first, then rankings, reviews, top 3 next actions.

**Quarterly**
- Category and service review against the current top 3; new categories Google added.
- Competitor velocity and catch-up math rerun.
- Citation and duplicate re-check; aggregator data.
- Spam sweep of the pack.
- Access audit: who has Owner and Manager.

## Alert thresholds

- New 1-star with no reply, or any review unanswered after 7 days
- No new review in 14 days (21 at most)
- Rating down 0.3+ in 30 days, or below 4.3
- Several reviews in a few hours from unknown accounts (possible attack)
- Profile shows "Closed", wrong phone or wrong hours
- GBP calls down 20%+ month over month while rankings are stable (check tracking and website clicks before blaming SEO)
- Brand search not #1 in a scan (data or listing problem)
