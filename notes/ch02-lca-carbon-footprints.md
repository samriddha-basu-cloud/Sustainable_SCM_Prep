# Environmental LCA, Carbon Footprints & Carbon Management
Syllabus topic 2 📘 (Lecture 4 LCA Fundamentals, Lecture 5 LCSA, and the deck "Carbon management, carbon accounting and carbon trading"). This chapter is the theory behind **CO3 (carbon accounting)**, one of the two **high-weightage** COs. The numericals are on [Carbon Accounting Numericals](p2-carbon-accounting-numericals.md) and [LCA & Energy Numericals](p5-lca-energy-numericals.md). Expect theory sub-parts such as "explain the four phases of LCA", "carbon footprint vs LCA", "net zero vs carbon neutral", "what is MRV" and "explain Scope 3".

---

## Part A — Life Cycle Assessment (Lecture 4)

### 1. What LCA is and why managers care ⭐⭐⭐
**ISO definition** 📘: *Life Cycle Assessment is a systematic method to evaluate the environmental impacts associated with every stage of a product's life* — raw-material extraction, manufacturing, distribution, use and end-of-life (the "life cycle wheel"). ISO 14040 sets the principles and framework; ISO 14044 sets the requirements and guidelines.

LCA underpins **ESG, carbon accounting, product sustainability, eco-design, the circular economy, green procurement and sustainable SC decision-making** 📘. *"Managers cannot improve what they don't measure."*

**Learning outcomes the lecture lists** (useful as a structure for long answers): explain LCA; understand ISO 14040/14044; perform basic LCA thinking; identify environmental hotspots; compare products using life-cycle thinking; apply LCA in SC decisions; appreciate its limitations; relate LCA to carbon footprint, ESG and the circular economy.

### 2. Evolution of LCA 📘 ⭐⭐
| Period | Focus |
|---|---|
| 1970s | Energy analysis (oil crises) |
| 1980s | Packaging comparison (e.g. bottles and cans) |
| 1990s | ISO framework (ISO 14040 series, 1997–2000; revised 2006) |
| 2000s | Corporate sustainability |
| Today | Carbon accounting, ESG, Digital Product Passport, circular economy |

### 3. System boundaries ⭐⭐⭐
| Boundary | Covers | Typical use |
|---|---|---|
| **Cradle-to-gate** | Raw materials → factory gate | Supplier data, EPDs, B2B footprints, CBAM embedded emissions |
| **Gate-to-gate** | One process or site only | Process improvement inside a plant |
| **Cradle-to-grave** | Raw materials → use → disposal | Consumer products, EV vs ICE comparison |
| **Cradle-to-cradle** | Cradle-to-grave + recycling back into new products | Circular-economy design |

### 4. The four phases of LCA (ISO 14040/44) 📘 ⭐⭐⭐
*"These steps are the backbone of LCA."* The phases are iterative: interpretation feeds back into every earlier phase.

**Phase I — Goal and scope.** Answer five questions: (i) why are we conducting the study? (ii) who will use the results? (iii) what is the **functional unit**? (iv) what are the system boundaries? (v) what are the assumptions?
- The **functional unit** is the quantified function the product delivers, and it is *"the most misunderstood"* 📘. Wrong: ❌ one plastic bottle, ❌ one shopping bag, ❌ one petrol barrel. Right: ✅ **delivering 1 litre of drinking water**, ✅ **carrying 20 kg of groceries per month**, ✅ **storing 159 litres of petrol**. Two products can only be compared when they deliver the same function ([worked example](p5-lca-energy-numericals.md)).

**Phase II — Life Cycle Inventory (LCI).** Quantify every input (materials, energy, water) and output (emissions to air, water and soil; waste; products) for each process in the boundary.
- **Primary data**: factory and supplier data, utility bills, meter readings.
- **Secondary data**: government statistics, scientific literature, databases such as **ecoinvent**.
- Issues: data quality, **allocation** of impacts across co-products (by mass, energy or economic value), cut-off rules.

