# CO2 Numericals: Supplier Weighted Scoring, Scorecards & TOPSIS

> 🎯 **Teacher's importants (CO2, 7 marks):** *weighted scoring of suppliers only, no TOPSIS*: select the best supplier by weighted average and conclude why. Problems tagged 🎯 match this pattern; exam-format versions with model conclusions are on [CO2 7-markers](e3-co2-supplier-7-markers.md). TOPSIS, AHP, Kraljic and the risk matrix below are background only.

This page covers **CO2: weighted scoring of suppliers**, the numerical your faculty named for CO2. It starts with the **exact problems from Lecture 6** 📘 (the weighted score model, the VoltTech supplier scorecard, the TOPSIS construction example and the supplier risk matrix) and the **Lecture 10 supplier sustainability scorecard** 📘, each solved step by step. After those come practice problems built in the same style (📗 = practice data, not from the course files). Turn on **Self-test** (press `T`) to hide the answers.

Theory is on [Sustainable Procurement & Supplier Selection](ch03-sustainable-procurement.md).

> **Exam marks (as your teacher announced):** the 40-mark end-sem paper has **CO3 and CO4 at 10 marks each, CO2 and CO5 at 7 marks each, CO1 and CO6 at 3 marks each**. Expect one 7-mark CO2 numerical (exam-format versions: [CO2 7-markers](e3-co2-supplier-7-markers.md)) with theory/interpretation sub-parts.

---

## The method you will use every time ⭐⭐⭐
**Step 1 — Criteria and weights.** List the criteria (price, quality, delivery, carbon, safety, innovation, compliance…). Weights must add to **100% (or 1.00)**. Convert % to decimals: 25% → 0.25.

**Step 2 — Score each supplier on each criterion** on a common scale (out of 10, or out of 100). The scale must run in **one direction: higher = better**, even for "cost-type" criteria like price or carbon. A supplier with the lowest price gets the highest *price score*.

**Step 3 — Weighted score = Score × Weight** (Lecture 6 formula: *Weighted Score = (Score out of 10) × (Weight)*).

**Step 4 — Total weighted score = Σ (Score × Weight)** for each supplier.

**Step 5 — Rank, recommend, and interpret.** Highest total wins, *but* always write two more lines in the exam:
1. **Margin check** — if the gap is small (say < 0.2 on a 10-point scale), the decision is sensitive; run a sensitivity test or a pilot order.
2. **Gate check** — weighted scoring is *compensatory* (a high score on price can hide a terrible score on labour). Non-negotiables (child labour, forced labour, serious safety or legal violations) must be **knock-out criteria applied before scoring**, not just low scores.

**Lecture 6 scoring guide (out of 10):** 9–10 Excellent · 7–8 Good · 5–6 Average · 3–4 Poor · 0–2 Very poor. Tip on the slide: *customise weights to organisational priorities; base scores on data and evidence.*

**Converting raw data into scores** (when the question gives ₹, ppm, kg CO₂e instead of scores):
- *Benefit criterion* (higher is better, e.g. quality score, patents): Score = x ÷ x_max × 10 (ratio method) or 1 + 9 × (x − x_min) ÷ (x_max − x_min) (min–max method).
- *Cost criterion* (lower is better, e.g. price, defects, CO₂e, LTIFR): Score = x_min ÷ x × 10 (ratio method) or 1 + 9 × (x_max − x) ÷ (x_max − x_min) (min–max method).
- State which method you use. Both are accepted; ratio normalisation is gentler, min–max exaggerates gaps.

---

## Problem 1. Weighted Score Model — Suppliers A, B and C (Lecture 6, slide 24) 📘 ⭐⭐⭐ 🎯
*"Demonstrating Weighted Scoring for Supplier Evaluation — Easy Classroom Example."* Scores are out of 10.

| Criteria | Weight (%) | Weight (decimal) | Supplier A score | Supplier B score | Supplier C score |
|---|---|---|---|---|---|
| Price | 25% | 0.25 | 8 | 7 | 9 |
| Quality | 20% | 0.20 | 9 | 8 | 7 |
| Delivery | 15% | 0.15 | 7 | 9 | 8 |
| Carbon | 15% | 0.15 | 8 | 6 | 9 |
| Safety | 10% | 0.10 | 9 | 8 | 7 |
| Innovation | 10% | 0.10 | 7 | 9 | 8 |
| Compliance | 5% | 0.05 | 9 | 8 | 9 |
| **Total** | **100%** | **1.00** | | | |

**Q1.1 Calculate the total weighted score of each supplier.**
Weighted score = Score × Weight (decimal).

