# CO5 · 7-Mark Numericals: SSCM Effective Performance Measurement Systems
Your teacher's pattern: **CO5 = 7 marks, a numerical on SSCM effective performance measurement systems**. Expect KPI calculations (OTIF, fill rate, perfect order, OEE, carbon and energy intensity, LTIFR), a scorecard or dashboard with targets, and an interpretation part (leading vs lagging, SMART, the five tests). This page has six full 7-mark questions with marks splits and model answers. Q3 and Q5 build on the course's own Lecture 3 dashboard and Lecture 9 TAS/NTV 📘; the rest are practice questions in the same style 📗. Turn on **Self-test** (`T`) to hide the answers.

Full theory and more problems: [Performance Measurement Numericals](p4-performance-measurement-numericals.md) · [Measuring SSCM Performance](ch08-performance-measurement.md).

---

## How a 7-mark performance answer earns its marks ⭐⭐⭐
| Step | What to write | Marks it usually carries |
|---|---|---|
| 1. Formula | The KPI definition, in words or symbols | 1 |
| 2. Calculate | Substitution and value with units (%, per unit, per million hours) | 3 |
| 3. Compare | Against target or benchmark: achievement = actual ÷ target (higher-better) or target ÷ actual (lower-better) | 1 |
| 4. Interpret | Leading or lagging, root cause, owner, the decision it changes | 1–2 |
| 5. Improve | One corrective action per weak KPI | 1 |

**Formulas:** OTIF = orders on time **and** in full ÷ total orders · fill rate = units shipped ÷ units ordered · perfect order ≈ OTIF × damage-free × correct documents · **OEE = Availability × Performance × Quality** · carbon intensity = t CO₂e ÷ output or ÷ ₹ crore · **LTIFR = lost-time injuries × 10⁶ ÷ person-hours** · composite index = Σ weight × capped achievement · required annual improvement = 1 − (target ÷ current)^(1/n) · **TAS** = 0.25 Econ + 0.25 Env + 0.20 Social + 0.15 Resilience + 0.15 Strategic fit · **NTV** = gross benefits − adoption cost − lifecycle sustainability cost − risk cost.

---

## Q1 (7 marks). Customer service KPIs for a DC 📗 ⭐⭐⭐
In a month a DC shipped **1,200 orders**: 1,104 on time, 1,140 in full, **1,068 both on time and in full**, 1,182 damage-free and 1,188 with correct documents. Customers ordered 36,000 units; 35,100 were shipped from stock.
(a) Compute on-time %, in-full %, OTIF %, fill rate and perfect-order rate. (4) (b) Why is OTIF not equal to OT% × IF%? (1) (c) Interpret and suggest actions. (2)

**Q1.1 (a) KPIs. [4 marks]**
On-time = 1,104 ÷ 1,200 = **92.0%** · In-full = 1,140 ÷ 1,200 = **95.0%** · **OTIF = 1,068 ÷ 1,200 = 89.0%** · Fill rate = 35,100 ÷ 36,000 = **97.5%** · Perfect order = 0.890 × (1,182 ÷ 1,200) × (1,188 ÷ 1,200) = 0.890 × 0.985 × 0.990 = **86.8%** (assuming damage and documents are independent of OTIF).

**Q1.2 (b) OTIF vs the product. [1 mark]**
92.0% × 95.0% = 87.4%, but the actual joint count is 89.0% because late orders and short orders often **overlap** (the same problem orders fail both). Always use the joint count when it is given.

**Q1.3 (c) Interpretation. [2 marks]**
Fill rate (97.5%) looks excellent, but **more than one order in eight is not perfect**: each failure means a re-delivery trip, a return or damaged goods, which is a cost *and* an emissions problem. Lateness is the biggest gap (8% late): fix dispatch cut-offs and carrier reliability; then packaging (1.5% damage) and invoicing errors. Report **OTIF and perfect order**, not fill rate alone.

---

## Q2 (7 marks). OEE, intensity and safety for a plant 📗 ⭐⭐⭐
A plant runs **two 8-hour shifts** (960 minutes planned). Breakdowns and changeovers take **90 minutes**. Ideal cycle time is **1.2 minutes** per unit; the day's output was **700 units**, of which **665 were good**. Annual data: 9,600 t CO₂e (Scope 1 + 2), 4.8 lakh units, revenue ₹1,200 crore, energy 52,000 GJ, water 1,44,000 kL, 1,500 employees × 2,000 hours, 3 lost-time injuries.
(a) Compute OEE. (3) (b) Compute carbon, energy and water intensity and LTIFR. (3) (c) Interpret. (1)

