# Supply Chain in the Energy Sector: Supplies, Production, End Use, Disposal
Syllabus topic 9 📘. The course material for this topic is the set of readings in the zip: the two **IISc papers** on the life-cycle energy and GHG emissions of automotive fuels in India (Part 1 Tank-to-Wheel, Part 2 Well-to-Wheel), **Rietmann, Hügler & Lieven (2020)** on forecasting EV sales and worldwide CO₂, the **Tesla battery supply chain** case (William Davidson Institute, 2022), plus the energy content of Lectures 1, 2, 7 and 11 (Hindustan Zinc, critical minerals, green hydrogen) and the carbon deck. The syllabus asks you to follow energy through four stages: **supplies → production → end use → disposal**. Numericals (WTW efficiency, EV vs ICE, logistic EV forecast, battery economics, solar PPA): [LCA & Energy Numericals](p5-lca-energy-numericals.md).

---

## 1. Why the energy sector is a supply-chain problem ⭐⭐⭐
- Energy is both a **product** (fuel, electricity, batteries) and an **input** to every other supply chain (Scope 1 fuels and Scope 2 electricity of every firm).
- Energy supply chains are long, capital-intensive and global: crude oil, LNG, coal, critical minerals and solar modules cross many borders, so geopolitics, price volatility and human rights are built into them.
- The energy transition moves the sustainability problem *upstream*: instead of burning fuel at the point of use, we now depend on **minerals** (lithium, nickel, cobalt, copper, graphite, rare earths) and on **clean electricity generation**. Lecture 11 calls this **the critical-minerals paradox**.
- Every stage has its own hotspot: extraction (land, water, biodiversity, labour), conversion (efficiency, emissions), transmission (losses), end use (efficiency, behaviour) and disposal (hazardous waste, recovery).

| Stage | Fossil-energy chain | Clean-energy chain | Key sustainability issues |
|---|---|---|---|
| **Supplies** | Oil & gas exploration, coal mining, crude imports | Lithium, nickel, cobalt, graphite, copper, rare earths, polysilicon | Methane leaks, biodiversity, water, conflict minerals, child labour, import dependence |
| **Production / conversion** | Refining, gas processing, thermal power | Solar/wind generation, battery-cell manufacturing, green hydrogen | Conversion efficiency, CO₂ intensity, local pollution |
| **Distribution** | Pipelines, tankers, rail, retail outlets | Transmission & distribution grids, charging networks | T&D losses, grid stability |
| **End use** | ICE vehicles, boilers, kilns | EVs, heat pumps, electrified industry | Tank-to-Wheel efficiency, behaviour, rebound |
| **Disposal / end-of-life** | Decommissioning wells and plants, fly ash | Battery recycling and second life, solar-panel and turbine-blade waste | Hazardous waste, recovery rates, EPR |

---

## 2. Supplies: fuels and critical minerals ⭐⭐⭐
### Fossil supplies (IISc WTW paper) 📘
- India imported **81.27%** of the crude it refined in 2010–11 (18.73% domestic); the overall weighted crude recovery efficiency was about 98.6% and refining efficiency differs by product.
- Natural gas: about 23% imported (2010–11); recovery and processing efficiencies of about 94–97%.
- **Well-to-Tank (WTT) efficiency** of petroleum fuels is **75–85%**; **LPG is highest at 85%**.
- Methane (CH₄) leakage in gas supply chains is a major hidden GHG source (GWP ≈ 28–30).

### The critical-minerals paradox (Lecture 11) 📘 ⭐⭐⭐
The green transition requires **more EVs + batteries and more solar + wind + grid**, which creates **high demand for lithium, copper, nickel, cobalt, graphite and rare earths**, which in turn creates **water, biodiversity and emission impacts plus social and geopolitical risks**. The IEA's **2025 Critical Minerals Outlook**: **lithium demand rose almost 30% in 2024**, and **7% of global copper supply was exposed to flood or drought disruption risk in 2024**.

