# Measurement: tracking, attribution, MER and incrementality

The agent needs three layers and must keep them apart: **platform numbers** to optimize inside a platform, **analytics** (GA4, UTMs) to compare channels, and **business truth** (store orders, CRM, bank) to decide budgets. Never sum platform conversions: Meta claims 100, Google 80, the store had 120 orders, you have 120 (AgriciDaniel, coreyhaines31, MIT).

## Minimum measurement stack

1. Platform tags on every page (Google tag, Meta pixel, TikTok pixel).
2. Server events where available: Meta CAPI, TikTok Events API, Google Enhanced Conversions (web and leads). Free first: Google Enhanced Conversions for web, Meta automatic advanced matching and TikTok `ttq.identify` cost nothing. Browser-only tracking typically loses 10 to 30% (ad blockers, Safari cookie caps, cross-device). Declined-consent visitors are not recoverable and should not be.
3. UTMs on every paid link, in a fixed vocabulary (below).
4. Click IDs (gclid, gbraid, wbraid, fbclid, ttclid) written to hidden form fields at first touch and stored in the CRM.
5. CRM lead ID and stages: `Lead > Qualified > Booked or Opportunity > Won or Purchase > Revenue`, with gross margin when margins differ.
6. A daily table linking spend to qualified leads to sales, by campaign and creative.
7. A one-question "How did you hear about us?" on the booking form, checkout or intake call. It catches word of mouth, podcasts, DMs and the memorable touch.

Server-side options and 2026 prices (coreyhaines31, MIT): Google tag gateway free on Cloudflare (Google reports 11% more signals); Shopify native Google and Meta channels $0 (CAPI at Enhanced or Maximum data sharing); Zapier or Make webhooks to CAPI; Stape from $17/month; self-hosted sGTM about $90/month; Elevar from $225/month. Server-side mainly pays at volume: 21 of 31 audited Google ecommerce accounts lacked it (r/PPC 212); Tag Gateway gives small advertisers most of the benefit.

## UTM and naming spec

```
utm_source   = fixed platform token: google | meta | tiktok | microsoft | reddit | pinterest | nextdoor
utm_medium   = cpc | paid_social | display | video
utm_campaign = {goal}_{audience}_{yyyymm}          e.g. leads_broad_202611
utm_content  = creative or ad ID                    e.g. c14-objection-v1 or {{ad.id}}
utm_term     = search keyword only
```

Lowercase only, no PII, auto-tagging on (gclid) with manual UTMs not colliding (aaron-he-zhu, Apache-2.0). Meta dynamic parameters: `utm_campaign={{campaign.name}}&utm_content={{ad.id}}`. Put UTMs at PMax asset-group level so the CRM can compare lead quality by asset group. Give influencer creative its own campaign and UTM.

Ad names encode what you will want to filter later: `PP - p3 - vv100 - adc72 - lp53 - [post ID] - [launch date]` (brand, page, video number, copy number, landing page, post ID, date) (r/PPC 155), or `C14 | objection-price | ugc | lp-quiz | 2026-11`.

## Conversion setup rules

- **One canonical event per money action.** Lead forms count "One", not "Every". Purchase carries value and a single currency plus `transaction_id` for dedup.
- **Fire on confirmed success,** not the button click or an unguarded thank-you page that fires on refresh.
- **Primary vs secondary:** GA4 import plus native Google tag both primary can double conversions. Bid on the native Google Ads tag (faster, supports Enhanced Conversions) and keep GA4 imports secondary to watch gaps. Page views or pricing-page views as primary teach the bidder to buy browsers.
- **Bookings or qualified leads as primary;** bot form fills as primary train Smart Bidding toward bots.
- **Changing primaries resets learning** on every campaign using them: draft the change and time it off-peak.
- **Dedup on Meta and TikTok:** same `event_id` and `event_name` from pixel and server. Check Test Events for one "Deduplicated" row. Pass `eventID = purchase-{order.id}` in custom builds.
- **Verification discipline:** a tag firing is not a conversion arriving. GA4 DebugView and Meta Test Events are instant; Google Ads columns lag a day. Close every tracking task with a status: built, firing confirmed, arrival confirmed, or arrival pending (coreyhaines31).

