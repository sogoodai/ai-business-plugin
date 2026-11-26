# Accessibility and the legal rules that touch conversion

Operational guidance, not legal advice. Obligations depend on country, sector, size and how the law is enforced locally. When a business is near a threshold, or sells in a high-risk sector (ecommerce in New York or California, healthcare, finance), tell the owner to get a lawyer's view. Sources in [sources.md](sources.md).

## Why this is a conversion topic too

The money path (cookie banner, navigation, product or service choice, form or cart, validation, scheduler or payment, confirmation) is exactly where accessibility failures cluster: third-party embeds, dialogs, CAPTCHA, checkout and booking widgets (research synthesis 2026). A form without labels is unusable by a screen reader and also hard for everyone on a phone. Fixing it is a conversion fix.

**How common the defects are** (WebAIM Million, February 2026, top 1 million home pages): 95.9% had detected WCAG failures (94.8% in 2025), 56.1 errors per page on average. Most common: low-contrast text 83.9% of pages, missing image alt text 53.1%, missing form input labels 51%, empty links 46.3%, empty buttons 30.6%, missing page language 13.5%. Pages using ARIA averaged 59.1 errors vs 42 without (more complex pages, not proof ARIA causes errors). Automated tools catch only part of the problems; a clean scan is not an accessible site.

## By jurisdiction

