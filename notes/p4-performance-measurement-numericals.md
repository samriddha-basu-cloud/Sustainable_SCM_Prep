# CO5 Numericals: Effective Performance Measurement Systems
This page covers **CO5: effective performance measurement systems**. It is a **7-mark** numerical in the end-sem paper, and it is also one of the two COs in the **20-mark online quiz** (CO5 + CO6, from PPTs 9, 10 and 11) 📘. The numericals come from **Lecture 3** (the performance dashboard and the performance management framework), **Lecture 10** (KPI architecture, SCOR + sustainability KPIs, quality as sustainability, the FMCG 5-KPI exercise, Company A vs B) and **Lecture 9** (Technology Adoption Score, Net Technology Value and the Navya exercise) 📘. Practice data are marked 📗. Turn on **Self-test** (`T`) to hide answers.

Theory: [Measuring Sustainable SC Performance](ch08-performance-measurement.md) and [Technology & Quality Tools](ch05-technology-quality-tools.md).

---

## Formulas you must know for CO5 ⭐⭐⭐
**Delivery and customer KPIs**
- **On-time delivery %** = orders delivered on or before the promised date ÷ total orders × 100.
- **In-full %** = orders delivered complete ÷ total orders × 100.
- **OTIF %** = orders delivered *both* on time *and* in full ÷ total orders × 100. (OTIF is not OT% × IF% unless the two are independent; count the orders that pass both.)
- **Fill rate (unit)** = units shipped from stock ÷ units ordered × 100.
- **Perfect order rate** = orders that are on time, in full, damage-free and with correct documents ÷ total orders. If only component rates are given and you assume independence, perfect order ≈ OTIF × damage-free % × correct-documents %.
- **NPS** = % promoters (9–10) − % detractors (0–6); range −100 to +100.

**Operational KPIs**
- **OEE** = Availability × Performance × Quality, where Availability = run time ÷ planned production time; Performance = (ideal cycle time × total units) ÷ run time; Quality = good units ÷ total units. World-class OEE is about 85%.
- **First-pass yield (FPY)** = units right first time ÷ units started.
- **Vehicle utilisation %** = load carried ÷ vehicle capacity; **empty km %** = empty km ÷ total km.
- **Inventory turns** = COGS ÷ average inventory; **days of inventory** = 365 ÷ turns.

**Environmental intensity KPIs** (always normalise; absolute numbers hide growth)
- **Carbon intensity** = t CO₂e ÷ output (per unit, per tonne, per ₹ crore of revenue). BRSR reports intensity per rupee of turnover (and per rupee of turnover adjusted for PPP).
- **Energy intensity** = GJ or kWh ÷ unit of output; **water intensity** = kL ÷ unit; **waste recycling rate** = waste recycled or reused ÷ total waste generated.
- **Transport carbon intensity** = g CO₂e ÷ tonne-km.

**Social KPIs**
- **LTIFR** (lost-time injury frequency rate) = number of lost-time injuries × 1,000,000 ÷ total person-hours worked (BRSR uses per one million person-hours).
- **Training hours per employee** = total training hours ÷ number of employees.
- **Supplier audit coverage %** = suppliers (or spend) audited ÷ total suppliers (or spend).

**Target achievement (for scorecards and composite indices)**
- Higher-is-better KPI: achievement = actual ÷ target.
- Lower-is-better KPI: achievement = target ÷ actual.
- Cap the achievement (for example at 1.2 or 120%) so one over-achievement cannot hide a failure elsewhere. Composite index = Σ (weight × capped achievement).
- **Gap to benchmark** = (your value − benchmark) ÷ benchmark. **Required annual improvement** to close a gap in n years = 1 − (benchmark ÷ current)^(1/n) for a lower-is-better KPI.

**Lecture 9 technology formulas** 📘
- **TAS (Technology Adoption Score)** = 25% Economic + 25% Environmental + 20% Social + 15% Resilience + 15% Strategic fit, each scored 1–5.
- **Net Technology Value** = Gross benefits − Adoption cost − Lifecycle sustainability cost − Risk cost.

---

## Problem 1. Monthly KPI computation for a distributor 📗 ⭐⭐⭐
A distribution centre's data for one month: 2,000 orders. 1,880 were delivered on time, 1,910 in full and 1,830 both on time and in full. 1,975 arrived damage-free and 1,985 had correct invoices and documents. Customers ordered 50,000 units, of which 48,600 were shipped from stock.