## Symptom routing

| Symptom | Likely cause |
|---|---|
| Spend and clicks, zero conversions | Click-ID chain broken (cross-domain booking page losing `_gcl_aw`), tag on wrong step, consent mode broken |
| Way too many conversions | Duplicate senders, "Every" counting, thank-you page refreshes, GA4 + native both primary |
| Smart Bidding ignores conversions | Action set to secondary or not in campaign goals |
| "Sales says leads are junk" | Conversion fires on click or validation, not success; bots; no qualified event |
| Meta ROAS beats Google | 7-day vs 30-day windows, view-through, no refund adjustment on Meta |
| Plenty of leads, no customers | Feed CRM outcomes back; check speed to lead |
| Everything dropped overnight | Consent Mode v2 misconfigured (can drop Ads conversions about 90%, only about 40% recoverable), Shopify checkout script change (Additional Scripts removed from Thank you pages for all remaining stores on 26 August 2026), hosted CAPI plan limit, attribution window change |

**Discrepancy rules:** an Ads vs GA4 gap of 10 to 30% is normal; investigate above about 40%, direction flips, sudden changes or any platform at zero. Never judge the last 3 days (conversions post to click date with up to 72 hours lag; GA4 24 to 48 hours; GA4 imports +1 to 3 days). Consent Mode modeling needs about 700 ad clicks over 7 days per country and domain grouping; most small sites never qualify, so assume no modeled backfill.

## Attribution windows

- Meta defaults to 7-day click + 1-day view; view windows were cut in January 2026 and attribution updates moved reported CPA 30 to 50% overnight in one account (r/FacebookAds 67). Store the attribution setting next to every ROAS figure.
- Match the evaluation window to the buying cycle: 1 to 7 days for gifts, impulse and accessories; 14+ days for supplements, skincare and wellness; judge Meta lead-gen CPL over 14 to 30 days (operators). A 1-day click window gave "tighter, more predictable" results for impulse buys (r/PPC 160).
- Window mismatch inside Google (PMax on 7 days, Search on 30) distorts budget allocation (r/PPC 212).
- Reddit defaults to 28-day click + 1-day view: much more generous than most SMBs realize.
- Meta has no documented refund mechanism, so high-return stores structurally inflate Meta ROAS. Google conversion adjustments can retract or restate within 54 days.
- Meta overreported conversions 15 to 30% against server-verified results in one practitioner's accounts (r/FacebookAds 337).
- Import Meta cost data into GA4 (Admin > Data source > Connect to Meta); source and medium must match your UTMs; takes 24 to 48 hours.

## Business metrics

```
MER = total revenue / total paid media spend                     (ecommerce)
new-customer CAC = paid spend / new customers                   (from the store, not the platform)
blended CAC = total ad spend / acquired customers               (lead gen, from the CRM)
cost per qualified lead, qualified rate, close rate             (lead gen diagnostics)
contribution after ads = gross profit - ad spend - fees         (the number that pays rent)
```

Rules:

- Report platform-attributed and blended side by side every week.
- Separate brand from non-brand before celebrating ROAS: a 17.49x account was mostly branded terms (r/PPC 122). Separate new from returning customers: 24 of 31 audited accounts did not (r/PPC 212).
- Split blended numbers by country and campaign before deciding: about 3x blended hid Canada at 7 to 9x and a weak US (r/FacebookAds 121).
- Back-solve traffic vs conversion problems: implied clicks = sales / CVR. 55 sales at 4.7% and 17 sales at 1.5% both imply about 1,150 clicks a day: traffic held, conversion collapsed, so look at targeting expansion and the page, not bids (r/googleads 37).
- Review contribution margin (% and $) weekly. Cohort LTV by first product, month, country and channel: first product alone can mean 5x LTV differences; Black Friday cohorts stay weak (r/PPC 356).

## Incrementality on small budgets

Lift = exposed conversion rate minus control rate (4.2% vs 3.6% = 0.6 points; the rest would have happened anyway). A confidence interval straddling zero means the test was too small, not that ads do nothing.

