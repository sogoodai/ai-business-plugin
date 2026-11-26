# Menu engineering and pricing

The menu is the restaurant's main sales tool and its main cost lever. Manage it on contribution dollars x demand, not food-cost %. Method adapted from ai-restaurant-claude and pm-claude-skills (MIT, see [sources.md](sources.md)), with evidence added and corrections marked.

## 1. Plate costing with yield

For every item, build a costing sheet:

| Line | How to compute |
|---|---|
| As-purchased (AP) cost | invoice price per unit (lb, kg, each) |
| Yield % | edible weight after trim and cooking / purchased weight. Measure it: weigh, trim, cook, weigh again, three times |
| Edible-portion (EP) cost | AP cost / yield % |
| Portion cost | EP cost x portion size |
| Q-factor line | a fixed amount per plate for oil, salt, garnish, sauce cups, bread |
| Packaging line | takeout and delivery only: container, lid, bag, cutlery, sauce cups |
| Plate cost | sum of the lines |
| Item contribution | net selling price (after average discount) - plate cost |
| Food cost % | plate cost / net selling price |

**Worked example (illustrative numbers):** brisket at $5.50/lb AP with a 50% yield after trim and smoke is $11.00/lb EP; a 6 oz portion is $4.13. Two sides at $0.90, Q-factor $0.35, bun $0.40: plate $6.68. At $18, contribution is $11.32 and food cost 37%. A $14 chicken plate at 27% food cost leaves $10.22. The brisket earns $1.10 more per plate even though its percentage looks worse.

Costing errors to catch (pm-claude-skills, MIT): costing at AP price and ignoring yield; chasing food-cost % instead of contribution; repricing a Plowhorse so hard it becomes a Dog; treating supplier price as fixed when spec and portion are the real levers. Label every yield you estimated rather than measured.

**Default food-cost ranges when actuals are missing** (ai-restaurant-claude, uncited, use only as a placeholder): pasta 18 to 25%, pizza 20 to 30%, appetizers 20 to 30%, burgers and sandwiches 25 to 32%, steak and seafood 30 to 40%, desserts 15 to 25%, cocktails 18 to 22% liquor cost, draft beer 22 to 25%, wine by the glass 22 to 30%, coffee and soft drinks 5 to 15%.

## 2. The matrix (Kasavana and Smith)

Run per category (starters with starters), on 90 days of POS data:

1. For each item: units sold, net price, plate cost, contribution, total contribution (contribution x units).
2. **Popularity threshold** = 70% of an equal share = 0.7 / number of items in the category. An item is popular if its share of category units is at or above it. (The source skill used the plain mean; the canonical rule is 70%.)
3. **Contribution threshold** = weighted average contribution = total category contribution / total category units.
4. Classify and act:

| Class | Popularity | Contribution | Action |
|---|---|---|---|
| Star | high | high | Protect recipe and portion, best placement, photo, staff recommend it. Small price tests only. |
| Plowhorse | high | low | Re-cost (portion, spec, cheaper side), rewrite description to carry a raise, raise in small steps, pair with a high-contribution add-on. |
| Puzzle | low | high | Rename and redescribe, move to first position in its category, photo or "chef's pick", bundle or pair it, have staff suggest it. Retest in 6 weeks. |
| Dog | low | low | Remove or convert (an entree salad becomes a side). Keep only if it anchors a group, serves a dietary need, or uses ingredients you must stock anyway. |

