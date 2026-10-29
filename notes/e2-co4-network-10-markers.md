# CO4 · 10-Mark Numericals: SSCM Network Design, Logistics Cost & Distance
Your teacher's pattern: **CO4 = 10 marks, a numerical on SSCM network design**. Expect cost **and** carbon in the same question, a choice between networks, sites, modes or numbers of DCs, and an interpretation. This page has six full 10-mark questions with marks splits and model answers. Q1, Q3 and Q6 are the course's own examples (Lectures 8 and 10) 📘; Q2, Q4 and Q5 are practice questions in the same style 📗. Turn on **Self-test** (`T`) to hide the answers.

Full theory and more problems: [Network & Logistics Numericals](p3-network-logistics-numericals.md) · [Designing the Sustainable Network](ch07-network-design.md) · [Sustainable Logistics](ch06-sustainable-logistics.md).

---

## How a 10-mark network answer earns its marks ⭐⭐⭐
| Step | What to write | Marks it usually carries |
|---|---|---|
| 1. Objective | **Minimise Z = C_total + λ·E_CO₂ + μ·W_waste** (Lecture 8); C_total = facility + production + transport + inventory + collection + recovery + disposal | 1 |
| 2. Data table | Each option's cost, CO₂ (t × km × factor, or litres × 2.68) and service or recovery | 1–2 |
| 3. Calculate | Totals for every option; load-distance or centre of gravity; switching carbon price | 4 |
| 4. Choose | The winner on cost, on carbon, and on the combined Z; any Pareto trade-off | 1–2 |
| 5. Interpret + recommend | Service (OTIF, lead time), resilience, circularity, one line of theory: *"The best sustainable network is not necessarily the cheapest network."* | 2 |

**Formulas:** transport CO₂ = tonnes × km × factor (road ≈ 0.09, rail ≈ 0.025, water ≈ 0.015, air ≈ 0.60 kg/t-km 📗) · **centre of gravity** Cx = Σxᵢwᵢ ÷ Σwᵢ, Cy = Σyᵢwᵢ ÷ Σwᵢ · **load-distance** = Σ load × distance (Euclidean √(Δx² + Δy²) or rectilinear |Δx| + |Δy|) · **switching price**: set Z_A = Z_B and solve for λ · in-transit inventory cost = annual tonnes × value per t × carrying rate × transit days ÷ 365.

---

## Q1 (10 marks). Which sustainable network: A, B or C? (Lecture 8) 📘 ⭐⭐⭐
| Network | Cost (₹) | CO₂ | Recovery |
|---|---|---|---|
| A | 100 | 100 | 20% |
| B | 108 | 75 | 50% |
| C | 115 | 55 | 70% |

(a) Is any network dominated? (1) (b) Compute the cost of each unit of CO₂ avoided moving A → B and B → C. (2) (c) Using Z = Cost + λ·CO₂, find the ranges of λ for which each network is best. (3) (d) With λ = 0.30 and a benefit of μ = ₹0.10 per percentage point of recovery (Z = Cost + λ·CO₂ − μ·Recovery), which network wins? (2) (e) Recommend. (2)

**Q1.1 (a) Dominance. [1 mark]**
None is dominated: A is cheapest, C has the lowest CO₂ and highest recovery, B is in the middle on all three. **All three are Pareto-efficient**, so the choice depends on the decision-maker's priorities.

**Q1.2 (b) Cost per unit of CO₂ avoided. [2 marks]**
A → B: ₹8 ÷ 25 = **₹0.32 per unit CO₂** (+30 points recovery). B → C: ₹7 ÷ 20 = **₹0.35 per unit CO₂** (+20 points recovery).

**Q1.3 (c) Ranges of λ. [3 marks]**
Z_A = 100 + 100λ; Z_B = 108 + 75λ; Z_C = 115 + 55λ.
A = B → 25λ = 8 → **λ = 0.32**. B = C → 20λ = 7 → **λ = 0.35**.
**λ < 0.32 → A; 0.32 < λ < 0.35 → B; λ > 0.35 → C.** Check λ = 0.5: A 150, B 145.5, C 142.5 → C ✓.

