# LCA, Life-Cycle Costing & Energy-Sector Numericals
This page supports **CO3** (carbon footprints sit inside LCA) and the syllabus topics **"Introduction to environmental LCA and carbon footprints"** and **"Supply chain in the energy sector"**. It uses the **Lecture 4** functional-unit examples, the **Lecture 5** LCSA examples (laptop E-LCA, petrol vs electric car, LED vs incandescent LCC, packaging LCSA), the two **IISc papers** on Tank-to-Wheel and Well-to-Wheel efficiency of Indian automotive fuels, the **Rietmann et al. (2020)** EV-forecast paper and the **Tesla battery supply chain** case from the course zip 📘. Practice data are marked 📗. Turn on **Self-test** (`T`) to hide answers.

Theory: [LCA & Carbon Footprints](ch02-lca-carbon-footprints.md) and [Supply Chain in the Energy Sector](ch09-energy-sector.md).

---

## Formulas and conventions ⭐⭐⭐
- **LCA (ISO 14040/14044)** has four phases: goal and scope (including the **functional unit** and system boundary), life-cycle inventory (LCI), life-cycle impact assessment (LCIA) and interpretation.
- **Impact = Σ (inventory flow × characterisation factor).** For climate change the factor is the GWP: CO₂ = 1, CH₄ ≈ 28–30, N₂O ≈ 265–273 (AR5/AR6, 100-year).
- **Always compare on the same functional unit.** Impact per functional unit = impact per product ÷ number of functional units the product delivers.
- **Life-cycle stages:** raw materials → manufacturing → distribution → use → end-of-life. Boundaries: cradle-to-gate, gate-to-gate, cradle-to-grave, cradle-to-cradle.
- **LCSA = E-LCA + S-LCA + LCC** (Klöpffer 2008, Lecture 5).
- **Life-cycle cost (LCC / TCO)** = purchase + operating (energy) + maintenance + replacement + end-of-life cost − residual value.
- **Use-phase electricity emissions** = power (kW) × hours × grid emission factor. Indian grid factor: about 0.71–0.79 kg CO₂ per kWh in the course sources (CEA ~0.71–0.72; Rietmann uses 0.791).
- **Well-to-Wheel efficiency = Well-to-Tank efficiency × Tank-to-Wheel efficiency.** WTT covers recovery, refining or generation, and transport/T&D; TTW covers the vehicle.
- **Energy at source per km** = energy needed at the wheels per km ÷ WTW efficiency.
- **Logistic growth (Rietmann):** I(t) = L ÷ [1 + (L ÷ I(0) − 1) · e^(−k·L·t)], where L is the saturation level.
- **Renewable generation** = capacity (MW) × capacity utilisation factor × 8,760 hours; avoided CO₂ = MWh × grid factor.

---

## Problem 1. The functional unit — why "per product" comparisons mislead (Lecture 4) 📘 concept + 📗 data ⭐⭐⭐
Lecture 4 calls the functional unit *"the most misunderstood"* part of LCA and gives examples such as **delivering 1 litre of …**, **carrying 20 kg of groceries** and **storing 159 litres of petrol**. The functional unit describes the *function delivered*, not the product.

A retailer compares carry bags. A plastic bag weighs 10 g, carries 10 kg and is used once; its footprint is 2.5 kg CO₂e per kg of plastic. A cotton bag weighs 150 g, carries 20 kg and lasts 150 trips; its footprint is 20 kg CO₂e per kg of cotton.

**Q1.1 Which bag looks greener "per bag"?**
Plastic: 0.010 × 2.5 = **0.025 kg CO₂e per bag**. Cotton: 0.150 × 20 = **3.0 kg CO₂e per bag**. Per bag, cotton is 120 times worse.

**Q1.2 Define a functional unit and compare again.**
Functional unit: *carrying 20 kg of groceries home once a week (or 500 trips) over its service life.*
- Plastic: 2 bags per trip × 500 trips = 1,000 bags × 0.025 = **25 kg CO₂e**.
- Cotton: 500 ÷ 150 = 3.33 bags × 3.0 = **10 kg CO₂e** (12 kg if you buy 4 whole bags).
- On the functional unit, **cotton is about 60% lower**.

**Q1.3 How many uses must the cotton bag achieve to break even with plastic?**
Plastic per trip = 2 × 0.025 = 0.05 kg. Break-even = 3.0 ÷ 0.05 = **60 uses**. If shoppers lose or discard the cotton bag before 60 trips, plastic wins on carbon (though not on litter or marine pollution, which a full LCIA would capture in other impact categories). This is why LCA conclusions depend on the functional unit, the use pattern and the impact categories chosen.

