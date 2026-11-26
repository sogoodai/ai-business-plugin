---
name: hospitality-travel
description: Grow a short-term rental (Airbnb, Vrbo host or small property manager), B&B, small hotel, hostel, tour guide or operator, or small travel agency. Listing photos and copy, Airbnb, Vrbo and Booking.com ranking, Guest Favorite and Superhost, reviews, dynamic pricing, minimum stays, cleaning fees, direct bookings vs OTAs, repeat guests, Viator and GetYourGuide, planning fees, local partnerships. Use for any marketing, pricing or guest-messaging task in lodging, tours or travel.
---

# Hospitality and travel: win the marketplace, then own the guest

Built from 571 practitioner threads (r/airbnb_hosts, r/AirBnB, r/vrbo, r/hotels, r/bedandbreakfast, r/travelagents, r/Tourguide), the 209 tactics extracted from them, the raw guest-side threads, a few hospitality tactics from other segments (real estate, creator, sales), and a November 2026 research pass on platform documentation and benchmark datasets (Airbnb, Vrbo, Booking.com, Google Hotel Center, Viator, GetYourGuide, Tripadvisor, AirDNA, KeyData, Cloudbeds, Revinate, Wheelhouse, PriceLabs, Beyond, Travel Market Report). "Operators report" marks a Reddit anecdote with its upvotes; everything else carries its source and year. Most Reddit voices are US hosts and guests; tour operators, hostels and B&Bs are thin in the data. Sources: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

## How these businesses actually grow

- **Marketplaces rank on predicted conversion and reliability, not keywords.** Airbnb weighs quality, popularity (saves, messages, bookings), total price against local comparables, availability and cancellations. Booking.com's model predicts the probability of a booking and uses click-through, gross bookings and net bookings after cancellations. Vrbo uses reviews, acceptance, cancellations, response and Instant Booking (platform docs, 2026). Better conversion buys more exposure, which buys more bookings.
- **The product is a perishable night or seat.** An empty Tuesday is gone. Revenue per available night (RevPAR), not occupancy, is the score: 90% occupancy at the wrong rate can lose to 75% (PriceLabs 2026).
- **Guests compare the total, and their alternative is a hotel.** A $77 Google result that became $329 at Vrbo checkout drove the guest to a Holiday Inn (r/vrbo, 3,071). Fees, chores and surprise rules are the top guest complaints in the data.
- **Reviews and badges are gates.** Guest Favorite, Superhost, Vrbo Premier Host and Booking.com review scores set visibility and click-through. One 4-star review can drop a Top 1% listing (operators report, r/airbnb_hosts 680 and 441).
- **OTAs rent you the guest; direct keeps them.** Independent hotels took 36.6% of 2025 bookings direct, 63.4% via OTAs; OTA bookings cancelled at 21.8% vs 10.6% direct (Cloudbeds 2026, 90M bookings). For managed vacation rentals, direct was 24% of reservations but 36% of revenue (KeyData 2025).
- **2026 changed the math.** Airbnb's 15.5% host-only fee (PMS-connected hosts moved 13 October 2026), Vrbo Premier Host rules (1 January 2026) and permanent removal for failing listings (15 September 2026), Google AI Mode hotel booking through partners (27 August 2026), GetYourGuide cancellation and no-show limits. Old playbooks are wrong on all of these.

## First session: ask, then compute

Ask the owner:

1. Business type, units or rooms (or tour capacity per departure), market, property type, sleeps and bed layout, hosted or not.
2. Channels live (Airbnb, Vrbo, Booking.com, Expedia, Google, own site, Viator, GetYourGuide, Tripadvisor, Airbnb Experiences) and the PMS or channel manager. Is calendar sync verified?
3. 12 months of reservations: channel, booked date, arrival, nights, guests, gross, fees, cleaning, cancellations, review score. Export it.
4. Pricing tool (PriceLabs, Wheelhouse, Beyond, Airbnb Smart Pricing, none), base and minimum price, minimum-stay rules, cleaning fee, extra-guest fee, discounts that are on, cancellation policy per channel.
5. Badges and scores: Superhost, Guest Favorite tier, Vrbo Premier Host, Booking.com score, Google rating, Tripadvisor rank. Reviews in the last 90 days.
6. Direct: website and booking engine, Google Business Profile, Google Hotel Center or Vacation Rentals feed, email list size and consent source, repeat-guest share.
7. Registration or license status for every address, renewal dates, local caps (nights per year, principal residence).
8. Costs per stay: cleaning, laundry, supplies, turnover labor, damage history. For tours: guide cost per departure, commission by channel. For advisors: host split and fees.
9. What the owner refuses: parties, pets, one-night stays, locals, Instant Book, long stays.

