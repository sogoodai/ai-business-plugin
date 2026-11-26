# Capture: growing a list that buys

The target is not "maximize submissions". It is incremental first-order or first-visit contribution after incentive cost:

```
allow_discount if incremental_conversion_lift x contribution_margin > discount_cost + expected_future_discount_leakage
value per 1,000 visitors = incremental first purchases x contribution - discount given to people who would have bought anyway
list growth per month = new consented contacts / list size at start of month   (1 to 3% "healthy", weak source)
opt-ins needed per day = target list size / days   (5,000 in 12 months = about 14 a day; ai-restaurant-claude, MIT)
```

Store `signup_source`, first product or service and consent text version on every contact from day one. Dedupe: about 25% of discount signups are repeat people re-claiming the code (13-pt comment, brands with 10k+ signups a day).

## Rates by method

| Method | Rate | Evidence |
|---|---|---|
| Website popup, median | 1.30% (Poptin, 2,305 popups, 2026); 2.3% (Klaviyo 2026) | vendor data |
| Website popup, good | 2.67% p75 (Poptin); 3%+ target (Klaviyo) | vendor |
| Discount / gamified / multi-step popup | 8.62% / 10.15% / 5.64% average | Wisepops customer base, selection effects |
| Exit intent / click-triggered | 3 to 10% / 10%+ | coreyhaines31 popups (MIT), uncited |
| Spin wheel | 9% | operator, 160-pt thread |
| Tested popup program | 2.8% to about 7%, best 8.2%, after 50+ variants in 7 months | operator, 28-pt thread |
| Lead magnet landing page | checklist or quiz 30 to 50%, paid landing page 10 to 25%, exit popup 2 to 5%, sidebar 0.5 to 2% | coreyhaines31 lead-magnets (MIT), uncited |
| Pinterest to free resource | 15,247 visitors to 1,847 subscribers (12.1%) in 90 days, then 23 sales of a $297 course | operator, 155-pt thread |
| SMS opt-in at checkout | 5 to 15% of customers | finsilabs (MIT), uncited |
| Email-to-SMS opt-in | 5 to 25% | coreyhaines31 sms (MIT), uncited |
| Double opt-in confirm rate | 60 to 80%; under 50% = poor source | AgriciDaniel (MIT), uncited |

No published rate exists for Wi-Fi portal or receipt QR capture. Measure your own with a unique QR or SSID per location and context.

## Website popups

Defaults (coreyhaines31 popups, MIT, plus 2026 data):

- **Trigger on engagement:** 30 to 60 seconds, 25 to 50% scroll, second page view (21-pt comment: "works well, reduces bounces"), or exit intent after 2+ product views (7-pt comment). Wisepops tests: delaying 20 to 50 s lifted capture 20 to 43% and cut bounce up to 45%.
- **One operator rule:** delay = average time on page minus 5 to 10 seconds; positive change for 3 of 3 clients (126-pt thread). A 13-pt commenter disputes any universal timing; new and returning visitors behave differently.
- **Exceptions:** if an ad promised the code, show it immediately and keep it findable as a sticky tab after dismiss (13-pt comment). A persistent teaser bar gave one operator the best opt-in-to-purchase rate.
- **Show twice across the journey, differently:** landing popup once, plus a product-page slide-out until subscribed; subscribers saw about 2 forms before signing up (181-pt thread).
- **Once per session, remember dismissals 7 to 30 days, never on checkout, never after signup or purchase.** Mobile: bottom slide-up, never full-screen before content (Google intrusive interstitial rules).
- **Copy:** "Get [result] in [timeframe]"; first-person CTA ("Get my 10% off"); polite decline ("No thanks"); never guilt ("No, I don't want to save money"). In November: "Do you want 10%? Subscribe to our mailing list for exclusive Black Friday Deals" beat wordier versions (181-pt thread).
- **Ask four questions after the email, not name or phone:** "What are you interested in?", "What matters most to you in what you're interested in?", "How many do you own?", "When are you looking to purchase?" About 96% completion; feed answers to segments (181-pt thread).
- **Put the inline form where people actually scroll.** One site's median scroll depth was 25% and the signup sat at the bottom, seen by 10% of visitors; moving it into view of 50%+ tripled signups (132-pt thread).
- **Kill test:** check purchase conversion and AOV with and without the popup. One operator team avoids popups and spin wheels because they lowered conversion and AOV (5-pt reply, unquantified). Discount popups can just move full-price buyers to a code.
- **Value exchange before discount** when the store converts without one: restock alerts, care guide, early booking access, cancellation list, "text me when weekend slots open" (research 2026).

## In person and on premises

- **QR with a job, not "join our newsletter"** (research 2026): table tent "join and get dessert next visit"; mirror or station "rebook and get your care guide"; receipt "review or loyalty signup"; packaging insert "Join our VIP list" (NX, MIT). One QR per placement so attribution survives.
- **Tablet or counter signup at checkout:** 10 to 15% off next visit; capture email, phone with separate SMS box, optional birthday (AgriciDaniel local-business template, MIT).
- **Wi-Fi portal with an explicit, unticked opt-in.** Logging in to Wi-Fi is not marketing consent.
- **Booking and online-order flows:** add a separate, unticked marketing box; the booking itself only covers reminders.
- **Pre-opening and events:** restaurants collected 1,200 signups at about $0.50 each over 45 days before opening (Debox agency case 2025). A giveaway for an item from an upcoming drop, pushed in Instagram Stories, drove 1,200 entries (334-pt thread). Tag event signups by postcode and intent so party guests don't swamp the first campaign.
- **Shows and markets:** when someone asks how you make it, "Oh, some day I will write a book. Would you like to sign up for my email list?" (38-pt comment).
- **Owned community:** a pet brand recruited 11,000 Discord members in under a year through social, Reddit and email; members contributed designs and content (103-pt thread; niche fit matters).

## Marketplaces and platforms (capture within the rules)

- Amazon, Etsy, TikTok Shop and Udemy restrict buyer contact. Use inserts, an owned site and content off-platform; never mine order data for marketing against terms.
- Udemy instructors route students to an educational blog that captures email; one calls email their most effective channel (26-pt thread). Udemy pays 97% on instructor-driven sales vs 37% on marketplace-driven (Udemy terms 2026), so the owned list is worth far more per sale.
- TikTok Lives three times a week sent repeat viewers to an email list while Live gifts paid pennies (18-pt thread).

## Why build it early

- A small list was the only source of first-week orders when Meta rejected a new store's ads for months (6-pt comment).
- A dropshipper with 3,000+ subscribers from a signup coupon made $200 to $700 per newsletter (1,260-pt thread).
- A food truck that emails 2,000+ people weekly chooses paid venues by audience size it cannot reach alone (operators report).

## Owner questions before launching capture

1. What do we promise in exchange, and can we deliver it in the first message?
2. Is a discount affordable on first-order margin? What is the floor product it may not apply to?
3. Which countries are visitors from (decides opt-in wording and unticked boxes)?
4. Will SMS be collected separately, with its own disclosure?
