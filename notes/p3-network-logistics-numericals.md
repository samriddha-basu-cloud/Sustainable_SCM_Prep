# CO4 Numericals: Distribution Networks, Logistics Cost & Distance Criteria
This page covers **CO4: SSCM distribution networks, logistics cost and distance criteria**. CO4 is one of the two **10-mark** COs of the end-sem paper (Lecture 11 📘). It starts with the **exact problems from Lecture 8** 📘 (the network A/B/C trade-off and objective function, the 10,000-returns allocation, and the consumer-electronics network exercise) and the **Lecture 10 FMCG distribution scenario** 📘, then the standard distance-criterion methods (load-distance, centre of gravity, factor rating), transport-emission and consolidation numericals, and the ITC eChoupal network economics 📘. Practice data are marked 📗. Turn on **Self-test** (`T`) to hide answers.

Theory: [Sustainable Logistics](ch06-sustainable-logistics.md) and [Designing the Sustainable Network](ch07-network-design.md).

---

## Formulas and conventions for CO4 ⭐⭐⭐
**Sustainable network objective (Lecture 8 📘):** Minimise **Total cost + Environmental cost + Social cost**.
- *Total cost* = facility cost + production cost + transportation cost + inventory cost + collection cost + recovery cost + disposal cost.
- *Environmental* = CO₂ emissions + energy consumption + waste + resource consumption.
- Mathematical form: **Minimise Z = C_total + λ·E_CO₂ + μ·W_waste**, where λ is the price (weight) put on each unit of CO₂ and μ on each unit of waste.
- Decision variables: **xᵢⱼ** = quantity transported from node i to node j; **yⱼ** = 1 if facility j is opened (0 otherwise); **rᵢ** = quantity recovered from returned products.
- Constraints: demand satisfaction, facility capacity, material balance, transport capacity, recovery capacity, collection constraints, recycling targets, non-negative flow. At every recovery facility: **Returns = Reuse + Repair + Remanufacture + Recycling + Disposal**.
- *"The model searches for a **Pareto-efficient** solution"* — one where you cannot reduce cost without increasing CO₂ (or vice versa).

**Transport emissions:** CO₂ = tonnes × km × emission factor (kg CO₂e per tonne-km), or CO₂ = litres of fuel × 2.68 kg/l for diesel. Lecture 8's mode hierarchy: **Air > Road > Rail > Water** in emission intensity; *actual performance depends on distance, load factor, vehicle and operating conditions.*

Illustrative emission factors used below (📗, state as assumptions in the exam): road truck 0.09 kg CO₂e/t-km, rail 0.025, inland/coastal water 0.015, deep-sea container 0.015, air freight 0.60.

**Distance criteria:**
- **Load-distance (ton-km) score** = Σ (load × distance). The site with the lowest score minimises transport effort, cost and (roughly) emissions.
- **Centre of gravity:** Cx = Σ(xᵢ·Wᵢ) ÷ ΣWᵢ, Cy = Σ(yᵢ·Wᵢ) ÷ ΣWᵢ (Wᵢ = volume shipped to/from location i). It gives a *starting* location, not always the exact optimum.
- **Euclidean distance** = √((x₁−x₂)² + (y₁−y₂)²); **rectilinear** = |x₁−x₂| + |y₁−y₂|.

**Logistics KPIs (Lecture 8 & 10):** vehicle utilisation % = load carried ÷ capacity; empty km % = empty km ÷ total km; g CO₂e per tonne-km; cost per unit; return rate, recovery rate, reuse rate, remanufacture rate, recycled content %.

---

## Problem 1. Network A, B or C? (Lecture 8, slides 36–37) 📘 ⭐⭐⭐
Lecture 8's simplified sustainable network example:

| Network | Cost | CO₂ | Recovery |
|---|---|---|---|
| A | ₹100 | 100 | 20% |
| B | ₹108 | 75 | 50% |
| C | ₹115 | 55 | 70% |

*"Question for students: for the example quoted, which network is best? Answer: there is no single answer without defining decision-maker priorities."* Objectives on the slide: minimise total cost, minimise CO₂ emissions, maximise recovered material, maximise social benefit.