Then compute ([references/economics.md](references/economics.md)):

```
RevPAR             = revenue / available nights            (compare to a local comp set, same data provider)
net RevPAR         = (revenue - channel fees - unrecovered cleaning) / available nights
channel net payout = guest total - taxes - platform fees - payment fees     (per channel, per typical stay)
Airbnb reprice     = old payout per night / (1 - 0.155)     ($97 / 0.845 = $114.79)
fee load           = (cleaning + extra fees) / guest total for the most common stay length
orphan nights      = open gaps in the next 60 days shorter than the minimum stay that applies to them
pickup pace        = nights on the books for month M now vs same lead time last year, or vs market
review velocity    = reviews in last 90 days / completed stays in last 90 days
direct share       = direct revenue / total revenue        (revenue, not bookings)
repeat value       = OTA commission rate x average booking x expected return stays
tour contribution  = price x (1 - commission) - guide and variable cost per head
advisor net        = gross commission x split - host and transaction fees + planning fees
```

Report the three biggest gaps in money. Typical first findings: Airbnb rates never adjusted for the 2026 fee, cleaning fee over a third of a two-night total, minimum stays stranding gaps, no review request, and no way to reach past guests.

## Route by business type

| Business | What sells | Main channels | Biggest lever | Watch out for |
|---|---|---|---|---|
| Whole-home STR | Space, location, amenity (hot tub, view, pets) | Airbnb, Vrbo, own site, Google VR | Photos, total price, min-stay rules | Fees, chores, parties, regulation |
| Room in home, guesthouse near host | Price, host, privacy terms | Airbnb, Booking.com | Honest disclosure of shared spaces and host proximity | Mismatch reviews |
| Mid-term (28+ nights) | Furnished home for work, insurance, relocation | Airbnb, Vrbo with 30-day minimum, relocation firms | Corporate and insurance referrals | Tenant rights, prepaid long stays |
| B&B, small hotel, inn | Rooms, breakfast, character | Booking.com, Expedia, Google free links, direct | Direct-booking benefits, Hotel Center feed | Rate parity contract, OTA cancellations |
| Hostel | Beds, social, location | Booking.com, Hostelworld, Google | Reviews and photos of common areas | Thin data here |
| Tour guide, operator | A time-slot experience | Viator, GetYourGuide, Tripadvisor, Airbnb Experiences, Google Things to do, hotels | First reviews, inventory loaded a year out | Commission vs margin, quality limits |
| Travel advisor | Expertise and supplier access | Referrals, niche content, host agency | Planning fee before research | Commodity trips, Costco and OTAs |

Depth by type: [references/by-business.md](references/by-business.md).

## Benchmarks to check first

| Metric | Value | Source, year |
|---|---|---|
| US STR occupancy forecast | 57.4% for 2026 | AirDNA, July 2026 |
| US STR month | 53.6% occupancy, $254 ADR, $136 RevPAR (RevPAR +15.3% YoY) | AirDNA, September 2026 |
| US managed vacation rentals | 41% paid occupancy, $309 ADR, $126 RevPAR | KeyData, 2025 |
| Independent hotel direct share | 36.6% global; US 53.3%, Canada 49.8% | Cloudbeds, 2025 data |
| Cancellation rate | OTA 21.8% vs direct 10.6% | Cloudbeds, 2025 data |
| Hotel booking window / stay | 40 days (NA 48) / 2.6 nights | Cloudbeds, 2025 data |
| Professional photos (Airbnb program) | +21% earnings, +19% bookings over 365 days | Airbnb, 2024 to 2025 cohort, observational |
| Hotel email, list under 5,000 | 43.3% open, 0.51% booking conversion (0.05% over 50,000) | Revinate, 2025 data |
| Abandoned-booking email | 6.8% conversion; cancellation recovery 5.8% | Revinate, 2025 data |
| Pricing engine A/B | +7.11% revenue, +7.49% RevPAR, ADR only +0.68% | Wheelhouse, 2026, vendor-run |
| Switching pricing tools | Median +7 to +11%, but about 1 in 3 flat or down | Beyond, 2026, self-selected |
| New activity reviews | 3 reviews = 3x more likely to be booked than 0 | GetYourGuide, 2026, platform claim |
| Advisor commission kept | 80% average via host agency; host fee about $500 a year | Travel Market Report, 2025 |

