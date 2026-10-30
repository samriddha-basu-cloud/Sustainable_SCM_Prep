# CO4 · 10-Mark Numericals: SSCM Distribution Networks, Logistics Cost, Distance Criteria
**What the exam asks (teacher's importants):** *different scenarios will be given with different costs; find the total cost for each scenario and compare which is the best scenario to select.* Every answer must have **six parts**:
1. **Identify the objective function**
2. **Define the decision variables**
3. **State the assumptions made**
4. **Calculate total cost** (it may not be given directly: build it from transportation, inventory, facility and other costs)
5. **Compare the total cost and select the best scenario**
6. **Write a short interpretation and recommendation** on how to improve cost using **new sustainable technologies** (IoT, blockchain, AI route optimisation, etc.) for traceability, operational efficiency and sustainability

Every question below is answered in exactly these six parts. Q1 and Q5 use the course's own examples (Lectures 8 and 10) 📘; Q2, Q3, Q4 and Q6 are practice questions in the same style 📗. Turn on **Self-test** (`T`) to hide the answers.

---

## The 10-mark answer template ⭐⭐⭐
| Part | What to write | Marks |
|---|---|---|
| 1. Objective function | **Minimise Z = Total cost = Σ (facility + transportation + inventory + handling/processing) + λ·CO₂** (Lecture 8: Z = C_total + λ·E_CO₂ + μ·W_waste). Say in words: minimise total annual cost (and carbon cost) subject to meeting demand | 1 |
| 2. Decision variables | **yⱼ** = 1 if scenario/facility j is selected (0 otherwise); **xᵢⱼ** = quantity moved from i to j; mode or number of DCs; **rᵢ** = quantity recovered | 1 |
| 3. Assumptions | Demand known and constant; costs linear and per unit/per t-km; capacity sufficient; same service level; emission factors; carrying rate; 365 days | 1 |
| 4. Total cost | A cost-build table per scenario: transport (t × km × ₹/t-km), inventory (in-transit + cycle/safety stock × value × carrying %), facility (fixed), handling, carbon (t CO₂ × price) | 4 |
| 5. Compare and select | A comparison table; pick the **lowest total cost**; mention CO₂ alongside | 1 |
| 6. Interpretation + technology | Why the winner wins (which cost drives it); **2–3 technologies with the cost line they cut** and the sustainability benefit | 2 |

**Cost formulas:** transport = tonnes × km × ₹ per t-km (or trips × ₹ per trip; litres × ₹ per litre) · in-transit inventory = annual t × value per t × carrying % × transit days ÷ 365 · cycle/safety stock cost = average units × value × carrying % · CO₂ = t × km × factor (road 0.09, rail 0.025, water 0.015 kg/t-km 📗) or litres × 2.68 · carbon cost = t CO₂ × internal carbon price · **load-distance** = Σ load × distance; centre of gravity Cx = Σxw ÷ Σw, Cy = Σyw ÷ Σw.

**Technology menu for Part 6 (what each one cuts):**
| Technology | Cost line it improves | Sustainability benefit |
|---|---|---|
| **AI route optimisation** | Transport: fewer km, fewer trips, higher utilisation (typically 5–15% 📗) | Less fuel and CO₂, fewer empty km |
| **IoT / telematics** | Fuel (eco-driving, idling), maintenance, cold-chain losses; warehouse energy | Real-time CO₂ and energy data, less spoilage |
| **Blockchain** | Fewer disputes, faster recalls, lower audit and documentation cost | **Traceability** of origin, ethical sourcing, verified carbon data |
| **AI demand forecasting** | Inventory: lower safety stock, less obsolescence | Less over-production and waste |
| **RFID / IoT tags** | Inventory accuracy, picking errors, returns sorting | Fewer lost goods, better reverse-logistics recovery |
| **Digital twin** | Avoids costly network mistakes; tests scenarios before building | Simulate CO₂ of each network option |
| **Control tower / visibility platform** | Expediting, premium freight, disruption cost | Resilience; fewer emergency air shipments |
Lecture 9 caution: technology adds its own energy, e-waste and cyber risk, so evaluate it on **Net Technology Value** and pilot first.

---

## Q1 (10 marks). Network A, B or C (Lecture 8, slides 36–37) 📘 ⭐⭐⭐ 🎯
| Network | Cost (₹ per unit) | CO₂ (kg per unit) | Recovery |
|---|---|---|---|
| A | 100 | 100 | 20% |
| B | 108 | 75 | 50% |
| C | 115 | 55 | 70% |
The company puts an internal price of **₹0.40 per kg CO₂** on emissions. Find the total cost of each network, select the best and recommend technologies.

**Q1.1 Objective function. [1 mark]**
**Minimise Z = Cᵢ + λ·Eᵢ** for the chosen network i, where Cᵢ = logistics cost per unit, Eᵢ = kg CO₂ per unit, λ = ₹0.40 per kg (Lecture 8: Z = C_total + λ·E_CO₂ + μ·W_waste; μ = 0 here).

**Q1.2 Decision variables. [1 mark]**
**y_A, y_B, y_C ∈ {0, 1}** = 1 if that network is selected, with y_A + y_B + y_C = 1 (exactly one network).

**Q1.3 Assumptions. [1 mark]**
Costs and CO₂ are per unit and constant with volume; all three networks give the same service level (OTIF); carbon price ₹0.40/kg is the firm's internal price; recovery is valued at zero in the base case.

**Q1.4 Total cost. [4 marks]**
| Network | Logistics cost | Carbon cost (λ × CO₂) | **Total Z** |
|---|---|---|---|
| A | 100 | 0.40 × 100 = 40.0 | **140.0** |
| B | 108 | 0.40 × 75 = 30.0 | **138.0** |
| C | 115 | 0.40 × 55 = 22.0 | **137.0** |
Switching prices: A = B at λ = 8 ÷ 25 = **₹0.32/kg**; B = C at λ = 7 ÷ 20 = **₹0.35/kg**. So A is best below ₹0.32, B between ₹0.32 and ₹0.35, **C above ₹0.35**.

**Q1.5 Compare and select. [1 mark]**
At λ = ₹0.40, **select Network C (₹137 per unit)**. Without a carbon price A would win (₹100); the decision depends on the decision-maker's priorities, as the slide says.

**Q1.6 Interpretation and technology. [2 marks]**
C costs ₹15 more per unit in logistics but saves 45 kg CO₂ and recovers 70% of material: *"the best sustainable network is not necessarily the cheapest network."* To close C's cost gap: **AI route optimisation** for the collection runs (fewer km, higher fill), **IoT/RFID tags** on returned products to grade them automatically at the sorting centre (lower handling cost, more reuse and remanufacture), and **blockchain** records of recovered material for verified recycled-content claims and EPR compliance.

---

## Q2 (10 marks). Road vs rail for a steel-products flow 📗 ⭐⭐⭐
A firm ships **20,000 t a year** Pune → Kolkata (1,800 km). Goods are worth ₹50,000 per t; inventory carrying cost 18% a year; internal carbon price ₹2,000 per t CO₂.
- **Scenario 1, Road:** ₹3.0 per t-km; 4 days door to door; 0.09 kg CO₂/t-km.
- **Scenario 2, Rail (multimodal):** 1,700 km rail at ₹1.8 per t-km and 0.025 kg/t-km + 100 km road first/last mile at ₹3.5 per t-km and 0.09 kg/t-km + handling ₹150 per t; 7 days.

**Q2.1 Objective function. [1 mark]**
**Minimise Z = Transport cost + In-transit inventory cost + Handling cost + λ·CO₂**, for 20,000 t a year.

**Q2.2 Decision variables. [1 mark]**
**x_road, x_rail** = tonnes per year by each mode, with x_road + x_rail = 20,000 and x ≥ 0 (here we compare the two pure scenarios: all road or all rail).

**Q2.3 Assumptions. [1 mark]**
Demand constant at 20,000 t; linear costs; 365 days; same safety stock policy (rail's extra 3 days handled by extra safety stock, shown separately); carbon price ₹2,000/t; factors as given.

**Q2.4 Total cost. [4 marks]**
| Cost line (₹ lakh) | Road | Rail |
|---|---|---|
| Transport | 20,000 × 1,800 × 3.0 = **1,080.0** | 20,000 × 1,700 × 1.8 = 612.0 + 20,000 × 100 × 3.5 = 70.0 → **682.0** |
| Handling | — | 20,000 × 150 = **30.0** |
| In-transit inventory | 20,000 × 50,000 × 0.18 × 4 ÷ 365 = **19.7** | × 7 ÷ 365 = **34.5** |
| CO₂ (t) | 20,000 × 1,800 × 0.09 ÷ 1,000 = 3,240 | 850 + 180 = 1,030 |
| Carbon cost | 3,240 × 2,000 = **64.8** | 1,030 × 2,000 = **20.6** |
| **Total Z** | **1,164.5** | **767.1** |

**Q2.5 Compare and select. [1 mark]**
**Select Scenario 2, rail: ₹7.67 crore vs ₹11.65 crore, a saving of ₹3.97 crore a year (34%) and 2,210 t CO₂ (−68%).** Even after adding 3 days of safety stock (≈ 164 t × ₹50,000 × 18% = ₹14.8 lakh), rail stays ≈ ₹3.8 crore cheaper.

**Q2.6 Interpretation and technology. [2 marks]**
Transport cost per t-km drives the result; rail is cheaper and greener, but slower. Keep **road for urgent orders** (10–20%) and move base volume by rail. Technologies: **IoT GPS trackers on rakes and containers** for real-time ETAs (lets the buyer cut the extra safety stock); **AI demand forecasting** to plan rail lots earlier; **blockchain e-documents** (e-BL, e-invoices) to cut handling delays and disputes at transfer points and give traceability.

---

## Q3 (10 marks). How many DCs? (facility, inventory and transport) 📗 ⭐⭐⭐
| DCs | Facility | Inventory | Inbound transport | Outbound transport | CO₂ (t/yr) |
|---|---|---|---|---|---|
| 1 | 4.0 | 6.0 | 2.0 | 20.0 | 5,800 |
| 2 | 7.0 | 7.5 | 2.6 | 13.0 | 4,500 |
| 3 | 10.0 | 8.7 | 3.2 | 9.5 | 4,075 |
| 4 | 13.0 | 9.8 | 3.8 | 7.8 | 4,100 |
| 5 | 16.0 | 10.8 | 4.4 | 7.0 | 4,350 |
(₹ crore a year.) Find the best number of DCs, with and without a carbon price of ₹2,000/t.

**Q3.1 Objective function. [1 mark]**
**Minimise Z(n) = Facility(n) + Inventory(n) + Inbound(n) + Outbound(n) + λ·CO₂(n)**, over n = 1 to 5 DCs.

**Q3.2 Decision variables. [1 mark]**
**n** = number of DCs opened; **yⱼ** = 1 if candidate DC j is opened; **xᵢⱼ** = flow from plant i or DC j to customer zones.

**Q3.3 Assumptions. [1 mark]**
Demand and service level are the same for every n; inventory rises with n (square-root law); costs as given; carbon price ₹2,000/t (= ₹0.002 crore per 10 t).

**Q3.4 Total cost. [4 marks]**
| DCs | Logistics total (₹ cr) | Carbon cost (CO₂ × 2,000) | **Z (₹ cr)** |
|---|---|---|---|
| 1 | 4.0 + 6.0 + 2.0 + 20.0 = **32.0** | 1.16 | **33.16** |
| 2 | **30.1** | 0.90 | **31.00** |
| 3 | **31.4** | 0.82 | **32.22** |
| 4 | **34.4** | 0.82 | **35.22** |
| 5 | **38.2** | 0.87 | **39.07** |

**Q3.5 Compare and select. [1 mark]**
**Select 2 DCs (₹30.1 crore; ₹31.0 crore with carbon).** 3 DCs has the lowest CO₂ but would only win at a carbon price above ₹1.3 crore ÷ 425 t = **₹30,588 per t**.

**Q3.6 Interpretation and technology. [2 marks]**
More DCs shorten the last mile but add buildings, inventory and inbound trips: total cost is U-shaped. With 2 DCs, outbound transport (₹13 crore, 43%) is the biggest line: **AI route optimisation and dynamic slotting** of deliveries can cut it 5–10%; **IoT-based warehouse energy management** with rooftop solar cuts facility energy; **AI forecasting + RFID** cuts the inventory needed to hold service with fewer DCs. A **digital twin** of the network can test a third DC before investing.

---

## Q4 (10 marks). Reverse network for 10,000 returns: centralised, decentralised or hybrid? 📗 ⭐⭐⭐
Each returned unit weighs 25 kg and is worth ₹2,000 in the pipeline; carrying cost 20% a year; road transport ₹4 per t-km and 0.09 kg CO₂/t-km.
| Scenario | Fixed facility cost (₹ lakh/yr) | Processing (₹/unit) | Average transport | Pipeline time |
|---|---|---|---|---|
| A: Centralised (one recovery plant) | 40 | 300 | 800 km | 12 days |
| B: Decentralised (4 regional centres) | 60 | 350 | 200 km | 5 days |
| C: Hybrid (3 local sorting centres + 1 central plant) | 58 | 310 | 150 km for all + 700 km for 40% | 8 days |

**Q4.1 Objective function. [1 mark]**
**Minimise Z = Fixed facility cost + Processing cost + Collection transport cost + Pipeline inventory cost (+ λ·CO₂)** for 10,000 returns a year, subject to Returns = Reuse + Repair + Remanufacture + Recycling + Disposal.

**Q4.2 Decision variables. [1 mark]**
**yⱼ** = 1 if recovery facility j is opened; **xᵢⱼ** = returns sent from collection point i to facility j; **rᵢ** = units recovered by each route.

**Q4.3 Assumptions. [1 mark]**
Volume fixed at 10,000; same recovery mix in every scenario; linear transport cost; 365 days; carbon optional.

**Q4.4 Total cost. [4 marks]**
| Cost line (₹ lakh) | A: Centralised | B: Decentralised | C: Hybrid |
|---|---|---|---|
| Fixed | 40.00 | 60.00 | 58.00 |
| Processing (10,000 × ₹) | 30.00 | 35.00 | 31.00 |
| Transport | 10,000 × 0.025 × 800 × 4 = **8.00** | × 200 = **2.00** | 0.025 × (150 + 0.4 × 700) × 4 × 10,000 = **4.30** |
| Pipeline inventory | 10,000 × 2,000 × 0.20 × 12 ÷ 365 = **1.32** | × 5/365 = **0.55** | × 8/365 = **0.88** |
| **Total** | **79.32** | **97.55** | **94.18** |
| CO₂ (t) | 2,00,000 t-km → 18.0 | 50,000 → 4.5 | 1,07,500 → 9.7 |

**Q4.5 Compare and select. [1 mark]**
**Select A, centralised (₹79.3 lakh).** It is ₹14.9–18.2 lakh cheaper; even at ₹2,000/t CO₂ its extra 13.5 t costs only ₹0.27 lakh more than B.

**Q4.6 Interpretation and technology. [2 marks]**
At low volume, fixed facility cost dominates, so one central plant wins (Lecture 8: centralised suits low-volume, high-value returns; decentralised suits high-volume, bulky returns). Technologies: **AI route optimisation / milk runs** to consolidate pickups (cut the ₹8 lakh transport and 18 t CO₂); **IoT/RFID tags and a returns app** to grade products at pickup so only units worth remanufacturing travel to the central plant; **blockchain product passports** recording product history for faster grading, warranty checks and verified recycled-content claims.

---

## Q5 (10 marks). FMCG distribution network: current vs improved (Lecture 10, slide 12) 📘 ⭐⭐⭐ 🎯
Scenario 1 (current): **10,000 deliveries a month**, average loaded distance **180 km**, diesel trucks, **62% vehicle utilisation**, **18% empty km**. Scenario 2 (improved): utilisation **80%**, empty km **10%**, same tonnage moved.

**Q5.1 Objective function. [1 mark]**
**Minimise Z = Fuel cost + Carbon cost** of monthly distribution = (total km ÷ km per litre) × ₹ per litre + CO₂ × λ, subject to delivering the same tonnage.

**Q5.2 Decision variables. [1 mark]**
**Number of trips Nᵗ**, **load per trip** (utilisation), **routing xᵢⱼ** (which truck serves which customers in which order), **backhaul allocation** to reduce empty km.

**Q5.3 Assumptions. [1 mark]**
9-t trucks; 4 km per litre; diesel ₹92/l and 2.68 kg CO₂/l; "18% empty" = share of total km; 180 km = loaded km per trip; driver and vehicle fixed costs ignored (they would favour Scenario 2 further).

**Q5.4 Total cost. [4 marks]**
| | Scenario 1: Current | Scenario 2: Improved |
|---|---|---|
| Tonnage | 10,000 × 0.62 × 9 = 55,800 t | 55,800 t |
| Trips | 10,000 | 55,800 ÷ (0.80 × 9) = **7,750** |
| Loaded km | 18,00,000 | 13,95,000 |
| Total km | ÷ 0.82 = **21,95,122** | ÷ 0.90 = **15,50,000** |
| Diesel (l) | ÷ 4 = **5,48,780** | **3,87,500** |
| Fuel cost | × ₹92 = **₹5.05 crore** | **₹3.57 crore** |
| CO₂ | × 2.68 = **1,470.7 t** | **1,038.5 t** |
| Carbon cost at ₹2,000/t | ₹0.29 crore | ₹0.21 crore |
| **Total Z** | **₹5.34 crore/month** | **₹3.77 crore/month** |
| g CO₂ per t-km | 146 | 103 |

**Q5.5 Compare and select. [1 mark]**
**Select Scenario 2: ₹1.57 crore a month cheaper (≈ ₹18.8 crore a year, −29%) and 432 t CO₂ a month less.**

**Q5.6 Interpretation and technology. [2 marks]**
The saving comes from eliminating kilometres, not from new trucks: *"the cleanest kilometre is often the kilometre eliminated."* Technologies: **AI route optimisation and load planning** to reach 80% utilisation; a **digital freight exchange** for backhauls (empty km 18% → 10%); **IoT telematics** for eco-driving, idling and tyre pressure (km per litre 4.0 → 4.4); then **EV trucks on renewable charging** for urban routes. Track the five slide KPIs: CO₂e per t-km, km per litre, utilisation %, empty km %, OTIF %.

---

## Q6 (10 marks). Choosing a DC site: distance, transport cost and facility cost 📗 ⭐⭐⭐
A firm serves five markets (grid unit = 100 km): Jaipur (2, 9) 3,000 t · Ahmedabad (1, 6) 5,000 t · Indore (4, 6) 2,000 t · Nagpur (7, 5) 4,000 t · Hyderabad (6, 1) 6,000 t. Candidate sites and annual facility cost: **Bhopal (4, 7) ₹1.20 crore · Aurangabad (4, 4) ₹1.50 crore · Nagpur (7, 5) ₹1.10 crore**. Road freight ₹2.5 per t-km, 0.09 kg CO₂/t-km; carbon price ₹2,000/t.

**Q6.1 Objective function. [1 mark]**
**Minimise Z = Facility cost + Σ (volume × distance × ₹2.5 per t-km) + λ·CO₂.**

**Q6.2 Decision variables. [1 mark]**
**yⱼ** = 1 if site j (Bhopal, Aurangabad, Nagpur) is opened, Σyⱼ = 1; **xⱼₖ** = tonnes shipped from DC j to market k (= market demand).

**Q6.3 Assumptions. [1 mark]**
Straight-line (Euclidean) distances × 100 km; demand fixed; same inventory at every site; road only.

**Q6.4 Total cost. [4 marks]**
Centre of gravity = (83,000 ÷ 20,000, 95,000 ÷ 20,000) = **(4.15, 4.75)**.
Load-distance (t × grid units): Bhopal **78,666**, Aurangabad **72,466**, Nagpur **80,686** (Aurangabad: Jaipur 5.385 × 3,000 + Ahmedabad 3.606 × 5,000 + Indore 2.000 × 2,000 + Nagpur 3.162 × 4,000 + Hyderabad 3.606 × 6,000).
| ₹ crore/yr | Bhopal | Aurangabad | Nagpur |
|---|---|---|---|
| Transport (score × 100 km × ₹2.5) | 1.97 | **1.81** | 2.02 |
| Facility | 1.20 | 1.50 | **1.10** |
| CO₂ (t) | 708 | **652** | 726 |
| Carbon cost | 0.14 | 0.13 | 0.15 |
| **Total Z** | **3.31** | **3.44** | **3.26** |

**Q6.5 Compare and select. [1 mark]**
**Select Nagpur (₹3.26 crore)**, although Aurangabad has the shortest distance and lowest CO₂: its higher facility cost outweighs the ₹21 lakh transport saving.

**Q6.6 Interpretation and technology. [2 marks]**
Distance criteria alone would pick Aurangabad; total cost picks Nagpur, so always add facility and inventory costs. To recover the extra 74 t CO₂ and transport cost at Nagpur: **AI route optimisation and consolidation** on the long Ahmedabad and Jaipur legs, **rail for the Nagpur–Hyderabad and Nagpur–Ahmedabad trunk flows**, **IoT energy monitoring and rooftop solar** at the DC, and a **digital twin** to re-test the choice as market volumes change.

---

## From the course material: where to practise more 🎯
| Exam-type item | Source | Page |
|---|---|---|
| Network A/B/C with objective function and λ | Lecture 8, slides 36–37 📘 | [P3 Problem 1](p3-network-logistics-numericals.md) |
| Allocating 10,000 returns (Returns = Reuse + Repair + Reman + Recycle + Disposal) | Lecture 8, slide 37 📘 | [P3 Problem 2](p3-network-logistics-numericals.md) |
| FMCG distribution network and five KPIs | Lecture 10, slide 12 📘 | [P3 Problem 3](p3-network-logistics-numericals.md) |
| Consumer-electronics network design exercise | Lecture 8, slide 42 📘 | [P3 Problem 10](p3-network-logistics-numericals.md) |
| ITC eChoupal network economics | HBS case in the zip 📘 | [P3 Problem 11](p3-network-logistics-numericals.md) |
| Centre of gravity, load-distance, factor rating, number of DCs | 📗 | [P3 Problems 5–7](p3-network-logistics-numericals.md) |
| Theory: objective function, decision variables, constraints | Lecture 8 📘 | [Designing the Sustainable Network](ch07-network-design.md) |
| Technologies for sustainability (IoT, AI, blockchain, digital twin) | Lecture 9 📘 | [Technology & Quality Tools](ch05-technology-quality-tools.md) |