**Q1.4 (d) Adding the value of recovery. [2 marks]**
Z_A = 100 + 30 − 2 = **128**; Z_B = 108 + 22.5 − 5 = **125.5**; Z_C = 115 + 16.5 − 7 = **124.5** → **C wins**, even though at λ = 0.30 alone A would win (130 vs 130.5 vs 131.5). Valuing circularity moves the decision towards the closed-loop network.

**Q1.5 (e) Recommendation. [2 marks]**
*"There is no single best network without defining decision-maker priorities"* (Lecture 8). A cost-only firm picks A; any firm that prices carbon above about ₹0.35 per unit, or values recovered material, picks **C**. **B is a sensible transition network**: only 8% dearer than A, 25% less CO₂, 50% recovery. Recommend B now with a roadmap to C as carbon prices (CCTS, CBAM) and EPR recovery targets tighten.

---

## Q2 (10 marks). Locating a central DC: centre of gravity and load-distance 📗 ⭐⭐⭐
A consumer-durables firm serves five markets (grid unit = 100 km) and will open one DC.

| Market | x | y | Annual volume (t) |
|---|---|---|---|
| Jaipur | 2 | 9 | 3,000 |
| Ahmedabad | 1 | 6 | 5,000 |
| Indore | 4 | 6 | 2,000 |
| Nagpur | 7 | 5 | 4,000 |
| Hyderabad | 6 | 1 | 6,000 |

Candidate sites: **Bhopal (4, 7), Aurangabad (4, 4), Nagpur (7, 5)**. Road freight costs ₹2.5 per t-km and emits 0.09 kg CO₂ per t-km.
(a) Find the centre of gravity. (2) (b) Compute the Euclidean load-distance score for each candidate and choose a site. (4) (c) Convert the scores into annual transport cost and CO₂. (2) (d) What else should a sustainable location decision consider? (2)

**Q2.1 (a) Centre of gravity. [2 marks]**
Σw = 20,000 t. Cx = (2×3,000 + 1×5,000 + 4×2,000 + 7×4,000 + 6×6,000) ÷ 20,000 = 83,000 ÷ 20,000 = **4.15**. Cy = (9×3,000 + 6×5,000 + 6×2,000 + 5×4,000 + 1×6,000) ÷ 20,000 = 95,000 ÷ 20,000 = **4.75**. CoG = **(4.15, 4.75)**, about 415 km east and 475 km north of the grid origin.

**Q2.2 (b) Load-distance scores. [4 marks]**
| Market (t) | Bhopal (4, 7) | Aurangabad (4, 4) | Nagpur (7, 5) |
|---|---|---|---|
| Jaipur (3,000) | √(4 + 4) = 2.828 → 8,485 | √(4 + 25) = 5.385 → 16,155 | √(25 + 16) = 6.403 → 19,209 |
| Ahmedabad (5,000) | √(9 + 1) = 3.162 → 15,811 | √(9 + 4) = 3.606 → 18,028 | √(36 + 1) = 6.083 → 30,414 |
| Indore (2,000) | √(0 + 1) = 1.000 → 2,000 | √(0 + 4) = 2.000 → 4,000 | √(9 + 1) = 3.162 → 6,325 |
| Nagpur (4,000) | √(9 + 4) = 3.606 → 14,422 | √(9 + 1) = 3.162 → 12,649 | 0 → 0 |
| Hyderabad (6,000) | √(4 + 36) = 6.325 → 37,947 | √(4 + 9) = 3.606 → 21,633 | √(1 + 16) = 4.123 → 24,739 |
| **Total (t × grid units)** | **78,666** | **72,466** | **80,686** |

**Aurangabad has the lowest load-distance (72,466)**, then Bhopal (78,666), then Nagpur (80,686). Aurangabad is also the candidate nearest the CoG (the CoG itself scores 70,284, a lower bound worth quoting).

