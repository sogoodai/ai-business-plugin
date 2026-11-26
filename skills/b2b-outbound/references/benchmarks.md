# Benchmarks

There is no single cold-email reply benchmark. Vendors use different denominators: Smartlead reports percentiles across senders; Instantly reports campaign and platform interactions; Hunter measures sequence replies per recipient; Belkins divides unique replies by all emails sent. Pick the one whose denominator matches yours, keep it, and never average across them. All vendor datasets are customer cohorts with a commercial interest in outbound looking good. Sources: [sources.md](sources.md).

Store at least four separate reply metrics, or a tool migration will look like performance doubling or halving:

```
delivered reply rate     = replies / delivered emails
sequence reply rate      = contacts who replied / contacts sequenced
positive reply rate      = positive replies / contacts sequenced
meeting rate             = meetings booked / contacts sequenced   (and held / booked)
```

## Cold email reply rates by source and year

| Metric | Typical | Strong | Source, data period |
|---|---|---|---|
| Reply rate, sender percentile | 0.74% median | 1.43% p75; 2.63% p90; 3.85% p95 | Smartlead State of Cold Email 2026, 850M+ emails, H1 2026, senders with 500+ emails |
| Reply rate, campaign or platform | 3.43% average | 5.5%+ top quartile; 10.7%+ top 10% | Instantly Benchmark Report 2026, 2025 data |
| Share of replies from follow-ups | 42% | | Instantly 2026 (58% come from email 1) |
| Campaign reply rate | 1.5% median | not published | Woodpecker, last 90 days of 2025, 56,614 campaigns, page updated Aug 2026 |
| Sequence reply rate | 4.5% average | 6.2% for 21 to 50 recipient sequences | Hunter State of Email Outreach 2026, 31M emails sent in 2025 |
| Strict reply rate (replies / all emails) | 0.45% | | Belkins, 7.53M emails, 34,393 replies, 2025, pub. June 2026 |
| Reply rate | 1.13% median; 2.72% average | 12.96% top 10% | Lemlist, Oct 2025 to Nov 2026 |
| Reply per prospect, services sellers | 4.9% median | 7.1% top quartile | Smarter Outbound, Sept 2026, 277,036 prospects |
| Positive reply per prospect | 0.79% median | 1.36% top quartile | Smarter Outbound 2026 |
| Sends per meeting | 344 average | | Gong, 28M+ emails, 2025 |
| Bounce rate | 1.54% median | worst quartile from 3.21%; 2% danger line | Smartlead H1 2026 |

**Trend:** reply rates fell from about 7 to 8% in 2020 to 2022 datasets to roughly 3.5 to 5.8% in 2024 to 2025 datasets (compiled by coreyhaines31 from several vendor reports, MIT). The gap between average and excellent is widening, and it comes from targeting.

**Funnel model on a static list** (estimate, not measured): 1,000 contacts, about 34 replies (3.4%), 10 to 15 positive, 5 to 8 meetings, 1 to 2 customers. Roughly 100 to 200 contacts per meeting; signal-based segments often need 30 to 60.

## What correlates with replies (Hunter 2026, 2025 sends unless noted)

| Variable | Better | Worse |
|---|---|---|
| Recipients per sequence | 21 to 50: 6.2% | 500+: 2.4% |
| Contacts per company | 1 to 2: 5.1% | 3+: 3.5% |
| Open tracking | Off: 7.4% | On: 4.4% |
| Emails in sequence | 3: 6.8% | 1: 3.3% |
| Personalization | 2 custom attributes: 5.6% | None: 3.6% |
| Editing | Manually edited: 5.2% | Fully automated: 4.4% |
| Sends per inbox per day | 20 to 49: 5.7% | Overall 4.5% |
| First email length (Smartlead 2026) | Under 50 words: 1.47% | 100 to 149 words: about 1 per 97 contacts |
| Step decay (Smartlead 2026) | Email 1: 1.18% | Email 7: 0.33% |

## LinkedIn

| Metric | Typical | Strong | Source |
|---|---|---|---|
| Invitation acceptance | 28.5% average | | Expandi, 13.2M requests, May 2025 to Apr 2026 |
| Invitation acceptance | 27.3% median; 29.4% average | 53.9%+ top 10% | Lemlist, Oct 2025 to Nov 2026 |
| Message reply | 10.4% average | | Expandi, 6.7M messages |
| Message reply | 6.6% average | 19.9%+ top 10% | Lemlist |
| With note vs without | Acceptance 25.3% vs 27.6%; reply 8.2% vs 5.3% | | Belkins, 11.5M requests, 2025 |
| Meetings per invite | 0.54% | | Reachium 2026 (concentrated sample) |

## Calling

