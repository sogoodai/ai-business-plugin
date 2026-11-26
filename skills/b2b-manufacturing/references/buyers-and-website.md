# How buyers find suppliers, and the website that gets the RFQ

Numbers carry source and year; full URLs in [sources.md](sources.md). Website mechanics shared with every business live in the `website-conversion` skill and search depth in `seo-content`. This file keeps the industrial angles.

## How technical buyers find suppliers in 2026

GlobalSpec/TREW 2026 (1,000+ engineers and technical buyers, vendor-sponsored):

- **62% of the buying process is done before the first vendor contact.** The shortlist forms on third-party pages, the supplier's own site and in conversations with peers. 6sense 2026 (broad B2B) found the shortlist order already set before first contact in 91.4% of deals.
- **Where they research routinely:** online technical publications 76%, supplier websites 74%, print publications 53%, sales or application engineers 41%, directories 31%, YouTube 30%, associations 28%, trade shows 27%, webinars 27%, newsletters 24%, generative AI 21%, LinkedIn 11%.
- **Brand familiarity decides ties.** 70% pick the better-known brand when two solutions are technically similar. Being named in trade publications, distributor catalogs and association channels matters even when it produces no last-click form.
- **What makes them contact sales:** pricing or inventory questions 26%, validating what they found online 23%, technical complexity 21%. Only 10% avoid sales on principle. So the site answers the qualification questions and makes a human easy to reach for the rest.
- **How they want to be contacted first:** email 59%, phone 22%, LinkedIn DM 1%.
- **What they value:** datasheets 79%, CAD drawings 37% (2025 edition).

Agent rules that follow:

1. The website is the main sales rep. Audit it before buying any traffic.
2. Get named where engineers already read: trade publications (editorial, application stories, bylined technical articles), distributor and CAD catalogs, association directories. Treat these as brand work measured by branded search and direct RFQs, not by last-click.
3. LinkedIn is for reaching named people at named accounts, not for primary technical research. Do not plan it as the discovery channel.
4. Ask every new RFQ "how did you find us?" in a free-text field and log it. Self-reported source catches trade publications, word of mouth and AI answers that analytics misses.

### Search and AI answers changed the click, not the job

- Google AI Mode rolled out in the US in May 2025. Google's 2026 documentation says no special schema, AI markup, `llms.txt` or content "chunking" is needed or helps for AI Overviews and AI Mode: pages must be indexable and useful under normal Search rules.
- Pew (March 2025, 68,879 consumer searches): with an AI summary, users clicked a traditional result 8% of the time versus 15% without; 1% clicked a source inside the summary. Expect fewer organic clicks for generic questions. Measure qualified RFQs from organic, not sessions.
- Grey Matter (Aug 2026, 592 US lower-middle-market manufacturers): the median firm ranks for about 404 keywords and gets about 1,100 organic visits a month; the top 10% take 65% of measured organic traffic. Most small manufacturers have thin sites, which leaves room for a specialist with deep pages.
- Search intent is narrow and technical: process + material + tolerance or spec + certification + industry + geography ("5-axis titanium machining AS9100", "food grade stainless fabrication Ohio"). Part numbers and competitor part numbers carry the highest intent.

**Tricks most owners miss**

