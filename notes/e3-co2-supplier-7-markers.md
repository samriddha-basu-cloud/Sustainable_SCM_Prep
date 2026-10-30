# CO2 · 7-Mark Numericals: Weighted Scoring of Suppliers
**What the exam asks (teacher's importants):** *weighted scoring of suppliers, 7 marks. No TOPSIS, only the weighted-average method. Select the best supplier on the weighted average and give a conclusion on why that supplier was selected.*

So every question below is the same shape: **criteria + weights → score × weight → total → rank → select → conclusion (why this supplier)**. Q1–Q3 come from the course material (Lecture 6) 📘; Q4–Q6 are practice questions in the same style 📗. Turn on **Self-test** (`T`) to hide the answers.

> **TOPSIS is not in the exam** (teacher's note). It stays on [P1 Supplier Selection](p1-supplier-selection-numericals.md) for reference only; do not spend revision time on it.

---

## The 7-mark answer template ⭐⭐⭐
| Step | What to write | Marks |
|---|---|---|
| 1. Criteria and weights | Table of criteria, weights (must total **100%** or **1.00**), scoring scale (1–10 or /100) | 1 |
| 2. Formula | **Weighted score = Σ (Weight × Score)** | 0.5 |
| 3. Working | One row per criterion: weight × score for every supplier | 2.5 |
| 4. Total and rank | Total per supplier, rank highest to lowest, **select the highest** | 1 |
| 5. Conclusion: why selected | Where the winner is strong (name the criteria with the biggest weighted contribution), its weakness, how close the runner-up is, and a sustainability reason (carbon, safety, compliance) | 2 |

**If raw data are given** (₹ price, defect %, kg CO₂, days), convert to scores first: lower-is-better → **score = (best ÷ actual) × 10**; higher-is-better → **score = (actual ÷ best) × 10**.

**Conclusion phrases that earn marks:** *"highest weighted score"*, *"best balance across cost, quality, delivery and sustainability"*, *"lowest price is not the lowest total cost"*, *"strong on the heavily weighted criteria"*, *"lower carbon footprint reduces our Scope 3 (Category 1) emissions"*, *"retain the runner-up as a second source / develop it"*.

---

## Q1 (7 marks). Weighted score model: Suppliers A, B, C (Lecture 6, slide 24) 📘 ⭐⭐⭐ 🎯
| Criteria | Weight | A | B | C |
|---|---|---|---|---|
| Price | 25% | 8 | 7 | 9 |
| Quality | 20% | 9 | 8 | 7 |
| Delivery | 15% | 7 | 9 | 8 |
| Carbon | 15% | 8 | 6 | 9 |
| Safety | 10% | 9 | 8 | 7 |
| Innovation | 10% | 7 | 9 | 8 |
| Compliance | 5% | 9 | 8 | 9 |

Select the best supplier using the weighted-average method and justify your selection.

**Q1.1 Weighted scores. [4 marks]**
| Criteria (w) | A | B | C |
|---|---|---|---|
| Price (0.25) | 8 × 0.25 = 2.00 | 7 × 0.25 = 1.75 | 9 × 0.25 = 2.25 |
| Quality (0.20) | 9 × 0.20 = 1.80 | 8 × 0.20 = 1.60 | 7 × 0.20 = 1.40 |
| Delivery (0.15) | 7 × 0.15 = 1.05 | 9 × 0.15 = 1.35 | 8 × 0.15 = 1.20 |
| Carbon (0.15) | 8 × 0.15 = 1.20 | 6 × 0.15 = 0.90 | 9 × 0.15 = 1.35 |
| Safety (0.10) | 9 × 0.10 = 0.90 | 8 × 0.10 = 0.80 | 7 × 0.10 = 0.70 |
| Innovation (0.10) | 7 × 0.10 = 0.70 | 9 × 0.10 = 0.90 | 8 × 0.10 = 0.80 |
| Compliance (0.05) | 9 × 0.05 = 0.45 | 8 × 0.05 = 0.40 | 9 × 0.05 = 0.45 |
| **Total (/10)** | **8.10** | **7.70** | **8.15** |
| **Rank** | 2 | 3 | **1** |

**Q1.2 Conclusion: which supplier and why? [3 marks]**
**Select Supplier C (8.15 / 10).**
- C scores highest on the **most heavily weighted criterion, price (9 → 2.25)**, and on **carbon (9 → 1.35)**, the joint second-largest sustainability weight; it is also top on compliance.
- C is good, not best, on quality (7) and safety (7), but these are outweighed by its price and carbon strength.
- It is the **best balance of economic and environmental performance**: choosing C also lowers our purchased-goods (Scope 3, Category 1) emissions.
- A is a close second (8.10, only 0.05 behind) with the best quality and safety: keep **A as the second source** and ask C for a quality and safety improvement plan. B (7.70) is last because of the highest carbon (6).

---

## Q2 (7 marks). Supplier scorecard: VoltTech Components (Lecture 6, slide 22) 📘 ⭐⭐⭐ 🎯
Scores out of 100: Price 88 (25%), Quality 90 (20%), Delivery 85 (15%), Carbon 80 (15%), Safety 92 (10%), Innovation 78 (10%), Compliance 95 (5%). Rating bands: 90–100 A (Excellent), 75–89 B (Good), 60–74 C (Average), below 60 D (Poor).
Compute the weighted score, rate the supplier, and conclude whether to continue with VoltTech.

**Q2.1 Weighted score. [4 marks]**
| Criteria | Weight × Score | Weighted |
|---|---|---|
| Price | 0.25 × 88 | 22.00 |
| Quality | 0.20 × 90 | 18.00 |
| Delivery | 0.15 × 85 | 12.75 |
| Carbon | 0.15 × 80 | 12.00 |
| Safety | 0.10 × 92 | 9.20 |
| Innovation | 0.10 × 78 | 7.80 |
| Compliance | 0.05 × 95 | 4.75 |
| **Total** | | **86.50 / 100 → Band B (Good)** |
(The slide's header shows "86.2, A". The table adds to 86.50, which falls in band B; write 86.50 and B.)

**Q2.2 Conclusion. [3 marks]**
**Continue with VoltTech as a preferred supplier.** It is strong on compliance (95), safety (92) and quality (90), and its score has risen every quarter (78.4 → 86.2). Its weakest areas are **innovation (78)** and **carbon (80)**: raising carbon to 90 adds 1.5 points and innovation to 88 adds 1.0, which would take it to 89.0, close to band A. Agree a carbon-reduction plan (renewable electricity, recycled copper) and joint innovation workshops.

---

## Q3 (7 marks). Laptop manufacturer: three battery-pack suppliers (Lecture 6 exercise, slide 32) 📘 + assumed data 📗 ⭐⭐⭐ 🎯
*"For a laptop manufacturing company, evaluate three suppliers using Price, Quality, Carbon, Safety, Innovation."* Assumed raw data:

| Supplier | Price (₹/pack) | Defects (ppm) | Carbon (kg CO₂e/pack) | Safety (LTIFR) | Innovation (patents) |
|---|---|---|---|---|---|
| P | 42,000 | 450 | 95 | 0.8 | 6 |
| Q | 45,000 | 200 | 70 | 0.4 | 9 |
| R | 40,000 | 900 | 120 | 1.5 | 3 |
Weights: Price 30%, Quality 25%, Carbon 20%, Safety 15%, Innovation 10%.

**Q3.1 Convert to scores and compute weighted totals. [4 marks]**
Lower-is-better (price, defects, carbon, LTIFR): (best ÷ actual) × 10. Higher-is-better (patents): (actual ÷ best) × 10.
| Criterion (w) | P | Q | R |
|---|---|---|---|
| Price (0.30) | 9.52 → 2.86 | 8.89 → 2.67 | 10.00 → 3.00 |
| Quality (0.25) | 4.44 → 1.11 | 10.00 → 2.50 | 2.22 → 0.56 |
| Carbon (0.20) | 7.37 → 1.47 | 10.00 → 2.00 | 5.83 → 1.17 |
| Safety (0.15) | 5.00 → 0.75 | 10.00 → 1.50 | 2.67 → 0.40 |
| Innovation (0.10) | 6.67 → 0.67 | 10.00 → 1.00 | 3.33 → 0.33 |
| **Total (/10)** | **6.86** | **9.67** | **5.46** |

**Q3.2 Conclusion. [3 marks]**
**Select Supplier Q (9.67).** Q is the **best on four of five criteria** (quality, carbon, safety, innovation) and loses only on price, where it is 12.5% dearer than R. For a battery pack, low defects and good safety matter because one battery fire or recall costs far more than the price difference; lowest carbon (70 kg vs 120 kg) cuts our Scope 3. R is cheapest but worst on quality, carbon and safety: *"lowest price is not the lowest total cost."* Keep P (6.86) as a 20–30% second source with a quality-improvement plan.

---

## Q4 (7 marks). Packaging suppliers from raw data 📗 ⭐⭐⭐
| Criterion (weight) | Better | P | Q | R |
|---|---|---|---|---|
| Price ₹/unit (30%) | Lower | 42 | 38 | 45 |
| Defect rate % (20%) | Lower | 1.2 | 2.0 | 0.8 |
| CO₂ kg/unit (20%) | Lower | 0.80 | 1.10 | 0.60 |
| Lead time days (10%) | Lower | 10 | 7 | 14 |
| Recycled content % (20%) | Higher | 30 | 20 | 50 |
Select the best supplier by weighted average and justify.

**Q4.1 Scores and weighted totals. [4 marks]**
| Criterion (w) | P | Q | R |
|---|---|---|---|
| Price (0.30) | 38/42 × 10 = 9.05 → 2.71 | 10.00 → 3.00 | 38/45 × 10 = 8.44 → 2.53 |
| Defects (0.20) | 0.8/1.2 × 10 = 6.67 → 1.33 | 4.00 → 0.80 | 10.00 → 2.00 |
| CO₂ (0.20) | 0.6/0.8 × 10 = 7.50 → 1.50 | 5.45 → 1.09 | 10.00 → 2.00 |
| Lead time (0.10) | 7/10 × 10 = 7.00 → 0.70 | 10.00 → 1.00 | 5.00 → 0.50 |
| Recycled (0.20) | 30/50 × 10 = 6.00 → 1.20 | 4.00 → 0.80 | 10.00 → 2.00 |
| **Total (/10)** | **7.45** | **6.69** | **9.03** |

**Q4.2 Conclusion. [3 marks]**
**Select Supplier R (9.03).** R is the most expensive (₹45, 18% above Q) but it is **best on defects, CO₂ and recycled content**, which together carry 60% of the weight. Its 50% recycled content helps meet India's **EPR plastic-packaging targets**, and the lowest CO₂ reduces our Scope 3. Q is cheapest but has 2.5 times R's defect rate, which means rework, returns and waste. Manage R's longer 14-day lead time with buffer stock or vendor-managed inventory; keep P (7.45) as the second source.

---

## Q5 (7 marks). EV battery-cell suppliers: four suppliers, sustainability criteria included 📗 ⭐⭐⭐
Scores out of 10:
| Criteria | Weight | S1 | S2 | S3 | S4 |
|---|---|---|---|---|---|
| Price | 25% | 9 | 7 | 8 | 6 |
| Quality | 20% | 7 | 9 | 8 | 8 |
| Delivery | 15% | 8 | 8 | 6 | 9 |
| Carbon footprint | 15% | 5 | 8 | 9 | 7 |
| Renewable energy use | 10% | 4 | 7 | 9 | 8 |
| Labour & safety | 10% | 7 | 8 | 6 | 9 |
| Traceability (minerals) | 5% | 6 | 8 | 7 | 9 |
Select the best supplier and justify. Would the choice change if the firm were cost-led (price 35%, carbon 10%, renewable energy 5%)?

**Q5.1 Weighted scores. [4 marks]**
| Criteria (w) | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| Price (0.25) | 2.25 | 1.75 | 2.00 | 1.50 |
| Quality (0.20) | 1.40 | 1.80 | 1.60 | 1.60 |
| Delivery (0.15) | 1.20 | 1.20 | 0.90 | 1.35 |
| Carbon (0.15) | 0.75 | 1.20 | 1.35 | 1.05 |
| RE use (0.10) | 0.40 | 0.70 | 0.90 | 0.80 |
| Labour & safety (0.10) | 0.70 | 0.80 | 0.60 | 0.90 |
| Traceability (0.05) | 0.30 | 0.40 | 0.35 | 0.45 |
| **Total (/10)** | **7.00** | **7.85** | **7.70** | **7.65** |
| **Rank** | 4 | **1** | 2 | 3 |
Cost-led weights: S1 7.45, **S2 7.80**, S3 7.60, S4 7.50 → **S2 still wins**.

**Q5.2 Conclusion. [3 marks]**
**Select S2 (7.85).** S2 has **no weak criterion** (every score 7 or above), the **best quality (9)**, which is critical for cell safety, and strong carbon (8) and traceability (8). It stays first even under cost-led weights, so the choice is **robust**. S1 is cheapest but has the worst carbon (5) and renewable-energy use (4), which would raise our Scope 3 and risk failing EU battery-regulation carbon and due-diligence rules. S3 (7.70) is the greenest and a good second source for the low-carbon product line.

---

## Q6 (7 marks). Weighted score with a minimum threshold: the 95-score supplier with labour violations (Lecture 10, slide 12) 📘 + assumed scores 📗 ⭐⭐ 🎯
Lecture 10 weights: cost 20, quality 20, delivery 15, environmental 15, labour & human rights 10, carbon reduction 10, governance 5, innovation 5. Supplier X: 95, 95, 95, 60, **10** (serious labour violations), 50, 40, 70. Supplier Y: 80, 85, 85, 80, 85, 75, 80, 70.
Select a supplier by weighted average, and comment on the slide's question: *should a supplier that scores 95 on cost, quality and delivery but has serious labour violations be retained?*

**Q6.1 Weighted scores. [4 marks]**
X = 0.20×95 + 0.20×95 + 0.15×95 + 0.15×60 + 0.10×10 + 0.10×50 + 0.05×40 + 0.05×70 = 19.00 + 19.00 + 14.25 + 9.00 + 1.00 + 5.00 + 2.00 + 3.50 = **72.75**.
Y = 16.00 + 17.00 + 12.75 + 12.00 + 8.50 + 7.50 + 4.00 + 3.50 = **81.25**.

**Q6.2 Conclusion. [3 marks]**
**Select Supplier Y (81.25).** Y is balanced across all eight dimensions, while X's high cost-quality-delivery scores hide very poor labour (10), governance (40) and carbon (50). Even so, X still scores 72.75 because labour carries only 10%, so a pure weighted average can **compensate** for a human-rights failure. Add a **minimum threshold** (any supplier below 50 on labour, safety or compliance is not eligible), suspend new orders to X pending an independent audit and corrective action, and grow Y. *"Do not outsource sustainability."*

---

## From the course material: where to practise more 🎯
| Exam-type item | Source | Page |
|---|---|---|
| Weighted score A/B/C (+ sensitivity) | Lecture 6, slide 24 📘 | [P1 Problem 1](p1-supplier-selection-numericals.md) |
| VoltTech scorecard | Lecture 6, slide 22 📘 | [P1 Problem 2](p1-supplier-selection-numericals.md) |
| Supplier sustainability scorecard (Lecture 10 weights) | Lecture 10, slide 12 📘 | [P1 Problem 5](p1-supplier-selection-numericals.md) |
| Laptop supplier exercise | Lecture 6, slide 32 📘 | [P1 Problem 6](p1-supplier-selection-numericals.md) |
| Practice Q10–Q11 (packaging, VoltTech-weights) | 📗 | [P1 Practice set](p1-supplier-selection-numericals.md) |
| Theory: ESG + RTI criteria, lowest price vs TCO | Lecture 6 📘 | [Sustainable Procurement](ch03-sustainable-procurement.md) |