**Phase III — Life Cycle Impact Assessment (LCIA).** Classify the inventory into impact categories and characterise it with factors (for example GWP for climate change). Categories on the slide: **climate change, ozone depletion, smog (photochemical oxidation), water scarcity, land occupation, ecotoxicity, biodiversity**; others include acidification, eutrophication and resource depletion.

**Phase IV — Interpretation.** Identify significant issues and hotspots, check completeness, run sensitivity analysis on key assumptions, draw conclusions and recommendations, and support decisions. Slide example: *"EVs have higher manufacturing emissions but often lower lifetime emissions depending on the electricity mix."*

### 5. Carbon footprint vs LCA 📘 ⭐⭐⭐
| | Carbon footprint | LCA |
|---|---|---|
| Measures | CO₂e only (GWP) | Multiple impacts |
| Scope | Climate | Whole environment |
| Effort | Simpler, faster | Comprehensive, more detailed |
| Standard | GHG Protocol, ISO 14067 (product), ISO 14064 (organisation) | ISO 14040/14044 |
| Risk | Burden shifting (cut CO₂ but raise water use or toxicity) | Captures trade-offs |

A carbon footprint is a single-indicator subset of LCA.

### 6. Indian case studies (Lecture 4) 📘 ⭐⭐⭐
| Company | Hotspots identified by LCA | Improvement actions |
|---|---|---|
| **UltraTech Cement** | Clinker production, kiln fuel, transportation | Waste-heat recovery, alternative fuels, fly-ash blending |
| **Tata Steel** | Iron-ore mining, blast furnace, coal, transport | Hydrogen, scrap recycling, renewable electricity |
| **Amul milk** | Farm emissions: feed, methane, cold chain, packaging, distribution | Efficient refrigeration, renewables, cattle-feed improvement |
| **Parle Agro / Bisleri** | Resin (PET) production, transportation, packaging | Lightweight bottles, recycled PET, solar electricity, rail transport |

*"LCA reduces the impact substantially."* The general pattern: in heavy industry the hotspot is **process energy and raw materials**; in food it is the **farm stage (methane, feed)**; in packaged beverages it is the **packaging material**.