### Battery-mineral hotspots (Tesla case) 📘 ⭐⭐⭐
| Mineral | Supply concentration | Sustainability issue |
|---|---|---|
| **Cobalt** (about 6% of NMC cell mass, the highest-cost input per tonne) | About **65%** from the **Democratic Republic of Congo** | Artisanal mines linked to child and forced labour and to conflict financing — *"the blood diamond of batteries"*; a 2019 lawsuit named Apple, Google, Microsoft and Tesla. Cobalt-free **LFP** chemistry is cheaper but has lower energy density and range. |
| **Lithium** | **Lithium Triangle** (Chile, Bolivia, Argentina) and Australia | About **500,000 gallons of water per tonne** of lithium extracted from brine; linked indirectly to the 2019 Bolivian crisis |
| **Nickel** | Indonesia, Philippines | In 2017 the Philippines closed **23 mines** on environmental grounds, causing panic because it supplied about **20%** of nickel |
| **Cells** | **CATL** controlled about **30%** of the global EV-battery market | Concentration risk; Tesla relies on Panasonic, CATL and LG |

### Geopolitics of energy supplies 📘 ⭐⭐
- Lecture 11's polycrisis lists **critical-resource constraints** (lithium, copper, nickel, cobalt, rare earths) and **geopolitical fragmentation** (trade restrictions, sanctions, protectionism, regionalisation).
- **McKinsey (2026), "Geopolitics and the geometry of global trade"** (in the zip): US–China direct trade fell by about 30%; trade is re-routing through "connector" economies; AI-related goods drive about one-third of trade growth; China is becoming the *"factory to the factories"* (exporting intermediate goods and machinery). For energy supply chains this means diversification ("China + 1"), friend-shoring and strategic stockpiles.
- Indian responses: production-linked incentives (PLI) for advanced-chemistry cells and solar modules, **KABIL** (Khanij Bidesh India Ltd) acquiring lithium assets abroad, the National Critical Mineral Mission (2025).

**Sourcing strategies for energy supplies**: supplier due diligence and traceability (OECD Due Diligence Guidance, Responsible Minerals Initiative), chemistry substitution (LFP, sodium-ion), long-term offtake contracts, recycling as a "secondary mine", regional diversification.

---

## 3. Production and conversion ⭐⭐⭐
### Electricity generation in India (IISc paper) 📘
- **69.9%** of electricity came from coal (12.1% natural gas in the data used); typical coal-plant efficiency in the paper's calculation was about **22%** (from 0.72 kg CO₂/kWh and coal's calorific value of 22,732 kJ/kg).
- **T&D losses of 25.4%** (since reduced to under 20% nationally).
- Result: **electricity WTT efficiency ≈ 20%**, the lowest of all fuels — *the losses are upstream*.
- Today non-fossil sources are about half of India's installed capacity (the carbon deck cites about 54%), but coal still supplies most of the *energy* generated, and the grid factor is about 0.71–0.79 kg CO₂/kWh.

### Hydrogen
- Hydrogen from natural-gas reforming has a production efficiency of about **70%**, giving WTT of only about **48%** (IISc), so fuel-cell vehicles were the least efficient on WTW.
- **Green hydrogen** (electrolysis with renewable power) is the Lecture 7 "future manufacturing" lever for **high-temperature processes and hard-to-abate sectors** (steel, cement, fertiliser, refining). India's National Green Hydrogen Mission targets 5 Mt a year by 2030.

### Renewable generation and corporate procurement ⭐⭐
Companies decarbonise Scope 2 through rooftop solar, open-access **PPAs** (power purchase agreements), green tariffs and RECs. Course examples: Asian Paints about 60% RE (FY25), ITC 50% RE, M&M 37% RE, Dalmia Cement targeting 100% RE by 2030, Apple's supply chain with **17.8 GW** of renewable electricity online (2024). ([PPA numerical](p5-lca-energy-numericals.md))

### Battery manufacturing
Battery cells are the most carbon-intensive part of an EV (the course's automotive case gives about 10 t CO₂e per EV including a 60 kWh battery vs about 6 t for an ICE car's materials). Gigafactories powered by renewable electricity (Tesla Gigafactory Nevada with Panasonic, planned for 500,000 packs a year) cut this embedded carbon.

---

## 4. End use: transport energy in India ⭐⭐⭐
### Context (IISc papers) 📘
Transport was India's second-largest energy-consuming sector (about **17.5%** of total energy in 2010–11 in Part 2; Part 1 puts transport at about **22% of energy and 8% of GHG emissions**), with **road transport about 87%** of transport's share and **124 of the 135 kg of per-capita transport CO₂** (2011). Passenger vehicles were about 13% of registered motor vehicles.