| Criteria (weight) | Supplier A | Supplier B | Supplier C |
|---|---|---|---|
| Price (0.25) | 8 × 0.25 = 2.00 | 7 × 0.25 = 1.75 | 9 × 0.25 = 2.25 |
| Quality (0.20) | 9 × 0.20 = 1.80 | 8 × 0.20 = 1.60 | 7 × 0.20 = 1.40 |
| Delivery (0.15) | 7 × 0.15 = 1.05 | 9 × 0.15 = 1.35 | 8 × 0.15 = 1.20 |
| Carbon (0.15) | 8 × 0.15 = 1.20 | 6 × 0.15 = 0.90 | 9 × 0.15 = 1.35 |
| Safety (0.10) | 9 × 0.10 = 0.90 | 8 × 0.10 = 0.80 | 7 × 0.10 = 0.70 |
| Innovation (0.10) | 7 × 0.10 = 0.70 | 9 × 0.10 = 0.90 | 8 × 0.10 = 0.80 |
| Compliance (0.05) | 9 × 0.05 = 0.45 | 8 × 0.05 = 0.40 | 9 × 0.05 = 0.45 |
| **Total weighted score** | **8.10 / 10** | **7.70 / 10** | **8.15 / 10** |

**Q1.2 Rank the suppliers and state the winner.**
1st **Supplier C (8.15)**, 2nd Supplier A (8.10), 3rd Supplier B (7.70). The slide declares **Supplier C the winner** with 8.15/10.

**Q1.3 Interpret the result. Is the decision robust?**
C wins on the two "big" criteria for sustainability: **price (9 → 2.25)** and **carbon (9 → 1.35)**. But A is only **0.05 behind**, and A beats C on quality (9 vs 7) and safety (9 vs 7). With a 0.05 margin the decision is *not* robust: a one-point change in a single score flips it. Recommended answer: select **C as primary supplier**, keep **A as qualified second source**, and write quality and safety improvement targets into C's contract (because C scores only 7 on both). B is dragged down by the weakest carbon score (6).

**Q1.4 Sensitivity: the company raises Carbon to 25% and cuts Price to 15%. Does the ranking change?**
Only the price and carbon rows change (−0.10 on price weight, +0.10 on carbon weight):
- A: 8.10 − (8 × 0.10) + (8 × 0.10) = **8.10** (A scores 8 on both, so no change)
- B: 7.70 − (7 × 0.10) + (6 × 0.10) = **7.60**
- C: 8.15 − (9 × 0.10) + (9 × 0.10) = **8.15**

Ranking unchanged: **C > A > B**. B falls further because it is the highest-carbon supplier.

**Q1.5 Sensitivity: management instead raises Quality to 30% and cuts Price to 15%. Does C still win?**
Price weight −0.10, quality weight +0.10:
- A: 8.10 − 0.80 + 0.90 = **8.20**
- B: 7.70 − 0.70 + 0.80 = **7.80**
- C: 8.15 − 0.90 + 0.70 = **7.95**

Now **A wins (8.20)**, then C (7.95), then B (7.80). The choice flips when the firm values quality over price. This is exactly why the slide's tip says *customise weights based on organisational priorities*.

**Q1.6 What carbon score would Supplier B need to tie with Supplier C?**
Gap = 8.15 − 7.70 = 0.45. Each carbon point is worth 0.15. Points needed = 0.45 ÷ 0.15 = **3 points**, so B's carbon score would have to rise from 6 to **9**. This is a supplier-development target you could put to B (e.g. renewable power, ISO 14001).

---

## Problem 2. Supplier Scorecard — VoltTech Components Pvt. Ltd. (Lecture 6, slide 22) 📘 ⭐⭐⭐ 🎯
Supplier: VoltTech Components Pvt. Ltd. · Category: electrical components (wires & connectors) · Industry: electrical appliances · Period: Apr–Jun 2025. Scores out of 100.

| Criteria | Weight | Scoring method / metric | Supplier score (/100) |
|---|---|---|---|
| Price | 25% | Delivered price vs benchmark (best price = 100) | 88 |
| Quality | 20% | PPM defects, First Pass Yield, return rate | 90 |
| Delivery | 15% | On-time delivery %, lead-time adherence | 85 |
| Carbon | 15% | CO₂e emissions (t) per unit vs industry benchmark | 80 |
| Safety | 10% | TRIR, lost-time injury, safety initiatives | 92 |
| Innovation | 10% | New product ideas, process improvement, R&D investment | 78 |
| Compliance | 5% | Legal, environmental, social compliance, certifications | 95 |