| Metric | Typical | Strong | Source |
|---|---|---|---|
| Connect rate | 5.4% | 13.3% top quartile | Gong, 300M calls, pub. 2024 |
| Connect rate | 9.1% median; 13.8% average | 34.1%+ top 10% | Lemlist, Oct 2025 to Nov 2026 |
| Opener success | "Bad time?" 2.15% | Permission 11.18%; peer 11.24% | Gong 2024 |
| Meetings per connect | Parallel dialer 3.8% | Power dialer 6.4% | Orum 2025 |
| Callback meeting likelihood | | 4x a normal connect | Orum, 2024 data |
| Seller talk share | 60% average | Won deals 57% vs lost 62% | Gong, 326K calls, Mar 2025 |

## Signal and AI cases (vendor stories, treat magnitude as promotional)

| Claim | Source |
|---|---|
| Job-change plays 17%+ reply, 10% meeting rate | Common Room, Jan 2025, its own play |
| AI-recommended contacts booked meetings at 2.5x cold contacts; replies +50%; lead-to-opportunity time -35%; closed-won pipeline 2.4x | Common Room, Superhuman case |
| 71 meetings, 32 SQOs, $610K pipeline, $44K closed-won in 4 to 5 months | UserGems, NetSPI case, Jan 2026 |
| 3x call volume, 2x email reply rate, 60% of North American pipeline | Salesforce, Perk case |
| 69% of US decision-makers bothered by AI-written email | Hunter 2026 buyer survey |
| AI-hyperpersonalized LinkedIn: 12% lower acceptance, flat replies | Expandi 2026, within-account |

## Operator-reported numbers (Reddit, single sources)

| Situation | Result | Thread |
|---|---|---|
| Agency, 43 campaigns: free deliverable instead of a call ask | 0.9% to 3.4% replies in 2 weeks | r/b2bmarketing 170 |
| 14 client campaigns by vertical | Cleaning 9 to 11%; staffing 8 to 12%; MSP 7 to 9%; HR tech 7 to 9%; ecommerce agency 6 to 8%; SaaS 4 to 6%; healthcare IT 3 to 5% | r/b2bmarketing 41 |
| Solo founder, 70 emails a day | About 4% reply, half interested, a quarter of those close | r/LeadGeneration 36 |
| Video editor, 600 emails | 21 replies (3.5%), 9 calls, 3 clients, $13.2K in a month | r/b2bmarketing 63 |
| Personal outreach vs automated | 1 client per 50 creative approaches vs 1 positive reply per 200 to 300 automated emails | r/LeadGeneration 90; r/EntrepreneurRideAlong 154 |
| Positive replies by industry | Construction 1 per 260 emails; agencies 1 per 120 | r/agency 32 |
| Cold email as a channel vs search ads | $0.19 per email sent, $1.92 per signup vs $10 a click on search | r/indiehackers 45 |
| SaaS operator benchmarks (OP sells outreach software) | Reply 3 to 5%, positive 1 to 2%, booking 0.5 to 1%, close 20 to 30% of booked calls | r/microsaas 54 |
| Blast that failed | 5,000 contacts, 6 replies, 1 client | r/digital_marketing 225 |
| LinkedIn funnel | 2,000 requests, 17.65% accepted, 35% of accepted replied, 10 clients | r/b2bmarketing 68 |
| LinkedIn problem DMs | 15 to 20 a day gave 2 to 3 customers a month | r/LeadGeneration 28 |
| Solo cold calling | 50 dials a day, 2.5% of dials became sales, about $120K a year | r/Entrepreneur 1838 |
| Missed call to LinkedIn note | 14.1% responses vs 2.3% voicemail callbacks | r/Entrepreneur 480 |
| Managed outbound ramp | 2 to 7 meetings in month 1, 10 to 15 in month 2, full speed month 3; 32 to 35 meetings over 3 months at 15% close = 4 to 6 clients | r/agency 88 (OP sells it) |
| Lead-gen agency at GBP 8K a month | About 4 qualified meetings a quarter; one in-house SDR did better by month 2 | r/b2bmarketing 128 |

## How to read your own numbers

| Symptom | First suspect | Check |
|---|---|---|
| Replies far below your chosen benchmark, few OOOs | Deliverability | Seed test, Postmaster, bounces, tracking on? |
| Replies normal, positives low | Offer or ICP | Read 20 replies; group the no-reasons |
| Positives fine, few meetings | Reply handling | Time to first response, two-times format |
| Meetings fine, low show | Booking quality | Who booked, title fit, reminders, pre-read |
| Shows fine, no opportunities | Discovery or targeting | Champion, authority, budget fields |
| LinkedIn acceptance low | Targeting and profile | Profile, list fit, note or no note |
| Acceptance fine, no conversations | Message 1 after acceptance | Shorter, a question about their process |
| Connect rate under 5% | Phone data | Direct dials, mobile coverage, time windows |
