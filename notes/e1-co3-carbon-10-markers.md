# CO3 · 10-Mark Numericals: Carbon Accounting, Scope 1, 2, 3 by Scenario
**What the exam asks (teacher's importants):** *calculate Scope 1, Scope 2 and Scope 3 emissions for the different scenarios given, draw a comparison table of the scopes, and interpret which scenario is better at scope level and overall. Then give a short interpretation of which scope is huge, what actions are needed to mitigate it, and why.*

So every question below follows the same five steps: **classify → calculate each scope for each scenario → comparison table → scope-level and overall verdict → biggest scope, mitigation actions and why**. Q1 and Q4 use the course's own data (carbon deck, Tata Motors BRSR) 📘; Q2 and Q3 are practice questions in the same style 📗, on the course's emission factors. Turn on **Self-test** (`T`) to hide the answers.

---

## The 10-mark answer template ⭐⭐⭐
| Step | What to write | Marks |
|---|---|---|
| 1. Formula and classification | **Emissions = Activity data × Emission factor**; CO₂e = gas × GWP. Classify each source: **Scope 1** what you burn (own fuel, own vehicles, process, refrigerant leaks) · **Scope 2** what you buy (electricity, steam, heat) · **Scope 3** what you influence (purchased goods, hired transport, travel, commuting, use of sold products) | 1.5 |
| 2. Calculations per scenario | One line per source with units; kg → t (÷ 1,000) | 4 |
| 3. Comparison table | Rows = Scope 1, Scope 2, Scope 3, Total (and % of total, intensity per unit); columns = scenarios | 1.5 |
| 4. Verdict | **Scope level**: which scenario is lowest on each scope. **Overall**: lowest total (and lowest per unit if outputs differ) | 1 |
| 5. Interpretation | Which scope is huge (usually Scope 3), **actions** to mitigate it and **why** those actions work | 2 |

**Course emission factors 📘:** diesel **2.68 kg CO₂/l** · natural gas **1.9 kg/Sm³** · LPG **3.0 t/t** · Indian grid **0.70 t/MWh** · petrol car 120 g/km · GWP: CH₄ ≈ 28, N₂O 273, HFC-134a ≈ 1,430, SF₆ 25,200. Use the paper's factors if it gives different ones.

**Mitigation by scope (learn the "why"):**
| Scope | Actions | Why they work |
|---|---|---|
| Scope 1 | Electrify heat, switch DG sets to solar + storage, biomass/green hydrogen, fix refrigerant leaks, EV/CNG company fleet | Removes fuel combustion at source; leaks have very high GWP, so small fixes give big cuts |
| Scope 2 | Rooftop solar, renewable PPA/open access, RECs, energy efficiency (LED, VFD motors, compressed-air leaks) | Grid power is coal-heavy (0.70 t/MWh); renewable power is ~0 under market-based accounting |
| Scope 3 | **Supplier engagement** (green steel, recycled content, supplier RE targets), low-carbon materials, modal shift to rail, load consolidation, product efficiency and EVs, design for recycling, primary supplier data | Scope 3 is usually **70–90%+** of the footprint and sits with suppliers and customers, so only procurement, design and logistics decisions can move it |

---

## Q1 (10 marks). ICE cars vs EVs from the same plant (carbon deck, slides 17–19) 📘 ⭐⭐⭐ 🎯
One plant makes **50,000 ICE cars** and **20,000 EVs** a year. Scope 1: natural gas 5,00,000 Sm³, diesel 2,00,000 l, LPG 50 t. Scope 2: 25,000 MWh grid. Scope 3: materials 6 t/ICE car and 10 t/EV; logistics and travel 23,500 t (upstream 15,000 + travel 500 + distribution 8,000); use phase 1.5 lakh km, ICE 120 g/km, EV 0.15 kWh/km on the 0.70 kg/kWh grid. Allocate the shared Scope 1, Scope 2 and logistics by volume (50/70 and 20/70).
(a) Compute Scope 1, 2, 3 for each product line (scenario). (4) (b) Draw the comparison table, total and per vehicle. (2) (c) Which scenario is better at scope level and overall? (2) (d) Which scope is huge; actions and why. (2)

**Q1.1 (a) Calculations. [4 marks]**
*Plant Scope 1* = 5,00,000 × 1.9 ÷ 1,000 (950 t) + 2,00,000 × 2.68 ÷ 1,000 (536 t) + 50 × 3.0 (150 t) = **1,636 t**. *Plant Scope 2* = 25,000 × 0.70 = **17,500 t**.
- **ICE line:** Scope 1 = 1,636 × 50/70 = **1,168.6 t**; Scope 2 = 17,500 × 50/70 = **12,500 t**; Scope 3 = materials 50,000 × 6 = 3,00,000 + use 50,000 × (1,50,000 × 120 g = 18 t) = 9,00,000 + logistics 23,500 × 50/70 = 16,785.7 → **12,16,785.7 t**.
- **EV line:** Scope 1 = 1,636 × 20/70 = **467.4 t**; Scope 2 = 17,500 × 20/70 = **5,000 t**; Scope 3 = materials 20,000 × 10 = 2,00,000 + use 20,000 × (22,500 kWh × 0.70 = 15.75 t) = 3,15,000 + logistics 23,500 × 20/70 = 6,714.3 → **5,21,714.3 t**.

**Q1.2 (b) Comparison table. [2 marks]**
| Scope | ICE line (t) | EV line (t) | ICE per car (t) | EV per car (t) |
|---|---|---|---|---|
| Scope 1 | 1,168.6 | 467.4 | 0.02 | 0.02 |
| Scope 2 | 12,500.0 | 5,000.0 | 0.25 | 0.25 |
| Scope 3 | 12,16,785.7 | 5,21,714.3 | 24.34 | 26.09 |
| **Total** | **12,30,454.3** | **5,27,181.7** | **24.61** | **26.36** |
| Scope 3 share | 98.9% | 99.0% | | |
Plant total = **17,57,636 t CO₂e**; Scope 1 + 2 = 1.09%, Scope 3 = 98.9%.

**Q1.3 (c) Verdict at scope level and overall. [2 marks]**
- **Scope 1 and 2:** equal per car (shared plant, allocated by volume), so no difference at scope level.
- **Scope 3:** per car, **ICE is lower (24.34 t vs 26.09 t)** on today's Indian grid. The EV's materials are heavier (10 t vs 6 t, battery) and its use phase is only slightly lower (15.75 t vs 18 t).
- **Overall:** in absolute terms the EV line is smaller only because it makes fewer cars; **per vehicle the ICE car is about 7% lower (24.61 vs 26.36 t)**. If the EVs are charged on renewable power, the slide's figures show the EV falling to about **13 t** vs ICE ~25 t, so the **EV becomes the better scenario by about half**.

**Q1.4 (d) Huge scope, actions and why. [2 marks]**
**Scope 3 is huge (≈ 99%)**: use phase 69% and purchased materials 28% of the plant total. Even a zero-emission factory would cut only about 1%. Actions: (1) **supplier decarbonisation**: green steel and aluminium, low-carbon cells with recycled cobalt and lithium (cuts Category 1); (2) **renewable charging partnerships** and better kWh/km (cuts Category 11, where the EV benefit depends on grid cleanliness); (3) **battery recycling and second life** (cuts future Category 1 and 12). Why: the emissions sit in suppliers' factories and customers' driving, so only procurement and product decisions can reduce them. This is the Toyota/Tesla route the slide points to.

---

## Q2 (10 marks). An auto-component plant: four decarbonisation scenarios 📗 ⭐⭐⭐
A plant making **20,000 units** a year has these data in the **base case (Scenario A)**: natural gas furnace 3,00,000 Sm³; diesel DG sets 80,000 l; company vehicles 20,000 l diesel; refrigerant R-134a top-up 60 kg (GWP 1,430); grid electricity 5,000 MWh; purchased steel 4,000 t (2.2 t CO₂e/t); inbound road freight 30,00,000 t-km and outbound 25,00,000 t-km (0.09 kg/t-km); business travel 100 t; employee commuting 150 t.
- **Scenario B (clean energy):** solar + PPA cover 60% of grid electricity; DG sets replaced by solar + batteries; the furnace is electrified on renewable power (natural gas removed). Everything else as A.
- **Scenario C (green supply chain):** energy as A; steel from a green-steel supplier at 1.2 t/t; 70% of inbound t-km moved to rail (0.025 kg/t-km); outbound consolidation cuts outbound t-km by 20%; commuting halved with EV buses.
- **Scenario D:** B and C together.
(a) Compute Scope 1, 2, 3 for each scenario. (5) (b) Comparison table with totals, per-unit intensity and % reduction vs A. (2) (c) Which scenario is better at scope level and overall? (1) (d) Which scope is huge; actions and why. (2)

**Q2.1 (a) Calculations. [5 marks]**
*Scenario A*
- Scope 1: natural gas 3,00,000 × 1.9 ÷ 1,000 = 570.0 · DG diesel 80,000 × 2.68 ÷ 1,000 = 214.4 · vehicles 20,000 × 2.68 ÷ 1,000 = 53.6 · R-134a 60 × 1,430 ÷ 1,000 = 85.8 → **923.8 t**
- Scope 2: 5,000 × 0.70 = **3,500.0 t**
- Scope 3: steel 4,000 × 2.2 = 8,800 · inbound 30,00,000 × 0.09 ÷ 1,000 = 270 · outbound 25,00,000 × 0.09 ÷ 1,000 = 225 · travel 100 · commuting 150 → **9,545.0 t**

*Scenario B*: Scope 1 = vehicles 53.6 + R-134a 85.8 = **139.4 t** (gas and DG removed) · Scope 2 = 40% × 5,000 = 2,000 MWh × 0.70 = **1,400.0 t** (the electrified furnace runs on renewable power, ≈ 0 market-based) · Scope 3 = **9,545.0 t** (unchanged).

*Scenario C*: Scope 1 = **923.8 t** · Scope 2 = **3,500.0 t** · Scope 3: steel 4,000 × 1.2 = 4,800 · inbound road 9,00,000 × 0.09 ÷ 1,000 = 81.0 + rail 21,00,000 × 0.025 ÷ 1,000 = 52.5 · outbound 20,00,000 × 0.09 ÷ 1,000 = 180 · travel 100 · commuting 75 → **5,288.5 t**.

*Scenario D*: Scope 1 = **139.4 t** · Scope 2 = **1,400.0 t** · Scope 3 = **5,288.5 t**.

**Q2.2 (b) Comparison table. [2 marks]**
| Scope (t CO₂e) | A: Base | B: Clean energy | C: Green supply chain | D: B + C |
|---|---|---|---|---|
| Scope 1 | 923.8 | **139.4** | 923.8 | **139.4** |
| Scope 2 | 3,500.0 | **1,400.0** | 3,500.0 | **1,400.0** |
| Scope 3 | 9,545.0 | 9,545.0 | **5,288.5** | **5,288.5** |
| **Total** | **13,968.8** | **11,084.4** | **9,712.3** | **6,827.9** |
| Per unit (t) | 0.698 | 0.554 | 0.486 | **0.341** |
| Reduction vs A | — | 20.6% | 30.5% | **51.1%** |
Shares in A: Scope 1 **6.6%**, Scope 2 **25.1%**, Scope 3 **68.3%** (steel alone 63%).

**Q2.3 (c) Verdict. [1 mark]**
**Scope level:** B (and D) is best on Scope 1 and Scope 2; C (and D) is best on Scope 3. **Overall:** **D is best (−51%)**. Of the single strategies, **C beats B (−30.5% vs −20.6%)** even though B transforms the factory, because C attacks the largest scope.

**Q2.4 (d) Huge scope, actions and why. [2 marks]**
**Scope 3 is huge (68%)**, and purchased steel is most of it. Actions: (1) contract **green or high-recycled-content steel** and set supplier carbon targets in the scorecard (CO2 link); (2) **modal shift to rail** and load consolidation for freight; (3) collect **primary data** from suppliers instead of average factors. Why: a tonne of steel avoided or decarbonised at the supplier saves more than every fuel and electricity measure inside the plant combined (4,000 t vs 2,884 t in B). Then do B as well, because Scope 1 + 2 are the scopes the firm fully controls and reports under BRSR Core.

---

## Q3 (10 marks). A 3PL's fleet: diesel, grid EV, solar EV or outsourcing? 📗 ⭐⭐⭐
A 3PL owns **200 diesel trucks** (1,00,000 km a year each, 4 km/l). Forklifts use 30 t LPG; reefer trucks leak 200 kg HFC-134a (GWP 1,430); warehouses use 6,000 MWh of grid power; sub-contracted haulage is 5 crore t-km (0.09 kg/t-km); business travel 150 t.
- **Scenario A:** as above.
- **Scenario B:** 50 trucks replaced by e-trucks (1.2 kWh/km) charged from the grid.
- **Scenario C:** the same 50 e-trucks charged from a solar PPA.
- **Scenario D:** instead of buying e-trucks, the work of those 50 trucks is **sub-contracted** to diesel carriers.
(a) Compute Scope 1, 2, 3 for each scenario. (5) (b) Comparison table. (2) (c) Verdict at scope level and overall. (1) (d) Interpretation and actions. (2)

**Q3.1 (a) Calculations. [5 marks]**
*Scenario A*: diesel = 200 × 1,00,000 ÷ 4 = 50,00,000 l × 2.68 ÷ 1,000 = 13,400 t · LPG 30 × 3.0 = 90 t · HFC 200 × 1,430 ÷ 1,000 = 286 t → **Scope 1 = 13,776 t** · **Scope 2** = 6,000 × 0.70 = **4,200 t** · **Scope 3** = 5,00,00,000 × 0.09 ÷ 1,000 = 4,500 + 150 = **4,650 t**.
*The 50 trucks:* 50 × 1,00,000 = 50,00,000 km → diesel 12,50,000 l × 2.68 = **3,350 t**; as e-trucks they need 50,00,000 × 1.2 = 60,00,000 kWh = **6,000 MWh**.
*Scenario B*: Scope 1 = 13,776 − 3,350 = **10,426 t** · Scope 2 = 4,200 + 6,000 × 0.70 = **8,400 t** · Scope 3 = **4,650 t**.
*Scenario C*: Scope 1 = **10,426 t** · Scope 2 = **4,200 t** (solar ≈ 0) · Scope 3 = **4,650 t**.
*Scenario D*: Scope 1 = **10,426 t** · Scope 2 = **4,200 t** · Scope 3 = 4,650 + 3,350 = **8,000 t** (the same diesel, now burnt by sub-contractors).

**Q3.2 (b) Comparison table. [2 marks]**
| Scope (t CO₂e) | A: Diesel | B: EV on grid | C: EV on solar | D: Outsource |
|---|---|---|---|---|
| Scope 1 | 13,776 | 10,426 | 10,426 | 10,426 |
| Scope 2 | 4,200 | 8,400 | 4,200 | 4,200 |
| Scope 3 | 4,650 | 4,650 | 4,650 | 8,000 |
| **Total** | **22,626** | **23,476** | **19,276** | **22,626** |
| Change vs A | — | **+3.8%** | **−14.8%** | 0% |

**Q3.3 (c) Verdict. [1 mark]**
**Scope level:** B, C and D all cut Scope 1 by 3,350 t; B doubles Scope 2; D raises Scope 3. **Overall: C is best (−3,350 t, −14.8%)**. B is *worse* than doing nothing, because India's grid (0.70 kg/kWh) is above the break-even of 3,350 ÷ 6,000 = **0.56 kg/kWh**. D changes nothing in reality: it only moves emissions from Scope 1 to Scope 3.

**Q3.4 (d) Interpretation and actions. [2 marks]**
**Scope 1 is huge here (61% in A)** because a transport company burns its own fuel. Actions: (1) e-trucks **only with renewable charging** (depot solar, green open-access); (2) cut diesel per t-km through **AI route optimisation, load consolidation and backhauls** (fewer empty km); (3) **fix reefer leaks** and move to low-GWP refrigerants (286 t from just 200 kg). Why: these remove combustion and leaks at source. Outsourcing (D) is not a reduction: *"do not outsource sustainability"*, and customers will see the same tonnes in their own Scope 3.

---

## Q4 (10 marks). Tata Motors (CV business) FY24 vs FY25 from the BRSR (course file) 📘 ⭐⭐ 🎯
| t CO₂e | FY24 (restated) | FY25 |
|---|---|---|
| Scope 1 | 48,736 | 43,754 |
| Scope 2 (market-based) | 1,72,409 | 1,31,407 |
| Scope 3: Cat 1 purchased goods | 61,09,148 | 52,28,249 |
| Scope 3: Cat 11 use of sold products | 15,86,21,101 | 13,95,71,557 |
| Scope 3 total | 16,48,85,353 | 14,49,44,801 |
Scope 1 + 2 intensity: 0.552 (FY24) and 0.462 (FY25) t per vehicle.
(a) Compute totals, shares and % change for each scope. (4) (b) Comparison table. (2) (c) Which year is better at scope level and overall? (2) (d) Which scope is huge; actions and why. (2)

**Q4.1 (a) Calculations. [4 marks]**
- FY24: Scope 1 + 2 = 2,21,145 t; total = 2,21,145 + 16,48,85,353 = **16,51,06,498 t**.
- FY25: Scope 1 + 2 = 1,75,161 t; total = 1,75,161 + 14,49,44,801 = **14,51,19,962 t**.
- Change: Scope 1 **−10.2%**; Scope 2 **−23.8%**; Scope 3 **−12.1%**; total **−12.1%**.
- Shares (FY25): Scope 1 **0.03%**, Scope 2 **0.09%**, Scope 3 **99.88%**; Cat 11 = **96.3%** of Scope 3. Vehicles ≈ 1,75,161 ÷ 0.462 ≈ **3.79 lakh**.

**Q4.2 (b) Comparison table. [2 marks]**
| Scope | FY24 | FY25 | Change |
|---|---|---|---|
| Scope 1 | 48,736 | 43,754 | −10.2% |
| Scope 2 | 1,72,409 | 1,31,407 | −23.8% |
| Scope 3 | 16,48,85,353 | 14,49,44,801 | −12.1% |
| **Total** | **16,51,06,498** | **14,51,19,962** | **−12.1%** |
| Scope 1 + 2 per vehicle | 0.552 t | 0.462 t | −16.3% |

**Q4.3 (c) Verdict. [2 marks]**
**FY25 is better on every scope and overall.** The biggest relative gain is Scope 2 (−23.8%, more renewable power and iRECs); Scope 1 + 2 per vehicle fell 16%, so the gain is real efficiency, not just lower volume. Caution: part of the Scope 3 drop may be lower sales and spend-based estimates (Cat 1), not real supplier reductions.

**Q4.4 (d) Huge scope, actions and why. [2 marks]**
**Scope 3, Category 11 (customers' diesel over the trucks' life) is huge: 96% of Scope 3 and ~827 times Scope 1 + 2.** Actions: (1) shift the product mix to **EV, CNG/LNG and hydrogen trucks** (like the Hindustan Zinc–GreenLine deal); (2) **fuel efficiency and telematics** for eco-driving; (3) replace spend-based Cat 1 with **supplier-specific data** and run supplier decarbonisation; (4) the **Re.Wi.Re** scrapping network to retire old, dirty trucks. Why: the footprint is in how the product is used, so only product design and portfolio decisions move it.

---

## From the course material: where to practise more 🎯
| Exam-type item | Source | Page |
|---|---|---|
| ICEV + EV plant, full Scope 1-2-3 | Carbon deck, slides 17–19 📘 | [P2 Problem 1](p2-carbon-accounting-numericals.md) |
| Diesel example and GWP conversion | Carbon deck 📘 | [P2 Problem 2](p2-carbon-accounting-numericals.md) |
| Full inventory with a solar PPA scenario | 📗 | [P2 Problem 3](p2-carbon-accounting-numericals.md) |
| TVS Motor BRSR (FY23 vs FY24) | TVS BRSR in the zip 📘 | [P2 Problem 4](p2-carbon-accounting-numericals.md) |
| Tata Motors BRSR (FY24 vs FY25) | Tata Motors BRSR in the zip 📘 | [P2 Problem 5](p2-carbon-accounting-numericals.md) |
| EV vs ICE on India's grid (WTW) | IISc papers + Rietmann 📘 | [P5 Problem 4](p5-lca-energy-numericals.md) |
| Theory: scopes, 15 categories, MRV, net zero | Carbon deck 📘 | [LCA & Carbon Footprints](ch02-lca-carbon-footprints.md) |
