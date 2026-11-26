# Direct bookings, repeat guests and measurement

OTAs are the acquisition channel for most small properties. The job is to keep their exposure while turning completed stays into owned, consented relationships. Flow mechanics and consent law: `email-sms-loyalty`. Booking page conversion: `website-conversion`. Sources in [sources.md](sources.md).

## Why bother (the numbers)

- Independent hotels: 36.6% direct, 63.4% OTA in 2025; US direct 53.3% (Cloudbeds 2026).
- OTA reservations cancelled at 21.8% vs 10.6% direct (Cloudbeds 2026).
- Managed vacation rentals: direct was 24% of reservations but 36% of revenue (KeyData 2025).
- An independent hotel reports paying OTAs 17 to 30% (r/hotels, 52 upvotes); Airbnb's host-only fee is 15.5% (2026).

Value of a converted guest = commission rate x average booking x expected return stays ([economics.md](economics.md)).

## The direct stack, in build order

**Small hotels, inns, B&Bs**

1. Google Business Profile complete and correct (see `local-seo`).
2. Booking engine on your own domain with live rates, mobile-first, total price shown early.
3. Google Hotel Center connection through your booking engine or channel manager, with free booking links on. No click fee; ranked on value, landing-page experience and price accuracy; Hotel Ads spend does not lift the free link (Google 2026).
4. Price accuracy check monthly: click your own Google result; guests report hotel sites charging $30 to $100 more than Google showed (r/hotels).
5. Abandoned-booking recovery email (6.8% conversion, Revinate 2025 data).

**Vacation rentals**

1. A direct-booking site from the PMS (OwnerRez, Hostaway, Guesty, Lodgify, Hospitable and similar) with the same photos and reviews.
2. Google Vacation Rentals through an approved connectivity partner: free links, 5+ images required, 20+ recommended, accurate price and availability.
3. Vacation-rental structured data on the property page once the feed integration exists (Google documents it for sites connected to its vacation-rental program; check eligibility before building).

**AI search:** Google AI Mode now compares hotels and, for some US users, books through partners (August 2026). Build accurate entity and inventory data (names, live rates, amenities, policies, images) before any "AI SEO" content.

## Reasons to book direct (give one that costs little)

- **Flexible cancellation for direct, stricter for OTA,** explicitly tied to commission (r/bedandbreakfast, 4 upvotes).
- **Room choice and upgrades for direct:** "Those are for members who book direct." Hotel staff say direct bookers get upgrades and better locations when inventory is tight (r/hotels, 91, 63 and 52 upvotes). A guest switched an OTA reservation to direct for $12 more after learning this.
- **Service control:** direct guests can change dates and get exceptions; OTA guests must go through the OTA.
- **Welcome credit, late checkout, early check-in where available, stored details.**
- Avoid discounts as the default reason; first remove friction.

Show it on the home page, the booking engine and the confirmation email. A guest found a direct promo in an app's offers tab and said they would have booked every night direct had it been on the home page (r/hotels 55).

## Converting OTA guests, within the rules

- **Never divert a live OTA reservation.** Do not send links or contact details through OTA messaging; platforms strip and penalize it. Guests can read off-platform invitations as scams; in one 4,825-upvote thread the host who had invited a guest to "book directly and avoid Airbnb fees" later filed a damage claim.
- **After the completed stay,** contact only through data the guest gave you directly with permission: a check-in registration card with an opt-in box, Wi-Fi splash page, a QR code in the guidebook to a "returning guest" list, a hotel's own folio email where the law and OTA contract allow. Record the consent source and date.
- **Make the next trip easy:** "Your previous stay details are already on file."
- **Long stays:** one host spoke with a 9-month Airbnb guest after two weeks and moved them to a month-to-month lease: "we still wanted to make the same profit as before but we could remove the Airbnb fees." $7,750 a month, four years, up to nine months prepaid (r/airbnb_hosts, 764 and 343 upvotes). Safer version: raise it only when the booked term ends, book the renewal off-platform after the OTA stay closes, and check local tenancy law first (long stays can create tenant rights).
- **Returning corporate clients:** if a known account shows up on an OTA at a higher rate, a call can move them to the corporate rate; OTAs may still audit and charge commission (r/hotels, 56 and 29 upvotes).

## Four email flows before any newsletter

Revinate (2.8B hotel emails, 2025 data): small segmented lists under 5,000 converted at 0.51%, lists over 50,000 at 0.05%; abandoned booking 6.8%; cancellation recovery 5.8%. Intent beats calendar.

| Flow | Trigger | Content |
|---|---|---|
| Checkout and review | Checkout day | Thanks, neutral review ask, where to message about problems |
| Post-stay rebooking | 30 to 60 days after checkout, and again before the same season next year | Direct link, direct benefit, same-season dates |
| Abandoned booking | Booking engine abandon, 1 to 4 hours later | Dates still available, deep link, "reply if the policy or room choice stopped you" (no discount first) |
| Cancellation recovery | After a cancellation | Alternative dates, flexible option, contact |

Then narrow seasonal segments (families who came in summer, couples who came for an event), never "all guests". Wording in [scripts.md](scripts.md).

Vendor case: Bachcare NZ (2,000+ homes) reported +20% booking conversions and 4x recovered abandoned bookings after behavior-based segmentation (Klaviyo case, 2024 to 2025). Directional for a solo host.

## Repeat and loyalty for small operators

- Personal gestures for repeat guests: a gift card to a local restaurant and extra snacks (21 upvotes); avoid alcohol gifts when you do not know the guest.
- Reduced chores and fees are themselves a loyalty program: a host since 2016 who absorbs minor messes and asks for no chores reports most rentals now come from returning guests despite a platform slowdown (r/airbnb_hosts 582).
- Returning guests become partners: a repeat guest asked to shoot product photos during the slowest month (r/airbnb_hosts 281).
- Travel advisors: check in during the trip; clients book transfers, upgrades and even a second cruise from the first (r/travelagents 26). See [travel-advisors.md](travel-advisors.md).

## Social media for lodging (brief)

Social rarely fixes an empty calendar on its own. Facebook snowbird and direct-rental groups in South Florida drew 40 to 50 competing listings per request (r/airbnb_hosts 640). Use social for proof (real guest moments, seasonal views, amenity reels) that feeds the direct site and repeat guests. Content systems and platform mechanics: `organic-social`.

## Measurement

- **Filter bots before trusting traffic.** A 32-room boutique hotel found 22% of GA4 sessions were fake (18% from Eswatini); real conversion was 3.2%, not 2.5%; $4,200 of extra ads had been bought on fake growth. Fix: country and hostname filters, server-log cross-checks, report "qualified sessions" (relevant geography, 10+ seconds, 1+ pages), which were 60% of reported (r/hotels 35, 2026).
- **Report revenue by channel net of fees**, plus cancellation rate by channel, plus direct share in revenue.
- **Attribution for offline promotions:** unique codes per placement. A sales rep sold hotels coupon listings by asking what their highway billboard produced; owners could not say (r/sales, 589). Do not buy what cannot be tracked.
- **Google free links:** read Hotel Center reports for clicks and bookings; compare to paid campaigns separately.

Tricks most owners miss: direct is measured in revenue, not bookings; the free Google booking link is the cheapest direct channel and is ranked partly on price accuracy, so a wrong rate on your site costs placement; and the abandoned-booking flow outperforms any newsletter by more than 10x.