**Q2.3 (c) Transport cost and CO₂. [2 marks]**
t-km = score × 100 km. Aurangabad: 72.47 lakh t-km × ₹2.5 = **₹1.81 crore**, × 0.09 kg = **652 t CO₂**. Bhopal: 78.67 lakh t-km → **₹1.97 crore, 708 t**. Nagpur: 80.69 lakh t-km → **₹2.02 crore, 726 t**. Aurangabad saves ₹15–21 lakh and 56–74 t CO₂ a year against the alternatives.

**Q2.4 (d) Beyond distance. [2 marks]**
Distance minimises transport effort, but Lecture 8 and 11 add: **rail and multimodal access** (can the long Hyderabad and Jaipur legs move by rail?), **grid carbon intensity and rooftop-solar potential**, **water stress and flood or heat risk**, land and labour cost, and dependence on a single highway or port. Use a **factor-rating** table (Σ weight × score) on these with the load-distance result as one factor, then decide.

---

## Q3 (10 marks). FMCG distribution network: logistics cost, CO₂ and KPIs (Lecture 10) 📘 ⭐⭐⭐
An FMCG company makes **10,000 deliveries a month**, average loaded distance **180 km**, diesel trucks, **62% average vehicle utilisation** and **18% empty return km**. Assume 9-t trucks, 4 km per litre, diesel 2.68 kg CO₂/l and ₹92/l (state these).
(a) Compute monthly total km, diesel, CO₂ and fuel cost. (3) (b) Compute g CO₂ per tonne-km. (1) (c) Utilisation rises to 80% and empty km falls to 10%. Recompute and state the savings. (4) (d) Give the five KPIs with targets. (2)

**Q3.1 (a) Current state. [3 marks]**
Loaded km = 10,000 × 180 = 18,00,000. Loaded = 82% of total → total = 18,00,000 ÷ 0.82 = **21,95,122 km** (empty 3,95,122). Diesel = 21,95,122 ÷ 4 = **5,48,780 l**. CO₂ = 5,48,780 × 2.68 = **1,470.7 t a month** (≈ 17,650 t a year). Fuel cost = 5,48,780 × ₹92 = **₹5.05 crore a month**.

**Q3.2 (b) Intensity. [1 mark]**
Payload = 62% × 9 = 5.58 t. t-km = 10,000 × 5.58 × 180 = 1,00,44,000. Intensity = 14,70,732 kg ÷ 1,00,44,000 = **146 g CO₂ per t-km**.

**Q3.3 (c) After consolidation and backhauls. [4 marks]**
Tonnage = 10,000 × 5.58 = 55,800 t. At 80%, each truck carries 7.2 t → trips = 55,800 ÷ 7.2 = **7,750**. Loaded km = 7,750 × 180 = 13,95,000; total = 13,95,000 ÷ 0.90 = **15,50,000 km**. Diesel = **3,87,500 l** → CO₂ = **1,038.5 t**; cost = **₹3.57 crore**.
**Savings: 432 t CO₂ a month (−29.4%) and ₹1.48 crore a month (≈ ₹17.8 crore a year).** New intensity = 10,38,500 ÷ 1,00,44,000 = **103 g per t-km**.

**Q3.4 (d) Five KPIs (Lecture 10 slide). [2 marks]**
| KPI | Current | Target |
|---|---|---|
| CO₂e per tonne-km | 146 g | ≤ 105 g |
| Fuel efficiency (km/l) | 4.0 | 4.4 |
| Vehicle utilisation % | 62% | ≥ 80% |
| Empty km % | 18% | ≤ 10% |
| OTIF % | measure | ≥ 95%, so consolidation does not hurt service |
*"The cleanest kilometre is often the kilometre eliminated."* Fixing utilisation and empty running beats buying new trucks.

---