**Q1.1 Compute on-time %, in-full %, OTIF %, fill rate and perfect-order rate.**
- On-time = 1,880 ÷ 2,000 = **94.0%**.
- In-full = 1,910 ÷ 2,000 = **95.5%**.
- OTIF = 1,830 ÷ 2,000 = **91.5%** (this is higher than the 94.0% × 95.5% = 89.8% you would get by multiplying, because late orders and short orders often overlap; always use the joint count when it is given).
- Fill rate (units) = 48,600 ÷ 50,000 = **97.2%**.
- Perfect order (assuming independence of damage and documents from OTIF) = 0.915 × (1,975 ÷ 2,000) × (1,985 ÷ 2,000) = 0.915 × 0.9875 × 0.9925 = **89.7%**.

**Q1.2 Interpret. Why is fill rate (97.2%) so much better than perfect order (89.7%)?**
Fill rate measures only whether *units* were available; perfect order measures the *whole customer experience*, so every failure mode (late, short, damaged, wrong paperwork) multiplies down. A company that reports only fill rate looks excellent while one order in ten still fails the customer. From a sustainability view every imperfect order also creates waste: re-delivery trips, returns, damaged goods and duplicate paperwork.

## Problem 2. OEE, intensity and safety KPIs for a plant 📗 ⭐⭐⭐
A plant runs one 480-minute shift. Breakdowns and changeovers take 60 minutes. The ideal cycle time is 0.8 minute per unit. The shift produced 470 units, of which 451 were good. For the year, the plant emitted 18,500 t CO₂e (Scope 1 + 2), made 1.25 million units, used 95,000 GJ of energy and 3,10,000 kL of water, on revenue of ₹2,500 crore. It had 2,400 employees working 2,100 hours each and recorded 4 lost-time injuries.

**Q2.1 Compute OEE.**
- Availability = (480 − 60) ÷ 480 = 420 ÷ 480 = **87.5%**.
- Performance = (0.8 × 470) ÷ 420 = 376 ÷ 420 = **89.5%**.
- Quality = 451 ÷ 470 = **96.0%**.
- **OEE = 0.875 × 0.895 × 0.960 = 75.2%** (below the ~85% world-class benchmark; the biggest loss is availability).

**Q2.2 Compute the intensity KPIs.**
- Carbon intensity = 18,500 ÷ 2,500 = **7.4 t CO₂e per ₹ crore** of revenue, or 18,500,000 kg ÷ 1,250,000 = **14.8 kg CO₂e per unit**.
- Energy intensity = 95,000 GJ ÷ 1.25 M units = 0.076 GJ = **76 MJ per unit**.
- Water intensity = 3,10,000 ÷ 12,50,000 = **0.248 kL (248 litres) per unit**.

**Q2.3 Compute LTIFR.**
Person-hours = 2,400 × 2,100 = 50,40,000. LTIFR = 4 × 10,00,000 ÷ 50,40,000 = **0.79 per million hours**.

**Q2.4 How does OEE link to sustainability?**
Lost availability, slow running and defects all consume energy and materials without producing good output. Raising OEE from 75% to 85% makes about 13% more good units from the same machines, energy base-load and floor space, so energy, water and CO₂ *per good unit* fall even if absolute use stays flat. This is Lecture 7's point that lean and sustainability reinforce each other.

## Problem 3. Reading the Lecture 3 performance dashboard 📘 ⭐⭐⭐
Lecture 3 (slide 24) shows a "Suggested MBA Dashboard" with six perspectives, each with four KPIs and a "vs target" variance:

| Perspective | KPI (actual, vs target) |
|---|---|
| Economic | Revenue growth 12.5% (+2.5); operating margin 15.8% (+1.8); cost per shipment $96.4 (−3.6%); ROCE 18.7% (+2.7) |
| Environmental | CO₂ per tonne-km 62.3 (−8.7%); energy intensity 1.45 (−6.3%); water intensity 2.10 (−5.1%); waste recycling 78% (+8) |
| Social | LTIFR 0.68 (−15%); employee training 24.6 h (+12%); diversity 36% (+6); supplier audit score 88 (+5) |
| Risk | High-risk suppliers 6% (−2); supply disruption incidents 3 (−25%); on-time risk assessment 92% (+7); risk exposure score 2.3 (−0.4) |
| Customer | On-time delivery 96.2% (+3.2); perfect order 93.1% (+2.1); order fill 98.4% (+1.4); NPS 68 (+8) |
| Innovation | New products 6 (+2); process improvement projects 14 (+4); automation coverage 43% (+8); R&D spend 2.8% of revenue (+0.3) |

Trend charts (Jan–Jun): operating margin rises from about 10% to 15–16%; CO₂ per tonne-km falls from about 78 to 62; LTIFR falls from about 1.4 to about 0.65; risk exposure peaks at about 3.2 in February and ends at about 2.3; on-time delivery rises from about 89% to about 96%. Risk level split: High 14%, Medium 32%, Low 54%. Innovation funnel: 48 ideas → 23 in progress → 11 testing → 6 launched. The slide's message is *"Balanced dashboard = performance data > strategic decisions."*