### Tank-to-Wheel (TTW) — Part 1 📘 ⭐⭐
- 28 vehicle configurations analysed (fuels × powertrains).
- TTW efficiency: **gasoline/LPG 15–27%**, **diesel 25–32%**; hybrids gain through regenerative braking (about 19–23% of energy recovered).
- **Split hybrids** reduce fuel use and CO₂ by about **20–40%**.

### Well-to-Wheel (WTW) — Part 2 📘 ⭐⭐⭐
- **WTW = WTT × TTW.** For liquid fuels about 75–84% of WTW energy is used in the TTW stage, while for electricity about 83% of WTW energy is consumed upstream.
- **Diesel split hybrid = most efficient** configuration overall.
- **BEV on the Indian grid ≈ gasoline car** on WTW efficiency, because of coal power and T&D losses.
- **Hydrogen fuel-cell vehicles = least efficient** (WTT about 48%).
- **Hybridisation raises WTW efficiency by an average of 41% and cuts WTW energy by 29%.**
- CO₂: 72–80% of WTW CO₂ from liquid fuels is emitted in the TTW stage; for BEVs almost all is at the power plant.

### EV adoption and global CO₂ (Rietmann et al., 2020) 📘 ⭐⭐⭐
- Model: logistic diffusion I(t) = L ÷ [1 + (L/I(0) − 1)·e^(−k·L·t)], fitted country by country.
- Findings: EVs reach about **30% of the fleet by 2032** and **42.5% by 2035**, yet **global passenger-car CO₂ still rises until about 2035** because the fleet grows and grids are still fossil-heavy.
- India-specific: ICE 0.135 kg CO₂/km; grid **0.791 kg CO₂/kWh**; 20,800 km/yr; India's car CO₂ rises about **+129.5% (2018–2035)**. EVs only cut emissions as the grid decarbonises.
- Charging energy for 439 million EVs (17,000 km/yr × 0.185 kWh/km) ≈ **1,381 TWh/yr** — the power-sector supply chain must expand with the fleet.

### Logistics end use: Hindustan Zinc and GreenLine (Lecture 1–2) 📘
Hindustan Zinc's ₹400 crore deal with GreenLine Mobility to move ore and metal with **LNG and EV trucks** is the course's "reduction-based" energy case. Trade-offs: cost, emissions, refuelling/charging infrastructure, scalability.

**Supply-chain lessons from end use**: compare fuels on WTW not TTW; pair electrification with renewable power; hybrids and efficiency are cheap early wins; demand-side measures (fewer km, higher load factor) matter as much as fuel switching.

---

## 5. Disposal: end-of-life energy assets ⭐⭐⭐
### The EV-battery wave (Tesla case) 📘
- By **2030, 1.2 million tonnes** of EV batteries a year will need disposal.
- Only about **5%** of Li-ion batteries are recycled globally; **95%** reach municipal waste.
- Tesla packs: up to **10,000** replacements by 2025 and **50,000 a year by 2030**.
- Tesla's 2020 impact report claimed *"none of our scrapped lithium-ion batteries go to landfills and 100 percent are recycled"* — the case treats this as positive sentiment rather than a plan (a greenwashing risk).

### End-of-life options (value-retention order)
1. **Second life** (stationary storage): adaptation costs **$3,500** (direct reuse), **$6,700** (module level), **$8,000** (cell level); Tesla remanufactures packs at module level; replacing 5–30% of cells can restore 95% state of health.
2. **Recycling**: economic return about **$5,600 per battery after 2025**.
   - **Pyrometallurgy**: shred and smelt at high temperature; tolerant of mixed designs but energy-intensive; lithium is often lost.
   - **Hydrometallurgy**: leach in acids; recovers lithium, cobalt, nickel and copper; chemical handling risks.
   - **Direct recycling** (US DOE **ReCell** Center): keeps the cathode structure intact, minimal processing.
   - **ReLiB** (UK): robotic disassembly and better separation.
   - Best case: recover about half of critical materials and cut up to **70%** of GHG.
3. **Disposal**: hazardous; the last resort.