Never compare AirDNA occupancy with KeyData or hotel occupancy; denominators differ. Benchmark to a local comp set. Full tables: [references/benchmarks.md](references/benchmarks.md).

## Decision rules, in order

1. **Fix money leaks before marketing.** Reprice Airbnb for the host-only fee, audit every channel's net payout, turn off discounts you did not choose (Vrbo auto-enabled booking discounts in 2025; r/vrbo 643), check custom trip lengths after connecting a pricing tool (a rogue PriceLabs setting set 90 to 135-night minimums for two years and bookings went to zero; r/airbnb_hosts 1,416).
2. **Make the listing true, then beautiful.** Every fee, chore, shared space, stair, noise source, host proximity and walking time disclosed before booking. Undisclosed items cause refunds that platforms enforce, then bad reviews.
3. **Replace amateur photos before buying traffic.** Cover photo wins the click; first five photos sell the stay; every room guests use is shown; exterior and window views exist.
4. **Price on RevPAR with rules, not a flat rate.** Dynamic pricing plus far-out minimum stays, gap-length minimums near arrival, event dates blocked or priced before they open. Judge any tool against its own control period.
5. **Simplify checkout and the fee stack.** Cleaning in the rate or a low fixed fee, a three-line checkout. Hosts report gains in both bookings and reviews.
6. **Earn the badge thresholds on purpose.** Superhost (4.8+, under 1% cancellations, 90%+ response), Guest Favorite (5+ reviews in 4 years, rated daily), Vrbo Premier Host (99% acceptance, 0% host cancellations, 4.6+). Never cancel a guest; it costs rank on every platform.
7. **Ask every guest for a review, the same way, on checkout day.** Never trade money for a review; never refund just to prevent one.
8. **Build direct last on the stack, but build it.** Google free booking links or Vacation Rentals, a booking engine, consented guest data from completed stays, four email flows. Never divert a live OTA reservation.
9. **Add local partners and second markets** (mid-term, corporate, insurance, production, events) when calendars have structural gaps.
10. **Paid ads last.** Google hotel and Things to do placements, then search; scale on net contribution, never on clicks. Depth: `paid-ads`.

## Listing in one screen

- **Copy opener:** "Walk to [demand generator] in [X minutes]. Sleeps [N] in [actual beds], with [2 to 3 differentiators]. Best for [segment]. Note before booking: [material constraint]." (research pass 2026, recommended procedure).
- **Lead with what removes friction:** "Super low cleaning fee ($25), and no list of chores to check out!" in the first two sentences (operator, r/AirBnB).
- **Photos:** top photo-quality quartile had a median of 35 photos vs 25 in the bottom (Surge, 3,103 listings, 2026). No attraction photos 60 km away ("I don't even know if the property had a toilet", r/AirBnB 675). Google Vacation Rentals needs 5+ images, recommends 8, strongly recommends 20+.
- **Show the outside:** guests check satellite views and Street View; one walked away from a listing with all blinds drawn and booked down the street (r/airbnb_hosts, 78-upvote comment).
- **Audit auto-added badges** ("Extra spacious" on a small studio caused a complaint Airbnb refused to fix; r/airbnb_hosts 739).
- **Repeat key limits after booking:** a post-booking message listing easy-to-miss limits and the free-cancellation deadline.

Full playbook: [references/listing-optimization.md](references/listing-optimization.md).

## Pricing and minimum stays in one screen

- **Airbnb 2026:** at 15.5% host-only, a $100 rate that paid $97 now pays $84.50; $115 restores it (Airbnb 2026). Guests no longer pay the separate service fee, so compare the guest total to comps, not the listed rate.
- **Minimum stays by window:** long far out on peak and event dates, shorter mid-window if pickup trails the market, gap-length minimum near arrival, arrival and departure rules that prevent one-night remainders (PriceLabs 2026).
- **Event dates:** block the month around a festival until dates are announced, then price and open. A San Diego host's Comic-Con dates booked within minutes of the announcement at normal rates (r/AirBnB, 68 and 13).
- **Cleaning fee:** one cabin owner removed a $200+ fee and went from about one weekend a month to every weekend for six weeks (r/AirBnB 218, uncontrolled). Fixed per-stay costs still decide the minimum stay: compute it ([references/pricing-and-stays.md](references/pricing-and-stays.md)).
- **Large homes in thin markets:** price for 2 to 3 guests, add an extra-guest fee, but the fee must show in the quoted total from search.
- **Long and work stays:** do not auto-discount production and corporate bookings; hosts report full-price film crews (257 upvotes) and a six-week $20,000 booking.
- **Hotels:** give the desk authority to match a verified OTA rate when ready to book direct; refusing sends the guest back to the OTA (r/hotels 2,299). In the EEA, Booking.com dropped parity in July 2024.