**Q1.1 Is any network dominated? Which ones are Pareto-efficient?**
A network is **dominated** if another is at least as good on every objective and better on one. Here A is cheapest, C is lowest-CO₂ and highest-recovery, and B is in the middle on all three. No network beats another on every criterion, so **all three are Pareto-efficient**; the choice depends on priorities (weights) or on prices put on carbon and recovery.

**Q1.2 Compute the trade-off ratios: how much extra cost buys each tonne of CO₂ reduction?**
- A → B: +₹8 for −25 CO₂ → **₹0.32 per unit of CO₂ avoided**, and +30 points of recovery.
- B → C: +₹7 for −20 CO₂ → **₹0.35 per unit of CO₂ avoided**, and +20 points of recovery.
- A → C: +₹15 for −45 CO₂ → ₹0.333 per unit.

**Q1.3 Use the objective function Z = Cost + λ·CO₂ (ignore recovery). For which carbon price λ is each network best?**
- Z_A = 100 + 100λ; Z_B = 108 + 75λ; Z_C = 115 + 55λ.
- A = B when 100 + 100λ = 108 + 75λ → 25λ = 8 → **λ = 0.32**.
- B = C when 108 + 75λ = 115 + 55λ → 20λ = 7 → **λ = 0.35**.
- **Result:** λ < 0.32 → **A** best; 0.32 < λ < 0.35 → **B** best; λ > 0.35 → **C** best. Check at λ = 0.5: A = 150, B = 145.5, C = 142.5 → C. At λ = 0.2: A = 120, B = 123, C = 126 → A.

**Q1.4 Now add a value of μ = ₹0.10 per percentage point of recovery (as a benefit). Z = Cost + λ·CO₂ − μ·Recovery. With λ = 0.30, which network wins?**
- Z_A = 100 + 30 − 2 = **128**; Z_B = 108 + 22.5 − 5 = **125.5**; Z_C = 115 + 16.5 − 7 = **124.5**.
- **C wins**, although at λ = 0.30 alone A would have won (A 130, B 130.5, C 131.5). Valuing circularity shifts the choice towards the closed-loop network.

**Q1.5 Solve with weighted scoring (min–max normalisation, 0 = worst, 1 = best) for three management priorities.**
Normalised scores: Cost — A 1.000, B (115−108)/15 = 0.467, C 0.000. CO₂ — A 0.000, B (100−75)/45 = 0.556, C 1.000. Recovery — A 0.000, B 30/50 = 0.600, C 1.000.

| Priority (weights cost/CO₂/recovery) | A | B | C | Choice |
|---|---|---|---|---|
| Cost-led (0.6 / 0.2 / 0.2) | 0.600 | 0.280 + 0.111 + 0.120 = **0.511** | 0.400 | **A** |
| Balanced (⅓ each) | 0.333 | **0.541** | **0.667** | **C** |
| Green (0.2 / 0.4 / 0.4) | 0.200 | 0.555 | **0.800** | **C** |

**Q1.6 Write the managerial answer.**
"There is no single best network without decision-maker priorities." A cost-led firm picks A; any firm that prices carbon above ~₹0.35 per unit, or gives balanced weight to environment and circularity, picks C. B is a sensible **transition** network (costs only 8% more than A but cuts CO₂ by 25% and recovers 50%). The Lecture 8 conclusion: *"The best sustainable network is not necessarily the cheapest network."* *"Create the lowest-cost network that delivers the required service while minimising environmental impact and maximising resource circularity."*

---

## Problem 2. Allocating 10,000 returned units (Lecture 8, slide 37) 📘 ⭐⭐⭐
At the recovery facility, **Returns = Reuse + Repair + Remanufacture + Recycling + Disposal**:

| Stream | Units |
|---|---|
| Reuse | 2,000 |
| Repair | 2,500 |
| Remanufacture | 2,000 |
| Material recycling | 3,000 |
| Disposal | 500 |
| **Total** | **10,000** |

*Question on the slide: where should each stream go to minimise cost and environmental impact?*

**Q2.1 Verify the material balance and compute the circularity KPIs.**
2,000 + 2,500 + 2,000 + 3,000 + 500 = **10,000** ✓.
- **Recovery rate** = (10,000 − 500) ÷ 10,000 = **95%**.
- **Value-retaining recovery** (reuse + repair + remanufacture, the top of the hierarchy) = 6,500 ÷ 10,000 = **65%**.
- **Reuse rate** = 20%; **remanufacture rate** = 20%; **recycling** = 30%; **disposal to landfill** = 5%.