## Q4 (10 marks). Road vs rail: total logistics cost with inventory and carbon 📗 ⭐⭐⭐
A steel-products firm ships **20,000 t a year** from Pune to Kolkata (1,800 km). Goods are worth ₹50,000 per t; inventory carrying cost is 18% a year; the internal carbon price is ₹2,000 per t CO₂.
- **Road:** ₹3.0 per t-km, 4 days door to door, 0.09 kg CO₂/t-km.
- **Rail (multimodal):** 1,700 km rail at ₹1.8 per t-km and 0.025 kg/t-km, plus 100 km of road first and last mile at ₹3.5 per t-km and 0.09 kg/t-km, plus handling ₹150 per t; 7 days door to door.
(a) Compute freight cost for each option. (3) (b) Compute in-transit inventory cost. (2) (c) Compute CO₂ and carbon cost, then the total cost of each option. (3) (d) Recommend, including service. (2)

**Q4.1 (a) Freight cost. [3 marks]**
Road = 20,000 × 1,800 × 3.0 = **₹10.80 crore**. Rail = 20,000 × 1,700 × 1.8 (₹6.12 cr) + 20,000 × 100 × 3.5 (₹0.70 cr) + 20,000 × 150 (₹0.30 cr) = **₹7.12 crore**.

**Q4.2 (b) In-transit inventory. [2 marks]**
Road = 20,000 × 50,000 × 0.18 × 4 ÷ 365 = **₹19.7 lakh**. Rail = × 7 ÷ 365 = **₹34.5 lakh**. Rail's 3 extra days cost ₹14.8 lakh a year; extra safety stock for 3 days (≈ 164 t × ₹50,000 × 18%) adds about ₹14.8 lakh more.

**Q4.3 (c) CO₂ and total cost. [3 marks]**
Road CO₂ = 20,000 × 1,800 × 0.09 ÷ 1,000 = **3,240 t** → carbon cost ₹64.8 lakh.
Rail CO₂ = 20,000 × 1,700 × 0.025 ÷ 1,000 (850 t) + 20,000 × 100 × 0.09 ÷ 1,000 (180 t) = **1,030 t** → ₹20.6 lakh.

| Option | Freight | Inventory | Carbon | **Total** |
|---|---|---|---|---|
| Road | 10.80 | 0.20 | 0.65 | **₹11.65 crore** |
| Rail | 7.12 | 0.35 | 0.21 | **₹7.67 crore** |

Rail saves **≈ ₹3.97 crore a year (34%)** and **2,210 t CO₂ (−68%)**, still ≈ ₹3.8 crore after the extra safety stock.

**Q4.4 (d) Recommendation. [2 marks]**
Move the **base, predictable volume by rail**, with safety stock at the Kolkata DC to absorb the longer and less reliable lead time; keep **road for urgent or small orders** (say 10–20%). Check rake availability and minimum lot sizes, and handling damage. This is Lecture 8's principle: *"use the lowest-impact transport mode compatible with service requirements"*, a **sustainable multimodal network**.

---

## Q5 (10 marks). How many DCs? Cost vs carbon 📗 ⭐⭐⭐
| DCs | Facility | Inventory | Inbound | Outbound | CO₂ (t/yr) |
|---|---|---|---|---|---|
| 1 | 4.0 | 6.0 | 2.0 | 20.0 | 5,800 |
| 2 | 7.0 | 7.5 | 2.6 | 13.0 | 4,500 |
| 3 | 10.0 | 8.7 | 3.2 | 9.5 | 4,075 |
| 4 | 13.0 | 9.8 | 3.8 | 7.8 | 4,100 |
| 5 | 16.0 | 10.8 | 4.4 | 7.0 | 4,350 |
(costs in ₹ crore a year)

(a) Total cost and the cost-minimising number of DCs. (3) (b) The CO₂-minimising number. (1) (c) At what carbon price does 3 DCs beat 2? (3) (d) Explain the trade-off and recommend. (3)

**Q5.1 (a) Total cost. [3 marks]**
1 DC = **32.0**, 2 = **30.1**, 3 = **31.4**, 4 = **34.4**, 5 = **38.2** → minimum at **2 DCs (₹30.1 crore)**.

**Q5.2 (b) Lowest CO₂. [1 mark]**
**3 DCs (4,075 t)**.

