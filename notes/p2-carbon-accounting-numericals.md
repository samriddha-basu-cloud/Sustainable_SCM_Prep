# CO3 Numericals: Carbon Accounting & Scope 1, 2, 3 Emissions
This page covers **CO3: carbon accounting, the calculation of Scope 1, 2 and 3 emissions**. CO3 is one of the two **high-weightage** COs in the 40-mark end-sem paper (Lecture 11, last slide 📘), so expect the biggest numerical here. It reproduces the **exact automotive plant case (ICEV + EV in the same plant)** from the deck *"Carbon management, carbon accounting and carbon trading"* 📘, solved line by line, plus the diesel example, GWP conversion, carbon credits, and real BRSR numbers from the **Tata Motors** and **TVS Motor** reports in your course zip 📘. Practice problems built in the same style are marked 📗. Turn on **Self-test** (`T`) to hide answers.

Theory is on [LCA, Carbon Footprints & Carbon Management](ch02-lca-carbon-footprints.md).

---

## The method and the factors you must know ⭐⭐⭐
**The basic formula (carbon deck 📘):**
**Emissions = Activity data × Emission factor**, then **CO₂e = Emission of the gas × GWP**.

**The five-step carbon accounting methodology (carbon deck 📘):**
1. **Identify emission sources**, scope-wise (natural gas furnace, diesel generators, purchased electricity, logistics).
2. **Collect activity data** (litres of diesel, kWh of electricity, tonnes of steel purchased).
3. **Apply emission factors** (sources: IPCC, DEFRA, national databases). Example: 10,000 litres diesel × 2.68 kg CO₂/litre = **26,800 kg CO₂**.
4. **Convert to CO₂e** by applying GWP multipliers.
5. **Aggregate and report** (BRSR, CDP, GRI 305, CBAM filings), with MRV: Measure → Report → Verify.

**Emission factors used in the course case 📘 (memorise):**

| Fuel / energy | Emission factor |
|---|---|
| Diesel | **2.68 kg CO₂ per litre** |
| Natural gas | **1.9 kg CO₂ per Sm³** |
| LPG | **3.0 t CO₂ per tonne** |
| Indian grid electricity | **≈ 0.70 t CO₂ per MWh** (= 0.70 kg per kWh) |
| Petrol car tailpipe (case) | 120 g CO₂ per km |

**GWP (100-year) values from the deck 📘:** CO₂ = **1**; CH₄ ≈ **27–30**; N₂O ≈ **273**; HFCs **12–14,000** (the range of the family; a common refrigerant such as HFC-134a is about 1,300–1,530); PFCs **7,000–12,000**; SF₆ ≈ **25,200**; NF₃ ≈ **17,000**. These seven are the Kyoto Protocol (1997) basket.

**Scope rules (carbon deck & Lecture 10 📘):**
- **Scope 1 — Direct, "what you burn":** fuel combustion (diesel in the plant generator), company vehicles (petrol in company cars), process emissions (chemical reactions in manufacturing), fugitive emissions (refrigerant leaks).
- **Scope 2 — Energy indirect, "what you buy":** purchased grid electricity (e.g. MSEDCL power), purchased heating (hot water for buildings), purchased cooling, purchased gases (e.g. hydrogen for an industrial process — as listed in the course slide).
- **Scope 3 — Value chain, "what you influence":** purchased goods and services, fuel- and energy-related activities not in Scope 1 & 2 (mining coal, refining petrol), product use (use of vehicles and end-of-life treatment), logistics (inbound materials and outbound products), and the rest of the 15 GHG Protocol categories. **Scope 3 typically contributes 70–90% of GHG emissions** and is the most challenging to measure.