**Q2.2 Assign each stream to a destination in the reverse network.**
Following the Lecture 8 condition → destination table: Good → **resale** (reuse; route to the secondary market directly from the regional consolidation centre, no factory trip); Repairable → **repair** (regional repair hub close to customers, short turnaround); Recoverable → **remanufacture** (central remanufacturing plant, like Tata Motors Prolife or Renault Refactory, where skills and tooling are concentrated); Material recovery → **recycling** (specialised recycler such as Attero/Lohum for electronics and batteries, or Mahindra CERO for vehicles); No recovery value → **responsible disposal** (authorised TSDF/landfill). The principle: *preserve the highest possible value for the longest possible time*, and process close to the customer for streams that go back to the market, centrally for streams that need scale.

**Q2.3 With the following assumed economics, compute the net value and CO₂ avoided. 📗**

| Stream | Units | Processing cost (₹/unit) | Recovered value (₹/unit) | CO₂ avoided (kg/unit) |
|---|---|---|---|---|
| Reuse | 2,000 | 200 | 2,000 | 40 |
| Repair | 2,500 | 800 | 1,800 | 30 |
| Remanufacture | 2,000 | 1,500 | 3,000 | 25 |
| Recycling | 3,000 | 300 | 500 | 8 |
| Disposal | 500 | 150 | 0 | −2 |

| Stream | Net value = units × (value − cost) | CO₂ avoided = units × kg |
|---|---|---|
| Reuse | 2,000 × 1,800 = ₹36,00,000 | 80,000 kg |
| Repair | 2,500 × 1,000 = ₹25,00,000 | 75,000 kg |
| Remanufacture | 2,000 × 1,500 = ₹30,00,000 | 50,000 kg |
| Recycling | 3,000 × 200 = ₹6,00,000 | 24,000 kg |
| Disposal | 500 × (−150) = −₹75,000 | −1,000 kg |
| **Total** | **₹96,25,000** | **2,28,000 kg = 228 t** |

Per returned unit: ₹962.5 net value and 22.8 kg CO₂ avoided. The 3,000 recycled units (30% of volume) earn only 6.2% of the value: moving even 500 units from recycling to remanufacture would add 500 × (1,500 − 200) = **₹6.5 lakh** and 500 × (25 − 8) = **8.5 t CO₂**. That is the Lecture 8 key principle: *"Recycling is usually lower in the value-retention hierarchy than reuse, repair and remanufacturing."*

---

## Problem 3. FMCG distribution network — current situation and KPIs (Lecture 10, slide 12) 📘 ⭐⭐⭐
*Scenario: an FMCG company wants to reduce the environmental impact of its distribution network.* Current situation: **10,000 deliveries per month; average distance = 180 km; diesel trucks; 62% average vehicle utilisation; 18% empty return kilometres.* The slide's five KPIs: **CO₂e per tonne-km, fuel efficiency (km per litre), vehicle utilisation %, empty km %, OTIF %.**

**Assumptions to complete the numerical (📗, state them):** 9-tonne trucks; diesel trucks average **4 km per litre**; diesel 2.68 kg CO₂ per litre; diesel ₹92 per litre; "180 km" is the loaded distance per delivery; "18% empty km" is the share of *total* km run empty.

**Q3.1 Compute monthly total km, diesel, CO₂ and fuel cost.**
- Loaded km = 10,000 × 180 = **18,00,000 km**. Since loaded km = 82% of total, total km = 18,00,000 ÷ 0.82 = **21,95,122 km**; empty km = **3,95,122 km**.
- Diesel = 21,95,122 ÷ 4 = **5,48,780 litres**.
- CO₂ = 5,48,780 × 2.68 = 14,70,732 kg = **1,470.7 t CO₂ per month** (≈ 17,650 t a year). This is Scope 1 if the fleet is owned, Scope 3 (Cat. 9) if hired.
- Fuel cost = 5,48,780 × ₹92 = **₹5.05 crore per month**.

**Q3.2 Compute the emission intensity in g CO₂e per tonne-km.**
Payload per delivery = 62% × 9 t = 5.58 t. Tonne-km = 10,000 × 5.58 × 180 = **1,00,44,000 t-km**. Intensity = 14,70,732 kg ÷ 1,00,44,000 t-km = 0.1464 kg = **146 g CO₂e per t-km**.