Score range guide on the slide: **90–100 A (Excellent) · 75–89 B (Good) · 60–74 C (Average) · < 60 D (Poor)**. Trend over the last four quarters: 78.4 (Q3 FY24) → 81.2 → 83.6 → 86.2 (Q2 FY25).

**Q2.1 Calculate the overall weighted score.**

| Criteria | Weight × Score | Weighted score |
|---|---|---|
| Price | 0.25 × 88 | 22.00 |
| Quality | 0.20 × 90 | 18.00 |
| Delivery | 0.15 × 85 | 12.75 |
| Carbon | 0.15 × 80 | 12.00 |
| Safety | 0.10 × 92 | 9.20 |
| Innovation | 0.10 × 78 | 7.80 |
| Compliance | 0.05 × 95 | 4.75 |
| **Total** | | **86.50 / 100** |

**Q2.2 What performance rating does VoltTech get?**
By the slide's own range guide, **86.5 falls in 75–89 → "B (Good)"**. Note: the slide's headline box shows "86.2/100, A (Excellent)". Both numbers are inconsistent with the table: the table adds to **86.50**, and any score below 90 is a **B** on the printed guide. In the exam, show the arithmetic (86.50) and apply the guide (B, Good); mention that it is the best-ever quarter and the trend is rising.

**Q2.3 Identify strengths and improvement areas, and suggest actions.**
- *Strengths:* compliance (95), safety (92) and quality (90) — the slide lists "strong quality performance, excellent compliance & safety".
- *Improvement areas:* **innovation (78)** and **carbon (80)** — the two lowest scores, exactly the slide's "innovation capability" and "carbon footprint reduction".
- *Actions:* joint innovation/value-engineering workshops with VoltTech; a carbon-reduction plan (renewable electricity, copper scrap recovery, low-carbon PVC), with a target of carbon ≥ 88 next year; keep quarterly reviews.
- *What the gain is worth:* raising carbon from 80 to 90 adds 0.15 × 10 = **1.5 points**; raising innovation from 78 to 88 adds 0.10 × 10 = **1.0 point**. Both together take the score to 89.0, close to the A band.

**Q2.4 Quarter-on-quarter improvement?**
From 78.4 to 86.2 over three quarters = +7.8 points (+9.9%). Average gain ≈ 2.6 points per quarter. Using the corrected 86.5, the gain is +8.1 points (+10.3%).

---

## Problem 3. TOPSIS — Supplier Selection in Construction (Lecture 6, slide 25) 📘 · not in exam (no TOPSIS)
*Project: residential building · Material: TMT steel bars · Requirement: 500 MT · Goal: select the best supplier.* TOPSIS = Technique for Order of Preference by Similarity to Ideal Solution: **choose the supplier closest to the ideal solution and farthest from the worst (negative-ideal) solution.**

**Decision criteria:**

| Criterion | Type | Weight (w) |
|---|---|---|
| C1 — Price (INR/MT) | Cost | 0.30 |
| C2 — Quality (score) | Benefit | 0.25 |
| C3 — Delivery performance (%) | Benefit | 0.20 |
| C4 — Safety performance (score) | Benefit | 0.15 |
| C5 — Sustainability (carbon score) | Benefit | 0.10 |

**Step 1 — Decision matrix (X):**

| Supplier | C1 Price | C2 Quality | C3 Delivery % | C4 Safety | C5 Sustainability |
|---|---|---|---|---|---|
| A (BuildStrong Pvt. Ltd.) | 56,000 | 8 | 92 | 9 | 7 |
| B (Apex Infra Materials) | 52,000 | 7 | 90 | 8 | 6 |
| C (ConstructPro Solutions) | 54,000 | 9 | 95 | 9 | 8 |
| D (SolidBase Industries) | 58,000 | 6 | 88 | 7 | 7 |

**Q3.1 Step 2 — Normalise the decision matrix (vector normalisation).**
r_ij = x_ij ÷ √(Σ x_ij²) for each column.

Column norms: C1 = √(56,000² + 52,000² + 54,000² + 58,000²) = **110,090.9**; C2 = √(64+49+81+36) = √230 = **15.166**; C3 = √(8,464+8,100+9,025+7,744) = √33,333 = **182.57**; C4 = √(81+64+81+49) = √275 = **16.583**; C5 = √(49+36+64+49) = √198 = **14.071**.

