# Pricing, trials, freemium and lifetime deals for software

General price psychology, raise notices and guarantee design live in `offers-pricing`. This file keeps what is specific to SaaS, apps and extensions. Operator numbers are one product each ([sources.md](sources.md)); measured data carries its source and year.

## Pick the first price

- **Order-of-magnitude buckets** (coreyhaines31 pricing, MIT, heuristic): about $10 a month for an individual or prosumer tool, about $100 for an SMB or team tool, about $1,000 for mid-market or sales-assisted. Start near the round number, move within the bucket on evidence.
- **The $9 trap:** across 12 micro-SaaS tools one founder studied, $15 to $39 a month was the self-serve band; "$9 attracts tire-kickers while $99 can require a sales call" (r/microsaas, 187). On web, sub-$5 monthly prices lose about 10% to fixed card fees.
- **Value metric test:** "As the customer uses more of [metric], do they get more value?" If yes, price on it (projects, contacts, minutes, credits). If value does not rise with seats, per-seat pricing invites login sharing (coreyhaines31, MIT).
- **Raise before you cut.** Nine separate founders report raises with flat or better conversion: $11 to $19 entry plan (customers read the higher price as quality, r/SaaS, 383); $29 to $79 single plan with "nobody who paid $29 complained" (r/SaaS, 768); annual $11 to $22 with no conversion change, "the highest-ROI change, took five minutes" (r/AppBusiness, 235); lifetime $7.50 to $22.50 in steps with no drop (r/microsaas, 105); a Mac utility successor at $25 instead of $8 grosses $1,250 instead of $400 on the same 50 sales a month (r/SideProject, 616). Cuts failed: $59 to $9 "without success", $39 worked after product fixes (r/SaaS, 250); repeated cuts brought "less serious users with higher churn" (r/microsaas, 63).
- **Contradiction:** €5 to €12 then €9 "worked best" (r/EntrepreneurRideAlong, 302); an app that cut every price still had $0 revenue because price was not the bottleneck (r/AppBusiness, 79). Rule: raise when users activate and pay without objection; when nobody pays, fix activation or the audience first.
- **Judge any price test by revenue per paywall or pricing-page view,** not per-plan uptake. After raising to €7.99 a month and €39.99 a year, monthly uptake "basically died", yearly held and revenue per view rose (r/SaaS, 438).
- **Show prices in USD** for a global audience: switching from EUR to USD alone raised conversion (r/microsaas, 65).
- Break-even for a raise at 80% gross margin: you can lose p / (0.8 + p) of customers; a 30% raise survives losing 27% ([economics.md](economics.md)).

## Tiers

- **Good, Better, Best,** Best at 2 to 3x Better; or 1x / 2.2x / 5x (swyx heuristic via aaron-he-zhu, Apache-2.0). Never gate the core-value feature; gate what separates casual from serious use (limits, seats, API, SSO, white-label, priority support).
- **Add a higher tier before adding users.** Adding €25 and €55 above €9: 2 customers at €55 matched 12 at €9 (r/buildinpublic, 88). Moving €9/€14 to $19/$29/$39/Custom: more users picked $39 than $19, about 30 took Custom with adjustable limits (r/microsaas, 65).
- **Done-for-you tier on a cheap tool:** DFY packages above $200 became 72% of $8,027 revenue; "selling one premium package was easier than selling ten" (r/indiehackers, 84).
- **Value-based add-ons:** a 40-hour integration first quoted at $200 a month sold for $2,000 up front after the founder asked what it saved (4 hours a week, about $10K a year); two more customers bought it that quarter (r/SaaS, 315). "Redline tax": $8K a year as listed, $15K if the buyer wants contract changes (r/SaaS, 350).
- **Grandfather early customers** when moving $9/$29 to $99/$299 (r/microsaas, 103). Grandfathering is a grace period, not forever: move 5 to 10% of old accounts first, announce 3 to 6 months ahead, offer "lock the old price if you go annual now" (coreyhaines31 pricing, MIT; rollout detail in `offers-pricing`).
- **AI products:** price base plus usage or credits once p90 usage costs more than about 40% of the plan price ([economics.md](economics.md)). Benchmarkit 2026: usage-priced NRR 108% vs seat-priced 98% (correlation). Mootion capped lifetime AI usage with monthly credits (AppSumo case, 2026).
- **Pricing page:** recommended tier highlighted, "who each tier is for", annual toggle, FAQ ("can I cancel", "is there a trial"), prices as HTML text so AI assistants can read them, limits stated in words (coreyhaines31 pricing-page teardown, MIT, lens credited to Kyle Poyar). Page design depth: `website-conversion`.

