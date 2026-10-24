# Rapid Revision — Everything on One Page
The night-before sheet: every formula, list and headline number from the ten syllabus topics and the five numerical pages. Click through to the full pages when something is unclear. 📘 = course material, 📗 = textbook or practice data.

---

## 0. Exam pattern (Lecture 11) 📘 ⭐⭐⭐
- **Quiz (OLT), 20 marks**: MCQs on **CO5 + CO6**, from **PPTs 9, 10 and 11 only** → drill the [MCQ Bank](mcq-bank.md) Q1–Q120.
- **End-sem, 40 marks**, pen and paper, full syllabus including cases.
- **Weightage**: CO3 and CO4 **high**; CO2 and CO5 **medium**; CO1 and CO6 **low** (3-mark theory questions).
- **Answer recipe for every numerical**: state assumptions → formula → substitution → boxed answer with units → one-line interpretation → one managerial recommendation.

## 1. CO2 — Weighted scoring of suppliers ⭐⭐⭐ ([P1](p1-supplier-selection-numericals.md))
- **Steps**: criteria → weights summing to 100% → score each supplier (same scale) → **Σ (score × weight)** → rank → sensitivity → recommend with conditions.
- **Gate + score**: knock-out thresholds (human rights, safety, legal compliance) *before* weighting. A 95/100 supplier with labour violations is suspended, not retained.
- **Normalising**: benefit criterion = x ÷ max; cost criterion = min ÷ x; or min–max (x − min) ÷ (max − min).
- **Lecture 6 example (slide 24)**: weights Price 25, Quality 20, Delivery 15, Carbon 15, Safety 10, Innovation 10, Compliance 5 → **A 8.10, B 7.70, C 8.15 → C wins** (C > A > B).
- **VoltTech scorecard**: 0.25×88 + 0.20×90 + 0.15×85 + 0.15×80 + 0.10×92 + 0.10×78 + 0.05×95 = **86.50 → B (Good)** on the 90/75/60 bands (slide's "86.2 A" is inconsistent). Weak: innovation 78, carbon 80.
- **Lecture 10 supplier scorecard** weights: cost 20, quality 20, delivery 15, environment 15, labour & HR 10, carbon 10, governance 5, innovation 5. X (labour 10) = **72.75**, Y = **81.25**.
- **TOPSIS**: vector-normalise rᵢⱼ = xᵢⱼ ÷ √Σx² → weight → ideal A⁺ / anti-ideal A⁻ (max for benefit, min for cost) → S⁺, S⁻ (Euclidean) → **Cᵢ* = S⁻ ÷ (S⁺ + S⁻)** → rank high to low. Construction case: **C wins** (slide Cᵢ* 0.608 > A 0.382 > B 0.251 > D 0.106).
- **Risk matrix**: Likelihood × Impact (1–5): **High 15–24 (25 extreme), Medium 6–14, Low 1–5**. Agri-food: A 4×4 = 16 high, B 3×3 = 9 medium, C 2×2 = 4 low.
- **AHP**: pairwise 1–9 scale → normalise columns → row averages = weights → **CR = CI ÷ RI < 0.10**, CI = (λmax − n) ÷ (n − 1).
- **Kraljic**: profit impact × supply risk → **Strategic** (partner), **Bottleneck** (secure supply), **Leverage** (compete), **Routine/non-critical** (simplify).
- **TCO** = price + transport + duties + quality + energy/maintenance + end-of-life + risk. Lowest price ≠ lowest TCO.
- **ESG + RTI** criteria families: Environmental, Social, Governance + Risk, Technology, Innovation.
- **Tools**: weighted scoring, AHP, TOPSIS, DEA, LP (+ expert judgement, audits).

## 2. CO3 — Carbon accounting, Scope 1, 2, 3 ⭐⭐⭐ ([P2](p2-carbon-accounting-numericals.md))
- **Emissions = Activity data × Emission factor**; **CO₂e = gas mass × GWP**.
- **Factors (course)**: diesel **2.68 kg/l**; natural gas **1.9 kg/Sm³**; LPG **3.0 t/t**; Indian grid **0.70 t/MWh** (= kg/kWh); petrol car 120 g/km.
- **GWP-100**: CO₂ 1 · CH₄ 27–30 · N₂O 273 · HFCs 12–14,000 (HFC-134a ≈ 1,430) · PFCs 7,000–12,000 · SF₆ 25,200 · NF₃ 17,000. Kyoto basket = 7 gases (1997).
- **Scope 1** "what you burn" (fuel, company vehicles, process, fugitive) · **Scope 2** "what you buy" (electricity, heat, steam, cooling) · **Scope 3** "what you influence" (15 categories; usually **70–90%**).
- **Scope 3 categories**: upstream 1 purchased goods, 2 capital goods, 3 fuel & energy, 4 upstream transport, 5 waste, 6 business travel, 7 commuting, 8 upstream leased · downstream 9 downstream transport, 10 processing, 11 use of sold products, 12 end-of-life, 13 downstream leased, 14 franchises, 15 investments.
- **5 steps**: identify sources → collect activity data → apply factors → convert to CO₂e → aggregate & report (MRV).
- **Location-based** Scope 2 = grid average; **market-based** = contracts (PPA, RECs).
- **Auto plant case (50,000 ICE + 20,000 EV)**: Scope 1 = 950 + 536 + 150 = **1,636 t**; Scope 2 = 25,000 × 0.70 = **17,500 t**; materials 300,000 + 200,000; use phase ICE 18 t/car → **9,00,000 t**, EV 22,500 kWh × 0.70 = 15.75 t/car → **3,15,000 t**; logistics 23,500 t. ICEV line **12,42,636 t**, EV line **5,15,000 t**, plant **17,57,636 t**. Scope 1+2 = **1.09%**, Scope 3 = **98.9%**.
- Per vehicle (slide): ICE ~25 t; EV India grid ~28 t; EV RE grid ~13 t. Break-even grid ≈ **0.58 kg/kWh** (12 t mfg) or 0.667 (10 t).
- **Diesel example**: 10,000 l × 2.68 = **26,800 kg**. GWP example: 10 t CH₄ = 280, 2 t N₂O = 546, 0.1 t SF₆ = 2,520 → **3,346 t CO₂e**.
- **Practice inventory (P3)**: Scope 1 645.5, Scope 2 2,800, Scope 3 10,700 → **14,145.5 t**; shares 4.6 / 19.8 / 75.6%. Solar PPA 40% → saves 1,120 t (7.9% of total). Green steel beats everything inside the fence.
- **Carbon credit = 1 t CO₂e**. Avoidance, reduction, removal (removal priced higher). Registries: Verra, Gold Standard, ACR, CAR. Compliance (EU ETS, India **CCTS** 2023) vs voluntary.
- **Neutral** (offsets) vs **net zero** (cut 90–95%, neutralise residual with removals) vs carbon zero vs climate positive. **"Reduction first, offset later."**
- Standards: **GHG Protocol** (WRI + WBCSD), IPCC (GWPs), **ISO 14064** (verification), UNFCCC. Reporting: CDP, **GRI 305**, TCFD (4 pillars), IR (6 capitals), **BRSR** (9 principles, Sections A–C).
- **CBAM**: EU levy on embedded emissions of imports (steel, aluminium, cement, fertiliser, hydrogen, electricity); verified MRV avoids punitive default values.

## 3. CO4 — Distribution networks, logistics cost, distance criteria ⭐⭐⭐ ([P3](p3-network-logistics-numericals.md))
- **Objective**: minimise **Z = C_total + λ·E_CO₂ + μ·W_waste**; C_total = facility + production + transport + inventory + collection + recovery + disposal.
- **Variables**: xᵢⱼ flows, yⱼ open/close (0/1), rᵢ recovered quantity. **Constraints**: demand, capacity, material balance, transport, recovery, collection, recycling targets, non-negativity. Look for a **Pareto-efficient** solution.
- **Material balance**: Returns = Reuse + Repair + Remanufacture + Recycling + Disposal.
- **Network A/B/C (Lecture 8)**: switching λ: A = B at **λ = 0.32**, B = C at **λ = 0.35** → A if λ < 0.32, B between, C above. "No single answer without decision-maker priorities."
- **10,000 returns**: 2,000 / 2,500 / 2,000 / 3,000 / 500 → recovery **95%**, value-retaining **65%**. Practice economics: **₹96.25 lakh** net value, **228 t** CO₂ avoided.
- **FMCG case (Lecture 10)**: 10,000 deliveries × 180 km, 62% utilisation, 18% empty → total 21.95 lakh km, 5.49 lakh l, **1,470.7 t CO₂/month**, **146 g/t-km**. At 80% utilisation and 10% empty → 1,038.5 t (**−29.4%**), 103 g/t-km, ₹1.48 cr/month saved. Grid-charged e-trucks emit *more* (390.6 vs 311.6 t).
- **Five FMCG KPIs**: CO₂e per t-km, fuel efficiency km/l, vehicle utilisation %, empty km %, OTIF %.
- **Transport CO₂** = t × km × factor (road 0.09, rail 0.025, water 0.015, air 0.60 kg/t-km 📗), or litres × 2.68. Intensity: **Air > Road > Rail > Water**.
- **Centre of gravity**: Cx = Σxᵢwᵢ ÷ Σwᵢ, Cy = Σyᵢwᵢ ÷ Σwᵢ. Practice: CoG (3.11, 3.61).
- **Load-distance** = Σ load × distance (Euclidean √(Δx² + Δy²) or rectilinear |Δx| + |Δy|). Practice: **Pune 64,629** < Hyderabad 69,998 < Nagpur 76,550 → Pune (107 t CO₂/yr less than Nagpur).
- **Factor rating**: Σ weight × score → Y 7.30 > X 7.20 > Z 6.65.
- **How many DCs?** Total cost U-shape: 1 → 32.0, **2 → 30.1**, 3 → 31.4, 4 → 34.4, 5 → 38.2 (₹ crore). More DCs: outbound ↓, facility + inventory ↑ (square-root law: inventory ∝ √n).
- **Cube**: 800 → 1,000 units per truck → 25 trips saved (−20%), 8.4 t CO₂ a month.
- **Decision levels**: strategic (where, how big), tactical (allocation, modes), operational (routing, frequency, consolidation).
- **9 nodes of the closed loop**: suppliers → plants → DCs → customers → collection → inspection/sorting → repair/reman/recycle → recovered materials → manufacturing again.
- **Collection networks**: centralised (scale, high-value low-volume), decentralised (local sorting, bulky high-volume), hybrid.
- **"The cleanest kilometre is often the kilometre eliminated."** Green transport ≠ sustainable logistics.

## 4. CO5 — Effective performance measurement systems ⭐⭐⭐ ([P4](p4-performance-measurement-numericals.md))
- **OTIF** = orders on time *and* in full ÷ total (joint count, not OT × IF). **Fill rate** = units shipped ÷ ordered. **Perfect order** = OTIF × damage-free × correct docs (if independent).
- Practice: OT 94.0%, IF 95.5%, **OTIF 91.5%**, fill rate **97.2%**, perfect order **89.7%**.
- **OEE** = Availability × Performance × Quality (world class ≈ 85%). Practice: 87.5% × 89.5% × 96.0% = **75.2%**.
- **Intensity**: t CO₂e ÷ output or ÷ ₹ crore revenue (BRSR per rupee of turnover, PPP-adjusted). Practice: 7.4 t/₹ cr, 14.8 kg/unit, 76 MJ/unit, 248 L/unit.
- **LTIFR** = LTIs × 10⁶ ÷ person-hours → practice **0.79**.
- **Achievement**: higher-better actual ÷ target; lower-better target ÷ actual; cap at 1.2; **composite = Σ weight × capped achievement** (Lecture 3 dashboard 1.117; BSC 1.003).
- **Required annual improvement** to reach a benchmark in n years = 1 − (benchmark ÷ current)^(1/n) → practice 9.0%/yr.
- **Leading** (training, RE contracts, supplier audits) vs **lagging** (injuries, actual emissions). Pair each lagging KPI with its drivers.
- **Four KPI questions**: What happened? Why did it happen? Who owns it? What decision will change?
- **KPI trap**: 75 + 40 + 30 indicators, no answer on whether the chain is more sustainable.
- **Five tests**: **Material, Balanced, Actionable, Comparable, Credible**. "If a KPI does not change a decision, question why it exists."
- **SMART**: Specific, Measurable, Achievable, Relevant, Time-bound.
- **Q + D + I + R + S** dimensions (Lecture 3): Quality, Delivery, Innovation, Resilience, Sustainability.
- **Sustainability BSC**: financial, customer, internal process, learning & growth + environmental & social.
- **SCOR + sustainability**: Plan, Source, Make, Deliver, Return, Enable, each with a green KPI.
- **Performance loop (7)**: Identify → Measure → Target → Improve → Verify → Report → Review.
- **TAS** = 0.25 Econ + 0.25 Env + 0.20 Social + 0.15 Resilience + 0.15 Strategic fit (1–5). **NTV** = gross benefits − adoption cost − lifecycle sustainability cost − risk cost.
- **Navya (practice)**: gross ₹46 cr, NTV ₹28 cr, NPV ₹20.9 cr, payback 2.9 yrs, TAS 3.80 → **pilot first**.
- **Decision matrix**: high value + high impact **Prioritise**; low value + high impact **Reconsider**; high value + low impact **Optimise**; low + low **Avoid**.
- **Cost of poor quality**: defects → rework energy, scrap, extra trips. "Quality failure = environmental failure."
- **Company A vs B**: a good report ≠ good performance; check boundary, baseline, assurance.

## 5. LCA, LCSA and energy numericals ⭐⭐ ([P5](p5-lca-energy-numericals.md))
- **ISO 14040/44 phases**: Goal & scope (functional unit, boundary) → Inventory (LCI) → Impact assessment (LCIA) → Interpretation (iterative).
- **Functional unit**: "carry 20 kg of groceries a month", not "one bag". Bags example: 25 vs 10 kg; reusable bag breaks even at **60 uses**.
- **Boundaries**: cradle-to-gate, gate-to-gate, cradle-to-grave, cradle-to-cradle.
- **LCSA = E-LCA + LCC + S-LCA**.
- **LED vs incandescent** (practice): ₹2,050 & 157.5 kg vs ₹13,000 & 1,050 kg; payback 515 h.
- **EV vs ICE, India WTW**: 0.146 vs **0.135 kg/km**; EV wins below a grid of about 0.63–0.73 kg/kWh.
- **Logistic (S-curve) adoption**: EV share 12.9 / 45.9 / 83.0%; 30% reached in 8.0 yrs.
- **Energy chain facts**: T&D losses **25.4%**; coal plant ~22% efficient; TTW 15–32%; 1.2 Mt of batteries by 2030, ~5% recycled; lithium brine ~500,000 gallons water per tonne.

---

## 6. CO1 — SSCM and business performance (3-markers) ⭐⭐⭐ ([Ch 1](ch01-sscm-business-performance.md))
- **SSCM** = managing material, information and capital flows and co-operation along the chain while integrating **economic, environmental and social** goals from stakeholder requirements.
- **TBL / 3P**: People, Planet, Profit. Resilience is the **fourth pillar** (Lecture 9).
- Linear (take–make–use–dispose, cradle-to-grave) vs circular (cradle-to-cradle).
- **5-step strategy**: assess current state → stakeholders → scenarios → design → operationalise.
- **Risks of ignoring**: CBAM and carbon taxes, disruptions, reputation, investor pressure, customer loss.
- **Business impact**: cost ↓ (energy, waste, logistics), revenue ↑ (green markets), risk ↓, cost of capital ↓, brand and talent, innovation.

## 7. Topic 2 — LCA and carbon footprints ⭐⭐⭐ ([Ch 2](ch02-lca-carbon-footprints.md))
- Carbon footprint = one impact category (climate). LCA = multi-impact (climate, ozone, smog, water, land, ecotoxicity, biodiversity).
- **Net-zero hierarchy**: Measure → Reduce → RE transition → Sustainable supply chain → Offset (afforestation, CCUS).
- **MRV**: Measure, Report, Verify. LCA limitations: data quality, allocation, boundary choice, cost, time.

## 8. Topic 3 — Sustainable procurement ⭐⭐⭐ ([Ch 3](ch03-sustainable-procurement.md))
- Procurement = **50–80% of cost** and the largest Scope 3 category.
- **Six challenges**: higher upfront cost, supplier resistance, limited data, greenwashing, poor visibility, regulatory uncertainty.
- Cases: **Walmart Project Gigaton**, Schneider Zero Carbon, **Nestlé** responsible sourcing, M&M supplier code (95% by value).

## 9. Topic 4 — Sustainable manufacturing and productivity ⭐⭐⭐ ([Ch 4](ch04-sustainable-manufacturing.md))
- **UNEP definition**: economically sound processes that minimise environmental impact, conserve energy and resources, and keep employees, communities and consumers safe.
- **Framework**: Inputs → Process → Outputs → Recycling → Reuse → Remanufacturing → Closed loop.
- **Principles**: lean (Toyota TPS), Six Sigma (3.4 DPMO), kaizen, circular economy (Interface, Michelin), cleaner production (3M 3P), eco-design (Philips, IKEA), life-cycle thinking (Intel, Tata Steel).
- **TIMWOOD**: Transport, Inventory, Motion, Waiting, Over-production, Over-processing, Defects (+ Skills).
- **Productivity chain**: resource efficiency → less waste → lower cost → higher productivity → profitability → competitive advantage.
- Takeaway: **Cleaner, Leaner, Smarter, Profitable, Resilient**.

## 10. CO6 — Technology and quality tools ⭐⭐⭐ ([Ch 5](ch05-technology-quality-tools.md))
- **Technology ≠ sustainability**: energy use, e-waste, capex, cyber risk; potential ≠ realised benefit.
- **Five trade-offs**: efficiency vs footprint; traceability vs energy; visibility vs privacy; global optimisation vs local resilience; digital inclusion vs supplier exclusion.
- **Tech-Sustain (7)**: define problem → baseline → alternatives → lifecycle impact → TBL → stress-test → pilot, measure, scale.
- Cases: **Walmart–IBM blockchain** (mango trace 7 days → 2.2 s), Asian Paints.
- **ISO's seven quality principles**: customer focus, leadership, engagement, process approach, improvement, evidence-based decisions, relationship management. ISO 14001 = EMS; integrated management system = 9001 + 14001 + 45001.

## 11. Topic 6 — Sustainable logistics ⭐⭐⭐ ([Ch 6](ch06-sustainable-logistics.md))
- **Green logistics levers**: modal shift, route optimisation, consolidation, EV/alternative fuel, green warehousing (solar, LED, natural light), right-sized returnable packaging.
- **DHL's six levers**; Indian cases: Hindustan Zinc LNG/EV trucks, GreenLine LNG fleet.
- **Recovery hierarchy**: reuse → repair → refurbish → remanufacture → recycle → energy recovery → disposal.
- **Why reverse logistics is hard**: uncertain quantity, timing and condition; low density; high sorting cost; information gaps; non-standard products; dependence on consumers.

## 12. Topic 7 — Designing the sustainable network ⭐⭐⭐ ([Ch 7](ch07-network-design.md))
- **R-ladder**: Refuse, Reduce, Reuse, Repair, Refurbish, Remanufacture, Repurpose, Recycle. "Recycling is usually lower in value retention."
- **PaaS**: CNH harvester rental, SDLG equipment leasing, JSW MG Windsor battery-as-a-service, Philips/Signify lighting-as-a-service, Furlenco furniture. The maker keeps economic incentive + physical control + material value.
- **Four integrated questions**: where to locate facilities, which flows to move, which transport mode, what happens to returns. Together they set **cost + carbon + circularity**.

## 13. Topic 8 — Measuring SSCM performance ⭐⭐⭐ ([Ch 8](ch08-performance-measurement.md))
- **GRI** (impacts, all stakeholders) · **TCFD/ISSB** (investors, climate risk) · **BRSR / BRSR Core** (SEBI, assured KPIs) · **CDP**.
- **Greenwashing** (overclaim) vs **greenhushing** (underclaim). Credible claim = metric + boundary + method + baseline + target + evidence.

## 14. Topic 9 — Energy-sector supply chain ⭐⭐ ([Ch 9](ch09-energy-sector.md))
- **Supplies** (fuels, critical minerals: Li, Co, Ni, graphite, rare earths) → **Production** (coal-heavy grid, RE, hydrogen) → **End use** (transport, TTW vs WTW) → **Disposal** (batteries, solar panels, EPR).
- **Critical-minerals paradox**: decarbonisation multiplies demand for minerals whose extraction carries water, biodiversity, social and geopolitical risk.
- **Tesla EoL batteries**: reuse/second life first, then hydrometallurgical recycling; partner (Redwood, Li-Cycle) before building in-house.

## 15. Topic 10 — SSCM best practices ⭐⭐⭐ ([Ch 10](ch10-sscm-best-practices.md))
- **Polycrisis (6)**: climate, geopolitics, critical resources, regulation, social risk, technology disruption.
- **Strategy architecture**: **D-P-R-C-M-I-S** — Diagnose, Prioritise, Redesign, Collaborate, Measure, Innovate, Scale.
- **Five strategies**: sustainable procurement ("do not outsource sustainability"), product design, circular chains, sustainable logistics, digital chains (IoT, AI, digital twin, blockchain, **DPP**).
- **JIT + JIC + JIS**; mitigation vs adaptation.
- **Eight transitions**: fossil → renewable; virgin → circular materials; linear → circular products; concentration → diversification; opaque → traceable; ownership → access; reactive → predictive; reporting → embedded in decisions.
- **Best-practice cases**: Apple, Walmart Gigaton, Schneider, Unilever, Nestlé, IKEA, Renault Refactory, DHL, Toyota; **ITC eChoupal**, HUL, Tata Motors Re.Wi.Re, Mahindra, Tata Steel, Asian Paints, Dalmia, Arvind, JSW Steel, Hindustan Zinc ([Case Studies](case-studies.md)).