## Problem 2. Laptop E-LCA: where are the hotspots? (Lecture 5) 📘 + 📗 ⭐⭐⭐
Lecture 5: *"Manufacturing 1 laptop = 320 kg CO₂e + 18,000 L water + 850 MJ energy."* Add (📗): the laptop draws 50 W, is used 8 hours a day for 250 days a year over 4 years; grid factor 0.71 kg/kWh; distribution and end-of-life add 20 kg CO₂e.

**Q2.1 Compute the cradle-to-grave carbon footprint and the share of each stage.**
- Use-phase electricity = 0.050 kW × 8 × 250 × 4 = **400 kWh** → 400 × 0.71 = **284 kg CO₂e**.
- Total = 320 + 284 + 20 = **624 kg CO₂e**.
- Shares: manufacturing **51%**, use **46%**, distribution + EoL **3%**.

**Q2.2 The company extends life to 6 years through repair and a battery swap. What happens to the footprint per year of service?**
- 6-year total = 320 + (0.050 × 8 × 250 × 6 × 0.71 = 426) + 20 = **766 kg**.
- Per year: 4-year life = 624 ÷ 4 = **156 kg/yr**; 6-year life = 766 ÷ 6 = **127.7 kg/yr** → **18% lower** per year of service.
The manufacturing "embodied" carbon is spread over more years. This is the logic of the R-strategies (repair, refurbish) in Lecture 8 and of product-as-a-service models.

**Q2.3 What would a carbon footprint study miss that a full LCA catches?**
A carbon footprint reports only GWP (kg CO₂e). A full LCA would also report the 18,000 L of water (water scarcity), the 850 MJ of energy (resource depletion), toxicity from electronics manufacturing and e-waste, and metal depletion (cobalt, gold, rare earths). Lecture 4: *a carbon footprint is a single-issue subset of LCA.*

## Problem 3. LED vs incandescent bulb — life-cycle costing (Lecture 5) 📘 + 📗 ⭐⭐⭐
Lecture 5's LCC table: LED purchase ₹250, lifetime 25,000 hours, electricity very low, maintenance low; incandescent purchase ₹40, lifetime 1,000 hours, electricity high, maintenance high. Add (📗): LED 9 W, incandescent 60 W, electricity ₹8 per kWh, grid factor 0.70 kg CO₂ per kWh. Functional unit: **25,000 hours of light at equal brightness**.

**Q3.1 Compute the life-cycle cost and CO₂ of each option.**

| | Incandescent | LED |
|---|---|---|
| Bulbs needed | 25,000 ÷ 1,000 = 25 | 1 |
| Purchase cost | 25 × ₹40 = ₹1,000 | ₹250 |
| Energy | 0.060 × 25,000 = 1,500 kWh | 0.009 × 25,000 = 225 kWh |
| Energy cost | 1,500 × ₹8 = ₹12,000 | 225 × ₹8 = ₹1,800 |
| **Life-cycle cost** | **₹13,000** | **₹2,050** |
| **Use-phase CO₂** | 1,500 × 0.70 = **1,050 kg** | 225 × 0.70 = **157.5 kg** |

The LED costs **84% less** over its life and emits **85% less CO₂**, even though its purchase price is 6.25 times higher.

**Q3.2 How many hours until the LED pays back its higher purchase price?**
Extra purchase cost = ₹250 − ₹40 = ₹210. Hourly saving = (60 − 9) W × ₹8 ÷ 1,000 = ₹0.408 per hour. Payback = 210 ÷ 0.408 ≈ **515 hours** (about two months at 8 hours a day), and that ignores the 24 replacement bulbs the incandescent option needs.

**Q3.3 What is the general managerial lesson?**
Purchase price is a poor decision criterion when most of the cost and impact sits in the use phase. This is the same TCO logic as sustainable procurement (Lecture 6): *cost vs value*.

## Problem 4. Petrol car vs electric car in India (Lecture 5 + Rietmann 2020) 📘 + 📗 ⭐⭐⭐
Lecture 5's qualitative E-LCA: raw materials — petrol medium, EV high (battery metals); manufacturing — petrol medium, EV high; use phase — petrol very high emissions, EV low; maintenance — petrol medium, EV low; end-of-life — petrol recycling possible, EV battery recycling critical. *"If only manufacturing is studied, the petrol car appears greener. If the entire life cycle is studied, the electric car generally has much lower lifetime emissions."*