**The 15 Scope 3 categories (as listed on the case slide):** *Upstream:* 1 Purchased goods & services, 2 Capital goods, 3 Fuel & energy related, 4 Upstream transport, 5 Waste generated, 6 Business travel, 7 Employee commuting, 8 Upstream leased assets. *Downstream:* 9 Downstream transport & distribution, 10 Processing of sold products, 11 Use of sold products, 12 End-of-life treatment of sold products, 13 Downstream leased assets, 14 Franchises, 15 Investments.

**Unit traps:** 1 t = 1,000 kg; 1 MWh = 1,000 kWh; kg/kWh = t/MWh; "1.5 L km" = 1.5 lakh km = 1,50,000 km; Indian notation 12,42,636 = 1,242,636. 1 carbon credit = 1 t CO₂e.

---

## Problem 1. Automotive manufacturing — ICEV + EV in the same plant (carbon deck, slides 17–19) 📘 ⭐⭐⭐
**Context:** one plant produces **50,000 ICE cars** and **20,000 EV cars** a year.

### Part A — Scope 1 (direct emissions, example data)

| Source | Quantity | Emission factor |
|---|---|---|
| Natural gas | 500,000 Sm³ | 1.9 kg CO₂/Sm³ |
| Diesel (DG sets) | 200,000 litres | 2.68 kg CO₂/l |
| LPG | 50 tonnes | 3.0 t CO₂/t |

**Q1.1 Calculate the plant's Scope 1 emissions.**
- Natural gas: 500,000 Sm³ × 1.9 kg = 950,000 kg = **950 t CO₂**
- Diesel: 200,000 l × 2.68 kg = 536,000 kg = **536 t CO₂**
- LPG: 50 t × 3.0 t CO₂/t = **150 t CO₂**
- **Total Scope 1 = 950 + 536 + 150 = 1,636 t CO₂e**

### Part B — Scope 2 (purchased electricity)
Grid electricity for body-shop robots, paint shop, assembly lines and the EV battery line. Annual electricity = **25,000 MWh**; Indian grid factor ≈ **0.70 t CO₂/MWh**.

**Q1.2 Calculate Scope 2.**
Scope 2 = 25,000 MWh × 0.70 t CO₂/MWh = **17,500 t CO₂e**.

### Part C — Scope 3 (value-chain emissions)
*"This is where EV vs ICEV diverge strongly. We take only key categories (not all 15)."*

| No. | Category | ICEV data | EV data |
|---|---|---|---|
| 1 | Purchased materials | Steel, aluminium, plastics, powertrain: ≈ 6 t CO₂e per vehicle | Body + motor + electronics + lithium battery (~60 kWh): ≈ 10 t CO₂e per vehicle |
| 4 | Upstream transport | Parts by truck & ship: total 15,000 t CO₂e | Same: 15,000 t CO₂e |
| 6 | Business travel | Flights + hotels: total 500 t CO₂e (printed "5,00") | Same: 500 t CO₂e |
| 9 | Downstream distribution | Shipping cars to dealers: total 8,000 t CO₂e | Same: 8,000 t CO₂e |
| 11 | Use phase | Lifetime distance 1.5 lakh km, 120 g CO₂/km | Electricity 0.15 kWh/km, lifetime 22,500 kWh, grid 0.70 kg CO₂/kWh |

**Q1.3 Calculate Scope 3 purchased materials (Category 1).**
- ICEV: 50,000 × 6 t = **300,000 t CO₂e**
- EV: 20,000 × 10 t = **200,000 t CO₂e**

**Q1.4 Calculate the use-phase emissions per vehicle and for the fleet (Category 11).**
- *ICEV per vehicle:* 1,50,000 km × 120 g/km = 18,000,000 g = **18 t CO₂e**. Fleet = 50,000 × 18 = **900,000 t CO₂e**.
- *EV per vehicle:* electricity = 1,50,000 km × 0.15 kWh/km = **22,500 kWh**; emissions = 22,500 × 0.70 kg = 15,750 kg = **15.75 t CO₂e**. Fleet = 20,000 × 15.75 = **315,000 t CO₂e**.