- Pull Search Console queries that already earn impressions at position 8 to 30, and build one page per missing specification dimension (material, tolerance band, industry, certification). This is the cheapest SEO win in the segment.
- Mine your RFQ inbox and sent quotes for page material: the exact nouns buyers use, the questions estimators keep answering, the reasons you declined work. That is your keyword list and your FAQ.
- Publish a cross-reference or "equivalent to" page if you make a part that replaces a known OEM or competitor part number, where your claims are true and the comparison is accurate.
- A competitor-versus-us page catches people searching the competitor's name ([r/Entrepreneur 1,469](https://www.reddit.com/r/Entrepreneur/comments/2y66lj/37_tactics_i_used_to_grow_my_company_to_50kmonth/)). Keep it factual.
- A wholesale or bulk page targeting "[product] wholesale" and "buy [product] in bulk", supported by 7 to 8 internal links and one paid link, reached the top result and drew buyers from three countries at about $4,000 a month from 300 visitors (operators report, [r/SEO 209](https://www.reddit.com/r/SEO/comments/lbldd4/how_i_earned_4000_per_month_from_the_page_that/)). Buying links carries penalty risk ([r/Entrepreneur 2,924](https://www.reddit.com/r/Entrepreneur/comments/5vtkwo/for_11_years_i_have_been_ranking_ecommerce_stores/): three years of removal requests); prefer a supplier or association link.

## The capability page: a searchable sales engineer

Page order for each core process or product line (research synthesis, GlobalSpec 2026 logic):

**What it is, who it is for, exact capabilities, limits, materials, certifications, tolerance or performance envelope, lead-time logic, files, examples, next step.**

Must-have facts, all on the page and in text (not only in images or PDFs):

| Block | What to show | Why |
|---|---|---|
| Capabilities | Processes, max part envelope (X x Y x Z), weight, tolerances you hold routinely vs on request, finishes | Engineers disqualify on envelope and tolerance first |
| Equipment list | Machine make, model, axes, bed size, count | Buyers check capacity and redundancy; also ranks for machine-specific searches |
| Materials | Every alloy, polymer, food-grade or medical grade you run, plus what you do not run | Saves a call; the "do not" list cuts junk RFQs |
| Certifications | ISO 9001, AS9100, IATF 16949, ISO 13485, ITAR registration, SQF/BRC/FSSC 22000, UL, with cert number and expiry | Procurement checks this before anything else |
| Quality documents | FAIR (AS9102), PPAP level, CoC, material certs, CMM reports, what is standard vs charged | Paperwork is a hidden cost; state it up front (see [quoting-and-pricing.md](quoting-and-pricing.md)) |
| Volumes and MOQ | Prototype to production quantities, MOQ, annual volume sweet spot | Stops mismatched RFQs |
| Lead time logic | Typical ranges by job type, and what makes it longer | "2 to 3 weeks for prototypes, 4 to 6 for production after FAI approval" |
| Industries and applications | One short application story per industry with a number | Buyers search by application |
| Files | Datasheets, spec sheets, CAD (STEP, IGES, DXF, native), drawings, installation guides | Datasheets are the most-valued asset (79%, 2025) |
| Next step | One primary CTA: upload a drawing for review | One clear ask per page |

**Tricks most owners miss**

- **One capability matrix, three copies.** Keep the website page, the downloadable PDF line card and the sales or AI knowledge base identical. Gartner (2024) found 69% of B2B buyers met inconsistencies between the vendor site and the salesperson, which kills trust. When a limit changes, change all three the same day.
- **Publish the "we do not do" list.** "We do not anodize in-house; we manage it through a certified partner" or "No parts over 2,000 lb." It lowers RFQ count and raises RFQ quality, which is what the estimator needs.
- **Standard builds with visible prices** beat the word "custom", which signals "unaffordable" to small buyers. List a few standard configurations with prices and a buy or order button, and take paid changes on top ([r/smallbusiness 710](https://www.reddit.com/r/smallbusiness/comments/17050bx/business_is_failing_struggling_to_get_out_of_this/), 48-upvote comment).
- **Price ranges for configurable equipment.** Buyers of six- and seven-figure equipment want a worst-case range for the cheapest and the most expensive model before the configuration meeting ([r/manufacturing 48](https://www.reddit.com/r/manufacturing/comments/ob25am/do_you_think_b2b_pricing_or_lack_thereof_on/)). A range saves both sides a wasted meeting. Name the spec that moves price most (example from the same thread: 1 kV vs 5 kV isolation) so nobody holds you to a ballpark that ignored it.
- **Shipping-cost check on product pages** for stock or catalog items: ZIP code and residential or business only, no contact details, reused on later pages. A buyer reported buying from a small shop with this even though shipping cost more than Amazon ([r/smallbusiness 1,076](https://www.reddit.com/r/smallbusiness/comments/man5ow/1_reason_that_i_leave_a_small_website_without/)).
- **Callback button instead of only a phone number** (call, SMS or WhatsApp), logging the page URL with each request: about $50 of revenue per callback request and more pre-sale than support calls in one shop (operators report, [r/Entrepreneur 1,120](https://www.reddit.com/r/Entrepreneur/comments/8brjty/i_replaced_my_phone_number_with_a_call_me_back/)).
- **Wholesale catalog for resellers:** unit price, suggested retail price and MOQ next to every product photo ([r/Entrepreneur 1,874](https://www.reddit.com/r/Entrepreneur/comments/15yu0h2/i_started_a_business_4_months_ago_and_its_already/)). Phone photos are fine.
- **Hours that match buyers.** Plant and maintenance buyers email at 5 to 6 a.m.; one firm opened at 7 a.m. while competitors opened at 9 or 10 (operators report, [r/smallbusiness 2,164](https://www.reddit.com/r/smallbusiness/comments/1glwmq3/lost_my_biggest_client_because_i_missed_their/)).
- **Claims rules.** "Made in USA" must be "all or virtually all" made in the US under the FTC rule. UL, CE and certification marks have usage rules. Government customers often forbid naming the agency or using its logo. Check before writing "trusted by the US Air Force" (coreyhaines31 manufacturing pack, MIT).

## The RFQ form and what happens after submit

Benchmarks: manufacturing sites convert about 2.2% of unique visitors to any conversion (First Page Sage client data, 2022 to 2025); DACH industrial firms 1.9% visitor-to-lead (Brixon, 2025). Both agency datasets with different definitions. Measure your own funnel in layers (below) rather than chasing one rate.

Form fields: only what changes qualification or the quote.

- Required: name, company, work email, part or application description, file upload.
- Strongly recommended: material, quantity (per order and annual), target date, certifications or quality documents required.
- Optional: phone, target price, "how did you hear about us" free text, "is this a new part or a current supplier switch?"
- File upload: accept STEP, IGES, SolidWorks, DXF, DWG and PDF, multiple files, at least 50 MB. State that you sign the buyer's NDA on request and how files are stored. For controlled data (ITAR, EAR), say how you handle it and do not take controlled files through a generic form.
- Never force buyers to pick a "buying stage" or persona.
- Add reCAPTCHA and ask for company name to filter bots ([r/b2bmarketing 46](https://www.reddit.com/r/b2bmarketing/comments/1rjq6nl/our_best_b2b_marketing_strategy_in_2026/)).

CTA wording that pre-qualifies (research synthesis, not a tested benchmark):

> **Request a manufacturability and quote review**
> Upload your drawing, CAD file or specification. Tell us quantity, material, required date and any certification requirements. We'll confirm fit first, then quote viable work.

After submit:

1. Automatic acknowledgement within minutes that names the next step and the date (wording in [scripts.md](scripts.md)).
2. A human fit check the same business day: quote, ask one round of questions, or decline with a reason. A fast, polite decline earns the next RFQ.
3. Log the RFQ with source, files, quantity, value band and decision.

### Measure the funnel in layers

| Layer | Example events | Use |
|---|---|---|
| Technical engagement | Datasheet, CAD, configurator, spec page depth | Intent signal, nurture; never an SQL by itself |
| RFQ submitted | Form, emailed drawing, phone RFQ logged | Secondary conversion |
| Qualified RFQ | In capability, real quantity and date, not a student or competitor | Primary conversion for ads |
| Quote sent | Value, expected margin, estimator hours | Pipeline |
| PO | Value, gross profit | Truth |

Do not let ads or SEO reports collapse these into one "conversion". A CAD download from someone who never asked for contact goes to nurture, unless the account is already active.

### Gating: asymmetric

- Keep datasheets, standard specs and standard CAD ungated: discovery and specification matter more than the email.
- Gate only things with clear extra value: custom CAD, configurators, design guides, calculators, application handbooks. In 2026, 85% of technical buyers would share contact info for valuable technical content; 47% for a guide or ebook, 37% a white paper, 34% a CAD drawing; 15% never fill a form.
- CAD platform claims ("92% prefer suppliers with CAD, 90% of downloaded parts get purchased") come from TraceParts' own 2020 user survey: old and self-selected. Do not use them to forecast ROI. Publish CAD because engineers need it to design you in.

**Tricks most owners miss**

- **Getting specified is the real conversion.** An engineer who puts your part number or process in a drawing creates years of orders. CAD files, spec sheets, application notes and configurators exist to win that moment (coreyhaines31 manufacturing pack, MIT).
- **List your CAD on TraceParts or CADENAS PARTcommunity and your parts on the catalog distributors your engineers use** (Grainger, McMaster-Carr, MSC for MRO; Digi-Key, Mouser, Arrow for electronics) where that fits the channel plan.
- **Export controls.** ITAR and EAR limit what technical data you may publish or send abroad. Do not post CAD for controlled items; check with counsel.

## Thomasnet and directories

Thomas reported 1.4 million registered buyers and 1.5 million+ monthly sourcing sessions across 78,000+ categories in April 2025 (platform claim; Thomas sells supplier advertising). Industry directories are a routine research source for 31% of technical buyers (GlobalSpec 2026).

Procedure:

1. Claim the free Thomasnet profile. Pick every category you genuinely serve, no stuffing.
2. Mirror the exact capability words from your website. Add certifications, equipment, materials, tolerances, geography served, photos and downloadable documents.
3. Tag the website link with UTMs and log Thomasnet RFQs as their own source.
4. After 90 days, compare referral sessions, RFQs, qualified RFQs, quotes and POs by category. Buy upgraded placement only for categories that already produce qualified RFQs on the free profile.
5. Repeat for the directories that matter in your sector: GlobalSpec (engineering components), IndustryNet, Kompass and Europages (EU), MFG.com, association member directories, state manufacturing directories, SAM.gov registration for government work.

No public dataset gives a Thomasnet RFQ-to-order rate. Use only your own CRM.

**Tricks most owners miss**

- Paid directories that cannot prove lead quality burn money: $1,500 a month on Clutch gave 0 qualified leads out of 100 (bots, SEO pitches, job seekers) with six months still billed ([r/smallbusiness 660](https://www.reddit.com/r/smallbusiness/comments/1flliys/thinking_of_using_clutch_think_again_they_are/)). Never sign a 12-month directory contract before a measured trial.
- A paid trade publication article bought about 2,800 visitors for $2,100 and no sales ([r/Entrepreneur 1,041](https://www.reddit.com/r/Entrepreneur/comments/9blez4/heres_my_real_attempt_at_starting_a_web_business/)). Editorial coverage and bylined technical articles beat paid placements; pitch an application story with numbers instead.
- Answer sourcing requests where buyers post them. On r/manufacturing a buyer asked for a US partner to flavor 2 million toothpicks; a Canadian supplier replied "Can definitely help as we run a GMP certified manufacturing facility but be aware that we're located in Canada. Message if you're interested" and the buyer answered "Canada should be fine. I'll dm you" ([r/manufacturing 47](https://www.reddit.com/r/manufacturing/comments/1kewcjl/looking_for_a_us_partner_to_flavor_2_million/)). Lead with the certification and disclose the constraint.
- Quoting marketplaces and manufacturing networks send work at prices they set. Treat them as capacity filler for idle machines, not as a brand channel, and track their margin separately.

## Content that technical buyers and shop people share

- **Show the hard job with exact numbers.** An archived company video of connecting-rod grinding at .00015 in roundness and .0003 in size tolerance, posted to r/Machinists with the constraints explained in comments, drew 3,652 upvotes ([r/Machinists 3,652](https://www.reddit.com/r/Machinists/comments/12jwve8/fun_job_this_is_an_experimental_connecting_rodhad/)). Most shops have this footage "collecting dust".
- **An absurd demo part announces a new capability.** SendCutSend's busy CNC part video drew 9,802 upvotes, with "Advertising done correctly" at 1,374; viewers watched two dozen more reels and learned the company now did CNC ([r/Machinists 9,802](https://www.reddit.com/r/Machinists/comments/1qcmjcg/thought_you_might_admire_this_part/)). Machinists noted the geometry was easy for the right machine: impress buyers, not peers.
- **Inspect a famous product.** Lumafield CT-scanned the Heinz cap with "Heinz spent 8 years and $1.2 million developing its new ketchup cap. We put one in our CT scanner to look inside..." ([r/manufacturing 471](https://www.reddit.com/r/manufacturing/comments/1b44g0i/heinz_spent_8_years_and_12_million_developing_its/)). Any test lab, metrology or failure-analysis firm can copy the format.
- **Teach the people who use your product.** A candle-supply seller grew a Facebook group from 52,000 to 105,000 members and YouTube from 62,000 to 108,000 by showing supplies in use, about 20 educational posts per promotional ask, then sold 25-seat paid classes every 2 to 3 months ([r/Entrepreneur 1,885](https://www.reddit.com/r/Entrepreneur/comments/qmpgla/update_4_years_later_started_a_candle_side_hustle/)).
- **Decision-stage videos.** About 30 comparison and how-it-works videos at 350 to 400 views a day were reported to feed 500+ sales calls at about 50% close for a B2B firm (secondhand, [r/b2bmarketing 103](https://www.reddit.com/r/b2bmarketing/comments/1qsteye/how_a_b2b_company_makes_millions_with_their_tiny/)). YouTube is routine research for 30% of engineers (2026).
- **Founder or engineer posts on LinkedIn beat the company page.** Launches got 3 to 5x the reach of normal posts; real photos and candid failures did best ([r/b2bmarketing 47](https://www.reddit.com/r/b2bmarketing/comments/1rvnpxw/10k_linkedin_followers_in_under_2_years/)). Use them as Thought Leader Ads later ([paid-ads.md](paid-ads.md)).
- Day-to-day posting cadence and formats live in `organic-social`.