**Q3.3 The company raises utilisation to 80% (load consolidation, better routing) and cuts empty km to 10% (backhauls, freight exchange). Recompute.**
- Same tonnage moved = 10,000 × 5.58 = 55,800 t. At 80% utilisation each truck carries 7.2 t → deliveries = 55,800 ÷ 7.2 = **7,750 trips**.
- Loaded km = 7,750 × 180 = 13,95,000; total km = 13,95,000 ÷ 0.90 = **15,50,000 km**.
- Diesel = 15,50,000 ÷ 4 = **3,87,500 l**; CO₂ = **1,038.5 t**; cost = **₹3.57 crore**.
- Savings: **432 t CO₂ a month (−29.4%)** and **₹1.48 crore a month** (≈ ₹17.8 crore a year). New intensity = 10,38,500 ÷ 1,00,44,000 = **103 g CO₂e per t-km**.
- Lesson from Lecture 11: *"The cleanest kilometre is often the kilometre eliminated"* — and *green transport ≠ sustainable logistics* unless packaging, delivery frequency, empty miles and returns are also fixed.

**Q3.4 Write the five KPIs with formulas, current values and targets.**

| KPI | Formula | Current | Target |
|---|---|---|---|
| CO₂e per tonne-km | kg CO₂e ÷ tonne-km | 146 g | ≤ 105 g |
| Fuel efficiency | km ÷ litres | 4.0 km/l | 4.4 km/l (eco-driving, tyre pressure, speed governors) |
| Vehicle utilisation | load ÷ capacity | 62% | ≥ 80% |
| Empty km % | empty km ÷ total km | 18% | ≤ 10% |
| OTIF % | orders on time and in full ÷ total orders | (measure) | ≥ 95%, so that consolidation does not hurt service |

**Q3.5 What would a switch of 30% of the km to electric trucks charged on the grid do? (Assume 1.2 kWh per km, grid 0.70 kg/kWh.)**
After Q3.3, 30% of 15,50,000 km = 4,65,000 km. Diesel avoided = 4,65,000 ÷ 4 = 1,16,250 l → 311.6 t. EV emissions = 4,65,000 × 1.2 × 0.70 = 3,90,600 kg = 390.6 t. **The EVs emit more (390.6 t vs 311.6 t) on the coal-heavy grid.** EV trucks need renewable charging (solar at depots, green open-access power) to deliver a carbon benefit; with renewable power the saving is the full 311.6 t. This is the Lecture 9 point: *technology ≠ sustainability.*

---

## Problem 4. Road vs rail — modal shift (Lecture 8 green transportation network) 📘 concept + 📗 data ⭐⭐
A Pune plant ships **1,000 t a month** to a Kolkata DC. Road route: 1,900 km. Rail route: 2,000 km plus 50 km of road drayage at each end. Factors: road 0.09, rail 0.025 kg CO₂e/t-km. Costs: road ₹3.2 per t-km; rail ₹1.6 per t-km + ₹400 per t for each terminal handling (two handlings).

**Q4.1 Compare annual CO₂.**
Annual tonnage = 12,000 t. Road: 12,000 × 1,900 × 0.09 = 20,52,000 kg = **2,052 t**. Rail + drayage: 12,000 × (2,000 × 0.025 + 100 × 0.09) = 12,000 × (50 + 9) = 7,08,000 kg = **708 t**. Saving = **1,344 t (−65.5%)**.

**Q4.2 Compare annual cost.**
Road: 12,000 × 1,900 × ₹3.2 = **₹7.30 crore**. Rail: 12,000 × [2,000 × 1.6 + 100 × 3.2 + 2 × 400] = 12,000 × [3,200 + 320 + 800] = 12,000 × 4,320 = **₹5.18 crore**. Rail is cheaper **and** cleaner (₹2.11 crore saving).

**Q4.3 Why do many firms still use road?**
Transit time and reliability (rail 5–7 days door-to-door vs road 3–4 days), extra handling and damage risk, rake availability, minimum lot sizes, and first/last-mile gaps. Answer with the Lecture 8 principle: *"Use the lowest-impact transport mode compatible with service requirements."* Solution: a **sustainable multimodal network** (supplier → rail/inland waterway → regional DC → electric truck → customer), with safety stock at the DC to absorb the longer lead time.

