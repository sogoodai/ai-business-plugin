# Deliverability for small senders

Mail that lands in spam earns nothing, and Gmail decides on engagement and complaints, not on how good the copy is. Set this up before volume requires it.

## The rules that apply (2024 to 2026)

| Mailbox | All senders | Bulk senders | Source |
|---|---|---|---|
| Gmail | SPF or DKIM; valid forward and reverse DNS; TLS; RFC-compliant format; spam rate under 0.3% | About 5,000+ messages a day to personal Gmail from one primary domain: SPF **and** DKIM, DMARC (at least `p=none`), DMARC alignment, one-click unsubscribe (RFC 8058) for marketing | Google sender guidelines and FAQ, Feb 2024 onward |
| Gmail enforcement | | Bulk status is **permanent** once reached; disruption of non-compliant traffic ramped up from **November 2025** | Google FAQ |
| Yahoo | SPF or DKIM, complaints under 0.3% | SPF + DKIM + DMARC; visible unsubscribe plus List-Unsubscribe; honor within **2 days**; no fixed numeric bulk threshold | Yahoo Sender Hub 2024 |
| Microsoft (Outlook, Hotmail) | | High-volume senders: SPF, DKIM, DMARC from 5 May 2025 | AgriciDaniel claude-email (MIT), citing Microsoft |

Small-sender rule: do all of the bulk requirements now. They cost an hour and the 5,000 threshold arrives in one Black Friday send.

## Setup steps (agent runs or hands to whoever owns DNS)

1. **List every service that sends as the domain:** Google Workspace or Microsoft 365, the ESP (Klaviyo, Mailchimp, Brevo...), booking tool, invoicing, store platform, helpdesk. Each needs to be in SPF or sign with DKIM.
2. **Use a branded sending domain or subdomain** (for example `mail.yourbusiness.com` or `news.yourbusiness.com`) authenticated in the ESP, not the ESP's shared domain. Marketing on a subdomain protects the main domain's reputation for one-to-one mail.
3. **SPF:** exactly one TXT record per domain, at most 10 DNS lookups (warn at 8, flatten if needed), end with `-all` or `~all`, never `+all` (AgriciDaniel, MIT). Example: `v=spf1 include:_spf.google.com include:sendgrid.net ~all`.
4. **DKIM:** enable in each sending service; publish the CNAME or TXT records it gives. 2048-bit keys (1024 is deprecated); rotate every 6 to 12 months; signature covers From, To, Subject, Date, List-Unsubscribe and List-Unsubscribe-Post (same source).
5. **DMARC:** start `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com; adkim=r; aspf=r`. Read the aggregate reports for 30+ days; when every legitimate sender passes aligned, move to `p=quarantine`, then after 30+ more days `p=reject` (same source). `p=none` already satisfies Gmail and Yahoo.
6. **One-click unsubscribe:** `List-Unsubscribe` with an HTTPS URL plus `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (most ESPs add this; check the raw headers of a test send).
7. **Register Google Postmaster Tools** for the domain to see spam rate and reputation; check weekly once sending.
8. **Verify:** send to a Gmail test address, "Show original", confirm SPF, DKIM and DMARC all say PASS. No seed or header test means not verified (aaron-he-zhu deliverability QA, Apache-2.0: "never pass by default").

## Warming a new domain or a cold list

Do not "warm" by mailing people who did not ask. Engagement and complaints are what count (Google). Ramp by audience, not by count alone:

| Days | Volume vs target | Who |
|---|---|---|
| 1 to 3 | 5 to 10% | Most engaged: clicked, bought or booked in the last 30 days |
| 4 to 7 | 15 to 25% | Engaged 30 to 60 days |
| 8 to 14 | 30 to 50% | Engaged 60 to 90 days |
| 15 to 21 | 60 to 75% | Recent customers |
| 22 to 30 | 80 to 100% | Rest of the consented list |

Pause if bounces pass 2% or complaints pass 0.2% (AgriciDaniel, MIT, uncited thresholds). Avoid week-to-week volume swings over 20%.

## Reputation targets

| Signal | Target | Hard limit |
|---|---|---|
| Spam complaints | under 0.1% | 0.3% (Gmail, Yahoo) |
| Hard bounces | under 1% (2% acceptable) | over 5% damages reputation |
| Unsubscribes per campaign | under 0.3% | rising trend = frequency or relevance problem |
| Unengaged share of list | under 20 to 25% | run a sunset above it |

Complaint math: at 10,000 delivered, 30 complaints is 0.3%. A small list hits the ceiling with a handful of angry people, so one bad import can sink a domain.

## List hygiene

- **Suppress immediately:** hard bounces, complaints (never re-mail), unsubscribes, role addresses (info@, abuse@).
- **Engagement on clicks, orders, bookings and replies, not opens.** Apple MPP makes opens unreliable; never suppress or retain on opens alone.
- **Cohorts by last click or purchase** (aaron-he-zhu list hygiene, Apache-2.0): active 0 to 30 days, cooling 31 to 90, dormant 91 to 180 (win-back), deep-dormant 181 to 365 (re-permission once, else sunset), never-engaged or 365+ (sunset). Flag when dormant plus deep-dormant plus never-engaged pass 25% of the list.
- **Tie the sunset to the buying cycle.** Promotional lists re-permission at 90 to 120 days without engagement and sunset at 180; newsletters re-permission at 180 and sunset at 365 (same source). A furniture buyer is not dormant at 90 days; a coffee buyer is.
- **Never delete suppressed contacts**; keep them suppressed so a re-import cannot re-add them. Check for suppression leakage (unsubscribed address still on an active list).
- **Imported or old lists:** no consent record, no send. If consent exists but the list is over 6 to 12 months cold, send one re-permission email to a small batch first and watch bounces and complaints.

## Content signals that hurt

- Fake "Re:" or "Fwd:", 3+ ALL-CAPS words, 2+ exclamation marks, stacked $ or %, unresolved {tokens}, 2+ of (free, guaranteed, act now, risk-free, winner, congratulations, 100%, click here) (aaron-he-zhu spam checklist, Apache-2.0).
- Image-only emails, link shorteners, mismatched link domains.
- Subject 30 to 40 characters show on mobile; front-load the point. Preheader 40 to 50 characters on mobile; set it or the client pulls body text (same source).

## Tricks most owners miss

- **Booking and invoicing tools send as your domain too.** If they are not in SPF or signing DKIM, enabling DMARC enforcement will bounce your own receipts. Read DMARC reports before moving past `p=none`.
- **Text that the email went out.** Quotes landing in Gmail Promotions were found once a one-line SMS said "sending pricing to your email now" (66-pt thread).
- **Reply-to a real inbox.** Replies are a strong positive signal and many of them are bookings.
- **Do not change ESP, domain and volume in the same month.** Change one thing, watch Postmaster for two weeks.