**Q3.1 Back-calculate the targets for CO₂ per tonne-km, LTIFR, on-time delivery and cost per shipment.**
- CO₂/t-km: actual is 8.7% below target → target = 62.3 ÷ (1 − 0.087) = **68.2 g/t-km**.
- LTIFR: actual is 15% below target → target = 0.68 ÷ 0.85 = **0.80**.
- On-time delivery: +3.2 points → target = **93.0%**.
- Cost per shipment: 3.6% below target → target = 96.4 ÷ 0.964 = **$100**.
(Read "%" variances on a percentage KPI as percentage points, and "%" variances on an absolute KPI as relative change. State this assumption in the exam.)

**Q3.2 Build a composite performance index with weights Economic 20%, Environmental 20%, Social 15%, Risk 15%, Customer 20%, Innovation 10%, using capped (1.2) achievement ratios averaged within each perspective.**

| Perspective | Achievement ratios (capped at 1.2) | Average | Weight | Contribution |
|---|---|---|---|---|
| Economic | 1.200, 1.129, 1.037, 1.169 | 1.134 | 0.20 | 0.227 |
| Environmental | 1.095, 1.067, 1.054, 1.114 | 1.083 | 0.20 | 0.217 |
| Social | 1.176, 1.120, 1.200, 1.060 | 1.139 | 0.15 | 0.171 |
| Risk | 1.200, 1.200, 1.082, 1.174 | 1.164 | 0.15 | 0.175 |
| Customer | 1.034, 1.023, 1.014, 1.133 | 1.051 | 0.20 | 0.210 |
| Innovation | 1.200, 1.200, 1.200, 1.120 | 1.180 | 0.10 | 0.118 |
| **Index** | | | | **1.117** |

(Examples: revenue growth 12.5 ÷ 10 = 1.25 → capped 1.20; CO₂ 68.2 ÷ 62.3 = 1.095; high-risk suppliers 8 ÷ 6 = 1.33 → capped 1.20.)

The company is performing at about **112% of target** overall; customer (1.05) and environmental (1.08) are the weakest perspectives.

**Q3.3 Every KPI is green. Is that good news? Give a manager's interpretation.**
Not necessarily. Lecture 10's "KPI trap" warns that more KPIs do not mean better management. When all 24 KPIs beat target, the likely causes are soft targets (set from last year's actuals instead of science-based or benchmark targets), or KPIs chosen because they are easy to hit. The useful questions are: is 62.3 g/t-km good against the **benchmark** (not only against our own target)? Is the 14% high-risk share of the supply base (risk donut) consistent with only 6% "high-risk suppliers"? Is a 36% diversity figure measured in the same way as peers? Do the trends (CO₂ per t-km flattening after April, LTIFR rising slightly in June) need action? The next step is to raise targets to benchmark or SBTi levels and check that each KPI changes a decision.

**Q3.4 Read the trends: what is the percentage improvement in CO₂ per tonne-km and in LTIFR from January to June?**
- CO₂/t-km: (78 − 62.3) ÷ 78 ≈ **20% reduction** in six months.
- LTIFR: (1.4 − 0.68) ÷ 1.4 ≈ **51% reduction**.
- On-time delivery: 89% → 96.2%, a gain of about **7 percentage points**.
Both environmental and safety improvements came with better delivery and margin, which supports the Lecture 3 claim that sustainability and business performance can move together.

## Problem 4. Sustainability balanced scorecard with weighted achievement 📗 ⭐⭐⭐
A logistics company uses a Sustainability Balanced Scorecard with these KPIs, targets and weights:

| KPI | Actual | Target | Better | Weight |
|---|---|---|---|---|
| Cost per shipment (₹) | 9,640 | 10,000 | Lower | 15% |
| ROCE (%) | 18.7 | 18.2 | Higher | 10% |
| CO₂ (g per t-km) | 62.3 | 68.2 | Lower | 15% |
| Energy intensity (kWh per unit) | 1.45 | 1.55 | Lower | 10% |
| Waste recycling (%) | 78 | 85 | Higher | 10% |
| LTIFR | 0.68 | 0.60 | Lower | 10% |
| Supplier audit score | 88 | 90 | Higher | 10% |
| OTIF (%) | 93.1 | 95 | Higher | 20% |

**Q4.1 Compute the achievement ratio for each KPI and the weighted index.**

| KPI | Formula | Ratio | Weighted |
|---|---|---|---|
| Cost/shipment | 10,000 ÷ 9,640 | 1.037 | 0.156 |
| ROCE | 18.7 ÷ 18.2 | 1.027 | 0.103 |
| CO₂/t-km | 68.2 ÷ 62.3 | 1.095 | 0.164 |
| Energy intensity | 1.55 ÷ 1.45 | 1.069 | 0.107 |
| Waste recycling | 78 ÷ 85 | 0.918 | 0.092 |
| LTIFR | 0.60 ÷ 0.68 | 0.882 | 0.088 |
| Supplier audit | 88 ÷ 90 | 0.978 | 0.098 |
| OTIF | 93.1 ÷ 95 | 0.980 | 0.196 |
| **Index** | | | **1.003** |