## Trial, freemium, paid-only, or card-required

Measured ranges (ChartMogul, February 2026, about 200 products): freemium 3 to 5% good, 8 to 12% great; free-to-paid overall 5 to 7% good, 12 to 16% great; card-required trials 25 to 35% good, 50 to 60% great. These are conversion among people who entered each model; they do not prove a gate maximizes revenue per visitor. Decide on visitor-to-paid and retained paid at day 60 to 90.

| Product | Default to test first | Why |
|---|---|---|
| B2B self-serve, $20 to $50 a month | 7-day trial, card required | Four founders agree: fewer starts, much higher paid conversion and engagement (r/buildinpublic, 64; r/microsaas, 65 and 63; r/SaaS, 574) |
| B2B, $100+ a month | Signup, demo, trial only if asked | Sales-assisted routing (r/SaaS, 574) |
| Consumer subscription app | Hard paywall after onboarding, trial on yearly only | RevenueCat 2026: D35 conversion 10.7% vs 2.1% freemium, same 1-year retention ([mobile-apps.md](mobile-apps.md)) |
| Tool with network or output sharing | Freemium with a felt cap | Free users spread it; cap at a natural threshold most users cross |
| Episodic job (resume, one analysis, a wedding) | One-time pass or lifetime | Subscriptions churn when the job ends: resume tool LTV about 3 months at 16% churn (r/SaaS, 2,460) |
| Developer tool or extension with near-zero marginal cost | Free core plus paid power features or lifetime | Lifetime replaced monthly for a Chrome extension after 3 failed months (r/SaaS, 835) |