Rietmann et al. (2020) give India-specific data: ICE car **0.135 kg CO₂ per km**; EV consumption **0.185 kWh per km**; Indian grid **0.791 kg CO₂ per kWh**; average driving **20,800 km per year**. Add (📗): manufacturing footprint ICE 6 t, EV 10 t (the battery adds about 4 t); life 10 years.

**Q4.1 Compare the use-phase emissions per km.**
- EV = 0.185 × 0.791 = **0.146 kg CO₂ per km**. ICE = **0.135 kg per km**.
- On India's coal-heavy grid the EV is about **8% worse** per km in the use phase. This is why Rietmann finds India's transport CO₂ still rising (+129.5% between 2018 and 2035) even with EV adoption.

**Q4.2 Compute 10-year lifecycle emissions.**
- Distance = 20,800 × 10 = 2,08,000 km.
- ICE = 6 + 0.135 × 2,08,000 ÷ 1,000 = 6 + 28.1 = **34.1 t CO₂**.
- EV = 10 + 0.146 × 2,08,000 ÷ 1,000 = 10 + 30.4 = **40.4 t CO₂**.

**Q4.3 At what grid factor does the EV break even (a) per km and (b) over the life cycle?**
- (a) Per km: 0.135 ÷ 0.185 = **0.730 kg/kWh**.
- (b) Lifecycle: 10 + 0.185 × g × 208 = 34.08 → g = 24.08 ÷ 38.48 = **0.626 kg/kWh**.
- If the grid reaches 0.45 kg/kWh (more renewables), EV lifecycle = 10 + 0.185 × 0.45 × 208 = **27.3 t**, about **20% below ICE**.

**Q4.4 What does this tell a supply-chain manager electrifying a fleet?**
Electrification only cuts emissions when paired with **clean electricity** (on-site solar, green PPAs, green tariffs). Without it, emissions shift from Scope 1 (diesel) to Scope 2 (grid power) and may even rise. It also shows why LCA boundaries matter: a tailpipe-only (TTW) view would wrongly score the EV as zero-emission.

## Problem 5. Well-to-Wheel efficiency of Indian fuels (IISc papers) 📘 + 📗 ⭐⭐
Key results from the two IISc papers: liquid petroleum fuels have **WTT efficiencies of 75–85%** (LPG best at 85%); **electricity WTT is only about 20%** because 69.9% of power comes from coal, a typical Indian coal plant runs at about 22% efficiency and **T&D losses are 25.4%**; hydrogen from natural-gas reforming has WTT of about 48% (reforming at 70%); TTW efficiencies are 15–27% for gasoline/LPG and 25–32% for diesel; hybridisation raises WTW efficiency by an average of **41%** and cuts WTW energy by **29%**; the **diesel split hybrid** is the most efficient configuration and a BEV on the Indian grid is roughly equal to a gasoline car on WTW.

