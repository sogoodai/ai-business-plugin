# Account audit checklist

Every control gets one of four states (AgriciDaniel and coreyhaines31 scoring, MIT): **PASS**, **FAIL**, **UNKNOWN** (no access or data; lowers coverage, never the score), **N/A** (leaves both denominators). Never pass by default. Coverage 80%+ = graded; 60 to 79% = provisional; under 60% = no score, list what access is missing.

Weights: critical 5, high 3, medium 1. `category health = 100 x sum(pass weights) / sum(known weights)`. One root failure is one failed control, not a penalty per symptom. Category weights: Meta measurement 25, creative 25, structure 20, audiences 15, delivery 10, policy 5. Google measurement 25, waste 20, structure 15, keywords 15, creative 15, settings 10. A verified veto (broken tracking, double counting, false claim, policy violation) caps the overall score at 59.

Pull 30 to 90 days of data, the change history and the search-terms report before scoring. Without a search-terms report, name zero negatives.

## Business and economics

| ID | Control | PASS rule | Weight |
|---|---|---|---|
| B1 | Allowable CAC defined | Written number derived from margin and repeat rate | Critical |
| B2 | Real outcome defined | Booked, paid or won event named and countable in CRM or store | Critical |
| B3 | Learning floor fits budget | Each campaign's budget can produce its platform's minimum (30 conversions per Google read; about 50/week per Meta ad set or a consolidation plan; 10x CPA/day for TikTok Smart+) | High |
| B4 | Channel count fits budget | Under $2,000/month: 2 channels or fewer | Medium |
| B5 | Blended view exists | Weekly MER or blended CAC from business data | High |

## Tracking (all platforms)

| ID | Control | PASS rule | Weight |
|---|---|---|---|
| T1 | Test conversion recorded | A real test submission or order arrived in each platform within the expected lag | Critical |
| T2 | One canonical event per money action | No duplicate primaries (GA4 import + native both primary = FAIL); lead counting "One" | Critical |
| T3 | Fires on success | Thank-you state or server confirmation, not button click | Critical |
| T4 | Deduplication | Pixel + server share `event_id` and exact `event_name`; Test Events shows "Deduplicated" | High |
| T5 | Meta EMQ | Purchase or Lead EMQ 6+ (target 8+) | High |
| T6 | Value and currency | Purchases carry value and one currency; `transaction_id` set | High |
| T7 | Click IDs reach the CRM | `?gclid=test` submission stored in CRM; hidden fields for gclid/gbraid/wbraid/fbclid | High |
| T8 | Offline outcomes flow back | Qualified, booked or won imported to Google and Meta (lead gen) | High |
| T9 | UTMs | Every paid link tagged, lowercase fixed vocabulary, no PII | Medium |
| T10 | Windows documented | Attribution window stated next to every ROAS; Google campaigns on consistent windows | Medium |
| T11 | Cross-domain | Booking or checkout on another domain preserves click IDs | High |
| T12 | Form delivers | A test submission reaches the inbox or CRM, not just a success message | High |
| T13 | Bot filter | Honeypot or validation on forms; Cloudflare or equivalent if bot signatures exist | Medium |

## Meta

| ID | Control | PASS rule | Weight |
|---|---|---|---|
| M1 | Structure matches budget | No ad set getting under about 1 expected conversion a day without a consolidation reason | High |
| M2 | One offer per campaign | Bundle, BOGO, sale and evergreen not mixed in one campaign | Medium |
| M3 | Concept diversity | 3+ materially different angles live per campaign (not hook-only variants) | Critical |
| M4 | Creative cadence | New concepts launched in the last 14 days, scaled to budget (4+/week at $50/day+) | High |
| M5 | Ads within ceiling | Active ads at or below daily budget x 14 / (2 x target CPA) | Medium |
| M6 | Fatigue | No ad with CTR down 30%+ from peak still taking over 20% of spend; prospecting 7-day frequency under about 2.5 | Medium |
| M7 | Placements checked | Placement breakdown reviewed; Audience Network not taking spend with abnormal CTR | Medium |
| M8 | Account-level AI toggles | Advantage+ creative enhancements, "test new optimizations", AI translations, auto music reviewed and set deliberately; rechecked after duplicates | High |
| M9 | Existing-customer control | Acquisition campaigns cap or exclude existing customers; Audience Segments report reviewed | High |
| M10 | Bid strategy fits data | No cost cap or ROAS goal under 50 conversions/month; caps set from known CPA | High |
| M11 | Lead form quality | Higher Intent form, 1 to 3 qualifiers or a non-autofill field; qualified event imported | High |
| M12 | Speed to lead | Median first response under 5 minutes on form and message leads (sample 10 leads) | Critical |
| M13 | Learning resets | No more than 1 significant edit per ad set per week; budget moves 20% or less | Medium |
| M14 | Special ad category | Housing, employment, financial and political ads in the right category | Critical |
| M15 | Sensitive names | No audiences or custom conversions named after health or financial traits | Critical |
| M16 | Account safety | 2FA on all admins, backup Business Manager pre-shared, prepaid or monitored billing | High |
| M17 | Post IDs preserved | Winners promoted by post ID; social proof kept | Medium |