---

## Problem 5. Distance criteria — load-distance and centre of gravity 📗 ⭐⭐⭐
A company serving four regional markets wants one central DC. Map grid units = 100 km.

| Market | x | y | Annual volume (t) |
|---|---|---|---|
| Delhi | 2 | 8 | 4,000 |
| Mumbai | 1 | 3 | 6,000 |
| Kolkata | 9 | 5 | 3,000 |
| Bengaluru | 3 | 0 | 5,000 |

Candidate sites: **Nagpur (4, 5), Pune (1.5, 2.5), Hyderabad (3.5, 2).**

**Q5.1 Find the centre of gravity.**
ΣW = 18,000. Cx = (2×4,000 + 1×6,000 + 9×3,000 + 3×5,000) ÷ 18,000 = (8,000 + 6,000 + 27,000 + 15,000) ÷ 18,000 = 56,000 ÷ 18,000 = **3.11**. Cy = (8×4,000 + 3×6,000 + 5×3,000 + 0×5,000) ÷ 18,000 = (32,000 + 18,000 + 15,000 + 0) ÷ 18,000 = 65,000 ÷ 18,000 = **3.61**. The CoG is at **(3.11, 3.61)**.

**Q5.2 Compute the load-distance score (Euclidean) for each candidate site.**

| Market (t) | Distance to Nagpur | Distance to Pune | Distance to Hyderabad |
|---|---|---|---|
| Delhi (4,000) | √(4+9) = 3.606 → 14,422 | √(0.25+30.25) = 5.523 → 22,092 | √(2.25+36) = 6.185 → 24,739 |
| Mumbai (6,000) | √(9+4) = 3.606 → 21,633 | √(0.25+0.25) = 0.707 → 4,243 | √(6.25+1) = 2.693 → 16,155 |
| Kolkata (3,000) | √(25+0) = 5.000 → 15,000 | √(56.25+6.25) = 7.906 → 23,717 | √(30.25+9) = 6.265 → 18,796 |
| Bengaluru (5,000) | √(1+25) = 5.099 → 25,495 | √(2.25+6.25) = 2.915 → 14,577 | √(0.25+4) = 2.062 → 10,308 |
| **Total (t × grid units)** | **76,550** | **64,629** | **69,998** |

Lowest load-distance: **Pune (64,629)**, then Hyderabad (69,998), then Nagpur (76,550). In km, Pune ≈ 64,629 × 100 = 64.6 lakh t-km a year.

**Q5.3 Why does Pune beat a site near the centre of gravity?**
The CoG minimises the sum of *squared*-type weighted distances, so it is a good *first approximation*, not the exact minimum of Σ(load × distance). Pune sits next to Mumbai, the heaviest market (6,000 t, one-third of volume). The CoG load-distance is 67,511 (Euclidean), worse than Pune. Always check candidate sites with the load-distance score.

**Q5.4 Add the sustainability lens: convert the difference between Pune and Nagpur into CO₂ by road (0.09 kg/t-km).**
Difference = (76,550 − 64,629) × 100 km = 11,92,100 t-km → × 0.09 = **107 t CO₂ a year** saved by Pune. But a full SSCM answer also checks rail connectivity, grid carbon intensity and renewable availability, flood/heat risk, water stress, land cost and labour — which is why we add a **factor-rating** step next. Lecture 11's new location questions: *What is the location's climate risk? Future water availability? Carbon intensity of electricity? Exposure to extreme weather? Dependence on a single port?*

---

## Problem 6. Factor rating for a sustainable DC location 📗 ⭐⭐
| Factor | Weight | Site X | Site Y | Site Z |
|---|---|---|---|---|
| Land & operating cost | 25 | 8 | 6 | 9 |
| Proximity to customers (load-distance) | 25 | 6 | 9 | 7 |
| Rail / multimodal access | 15 | 9 | 5 | 4 |
| Renewable power availability / grid carbon | 15 | 7 | 8 | 5 |
| Climate & flood risk (10 = lowest risk) | 10 | 6 | 8 | 4 |
| Labour & community acceptance | 10 | 7 | 8 | 9 |