| Where | Rule | Who it covers | What to aim for |
|---|---|---|---|
| EU | European Accessibility Act (Directive 2019/882), applies to products and services placed on the market from 28 June 2025 | Ecommerce services to consumers, consumer banking, e-books, transport ticketing, among others; also non-EU sellers selling to EU consumers. Service microenterprises (fewer than 10 staff and under €2 million turnover or balance sheet) are exempt | EN 301 549, which maps to WCAG 2.1 AA; an accessibility statement describing how the service meets the requirements. Enforcement and fines are national (Germany's BFSG allows fines up to €100,000) |
| US | ADA Title III (businesses open to the public); DOJ guidance says goods and services offered online must be accessible | No size threshold in Title III; ecommerce is the main lawsuit target | WCAG 2.1 or 2.2 AA as the working standard; DOJ points to WCAG and Section 508 but has no Title III web rule. The 2024 Title II rule covers state and local government only, not private businesses |
| US, California | Unruh Civil Rights Act | Businesses serving Californians | Statutory damages of $4,000 per violation drive many state-court suits |
| UK | Equality Act 2010 (reasonable adjustments); public-sector regulations require WCAG 2.2 AA for public bodies only | Private businesses under the Equality Act | WCAG 2.2 AA as the practical baseline |
| Canada | Accessible Canada Act digital amendments (2026) for federally regulated private businesses with 100+ employees; provinces separate | Ontario AODA: private and nonprofit organizations with 50+ employees must make public websites meet WCAG 2.0 AA | WCAG 2.1 AA, plus provincial and human-rights duties |
| Australia | Disability Discrimination Act; AHRC 2025 guidance recommends WCAG 2.2 at least AA | Goods and services providers | WCAG 2.2 AA |

**US lawsuit pressure, 2025:** UsableNet counted 5,114 digital accessibility lawsuits in federal and New York and California state courts; Seyfarth Shaw counted 3,117 federal website suits, up 27% from 2,452 in 2024. Ecommerce made up 69% of first-half 2025 filings (UsableNet midyear). About 45% of federal suits targeted companies already sued before. New York leads. A small Shopify store is a realistic target, not an edge case.

## Overlays are not a strategy

- The FTC ordered accessiBe to pay $1 million (proposed January 2025, final April 2025) for claiming its widget made any site WCAG compliant and for disguising paid reviews as independent ones.
- Overlays do not fix missing labels, keyboard traps in checkout, inaccessible booking iframes or CAPTCHA. Sites running overlay widgets still get sued.
- Never recommend an overlay as the compliance answer. If the owner already has one, keep it only if it does not break keyboard or screen-reader use, and fix the underlying HTML anyway.

## The agent's accessibility pass on the money path

Run on the real pages, keyboard only first, then a screen reader (VoiceOver on iPhone or NVDA on Windows), then an automated scan (WAVE, axe, Lighthouse accessibility).

| Check | Pass rule |
|---|---|
| Keyboard | Every link, button, form field, menu, accordion, popup and scheduler reachable with Tab, usable with Enter or Space, closable with Esc; visible focus outline everywhere |
| Popups and chat | Focus moves into the dialog and returns after closing; no keyboard trap; close button has an accessible name |
| Form labels | Every input has a visible `<label>` (placeholders are not labels); required fields marked in text, not color only |
| Errors | Error text next to the field, announced to screen readers, explains how to fix; entered data kept |
| Contrast | Body text at least 4.5:1, large text and UI components at least 3:1; check CTA text on its button color and text over hero images |
| Images | Informative images have alt text that says what matters (product color, before/after); decorative images `alt=""` |
| Buttons and links | No empty buttons (icon-only cart, close, menu) without an accessible name; link text makes sense alone ("Book a cleaning", not "Click here") |
| Language | `<html lang="...">` set |
| Zoom and reflow | Page usable at 200% zoom and at 320 px width without horizontal scrolling |
| Media | Captions on videos with speech; autoplaying media can be paused |
| Third parties | Booking widget, payment form, review widget, CAPTCHA and cookie banner all pass the keyboard test; if one fails, record it and push the vendor or swap it |
| CAPTCHA | Prefer invisible or honeypot spam protection over image puzzles |
| Statement | EU sellers in scope publish an accessibility statement; elsewhere publish an accessibility contact so problems reach the owner before a lawyer does |

## Other legal rules that bite conversion tactics

**Reviews and testimonials (US).** The FTC Consumer Reviews and Testimonials Rule took effect 21 October 2024. It bans fake reviews and testimonials (including AI-written ones), buying reviews, incentives conditioned on positive or negative sentiment, insider reviews without disclosure, suppressing negative reviews through threats, and misrepresenting that the reviews shown are all or most reviews. Fake social proof such as bought followers or views also falls under it. The FTC sent warning letters to 10 companies in December 2025; civil penalties run to tens of thousands of dollars per violation ($53,088 under the 2025 inflation adjustment). A site review widget that silently hides 1 to 3 star reviews while implying it shows all of them is a risk.

**Reviews (Google).** No incentives of any kind for Google reviews, no gating ("happy? review us on Google; unhappy? tell us privately"). Google is stricter than the FTC. Depth in sibling `local-seo`.

**Fake urgency and scarcity.** EU consumer law blacklists falsely stating a product is available only for a very limited time to force a quick decision (Unfair Commercial Practices Directive, Annex I point 7). The FTC treats fake countdown timers and false low-stock messages as dark patterns. Use real stock counts, real cutoffs and real deadlines only.

**Reference prices.** EU: any announced price reduction must show the lowest price applied in the prior 30 days (Price Indication Directive as amended by the Omnibus Directive). US: compare-at prices must be real former prices offered in good faith; class actions over markdown pricing hit Shopify merchants repeatedly. Keep dated price records.

**Drip pricing.** California SB 478 (from 1 July 2024) requires advertised prices to include all mandatory fees except taxes and shipping, for nearly all businesses selling to Californians. The FTC fees rule (from 12 May 2025) requires the total price up front for live-event tickets and short-term lodging. Show the total early anyway: hidden costs are the top abandonment reason in Baymard's 2026 data.

**Subscriptions and cancellation.** The FTC's broader "click to cancel" rule was vacated by a federal appeals court in July 2025, but ROSCA still requires clear disclosure and consent for recurring charges, and California's auto-renewal law (amended from 1 July 2025) requires online cancellation for online sign-ups plus clear disclosure. Show the recurring price, billing interval and how to cancel next to the subscribe button.

**Consent.** Under GDPR and UK GDPR, marketing consent needs an unticked box or explicit action; a pre-ticked box is not consent (CJEU Planet49, 2019). Cookie banners in the EU need "reject" as easy as "accept". Shopify's "preselect email signup" setting is not for EU or UK shoppers.

## Tricks most owners miss

- **Test the third-party widgets, not just your HTML.** The booking iframe, payment form, review carousel and cookie banner are where audits fail, and they are also the steps closest to money.
- **Contrast on the CTA button is the most common single fix** with both accessibility and conversion upside.
- **An accessibility contact link** ("Trouble using this site? Email or call us at...") catches problems before they become demand letters and recovers sales from users who got stuck.
- **The EU microenterprise exemption is a threshold, not a status.** A store that passes 10 staff or €2 million turnover is in scope from then on. Build new pages accessibly now so growth does not trigger a rebuild, and note that the US, UK and Australian rules have no such exemption.
- **Price records double as legal defense.** Export the catalog with compare-at prices every time prices change.