| Method | When | How |
|---|---|---|
| Budget halving | Any size | Cut one channel's spend 50% for 2 to 4 weeks; if total new customers barely move, the spend was not incremental. At about $10k/month a 50% Meta cut left results unchanged (r/FacebookAds 277) |
| Brand pause | Sole bidder on your brand, strong organic | Pause brand Search 2 to 4 weeks; watch total brand conversions (paid + organic). Two pauses lost leads when competitors bid (r/googleads 58, 34) |
| Geo holdout | Several comparable regions, $1,000+/day, or a local business with 2+ separable areas | Turn ads off in matched regions for a full sales cycle, compare to forecast. Google's open-source [Meridian GeoX](https://developers.google.com/meridian/geox) reports lift, confidence intervals and incremental ROAS |
| Platform lift | Meta Conversion Lift via your rep; above about $100k/month start with audience exclusions | One practitioner says most brands overspend 25 to 35%+ on Meta; another found no gain over 1-day click |
| Holdout audiences | Retargeting, email, SMS | Hold 10 to 15% out of retargeting and compare |
| Pulse | Seasonal or uneven spend | On/off weeks in randomized time blocks |
| Post-purchase survey | Always | "How did you hear about us?" as triangulation |

For $10 to 50/day accounts there is too little signal for geo experiments; use budget halving, brand pause and the survey. Geo holdouts become practical at $1,000 to 5,000/day across several markets (research report inference). A large retailer that copied a famous ad shutdown restarted after 4 to 5 days each time, every 18 months (r/DigitalMarketing 562): plan the duration and success metric before pausing.

Also track net-new reach and its CPM weekly as a proxy for finding new buyers.

## Offline conversion import (lead gen)

- Send `Qualified`/`Disqualified` and sold or unsold values back to Google and Meta; train staff to attach the estimate and invoice to each CRM lead (r/DigitalMarketing 114, roofer to $2.2M revenue).
- Value ladder: low value for on-site behavior, medium for calls and forms, higher for contacted, actual deal value at close; then value-based bidding.
- The cheapest-CPL campaign closed at 2% while the most expensive was 3x more profitable (r/FacebookAds 187).
- Mechanics for Google Enhanced Conversions for Leads and Meta CRM events: [google.md](google.md#offline-conversions-and-enhanced-conversions-for-leads), [meta.md](meta.md#capi-and-event-match-quality).
- B2B clicks close in 60 to 180 days: reconcile monthly and let the CRM win.

## Bot and invalid traffic checks

- CTR above 10% on Meta (one account showed 48%), or a 40 to 50% gap between link clicks and landing page views: bot traffic (r/FacebookAds 70).
- Cheap delivery can be junk: Meta CPM about $0.50 with $0.07 landing page views while page CVR fell from 5.5% to 0.5% (r/FacebookAds 58).
- Watch replays for sessions with no scroll and no clicks; check country mix (Thailand was 46% of Meta traffic in one account over 5 days).
- Keep bots out of optimization: optimize purchases or offline conversions; Cloudflare WAF; keep bots out of remarketing pools.

## Reporting

**Weekly scorecard (8 to 10 numbers):** spend, platform conversions, CRM qualified leads or new customers, cost per qualified lead or new-customer CAC, close rate, MER or blended CAC vs target, contribution after ads, top wasted terms or placements, search impression share lost to budget vs rank, new concepts launched and winners found.

**Friday readout under 200 words** (coreyhaines31): results vs target per program (green, amber, red), top 2 to 3 movers each with cause and confidence, next week's calls labelled HOLD, FIX, TEST or INVESTIGATE. INVESTIGATE overrides the rest when data is untrustworthy. Money-moving changes await owner approval. Close with Facts / Hypotheses / Missing data; write MISSING instead of estimating.

**Claim labels on every client-facing finding:** Verified (pulled live, reconciled to a total), Inferred, Stale (from a document or the client, with its date). Test before sending: could the owner disprove this in a minute with their own access?

**Free reporting stack:** daily exports into one sheet tab per channel, then Looker Studio blended on date (r/PPC 538).
