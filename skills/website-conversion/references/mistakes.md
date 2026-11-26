# Expensive mistakes

Two tables: what the data shows, and what practitioners report losing. Sources in [sources.md](sources.md).

## From the data

| Mistake | What it costs | Do instead |
|---|---|---|
| Hiding fees until checkout | Extra costs are cited by 40% of actionable abandoners, hidden totals by 12% (Baymard 2026) | Shipping cost, threshold and surcharges on the product page and cart |
| Forcing account creation | 18% of actionable abandoners (Baymard 2026); 56% of large sites still ask before confirmation | Guest checkout first, account invite after payment |
| Long checkout | 17% abandon for length; average 23.48 form elements vs 12 to 14 achievable (Baymard 2026) | Field audit, autocomplete, optional fields hidden behind links |
| Judging a form change on submits only | Optimizely's 9-to-3 field test lifted leads 42% with a lead-quality warning (January 2026) | Guardrails: qualified, booked, held, won, revenue per visitor |
| "We'll be in touch" after a high-intent form | Booking rate about 50% before an embedded scheduler vs 80%+ after (NetSPI, vendor 2026) | Calendar immediately after qualification, phone fallback |
| Lazy-loading the hero image | Nuvemshop found deprioritized above-the-fold images were the main LCP cause across 180,000+ stores; fixing them coincided with +8.9% mobile organic conversion (2026, observational) | No `loading="lazy"` above the fold; `fetchpriority="high"` on the LCP image |
| Ignoring mobile as its own funnel | 81% of professional-services visits were mobile, converting 8.3% vs 11.6% desktop (Unbounce 2024) | Device-split reporting; real-phone journeys |
| Stripping desktop depth "because everyone is mobile" | Desktop still converts better in the same data | Fix the mobile action path; keep the detail |
| Stopping an A/B test when it first hits significance | Peeking inflates false positives (Statsig docs, 2026); a false winner can run for months on a small site | Pre-set sample and stop rule, or sequential testing |
| Testing button colors on 2,000 visitors a month | A 20% lift at 3% baseline needs about 13,900 visitors per variant | Ship no-regret fixes; test only big changes |
| Believing "chat users convert 3x" | Body Glove Hawaii: 6.34% vs 1.9% with no control (2025); self-selection | Holdout test; Mindbody's controlled +10.3% MQL to SQL is the evidence standard |
| Relying on an accessibility overlay | FTC ordered accessiBe to pay $1 million for compliance claims (2025); 5,114 US digital accessibility suits in 2025, 69% ecommerce in H1 (UsableNet) | Fix labels, keyboard, contrast and third-party widgets on the money path |
| Review gating or paid reviews | Google bans incentives and gating; FTC rule (October 2024) allows civil penalties per violation; warning letters to 10 firms in December 2025 | One neutral request to every customer |
| Fake timers and stock counts | Blacklisted in EU consumer law; read as fake by shoppers | Real cutoffs ("order in 3 h for same-day dispatch") and real stock |
| Quoting a reference price you never charged | Markdown-pricing lawsuits against Shopify merchants; EU 30-day lowest-price rule | Dated price records; real compare-at prices only |
| Overpaying for speed scores | $50 to $200 "90+ PageSpeed" gigs that fool test tools and sometimes inject spam pages (r/shopify, 157) | Field data and a real phone; audit theme code after outsourced work |

## From practitioners

| Mistake | What it cost | Do instead |
|---|---|---|
| CTAs pointing to the wrong place | $50k+ of Google and Facebook spend sent to a page whose main buttons went to an external site; no leads (r/marketing, 443) | Click every CTA on every device before spend |
| Social links and WhatsApp added to a focused paid page | 0 sales in 3 days vs about 150 a week on the focused version (r/googleads, 74) | No exits on paid pages |
| Affiliate button URL pasted twice | Buyers sent to a 404; the fix was worth $812.40 a month (r/juststart, 76) | Monthly link check |
| Offer buried three-quarters down the page | A menu link to a dedicated page made $120 the first month (r/juststart, 115) | Primary offer in the first screen and the nav |
| Tech-focused headline | Zero signups for a week vs 40 in 2 weeks with an outcome headline (r/indiehackers, 113) | Outcome plus time or number |
| Jargon label in the product | Activation stuck at 30% until "Workspaces" became "Projects" (54%) (r/indiehackers, 70) | Customer words |
| Desktop-only store | Hundreds in ads over 2 months, zero add to carts (r/dropship) | Mobile first test before any spend |
| Surprise fee at checkout | Sales "tanked" within 2 days of a tariff surcharge at checkout (r/ecommerce, 519) | All-in price or the fee beside the product price |
| Long form for emergency search traffic | $1,300 for 3 poor leads (about $433 each) (r/googleads, 21) | Call-first page and call ads for urgent terms |
| Unanswered calls and slow replies | Prospects booked someone else after 30+ minutes; close rate 40% vs 75% when answering within about 5 minutes (r/pressurewashing, 28) | Instant alerts, missed-call text-back, answering service |
| Silent checkout failure | Every new buyer's checkout failed for 14 days after a Stripe price ID change (r/juststart, 43) | Weekly real test order and a health alert |
| Discount code with no market limits | A Germany-only 30% code worked in Austria: 400 orders, about €18,000 lost (r/ecommerce, 36, disputed) | Test every code in every market |
| Dead shipping option left selectable | A customer paid a $99,999 "do not use" rate; Stripe kept several thousand in fees on refund (r/Entrepreneur, 1,065) | Delete, do not rename, unused options |
| Uncapped results guarantee | 20 refunds of $2,600 ($52,000); business closed with $76k debt (r/startups, 270) | Specific, capped guarantees with conditions |
| Redesigning the live site directly | Theme change broke features; pageviews -20% and a $400 repair (r/juststart, 76) | Staging first, then compare 4 weeks |
| Preloader hiding the page | About 13 seconds of loading screen on an admired agency site (r/web_design, 976) | No preloaders; content first |
| Pre-checked recurring donation boxes | A fundraising platform refunded about $122 million (r/userexperience, 138) | Explicit opt-in for recurring and upsells |
| Fake social proof | "23,000+ happy customers" on a store with no sales read as a scam (r/dropship) | Real counts or none |
| Paying a CRO agency before basics | $6,500 the owner says they could have saved by testing themselves (r/juststart, 72) | Run the page audit and five journeys first |
| Bot traffic on serverless hosting | Meta's crawler made 11.2 million requests; bill $30 to $1,933.93 in a month (r/webdev, 3,232) | Check logs and bills; block abusive crawlers |
| Polishing the page instead of the channel | 2 years of landing page changes, still zero cold-email replies (r/Entrepreneur) | Confirm traffic quality and offer before page work |
