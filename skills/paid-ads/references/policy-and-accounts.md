# Policy, restricted verticals and account safety

Policy changes what optimization is available, and a ban erases pixel history, audiences and learned delivery. Treat policy as a gate before campaign creation: check (vertical x country x platform), not one global "restricted" flag. Policies change often; fetch the live page before giving a definitive answer and say which date you checked.

## Special and restricted categories

### Meta special ad categories

Categories: **Financial products and services** (replaced "Credit"; mandatory for US-related financial ads since early 2025), **Employment**, **Housing**, and **Social issues, elections or politics** ([Meta Marketing API, special ad category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category); summaries by [Jon Loomer](https://www.jonloomer.com/special-ad-categories-meta-ads/), 2025).

Typical restrictions for housing, employment and financial ads (verify live; secondary sources differ in detail):

- Age fixed at 18 to 65+, all genders, no exclusions.
- Location: at least a 15-mile (25 km) radius around a point in the US, no ZIP code targeting; other countries can differ.
- No lookalikes; most detailed targeting and exclusions removed; Special Ad Audiences reported deprecated in 2026.
- API: restrictions enforced with hard errors; from v26.0, creating these ad sets with relaxable non-broad targeting requires `targeting_automation.advantage_audience` set explicitly to 0 or 1.
- EU: Meta stopped political, electoral and social issue ads in the EU from October 2025 under the TTPA regulation.

Who gets caught: mortgage brokers, insurance, debt or credit repair, loans, BNPL offers, recruiting and staffing (even a "we're hiring" ad), real estate, rentals, home-service financing offers ("0% financing on a new roof" can count as a financial product). Misclassification costs: one account had an ad wrongly classified as financial by a Meta employee's change; ads re-entered learning and ROAS fell 80%, with compensation denied (r/FacebookAds 72). Check account history for who changed the category.

Working inside the category: creative and copy become the targeting (name the audience in the hook: "Nurses in Phoenix:"), use a wider geo with a local hook, use Advantage+ audience, and qualify in the form.

### Meta sensitive data rules

From 2 September 2025 Meta proactively restricts custom audiences and custom conversions that suggest health conditions (arthritis, diabetes) or financial status (credit score, high income). Event and audience names must describe business actions: `Lead`, `QualifiedLead`, `AppointmentBooked`, `Purchase`. For med spas, clinics, therapy-adjacent coaching and supplements: no condition-revealing audiences, URL parameters or event names; copy talks about the service, never implies you know the viewer's condition ("Are you depressed?" style personal attributes are rejected under Meta's personal attributes rule).

### Google

- **Personalized-ad restrictions:** housing, employment and consumer finance in the US and Canada cannot target by age, gender, parental status, marital status or ZIP code; advertiser-curated audiences are blocked for sensitive-interest categories ([Google](https://support.google.com/adspolicy/answer/143465); updated June 2026, [Google](https://support.google.com/adspolicy/answer/17135641)).
- **Certifications required** for categories including certain healthcare and medicines, financial services in many countries, gambling, and addiction services ([Google](https://support.google.com/adspolicy/answer/16114090), [healthcare policy](https://support.google.com/adspolicy/answer/176031)).
- **Other restricted businesses** (locksmiths, garage door, pest and similar high-fraud local categories in some regions often need advanced verification) ([Google](https://support.google.com/adspolicy/answer/6368711)).
- **Advertiser verification** is required for most accounts; unverified accounts stop serving.
- **Destination review:** Google reviews the landing page, not just the ad. Vague ad copy pointing at an openly crypto page risks disapproval or suspension; say "cryptocurrency" plainly, keep claims accurate and describe the service, not returns (r/PPC 345). Identical ads got different limitations depending on keywords and audience: treat those as diagnostic variables.
- **Weapons-adjacent:** a paintball park took repeated "weapons" strikes on Google and moved most budget to Meta (r/GoogleMyBusiness 253).

### TikTok

Country-specific matrix for legal, financial, healthcare and other services, updated October 2026. Example: French prescription-medicine ads are not allowed; some OTC medicines and medical devices may be allowed with certification and 18+ targeting ([TikTok](https://ads.tiktok.com/resources/help/article/tiktok-ads-policy-other-products-and-services), [healthcare](https://ads.tiktok.com/resources/help/article/tiktok-ads-policy-healthcare-pharmaceuticals)).

### Claims and content rules that apply everywhere

- No fake or sentiment-conditioned reviews or testimonials (FTC rule effective 21 October 2024); no fabricated before/after; real before/after only with consent, matched lighting and a typical-results disclosure.
- No guarantees of client-controlled outcomes (income, weight loss, exam scores).
- Disclose paid creator relationships (partnership ad labels).
- Alcohol: 21+ in the US, 18+ or more by country; no targeting minors anywhere for restricted products.
- "Google Guaranteed" wording in ads or scripts is outdated since the October 2025 move to Google Verified.
- Weight loss, cosmetic procedures and supplements: no body shaming, no "before" images that imply the viewer's body, no unapproved health claims.

## Preventing bans and restrictions (Meta)

Operators report these patterns (several are from 2022 and may be dated; they cost nothing to follow):

- **New ad account:** spend small at first (one 2022 operator ran $1/day page likes until 1 to 2 successful billings before conversion campaigns, after instant bans going straight to conversions). Raise budgets gradually; no bulk toggles or mass publishes within 1 to 2 minutes.
- **One card per ad account;** simultaneous charges on a shared card triggered a disable. Never let a card expire or a payment fail on an active account (a card change led to a ban in one `ecommerce-brand` case).
- **Never recreate a disabled account's campaign with the same Page in the next ad account of the same Business Manager:** the new account was banned immediately (r/FacebookAds 140). Fix the cause and appeal first.
- **Admins' personal profiles matter:** a drug joke posted on an admin's personal profile triggered a 30-day ad suspension (r/FacebookAds 58). Every admin uses 2FA and a real, long-lived profile.
- **Bought followers or engagement** risk restriction and pollute audience data.
- **Franchise and multi-client setups:** pre-creating about 15 unused ad accounts for franchisees got all of them disabled with no reactivation; each franchisee creates its own account and grants your Business Manager access (r/PPC 187).
- **AI agents with write access:** one advertiser gave an AI coding agent write access to budgets and publishing and got a permanent ban after about a week (cause disputed); another agent paused the best keyword at 2 am citing "creative fatigue" from a scraped post. Read-only by default (see below).
- **Do not depend on one platform:** a business selling through Facebook groups with 600,000 members lost 90% of orders when the groups were banned and went bankrupt; it had no email list. Build the list from day one.
- **Backup:** pre-share Pages, pixels and ad accounts with a backup Business Manager before you need it. A year-old backup BM was capped at $50/day against normal spend of $2,000 to 3,000/day (r/FacebookAds 214), so keep it lightly active.

## Recovering a restricted Meta account

1. **Identify the restricted layer:** ad account, Business Manager (portfolio), Page, or a person's profile. Requesting review of the ad account does nothing if an admin's profile is the restricted asset.
2. **Read the reason** in Account Quality (now inside Business Support Home in many accounts). Check change history for the action that preceded it.
3. **Fix the cause first:** edit or remove the violating ads, correct the special ad category, update the landing page, remove the admin who triggered it.
4. **Request review** with a short, factual statement of what happened and what you changed; provide ID if asked. Guides report a 180-day window and a limited number of review attempts; reviews often complete in about 48 hours (secondhand, unconfirmed).
5. **Escalate** through business support chat (available to many advertisers, or via Meta Verified for business), with ticket IDs, screenshots and a written timeline. Keep every support exchange in writing.
6. **Meanwhile:** run another channel; do not open a new account to dodge the restriction ("circumventing systems" is a separate, harsher violation).

Billing protection:

- Fund Meta with prepaid top-ups every few days, not an open credit line: one account lost $112,311 to fraudulent spend in under 30 minutes despite 2FA, with no refund after 26 days; a card-issuer dispute recovered money in another case where Meta took 12 months to respond (r/FacebookAds 144).
- A disabled account billed over $1,000 after the "ads will stop" email: check that billing actually stopped.
- Overspend refunds: document abnormal days (one account spent $65k on a $30 to 40k/day baseline with no extra sales) and claim them; one operator recovered about 70% of over $100k across 5 to 6 incidents (r/FacebookAds 182).
- Ads stuck in "error": duplicate and relaunch; 6 of 10 recovered at $50/day (r/FacebookAds 136).

## Google account problems

- **Account under review with zero spend for 12 days:** submitting the account-wide Daily Spend Limit increase form, citing business expansion, restored delivery the next day (r/googleads 51).
- **Merchant Center misrepresentation:** $2k on an agency failed; a single lawyer's letter got reinstatement within about a month (r/googleads 16). Before appealing: visible returns, shipping, contact address and phone, real "about" page, prices matching the feed, no fake urgency.
- **Hijacked account or MCC:** after Google restores access, re-check linked managers (a hacker MCC was still attached) and duplicate legitimate campaigns Google removed. Report template (r/googleads 31): "On [DATE] our Google Ads [MCC or ACCOUNT ID] was compromised via an employee's Gmail account with admin access. The hackers added [HACKER EMAIL], which removed our team's access. They added [X] accounts to our invoice and ran unauthorized campaigns against it." Suspension appeal: "We regained access to [ACCOUNT ID] under ticket [TICKET ID]; the account is suspended. We agree the hackers violated policy, but this was not authorized by [COMPANY]. We want to remove the unauthorized campaigns but cannot edit them while suspended." Attach payment receipts, the compromise confirmation, ticket IDs and 2FA proof.
- **Phishing:** fake prospects claiming $30 to 50k/month budgets from look-alike domains registered days earlier. Verify the domain and person before opening any link or access invite (r/PPC 36).
- **Wrongly disapproved keywords:** live chat at Google Ads support; chat availability depends on the issue you select.

## Rules for any agent that writes to ad accounts

Read-only by default. A write needs (AgriciDaniel mutation gate, MIT):

- a tested capability and explicit object IDs;
- a before/after diff with blast radius and learning impact;
- the owner's approval of the exact plan and spend ceilings;
- an audit record, a rollback plan and a verification time;
- pause or archive rather than delete; never permanent deletion.
- hard limits the agent cannot exceed: a total spend limit, a daily cap and a maximum budget step per change. One public Claude Code skill for Meta ads uses +20% per change and logs every approval (Tobi, [X post](https://x.com/tobiadonadon_/status/2116291073886818736)); that is a practitioner guardrail, not a Meta rule, and its example result (cost per lead $3.15 to $1.84 in 4 weeks) is reported by the author, not independently checked.

Create and duplicate paused. Activation, publishing and budget increases are separate approvals. Log every change where the owner can see it (a shared sheet of keyword and RSA changes works). Stage proposed changes for manual approval the way Google Ads Editor holds pending changes (a manager of 118 accounts, r/PPC).