### 7. LCA in supply-chain management 📘 ⭐⭐
LCA supports supplier selection (compare suppliers' cradle-to-gate footprints), product and packaging design (eco-design), make-or-buy, mode and network choices, end-of-life strategy and claims substantiation. **"LCA supports Scope 3 accounting"** 📘 because Scope 3 categories (purchased goods, use of sold products, end-of-life) are life-cycle stages.

### 8. Advantages and limitations 📘 ⭐⭐⭐
| Advantages | Limitations |
|---|---|
| Scientific | Data-intensive |
| Transparent | Time-consuming |
| Decision support | Expensive |
| Identifies hotspots | Different assumptions give different answers |
| Supports ESG | Regional variation (grid mix, farming practices) |
| Supports eco-design | Allocation issues |
| Supports carbon neutrality | Interpretation complexity |

### 9. LCA software and trends 📘 ⭐
| Software | Type | Company |
|---|---|---|
| **OpenLCA** | Free | GreenDelta, Germany |
| **SimaPro** | Licence fee | PRé Sustainability, Netherlands |
| **GaBi** | 45-day free trial, then licence | Sphera, USA |
| **Umberto** | Licence fee | iPoint Systems, Germany |

**Emerging trends**: AI-enabled LCA, Digital Product Passport (EU DPP), blockchain traceability, real-time LCA, supplier digital twins, automated Scope 3 reporting.

**Key takeaways** 📘: LCA measures footprint across the entire life cycle; follows the ISO 14040 framework; supports sustainable product design, procurement and the circular economy; supports ESG; is an essential tool for operations managers.

---

## Part B — Life Cycle Sustainability Assessment (Lecture 5)

### 10. LCSA = E-LCA + S-LCA + LCC ⭐⭐⭐
Lecture 5 aligns with **UNEP/SETAC, ISO 14040/14044, ISO 15686-5** (life-cycle costing for buildings) and the **Klöpffer (2008)** LCSA framework: **LCSA = Environmental LCA + Social LCA + Life Cycle Costing.**

*Traditional LCA* = environmental impacts only. *Modern LCA = LCSA* covers all three pillars, so that a product is **environmentally friendly + socially ethical + economically viable**.

| Component | Question it answers | Example (Lecture 5) |
|---|---|---|
| **E-LCA** | "What happens to the environment?" | Manufacturing 1 laptop = **320 kg CO₂e + 18,000 L water + 850 MJ energy** |
| **S-LCA** | "What happens to people?" | Indian tea plantation: E-LCA low carbon, but S-LCA shows poor labour conditions → *not fully sustainable* |
| **LCC** | "What does it really cost over its life?" (TCO) | LED ₹250 / 25,000 h vs incandescent ₹40 / 1,000 h: LED has a higher purchase price but lower ownership cost, lower environmental impact and lower carbon footprint |

### 11. E-LCA example: petrol car vs electric car 📘 ⭐⭐⭐
| Life stage | Petrol car | Electric car |
|---|---|---|
| Raw materials | Medium | High (battery metals) |
| Manufacturing | Medium | High |
| Use phase | Very high emissions | Low emissions |
| Maintenance | Medium | Low |
| End-of-life | Recycling possible | Battery recycling critical |

*If only manufacturing is studied, the petrol car appears greener; if the entire life cycle is studied, the electric car generally has much lower lifetime emissions.* The carbon deck adds that on the Indian grid, a typical ICE car is about 7 t (manufacturing) + 18 t (use) ≈ 25 t; an EV on the Indian grid about 12 t + 16 t ≈ 28 t; an EV on a renewable grid about 10 t + 3 t ≈ 13 t. **The EV benefit depends on grid cleanliness.**

### 12. S-LCA impact categories (Lecture 5) 📘 ⭐⭐
| Stakeholder group | Issues |
|---|---|
| **Workers** | Child labour, forced labour, occupational safety, equal wages, working hours, gender equality |
| **Consumers** | Product safety, privacy, product quality |
| **Society / community** | Local employment, community development, indigenous rights, access to resources |
| **Governance (value chain)** | Ethical governance, corruption, human rights, fair competition |

(UNEP 2020 S-LCA guidelines use the stakeholder groups workers, local community, value-chain actors, consumers, society and children.)

### 13. Integrating the three: packaging choice 📘 ⭐⭐⭐
| Option | Environmental | Social | Cost |
|---|---|---|---|
| Plastic | Poor | Average | Low |
| Aluminium | Moderate | Moderate | High |
| Paper | Good | Good | Moderate |

- Decision on **cost only** → plastic.
- Decision on **E-LCA** → paper.
- Decision on **LCSA** → **paper from certified sustainable forests** (FSC/PEFC), because it balances environment, society and economics.

**Final framework** 📘: sustainability → environmental (E-LCA) + social (S-LCA) + economic (LCC) → LCSA. *To gain competitive advantage, a sustainable business must optimise environmental performance + social responsibility + economic value.*

---

## Part C — Carbon management, carbon accounting and carbon trading

### 14. Why carbon has become a business variable 📘 ⭐⭐⭐
- **Greenhouse gases**: atmospheric gases such as CO₂, CH₄ and N₂O that trap heat and cause global warming.
- **Global drivers**: climate change and net-zero commitments, investor ESG expectations, supply-chain decarbonisation, carbon border taxes.
- **Indian context**: SEBI **BRSR** reporting (mandatory for the top 1,000 listed companies), export competitiveness (**CBAM**), energy transition (the deck cites renewable/non-fossil capacity at about 54% of India's total).
- **Business reality**: **carbon = financial risk + opportunity.** *"Carbon emissions are now economic variables, not environmental topics."*

### 15. Carbon neutral vs net zero vs carbon zero vs climate positive 📘 ⭐⭐⭐
| Concept | Meaning |
|---|---|
| **Carbon neutral** | Emissions balanced through offsets |
| **Net zero** | Reduce emissions deeply (**90–95%**) and neutralise only the residual emissions (with removals) |
| **Carbon zero** | Near-zero emissions across operations and value chain |
| **Climate positive** | Removes more carbon than it emits |

### 16. The net-zero hierarchy 📘 ⭐⭐⭐
1. **Measure** — Scope 1, 2 and 3 emissions; calculate CO₂e.
2. **Reduce** — decarbonisation, energy efficiency, circularity, nature-based solutions.
3. **RE transition** — shift from fossil fuels to solar, wind, hydro; EV fleets; efficient and renewable energy use.
4. **Sustainable supply chain** — circularity, biodegradable packaging.
5. **Offset unavoidable emissions** — afforestation, **CCUS** (carbon capture, utilisation and storage).

**"Magic mantra: reduction first, offset later."** 📘 The deck frames the path as *"Carbon to competitive advantage: the roadmap to net zero 2050."*

### 17. ESG and its metrics (carbon deck) 📘 ⭐⭐
| Environmental | Social | Governance |
|---|---|---|
| GHG emissions (Scope 1, 2, 3); carbon intensity (tCO₂e per unit revenue or production) | Employee health & safety: LTIFR | Board independence: independent directors % |
| Energy efficiency & renewable adoption: RE % | Diversity, equity & inclusion: gender-diversity ratio | Audit & risk oversight: ESG-linked executive pay |
| Water withdrawal & discharge: water intensity | Human rights in supply chain; attrition rate | Anti-corruption policies; whistle-blower cases resolved |
| Waste & circular economy: waste recycled % | Community engagement: CSR spending | Executive-compensation alignment; customer data protection |
| Biodiversity impact; SBTi alignment; climate risk & resilience | Supply-chain audits | Compliance incidents |

*"ESG = business sustainability scorecard for future business."*

### 18. Global standards and frameworks 📘 ⭐⭐⭐
| Body / standard | Role |
|---|---|
| **GHG Protocol** (WRI + WBCSD) | Corporate accounting standard; introduced the **Scope 1, 2, 3** classification |
| **IPCC** | Scientific basis and emission factors; defines **GWPs** |
| **ISO 14064** | Formal standard for GHG quantification and **verification** |
| **UNFCCC** | Governs global reporting and national GHG inventories (Kyoto 1997, Paris 2015) |

*These frameworks make emissions auditable like financial data: standardisation, auditability, comparable reporting.*

**Reporting frameworks** 📘: **CDP** (climate change, water security, forests and deforestation, plastics and biodiversity); **GRI 305** (Scope 1, 2, 3; GHG intensity; reductions; ozone-depleting substances; NOx, SOx and other air emissions); **TCFD** (four pillars: governance, strategy, risk management, metrics and targets); **Integrated Reporting** (six capitals: financial, manufactured, intellectual, human, social and relationship, natural); **BRSR** (India: 9 principles, ~140 parameters; Section A general disclosure, Section B management and process, Section C principle-wise performance; P2 sustainable products and services, P6 environment).

### 19. Scope 1, 2 and 3 (GHG Protocol) 📘 ⭐⭐⭐
| Scope 1 — direct ("what you burn") | Scope 2 — energy indirect ("what you buy") | Scope 3 — value chain ("what you influence") |
|---|---|---|
| Fuel combustion (diesel in a plant generator) | Purchased grid electricity (e.g. MSEDCL power) | Purchased products and services from suppliers |
| Company vehicles (petrol in company cars) | Purchased heating (hot water for buildings) | Fuel and energy not in Scope 1 & 2 (mining coal, refining petrol) |
| Process emissions (chemical reactions in manufacturing, e.g. cement calcination) | Purchased cooling (energy for AC/refrigeration) | Product use and end-of-life treatment |
| Fugitive emissions (refrigerant leaks) | Purchased gases (hydrogen for an industrial process) | Logistics of inbound materials and outbound products |

- **Scope 3 is the most challenging and is often 70–90% (or more) of total emissions** 📘. In the course's automotive case Scope 1 + 2 are **under 5%** and Scope 3 **over 95%**; Tata Motors' BRSR shows "use of sold products" alone at about 96% of Scope 3.
- *"A company may reduce Scope 1 substantially while its total supply-chain footprint continues increasing → carbon accounting must follow the value chain"* (Lecture 10).
- **15 Scope 3 categories**: upstream 1 purchased goods & services, 2 capital goods, 3 fuel & energy-related, 4 upstream transport, 5 waste, 6 business travel, 7 employee commuting, 8 upstream leased assets; downstream 9 downstream transport, 10 processing of sold products, 11 use of sold products, 12 end-of-life of sold products, 13 downstream leased assets, 14 franchises, 15 investments.
- **Location-based vs market-based Scope 2**: location-based uses the average grid factor; market-based uses the factor of contracts actually bought (green PPAs, RECs).

### 20. Carbon accounting methodology (5 steps) 📘 ⭐⭐⭐
1. **Identify emission sources** scope-wise (natural-gas furnace, diesel generators, purchased electricity, logistics).
2. **Collect activity data** (litres of diesel, kWh of electricity, tonnes of steel purchased).
3. **Apply emission factors**: **Emissions = Activity data × Emission factor** (e.g. 10,000 litres diesel × 2.68 kg CO₂/l = 26,800 kg CO₂; sources IPCC, DEFRA, national databases).
4. **Convert to CO₂e** with GWP multipliers: CO₂e = emission × GWP.
5. **Aggregate and report.**
*"If you cannot measure carbon, then you cannot manage it!"*

### 21. The Kyoto basket of GHGs and GWPs (100-year) 📘 ⭐⭐
| Gas | Formula | GWP-100 | Note |
|---|---|---|---|
| Carbon dioxide | CO₂ | 1 | Rising sea levels, ocean acidification |
| Methane | CH₄ | ~27–30 | Melting glaciers, crop damage |
| Nitrous oxide | N₂O | ~273 | Ozone-layer thinning, soil and water pollution |
| Hydrofluorocarbons | HFCs | 12–14,000 | Refrigerants |
| Perfluorocarbons | PFCs | 7,000–12,000 | Very long lifetime (50,000+ years) |
| Sulphur hexafluoride | SF₆ | ~25,200 | Switchgear; lifetime 3,200+ years |
| Nitrogen trifluoride | NF₃ | ~17,000 | Electronics manufacturing; lifetime ~500–750 years |

### 22. Financial accounting vs carbon accounting 📘 ⭐⭐
| Attribute | Financial accounting | Carbon accounting |
|---|---|---|
| Measure | Currency | CO₂e |
| Record | Ledger | Emission inventory |
| Source | Cost centres | Emission sources |
| Assessment | Audit | Verification |
| Results | Profitability | Carbon intensity |

Emerging concept: the **carbon ledger**; new roles: carbon accountants, ESG controllers.

### 23. MRV — Measure, Report, Verify 📘 ⭐⭐⭐
MRV is *the foundation of carbon accounting and ESG reporting.*
- **Measure**: collect activity and emission data (kWh, litres of diesel, m³ of natural gas, production units).
- **Report**: disclose emissions (ESG reports, BRSR, CBAM filings, CDP).
- **Verify**: independent validation (internal audit, third-party assurance, accredited agencies such as Bureau Veritas, TÜV, KBS).
Without MRV, carbon data lacks credibility, ESG disclosures become unreliable and export risk rises under CBAM. With MRV: trusted reporting, investor confidence, global competitiveness. *"MRV converts sustainability claims into measurable, auditable and business-relevant data."*

### 24. Carbon accounting software for India (carbon deck) 📘 ⭐
SAMESG Lite (MSMEs, BRSR), Greenly (France, SMEs), IBM Envizi (mid-large enterprises), Sprih (Pune; BRSR/GRI/TCFD), Bharat Carbon (Pune; MSMEs), CleanCarbon (Noida; CBAM exporters). They help MSMEs measure emissions, simplify ESG reporting, meet BRSR compliance and compete globally.

### 25. Carbon credits and carbon markets 📘 ⭐⭐⭐
- A **carbon credit** = **1 tonne of CO₂e** avoided, reduced or removed, verified and issued by a registry.
- Credits come from **avoided emissions** (solar, wind, biomass), **emission reductions** (methane capture) or **carbon removals** (afforestation, CCUS). Removal credits usually command higher prices.
- Deck examples: a 50 kW solar farm generates about 50–55 credits a year (₹45–60 thousand at ₹850–1,100 per credit); a 50 kW wind farm 50–80 a year; 50 acres of afforestation 0.2–0.8 t CO₂ per acre a year at ₹800–3,000 per credit; a 50-tonne methane-capture plant about 1,250 credits a year (about $25–30 thousand at $20 per credit, ≈ ₹23–28 lakh); a 50 kW biomass plant 200–500 a year. ([Numericals](p2-carbon-accounting-numericals.md))
- **Registries**: Verra (VCS), Gold Standard, American Carbon Registry, Climate Action Reserve.
- **Compliance market** (mandatory: EU ETS, national schemes) vs **voluntary market** (corporate commitments, net-zero pledges).
- **India's Carbon Credit Trading Scheme (CCTS)**, notified in 2023 under the Energy Conservation Act and operational from 2025–26, sets emission-intensity targets for energy-intensive sectors; firms that beat targets earn tradable credits. *"From carbon compliance to carbon competitiveness."*

### 26. Key takeaways of carbon management 📘
- Carbon is becoming a business currency: you must measure and manage it.
- Carbon accounting is the foundation: follow MRV and improve.
- Net zero is a business transformation journey, not an environmental project.
- Carbon credits create new value: environmental + financial.
- Future competitiveness = **Carbon + Cost + Technology + ESG.**
- New careers: carbon accounting, ESG reporting, sustainability analytics, carbon markets, climate-risk management.

---

## Quick exam answers ⭐⭐⭐
**Q1. Explain the four phases of LCA with an example.**
(1) Goal and scope: purpose, audience, functional unit (e.g. delivering 1 litre of drinking water), boundary (cradle-to-grave), assumptions. (2) Inventory: collect primary (plant, supplier, utility bills) and secondary (ecoinvent) data on inputs and outputs. (3) Impact assessment: convert flows into categories (climate change via GWP, water scarcity, ecotoxicity). (4) Interpretation: find hotspots (e.g. PET resin for Bisleri), run sensitivity, recommend (lightweight bottles, rPET, rail transport).

**Q2. Distinguish carbon neutral and net zero.**
Carbon neutral balances emissions with offsets, whatever the reduction. Net zero requires deep reductions (90–95% across Scopes 1–3, SBTi-aligned) and neutralises only residual emissions with permanent removals. "Reduction first, offset later."

**Q3. Why is Scope 3 the most important and the hardest?**
It is usually 70–90%+ of emissions (over 95% in the automotive case), but it sits outside the company's control: it depends on suppliers' data, customers' use and end-of-life, with 15 categories and heavy use of secondary data. Managing it needs supplier engagement, LCA and procurement levers.

**Q4. What is MRV and why does it matter for CBAM?**
Measure, Report, Verify. CBAM requires exporters to declare verified embedded emissions; without MRV the importer must use punitive default values, so verified data protects competitiveness.