**Q1.5 Logistics and travel (Categories 4, 6, 9).**
15,000 + 500 + 8,000 = **23,500 t CO₂e**. The slide books this once, against the ICEV line ("same" for EV), so it is not added twice.

**Q1.6 Prepare the summary table and the plant total.**

| Scope | ICEV (t CO₂e) | EV (t CO₂e) |
|---|---|---|
| Scope 1 | 1,636 | Included (shared plant) |
| Scope 2 | 17,500 | Included |
| Scope 3 — Materials | 300,000 | 200,000 |
| Scope 3 — Logistics + travel | 23,500 | Same (counted once) |
| Scope 3 — Use phase | 900,000 | 315,000 |
| **Total** | **12,42,636** | **5,15,000** |

ICEV total = 1,636 + 17,500 + 300,000 + 23,500 + 900,000 = **12,42,636 t**. EV total = 200,000 + 315,000 = **5,15,000 t**.
**Plant total = 12,42,636 + 5,15,000 = 17,57,636 t CO₂e.**

**Q1.7 What share of the plant footprint is Scope 1 + 2 versus Scope 3? What does this mean for strategy?**
Scope 1 + 2 = 1,636 + 17,500 = 19,136 t → 19,136 ÷ 17,57,636 = **1.09%**. Scope 3 = 17,38,500 t → **98.9%**. (The slide's note: *Scope 1 + 2 < 5%, Scope 3 > 95%.*) Use phase alone = 12,15,000 t = **69.1%**; purchased materials = 5,00,000 t = **28.4%**.
**Implication:** even a 100% renewable, zero-fuel factory would cut the footprint by only about 1%. That is why OEMs such as **Toyota and Tesla focus on supplier decarbonisation, renewable energy, battery recycling and green logistics** (slide note), and why the product's use phase (efficiency, electrification, grid mix) dominates.

**Q1.8 Compare an ICE car and an EV per vehicle. Interpret the slide's "vehicle type" table.**

| Vehicle type | Manufacturing phase | Use phase | Total (life cycle) |
|---|---|---|---|
| ICE | ~7 t | ~18 t | **~25 t** |
| EV (India grid) | ~12 t | ~16 t | **~28 t** |
| EV (RE grid) | ~10 t | ~3 t | **~13 t** |

The slide's four lessons: (1) Scope 1 + 2 < 5% and Scope 3 > 95%; (2) **EV is high in manufacturing because of battery materials**; (3) **ICEV is high in life usage**; (4) **EV benefit depends on grid cleanliness**. On today's coal-heavy Indian grid (0.70 kg/kWh) the EV's lifetime footprint (~28 t) can even exceed the ICE car's (~25 t); on a renewable grid it falls to about half (~13 t).

**Q1.9 At what grid emission factor would the EV and the ICE car have the same life-cycle footprint?** ⭐⭐
EV total = 12 t (manufacturing) + 22,500 kWh × g; ICE = 25 t. Set 12 + 22.5 × g = 25 (g in kg/kWh, because 22,500 kWh × g kg = 22.5 g t). g = 13 ÷ 22.5 = **0.578 kg CO₂/kWh**. Below about 0.58 kg/kWh, the EV is better over its life. India's grid has to decarbonise by about 17% from 0.70 for the EV in this case to break even. (Using the case's 10 t materials figure instead: 10 + 22.5g = 25 → g = 0.667 kg/kWh.)

**Q1.10 Per-vehicle intensity: which product line is more carbon-intensive per car?**
ICEV: 12,42,636 ÷ 50,000 = **24.85 t per car**. EV: 5,15,000 ÷ 20,000 = **25.75 t per car** (no plant or logistics share allocated). If you allocate the shared Scope 1 + 2 by volume (20/70 of 19,136 = 5,467 t) and logistics (20/70 of 23,500 = 6,714 t) to the EV line, EV = (5,15,000 + 5,467 + 6,714) ÷ 20,000 = **26.36 t per car**, and the ICEV line falls to (12,42,636 − 5,467 − 6,714) ÷ 50,000 = **24.61 t**. Allocation choices change the answer, which is why the course lists "allocation issues" as an LCA limitation.