**Q6.1 Rank the sites.**
X = (25×8 + 25×6 + 15×9 + 15×7 + 10×6 + 10×7) ÷ 100 = (200 + 150 + 135 + 105 + 60 + 70) ÷ 100 = **7.20**. Y = (150 + 225 + 75 + 120 + 80 + 80) ÷ 100 = **7.30**. Z = (225 + 175 + 60 + 75 + 40 + 90) ÷ 100 = **6.65**. Ranking: **Y > X > Z**, with Y only 0.10 ahead of X.

**Q6.2 Interpret.**
Z is cheapest but has poor rail access and high flood risk (a "cheapest location" that the Lecture 11 climate-risk questions would reject). Y wins narrowly through customer proximity and low climate risk; X is the best multimodal site. With a margin of 0.10, check sensitivity: if the firm commits to rail-based distribution (rail weight 25, cost 15), X = 7.30 and Y = 6.90, so X wins. State the recommendation conditional on the transport strategy.

---

## Problem 7. How many DCs? Cost vs carbon trade-off 📗 ⭐⭐⭐
| No. of DCs | Facility cost | Inventory cost | Inbound transport | Outbound transport | CO₂ (t/yr) |
|---|---|---|---|---|---|
| 1 | 4.0 | 6.0 | 2.0 | 20.0 | 5,800 |
| 2 | 7.0 | 7.5 | 2.6 | 13.0 | 4,500 |
| 3 | 10.0 | 8.7 | 3.2 | 9.5 | 4,075 |
| 4 | 13.0 | 9.8 | 3.8 | 7.8 | 4,100 |
| 5 | 16.0 | 10.8 | 4.4 | 7.0 | 4,350 |

(Costs in ₹ crore per year. CO₂ includes transport and facility energy.)

**Q7.1 Find the cost-minimising number of DCs.**
Totals: 1 DC = **32.0**; 2 DCs = **30.1**; 3 DCs = **31.4**; 4 DCs = **34.4**; 5 DCs = **38.2**. Minimum cost at **2 DCs (₹30.1 crore)**. More DCs cut outbound (last-mile) cost but raise facility, inventory (more safety stock, the square-root law) and inbound cost.

**Q7.2 Find the CO₂-minimising number.**
Lowest CO₂ at **3 DCs (4,075 t)**. Beyond 3, the energy of extra buildings and the extra inbound trips outweigh the shorter last mile.