### Waste-management frameworks (Tesla case) 📘 ⭐⭐
- **US EPA hierarchy** (most to least desirable): source reduction & reuse → recycling/composting → energy recovery → treatment/disposal.
- **EU Waste Framework Directive** (five levels): prevention → preparing for reuse → recycling → recovery → disposal, with the **"polluter pays" principle** and **Extended Producer Responsibility (EPR)**. The EU Battery Regulation (2023) adds recycled-content targets and a **battery passport** (from 2027).
- **India**: Battery Waste Management Rules 2022 (EPR for producers, recovery targets), E-Waste (Management) Rules 2022 (solar panels included), Vehicle Scrappage Policy (Mahindra CERO, Tata Re.Wi.Re).

### Recycling partners (Tesla case) 📘
- **Redwood Materials** (founded 2017 by Tesla's ex-CTO **JB Straubel**; Carson City, Nevada; about **95% recovery**; valued at **$3.78 billion**, not yet profitable).
- **Li-Cycle** (founded 2016; Kingston, Ontario plant for **5,000 t/yr**; **>95% recovery** with no landfill; provides logistics; raised **$1.6 billion**).

### Tesla's decision: build, buy or partner? 📘 ⭐⭐⭐
| Option | Pros | Cons |
|---|---|---|
| **Build** internal recycling | Control, material security, closed loop with Gigafactories, ESG credit | Capex, low early volumes, new competence |
| **Buy** a start-up | Speed, technology, talent | Acquisition price, integration risk, immature technology |
| **Partner** with Redwood / Li-Cycle | Low capex, scale through pooled volumes, flexibility | Less control; risk that the market cannot meet Tesla's needs in time |
**Model answer**: partner now (volumes too small; recyclers need pooled scale), with equity or long-term offtake agreements that guarantee recovered cobalt, nickel and lithium back to Tesla; build in-house capability as packs reach 50,000 a year; design packs for disassembly. This improves ESG performance on both the "E" (recovery, lower Scope 3) and the "S" (less conflict-mineral demand).

### ESG ratings divergence (Tesla case) 📘 ⭐⭐
ESG assets reached **$40.5 trillion** in 2020. Raters disagree: **MSCI** scored Tesla high on environment; **FTSE gave Tesla zero** on environment because its scoring looked at factories, not the emissions avoided by the cars; **Sustainalytics** was in between. Other frameworks in the case: SASB, TCFD, GRI. Lesson: **boundaries and methodology** (factory vs product life cycle) decide the score, the same lesson as LCA.

---

## 6. Energy-sector KPIs (Lecture 10) 📘 ⭐⭐
Oil & gas: **tCO₂e per unit, methane intensity, energy intensity**; hotspots: GHG emissions, methane, energy use, biodiversity. Power: g CO₂ per kWh, T&D loss %, plant load factor, % RE. Batteries/EV: kg CO₂e per kWh of cells, % recycled content, battery traceability, recovery rate. Corporate users: % RE electricity, energy intensity, Scope 2 (location- and market-based).

---

## Quick exam answers ⭐⭐⭐
**Q1. Explain the energy supply chain from supplies to disposal with one sustainability issue at each stage.**
Supplies: fuel extraction and critical minerals (methane leaks; cobalt from the DRC with child labour; lithium brine using 500,000 gallons of water per tonne). Production: power and refining (coal plants at about 22% efficiency, WTT of electricity about 20%). Distribution: T&D losses of 25.4%. End use: vehicle efficiency (TTW 15–32%; EV benefit depends on the grid). Disposal: 1.2 Mt of batteries by 2030 with only 5% recycled; EPR and recycling needed.

**Q2. What is the critical-minerals paradox?**
Decarbonising energy needs EVs, batteries, solar, wind and grids, which multiply demand for lithium, copper, nickel, cobalt, graphite and rare earths; their extraction brings water, biodiversity, emission, social and geopolitical risks (IEA 2025: lithium demand +30% in 2024; 7% of copper supply exposed to flood or drought).

**Q3. Why can an EV be worse than a petrol car in India?**
On WTW, India's coal-heavy grid (about 0.79 kg CO₂/kWh, WTT about 20%) makes an EV's use-phase emissions about 0.146 kg/km vs 0.135 for an ICE car (Rietmann data), and battery manufacturing adds embedded carbon. The EV wins once the grid falls below about 0.63–0.73 kg/kWh or is charged with renewables.

**Q4. What should Tesla do with end-of-life batteries?**
Follow the hierarchy: remanufacture and second-life use first, then hydrometallurgical or direct recycling; partner with Redwood or Li-Cycle now and build in-house as volumes grow; design for disassembly; report recovery honestly to avoid greenwashing.
