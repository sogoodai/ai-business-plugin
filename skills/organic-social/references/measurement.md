# Measurement that predicts sales

No public study shows that likes, follower growth or engagement rate predict revenue across businesses. Platforms optimize viewer satisfaction; revenue happens in your funnel. So measure three layers separately and connect them to each post (research report, 2026). Evidence of the gap: an account with 5.4M monthly views and 350 new followers a day stayed flat at 250K followers for 3 months while the business stayed fully booked (r/InstagramMarketing, 60 pts); a LinkedIn news post got 50,000+ views and 60 comments, while practical template posts at about 500 views produced the resource downloads, workshop signups and sales inquiries (r/LinkedInTips, 24 pts).

## The metric tree

| Layer | Metric | Why it matters | Where |
|---|---|---|---|
| Distribution | Non-follower reach share | Is the post entering recommendations? | Instagram Insights, TikTok analytics |
| | 3-second hold (or 1 - skip rate), chose-to-view (Shorts) | Hook works | Insights, Edits app, YouTube Studio |
| | Average watch time, average percentage viewed | Payoff works | All video platforms |
| | Sends per reach, saves per reach | Instagram's discovery signal, reference value | Instagram Insights |
| | Search impressions and queries | Evergreen discovery | TikTok, YouTube, Pinterest, Google Search Console platform properties |
| Intent | Profile visits per 1,000 views | The post made someone curious about the business | Insights |
| | Qualified comments (from target customers) | Right audience | Manual tag |
| | DM starts, keyword triggers | Intent captured | Inbox, ManyChat |
| | Link clicks, outbound clicks (Pinterest) | Off-platform intent | Platform, UTMs |
| Commercial | Leads (email, quote request, booking) | Owned contact | CRM, form, ESP |
| | Qualified leads, consults, sales, revenue, gross margin | Money | CRM, POS, booking system, Shopify |

## Formulas

```
non-follower share        = views from non-followers / total views
hook rate (proxy)         = viewers past 3 s / views          (Instagram: 1 - skip rate)
sends per reach           = sends / accounts reached
saves per reach           = saves / accounts reached
profile visit rate        = profile visits / views x 1,000
DM rate                   = DM starts (incl. keyword triggers) / views x 1,000
leads per 1,000 views     = leads attributed to the post / views x 1,000
DM to qualified lead      = qualified leads / DM starts
qualified lead to sale    = sales / qualified leads
revenue per 1,000 views   = attributed revenue / views x 1,000
revenue per production hour = attributed gross profit / hours to make the post
theme return              = gross profit from a pillar or topic / hours spent on it (rank monthly)
```

**Worked example.** A kitchen remodeler's carousel: 6,000 views, 42 profile visits (7 per 1,000), 9 PRICE keyword DMs, 3 quote visits booked, 1 job at $18,000 with $5,400 gross profit, 2 hours to make. Revenue per 1,000 views $3,000; gross profit per production hour $2,700. A Reel with 60,000 views and zero DMs has a lower business value than this carousel.

**Economics rule.** A post producing $500 gross profit in 1 hour beats one producing $700 in 5 hours, even if the second wins every platform metric (research report, 2026).

## Attribution that works for a small business

1. **One conversion event first:** quote request, booking, email signup, trial or purchase. Pick before posting.
2. **UTMs on every link,** with `utm_content` = post ID or keyword. Use a different link per pinned post, Story and creator.
3. **Keyword per offer** in comment-to-DM flows; tag each contact with post ID and keyword.
4. **CRM source fields:** platform, post ID, content theme, offer.
5. **Ask at booking or checkout:** "How did you hear about us?" with options plus "which post or video?" free text. Self-reported attribution catches dark social (shares in DMs and group chats) that UTMs miss.
6. **Codes per platform or creator** for product businesses.
7. **Google Search Console platform properties** (global since 29 July 2026): verify Instagram, TikTok and YouTube; export the Google queries and top posts monthly.
8. **Do not trust follower counts for revenue,** and do not trust platform "conversions" without your own sales data.

## When to judge a post

| Platform | First read | Final read |
|---|---|---|
| Instagram Reels and carousels | 24 to 48 hours (not the first hour) | 7 days; monthly reports 15 days after month end |
| Trial Reels | about 24 hours for early metrics | 72 hours for auto-share decision |
| TikTok | 48 hours | 7 days |
| LinkedIn | 24 hours | 5 to 7 days (posts peaked on day 5 or took off on day 2 in operator reports) |
| YouTube Shorts and long-form | 48 hours vs the channel's typical range | Months (one video sat under 500 views for 8 months, then reached 66,000) |
| Pinterest | 30 days | 90 days and beyond (no fixed engagement window) |

Judge formats on the **median of 5+ comparable posts**, never on the best one. Log each upload's first-48-hour result against the channel's own typical range so a declining average does not hide repeated underperformance (r/youtubers, 75 pts).

## Diagnostic tree

1. **Low views, low non-follower share:** hook or topic problem. Check 3-second hold. Audit the last 5 openings; remove slow intros; test 3 hook variants via Trial Reels. If holds are fine but reach stays with followers, the topic is too narrow or the account's niche signal is mixed (publish 5 to 7 tightly related posts).
2. **Good hold, low watch time:** payoff or pacing. Payoff inside 10 seconds, visual change every 3 seconds, remove end cues, cut pauses.
3. **Good watch time, few sends or saves:** nothing worth passing on. Add a specific reference value (checklist, cost, comparison) or write for one recognizable person.
4. **Good reach, few profile visits:** the content entertains but does not signal the business. Add credentials in the first 2 seconds, show the product or service, keep topics adjacent to what you sell.
5. **Profile visits, no DMs or clicks:** the profile is not a landing page. Fix bio, pinned posts, CTA keyword.
6. **DMs, few sales:** response time, qualification or offer. Measure time to first reply; script the price answer; check the offer with `offers-pricing`.
7. **Everything fell at once:** check for policy hits (unoriginal content, watermark, engagement bait), account status, a recent change in format mix (all Reels, no carousels), or a long gap. Test archiving failed Trial Reels.

## Reading benchmarks without fooling yourself

- **Denominators differ.** Socialinsider divides by followers (Instagram 0.45% in Q3 2026); Hootsuite uses its own method and reports 3 to 5% for Instagram in some industries; creator benchmarks (Kyra) divide by views. Pick one source, track against it consistently, never average them.
- **Compare with the account's own median first,** then with accounts of similar size in the same industry. LinkedIn at 5,000 to 10,000 followers: 27 reactions is normal, 10 comments is a great post (r/LinkedInTips, 152 pts).
- **Don't abandon a creative change on likes alone.** A county parks account added a recurring illustrated character; for six weeks it lost about 50 followers and likes fell from 22 to 15, but comments rose from 1 to 2 to 6 to 7 per post; it then grew from 1,400 to 3,200 followers in seven months after 14 flat months (r/socialmedia, 34 pts).

## Weekly scorecard (owner report)

One screen, every Monday:

```
Week of ____        Posts: __ (plan __)     Production hours: __
Median views (this week / 8-week median):             __ / __
Non-follower share (median):                           __%
Sends + saves per 1,000 reach:                          __
Profile visits per 1,000 views:                         __
DM starts / keyword triggers:                           __
Leads (email, quote, booking):                          __
Sales attributed (self-reported + UTM):                 __   Revenue: __
Best post (why) / Worst post (why):                     __
Next week: keep __ / test __ / stop __
Decision needed from owner:                             __
```

Monthly: rank pillars and topics by gross profit per production hour; cut the bottom one; double the top one.