**Q4.2 The index is 100.3%, "on target". What does the manager actually learn?**
The headline hides that **four of eight KPIs are below target**, including the safety KPI (LTIFR 12% worse than target) and recycling (8% short). Over-achievement on cost and carbon offsets these. Two fixes are common: (a) a **knock-out or minimum threshold** for critical KPIs (for example any safety KPI below 95% of target turns the scorecard red, the same logic as Lecture 10's "95/100 on cost-quality-delivery but serious labour violations" supplier question); (b) report the index **by perspective** and not only as one number. A single composite is useful for ranking but dangerous for management.

**Q4.3 Map these KPIs to the four Balanced Scorecard perspectives from Lecture 10.**
- Financial: cost per shipment, ROCE (Lecture 10 examples: supply chain cost, ROIC, cost avoidance).
- Customer: OTIF (Lecture 10: sustainable product share, customer complaints, green customer retention).
- Internal process: CO₂/t-km, energy intensity, waste recycling, supplier audit score (Lecture 10: carbon intensity, supplier quality, circularity).
- Learning and growth: none here. That is a gap; add ESG skills or training hours, innovation or employee engagement (Lecture 10 examples) and LTIFR could sit with people as well.

## Problem 5. Five KPIs for the FMCG distribution network (Lecture 10, slide 12) 📘 ⭐⭐⭐
Lecture 10's exercise: *An FMCG company wants to reduce the environmental impact of its distribution network. Current situation: 10,000 deliveries/month, average distance 180 km, diesel trucks, 62% average vehicle utilisation, 18% empty return kilometres. Develop 5 KPIs.* The slide's answer: **1) Carbon → CO₂e per tonne-km; 2) Cost → fuel efficiency (km per litre); 3) Utilisation → vehicle utilisation %; 4) Empty km → empty km %; 5) Reliability → OTIF %.**

**Q5.1 For each KPI write the formula, the baseline and a SMART target.**

| KPI | Formula | Baseline (📗 where not given) | SMART target |
|---|---|---|---|
| CO₂e per tonne-km | Total fleet CO₂e ÷ total tonne-km delivered | 146 g/t-km (computed in CO4 Problem 3) | Reduce to 110 g/t-km by March 2028 through consolidation and CNG/EV pilots |
| Fuel efficiency | Total km ÷ litres of diesel | 4.0 km/l | Improve to 4.6 km/l in 12 months through driver training and route optimisation |
| Vehicle utilisation | Load carried ÷ capacity (weight or cube) | 62% | Raise to 80% within 9 months via load planning and milk runs |
| Empty km % | Empty km ÷ total km | 18% | Cut to 8% within 12 months through backhaul partnerships |
| OTIF % | Orders on time and in full ÷ total orders | 92% | Hold at ≥ 95% while the changes above are made |

**Q5.2 Why is OTIF on the list when the goal is environmental?**
OTIF is the **guard-rail KPI**. Higher utilisation and fewer trips can be achieved by delaying shipments until trucks are full, which would hurt customers. Lecture 10's five tests say a KPI set must be **balanced**, so an environmental programme carries one service KPI to make sure CO₂ is not cut at the expense of reliability.

**Q5.3 Classify the five KPIs as leading or lagging.**
CO₂e per t-km, fuel efficiency and OTIF are **lagging** (they report what happened). Vehicle utilisation and empty km % are closer to **leading** for carbon, because improving them today predicts lower CO₂ next month. Lecture 10: *"Lagging KPIs tell you what happened; leading KPIs tell you whether you are likely to improve."* Add a pure leading KPI such as **% of trips planned with the route-optimisation tool** or **% of drivers trained in eco-driving**.

## Problem 6. Leading vs lagging and the KPI architecture (Lecture 10) 📘 ⭐⭐
Lecture 10's KPI architecture pairs each leading indicator with the lagging result it drives:

| Leading indicator | Lagging indicator |
|---|---|
| Supplier ESG assessments | Actual supplier incidents |
| Employee training | Injury rate |
| Renewable-energy contract | Actual Scope 2 emissions |
| Eco-design projects | Product carbon footprint |
| Preventive maintenance | Equipment failure |
| Supplier development | Defect rate |
| Risk assessments | Disruption losses |