5. Then check what the matrix misses:
   - **Labor and complexity:** a cheap-ingredient special needing the only two cooks who know it, with uneven demand and high waste, cost more than it looked. One owner cut a weekly pinto bean special and prime cost improved, despite pushback from regulars (operators report).
   - **Orphan ingredients:** items that force stock used nowhere else are first to cut (operators report).
   - **Substitution:** raising one item shifts demand to its neighbors. The steakhouse field experiment that raised entrees about 2% with substitution-aware placement gained 1.8% net revenue, about $28,800 a store across 48 outlets ([IJHM 2020](https://www.sciencedirect.com/science/article/pii/S0278431920300566), possibly outdated).
   - **Component reconstruction:** a guest rebuilt $25 fajitas from a $10 salmon side, $3 vegetables and $1 tortillas: an $11 gap per order. A $4 plain hot dog plus $2 syrup, $2 ricotta, $2 bacon and $1 onions totals $11 against an $8 signature version (operators report). Price custom builds at or above the comparable dish.

**Quick wins, in order** (ai-restaurant-claude, MIT): move Stars to prime positions; rewrite Plowhorse descriptions before raising them; give Puzzles a photo, badge or pairing; remove or convert Dogs; add 2 to 3 add-ons (the source claims an 8 to 12% ticket lift, uncited). Rollout: this week placement and add-ons, within 2 weeks copy and prices, within 30 days photos, within 60 days reprint.

**Practitioner patterns worth testing:**

- Pause the bottom 20% of sellers even if they seem to be favorites; pick 2 to 3 high-contribution anchors and give staff agreed words to sell them (operators report, untested).
- Use a compact menu with shared ingredients. A 55-seat full-service place ran full houses with 2 to 3 cooks and a dishwasher that way (operators report).
- Add the basic version guests keep asking for. One operator resisted, added it, and it became the number one seller at every location (operators report).
- Real gluten-free dishes, not just gluten-free bread: +30% sales overnight in one nine-year-old restaurant (operators report). Never claim gluten-free without the owner confirming kitchen practice.
- Try new dishes as specials first, and keep a regular burger next to the fancy one in a small market.
- Rotate one monthly special and keep the core stable; private and corporate buyers book the core (truck operator).
- Don't serve distributor show specials as presented: guests notice identical dishes at nearby bars.
- Sell a sauce as a product: ranch at $1.29 for 4 oz and $5.99 for 16 oz, 20 gallons a day across three stores, guests coming in only for tubs (operators report).

## 3. Menu design: what the evidence supports

| Tactic | Evidence | Rule |
|---|---|---|
| Drop currency symbols | Guests with numeral-only prices spent significantly more than with "$" or prices in words; 201 diners at a CIA cafe, lunch; coverage reports about $5.55 (about 8%) more. [Yang, Kimes and Sessarego 2009, IJHM 28(1)](https://news.cornell.edu/node/273666), possibly outdated, one site | Use "16" not "$16.00" for full-service and cafes; test on check average |
| "Sweet spot" top right, golden triangle | Eye tracking (25 subjects) found guests read menus like a book, no sweet spot; a "sour spot" at the bottom corners. [Yang 2012, IJHM](https://www.eurekalert.org/news-releases/829582), possibly outdated | Put the item you want sold first in its category and at the top of the page; nothing important in bottom corners. Don't pay for a redesign sold on the golden triangle |
| Descriptive names | Descriptive labels sold 27% more in a 6-week cafeteria field study and were rated higher quality and value ([Wansink, Painter and Van Ittersum 2001, Cornell HRA Quarterly 42(6)](https://foodservicedirector.com/menu/menu-descriptions-help-sales-study-says)). Wansink resigned from Cornell in 2019 after many retractions; treat as weak | Specific, true descriptions: technique, named ingredients, origin. Test, don't promise 27% |
| Decoy or anchor item | Mixed: online RCTs in Appetite (2020) found no effect of a price-based decoy; an International Hospitality Review study (2024) found decoys pushed choices toward pricier restaurant bundles | Keep one premium anchor if it sells some units; never as the only tactic |
| Substitution-aware placement | Steakhouse field experiment above (2020) | Move and price neighbors together |
| Photos, item count, charm prices, inline prices | ai-restaurant-claude claims 20 to 30 items is the "sweet spot", photos on 30 to 50% of digital items and 0 to 20% of print, items with photos sell 30 to 50% more on delivery apps. All uncited | Heuristics only. On delivery apps photograph every Star and Puzzle |

**Description rubric** (ai-restaurant-claude, MIT): 15 to 30 words; a sensory verb (charred, slow-braised); 2 to 3 named ingredients; origin or technique; one differentiator. Reject plain component lists, anything over 40 words, and under 8 words on items over $20. Worked rewrite: "Traditional lasagna with meat sauce" becomes a line naming a 6-hour Bolognese, fresh ricotta, Grana Padano and the family recipe year, supporting $17 to $18.50.

**Name things the way guests order them.** Cafes: "espresso macchiato" grouped with espresso and americano, plus a sign that it is not the Starbucks drink. Retail coffee bags: "sweet", "lime", "stone fruit", "nutty" instead of "rock candy" or "kaffir lime", and no cupping scores, which describe green-coffee samples, not the brewed cup (a 20-year green coffee importer and Q Grader). Date every downloadable menu: operators report third-party sites showing 3 to 4-year-old menus and guests demanding 2014 prices. Keep one permanent menu URL and replace the file.

## 4. Add-ons, modifiers and the free extras

- **Charge for real upgrades:** protein $2 to $4 ("add meat to any pasta $4", 90%+ margin), premium toppings $3, truffle $7, dessert duo + espresso $8 (ai-restaurant-claude, uncited prices).
- **Hidden build-your-own POS button:** an unadvertised "custom" item that opens ingredient groups with priced modifiers lets staff handle exceptional requests consistently (taqueria and burger operators).
- **Do not nickel-and-dime the expected:** a $2 charge for Thousand Island on a Reuben lost a once-or-twice-a-month regular; a $0.50 ranch charge turned guests off (operators report). Measure first: free extra ranch and charcuterie crackers cost under 0.1% of food cost over a year; pickles cost about $0.006 a slice.
- **Fold the extra into the price instead:** mussels +$3 with more bread included, no drop in sales and no complaints; "raise the price $1 and include two sauces"; include the first ranch or blue cheese cup with wings, charge for dipping sauce with pizza (operators report).
- **Make the paid portion visible before ordering:** if more than half of orders ask for more bread, raise the starting portion from 2 slices to 3 and list "Double the bread! 3.00".
- **Container size is perceived value:** a $7 potato salad looked stranded in an oversized box; a smaller container, leaf lettuce, aioli and chives cost almost nothing. Choose the sauce cup that looks full at the portion you sell.
- **Cheap bulk on the plate:** a bigger portion of fries makes guests leave full at little cost (operators report).

## 5. Pricing and price increases

**Set prices** by target contribution, then check the market:

- Plate cost / target food-cost % gives a starting price; a takeaway operator prices at about 3x ingredient plus packaging cost, then adds VAT (operators report).
- Compare 5 to 7 competitors within 3 miles at the same cuisine and price tier on 3 to 5 signature dishes plus one dish everyone sells. Flag "underpriced" more than 8% below the average without a value reason, "overpriced" more than 10% above without a premium reason (ai-restaurant-claude, MIT).
- Use Toast's Menu Price Monitor for the item and city where available ([benchmarks.md](benchmarks.md)).

**Raise prices: the playbook**

1. **Item by item.** Price movement differs by product (coffee +7.1%, wings +0.7% in Sept 2026, Toast). Raise inelastic signatures and drinks first; keep high-elasticity impulse items (desserts) at or below competitors.
2. **Small, regular steps.** Never more than 12% in one move (ai-restaurant-claude). Owners who raised most items by 0.50 to 1.00 after months of stagnant cash saw the account grow about 25,000 in two months; another said waiting too long caused the stress (operators report).
3. **Keep a visible entry anchor.** One owner keeps a "rotisserie chicken" item priced at no profit so budget guests still come; sales grew two years running (operators report). In tourist towns keep staples locals can afford 2 to 3 times a week and add 2 to 3 shareable showpieces for visitors; raising the staples drove regulars away (operators report).
4. **Attach visible value.** 72% of consumers tolerate local increases paired with added value (Square 2026) while only 18% of diners see restaurant hikes as justified (Toast 2026). Better bundle, bigger side, included sauce, loyalty privilege.
5. **Sequence** (ai-restaurant-claude, MIT, uncited rationale): week 1 drinks (+$2 wine by the glass, +$1 cocktails), week 2 add-ons, week 3 underpriced entrees, weeks 4 to 6 a premium anchor, month 2 bring overpriced items down and improve their copy.
6. **Temporary costs get temporary surcharges, clearly labeled.** An NYC cafe with a roastery added 1% to all sales until it recouped tariff costs; most guests understood (operators report).
7. **Measure for 4 to 6 comparable weeks:** units per item, mix, transactions, contribution per check, complaints. Reverse what lost total contribution.
8. **Never defend a raise in a review reply** by citing your expansion costs or comparing yourself with a Michelin restaurant; a longtime guest who saw a bill 2.5x higher only got angrier (operators report).

**Beverage levers** (ai-restaurant-claude, uncited): a $50 bottle poured at $14 a glass is 28% cost, move to $16; beverage margins run 70 to 85% vs food 60 to 72%. A restaurant already licensed for private events added beer and spiked versions of its mocktails and saw alcohol add 20 to 50% to many bills (operators report; licensing can be expensive, check first). Keep the local cheap beer at a familiar town-bar price in rural places.

**Psychological pricing that operators report** (untested anecdotes): a coffee shop next to a church priced its top drink to total $6.66 and guests usually added a muffin; a $5.99 meal plus tax hit $6.41, and a $0.25 sauce made it $6.66, so a quarter to a third of guests bought something extra. Use with care and taste.
