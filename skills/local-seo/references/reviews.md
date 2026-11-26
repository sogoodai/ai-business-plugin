# Reviews: math, system, policy, removal

Wording for requests and replies is in [review-templates.md](review-templates.md). Sources in [sources.md](sources.md).

## Why reviews matter twice

- **Ranking.** Google says review count and rating feed prominence. Whitespark 2026 experts rank rating, review count with text, recency (#11) and steady influx (#14) among Maps factors. A machine-learning study of local packs (Search Atlas, Aug 2025, via claude-seo) put review count at 19.2% of explained variance, second only to proximity (55.2%).
- **Recency beats the total.** Sterling Sky (Apr and Jul 2025): a clear ranking change around the first **10 reviews**, then little from count alone, while fresh reviews kept helping. One tracked business slid after about **18 days** with no new review. That is one observation, not a Google threshold. Working rule: never let the newest review get older than 2 to 3 weeks.
- **Conversion.** BrightLocal (US, 2026): 47% of consumers call fewer than 20 reviews insufficient; 31% only use businesses rated 4.5+ (17% in 2025); 74% only care about reviews from the last 3 months; 89% expect owners to reply. Localo (2026, correlation): 4.3 to 4.4 stars ranked top 3 in 58.1% of checks, 4.5 to 4.6 in 64.8%.
- **Operators agree.** A client with no review for over a year got 3 new ones and a "massive" ranking jump (r/GoogleMyBusiness, 2025). A business adding 30 a month at 150 total is expected to outrank one at 400 adding 2 (r/localseo, 2026, illustrative).

## The math (run it before setting any target)

Inputs per business, read from Maps: rating, review count, reviews dated in the last 90 days (count them by sorting reviews by "Newest"). Match businesses on their Maps URL or place ID, never on name. Formulas adapted from unifapi-agent/agents (MIT).

**1. Velocity.** `velocity_q = reviews in trailing 90 days` (one quarter). `velocity_m = velocity_q / 3`. Use 90 days, not 30, so one viral week does not distort it. Flag any rival with a big total and low velocity as "coasting": beatable.

**2. Catch-up target.**
```
volume_gap = leader_count - your_count
if leader_velocity_q <= your_velocity_q:
    target_q = your_velocity_q            # gap closes on its own; keep pace
    quarters_to_parity = ceil(volume_gap / (your_velocity_q - leader_velocity_q))
else:
    target_q = volume_gap / H + leader_velocity_q   # H = quarters, default 4
```
If `target_q` is more than about 3x your current pace, the leader is a multi-year goal. Re-run against the nearest beatable rival and report that number. Worked example: you 70 reviews at 4 per quarter, leader 612 at 22: target 158 per quarter (40x, unrealistic). Third place has 210 at 9: target 44 per quarter. Report 44.

**3. Rating repair.** New reviews needed to reach a target average:
```
n = ceil(count x (target - rating) / (avg_new - target))
```
Use `avg_new = 5` for the best case and your real recent average for the honest case. Example: 40 reviews at 4.2, target 4.5. Best case n = ceil(40 x 0.3 / 0.5) = 24. If new reviews average 4.8, n = 40. Below about 4.3 stars, fix the rating (service problems, reply quality) before chasing volume, because rating gates clicks.

**4. Requests needed.** `requests_per_month = target_reviews_per_month / request_to_review_rate`. Measure your own rate for 30 days. Until then assume 10%. Reported rates vary widely: one owner got about 1 review per 20 customers asking in person plus a later text (r/GoogleMyBusiness, 2025); a commenter claims 90% when the link is texted while still with a happy customer (same thread, unmeasured); vendor estimates (uncited, dmp skill): in person 30 to 50%, SMS 15 to 25%, email 5 to 15%, table QR 5 to 10%.

**5. Prominence score (optional, 0 to 100).** `40 x min(count / leader_count, 1) + 35 x min(velocity / leader_velocity, 1) + 15 x clamp((rating - 3.5) / 1.5, 0, 1) + 10 x share of your reviews naming the town or service`. Use it to rank a field, not to promise rankings.

**6. Consumer floor check.** Below 20 reviews you lose about half of US shoppers before rank matters (BrightLocal, 2026). Below 10 you also miss the Sterling Sky ranking step. For a new business, 10 then 20 are the first two milestones.

## Benchmarks to compare against

Use local competitor numbers first. National medians are wide.

| Metric | Typical | Strong | Source, year |
|---|---|---|---|
| Reviews per Maps-visible business | 86 median (mean 513) | 418 (p75) | SEO Bandwagon, Sep 2026, 164,241 profiles |
| Profiles rated 4.5+ | 66.2% of rated profiles | | SEO Bandwagon, Sep 2026 |
| SMBs with under 20 reviews | 47% | Only 16% have 50+ | BrightLocal SMB report, Oct 2026 |
| US restaurant Google reviews | 214 median | | Suff Digital, Sep 2026, 233 profiles |
| Restaurants replying to none of last 20 | 50.3% | | Suff Digital, Sep 2026 |
| Home-service "top performers" | | 4.5+ stars and 50+ reviews | Jobber, 2026 (vendor cohort) |
| Monthly velocity by size | Solo 4 to 8; 5 to 20 staff 10 to 20; multi-location 20 to 50 per location | | localseoskills (MIT), uncited |
| Monthly velocity by vertical | Restaurant 15 to 30, medical 8 to 15, home services 5 to 10, legal 3 to 5 | | localseoskills (MIT), uncited |

Operator targets seen: 50 reviews in the first 90 days, matched to the leading rival's monthly pace (r/localseo, 147 upvotes, 2026); 30+ a month at 4.5+ for a tire shop (r/localseo, 2026); "2 a week for a year beats 30 in one month" (r/localseo, 96 upvotes, 2026).

## The review system

1. **Get the link.** In the GBP dashboard use "Ask for reviews" (short link and QR). Or build `https://search.google.com/local/writereview?placeid=PLACE_ID` (find the ID with Google's Place ID Finder). Test it logged out on a phone.
2. **Trigger on completion, not on satisfaction.** Job done, order picked up, table paid, class finished, support ticket resolved. Everyone gets the same request. No pre-survey that routes only happy people to Google.
3. **Ask in person at the relief moment**, then text the link while still there. "I texted you the link, it takes a second" beats a counter QR or "search for us" (r/GoogleMyBusiness, 2025 and 2026).
4. **Timing.** Text within 2 hours of finishing, one reminder about 3 days later, then stop (r/localseo, 2026). Jobber's defaults are reminders on day 3 and day 5, with no repeat request to the same client for 6 months (Jobber help, 2026). Next-day texts pulled from the booking system built 88, 58 and 39 reviews for an esthetician, massage therapist and nail tech in a few months (r/localseo, 2026). Keep SMS under 160 characters.
5. **Automate the trigger.** POS or CRM webhook (Square, Jobber, Housecall Pro, Toast) to SMS via the booking tool, Zapier or n8n. Owners forget to ask manually (r/localseo, 2026).
6. **Restart a dead profile.** Send individual plain-text requests to the last 20 customers this week (r/localseo, 2026). Past customers count.
7. **Ask for a photo of the finished work or place.** Operators say photo reviews look more trustworthy (r/smallbusiness, 122 upvotes, 2025).
8. **Name one owner.** One person, a daily ask count or "every completed job", checked weekly (r/GoogleMyBusiness, 2026).
9. **Field tricks.** Review QR on the technician's ID badge or clipboard (r/GoogleMyBusiness, 2025). Mention reviews at arrival and again at departure. Hand-written thank-you note with the QR for high-ticket jobs.
10. **Unsolicited thank-you = ask now.** Reply with the link the same day (r/smallbusiness, 2020).
11. **Steady, not bursts.** Google lists unusual review volumes or patterns as manipulation signals. Spread a backlog campaign over weeks.

Tricks owners miss:
- **Put the service in your own message, not in an instruction.** "Thanks for having us fix the roof leak today" primes the customer to describe the job. A roofer at 47 reviews with no repair calls started ranking top 3 for repair terms about three weeks after reviews began naming repairs (r/smallbusiness, 323 upvotes, 2026; OP sells a review tool). Google's policy forbids requesting specific content, so never write "please mention roof repair" or a staff name.
- **Wedding and event pros:** leave your own Google review with photos on each venue you work, and update it with new photos after repeat visits. One photographer credits 30+ bookings over about 5 years (r/WeddingPhotography, 2025). Works for florists, caterers, DJs, makeup artists.
- **Tip redirect:** "Only hugs, referrals or reviews accepted" for no-tip businesses (r/Esthetics, 2024). Fine as a joke, but never trade a discount for a review.

## Policy lines (hard rules)

| Never | Why |
|---|---|
| Offer anything for a review: discount, free item, entry, credit, "10% off if you show us your review" | Google bans incentives outright. Penalties seen: review removal, review posting disabled, rating unpublished, public warning banner. A shop that gave free product for reviews lost all 50+ reviews, was suspended and got a 30-day review block (r/GoogleMyBusiness, 2026) |
| Gate: ask "how did we do?" and send only 4 to 5 stars to Google | Google and Tripadvisor ban selective solicitation. Turn off the "private feedback for 1 to 4 stars" feature in tools like Boulevard, Phorest, ClientMax and similar |
| Ask for 5 stars, keywords or a staff name | Google bans requested content (2026 policy wording includes staff names) |
| Staff review quotas, per-review bonuses, "mention me so my boss pays me" | Google bans staff quotas for solicitation; Tripadvisor bans employee incentives. Operators recommend them (r/localseo, r/GoogleMyBusiness): do not. Reward service quality instead |
| Buy reviews | 12 of 20 bought reviews vanished in 3 weeks, the rest a month later, rankings fell below the start (r/smallbusiness, 69 upvotes, 2025). FTC rule (US, effective 21 Oct 2024) |
| Review kiosk or tablet in the shop | Same device and IP gets filtered. A QR that opens the customer's own phone is fine |
| Ask for Yelp reviews | Yelp says solicited reviews may be filtered by its recommendation software. Claim, complete and reply on Yelp; a passive "Find us on Yelp" sign is allowed per Yelp's business guide (2018 to 2020 document, verify live) |
| Use one "leave us a review" automation for all platforms | Google and Tripadvisor allow neutral asks; Yelp does not |

Legal context: US FTC Consumer Reviews and Testimonials Rule (effective 21 Oct 2024) bans fake reviews, sentiment-conditioned payments, undisclosed insider reviews and review suppression; claude-seo cites up to $53,088 per violation. UK DMCC Act rules from 6 April 2025 cover fake and concealed-incentive reviews, with fines up to 10% of global turnover (CMA). Australia (ACCC) and Canada (Competition Bureau) require disclosure of incentives and employee reviews. Google is stricter than all of them: no incentives at all.

Friends and family: a friend who paid full price for a real job is a customer. A free job "in exchange for a review" is an incentive. Tripadvisor bans friends and family reviews entirely.

## Replying

- **SLA:** negatives same business day, positives within 48 hours, nothing unanswered after 7 days. BrightLocal (2026): 19% expect a same-day reply, 81% within a week, 50% are put off by generic or templated replies.
- **Order of work when catching up:** last-30-day negatives today, older negatives within 48 hours, mixed within a week, then positives. Late replies to 1-stars up to 12 months old still help readers (zubair-trabzada restaurant skill, MIT).
- **Write for the next customer, not the reviewer.** Facts, calm, short, an offline route with a real name.
- **Mention the actual job in positive replies** ("glad the water heater install in Scottsdale went smoothly"). Operators claim a relevance boost (r/localseo, 2026); a commenter disputes it and no evidence was shown. Do it because it reads as real, not as a ranking hack. Never paste the same reply twice.
- Healthcare and legal: never confirm someone is a patient or client, even if they say so.
- Approve public replies one at a time. An agent drafts; the owner posts unless authorized.

## Fake reviews, extortion and removal

Reality first: most removal requests are declined. Google removes clear policy violations (no real interaction, conflict of interest, off-topic, harassment, coordinated attacks, extortion). It will not remove a real customer's harsh opinion. Tell the owner that up front.

**Signals of fake or coordinated reviews (flag on 2+):** several reviews within hours versus normal pace; reviewer accounts with hundreds of 1-stars across a region; identical wording; reviewers from another town; no matching customer, call or booking record; a payment demand by WhatsApp, text or email.

**Procedure:**
1. **Do not engage or pay** the extortionist. One owner who paid was hit again a week later (r/GoogleMyBusiness, 2025). Unsolicited "we can remove it" DMs and emails are scams; one owner got a fresh fake review right after declining (r/GoogleMyBusiness, 61 upvotes, 2026).
2. **Evidence log (one document):** link to each review, screenshot, timestamp, reviewer profile notes, customer-record check, the extortion message, the exact policy each one breaks. Prove the reviews are connected, not each one fake on its own.
3. **Flag each review** from the dashboard (three dots > Report) under the right reason, e.g. fake engagement or conflict of interest.
4. **Extortion:** use Google's merchant extortion form, `https://support.google.com/business/contact/merchant_extortion`. Operators report removals in under 48 hours (r/GoogleMyBusiness, 2025).
5. **Wait about 3 days**, then open the Reviews Management Tool `https://support.google.com/business/workflow/9945796`, choose "Check the status of a review I reported previously", and appeal with the evidence document attached.
6. **Still up after 10 days:** post in the Business Profile Community `https://support.google.com/business/thread/new` with Profile ID, case ID, links to every review and screenshots, asking a Product Expert to escalate. Keep all follow-ups in that one thread; duplicates get locked.
7. **Other routes operators used:** a Google Ads account manager escalating (removed 2 fake reviews in a day, r/GoogleMyBusiness, 2025); a police report on harassment that got all recent 1-stars removed (r/smallbusiness, 2026); a lawyer's cease-and-desist to a client's friends and family that got 2 of 5 taken down faster than Google (r/GoogleMyBusiness, 2026). Paid "removal firms" are unverified; one testimonial credits flagging through an ad account in a stricter-defamation country, treat as hearsay.
8. **Reply publicly while you wait** (templates in [review-templates.md](review-templates.md)). Readers see the dispute even if removal fails.
9. **Recover the rating** with genuine asks to recent customers. One fake 1-star took a small profile from 5.0 to 4.2 while rivals sat at 5.0 (r/GoogleMyBusiness, 2025).

Expect reviews to come back: in one case Google removed an attack, the same accounts edited the reviews and they reappeared (r/GoogleMyBusiness, 54 upvotes, 2026).

## Real reviews disappearing

- **Count before panicking.** Displayed totals drift. One profile showed 126 while 148 reviews were still listed (r/GoogleMyBusiness, 84 upvotes, 2025).
- Desktop display bugs happen; the Maps mobile app may still show and allow replies (r/GoogleMyBusiness, 2026).
- Filter triggers reported: bursts, reviewers on the same Wi-Fi, a review naming staff. 38% of reviews deleted in early 2025 were 5-star (GMBapi.com, unverified).
- **Recovery:** open a support ticket while the removal is recent, include screenshots, reply to the acknowledgment email. A mover who lost 7 of 37 reviews filed daily for 4 days and Google restored all of them (r/GoogleMyBusiness, 2026). A customer editing their hidden review can make it reappear (works one at a time).