**Q5.1 Compute WTW efficiency for these vehicles (📗 TTW values within the paper's ranges): gasoline car (WTT 80%, TTW 20%); diesel car (80%, 28%); BEV (WTT 20%, TTW 80%); hydrogen fuel-cell car (48%, 30%); diesel split hybrid (80%, 28% × 1.41).**

| Vehicle | WTT | TTW | WTW = WTT × TTW | Source energy per km if 0.5 MJ/km is needed at the wheels |
|---|---|---|---|---|
| Gasoline | 0.80 | 0.20 | **16.0%** | 0.5 ÷ 0.160 = 3.13 MJ |
| Diesel | 0.80 | 0.28 | **22.4%** | 2.23 MJ |
| BEV (Indian grid) | 0.20 | 0.80 | **16.0%** | 3.13 MJ |
| Hydrogen FCEV | 0.48 | 0.30 | **14.4%** | 3.47 MJ |
| Diesel split hybrid | 0.80 | 0.395 | **31.6%** | 1.58 MJ |

The ranking matches the paper: diesel hybrid best, BEV ≈ gasoline, hydrogen lowest.

**Q5.2 Show how the electricity WTT of about 20% arises.**
WTT is a chain of stage efficiencies: coal recovery and transport (~0.95) × weighted generation efficiency across the mix (~0.29, 📗) × (1 − 0.254 T&D losses = 0.746) = 0.95 × 0.29 × 0.746 ≈ **0.206 ≈ 20%**. Cutting T&D losses to 10% alone would raise WTT to 0.95 × 0.29 × 0.90 = 24.8%, a 20% relative gain. *Supply-chain lesson: in the energy sector the losses are upstream (generation and distribution), not at the point of use.*

## Problem 6. Forecasting EV adoption with the logistic curve (Rietmann 2020) 📘 + 📗 ⭐⭐
Rietmann et al. model EV adoption with the logistic function I(t) = L ÷ [1 + (L ÷ I(0) − 1) · e^(−k·L·t)]. Their findings: EVs reach a 30% fleet share globally by about 2032 and 42.5% of the fleet by 2035, yet global passenger-car CO₂ still rises until about 2035; EV consumption 0.185 kWh/km; 17,000 km per year; ICE 2.45 kg CO₂ per litre.

Assume (📗) a saturation share L = 100%, today's share I(0) = 2.5% and k·L = 0.35 per year.

**Q6.1 Forecast the EV share after 5, 10 and 15 years.**
I(t) = 1 ÷ [1 + 39 · e^(−0.35t)].
- t = 5: e^(−1.75) = 0.174 → 1 ÷ (1 + 6.78) = **12.9%**.
- t = 10: e^(−3.5) = 0.0302 → 1 ÷ (1 + 1.18) = **45.9%**.
- t = 15: e^(−5.25) = 0.00525 → 1 ÷ (1 + 0.205) = **83.0%**.
The S-curve is slow at first, fastest around 50% and then saturates.

**Q6.2 When does the share reach 30%?**
0.30 = 1 ÷ (1 + 39e^(−0.35t)) → 39e^(−0.35t) = 2.333 → e^(−0.35t) = 0.0598 → t = ln(16.71) ÷ 0.35 = **8.0 years**.

**Q6.3 Reproduce Rietmann's charging-energy figure: 439 million EVs, 17,000 km a year, 0.185 kWh per km.**
Energy = 439 × 10⁶ × 17,000 × 0.185 = 1.38 × 10¹⁵ Wh = **1,381 TWh per year**. That is new electricity demand of the size of a large country's whole grid, so power-sector supply chains (generation, transmission, charging infrastructure) must expand with the vehicle fleet.

**Q6.4 For India, compare annual CO₂ per car: EV at 0.791 kg/kWh vs ICE at 0.135 kg/km, 20,800 km per year.**
EV = 20,800 × 0.185 × 0.791 = **3.04 t per year**; ICE = 20,800 × 0.135 = **2.81 t per year**. Same conclusion as Problem 4: India must decarbonise the grid for EVs to help.

## Problem 7. Tesla battery end-of-life economics (HBS case) 📘 + 📗 ⭐⭐⭐
From the case: by 2025 up to **10,000** Tesla packs could need replacement, rising to **50,000 a year by 2030**; globally **1.2 million tonnes** of EV batteries will need disposal annually by 2030; only about **5%** of Li-ion batteries are recycled (95% reach municipal waste); second-life adaptation costs **$3,500 per battery for direct reuse, $6,700 when dismantled to module level, $8,000 at cell level**; recycling returns stay at about **$5,600 per battery after 2025**; recycling can recover about half of critical materials and cut up to **70% of GHG emissions**; replacing 5–30% of cells can restore a pack to 95% state of health.

**Q7.1 What is the annual recycling value of Tesla's replacement packs in 2025 and 2030?**
2025: 10,000 × $5,600 = **$56 million**. 2030: 50,000 × $5,600 = **$280 million a year**.

**Q7.2 A used pack has 60 kWh nominal capacity and 70% state of health. Stationary-storage buyers pay $100 per usable kWh (📗). Compare direct reuse, module-level reuse and recycling.**
- Second-life value = 60 × 0.70 × $100 = **$4,200**.
- Direct reuse net = 4,200 − 3,500 = **+$700**, and the pack can still be recycled later (about $5,600 then), so the total value chain is about $6,300.
- Module-level reuse net = 4,200 − 6,700 = **−$2,500** (only worth it if module grading lifts the value above $6,700).
- Cell-level reuse net = 4,200 − 8,000 = **−$3,800**.
- Immediate recycling = **+$5,600**.
**Answer:** on these numbers immediate recycling ($5,600) beats direct reuse alone ($700) on cash, but **reuse first, recycle later** (≈ $6,300) maximises value and follows the waste hierarchy (EPA and EU directive: reduce → reuse → recycle → recover → dispose). Deeper dismantling only pays if second-life prices rise.

**Q7.3 Which strategy (build, buy or partner) would you recommend for Tesla's recycling, and why?**
**Partner** in the short term with specialists such as **Redwood Materials** (founded by Tesla's ex-CTO J.B. Straubel; about 95% recovery; valued at $3.78 billion) or **Li-Cycle** (5,000 t a year in Kingston, Ontario; >95% recovery; raised $1.6 billion). Volumes (10,000 packs in 2025) are too small for an efficient in-house plant, and recycling cost is highly sensitive to volume. Build in-house capability (for example at the Gigafactories) once volumes approach 50,000 packs a year, which also secures cobalt, nickel and lithium and reduces exposure to the DRC (≈65% of cobalt) and to ESG-rating criticism (FTSE scored Tesla zero on environment).

## Problem 8. Energy-sector numericals: renewable PPA and avoided emissions 📗 ⭐⭐
A cement plant signs a PPA for a 10 MW solar farm with a 19% capacity utilisation factor. Grid factor 0.71 kg CO₂ per kWh.

**Q8.1 How much electricity does the solar farm generate and how much Scope 2 CO₂ does it avoid?**
Generation = 10 MW × 0.19 × 8,760 h = **16,644 MWh a year**. Avoided CO₂ = 16,644 × 0.71 = **11,817 t CO₂ a year** (market-based Scope 2).

**Q8.2 If the plant uses 60,000 MWh a year, what share is renewable, and what remains?**
RE share = 16,644 ÷ 60,000 = **27.7%**. Remaining grid Scope 2 = (60,000 − 16,644) × 0.71 = **30,783 t CO₂**. To reach Asian Paints' level (about 60% RE, Lecture 7) the plant would need about 36,000 MWh of RE, roughly **22 MW** of solar at the same CUF.

**Q8.3 Map the energy supply chain stages the syllabus asks about, with one sustainability KPI each.**
- **Supplies** (fuel extraction, critical minerals, equipment): methane-leak rate, % of minerals from audited sources.
- **Production / conversion** (power plants, refineries): generation efficiency (coal plant ≈ 22% in the IISc paper), g CO₂ per kWh.
- **Transmission and distribution**: T&D loss % (25.4% in the IISc paper).
- **End use**: energy intensity per unit of output, % renewable electricity.
- **Disposal**: battery and solar-panel recycling rate, decommissioning liabilities.

---

## Practice set 📗

**Q9. A 1-litre PET bottle has a footprint of 0.08 kg CO₂e and is used once. A 1-litre steel bottle has 2.4 kg CO₂e and is used 500 times (washing adds 0.002 kg per use). Compare per litre delivered over 500 uses.**
PET = 500 × 0.08 = **40 kg**. Steel = 2.4 + 500 × 0.002 = **3.4 kg**. Break-even uses: 2.4 ÷ (0.08 − 0.002) = **31 uses**.

**Q10. A 1.5-tonne AC uses 1.5 kW for 1,500 hours a year; a 5-star model uses 1.0 kW and costs ₹12,000 more. Electricity ₹8 per kWh, grid 0.71 kg/kWh. Compute payback and annual CO₂ saving.**
Energy saving = 0.5 × 1,500 = 750 kWh → ₹6,000 a year → **payback 2 years**; CO₂ saving = 750 × 0.71 = **532.5 kg a year**.

**Q11. A cradle-to-gate study of a T-shirt finds: cotton growing 2.1 kg CO₂e, spinning and weaving 1.8, dyeing 0.9, cutting and sewing 0.3. Use phase (50 washes at 0.04 kg per wash) and end of life (0.1) are excluded. What is the cradle-to-gate footprint, what is cradle-to-grave, and what is the biggest hotspot?**
Cradle-to-gate = 2.1 + 1.8 + 0.9 + 0.3 = **5.1 kg**. Cradle-to-grave = 5.1 + 50 × 0.04 + 0.1 = **7.2 kg**. The biggest single hotspot is **cotton growing (29% of cradle-to-grave)**; the use phase (2.0 kg, 28%) is almost as large, so a cradle-to-gate boundary misses a major lever (cold-water washing).

**Q12. Characterise these emissions into CO₂e (GWP: CH₄ 28, N₂O 265): 1,000 kg CO₂, 20 kg CH₄, 2 kg N₂O.**
1,000 + 20 × 28 + 2 × 265 = 1,000 + 560 + 530 = **2,090 kg CO₂e**.

**Q13. Using WTT 85% for LPG and TTW 24%, compute WTW. If a hybrid improves WTW by 41%, what is the new WTW and the energy saving?**
WTW = 0.85 × 0.24 = **20.4%**. Hybrid = 20.4 × 1.41 = **28.8%**. Energy at source falls by 1 − 20.4 ÷ 28.8 = **29%**, matching the IISc average.
