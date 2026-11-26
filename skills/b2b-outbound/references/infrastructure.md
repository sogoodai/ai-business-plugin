# Cold email infrastructure: domains, inboxes, warmup, volume

Copy only matters if the mail lands. This file covers the 2024 to 2026 mailbox-provider rules, the sending setup, volume per inbox, warmup, monitoring, stop-loss rules and costs. Provider rules are primary sources (Google, Microsoft, Yahoo). Volume and warmup numbers are vendor data or operator reports: starting points, not policy. Sources: [sources.md](sources.md).

## The provider rules (primary sources, current November 2026)

| Provider | What every sender needs | What bulk senders need | Enforcement |
|---|---|---|---|
| Gmail (personal @gmail.com) | SPF or DKIM, valid forward and reverse DNS (PTR), TLS, RFC 5322 formatting, user-reported spam under 0.3% | About 5,000+ messages in 24 hours to personal Gmail: SPF **and** DKIM, DMARC (p=none is enough), From-domain alignment, RFC 8058 one-click unsubscribe on marketing mail plus a visible body link, unsubscribes honored within 48 hours | Rules since 1 Feb 2024; Google ramped rejections (temporary, then permanent) from November 2025 |
| Yahoo / AOL | Same shape as Google | Same as Google | Since 2024 |
| Outlook.com, Hotmail, Live (consumer) | Authentication strongly expected | Domains sending more than 5,000 a day: SPF, DKIM and DMARC must pass | Since 5 May 2025; non-compliant mail rejected with `550 5.7.515` |

Facts an agent gets wrong:

- **The 5,000 threshold counts the primary registrable domain.** `sales.acme.com` and `news.acme.com` both count toward `acme.com`. A subdomain does not dodge it. Crossing it once makes the domain a bulk sender permanently (Google sender FAQ).
- **Bulk rules target personal Gmail.** Mail to Google Workspace business addresses is filtered by the same reputation system, so follow the rules anyway. The complaint thresholds apply to everyone.
- **Spam rate: keep under 0.1%, never reach 0.3%.** Above 0.1% already hurts bulk delivery; at 0.3% a sender loses eligibility for Google's mitigation help.
- **Service caps are not safe volumes.** Google Workspace allows 2,000 outgoing messages a day per user; Exchange Online SMTP AUTH allows 10,000 recipients a day and 30 messages a minute. Microsoft says Microsoft 365 is not a supported bulk platform. Cold programs run at a hundredth of these caps.
- **No provider endorses "warmup networks".** Google and Microsoft describe warming as gradually raising real mail volume. Synthetic engagement pools are a vendor product, not a provider recommendation.
- **Fake "Re:" or "Fwd:" subjects and deceptive display names** break Google's sender guidelines and CAN-SPAM's header rules.

## Sending setup checklist

Run this before the first cold send. Every line is a yes or a stop.

1. **Never send cold from the primary domain.** It carries invoices, password resets and customer support. One bad campaign can damage it for months.
2. **Buy 2 to 5 secondary domains that are obviously yours** (`getacme.com`, `acmehq.com`, `tryacme.com`, `acme-team.com`). Avoid hyphen spam and odd TLDs for the first set. Redirect each to the main site, or to a landing page for the service it sells (one agency gives each service its own infrastructure with a matching landing page and outcome video, r/LeadGeneration 169).
3. **2 to 3 mailboxes per domain, each a real person** with full name, photo and signature. Never aliases of one mailbox. Never shared "sales@" as a sender.
4. **Authenticate every domain:** SPF (one record, under 10 lookups), DKIM (2048-bit), DMARC starting at `p=none` with an `rua` reporting address, aligned to the From domain. Add a custom tracking domain only if you will track clicks.
5. **Buy mailboxes only from properly licensed tenants.** In late 2025 Google reportedly suspended large numbers of resold Workspace mailboxes built on education, nonprofit or legacy tenants (coreyhaines31 cold-email skill, MIT). Cheap reseller inboxes can vanish together.
6. **Match the mailbox provider to the prospects' provider.** Check each prospect's MX record. Google-hosted senders for Google Workspace audiences (most startups, agencies, SaaS); Microsoft-hosted for Microsoft 365 audiences (enterprise, manufacturing, public sector, many professional firms). One operator keeps 15 to 20% of inboxes on Outlook 365 for Microsoft recipients (r/b2bmarketing 46). Another splits campaigns by recipient provider and parks Outlook recipients until new domains are older than 2 weeks, because new domains inbox worst at Outlook (r/LeadGeneration 16 to 17).
7. **Google Workspace over generic SMTP.** A 3-month 2024 test with everything else equal: SMTP reply rates were half of Workspace (r/b2bmarketing 46).
8. **Plain text, no images, no attachments, no link in email 1,** at most one link later, never a link shortener.
9. **Open tracking off. Click tracking off** unless needed (then only with a custom tracking domain). Hunter's 2025 sends: 7.4% replies without tracking vs 4.4% with (31M emails, observational). An agency running 43 campaigns reports +0.5 to 0.8 reply points and better placement after turning both off (r/b2bmarketing 170).
10. **Opt-out line and postal address** in every email (see [legal.md](legal.md)).
11. **Google Postmaster Tools and Microsoft SNDS** set up for each sending domain (Postmaster lags 24 to 48 hours; SNDS needs approval).
12. **A suppression list shared by every sending tool,** keyed on email, LinkedIn URL and phone (see [lists-and-signals.md](lists-and-signals.md)).
13. **10 to 20% spare domains warmed and idle,** so a burned domain is swapped without stopping the program.