---

## Problem 2. The deck's diesel example and GWP conversion 📘 ⭐⭐
**Q2.1 A plant uses 10,000 litres of diesel. Emission factor 2.68 kg CO₂/l. Emissions?**
10,000 × 2.68 = **26,800 kg = 26.8 t CO₂** (Scope 1 if burnt in the company's own DG set or vehicles; Scope 3 if burnt by a hired transporter).

**Q2.2 Convert to CO₂e: 10 t CH₄ from a biogas leak, 2 t N₂O from fertiliser use, 0.1 t SF₆ leaking from switchgear. Use GWPs CH₄ = 28, N₂O = 273, SF₆ = 25,200.**
CH₄: 10 × 28 = **280 t CO₂e** · N₂O: 2 × 273 = **546 t CO₂e** · SF₆: 0.1 × 25,200 = **2,520 t CO₂e** · Total = **3,346 t CO₂e**. Notice how 100 kg of SF₆ outweighs 10 t of methane: tiny leaks of high-GWP gases matter, which is why fugitive emissions are a Scope 1 category.

**Q2.3 Why convert everything to CO₂e?**
Different gases trap different amounts of heat for different lengths of time. Converting with GWP (100-year) puts them on one comparable scale so that they can be added, targeted and traded (1 credit = 1 t CO₂e).

---

## Problem 3. Full Scope 1-2-3 inventory for a mid-size manufacturer 📗 ⭐⭐⭐
*(Practice data in the style of the course case. Factors from the course where available; others are stated assumptions.)*
An auto-component plant in Pune produces **20,000 units** a year and records:
- Diesel in DG sets and forklifts: 50,000 litres (2.68 kg CO₂/l)
- Natural gas in heat-treatment furnaces: 200,000 Sm³ (1.9 kg CO₂/Sm³)
- LPG in the canteen and paint oven: 20 t (3.0 t CO₂/t)
- Refrigerant top-up (HFC-134a) of 50 kg in the AC system; **assume GWP 1,430**
- Grid electricity: 4,000 MWh (0.70 t CO₂/MWh)
- Purchased steel: 5,000 t; **assume 2.0 t CO₂e per t steel**
- Inbound freight by hired trucks: 2,000,000 tonne-km; **assume 0.10 kg CO₂e per t-km**
- Business travel 300 t CO₂e; employee commuting by contracted buses 150 t CO₂e; waste sent to landfill 50 t CO₂e (given)

**Q3.1 Classify each source by scope.**
Scope 1: diesel (own DG sets/forklifts), natural gas, LPG, refrigerant leak (fugitive). Scope 2: grid electricity. Scope 3: purchased steel (Cat. 1), hired inbound trucks (Cat. 4), business travel (Cat. 6), employee commuting (Cat. 7), waste (Cat. 5).

**Q3.2 Calculate each scope and the total.**

| Source | Calculation | t CO₂e | Scope |
|---|---|---|---|
| Diesel | 50,000 × 2.68 ÷ 1,000 | 134.0 | 1 |
| Natural gas | 200,000 × 1.9 ÷ 1,000 | 380.0 | 1 |
| LPG | 20 × 3.0 | 60.0 | 1 |
| HFC-134a leak | 0.05 t × 1,430 | 71.5 | 1 |
| **Scope 1** | | **645.5** | |
| Grid electricity | 4,000 × 0.70 | **2,800.0** | **2** |
| Purchased steel | 5,000 × 2.0 | 10,000.0 | 3 |
| Inbound freight | 2,000,000 × 0.10 ÷ 1,000 | 200.0 | 3 |
| Business travel | given | 300.0 | 3 |
| Employee commuting | given | 150.0 | 3 |
| Waste | given | 50.0 | 3 |
| **Scope 3** | | **10,700.0** | |
| **Grand total** | | **14,145.5** | |

**Q3.3 Compute shares and intensity.**
Scope 1 = 645.5 ÷ 14,145.5 = **4.6%**; Scope 2 = **19.8%**; Scope 3 = **75.6%** (inside the course's 70–90% range). Scope 1 + 2 intensity = 3,445.5 ÷ 20,000 = **0.172 t CO₂e per unit**; total intensity = **0.707 t per unit**. Steel alone is 70.7% of the footprint, so the top lever is **green/low-carbon steel or higher recycled content**, a procurement decision.

**Q3.4 The plant signs a solar PPA covering 40% of its electricity. New Scope 2 (market-based) and total reduction?**
Grid share = 60% × 4,000 = 2,400 MWh → Scope 2 = 2,400 × 0.70 = **1,680 t**. Reduction = 2,800 − 1,680 = **1,120 t**, i.e. 32.5% of Scope 1 + 2 but only **7.9% of the total footprint**. Location-based Scope 2 (grid average) stays at 2,800 t; market-based reflects the contract. Tata Motors reports its Scope 2 market-based, after renewable certificates (iRECs).

**Q3.5 Rank three projects by t CO₂e saved: (a) fix refrigerant leaks; (b) switch the furnace from natural gas to electricity bought from a renewable PPA; (c) source 50% of steel from a supplier with 1.2 t CO₂e/t.**
(a) 71.5 t. (b) Removes 380 t of Scope 1 (assume the renewable electricity is zero-emission under market-based accounting) → **380 t**. (c) 2,500 t × (2.0 − 1.2) = **2,000 t**. Rank: **c > b > a**. Supplier decarbonisation beats everything inside the fence, the same lesson as Problem 1.

---

## Problem 4. Real BRSR numbers — TVS Motor Company, FY 2023-24 📘 ⭐⭐
From the TVS Motor BRSR in your course zip (Principle 6):

| Parameter | FY 2023-24 | FY 2022-23 |
|---|---|---|
| Total Scope 1 emissions | 22,693.34 t CO₂e | 19,046 t CO₂e |
| Total Scope 2 emissions | 4,437.47 t CO₂e | 9,584.32 t CO₂e |
| Total Scope 3 emissions (in progress) | 2,27,00,763.36 t CO₂e | — |
| Electricity from renewable sources (A) | 3,06,833.17 GJ | 2,96,430.00 GJ |
| Electricity from non-renewable sources (D) | 22,499.84 GJ | 40,913.92 GJ |
| Fuel from non-renewable sources (E) | 2,99,342.59 GJ | 2,90,369.94 GJ |
| Total energy consumed | 6,28,675.60 GJ | 6,27,713.86 GJ |

**Q4.1 Compute Scope 1 + 2 for both years and the change.**
FY24: 22,693.34 + 4,437.47 = **27,130.81 t**. FY23: 19,046 + 9,584.32 = **28,630.32 t**. Change = −1,499.51 t = **−5.2%**. Scope 2 fell 53.7% (more renewable power) while Scope 1 rose 19.1% (TVS notes the boundary was widened to include the corporate office, test tracks and the Institute of Quality and Leadership, and that refrigerants and ODS are included in Scope 1).

**Q4.2 What share of TVS's electricity is renewable? What share of total energy?**
Renewable electricity share = 3,06,833.17 ÷ (3,06,833.17 + 22,499.84) = 3,06,833.17 ÷ 3,29,333.01 = **93.2%** (the report's "93% of our energy requirements met through renewable energy" refers to electricity). Share of *total energy* = 3,06,833.17 ÷ 6,28,675.60 = **48.8%**, because fuel (2,99,342.59 GJ) is still 100% fossil. Next lever: electrify fuel-based processes (paint ovens, heat treatment) or switch to biofuels.

**Q4.3 What share of TVS's total footprint is Scope 3?**
2,27,00,763.36 ÷ (2,27,00,763.36 + 27,130.81) = **99.88%**. Scope 3 per vehicle sold is reported as **5.41 t CO₂e**, versus Scope 1 + 2 per vehicle of about **0.01 t**. The two-wheeler's use phase and purchased parts dominate.

---

## Problem 5. Real BRSR numbers — Tata Motors Ltd (CV business, TML), FY 2024-25 📘 ⭐⭐
From the Tata Motors integrated report BRSR (assured by KPMG):

| Parameter (TML) | FY 25 | FY 24 (restated) |
|---|---|---|
| Scope 1 | 43,754 t CO₂ | 48,736 t CO₂ |
| Scope 2 (market-based, after iRECs) | 1,31,407 t CO₂ | 1,72,409 t CO₂ |
| Scope 1 + 2 intensity | 0.462 t CO₂ per vehicle produced | 0.552 |
| Scope 3 Cat. 1 Purchased goods & services (spend-based) | 52,28,249 | 61,09,148 |
| Scope 3 Cat. 11 Use of sold products | 13,95,71,557 | 15,86,21,101 |
| Total Scope 3 | 14,49,44,801 | 16,48,85,353 |

**Q5.1 Compute TML's Scope 1 + 2 and its % reduction.**
FY25: 43,754 + 1,31,407 = **1,75,161 t**. FY24: 48,736 + 1,72,409 = **2,21,145 t**. Reduction = 45,984 t = **20.8%**.

**Q5.2 Estimate the number of vehicles produced in FY25 from the intensity.**
Vehicles ≈ 1,75,161 ÷ 0.462 = **≈ 3,79,000 vehicles**.

**Q5.3 What share of Scope 3 is "use of sold products"? What does it tell you?**
13,95,71,557 ÷ 14,49,44,801 = **96.3%**; purchased goods = 3.6%. Scope 3 is about **827 times** Scope 1 + 2 (14,49,44,801 ÷ 1,75,161). For a truck maker, the diesel its customers burn over the trucks' life is the footprint. Strategic levers: EV/CNG/LNG/hydrogen trucks, fuel efficiency, telematics for eco-driving, and the Re.Wi.Re vehicle-scrapping network (Lecture 11). This mirrors the Hindustan Zinc–GreenLine LNG/EV truck deal in Lecture 1.

**Q5.4 TML's Cat. 1 is "spend-based". What does that mean and what is its weakness?**
Spend-based Scope 3 multiplies ₹ spent per category by an average emission factor per ₹. It is quick but cannot reward a supplier that actually decarbonises (spend stays the same, so the estimate stays the same). Better: supplier-specific (primary) data or average-data (t of steel × factor), moving towards product carbon footprints from suppliers.

---

## Problem 6. Carbon credits — how much is a project worth? (carbon deck, slide 25) 📘 ⭐⭐
**1 carbon credit = 1 t CO₂e reduced, avoided or removed.**

| Project | Credits generated | Potential financial return |
|---|---|---|
| 50 kW solar farm | Avoided emissions: 50–55 per year | ₹45–60 K at ₹850–1,100 per credit |
| 50 kW wind farm | Avoided emissions: 50–80 per year (depends on wind) | ₹45–90 K at ₹850–1,100 per credit |
| 50 acres afforestation | Removal: 40–100 per year, at 0.2–0.8 t CO₂ per acre | ₹32–300 K at ₹800–3,000 per credit |
| 50 t methane capture plant | Emission reduction: about 1,250 per year | ~$25–30 K at $20 per credit ≈ ₹23–28 lakh |
| 50 kW biomass plant | Avoided emissions: 200–500 per year | ₹80–625 K at ₹400–1,250 per credit |

**Q6.1 Verify the solar farm's revenue range.**
Low: 50 × ₹850 = ₹42,500; high: 55 × ₹1,100 = ₹60,500 → about **₹45–60 thousand a year** (the slide rounds the low end up).

**Q6.2 Why does the methane capture plant earn so much more than the solar farm?**
Methane has a GWP of about 27–30, so capturing 50 t of CH₄ avoids ~50 × 25 ≈ 1,250 t CO₂e (the slide's figure is consistent with a GWP of 25). 1,250 credits × $20 = **$25,000** (≈ ₹23 lakh at ~₹92/$). A 50 kW solar plant avoids only ~50 t because a small plant generates ~70 MWh a year, and 70 MWh × 0.70 t/MWh ≈ 49 t.

**Q6.3 Check the biomass revenue range.**
Low: 200 × ₹400 = **₹80,000**; high: 500 × ₹1,250 = **₹6,25,000** → ₹80–625 K, as on the slide.

**Q6.4 Check the afforestation numbers. Are they consistent?**
At 0.2–0.8 t CO₂ per acre, 50 acres removes only 10–40 t a year. The slide's "40–100 credits a year" implies 0.8–2.0 t per acre, so the per-acre range and the credit range do not quite match; young plantations remove little and mature ones more. Revenue at the slide's figures: 40 × ₹800 = ₹32,000 to 100 × ₹3,000 = ₹3,00,000 → **₹32–300 K**, as printed. Removal credits command higher prices (₹800–3,000) because they are permanent removals, if they are verified.

**Q6.5 Name the carbon market structures from the deck.**
Credit life cycle: Project developer → Validation → Verification → Carbon registry → Carbon credit issued (1 credit = 1 t CO₂e) → Buyer purchases credit. Registries: **Verra (VCS), Gold Standard, American Carbon Registry, Climate Action Reserve**. **Compliance market** (mandatory: EU ETS, national schemes) vs **voluntary market** (corporate commitments, net-zero pledges). **India's CCTS** (Carbon Credit Trading Scheme, developed by BEE and the Ministry of Power, operative from 2025): India → Industry → Carbon reduction → Credits → Global market.

---

## Problem 7. Net-zero arithmetic and the hierarchy 📘 + 📗 ⭐⭐
**Definitions (carbon deck 📘):** Carbon neutral = emissions balanced through offsets. **Net zero = reduce emissions deeply (90–95%) and neutralise residual emissions.** Carbon zero = near-zero emissions across operations and value chain. Climate positive = removes more carbon than emitted. **Net-zero hierarchy:** Measure (Scope 1, 2, 3, CO₂e) → Reduce (decarbonisation, energy efficiency, circularity, nature-based solutions) → RE transition (solar, wind, hydro) → Sustainable supply chain (EV fleets, circularity, biodegradable packaging) → Offset unavoidable emissions (afforestation, CCUS). **"Reduction first, offset later."**

**Q7.1 A company's baseline is 1,00,000 t CO₂e. To call itself net zero, how much must it reduce and how much may it neutralise?**
Reduce by 90–95% → residual 5,000–10,000 t. Only that residual may be neutralised (preferably with **removals**: afforestation, CCUS). A firm that offsets all 1,00,000 t without reducing is "carbon neutral", not net zero.

**Q7.2 The same company plans a linear path from 2026 to 90% reduction by 2050. What is the annual reduction?**
90,000 t over 24 years = **3,750 t a year** (3.75% of the baseline). On the course's decarbonisation pathway: 2026 measure, 2028 energy efficiency, 2030 renewable electricity, 2035 green supply chain, 2040 low-carbon products, 2050 net zero.

**Q7.3 Carbon-neutral claim check: a firm emits 20,000 t, buys 20,000 avoidance credits from a solar project, and advertises its product as "carbon neutral". Comment.**
Technically "carbon neutral" (balanced through offsets), but it may be **greenwashing** if the claim implies reduced emissions, if the credits are low quality (non-additional, unverified), or if Scope 3 is excluded. A credible claim states the claim, metric, boundary, methodology, baseline, target and evidence (the Lecture 10 "good reporting" list), with MRV and third-party assurance (e.g. Bureau Veritas, TÜV, KBS).

---

## Practice set 📗

**Q8. Classify into Scope 1, 2 or 3: (a) electricity bought from MSEDCL; (b) diesel in the company's own trucks; (c) diesel in a 3PL's trucks carrying your goods; (d) CO₂ released when limestone is calcined in your kiln; (e) R-410A leaking from your office AC; (f) steam bought from a neighbouring plant; (g) customers driving the cars you sold; (h) employees flying to a conference; (i) hydrogen bought for your hydrogenation process; (j) emissions from mining the coal burnt at your power supplier's plant.**
(a) 2 · (b) 1 · (c) 3 (Cat. 4 or 9) · (d) 1 (process emissions) · (e) 1 (fugitive) · (f) 2 (purchased heat) · (g) 3 (Cat. 11) · (h) 3 (Cat. 6) · (i) 2 as the course slide lists purchased gases under Scope 2 (under the GHG Protocol, the production emissions of purchased hydrogen sit in Scope 3 Cat. 1 or 3; mention both if asked) · (j) 3 (Cat. 3, fuel- and energy-related activities).

**Q9. A warehouse uses 1,20,000 kWh of grid electricity a month. It installs rooftop solar producing 40,000 kWh a month (Myntra, in Lecture 8, is the course example). Monthly Scope 2 before and after? Annual saving in t CO₂e?**
Before: 1,20,000 × 0.70 kg = 84,000 kg = **84 t/month**. After: 80,000 × 0.70 = **56 t/month**. Saving 28 t/month = **336 t/year**. The KPI to report is energy (or kg CO₂e) per unit handled (the Lecture 8 green-warehousing KPI).

**Q10. A fleet of 40 company-owned diesel trucks each runs 80,000 km a year at 4 km per litre. Compute Scope 1. If they are replaced by LNG trucks emitting 15% less per km, what is the saving?**
Diesel = 40 × 80,000 ÷ 4 = 8,00,000 l → 8,00,000 × 2.68 = 21,44,000 kg = **2,144 t CO₂**. 15% saving = **321.6 t** a year (the Hindustan Zinc–GreenLine idea).

**Q11. An exporter of steel to the EU emits 2.3 t CO₂ per t of steel; the EU benchmark is 1.4 t. Assuming a CBAM price of €80/t CO₂ applied to the excess, what is the CBAM cost per tonne of steel and for 10,000 t?**
Excess = 0.9 t CO₂/t steel → 0.9 × €80 = **€72 per t of steel**; for 10,000 t = **€7,20,000**. (Simplified; actual CBAM uses embedded emissions, free-allocation phase-out and any carbon price paid at home.) Message from the deck: carbon is becoming a **financial variable**, and MRV-quality data are needed for CBAM filings.

**Q12. Why is it said that "a company may reduce Scope 1 substantially while its total supply-chain footprint continues increasing" (Lecture 10)? Give a numerical illustration.**
If a firm outsources its own fleet to a 3PL, its Scope 1 falls, but the same diesel now appears in its Scope 3 (Cat. 4/9). Example: 2,144 t moves from Scope 1 to Scope 3, and if the 3PL runs emptier trucks, the total rises. Therefore **carbon accounting must follow the value chain.**

**Q13. Carbon accounting vs financial accounting: fill the table.**
Measure: currency vs **CO₂e**; Record: ledger vs **emission inventory**; Source: cost centres vs **emission sources**; Assessment: audit vs **verification**; Results: profitability vs **carbon intensity**. Emerging concept: the **carbon ledger**; new roles: carbon accountants, ESG controllers.