| Supplier | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| A | 56,000/110,091 = 0.509 | 8/15.166 = 0.528 | 92/182.57 = 0.504 | 9/16.583 = 0.543 | 7/14.071 = 0.497 |
| B | 0.472 | 0.462 | 0.493 | 0.482 | 0.426 |
| C | 0.491 | 0.593 | 0.520 | 0.543 | 0.569 |
| D | 0.527 | 0.396 | 0.482 | 0.422 | 0.497 |

**Q3.2 Step 3 — Weighted normalised matrix V = R × w.**

| Supplier | C1 (×0.30) | C2 (×0.25) | C3 (×0.20) | C4 (×0.15) | C5 (×0.10) |
|---|---|---|---|---|---|
| A | 0.1526 | 0.1319 | 0.1008 | 0.0814 | 0.0497 |
| B | 0.1417 | 0.1154 | 0.0986 | 0.0724 | 0.0426 |
| C | 0.1472 | 0.1484 | 0.1041 | 0.0814 | 0.0569 |
| D | 0.1581 | 0.0989 | 0.0964 | 0.0633 | 0.0497 |

**Q3.3 Step 4 — Ideal (A⁺) and negative-ideal (A⁻) solutions.**
Rule: for a **benefit** criterion A⁺ = max, A⁻ = min; for a **cost** criterion (price) A⁺ = **min**, A⁻ = **max**.

| | C1 (cost) | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| A⁺ (ideal) | 0.1417 (B) | 0.1484 (C) | 0.1041 (C) | 0.0814 (A, C) | 0.0569 (C) |
| A⁻ (negative-ideal) | 0.1581 (D) | 0.0989 (D) | 0.0964 (D) | 0.0633 (D) | 0.0426 (B) |

**Q3.4 Step 5 — Separation measures S⁺ and S⁻.**
S⁺ = √Σ(v_ij − A⁺_j)², S⁻ = √Σ(v_ij − A⁻_j)².

*Worked for Supplier C:* differences from A⁺ are (0.1472−0.1417) = 0.0055 on C1 and 0 on C2–C5 → **S⁺ = 0.0055**. Differences from A⁻: C1 −0.0109, C2 +0.0495, C3 +0.0077, C4 +0.0181, C5 +0.0143 → squares sum = 0.000119 + 0.002450 + 0.000059 + 0.000328 + 0.000204 = 0.003160 → **S⁻ = 0.0562**.

| Supplier | S⁺ (to A⁺) | S⁻ (to A⁻) |
|---|---|---|
| A | 0.0213 | 0.0389 |
| B | 0.0374 | 0.0250 |
| C | 0.0055 | 0.0561 |
| D | 0.0561 | 0.0071 |

**Q3.5 Step 6 — Relative closeness Cᵢ* = S⁻ ÷ (S⁺ + S⁻) and rank.**

| Supplier | Cᵢ* | Rank |
|---|---|---|
| A (BuildStrong) | 0.0389 ÷ 0.0602 = **0.647** | 2 |
| B (Apex Infra) | 0.0250 ÷ 0.0624 = **0.401** | 3 |
| C (ConstructPro) | 0.0561 ÷ 0.0616 = **0.912** | **1** |
| D (SolidBase) | 0.0071 ÷ 0.0632 = **0.112** | 4 |

**Final recommendation: select ConstructPro Solutions (Supplier C)** for the 500 MT of TMT bars. Cᵢ* close to 1 means close to the ideal. C has the best quality (9), best delivery (95%), joint-best safety (9) and best sustainability (8), at a mid-range price (₹54,000, not the cheapest). This matches the slide: *"lowest price is not the lowest, but balanced with high performance… best overall balance across all criteria."*