## Volume per inbox

There is no official safe cold-email number. What the data and operators converge on:

| Source | Sends per inbox per day | Note |
|---|---|---|
| Smartlead State of Cold Email 2026 (850M+ emails, H1 2026) | Median sender 13.9; heaviest 10% about 42 | Observational, vendor |
| Hunter 2026 report (2025 sends) | 20 to 49 a day: 5.7% replies vs 4.5% overall | Correlation, vendor |
| Agency, 43 live campaigns (r/b2bmarketing 170) | Cut from 20 to 15 to 18, added inboxes | Better placement, no number |
| Operator (r/b2bmarketing 80) | 10 to 15; 30 to 40 now risks spam | 200 sends a day = 15 to 20 inboxes |
| Operator (r/LeadGeneration 23) | 8 a day, stay under 15 | Scale by adding domains |
| Operator with 170 inboxes (r/b2bmarketing 35) | About 30 | Workspace, 15 days warmup, no reply data given |

**Rule:** start at 10 a day per new inbox in week 3, ramp to 15 to 25 on Google-hosted, lower and tested on Microsoft-hosted. Follow-ups count toward the daily number.

**Capacity math:**

```
daily new contacts = (inboxes x sends per inbox) / emails per contact in the sequence
inboxes needed     = target sends per day / 15 to 25
domains needed     = inboxes / 2 to 3, plus 10 to 20% spares
```

Example: 60 new contacts a day on a 3-email sequence = 180 sends a day = 9 to 12 inboxes = 4 to 5 domains plus 1 spare.

## Warmup

| Week | What to send |
|---|---|
| 1 to 2 | Warmup only, plus a handful of real emails to people likely to answer (partners, friends, customers) |
| 3 | First cold sends at 5 to 10 a day per inbox |
| 4 to 6 | Raise by a few a day while bounce, complaints and placement hold |
| After | Keep light background warmup; real replies are the strongest reputation signal |

- Operators: at least 14 days, ideally 21; inboxes warmed only 5 to 7 days get throttled in week one (r/b2bmarketing 80). 2 weeks then 10 a day ramping to about 25 over 2 to 3 weeks (r/microsaas 54, OP sells outreach software).
- Smartlead warmup settings one operator runs: max 10 warmup emails a day, ramp 2 a day, random 1 to 10, warmup reply rate 35%, weekdays only (r/LeadGeneration 15).
- A replacement domain for a burned opt-in sender started at 50 a day and ramped over 6 weeks (r/Emailmarketing 89).
- **Buy domains ahead of need and let them age** rather than paying for "aged" domains (r/LeadGeneration 16).
- A mailbox whose only engagement is warmup traffic is a recognizable pattern. Warmup buys time; replies earn reputation.

## Verification and bounces

- Verify every list right before upload. Re-verify anything older than about a week. One agency verifies at build and again before upload when the gap is 1 to 2 weeks: about $50 a month extra, bounces fell from 1.1% to 0.4% (r/b2bmarketing 170).
- **Bounce bands:** Smartlead H1 2026 median 1.54%; worst quartile starts around 3.21%; Smartlead calls about 2% the danger line (vendor guidance, not a provider rule). Under 1% is best in class.
- "Verified" database emails are not verified: Apollo exports bounced at 30% for one agency until it moved to waterfall verification (r/agency 129). Operators estimate Apollo emails at 80 to 85% accurate (r/b2bmarketing 35). Data decays about 2% a month, 20 to 30% a year (vendor estimates).
- **Catch-all domains** (15 to 28% of B2B domains, vendor estimates) accept anything. Resolve them with a catch-all-capable verifier, send resolved ones from separate lower-volume inboxes, send unresolved ones only for Tier 1 accounts (r/LeadGeneration 169; coreyhaines31 prospecting skill, MIT).
- Dedupe across every list: one lead got 8 emails from different lists in a month (r/b2bmarketing 35).