**Q2.1 (a) OEE. [3 marks]**
Run time = 960 − 90 = 870 min. Availability = 870 ÷ 960 = **90.6%**. Performance = (1.2 × 700) ÷ 870 = 840 ÷ 870 = **96.6%**. Quality = 665 ÷ 700 = **95.0%**. **OEE = 0.906 × 0.966 × 0.950 = 83.1%**, just below the ~85% world-class benchmark.

**Q2.2 (b) Intensity and safety. [3 marks]**
Carbon = 9,600 ÷ 1,200 = **8.0 t CO₂e per ₹ crore**, or 96,00,000 kg ÷ 4,80,000 = **20 kg per unit**. Energy = 52,000 GJ ÷ 4,80,000 = **108 MJ per unit**. Water = 1,44,000 kL ÷ 4,80,000 = **0.30 kL (300 litres) per unit**. **LTIFR = 3 × 10⁶ ÷ (1,500 × 2,000) = 3 × 10⁶ ÷ 30,00,000 = 1.0** per million hours.

**Q2.3 (c) Interpretation. [1 mark]**
The biggest OEE loss is **availability** (90.6%): predictive maintenance and SMED changeovers would raise output *and* cut idle energy. The 5% scrap is also an environmental loss (materials, energy, landfill): *quality failure = environmental failure*. Normalised intensities let the plant compare itself across years and with peers even as volume grows.

---

## Q3 (7 marks). Reading the Lecture 3 dashboard 📘 ⭐⭐⭐
Lecture 3's dashboard shows: CO₂ per t-km **62.3** (8.7% below target), LTIFR **0.68** (15% below target), on-time delivery **96.2%** (+3.2 points), cost per shipment **$96.4** (3.6% below target). Trend Jan → Jun: CO₂/t-km about 78 → 62.3; LTIFR about 1.4 → 0.68.
(a) Back-calculate the four targets. (3) (b) Compute the six-month improvement in CO₂/t-km and LTIFR. (2) (c) All KPIs are green: is that good news? (2)

**Q3.1 (a) Targets. [3 marks]**
CO₂/t-km target = 62.3 ÷ (1 − 0.087) = **68.2 g**. LTIFR target = 0.68 ÷ 0.85 = **0.80**. On-time target = 96.2 − 3.2 = **93.0%**. Cost target = 96.4 ÷ 0.964 = **$100**. (Assumption: % variance on an absolute KPI = relative change; on a % KPI = percentage points.)

**Q3.2 (b) Improvement. [2 marks]**
CO₂/t-km: (78 − 62.3) ÷ 78 = **≈ 20% reduction**. LTIFR: (1.4 − 0.68) ÷ 1.4 = **≈ 51% reduction**. Both came with better delivery and margin: sustainability and business performance moved together.

