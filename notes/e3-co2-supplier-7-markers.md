# CO2 · 7-Mark Numericals: SSCM Supplier Selection Strategies
Your teacher's pattern: **CO2 = 7 marks, a numerical on SSCM supplier selection strategies**. The core is **weighted scoring**, with possible add-ons: a supplier scorecard, normalising raw data, TOPSIS, a risk matrix, total cost of ownership, and an interpretation part. This page has six full 7-mark questions with marks splits and model answers. Q1–Q3 are the course's own Lecture 6 examples 📘; Q4–Q6 are practice questions in the same style 📗. Turn on **Self-test** (`T`) to hide the answers.

Full theory and more problems: [Supplier Selection Numericals](p1-supplier-selection-numericals.md) · [Sustainable Procurement](ch03-sustainable-procurement.md).

---

## How a 7-mark supplier answer earns its marks ⭐⭐⭐
| Step | What to write | Marks it usually carries |
|---|---|---|
| 1. Set-up | Criteria, weights (sum = 100%), scale; say which criteria are **cost** (lower is better) and which **benefit** | 1 |
| 2. Normalise (if raw data) | Benefit: x ÷ max · Cost: min ÷ x (or min–max) | 1 |
| 3. Weighted totals | **Σ (weight × score)** per supplier in a table | 2–3 |
| 4. Rank + recommend | Highest total wins; name the runner-up | 1 |
| 5. Interpret | Sensitivity (does a weight change flip it?), knock-out criteria (human rights, safety), development plan | 1–2 |

Lecture 6's selection criteria: **"ESG + RTI"** (Environmental, Social, Governance + Risk, Technology, Innovation). Tools: weighted scoring, AHP, **TOPSIS**, DEA, linear programming.

---

## Q1 (7 marks). Weighted score model: Suppliers A, B, C (Lecture 6, slide 24) 📘 ⭐⭐⭐
| Criteria | Weight | A | B | C |
|---|---|---|---|---|
| Price | 25% | 8 | 7 | 9 |
| Quality | 20% | 9 | 8 | 7 |
| Delivery | 15% | 7 | 9 | 8 |
| Carbon | 15% | 8 | 6 | 9 |
| Safety | 10% | 9 | 8 | 7 |
| Innovation | 10% | 7 | 9 | 8 |
| Compliance | 5% | 9 | 8 | 9 |

(a) Compute the weighted scores and rank. (4) (b) The quality manager wants quality at 30% and carbon at 5%. Re-rank. (2) (c) Interpret. (1)

**Q1.1 (a) Weighted scores and rank. [4 marks]**
| Criteria (w) | A | B | C |
|---|---|---|---|
| Price (0.25) | 2.00 | 1.75 | 2.25 |
| Quality (0.20) | 1.80 | 1.60 | 1.40 |
| Delivery (0.15) | 1.05 | 1.35 | 1.20 |
| Carbon (0.15) | 1.20 | 0.90 | 1.35 |
| Safety (0.10) | 0.90 | 0.80 | 0.70 |
| Innovation (0.10) | 0.70 | 0.90 | 0.80 |
| Compliance (0.05) | 0.45 | 0.40 | 0.45 |
| **Total (/10)** | **8.10** | **7.70** | **8.15** |
Rank: **C (8.15) > A (8.10) > B (7.70) → select C.**

**Q1.2 (b) Quality 30%, carbon 5%. [2 marks]**
A = 8.10 + 0.10 × 9 − 0.10 × 8 = **8.20**; B = 7.70 + 0.8 − 0.6 = **7.90**; C = 8.15 + 0.7 − 0.9 = **7.95**. New rank: **A > C > B**. The winner flips.

**Q1.3 (c) Interpretation. [1 mark]**
C and A are only 0.05 apart, so the decision is **sensitive to the weights**. C wins only if carbon carries real weight; a sustainability-led firm should fix the weights *before* scoring (AHP helps), and could **dual-source** C (main) and A (backup, with a quality-to-carbon development plan).

---

## Q2 (7 marks). Supplier scorecard: VoltTech Components (Lecture 6, slide 22) 📘 ⭐⭐⭐
Scores (/100): Price 88 (25%), Quality 90 (20%), Delivery 85 (15%), Carbon 80 (15%), Safety 92 (10%), Innovation 78 (10%), Compliance 95 (5%). Bands: 90–100 A (Excellent), 75–89 B (Good), 60–74 C (Average), < 60 D (Poor). Trend: 78.4 → 81.2 → 83.6 → 86.2.
(a) Compute the overall score and band. (3) (b) Identify strengths and weaknesses and the gain from fixing the two weakest. (3) (c) Comment on the trend. (1)

