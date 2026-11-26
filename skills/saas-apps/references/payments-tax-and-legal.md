# Payments, tax and legal basics

What a small software business needs in place before the first charge. Fees were checked on 26 November 2026; recheck the live page before modeling, they changed in 2025 and 2026. This is not legal or tax advice: when money, contracts or personal data are at stake, tell the founder to confirm with an accountant or lawyer in their country. Sources in [sources.md](sources.md).

## Stripe or a merchant of record

A merchant of record (MoR) is the legal seller on each order. It charges the customer, collects and files VAT and sales tax, handles chargebacks and pays you out. With plain Stripe, your company is the seller and you register and file tax yourself.

| Option | Fee (2026) | You still handle | Fits |
|---|---|---|---|
| Stripe Payments + Billing + Tax | 2.9% + $0.30 per US card; Billing 0.7% of billed volume; Tax 0.5% per transaction (no-code) | Tax registration and filing in each place you are liable; disputes | B2B, mostly one country, founder or accountant can file |
| Stripe Managed Payments | Card processing plus 3.5% on the full amount incl. tax | Not available with Stripe Connect or custom Elements checkouts; subscriptions created only through Checkout or Payment Links | Digital products sold to consumers worldwide, already on Stripe |
| Paddle | 5% + 50 cents per checkout transaction; custom pricing under $10 orders | Nothing tax-related; Paddle files | Solo founder selling globally, wants no tax admin |
| Lemon Squeezy | 5% + 50 cents, but no new sign-ups and shutdown on 31 March 2027 | Migrate existing stores before the shutdown | Nobody new |
| App Store / Google Play billing | 15% to 30% (see below) | Nothing tax-related on in-app purchases | Required for most in-app digital purchases |

Rules:
- **Compare the all-in cost on your real price.** On a $10 monthly plan: Stripe US card plus Billing is about $0.59 + $0.07 = $0.66 (6.6%) before Tax; Paddle is $1.00 (10%). On $100: Stripe about $3.90 (3.9%), Paddle $5.50. The MoR premium buys tax filing and fraud handling; small products with consumer buyers in many countries usually pay it gladly.
- **Fixed fees punish small prices.** A $3 monthly plan loses $0.39 (13%) to a US card fee alone. Prefer annual plans or a higher monthly price.
- **Never build on a payments provider that has announced a shutdown.** Lemon Squeezy stopped accepting new sign-ups and will shut down on 31 March 2027 (Lemon Squeezy, 2026).
- **Disputes cost money even when you win.** Stripe charges a fee per dispute received (EUR 20 on its EU price list, 2026). Refund fast when a customer is unhappy; a refund is cheaper than a dispute and protects your account.

## App stores and marketplaces

| Platform | Commission or rule | Source |
|---|---|---|
| Apple App Store, Small Business Program | 15% on paid apps and in-app purchases if proceeds were up to $1M in the prior calendar year (new developers qualify); above $1M in the current year, the standard rate applies | Apple Developer, 2026 |
| Apple, auto-renewable subscriptions (standard) | You receive 70% in a subscriber's first year, 85% after one year of paid service | Apple Developer, 2026 |
| Google Play, most markets | 15% on the first $1M earned each year, 30% above; auto-renewing subscriptions 15% | Google Play Console Help, 2026 |
| Google Play, EEA, UK, US (from 30 June 2026; Australia and Japan from 30 Sept 2026) | Auto-renewing subscriptions on the first $1M: 10% + 5% billing fee; other new-install transactions 20% + 5% | Google Play Console Help, 2026 |
| Shopify App Store | 0% on the first $1M of lifetime gross app revenue (only revenue from 1 Jan 2025 counts), then 15%; 15% on everything for developers with $20M+ App Store revenue or $100M+ company revenue; $19 one-time account fee; 2.9% processing separate | Shopify Dev Docs, 2026 |
| Chrome Web Store | One-time developer registration fee; no store payments since 1 Feb 2021 (charge through your own checkout and check licences yourself) | Chrome docs, 2026; Chromium Extensions group, 2020 |

Store rules move fast (US link-out rulings, regional Play fees). Model web checkout as a scenario, never as the only plan, and read the current guideline before sending users from an app to a web checkout.

## Sales tax and VAT in plain words

- **EU consumers:** VAT on electronically supplied services is due in the buyer's country. A non-EU business selling to EU consumers can declare all EU sales in one quarterly return through the non-Union One Stop Shop, filed in one member state of its choice (European Commission OSS portal, 2026). B2B sales to VAT-registered businesses are usually reverse-charged: collect and validate the buyer's VAT number.
- **US:** sales tax on SaaS depends on the state, and each state sets its own economic-nexus threshold. Stripe Tax monitors thresholds; an MoR removes the question.
- **UK, Canada, Australia and others** have their own digital-services rules. If the founder sells to consumers in many countries and has no accountant, recommend an MoR.
- **App store purchases:** Apple and Google collect and remit tax on in-app purchases they process.

## Legal pages before the first charge

Not legal advice. A founder should have these live, linked from signup and checkout:

1. **Terms of service:** what the product does, plans and billing, renewal and cancellation, refunds, acceptable use, liability limit, termination, governing law.
2. **Privacy policy:** what personal data you collect, why, legal basis (EU), which vendors receive it (hosting, email, analytics, payments, AI providers), retention, user rights and a contact.
3. **Refund policy:** state it plainly. In the EU, consumers have a 14-day right to cancel online purchases; for digital content it does not apply only if the buyer expressly agreed to start immediately and to lose that right (Your Europe, European Commission). Add that consent checkbox at checkout if you sell to EU consumers.
4. **Data processing agreement (B2B):** under GDPR, a processor's work for a controller must be governed by a contract (Art. 28). Business customers will ask for one; have a template and a list of sub-processors.
5. **Cookie and tracking consent** where analytics or ads tags set non-essential cookies for EU and UK visitors.

GDPR basics for a small team:
- Collect only what the product needs; delete what you no longer use.
- Sign the DPA offered by each vendor that touches personal data (hosting, email, analytics, AI APIs) and list them in the privacy policy.
- Answer access and deletion requests; keep a simple log.
- Fines reach up to EUR 20 million or 4% of worldwide annual turnover for the most serious breaches (GDPR Art. 83(5)). Small teams rarely see those, but the risk is real enough to do the basics.
- If the product sends customer data to an AI provider, say so in the privacy policy and check the provider's data-retention settings.

## Auto-renewal and cancellation

- **US:** the FTC's click-to-cancel rule was vacated by the Eighth Circuit on 8 July 2025, before it took effect. ROSCA, the Telemarketing Sales Rule, FTC Act section 5 and the auto-renewal laws in more than half of US states still apply, and many state laws are as strict (Greenberg Traurig, July 2025). Practical baseline: clear terms before purchase, express consent to renew, a reminder before a trial converts or an annual plan renews, and online cancellation as easy as signup.
- **EU and UK:** check consumer law in the main markets; the safe default is the same baseline.
- **App stores:** Apple and Google run the subscription and cancellation flow; your paywall must still show price, period, trial length and renewal terms.

## Checklist the agent runs before launch

- Checkout tested end to end with a real card and a refund.
- Tax: MoR chosen, or Stripe Tax on with registrations listed.
- Terms, privacy, refund policy live and linked from signup and checkout; EU digital-content consent if relevant.
- Renewal reminder email live for trials and annual plans.
- Cancel path tested from the account page.
- Failed-payment emails and card updater on ([activation-and-retention.md](activation-and-retention.md)).
- Vendor DPAs signed and listed.