**Q5.3 (c) Switching carbon price. [3 marks]**
30.1 crore + 4,500p = 31.4 crore + 4,075p → 425p = ₹1.3 crore → **p = ₹30,588 per t CO₂**. Below about ₹30,600 per tonne (far above current Indian or EU prices), 2 DCs stays optimal.

**Q5.4 (d) Trade-off and recommendation. [3 marks]**
More DCs shorten the last mile (outbound ↓) but add buildings, energy and inbound trips, and raise inventory (safety stock grows with the square root of the number of DCs). CO₂ falls up to 3 DCs and then rises as facility energy and inbound trips outweigh shorter delivery. **Recommend 2 DCs now**, with rooftop solar, EV last-mile in the metros and consolidated inbound to cut the 4,500 t, and design for a third DC if carbon prices, service targets or demand rise.

---

## Q6 (10 marks). Reverse network: allocating 10,000 returned units (Lecture 8) 📘 ⭐⭐⭐
Returns = Reuse 2,000 · Repair 2,500 · Remanufacture 2,000 · Recycling 3,000 · Disposal 500. Assumed economics (📗):

| Stream | Processing cost (₹/unit) | Recovered value (₹/unit) | CO₂ avoided (kg/unit) |
|---|---|---|---|
| Reuse | 200 | 2,000 | 40 |
| Repair | 800 | 1,800 | 30 |
| Remanufacture | 1,500 | 3,000 | 25 |
| Recycling | 300 | 500 | 8 |
| Disposal | 150 | 0 | −2 |

(a) Verify the material balance and compute the recovery rate. (2) (b) Compute net value and CO₂ avoided. (4) (c) Value of moving 500 units from recycling to remanufacture. (2) (d) Where should each stream be processed? (2)

**Q6.1 (a) Balance and recovery rate. [2 marks]**
2,000 + 2,500 + 2,000 + 3,000 + 500 = **10,000** ✓. Recovery rate = 9,500 ÷ 10,000 = **95%**; value-retaining recovery (reuse + repair + remanufacture) = **65%**.

**Q6.2 (b) Net value and CO₂ avoided. [4 marks]**
| Stream | Net value | CO₂ avoided |
|---|---|---|
| Reuse | 2,000 × 1,800 = ₹36.00 lakh | 80 t |
| Repair | 2,500 × 1,000 = ₹25.00 lakh | 75 t |
| Remanufacture | 2,000 × 1,500 = ₹30.00 lakh | 50 t |
| Recycling | 3,000 × 200 = ₹6.00 lakh | 24 t |
| Disposal | 500 × (−150) = −₹0.75 lakh | −1 t |
| **Total** | **₹96.25 lakh** | **228 t** |

**Q6.3 (c) Moving 500 units up the hierarchy. [2 marks]**
+500 × (1,500 − 200) = **₹6.5 lakh** and +500 × (25 − 8) = **8.5 t CO₂**. Recycling is 30% of volume but only 6% of value: *"Recycling is usually lower in the value-retention hierarchy than reuse, repair and remanufacturing."*

**Q6.4 (d) Where to process. [2 marks]**
Reuse → resale direct from a **regional collection/sorting centre** (no factory trip); repair → **regional repair hub** near customers; remanufacture → **central plant** where skills and tooling are concentrated (Renault Refactory, Tata Prolife); recycling → **specialist recycler** (Attero, Lohum); disposal → authorised TSDF. Process close to the customer for streams that return to the market and centrally for streams that need scale: a **hybrid collection network**.

---

## Quick checklist before you hand in a CO4 answer ⭐⭐⭐
- Did you write the **objective function** and define every term?
- Did you compute **both cost and CO₂** for every option?
- Did you show the **switching λ** or the trade-off ratio, not only one winner?
- Did you include **inventory** (in-transit, safety stock) when lead times differ?
- Did you comment on **service** (OTIF, lead time), **resilience** and **circularity**?
- Did you close with a Lecture 8 line: *"the best sustainable network is not necessarily the cheapest"*?