**Q3.6 How do your numbers compare with the slide?** ⭐⭐
The slide reaches the same winner (C, Cᵢ* = 0.608) but its intermediate numbers are illustrative (the slide's own note: *"Numbers are illustrative for learning purpose"*). It also prints ranks that do not follow its own Cᵢ* values (it ranks D, with 0.106, second and A, with 0.382, third). Ranking by Cᵢ* always goes from highest to lowest: on the slide's values that is **C (0.608) > A (0.382) > B (0.251) > D (0.106)**, the same order as the full recomputation above. In the exam, compute from the raw matrix as shown and rank strictly by Cᵢ*.

**Q3.7 Why use TOPSIS instead of simple weighted scoring?**
(1) It uses **raw data** in different units (₹/MT, %, scores) through normalisation, so you do not have to invent 1–10 scores. (2) It treats **cost and benefit criteria correctly** (ideal = minimum price). (3) It rewards *balance*: a supplier is judged on distance from the best **and** the worst, so one extreme weakness hurts (D is worst on four criteria and ends at 0.112). Limitations: results depend on the weights and the normalisation; adding or removing a supplier can change the ideal points ("rank reversal"); it still needs knock-out screening for ethics.

---

## Problem 4. Supplier Risk Matrix — Agri-food industry (Lecture 6, slide 26) 📘 ⭐⭐
Likelihood scale: **Certain (> 80%), Most likely (60–80%), Possible (30–60%), Unlikely (10–30%), Rare (< 10%)**. Impact scale: **Insignificant, Minor, Moderate, Major, Severe**. Risk bands: **High 15–24 · Medium 6–14 · Low 1–5.** (Score = Likelihood 1–5 × Impact 1–5.)

| Supplier | Risk | Key drivers | Mitigation |
|---|---|---|---|
| A | High | Drought risk, single-region sourcing | Weather monitoring, diversify sourcing |
| B | Medium | Moderate leverage, seasonal cash flow | Financial monitoring, advance payments with controls |
| C | Low | Strong fleet, good on-time performance | Continue KPI monitoring |

**Q4.1 Assign likelihood and impact values that are consistent with the slide's classification and compute the risk score.**
Using Rare = 1 … Certain = 5 and Insignificant = 1 … Severe = 5:
- **Supplier A:** drought in a single sourcing region is *Most likely* (4) and its impact is *Major* (4) because the whole category stops → **4 × 4 = 16 → High (15–24)**.
- **Supplier B:** cash-flow stress is *Possible* (3) with *Moderate* impact (3) → **3 × 3 = 9 → Medium (6–14)**.
- **Supplier C:** a delivery failure is *Unlikely* (2) with *Minor* impact (2) → **2 × 2 = 4 → Low (1–5)**.

**Q4.2 What should the buyer do with each supplier?**
A: treat (dual sourcing from a second agro-climatic region, weather-indexed contracts, safety stock before the monsoon, farmer support for drought-resistant practice). B: monitor (quarterly financial health review, advance payments released against milestones, escrow or bank guarantee). C: accept and monitor through the scorecard. Re-score every quarter; the matrix is a living tool.

**Q4.3 Supplier A's sourcing is split across two regions so that likelihood falls to "Possible". What is the new score?**
3 × 4 = **12 → Medium**. Diversification moved A from High to Medium without changing the impact. To reach Low you must also cut the impact (e.g. buffer stock reduces impact to Minor: 3 × 2 = 6, still Medium; Unlikely × Minor = 2 × 2 = 4, Low).

---

## Problem 5. Supplier Sustainability Scorecard — retain a 95/100 supplier with labour violations? (Lecture 10, slide 12) 📘 ⭐⭐⭐ 🎯
Lecture 10 gives this scorecard and asks: *"Should a supplier with the following score be retained? 95/100 on cost-quality-delivery, but serious labour violations."* The slide's punchline: *"This is where sustainability becomes a management decision rather than a reporting exercise."*

| Dimension | Weight |
|---|---|
| Cost competitiveness | 20 |
| Quality | 20 |
| Delivery | 15 |
| Environmental performance | 15 |
| Labour & human rights | 10 |
| Carbon reduction | 10 |
| Governance | 5 |
| Innovation | 5 |
| **Total** | **100** |

**Q5.1 Using assumed scores, show why a weighted score alone can wrongly retain the supplier.**
**Assumed scores (state them in the exam):** Supplier X scores 95 on cost, quality and delivery; environment 60; labour & human rights **10** (serious violations); carbon 50; governance 40; innovation 70. Supplier Y is a balanced alternative: 80, 85, 85, 80, 85, 75, 80, 70.

| Dimension (weight) | Supplier X | Supplier Y |
|---|---|---|
| Cost (0.20) | 95 → 19.00 | 80 → 16.00 |
| Quality (0.20) | 95 → 19.00 | 85 → 17.00 |
| Delivery (0.15) | 95 → 14.25 | 85 → 12.75 |
| Environmental (0.15) | 60 → 9.00 | 80 → 12.00 |
| Labour & human rights (0.10) | 10 → 1.00 | 85 → 8.50 |
| Carbon reduction (0.10) | 50 → 5.00 | 75 → 7.50 |
| Governance (0.05) | 40 → 2.00 | 80 → 4.00 |
| Innovation (0.05) | 70 → 3.50 | 70 → 3.50 |
| **Total** | **72.75** | **81.25** |

Even with a near-zero labour score, X still totals **72.75**, which most scorecards would call "Average/acceptable". Labour carries only 10% weight, so the 95s on cost-quality-delivery (55% of the weight) compensate. Y wins on the weighted score anyway (81.25), but the deeper point is that X should not be "scored" at all.

**Q5.2 So, should Supplier X be retained? Give a managerial answer.**
**No — not on current terms.** Serious labour or human-rights violations are a **knock-out (minimum-threshold) criterion**, not a 10% trade-off. Reasons: legal exposure (EU CSDDD due-diligence rules for exporters, BRSR Principle 5 on human rights), brand and investor risk (Nike, Intel and Patagonia examples in Lecture 6), and the course principle "*do not outsource sustainability*" (Lecture 11). Recommended action: (1) suspend new orders; (2) demand a corrective action plan with independent audit within 30–90 days; (3) remediate workers (back pay, safe conditions); (4) develop an alternative supplier (Y) in parallel; (5) exit if the audit fails. Then redesign the scorecard as **gate + score**: suppliers must pass minimum thresholds on human rights, safety and legal compliance before any weighted score is computed.

**Q5.3 Mahindra & Mahindra link (Lecture 10, slide 25).**
M&M's supplier code of conduct is signed by **95% of suppliers by purchase value**, and environmental due diligence since FY2024 covers **68.1% by value**. The slide's question: *is supplier ESG assessment enough, or should supplier ESG performance affect purchasing decisions?* Answer: assessment is an **activity**; it only becomes performance management when the score changes volume allocation, prices, contract renewal or development support (this is the logic of Problem 5).

---

## Problem 6. Laptop manufacturer — evaluate three suppliers (Lecture 6 exercise, slide 32) 📘 + practice data 📗 ⭐⭐ 🎯
The Lecture 6 exercise: *"For a laptop manufacturing company, evaluate three suppliers using Price, Quality, Carbon, Safety, Innovation and create your own supplier scorecard."* The slide gives no data, so here is a fully worked version with **assumed raw data** (state it in the exam).

| Supplier (battery packs) | Price (₹/pack) | Defects (ppm) | Carbon (kg CO₂e/pack) | Safety (LTIFR) | Innovation (patents, 3 yrs) |
|---|---|---|---|---|---|
| P | 42,000 | 450 | 95 | 0.8 | 6 |
| Q | 45,000 | 200 | 70 | 0.4 | 9 |
| R | 40,000 | 900 | 120 | 1.5 | 3 |

Weights: Price 30%, Quality 25%, Carbon 20%, Safety 15%, Innovation 10%. Price, defects, carbon and LTIFR are **cost-type** (lower is better); patents are **benefit-type**.

**Q6.1 Convert the raw data to scores out of 10 using ratio normalisation and compute weighted totals.**
Cost-type: score = (best ÷ actual) × 10. Benefit-type: score = (actual ÷ best) × 10.

| Criterion (weight) | P | Q | R |
|---|---|---|---|
| Price (0.30) | 40,000/42,000×10 = 9.52 → 2.86 | 40,000/45,000×10 = 8.89 → 2.67 | 10.00 → 3.00 |
| Quality (0.25) | 200/450×10 = 4.44 → 1.11 | 10.00 → 2.50 | 200/900×10 = 2.22 → 0.56 |
| Carbon (0.20) | 70/95×10 = 7.37 → 1.47 | 10.00 → 2.00 | 70/120×10 = 5.83 → 1.17 |
| Safety (0.15) | 0.4/0.8×10 = 5.00 → 0.75 | 10.00 → 1.50 | 0.4/1.5×10 = 2.67 → 0.40 |
| Innovation (0.10) | 6/9×10 = 6.67 → 0.67 | 10.00 → 1.00 | 3/9×10 = 3.33 → 0.33 |
| **Total (/10)** | **6.86** | **9.67** | **5.46** |

Ranking: **Q (9.67) > P (6.86) > R (5.46).** Q is 12.5% dearer than R but best on everything else.

**Q6.2 Recompute with min–max normalisation (score = 1 + 9 × relative position). Does the winner change?**
Totals: **Q = 7.30, P = 6.28, R = 3.70**. Same ranking; min–max widens the gaps because the worst supplier on each criterion gets exactly 1.

**Q6.3 Is Q's 7% higher price than P (₹3,000/pack) justified? Use a TCO view.**
Quality: P has 250 ppm more defects; at 500,000 packs a year that is 125 more field failures. If each battery failure in warranty costs ₹25,000 (replacement + logistics + brand), that is ₹31.25 lakh. Carbon: P emits 25 kg CO₂e more per pack → 12,500 t CO₂e a year, a Scope 3 cost (at an internal carbon price of ₹2,000/t, ₹2.5 crore). The price premium is ₹3,000 × 500,000 = ₹150 crore, so on these assumptions the premium is **not** fully paid back by quality and carbon alone. The decision depends on the firm's carbon commitments and safety risk (a battery fire recall can dwarf all of these). A good answer: **award Q the majority share (e.g. 70%) and P 30% with a development plan**, and drop R (worst on quality, carbon and safety).

---

## Problem 7. TCO vs lowest price — "Which supplier would you choose?" (Lecture 6, slide 7) 📘 + practice data 📗 ⭐⭐
Lecture 6 debate: **Supplier A** — lowest cost, high emissions, child-labour allegations. **Supplier B** — 12% more expensive, renewable energy, zero human-rights issues, ISO 14001 certified. *"Focus change: best cost → best value (economic + environmental + social)."*

**Assumed data:** A's price ₹100/unit, so B = ₹112. Annual volume 1,00,000 units. Defect rates A 3%, B 1%; each defect costs ₹200 to handle. Emissions A 2.0 kg CO₂e/unit, B 0.8 kg; carbon cost (CBAM/internal price) ₹8,000/t. Compliance/reputation risk: A has a 10% chance of a ₹50 lakh loss per year; B has 1%. Logistics ₹4/unit for both.

**Q7.1 Compute the total cost of ownership per unit for each supplier.**

| Cost element (₹/unit) | Supplier A | Supplier B |
|---|---|---|
| Purchase price | 100.00 | 112.00 |
| Quality cost = defect rate × ₹200 | 0.03 × 200 = 6.00 | 0.01 × 200 = 2.00 |
| Carbon cost = kg ÷ 1,000 × ₹8,000 | 2.0/1,000 × 8,000 = 16.00 | 0.8/1,000 × 8,000 = 6.40 |
| Expected risk cost = p × loss ÷ volume | 0.10 × 50,00,000 ÷ 1,00,000 = 5.00 | 0.01 × 50,00,000 ÷ 1,00,000 = 0.50 |
| Logistics | 4.00 | 4.00 |
| **TCO per unit** | **131.00** | **124.90** |

**Q7.2 Conclusion.**
B is **₹6.10 per unit (4.7%) cheaper on TCO** although it is 12% dearer on price; annual saving ≈ ₹6.1 lakh, before counting brand value. And A's child-labour allegation is a knock-out anyway. This is the "lowest purchase cost → lowest total cost of ownership" message of the Cost vs Value slide (lifecycle cost components: purchase price, maintenance, waste, energy, end-of-life).

**Q7.3 At what carbon price would A and B have equal TCO (ignoring the child-labour issue)?**
Without the carbon line: A = 100 + 6 + 5 + 4 = 115; B = 112 + 2 + 0.5 + 4 = 118.5. B is ₹3.5 dearer. B saves 1.2 kg = 0.0012 t per unit. Break-even carbon price = 3.5 ÷ 0.0012 = **₹2,917 per t CO₂e**. Above about ₹2,900/t, B is cheaper on TCO even before ethics.

---

## Problem 8. AHP — deriving the weights (Lecture 6 decision tools) 📘 method + practice data 📗 ⭐
Lecture 6 lists AHP as *"a structured technique to organise and analyse complex decisions using a hierarchy of goals, criteria and alternatives."* AHP gives you defensible weights instead of guessing them.

A buyer compares three criteria on Saaty's 1–9 scale: Cost is **2×** as important as Quality and **3×** as important as Carbon; Quality is **2×** as important as Carbon.

**Q8.1 Build the pairwise matrix and find the weights (geometric-mean method).**

| | Cost | Quality | Carbon | Geometric mean | Weight |
|---|---|---|---|---|---|
| Cost | 1 | 2 | 3 | (1×2×3)^(1/3) = 1.817 | 1.817 ÷ 3.367 = **0.540** |
| Quality | 1/2 | 1 | 2 | (0.5×1×2)^(1/3) = 1.000 | **0.297** |
| Carbon | 1/3 | 1/2 | 1 | (0.333×0.5×1)^(1/3) = 0.550 | **0.163** |
| | | | | Sum = 3.367 | 1.000 |

**Q8.2 Check consistency.**
A×w = (1.624, 0.894, 0.492). λ_max = average of (1.624/0.540, 0.894/0.297, 0.492/0.163) = **3.009**. CI = (λ_max − n) ÷ (n − 1) = 0.009 ÷ 2 = **0.0046**. CR = CI ÷ RI = 0.0046 ÷ 0.58 = **0.008**, well below **0.10**, so the judgements are consistent. These weights (54/30/16) then feed a weighted-scoring or TOPSIS model.

---

## Problem 9. Kraljic matrix — classify the purchases (Lecture 6, slide 27) 📘 ⭐⭐
Kraljic segments purchases on **supply risk** (vertical) and **profit impact** (horizontal): **Strategic** (high risk, high impact: partner and collaborate, joint innovation), **Leverage** (low risk, high impact: maximise value through negotiation and volume), **Bottleneck** (high risk, low impact: ensure supply security, build alternatives and buffers), **Routine** (low risk, low impact: automate, simplify, reduce transaction cost).

**Q9.1 Classify these items for an EV two-wheeler maker: lithium-ion cells; steel tubes for the frame; a single-source special rare-earth magnet costing little per unit; office stationery; tyres from five qualified suppliers; packaging cartons.**
Lithium-ion cells → **Strategic** (40% of BOM cost, concentrated supply, conflict-mineral risk). Rare-earth magnet → **Bottleneck** (cheap but single-source, China-concentrated). Steel tubes and tyres → **Leverage** (big spend, many suppliers; use competitive tendering, but add carbon criteria, e.g. green steel). Stationery and cartons → **Routine** (e-catalogue; for cartons, specify recycled content, which costs nothing extra).

**Q9.2 Supplier development tools from the same slide:** training, joint innovation, technology transfer, audits, continuous improvement, long-term partnerships. Use them mainly on strategic and bottleneck suppliers.

---

## Practice set (no solutions shown until you reveal) 📗

**Q10. An FMCG firm scores two packaging suppliers out of 10. Weights: Cost 30%, Recycled content 25%, Quality 20%, Delivery 15%, Social compliance 10%. Supplier M: 9, 4, 8, 8, 7. Supplier N: 7, 9, 8, 7, 9. Who wins? What if Cost weight rises to 40% and Recycled content falls to 15%?**
Base: M = 2.70 + 1.00 + 1.60 + 1.20 + 0.70 = **7.20**; N = 2.10 + 2.25 + 1.60 + 1.05 + 0.90 = **7.90** → **N wins**. Changed weights: M = 7.20 + 0.10×9 − 0.10×4 = **7.70**; N = 7.90 + 0.10×7 − 0.10×9 = **7.70** → a **tie**. The decision hinges entirely on how much the firm values recycled content; with the EPR plastic-packaging obligations in India, a defensible choice is N.

**Q11. A supplier's scores out of 100 are Price 82, Quality 91, Delivery 76, Carbon 64, Safety 88, Innovation 70, Compliance 98 under the VoltTech weights (25/20/15/15/10/10/5). Compute the score and rating.**
20.50 + 18.20 + 11.40 + 9.60 + 8.80 + 7.00 + 4.90 = **80.40 → B (Good)**. The weakest area is carbon (64). Raising carbon to 80 adds 2.4 points (82.8).

**Q12. (Not in exam: TOPSIS) In TOPSIS, a supplier has S⁺ = 0.030 and S⁻ = 0.045. Another has S⁺ = 0.020 and S⁻ = 0.025. Which is preferred?**
C₁* = 0.045 ÷ 0.075 = **0.600**; C₂* = 0.025 ÷ 0.045 = **0.556**. The first supplier is preferred even though it is farther from the ideal, because it is relatively much farther from the worst.

**Q13. Using the Lecture 6 risk bands, classify: (i) Possible × Severe; (ii) Certain × Minor; (iii) Rare × Severe; (iv) Most likely × Moderate.**
(i) 3 × 5 = 15 → **High**; (ii) 5 × 2 = 10 → **Medium**; (iii) 1 × 5 = 5 → **Low** (but a "black-swan" item: keep a contingency plan); (iv) 4 × 3 = 12 → **Medium**.

**Q14. Why should "Carbon" be scored as a benefit criterion in the weighted score model but entered as a cost criterion in TOPSIS?**
In the weighted model you enter a **score** (9 = low-carbon, good), so higher is better. In TOPSIS you enter **raw emissions** (kg CO₂e/unit), where lower is better, so its ideal value is the minimum. If TOPSIS uses a "carbon score" (like the Lecture 6 C5), it is a benefit criterion. Always check what the number means before choosing the direction.

**Q15. Write the five-step "Recap" of Lecture 6 and connect it to a scoring numerical.**
Step 1 sustainable procurement → Step 2 supplier sustainability → Step 3 decision tools → Step 4 business performance → Step 5 competitive advantage. A scoring model is Step 3: it turns the sustainability criteria of Step 2 into a supplier choice whose results show up in Step 4 KPIs (OTIF, defect rate, Scope 3, cost savings).