General price psychology: `offers-pricing`.

## Reviews and recovery in one screen

- **Request on checkout day,** after any issue is handled: "If the stay matched what you expected, we'd really appreciate an honest review" ([references/scripts.md](references/scripts.md)). Airbnb's review window is 14 days.
- **Keep automated review asks neutral** (no "you were great guests"), so they stay usable after a bad stay (r/airbnb_hosts 1,690).
- **Recovery beats perfection:** coffee delivered while a Keurig was replaced the same day ($15; r/airbnb_hosts 415); dinner bought for a group while an odor was treated ($100; r/AirBnB 71).
- **Refund only against rebooked nights,** paid after the replacement stay completes. Scripts in [references/reviews-and-recovery.md](references/reviews-and-recovery.md).
- **Appeal with facts, not feelings:** screenshots of a written threat plus the policy; a second, factual request removed a retaliatory review (r/airbnb_hosts 1,128).

## Direct bookings and repeat guests in one screen

- Stack for small hotels and B&Bs: Business Profile, Hotel Center feed, accurate live rates, free booking link, booking engine, abandoned-booking email. For rentals: Google Vacation Rentals through a connectivity partner. No click or booking fee from Google on free links (Google 2026).
- Give direct a reason: flexible cancellation for direct, non-refundable for OTA (r/bedandbreakfast); upgrades and room choice for direct ("Those are for members who book direct", r/hotels).
- Four flows first: checkout and review, post-stay rebooking, abandoned booking, cancellation recovery. Small segmented lists beat big blasts 10x (Revinate 2026).
- Convert long stays to direct only when the booked term ends and only after checking local tenancy law; one host turned a 9-month booking into a $7,750 monthly lease and kept the tenants four years (764 upvotes).

Playbook: [references/direct-and-repeat.md](references/direct-and-repeat.md). Flows and consent: `email-sms-loyalty`.

## Tours and advisors in one screen

- **Tours:** load GetYourGuide inventory a year ahead and bookable until start; use the 30-day launch offer (20% recommended) to buy the first reviews; keep cancellations at or under 1.0% and no-shows at or under 0.2% (rolling 90 days). Viator charges $29 per new experience and sells extra exposure for extra commission (Accelerate). Playbook: [references/tours-and-activities.md](references/tours-and-activities.md).
- **Advisors:** send the service list, questionnaire and fee before any research; a $200 quoting deposit credited on booking weeds out shoppers (r/travelagents, 56). Sell one niche, not "I can book anything". Playbook: [references/travel-advisors.md](references/travel-advisors.md).

## Local partnerships