**Q7.3 At what carbon price does 3 DCs become better than 2?**
Z = cost + p × CO₂. 30.1 crore + 4,500p = 31.4 crore + 4,075p → 425p = ₹1.3 crore → p = 1,30,00,000 ÷ 425 = **₹30,588 per t CO₂**. Below ~₹30,600/t (far above today's market prices), 2 DCs stays optimal. Recommendation: **2 DCs now**, with solar roofs and EV last-mile to cut the 4,500 t, and design so that a third DC can be added if carbon prices or service needs rise.

---

## Problem 8. Packaging cube and milk-run consolidation (Lecture 8 green packaging & route optimisation) 📘 concept + 📗 data ⭐⭐
Lecture 8: *"Packaging is not simply a procurement decision. It affects cube → vehicle utilisation → number of trips → fuel → CO₂."*

**Q8.1 Right-sizing the carton raises units per truck from 800 to 1,000. Monthly volume 1,00,000 units; each trip 500 km at 4 km/l. Savings?**
Trips: 1,00,000 ÷ 800 = 125 → 1,00,000 ÷ 1,000 = 100 → **25 trips saved (−20%)**. Diesel per trip = 500 ÷ 4 = 125 l → 25 × 125 = 3,125 l saved → **8.4 t CO₂ a month** (3,125 × 2.68) and ₹2.9 lakh of diesel at ₹92/l.

**Q8.2 A depot serves three customers with separate round trips: D–A 40 km, D–B 50 km, D–C 60 km. A milk run D→A→B→C→D uses A–B 15 km and B–C 20 km. One truck can carry all three loads. Compare km and CO₂ (truck: 6 km/l).**
Separate: 2 × (40 + 50 + 60) = **300 km** → 50 l → 134 kg CO₂. Milk run: 40 + 15 + 20 + 60 = **135 km** → 22.5 l → 60.3 kg CO₂. Saving **165 km (55%)** and 73.7 kg CO₂ per cycle. This is the Lecture 8 network decision *"which customers should be consolidated? — consolidate customers A, B and C for one delivery."*

---

## Problem 9. Air vs sea for an export order 📗 ⭐
A 20 t shipment from Chennai to Rotterdam. Sea: 16,000 km, 0.015 kg/t-km, ₹3 lakh, 30 days. Air: 8,500 km, 0.60 kg/t-km, ₹40 lakh, 3 days.

**Q9.1 Emissions and the cost of speed.**
Sea: 20 × 16,000 × 0.015 = **4.8 t CO₂**. Air: 20 × 8,500 × 0.60 = **102 t CO₂** (21 times more). Air costs ₹37 lakh more and emits 97.2 t more. Use air only for urgent, high-value, low-weight items (spares, pharma). Better: plan earlier (forecasting), keep sea as default, and use sea-air for partial urgency. Lecture 10 trap: *"Fast delivery but excessive inventory/air freight"* is green-looking efficiency that is not sustainable.

---

## Problem 10. Consumer-electronics network design exercise (Lecture 8, slide 42) 📘 + 📗 data ⭐⭐⭐
*A consumer-electronics company has 3 suppliers, 2 manufacturing plants, 4 regional DCs, 10,000 customers and 20% expected product returns. It is considering one centralised recycling centre, two regional collection centres and one remanufacturing facility.* Design choices:

| Decision | Option A | Option B |
|---|---|---|
| Collection | Centralised | Regional |
| Transport | Road | Rail + road |
| Recovery | Recycle | Remanufacture |
| Warehouse | Conventional | Solar |
| Packaging | Single-use | Returnable |

*Then evaluate cost, CO₂, recovery and service. Question: should the company select the cheapest network?* The slide's three network options: Network A — low cost but high emissions; Network B — higher initial investment but lower operating emissions; Network C — higher reverse-logistics complexity but higher material recovery.

**Q10.1 How many returns must the reverse network handle?**
20% × 10,000 customers = **2,000 returned units a year** (if each customer buys one unit a year).

**Q10.2 Evaluate Option A vs Option B with the assumed annual data below. 📗**

| Element (₹ lakh / year) | Option A | Option B |
|---|---|---|
| Collection | 30 | 42 (two regional centres) |
| Transport | 60 | 52 (rail for long-haul) |
| Recovery processing | 10 (recycle at ₹500/unit) | 50 (remanufacture at ₹2,500/unit) |
| Warehouse energy | 20 | 22 (14 energy + 8 annualised solar capex) |
| Packaging | 15 | 13 (9 + 4 returnable-pool amortisation) |
| **Gross logistics cost** | **135** | **179** |
| Recovery revenue | 16 (scrap at ₹800/unit) | 120 (resale at ₹6,000/unit) |
| **Net cost** | **119** | **59** |

| Element (t CO₂e / year) | Option A | Option B |
|---|---|---|
| Transport | 400 | 260 |
| Warehouse | 150 | 40 |
| Packaging | 60 | 25 |
| Credit for recovery | −16 (8 kg/unit) | −120 (60 kg/unit) |
| **Net CO₂** | **594** | **205** |

Recovery: A recovers materials only (lowest value-retention); B returns products to use (remanufacture, high value-retention). Service: return turnaround ~14 days (A, centralised) vs ~6 days (B, regional).

**Q10.3 Should the company select the cheapest network?**
On **gross logistics cost**, A is cheapest (₹135 lakh vs ₹179 lakh). But on **net cost after recovery value** B is cheaper (₹59 lakh vs ₹119 lakh), and B cuts CO₂ by **65%** (594 → 205 t), retains more value and gives faster service. So **no**: choose B, or a hybrid (regional collection with rail-based consolidation to a central remanufacturing plant, recycling only what cannot be remanufactured). The answer depends on remanufacturable share and resale price, so test the sensitivity: if only 40% of returns are remanufacturable, B's revenue falls and the gap narrows. Key message: **design the forward and reverse network together.**

---

## Problem 11. ITC eChoupal — the network economics (HBS case in the course zip) 📘 ⭐⭐
Facts from the case: a typical farmer's lot = **20 quintals (2 t)**; at the mandi he loses about **10 kg (0.5%)** in manual weighing ≈ **₹100 per lot**; farmers travelled **30–50 km** to the mandi; the eChoupal design puts a **kiosk within walking distance (< 5 km)** and a **hub within driving distance (< 30 km)** of every farmer (average 20 km, range 5–30 km); ITC saved about **$5 per tonne** on freight and the farmer gained about **$8 per tonne** on average; ITC reimbursed transport cost; the Sanchalak earned **0.5%** commission on purchases (2–3% on inputs); setup cost **₹1,70,000** per eChoupal plus **₹1,00,000** for people, travel and training; ITC had **1,695 eChoupals covering 8,400 villages** in MP, and **5 processing units + 39 warehouses = 44 points** versus 51 large soybean mandis. Exchange rate in the case: $1 = ₹45.23.

**Q11.1 What does a farmer gain per lot of 2 t by selling through the eChoupal hub?**
Price/efficiency gain: 2 t × $8 = $16 = **₹724**; weighing loss avoided ≈ **₹100**; plus freight reimbursed and cash paid immediately (no credit period, no 2–3 day queue). Total ≈ **₹824 per lot**, against an average farmer's annual net income of ~₹20,000 from soybean and wheat (≈ 4%).

**Q11.2 How many villages does one eChoupal serve? What does that say about network density?**
8,400 ÷ 1,695 ≈ **5 villages per eChoupal**. Information nodes are dense and cheap (one PC kiosk), while physical nodes (44 hubs) are few and large. This splits the **information flow** (price discovery at village level) from the **physical flow** (bulk movement to hubs), the same physical + information + financial integration Lecture 8 asks for.

**Q11.3 Using the distance criteria, why did ITC add hubs after launch?**
To keep every farmer within **30 km** of a hub, ITC added 3 processing hubs and 36 warehouses in MP. If the average one-way distance falls from ~40 km (mandi) to ~20 km (hub), a tractor trip saves ~40 km round-trip. At an assumed 0.25 l diesel per km, that is 10 l (≈ 27 kg CO₂) and roughly ₹900 per trip. Shorter distance, fewer intermediaries (the "village → mandi → factory" cycle broken) and less handling also reduce crop wastage, which is why Lecture 1 classifies it as a delivery-based SSCM initiative.

**Q11.4 Break-even on one eChoupal kiosk?**
Investment ≈ ₹1,70,000 + ₹1,00,000 = ₹2,70,000. If a kiosk channels 1,000 t a year, ITC's freight saving alone = 1,000 × $5 × 45.23 = **₹2,26,150 a year**, so payback ≈ **1.2 years** (the case says ITC expected to recover cost within three years). The Samyojak (former commission agent) keeps a role in logistics, an example of inclusive network redesign.

---

## Practice set 📗

**Q12. A DC handles 2,40,000 units a month using 1,80,000 kWh. After LEDs and smart HVAC (IKEA, Prologis examples) use falls to 1,35,000 kWh. Compute the KPI "energy per unit handled" before and after and the CO₂ saving.**
Before: 0.75 kWh/unit; after: 0.5625 kWh/unit (−25%). Saving 45,000 kWh × 0.70 = **31.5 t CO₂ a month**.

**Q13. A reverse network collects 600 returned units a month from rural customers, 6 units per village visit, at ₹900 per visit. A drop-off point at the local kirana store (decentralised configuration) lets the truck collect 60 units per visit at ₹1,500. Compare cost per unit.**
Village visits: 100 visits × ₹900 = ₹90,000 → **₹150/unit**. Drop-off: 10 visits × ₹1,500 = ₹15,000 → **₹25/unit**. Low return density is a top reverse-logistics challenge (Lecture 8); aggregation points fix it.

**Q14. A firm moves 5,000 t over 800 km by road (0.09 kg/t-km). Utilisation improves from 60% to 75% by consolidation. If emissions scale with vehicle-km, what is the new CO₂?**
Base: 5,000 × 800 × 0.09 = **360 t**. Vehicle-km fall by 60/75 = 0.8, so CO₂ ≈ 360 × 0.8 = **288 t** (−20%). (Fuel per km rises slightly with load, so the true saving is a little smaller.)

**Q15. Strategic, tactical or operational? (a) Location of a new recycling facility; (b) which DC serves the eastern customers; (c) collection frequency for returns; (d) capacity of a remanufacturing plant; (e) which transport mode for returns; (f) shipment consolidation.**
Strategic: (a), (d). Tactical: (b), (e). Operational: (c), (f). Lecture 8: *"Strategic sets the network. Tactical connects the network. Operational makes it perform."*