**Q6.1 Classify each of these as leading or lagging, and as input, process, output, outcome or business value (Lecture 3 performance management framework): (a) % of suppliers trained on decarbonisation; (b) Scope 3 Category 1 emissions; (c) number of energy audits completed; (d) energy cost saved (₹ crore); (e) % of renewable electricity contracted for next year; (f) customer complaints on damaged packaging; (g) investment in solar rooftop; (h) market share of green products.**
- (a) Leading; process.
- (b) Lagging; outcome.
- (c) Leading; process (activity).
- (d) Lagging; business value.
- (e) Leading; input.
- (f) Lagging; outcome.
- (g) Leading; input.
- (h) Lagging; business value.
The Lecture 3 chain runs **inputs (resources, investments) → processes (activities) → outputs (immediate results) → outcomes (impact on stakeholders and the environment) → business value (profit, growth, reputation)**. A good system has KPIs at every stage, so leaders can see the problem before it reaches the lagging result.

**Q6.2 Lecture 10 says every KPI must answer four questions. Apply them to "energy per unit".**
The four questions on the slide: ***What happened? Why did it happen? Who owns it? What decision will change because of it?*** For energy per unit (kWh per good unit): *what happened* — it rose from 3.0 to 3.3 kWh/unit this month; *why* — compressed-air leaks and idle running during a changeover-heavy schedule; *who owns it* — the plant head with the maintenance lead; *what decision changes* — run a leak audit, switch off idle machines and reschedule energy-intensive batches to solar hours. If no decision would change, the KPI is noise (Lecture 10's "KPI trap": a company may track 75 sustainability, 40 supplier and 30 logistics indicators *"yet managers still cannot answer: are we becoming more sustainable?"*).

## Problem 7. SCOR + sustainability KPI set (Lecture 10) 📘 concept + 📗 data ⭐⭐⭐
Lecture 10 adds one sustainability KPI to each SCOR process: **Plan** – carbon-aware demand planning (forecast accuracy); **Source** – supplier sustainability score; **Make** – energy per unit; **Deliver** – CO₂e per shipment; **Return** – product recovery rate; **Enable** – ESG data quality.

Data for one year 📗: forecast MAPE 18%; procurement spend ₹600 crore, of which ₹420 crore is with suppliers scoring ≥ 70 on the ESG scorecard; plant electricity 3,600 MWh for 1.2 million units; outbound logistics 1,850 t CO₂e over 46,000 shipments; 9,500 units returned, 8,550 recovered by reuse, refurbishment or recycling; 1,300 ESG data points reported, 1,170 of them verified against source evidence.

**Q7.1 Compute the SCOR sustainability KPIs.**
- Plan: forecast accuracy = 1 − 0.18 = **82%**. (Better forecasting reduces over-production, expediting by air and obsolete stock, so it is a carbon lever.)
- Source: % of spend with ESG-qualified suppliers = 420 ÷ 600 = **70%**.
- Make: energy per unit = 3,600,000 kWh ÷ 1,200,000 = **3.0 kWh per unit**.
- Deliver: CO₂e per shipment = 1,850,000 kg ÷ 46,000 = **40.2 kg CO₂e per shipment**.
- Return: recovery rate = 8,550 ÷ 9,500 = **90%**.
- Enable: ESG data quality = 1,170 ÷ 1,300 = **90% verified**.

**Q7.2 Which KPI should the board look at first, and why?**
**Enable (data quality)**. With only 90% of data points verified, every other figure carries uncertainty; BRSR Core (Lecture 10) is moving companies from *"we are committed to sustainability"* to *"show me the data"*, with assurance, evidence trails and internal controls. The second priority is Source (70%), because purchased goods are usually the largest Scope 3 category.

## Problem 8. Quality failure as an environmental failure (Lecture 10, Section B) 📘 concept + 📗 data ⭐⭐⭐
Lecture 10: defects lead to rework, which needs extra materials and extra energy, then extra transport, then waste and more CO₂. *"Quality failure is simultaneously an economic and environmental failure."*

A component plant makes 5,00,000 units a year with a 4% defect rate. Of defective units, 60% are reworked (5 kWh and ₹150 each) and 40% are scrapped and remade (2.5 kg steel per unit at 2.0 kg CO₂e per kg steel, 12 kWh per remade unit, ₹900 per scrapped unit). Grid factor 0.71 kg CO₂e per kWh.

**Q8.1 Compute the annual carbon and cost of poor quality.**
- Defective units = 4% × 5,00,000 = 20,000 → reworked 12,000, scrapped 8,000.
- Rework energy = 12,000 × 5 = 60,000 kWh → 60,000 × 0.71 = **42.6 t CO₂e**; cost 12,000 × ₹150 = ₹18 lakh.
- Scrap material = 8,000 × 2.5 kg = 20,000 kg steel × 2.0 = **40.0 t CO₂e**.
- Re-production energy = 8,000 × 12 = 96,000 kWh × 0.71 = **68.2 t CO₂e**.
- Scrap cost = 8,000 × ₹900 = ₹72 lakh.
- **Total: about 150.8 t CO₂e and ₹90 lakh a year.**

**Q8.2 A Six Sigma project cuts defects to 1%. What are the savings, and what is the change in sigma level?**
Defects fall by 75%, so savings are 0.75 × 150.8 = **113 t CO₂e** and 0.75 × ₹90 lakh = **₹67.5 lakh a year**. DPMO falls from 40,000 to 10,000, which is roughly **3.25σ → 3.8σ** (with the conventional 1.5σ shift). This is the TQM + Lean + Six Sigma + Green Supply Chain connection the slide makes; the waste type is the "D" (defects) of TIMWOOD.

## Problem 9. Benchmarking gap and the required rate of improvement (Lecture 3) 📘 concept + 📗 data ⭐⭐
Lecture 3 defines benchmarking as *comparing performance, processes and practices with the best-performing organisations or recognised standards to identify gaps and opportunities*, against industry leaders (Amazon logistics, Toyota lean, Unilever sourcing), competitors (Tata Motors vs M&M, Asian Paints vs Berger, HUL vs ITC), global standards (ISO 9001, 14001, 45001, 27001; BRSR, GRI, CDP, SBTi) and your own history. *"Benchmark not to imitate competition but to continuously outperform self."*

A paint company's carbon intensity is 0.80 t CO₂e per tonne of product. The industry leader is at 0.50.

**Q9.1 What is the gap?**
Gap = (0.80 − 0.50) ÷ 0.50 = **60% above the leader** (or the leader is 37.5% lower than the company).

**Q9.2 What constant annual reduction closes the gap in 5 years (assuming the leader stands still)?**
Required rate r: 0.80 × (1 − r)⁵ = 0.50 → (1 − r) = (0.625)^(1/5) = 0.9103 → **r ≈ 9.0% a year**. (A straight-line path would be 0.06 t per year, which is 7.5% of the base in year 1 but 11% of the remaining level by year 5.)

**Q9.3 If the company can manage only 5% a year, how long will it take?**
n = ln(0.625) ÷ ln(0.95) = **9.2 years**, and the leader will have moved on. The managerial message is that benchmarking must lead to a step change (for example renewable PPAs, low-carbon raw materials) and not only to incremental improvement.

## Problem 10. Company A vs Company B: report vs performance (Lecture 10) 📘 + 📗 data ⭐⭐
Lecture 10 asks *"Which company would be more profitable after 10 years?"* Company A has an excellent sustainability report, beautiful graphics, ambitious targets and a strong narrative. Company B has a less attractive report, but: energy ↓ 25%, CO₂ per unit ↓ 30%, water per unit ↓ 20%, supplier violations ↓ 40%, waste-to-landfill ↓ 60%. The slide's answer: *"The report is not the performance. Measure performance first, report performance later."*

**Q10.1 Assume both companies started with an energy bill of ₹50 crore, water cost of ₹5 crore, waste disposal of ₹4 crore and 1,00,000 t CO₂e exposed to a carbon price of ₹2,000 per tonne (for example through CBAM on exports) 📗. Estimate Company B's annual and 10-year advantage.**
- Energy: 25% × ₹50 cr = ₹12.5 cr.
- Water: 20% × ₹5 cr = ₹1.0 cr.
- Waste: 60% × ₹4 cr = ₹2.4 cr.
- Carbon cost avoided: 30% × 1,00,000 t × ₹2,000 = ₹6.0 cr.
- **Total ≈ ₹21.9 crore a year, about ₹219 crore over 10 years** (undiscounted, and before counting lower disruption risk from a 40% fall in supplier violations).

**Q10.2 What term describes Company A's risk?**
**Greenwashing**: claims and narrative that run ahead of measured performance. Lecture 10 also names the opposite, **greenhushing**: a company doing real work but under-reporting it to avoid scrutiny (closer to Company B). BRSR Core assurance exists to close this gap.

## Problem 11. Technology Adoption Score and Net Technology Value: Navya Consumer Products (Lecture 9) 📘 + 📗 assumptions ⭐⭐⭐
Lecture 9 exercise: *Navya Consumer Products Ltd., an Indian FMCG company, wants to adopt PROJECT SUSTAIN_X, an AI + IoT + blockchain platform. It operates 5 plants, 20 warehouses, 1,500 suppliers, 8,000 distributors and 50,000 retail outlets. Costs: ₹80 crore initial investment, ₹12 crore per year operating cost, plus supplier training, cybersecurity, data integration and technology dependence. Expected benefits: inventory −15%, transport cost −8%, product waste −20%, forecast accuracy +15%, traceability and supplier visibility "major improvement". Use five criteria (financial return, environmental benefit, social impact, supply-chain resilience, technology/adoption risk). Should it ADOPT, PILOT or REJECT?*

The case gives no base values, so assume (📗, state them in the exam): average inventory ₹400 crore with a 20% annual carrying cost; annual transport spend ₹300 crore; product waste worth ₹50 crore a year; lifecycle sustainability cost (IoT device manufacture and e-waste, data-centre and blockchain energy) ₹2 crore a year; expected risk cost (cyber incident, adoption failure among small suppliers) ₹4 crore a year; discount rate 12%; 5-year horizon.

**Q11.1 Compute gross annual benefits.**
- Inventory: 15% × ₹400 cr = ₹60 cr less inventory; carrying-cost saving = ₹60 cr × 20% = **₹12 cr a year** (plus a one-time working-capital release of ₹60 cr).
- Transport: 8% × ₹300 cr = **₹24 cr a year**.
- Waste: 20% × ₹50 cr = **₹10 cr a year**.
- **Gross benefits = ₹46 crore a year** (forecast accuracy and traceability benefits are mostly captured in these lines or are strategic, so do not double count them).

**Q11.2 Compute Net Technology Value (Lecture 9 formula).**
- Annual net = Gross benefits − Operating cost − Lifecycle sustainability cost − Risk cost = 46 − 12 − 2 − 4 = **₹28 crore a year**.
- Simple 5-year NTV = 5 × 46 − 80 − 5 × (12 + 2 + 4) = 230 − 80 − 90 = **₹60 crore**.
- NPV at 12% = 28 × 3.605 − 80 = **₹20.9 crore** (₹80.9 crore if the ₹60 crore working-capital release is counted).
- Payback = 80 ÷ 28 = **2.9 years**.

**Q11.3 Sensitivity: what if only 60% of the benefits are realised? What is the break-even realisation?**
- At 60%: annual net = 0.6 × 46 − 18 = ₹9.6 cr → NPV = 9.6 × 3.605 − 80 = **−₹45.4 crore**.
- Break-even: net × 3.605 = 80 → net = ₹22.2 cr → gross needed = 22.2 + 18 = ₹40.2 cr → **87% of the promised benefits**.
The project is positive only if almost all the promised benefits arrive.

**Q11.4 Score it on TAS (1–5).**

| Dimension | Weight | Score | Reason | Weighted |
|---|---|---|---|---|
| Economic | 25% | 4 | NPV positive, 2.9-year payback, but sensitive | 1.00 |
| Environmental | 25% | 4 | Less waste, fewer truck km, less over-production; but device and data-centre footprint | 1.00 |
| Social | 20% | 3 | Traceability helps consumers; risk of excluding small suppliers and distributors who cannot adopt (Lecture 9 trade-off #5: digital inclusion vs supplier exclusion) | 0.60 |
| Resilience | 15% | 4 | Supplier visibility and better forecasts; new cyber and vendor-dependence risk | 0.60 |
| Strategic fit | 15% | 4 | Fits FMCG need for traceability and BRSR data | 0.60 |
| **TAS** | | | | **3.80 / 5** |

**Q11.5 Recommendation.**
**PILOT, not full adoption and not rejection.** TAS of 3.8 and a positive NPV put the project in the **"Prioritise"** quadrant on paper, but the 87% break-even realisation, the complexity of 1,500 suppliers and 8,000 distributors, and Lecture 9's warning that *"technology is an enabler, not a sustainability strategy"* call for proof first. Pilot in one plant, about four warehouses and the top 200–300 suppliers (perhaps ₹10–15 crore) for 9–12 months, with stage-gate KPIs: inventory days, transport cost per case, waste %, forecast MAPE, supplier onboarding rate and system energy use. Fund supplier training so smaller suppliers are not excluded. Scale up only if the pilot delivers at least 85–90% of the promised benefits. *"Don't digitise the problem — transform it sustainably."*

## Problem 12. The technology–sustainability decision matrix (Lecture 9) 📘 + 📗 data ⭐⭐
Lecture 9's matrix: **low business value + low sustainability impact = Avoid; low business value + high sustainability impact = Reconsider; high business value + low sustainability impact = Optimise; high business value + high sustainability impact = Prioritise.**

A retailer scores six technologies (1–5, cut-off 3 = "high"):

| Technology | Business value | Sustainability impact |
|---|---|---|
| AI route optimisation | 5 | 4 |
| Blockchain traceability for all SKUs | 2 | 4 |
| Warehouse robotics | 4 | 2 |
| IoT cold-chain sensors | 4 | 4 |
| Metaverse showroom | 2 | 1 |
| Solar + battery at DCs | 3 | 5 |

**Q12.1 Place each in the matrix.**
- Prioritise: AI route optimisation, IoT cold-chain sensors, solar + battery at DCs.
- Optimise (good business case, improve its sustainability side): warehouse robotics (check its energy use and job effects).
- Reconsider (sustainability benefit but weak business case; redesign the scope, for example only high-risk SKUs like seafood or mangoes as in the Walmart–IBM pilot, 7 days → 2.2 seconds): blockchain for all SKUs.
- Avoid: metaverse showroom.

**Q12.2 Compute TAS for AI route optimisation with scores Economic 5, Environmental 4, Social 3, Resilience 3, Strategic fit 4.**
TAS = 0.25 × 5 + 0.25 × 4 + 0.20 × 3 + 0.15 × 3 + 0.15 × 4 = 1.25 + 1.00 + 0.60 + 0.45 + 0.60 = **3.90**.

## Problem 13. Make a KPI SMART and run the five tests (Lecture 10) 📘 ⭐⭐
Lecture 10's five tests for a KPI set: **material, balanced, actionable, comparable, credible.** Its closing line: *"If a KPI does not change a decision, question why it exists."*

**Q13.1 Rewrite "Be more sustainable in logistics" as a SMART KPI.**
"Reduce outbound transport emissions from 146 to 110 g CO₂e per tonne-km (−25%) across all four DCs by 31 March 2028, measured monthly from fuel cards and the TMS, owned by the Head of Logistics." This is Specific (outbound, g/t-km), Measurable (fuel and TMS data), Achievable (consolidation and modal shift), Relevant (transport is a major Scope 1/3 source) and Time-bound (March 2028).

**Q13.2 A company tracks "number of trees planted" as its main climate KPI. Apply the five tests.**
It fails **material** (it does not measure the company's own emissions hotspots), **actionable** (it does not tell operations what to change), **comparable** (peers report tCO₂e per unit, not trees) and **credible** (survival and permanence of the trees is uncertain). Replace it with Scope 1 + 2 intensity, Scope 3 Category 1 and 4 emissions and a renewable-electricity %, and keep tree planting as a separate offset activity with verified survival rates.

---

## Practice set 📗

**Q14. A DC shipped 3,600 orders: 3,420 on time, 3,456 in full, 3,330 on time and in full; 3,564 damage-free; 3,582 with correct documents. Compute OTIF and an approximate perfect-order rate.**
OTIF = 3,330 ÷ 3,600 = **92.5%**. Perfect order ≈ 0.925 × (3,564 ÷ 3,600) × (3,582 ÷ 3,600) = 0.925 × 0.99 × 0.995 = **91.1%**.

**Q15. A line has 450 minutes planned, 45 minutes downtime, ideal cycle time 1.2 minutes, 300 units produced, 285 good. Compute OEE.**
Availability = 405 ÷ 450 = 90.0%; performance = (1.2 × 300) ÷ 405 = 88.9%; quality = 285 ÷ 300 = 95.0%. **OEE = 0.90 × 0.889 × 0.95 = 76.0%.**

**Q16. A firm with 1,800 employees each working 2,200 hours recorded 3 lost-time injuries. Compute LTIFR. If the target is 0.50, what is the achievement ratio?**
Hours = 39,60,000. LTIFR = 3 × 10,00,000 ÷ 39,60,000 = **0.76**. Achievement (lower is better) = 0.50 ÷ 0.76 = **0.66**, which is red.

**Q17. Water intensity is 3.2 kL per tonne and the benchmark is 2.0. What constant annual reduction closes the gap in 4 years?**
(2.0 ÷ 3.2)^(1/4) = 0.625^0.25 = 0.889 → **11.1% a year.**

**Q18. A technology scores Economic 3, Environmental 5, Social 4, Resilience 2, Strategic fit 3. Compute TAS. Gross benefits are ₹18 crore a year, adoption cost ₹40 crore (5-year life, straight-line ₹8 crore a year), lifecycle sustainability cost ₹1 crore a year and risk cost ₹3 crore a year. Compute annual Net Technology Value.**
TAS = 0.75 + 1.25 + 0.80 + 0.30 + 0.45 = **3.55**. Annual NTV = 18 − 8 − 1 − 3 = **₹6 crore a year** (₹30 crore over 5 years), so it is worth adopting, with a resilience plan because resilience scored only 2.

**Q19. A plant's defect rate falls from 3% to 1.5% on 8,00,000 units. Each defect costs ₹400 and 6 kg CO₂e. Compute the savings.**
Defects avoided = (0.03 − 0.015) × 8,00,000 = 12,000. Savings = 12,000 × ₹400 = **₹48 lakh** and 12,000 × 6 = **72 t CO₂e a year**.

**Q20. Revenue grew from ₹1,800 crore to ₹2,250 crore while Scope 1 + 2 emissions rose from 12,600 t to 13,500 t. Did the company improve?**
Absolute emissions rose 7.1%, but intensity fell from 7.0 to 6.0 t per ₹ crore, a **14.3% improvement**. The company decoupled growth from emissions *relatively*, not absolutely. A net-zero or SBTi target requires absolute reductions, so the answer is "improved efficiency, not yet on a net-zero path".