Guest-booklet offers paid per redemption ($50 off a helicopter tour, $15 per ticket to the booklet owner; r/Affiliatemarketing), corporate, insurance and relocation housing, film and photo shoots, event blocks sized from 10 rooms, influencer stays with a paid night. [references/partnerships.md](references/partnerships.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data or mechanism says | Rule |
|---|---|---|---|
| Instant Book | "Turned it off, still page one" (1,009) vs "huge volume with it on" | Vrbo ranks Instant Book higher; Airbnb weighs booking friction | Keep on with guest requirements and 2-day advance notice; turn off only for high-risk dates, then track views and bookings |
| Minimum stays | "Gap nights brought a 30-person party" ($1,348 damage, 1,690) | Availability and stay flexibility affect exposure; gap-length minimums raise RevPAR (PriceLabs) | Gap minimums yes, with screening, advance notice and no same-day local one-nighters |
| Cleaning fee | Fold it in or drop it; bookings jumped | No controlled data; Airbnb ranks total price | Rate plus low fee or none for short stays; fixed fee per stay for long stays |
| Pricing tools | Some swear by them; one tool zeroed bookings | Wheelhouse A/B +7.5% RevPAR; Beyond: a third of switchers flat or down | Use with rules and a control comparison; audit settings weekly for 4 weeks |
| Badges as pricing power | Gold Guest Favorite at 95% occupancy, any raise stopped bookings (Dubai, 291) | Price is judged against local comps; supply grew 20,000 listings there | Badges lift conversion, not price ceilings; raise in small steps and watch pace |
| Refunds to save reviews | "Paid $100 extra, got 5 stars" (723) vs "refunded, still got 2 stars" (905) | Airbnb removes reviews tied to extortion | Never pay for a review; screenshot any threat and report before the review posts |
| Booking.com parity | "Must match the lowest web price" | Removed in the EEA in July 2024; external prices not used for ranking there | In the EEA price direct lower if margin allows; elsewhere read your contract |
| Social media | Advisors report building on talking-head videos with under 1,000 followers | Usage stats only; no effectiveness data | Niche proof content for advisors and tours; for lodging, fix the listing first |

## Never

- Never cancel a confirmed guest to reprice a date you underpriced. Honor it, fix the calendar. Cancellations cost rank on every platform and Vrbo invoices a penalty ($119, r/vrbo 316).
- Never let a cleaner or worker enter an occupied unit on a schedule alone; get written permission the day before (a long-stay guest was refunded about 25 nights; r/airbnb_hosts 4,143).
- Never hide a mandatory fee, chore, ID upload, AC charge or amenity outage until after booking.
- Never offer money, discounts or refunds for a review, or ask only happy guests. US FTC rule since October 2024; UK fines since April 2025 (see `local-seo`).
- Never pull a live OTA reservation off-platform, or put contact details or links in OTA messages against the platform's rules.
- Never trust a hidden, inactive or incomplete listing to be unbookable. Delete it through support (Vrbo took five bookings on one; r/airbnb_hosts 2,554).
- Never mass-email past guests without marketing consent; OTA bookings do not grant it.
- Never treat registration as one-time; check every address against local rules on a schedule.
- Never invent a benchmark, a review, a scarcity claim or an offer the owner has not approved.

## Before you write any guest message

Use [references/scripts.md](references/scripts.md): post-booking limits message, arrival message, checkout lines, review request, mid-stay entry permission, cancellation and refund-if-rebooked, early departure, weather cancellation, service recovery, review replies, direct rebooking email, abandoned booking, influencer counter, OTA rate match, advisor fee and quote scripts, price-drop offer.

## References

- [benchmarks.md](references/benchmarks.md): STR, hotel, email, photo, pricing, tour and advisor numbers with source and year; operator numbers; evidence gaps.
- [economics.md](references/economics.md): formulas with worked examples (Airbnb repricing, channel payout, RevPAR, fee load, minimum stay break-even, Accelerate, launch discount, advisor split).
- [platforms.md](references/platforms.md): Airbnb, Vrbo, Booking.com, Expedia, Google, Tripadvisor ranking signals, thresholds, fees and setting traps.
- [listing-optimization.md](references/listing-optimization.md): photos, copy, disclosures, amenities, checkout, guest-pleasing details.
- [pricing-and-stays.md](references/pricing-and-stays.md): dynamic pricing, minimum stays, gaps, events, fees, guest-count pricing, long stays, hotel rate tactics.
- [reviews-and-recovery.md](references/reviews-and-recovery.md): badges, requests, replies, removal appeals, refunds, service recovery.
- [direct-and-repeat.md](references/direct-and-repeat.md): Google free links, booking engine, OTA guest conversion, email flows, measurement.
- [partnerships.md](references/partnerships.md): local businesses, mid-term and corporate, production, events, influencers, city pages.
- [tours-and-activities.md](references/tours-and-activities.md): Viator, GetYourGuide, Tripadvisor, Airbnb Experiences, Google Things to do, reviews, launch.
- [travel-advisors.md](references/travel-advisors.md): niche, fees, quoting, host agencies, leads, first clients, retention.
- [by-business.md](references/by-business.md): whole homes, rooms, mid-term, B&Bs and inns, small hotels, hostels, glamping, tours, advisors.
- [regulation-and-rules.md](references/regulation-and-rules.md): STR registration (EU, England, BC, NSW), review law, platform rules, consent.
- [scripts.md](references/scripts.md): exact wording for every recurring conversation.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan with exit checks.
- Sibling skills: `local-seo` (Google Business Profile, reviews law), `email-sms-loyalty` (flows, consent, WhatsApp), `paid-ads` (Google and Meta accounts), `organic-social` (content and Reels), `website-conversion` (booking pages), `offers-pricing` (price psychology and increases), `events-weddings` (venues and wedding blocks).