**Q3.3 (c) All green? [2 marks]**
Not necessarily. All 24 KPIs beating target suggests **soft targets** (set from last year's actuals) or easy KPIs: the **KPI trap**. Compare with **external benchmarks** or science-based targets, not only internal targets; check that each KPI has an owner and changes a decision; and apply the **five tests** (material, balanced, actionable, comparable, credible).

---

## Q4 (7 marks). Sustainability balanced scorecard with a composite index 📗 ⭐⭐⭐
| KPI | Actual | Target | Better | Weight |
|---|---|---|---|---|
| Logistics cost % of sales | 8.4 | 8.0 | Lower | 20% |
| OTIF % | 94.0 | 95.0 | Higher | 20% |
| CO₂ kg per unit | 1.80 | 2.00 | Lower | 20% |
| Renewable energy share % | 45 | 40 | Higher | 15% |
| Waste recycled % | 72 | 80 | Higher | 10% |
| LTIFR | 0.50 | 0.40 | Lower | 15% |

(a) Compute each achievement ratio (cap 1.2) and the composite index. (4) (b) Interpret. (2) (c) Classify each KPI as leading or lagging. (1)

**Q4.1 (a) Ratios and index. [4 marks]**
| KPI | Ratio | × weight |
|---|---|---|
| Logistics cost | 8.0 ÷ 8.4 = 0.952 | 0.190 |
| OTIF | 94 ÷ 95 = 0.989 | 0.198 |
| CO₂/unit | 2.00 ÷ 1.80 = 1.111 | 0.222 |
| RE share | 45 ÷ 40 = 1.125 | 0.169 |
| Waste recycled | 72 ÷ 80 = 0.900 | 0.090 |
| LTIFR | 0.40 ÷ 0.50 = 0.800 | 0.120 |
| **Composite index** | | **0.989 (98.9%)** |

**Q4.2 (b) Interpretation. [2 marks]**
The index is close to target, but it **hides that four of six KPIs miss target**, including **safety (LTIFR 25% worse)**, the worst result. Strong carbon and renewable figures offset it. Fix: a **minimum threshold** for safety and human-rights KPIs (red regardless of the index) and reporting by perspective, not one number. Actions: safety walks and near-miss reporting, segregated waste streams with recycler contracts, route consolidation for logistics cost.

**Q4.3 (c) Leading vs lagging. [1 mark]**
Lagging: logistics cost %, OTIF, CO₂/unit, waste recycled, LTIFR (results). Leading: **renewable energy share** (drives future CO₂). Add leading KPIs such as safety-training hours and supplier audits completed.

---

## Q5 (7 marks). Technology Adoption Score and Net Technology Value (Lecture 9 method) 📘 + 📗 ⭐⭐⭐
A logistics firm evaluates an IoT + AI route-optimisation system: investment **₹12 crore**; gross benefits **₹6.5 crore a year** (fuel, fewer trips, less waste); operating cost ₹1.2 crore; lifecycle sustainability cost (devices, e-waste, data-centre energy) ₹0.3 crore; expected risk cost (cyber, adoption failure) ₹0.5 crore a year; 5 years at 10%. Scores (1–5): economic 4, environmental 5, social 3, resilience 3, strategic fit 4.
(a) Compute TAS. (2) (b) Compute annual NTV, 5-year NPV and payback. (3) (c) Adopt, pilot or reject? (2)

**Q5.1 (a) TAS. [2 marks]**
0.25 × 4 + 0.25 × 5 + 0.20 × 3 + 0.15 × 3 + 0.15 × 4 = 1.00 + 1.25 + 0.60 + 0.45 + 0.60 = **3.90 / 5**.

**Q5.2 (b) NTV, NPV, payback. [3 marks]**
Annual net = 6.5 − 1.2 − 0.3 − 0.5 = **₹4.5 crore**. Annuity factor (10%, 5 yr) = 3.791 → NPV = 4.5 × 3.791 − 12 = **₹5.06 crore**. Simple 5-year NTV = 5 × 4.5 − 12 = **₹10.5 crore**. Payback = 12 ÷ 4.5 = **2.7 years**.

**Q5.3 (c) Decision. [2 marks]**
High business value and high sustainability impact → the **"Prioritise"** quadrant of the decision matrix; TAS 3.9 and a positive NPV support **adoption, staged through a short pilot** to confirm the fuel savings (break-even needs net ≥ ₹3.17 crore, i.e. gross ≥ ₹5.17 crore, 80% of promised benefits). Track leading KPIs: km per delivery, utilisation, empty km, g CO₂/t-km, and system energy use. *"Technology is an enabler, not a sustainability strategy."*

---

## Q6 (7 marks). Benchmarking gap and required rate of improvement (Lecture 3) 📗 ⭐⭐
A firm's carbon intensity is **0.95 kg CO₂e per unit**; the best-in-class benchmark is **0.60**. It wants to close the gap in **5 years**.
(a) Compute the gap. (1) (b) Compute the required annual reduction. (2) (c) At the current pace of 6% a year, how long will it take? (2) (d) Write the KPI as a SMART target. (2)

**Q6.1 (a) Gap. [1 mark]**
(0.95 − 0.60) ÷ 0.60 = **58.3% above the benchmark**.

**Q6.2 (b) Required annual reduction. [2 marks]**
1 − (0.60 ÷ 0.95)^(1/5) = 1 − 0.9122 = **8.8% a year** (compounded).

**Q6.3 (c) At 6% a year. [2 marks]**
n = ln(0.60 ÷ 0.95) ÷ ln(0.94) = (−0.4595) ÷ (−0.0619) = **≈ 7.4 years**: the current pace is about 2.4 years too slow.

**Q6.4 (d) SMART target. [2 marks]**
"Reduce **Scope 1 + 2 carbon intensity** from 0.95 to **0.60 kg CO₂e per unit** by **FY 2031** (−8.8% a year), owned by the **plant head**, measured monthly from metered energy data with DEFRA/CEA factors and verified annually under **BRSR Core**." Specific, measurable, achievable (with RE + efficiency), relevant (CBAM and buyer requirements), time-bound.

---

## Quick checklist before you hand in a CO5 answer ⭐⭐⭐
- Formula written **before** the numbers?
- Lower-is-better KPIs inverted (target ÷ actual) in any scorecard?
- Units: %, per unit, per ₹ crore, per **million** person-hours?
- Compared with a **target or benchmark**, not just stated?
- One line on **leading vs lagging**, the **owner** and the **decision** the KPI changes?
- If a composite index looks fine, did you check for **hidden failures** (safety, human rights)?