**Q2.1 (a) Score and band. [3 marks]**
22.00 + 18.00 + 12.75 + 12.00 + 9.20 + 7.80 + 4.75 = **86.50 / 100 → Band B (Good)**. (The slide's header says "86.2, A": that contradicts its own table and bands. Show 86.50 and B, and note the discrepancy in one line.)

**Q2.2 (b) Strengths, weaknesses, value of improvement. [3 marks]**
Strengths: compliance 95, safety 92, quality 90. Weakest: **innovation 78** and **carbon 80**. Raising carbon to 90 adds 0.15 × 10 = **1.5**; innovation to 88 adds 0.10 × 10 = **1.0** → **89.0**, at the edge of Band A. Actions: a supplier carbon-reduction plan (renewable power, recycled copper, low-carbon PVC) and joint value-engineering workshops.

**Q2.3 (c) Trend. [1 mark]**
+7.8 points in three quarters (+9.9%), ≈ 2.6 points a quarter: a **developing, improving** supplier to keep and grow, not replace.

---

## Q3 (7 marks). TOPSIS: TMT steel supplier for a building (Lecture 6, slide 25) 📘 ⭐⭐⭐
Price (₹/MT, cost, 0.30), Quality (0.25), Delivery % (0.20), Safety (0.15), Sustainability (0.10). A: 56,000, 8, 92, 9, 7 · B: 52,000, 7, 90, 8, 6 · C: 54,000, 9, 95, 9, 8 · D: 58,000, 6, 88, 7, 7.
(a) State the TOPSIS steps. (1) (b) Compute Cᵢ* and rank. (5) (c) Interpret. (1)

**Q3.1 (a) Steps. [1 mark]**
Normalise rᵢⱼ = xᵢⱼ ÷ √Σx²ᵢⱼ → weight vᵢⱼ = wⱼ·rᵢⱼ → ideal A⁺ (best: min for cost, max for benefit) and anti-ideal A⁻ → distances S⁺, S⁻ → **Cᵢ* = S⁻ ÷ (S⁺ + S⁻)** → rank high to low.

**Q3.2 (b) Computation. [5 marks]**
Column norms: 1,10,090.9 · 15.166 · 182.57 · 16.583 · 14.071.
| Supplier | v (Price, Quality, Delivery, Safety, Sust.) | S⁺ | S⁻ | Cᵢ* |
|---|---|---|---|---|
| A | 0.1526, 0.1319, 0.1008, 0.0814, 0.0497 | 0.0213 | 0.0389 | **0.647** |
| B | 0.1417, 0.1154, 0.0986, 0.0724, 0.0426 | 0.0374 | 0.0250 | **0.401** |
| C | 0.1472, 0.1484, 0.1041, 0.0814, 0.0569 | 0.0055 | 0.0561 | **0.912** |
| D | 0.1581, 0.0989, 0.0964, 0.0633, 0.0497 | 0.0561 | 0.0071 | **0.112** |
A⁺ = (0.1417, 0.1484, 0.1041, 0.0814, 0.0569); A⁻ = (0.1581, 0.0989, 0.0964, 0.0633, 0.0426).
Rank: **C (0.912) > A (0.647) > B (0.401) > D (0.112) → ConstructPro (C).**

**Q3.3 (c) Interpretation. [1 mark]**
C is not the cheapest (B is) but is closest to the ideal on quality, delivery, safety and sustainability: *"lowest price is not the lowest, but balanced with high performance."* (The slide's intermediate numbers are illustrative; its winner is also C.)

---

## Q4 (7 marks). Raw data to weighted score: packaging suppliers 📗 ⭐⭐⭐
| Criterion (weight) | Type | P | Q | R |
|---|---|---|---|---|
| Price ₹/unit (30%) | Cost | 42 | 38 | 45 |
| Defect rate % (20%) | Cost | 1.2 | 2.0 | 0.8 |
| CO₂ kg/unit (20%) | Cost | 0.80 | 1.10 | 0.60 |
| Lead time days (10%) | Cost | 10 | 7 | 14 |
| Recycled content % (20%) | Benefit | 30 | 20 | 50 |

(a) Normalise (cost: min ÷ x; benefit: x ÷ max). (2) (b) Compute weighted scores and rank. (3) (c) Interpret, including the price question. (2)

**Q4.1 (a) Normalised scores. [2 marks]**
| | Price | Defects | CO₂ | Lead | Recycled |
|---|---|---|---|---|---|
| P | 38/42 = 0.905 | 0.8/1.2 = 0.667 | 0.6/0.8 = 0.750 | 7/10 = 0.700 | 30/50 = 0.600 |
| Q | 1.000 | 0.8/2.0 = 0.400 | 0.6/1.1 = 0.545 | 1.000 | 20/50 = 0.400 |
| R | 38/45 = 0.844 | 1.000 | 1.000 | 7/14 = 0.500 | 1.000 |

**Q4.2 (b) Weighted scores. [3 marks]**
P = 0.30×0.905 + 0.20×0.667 + 0.20×0.750 + 0.10×0.700 + 0.20×0.600 = 0.272 + 0.133 + 0.150 + 0.070 + 0.120 = **0.745**.
Q = 0.300 + 0.080 + 0.109 + 0.100 + 0.080 = **0.669**.
R = 0.253 + 0.200 + 0.200 + 0.050 + 0.200 = **0.903**.
Rank: **R (0.903) > P (0.745) > Q (0.669) → select R.**

**Q4.3 (c) Interpretation. [2 marks]**
R is the **most expensive** (₹45, 18% above Q) yet wins clearly because it has the lowest defects, lowest CO₂ and highest recycled content, which also helps with India's **EPR plastic-packaging targets**. Q is cheapest but has 2.5× R's defects: rework, returns and waste make it costlier in **TCO** terms. Manage R's 14-day lead time with a buffer stock or a VMI agreement, and keep P as a second source for resilience.

---

## Q5 (7 marks). Gate + score: should a 95-score supplier with labour violations be kept? (Lecture 10) 📘 + 📗 ⭐⭐⭐
Weights: cost 20, quality 20, delivery 15, environment 15, labour & human rights 10, carbon 10, governance 5, innovation 5. Supplier X scores 95 on cost, quality and delivery, 60 environment, **10 labour** (serious violations), 50 carbon, 40 governance, 70 innovation. Supplier Y scores 80, 85, 85, 80, 85, 75, 80, 70.
(a) Compute both weighted scores. (3) (b) Should X be retained? (2) (c) Redesign the scorecard. (2)

**Q5.1 (a) Weighted scores. [3 marks]**
X = 19.00 + 19.00 + 14.25 + 9.00 + 1.00 + 5.00 + 2.00 + 3.50 = **72.75**. Y = 16.00 + 17.00 + 12.75 + 12.00 + 8.50 + 7.50 + 4.00 + 3.50 = **81.25**.

**Q5.2 (b) Retain X? [2 marks]**
**No, not on current terms.** X still scores 72.75 ("average") because 55% of the weight sits on cost-quality-delivery, so the weighted model **compensates** for a human-rights failure. Serious labour violations create legal risk (EU due-diligence rules, BRSR Principle 5), brand and investor risk, and contradict *"do not outsource sustainability."* Suspend new orders, require a corrective action plan with an independent audit in 30–90 days, remediate workers, develop Y in parallel and exit if the audit fails.

**Q5.3 (c) Redesign. [2 marks]**
Use **gate + score**: minimum thresholds (knock-out) on human rights, safety and legal compliance **before** any weighted score is computed, then the weighted score for suppliers that pass. Link the score to **volume allocation and contract renewal** so that ESG assessment changes purchasing decisions (M&M: code signed by 95% of suppliers by value; due diligence covers 68.1%).

---

## Q6 (7 marks). Total cost of ownership vs lowest price (Lecture 6) 📗 ⭐⭐
A company buys 10,000 motors a year. Supplier X (imported): price ₹1,000, defect rate 4%, freight ₹30/unit, lifetime energy 50 kWh/unit, 12 kg CO₂ per unit made. Supplier Y (local): price ₹1,100, defects 1%, freight ₹10/unit, 40 kWh/unit, 8 kg CO₂/unit. Each defect costs ₹600; electricity ₹8/kWh; internal carbon price ₹2,000/t.
(a) Compute TCO per unit for each. (4) (b) Annual difference and CO₂ difference. (1) (c) Recommend. (2)

**Q6.1 (a) TCO per unit. [4 marks]**
| Element | X | Y |
|---|---|---|
| Price | 1,000 | 1,100 |
| Defects (rate × ₹600) | 24 | 6 |
| Freight | 30 | 10 |
| Lifetime energy (kWh × ₹8) | 400 | 320 |
| Carbon (kg ÷ 1,000 × ₹2,000) | 24 | 16 |
| **TCO (₹/unit)** | **1,478** | **1,452** |

**Q6.2 (b) Annual difference. [1 mark]**
Y is ₹26 per unit cheaper → **₹2.6 lakh a year**, with **40 t less embedded CO₂** ((12 − 8) × 10,000 ÷ 1,000) and 10,000 × 10 kWh = 1 lakh kWh less electricity used by customers every year of the motors' life.

**Q6.3 (c) Recommendation. [2 marks]**
Choose **Y**: it is 10% dearer on price but **lower on TCO**, carbon and supply risk (local, shorter lead time, no currency exposure). *"Lowest price ≠ lowest total cost"* (Lecture 6). Write the decision into the category strategy: evaluate on TCO, not invoice price.

---

## Quick checklist before you hand in a CO2 answer ⭐⭐⭐
- Weights sum to **100%**? Cost criteria **inverted** when normalising?
- Weighted-score **table** with totals, then a clear **rank**?
- A **sensitivity** line: does a reasonable weight change flip the winner?
- **Knock-out** criteria mentioned (human rights, safety, compliance)?
- A recommendation with a **development plan** or second source?