## Monitoring

| Check | Tool | Frequency |
|---|---|---|
| Inbox placement | Seed tests (MailReach, GlockApps, sender's built-in test) | Before each new campaign, then weekly |
| Domain reputation | Google Postmaster Tools, Microsoft SNDS | Weekly |
| Bounce rate | Sending tool, per campaign and per inbox | Daily |
| Complaints | Postmaster; replies containing "spam", "stop", "remove" | Weekly |
| Blocklists | Any blocklist checker per sending domain | Weekly |
| DMARC reports | EasyDMARC, dmarcian, Valimail | Monthly |

- **Out-of-office replies prove arrival.** Count them as delivered signals (r/LeadGeneration 16).
- **Per-supplier fatigue.** If inboxes come from several providers, compare reply rate per supplier; an average hides a burned one (r/LeadGeneration 169).
- **Placement tests from operators (about one month, 2025 data):** PuzzleInbox mid-to-high 80s, Inframail mid-70s, some Mailforge inboxes in the 60s, Emailroach below self-managed Workspace (r/b2bmarketing 35; two posts praising the same vendor, treat as possibly coordinated).
- **Scale fatigue is real.** One sender's reply rate fell from 2.1% to 0.7% around email 150,000 of 217,000 in 2025 because domains burned faster than replacements warmed (r/b2bmarketing 49).

## Stop-loss rules (set before launch)

| Trigger | Action |
|---|---|
| Bounce above 2% on a campaign | Pause, re-verify the list |
| Placement below about 70% on an inbox or domain | Pull it from rotation, back to warmup, investigate |
| Complaints approaching 0.1% | Pause, cut volume, review targeting and copy |
| Domain on a major blocklist | Stop sending from it; delist or retire |
| Reply rate under about 1% after 300+ delivered | Stop the campaign. Targeting or offer is wrong; volume makes it worse |
| Mail suddenly landing in spam | Stop all sends, rewrite the sequence from scratch, restart slowly (r/b2bmarketing 35) |

Domain rotation: one agency retires sending domains about every 90 days (r/b2bmarketing 170). Treat that as a ceiling to plan spares around, not a rule.

## Build or buy, and what it costs

| Setup | Cost (operator reports) | When |
|---|---|---|
| DIY founder setup | 5 to 10 domains at about $12 a year, 15 to 30 inboxes at about $3.50 a month, sender $100 to $200 a month: $200 to $400 a month plus 5 to 10 founder hours a week (r/agency 88, OP sells managed outbound) | Up to about 20 inboxes |
| Pre-warmed or managed inboxes | About $3 per Workspace inbox with domain included; paying $1 to $2 more per inbox is "worth it" to avoid burned domains (r/b2bmarketing 46) | Past 20 inboxes, DIY costs 6 to 8 hours a week (same thread) |
| VA test stack | Apollo, Findymail, Instantly about $250 to $300 a month, Claude Pro $20, about 5 VA hours a week (r/b2bmarketing 128) | Testing a market |
| Agency-grade infrastructure | $2,000 to $3,000 a month for 35 clients; cheap domains, inboxes and free warmup burned domains (r/b2bmarketing 61) | Running outbound for others |

Commercial verification runs about $25 to $75 per 10,000 addresses (r/Emailmarketing 72).

Common tools (no endorsement): sending Instantly, Smartlead, lemlist, Woodpecker, EmailBison; inboxes Google Workspace and Microsoft 365 direct, or Inframail, Mailforge, Maildoso, Zapmail, PuzzleInbox; placement GlockApps, MailReach; verification NeverBounce, ZeroBounce, MillionVerifier, Bouncer, Reoon, BounceBan for catch-alls.

## Tricks most owners miss

- A subdomain isolates reputation but never dodges Google's 5,000 count. Use separate registrable domains for cold.
- Turn tracking off before you judge copy. Opens are inflated by Apple Mail Privacy Protection and security scanners; clicks seconds after delivery, clicks with no open, or several clicks in the same second are bots (r/Emailmarketing 16).
- Microsoft recipients deserve their own campaign, sender provider and slower ramp. Mixing them hides a provider-specific failure in the average.
- Sender display name decides Gmail tabs too: "The Driven" went to Promotions; "Mdrive" reached the inbox (r/Emailmarketing 49, newsletter context).
- Fix infrastructure before rewriting copy: correcting warmup, DNS and per-inbox volume with identical copy roughly doubled reply rate for one agency (r/b2bmarketing 61).
- Never import opt-in newsletter rules (list hygiene cadences, best send day) as cold-email rules, and never use the cold infrastructure for newsletters. Marketing email deliverability belongs to `email-sms-loyalty`.