Trial mechanics:
- **Trial-to-paid peaks around day 7** and falls fast after (ChartMogul GTM report, 2,500 companies, June 2025). For web SaaS, 7 days is the default; extend to 14 only when setup takes days. One founder moved a 3-day card trial to 7 days because users needed time to see value, and conversion improved (r/microsaas, 65).
- **Mobile trial length is a test:** RevenueCat 2026 median trial-to-paid 25.5% at 4 days or less, 37.4% at 5 to 9 days, 42.5% at 17 to 32 days. Correlation; judge on D60 revenue per install, not trial conversion.
- **If most trial cancellations happen on day 1** (users turn off auto-renew at once), test removing the trial: one app saw no drop in conversion, then added a $1.99 weekly plan as a paid trial and many weekly users moved to annual (r/AppBusiness, 235). Keep a 3-day trial on annual only (a commenter's setup across three apps).
- **Weekly plans conflict:** they work when value recurs and fail for one-shot jobs (stock analysis users paid a week and cancelled, r/AppBusiness, 107). Rule: weekly only if the user needs the app every week.
- **Paid trial:** $7 to $10 for 7 days filters tire-kickers (coreyhaines31 activation models, MIT, heuristic).
- **Reverse trial:** full access for the trial, then drop to a free tier, not to nothing. Use when free users drive referrals.
- **Charge the beta:** free beta users hunt edge cases, paying users report what blocks their outcome (r/startups, 310). 97 beta customers at 50% off, "even at $6/month", drove the core redesign (r/SaaS, 283).
- **Card-trial honesty:** some card-trial conversions are people who forgot to cancel (r/buildinpublic, 64). Send a reminder before the charge; surprise renewals turn into refunds, 1-stars and chargebacks.

## Freemium: where to put the limit

- **If free does the core job, nobody upgrades.** Free time tracking into invoices, Pro with Gantt, sync, AI and reports: 49 downloads, 0 Pro in 5 months. Commenters said gate project or invoice counts instead (r/indiehackers, 54).
- **Cap at a natural threshold most users cross:** a wedding app's free tier covers 100 guests when most weddings have 120 to 200+ (558 upvotes, via `offers-pricing`). Free up to 50 slides, one-time unlock for unlimited, on a 130,000-user Figma plugin: about $3,500 in week one (r/buildinpublic, 155).
- **Ask before you gate:** an in-product banner "Would you pay for this?" got about 10% yes on that same plugin.
- **Mobile:** cap the free tier daily so users feel the limit inside the habit, not after a month (coreyhaines31 paywalls, MIT).
- **Measure the free tier:** free-to-paid, time to hit the cap, share of users who hit it, and upgrades within 7 days of the first hit.

## Annual, monthly, lifetime

- **Annual above the fold, framed per month:** "$3.33/mo billed yearly" lifted trial starts per paywall view from 24.1% to 30.1% (not yet significant, r/AppBusiness, 219). Annual hidden below the fold sold "almost zero" (r/AppBusiness, 107). 60% off annual led 70% of users to pick yearly (r/AppBusiness, 164). Keep the billed amount and period visible; App Review rejects paywalls that hide them.
- **Annual as financing:** heavily discounted annual funded ad spend with upfront cash (r/AppBusiness, 129). A $1,000 month on $150 MRR came from annual and lifetime sales (r/AppBusiness, 179). Track cash and MRR separately.
- **Lifetime next to subscription can lift subscriptions** (a 100-upvote commenter after negative reviews about subscriptions, r/androiddev, 796). Price lifetime at about 12 months of subscription (r/AppBusiness, 75), higher if usage costs money.
- **One-time can beat subscription outright** for utilities: a file renamer at $19 to $29 one-time with the user's own API key vs $5 a month managed: 90% chose one-time (r/microsaas, 807). A coding-challenge site made $67K mostly from one-time purchases after subscriptions peaked at $300 MRR (r/SaaS, 406).
- **Lifetime is only safe when marginal cost is near zero:** on-device AI ("another hour transcribed creates no additional transcription API bill") made $7,591 in 28 days (r/AppBusiness, 353); bring-your-own-key lifetime for an AI extension (r/SideProject, 1,629). Lifetime on paid API calls is a liability that grows with every sale.
- **Discounted lifetime can kill MRR:** 42 lifetime vs 7 subscriptions left $24.40 MRR (r/buildinpublic, 53). Do not run a lifetime discount and a subscription discount at the same time.
- **BYOK as a pricing choice, never a setup gate:** requiring the user's own Gemini key lost 90% at that step (r/microsaas, 166).

## Launch pricing and lifetime-deal ladders

- **Capped early price with a real cap:** first 15 buyers at $39.99, then $49.99 capped at 50; an email to users before closing ("closing, price going up, two new features") drove many late conversions (r/microsaas, 59). $24.99 for the first 500 vs $49.99 regular, 7-day no-questions refund: 84 sales in about a day (authenticity questioned, r/microsaas, 218).
- **Public ladders anchor the cheapest step:** first 100 at $14.99, next 200 at $19.99: the first 100 sold in 4 days, then only 11 at $19.99 in two weeks; "$14.99 became anchored as the deal" (r/indiehackers, 36). Prefer one launch price with a date, then the regular price.
- **Descending coupon:** 50% off on day 1, minus 10 points a day, 5-day deadline: $425 in a week after zero paid customers (r/microsaas, 204).
- **Subreddit thank-you code:** lifetime 50% off for the community that supported the launch: first 11 subscribers in two weeks (r/SaaS, 333).
- **Beta seat coupon:** `BETATEST`, Solo plan free for a month, capped at 30, no card, in exchange for "what's useful, confusing, or missing" (r/microsaas, 64).
- **Marketplace lifetime deals (AppSumo and similar):** model net per code against 3 years of cost to serve at p90 usage before applying ([economics.md](economics.md), [launches-and-marketplaces.md](launches-and-marketplaces.md)). Honest scarcity only: a cap must really close, a price must really rise.

## Tricks most owners miss

- Charge for setup or done-for-you on top of a cheap plan; buyers who want outcomes pay 10x.
- Quote add-ons by the customer's saving, not by your dev hours.
- An "Are you sure?" cancel survey is not pricing research. Run Van Westendorp with 100 to 300 target users or a Gabor-Granger "would you buy at $X" split before a big repricing (coreyhaines31 research methods, MIT).
- Show the time-saved math next to the price: "If the app saves you just 30 minutes of management time a month, it's already paid for itself" (r/AppBusiness, 105).
- Raise on new signups first; raise existing customers only with notice and a grace option.