## Google

| ID | Control | PASS rule | Weight |
|---|---|---|---|
| G1 | Location option | "Presence" on every campaign | Critical |
| G2 | Networks | Search Partners and Display expansion off on Search (unless deliberately tested with results) | High |
| G3 | Auto-apply | All auto-apply recommendations off; change history shows no unapproved "Google Ads Team" changes | Critical |
| G4 | Automated assets | Account-level automated assets and Location Manager data reviewed and off unless proven | Medium |
| G5 | Brand split | Brand in its own campaign and budget, not on Max Conversions or uncapped tCPA | High |
| G6 | PMax brand exclusion | Brand exclusions or negatives on PMax; brand vs non-brand split before judging | High |
| G7 | Primary conversions | One primary per goal; no page views, no bots, bookings or qualified leads for lead gen | Critical |
| G8 | Wasted spend | Search terms with 3+ clicks, zero conversions and irrelevant intent under 10% of spend over 30 days | High |
| G9 | Negative lists | Shared lists exist (jobs, free, DIY, research) and were updated in the last 30 days | Medium |
| G10 | Match type vs data | Broad match only where the campaign has 30+ conversions/month and smart bidding | High |
| G11 | Bid strategy vs volume | Target strategies only with 30+ conversions/30 days; targets within 20% of trailing actuals since 17 August 2026 | High |
| G12 | Target and cap conflict | No campaign with a target and a binding budget cap | Medium |
| G13 | RSAs | 2 to 3 RSAs per ad group, 8+ unique headlines; pins limited to 1 to 3 | Medium |
| G14 | Disapprovals | No disapproved or limited assets unnoticed for over 7 days | Medium |
| G15 | Call tracking | Calls counted by duration or outcome; DNI on site; call details reviewed | High |
| G16 | PMax hygiene | Sourced videos off; own video supplied; placement report reviewed; Final URL expansion controlled | Medium |
| G17 | AI Max | Only as an experiment with weekly search-term review | Medium |
| G18 | Customer lists | Customer Match uploaded and used as signal or exclusion | Medium |
| G19 | Budget safety | Account-level budget on invoiced accounts; daily budget entries checked against monthly plan | High |
| G20 | Feed (ecommerce) | Merchant Center diagnostics clean (GTIN, price match), titles front-loaded, refresh daily+ | High |

## TikTok, Pinterest and others

| ID | Control | PASS rule | Weight |
|---|---|---|---|
| X1 | Learning budget | Smart+ at 10x CPA/day or more; Pinterest Performance+ at 5x CPA/day and 50 conversions/week | Critical |
| X2 | Creative count | TikTok 6+ creatives, Pinterest 10+ per ad group | High |
| X3 | Edit discipline | No disruptive edits in TikTok's first 7 days; Pinterest 2 or fewer change rounds per week | Medium |
| X4 | Pangle and audience networks | Off unless tested with real conversions | Medium |
| X5 | Attribution honesty | GMV Max and Reddit (28-day click + view) reported next to blended numbers | High |
| X6 | Events API | `event_id` dedup and `ttclid` passed server-side | Medium |

## Operations

| ID | Control | PASS rule | Weight |
|---|---|---|---|
| O1 | Owner holds access | The business owns the ad accounts and pixel; agency has partner access only | Critical |
| O2 | Change log | Every change recorded with date, reason and expected effect | Medium |
| O3 | Weekly cadence | Search terms, placements, pacing and disapprovals checked weekly | Medium |
| O4 | Policy matrix | Vertical x country x platform checked for regulated offers | High |

## Output format

1. Score per category and overall, with coverage and the list of UNKNOWNs.
2. The 3 biggest problems in money ("$X/month on Search Partners with 0 conversions"), each with the fix and expected effect.
3. Safe to do now vs needs owner approval (anything touching budgets, bids, targeting or live ads).
4. Facts / Hypotheses / Missing data.

Wasted-spend workflow for G8: pull 30 to 60 days of search terms and placements; flag spend above target CPA with zero conversions after the break-even CVR check; group by reason (intent, geography, junk placement, competitor, job seekers); split into "safe to add now" vs "check before excluding" (brand-adjacent, research queries); total the last-period savings per list (coreyhaines31). Optional: split a CPA spike into shares by cause (for example 73% one fatigued ad set, 18% broad-match drift, 9% slower page).
