# Designing a Sustainable Supply Chain Network
Syllabus topic 7 📘 (Lecture 8: "Designing a sustainable supply chain network model incorporating green logistics, reverse logistics and circular-economy principles"). It is the theory behind **CO4 (SSCM distribution networks)**, the **10-mark** network design numerical. The network numericals (network A/B/C with λ break-evens, the 10,000-returns allocation, the consumer-electronics exercise, centre of gravity, load-distance, factor rating, number of DCs) are on [Network & Logistics Numericals](p3-network-logistics-numericals.md).

**Learning objectives (Lecture 8)** 📘: (1) explain sustainable SC network design; (2) distinguish forward, reverse and closed-loop logistics; (3) integrate green logistics into network decisions; (4) apply circular-economy principles to network design; (5) identify appropriate facilities and material flows; (6) formulate a basic sustainable network-optimisation model; (7) evaluate economic, environmental and social trade-offs; (8) analyse real Indian and international cases.

---

## Section A — Why network design must change

### 1. The traditional network ignores half the picture 📘 ⭐⭐⭐
The traditional chain (supplier → manufacturer → warehouse → distributor → retailer → customer) often ignores **CO₂ emissions, resource depletion, packaging waste, product returns, end-of-life products, recycling opportunities and social impacts**. **Key message: "The supply chain does not end at the customer."**

The sustainable network adds a **reverse flow**: customer → collection centre → inspection and sorting → repair / reuse / remanufacture / recycle → back to the manufacturer or a secondary market. *The sustainable supply chain moves from linear to closed loop.*

### 2. Why network design matters 📘 ⭐⭐⭐
**Strategic network decisions determine**: number of factories, warehouse locations, distribution centres, collection centres, recycling facilities, remanufacturing plants, transport modes, supplier locations and customer allocation.
- **A poor network creates**: longer distances → higher fuel consumption → higher CO₂ emissions → higher cost.
- **A circular network creates**: recovery → reuse → lower virgin-material demand → lower waste → lower environmental impact ("circularity creates a positive impact at every step").

**Network objective: Cost + Carbon + Resources + Resilience + Social value.** 📘

Because most cost and emissions are locked in when facilities and flows are chosen (a DC built in the wrong place adds truck-km every day for 20 years), network design is the most leveraged sustainability decision in logistics.

### 3. The three pillars of sustainable network design 📘 ⭐⭐
| Environmental (Planet) | Social (People) | Economic (Profits) |
|---|---|---|
| Which network produces the lowest environmental impact? | Which network creates acceptable social value? | Which network is of lowest cost? |

*The network must be environmentally friendly + socially ethical + economically viable.* (Lecture 9 adds resilience as the fourth pillar.)

### 4. From cost optimisation to sustainability optimisation 📘 ⭐⭐⭐
| Traditional | Sustainable |
|---|---|
| **Minimise** transportation cost + facility cost + inventory cost + procurement cost = **minimise total supply-chain cost** | **Minimise** cost + λ₁ CO₂ + λ₂ waste + λ₃ resource consumption |
| | **While maintaining**: customer service (desired service levels), capacity (operate within available capacity), demand satisfaction (meet demand on time), regulatory compliance (laws and standards), recovery targets (return and recovery goals) |

The λ weights convert CO₂, waste and resources into the same units as cost (for example λ₁ = a carbon price in ₹ per tonne).

---

## Section D — Circular economy in the network

### 5. Linear vs circular 📘 ⭐⭐⭐
*"Circularity seeks to retain products, components and materials in productive use and reduce waste."* UNEP emphasises **redesign, reuse, repair, remanufacturing and recycling** as the key circularity mechanisms. SCM is "cradle to grave"; SSCM is "cradle to cradle". (The Ellen MacArthur Foundation's three principles: eliminate waste and pollution, circulate products and materials at their highest value, regenerate nature.)

### 6. Material loops — biological and technical cycles 📘 ⭐⭐
- **Biological cycle**: biological resources → organic material → use → compost / regeneration → back to biological resources (food, cotton, wood, bio-packaging).
- **Technical cycle**: product → use → repair → reuse → remanufacture → recycle → new product (metals, plastics, electronics).

### 7. The R-strategy hierarchy (highest value first) 📘 ⭐⭐⭐
| # | Strategy | Meaning | Slide example |
|---|---|---|---|
| 1 | **Refuse** | Don't accept products you don't need | Refuse plastic straws |
| 2 | **Reduce** | Use fewer resources and less material | Buy products with minimal packaging |
| 3 | **Reuse** | Use items again for the same purpose | Reusable water bottle |
| 4 | **Repair** | Fix and extend the life of products | Repair a torn backpack |
| 5 | **Refurbish** | Restore and update to good working condition | Refurbish an old sofa |
| 6 | **Remanufacture** | Rebuild to like-new condition with warranty | Remanufactured car alternator |
| 7 | **Repurpose** | Use items for a different purpose | Old boots turned into planters |
| 8 | **Recycle** | Process materials to create new products | Recycle paper into new paper |

**Each R-strategy requires different elements** 📘: facilities, transportation, skills, technology, inventory and information systems. **Key principle: "Recycling is usually lower in the value-retention hierarchy than reuse, repair and remanufacturing."**

### 8. Circular design changes the supply chain 📘 ⭐⭐⭐
**Products designed for**:
1. **Disassembly** → easier recovery.
2. **Modularity** → easier repair.
3. **Durability** → longer life.
4. **Standardised components** → easier remanufacturing.
5. **Material identification** → easier recycling.
*"Sustainable network design begins at product design, not at the warehouse."*

### 9. Product as a Service (PaaS) 📘 ⭐⭐⭐
| Category | Example |
|---|---|
| Equipment leasing | CNH: harvester machine rental |
| Industrial machinery as a service | SDLG: leasing construction equipment |
| Battery-as-a-service (BaaS) | JSW MG Motor: Windsor EV (battery rented per km) |
| Lighting-as-a-service | Philips / Signify solutions (pay for light, not bulbs) |
| Furniture leasing | Furlenco: subscribe to furniture |

**The manufacturer retains economic incentive + physical control + material value**, so it has a reason to design durable, repairable products and to take them back.

### 10. Circular economy requires a different network — it becomes multidirectional 📘 ⭐⭐⭐
Traditional network: supplier → factory → DC → customer. Circular network: the same forward chain **plus** customer → collection → sorting → reuse / repair / remanufacture / recycle, feeding back into the factory, the DC or secondary markets.

---

## Section E — The sustainable network model

### 11. The closed-loop sustainable network model and its nine nodes 📘 ⭐⭐⭐
| Node | Role |
|---|---|
| 1. **Suppliers** | Provide raw materials, components and parts; ensure quality and timely supply |
| 2. **Manufacturing plants** | Convert inputs into finished goods; ensure quality, efficiency and compliance |
| 3. **Distribution centres** | Store finished goods; manage inventory and outbound shipments |
| 4. **Customers** | Purchase and use products; provide feedback and return products |
| 5. **Collection centres** | Collect end-of-life or returned products; consolidate and transport |
| 6. **Inspection / sorting centres** | Inspect returned items; sort by condition, type and material |
| 7. **Repair / remanufacturing / recycling** | Repair usable items; remanufacture to like-new; recycle what can't be reused |
| 8. **Recovered materials** | Recover metals, plastics and other materials; ensure quality and purity |
| 9. **Manufacturing (again)** | Use recovered materials as inputs; close the loop and reduce virgin resource use |
*"This is a closed-loop sustainable supply chain network."*

### 12. Network flows and decision levels 📘 ⭐⭐⭐
**Critical insight: a circular supply chain requires physical + information + financial integration.**

| Level | Decisions | Role |
|---|---|---|
| **Strategic** | Location of factories, DCs, collection centres and recycling facilities; capacity | *Strategic sets the network* |
| **Tactical** | Which customers are served by which DC; which returns go to which recovery facility; which transport mode | *Tactical connects the network* |
| **Operational** | Routing, collection frequency, shipment consolidation, inventory allocation | *Operational makes it perform* |

### 13. Objective function — a simplified sustainable network 📘 ⭐⭐⭐
**Minimise: Total cost + Environmental cost + Social cost**
- **Total cost** = facility cost + production cost + transportation cost + inventory cost + collection cost + recovery cost + disposal cost.
- **Environmental** = CO₂ emissions + energy consumption + waste + resource consumption.
- Example: Network A ₹100, CO₂ 100, recovery 20%; Network B ₹108, 75, 50%; Network C ₹115, 55, 70%. *"The model searches for a Pareto-efficient solution."* Which is best? *"There is no single answer without defining decision-maker priorities."* (Worked: A is best below λ = 0.32, B between 0.32 and 0.35, C above 0.35. See [P1](p3-network-logistics-numericals.md).)

### 14. Basic mathematical model 📘 ⭐⭐⭐
- **Decision variables**: xᵢⱼ = quantity transported from node i to node j; yⱼ = 1 if facility j is opened (binary); rᵢ = quantity recovered from returned products.
- **Objective**: **Minimise Z = C_total + λ·E_CO₂ + μ·W_waste.**
- **Subject to**: demand satisfaction; facility capacity; material balance; transport capacity; recovery capacity; collection constraints; recycling targets; non-negative flow.
- **At every recovery facility: Returns = Reuse + Repair + Remanufacture + Recycling + Disposal.**
- Example: 10,000 returned units → 2,000 reuse, 2,500 repair, 2,000 remanufacture, 3,000 material recycling, 500 disposal. *"Where should each stream go to minimise cost and environmental impact?"* ([worked](p3-network-logistics-numericals.md))

This is a **mixed-integer linear programme (MILP)**: binary yⱼ for open/close decisions and continuous xᵢⱼ and rᵢ for flows. Multi-objective versions are solved by weighting (as above), by ε-constraint (minimise cost subject to CO₂ ≤ cap) or by tracing the Pareto frontier.

### 15. The integrated sustainable network — four questions 📘 ⭐⭐⭐
1. **Where should facilities be located?**
2. **Which flows should move between facilities?**
3. **Which transportation mode should be used?**
4. **What should happen to returned products?**
These four decisions determine much of the network's **cost + carbon + circularity**. **Key message: green logistics overlays the entire network.**

### 16. Facility-location methods you can apply (distance criteria) ⭐⭐⭐
The syllabus's "distance criteria" are answered with:
- **Load-distance (tonne-km) method**: choose the candidate site that minimises Σ (load × distance). Tonne-km is a direct proxy for transport cost and CO₂.
- **Centre of gravity**: Cx = Σ xᵢWᵢ ÷ ΣWᵢ, Cy = Σ yᵢWᵢ ÷ ΣWᵢ; gives a starting point, then test nearby feasible sites.
- **Factor rating**: weighted scoring of qualitative and quantitative factors (land cost, labour, RE availability, rail access, flood risk, community impact).
- **Break-even (locational cost-volume) analysis**: fixed + variable cost lines per site.
- **Number of DCs trade-off**: more DCs → shorter outbound km (lower transport cost and CO₂) but higher facility and inventory cost (square-root law of inventory). The cost-optimal and carbon-optimal number of DCs often differ ([P7](p3-network-logistics-numericals.md)).
- **MILP network models** (as above) for real decisions.

### 17. Sustainable network KPI dashboard 📘 ⭐⭐⭐
| Environmental | Circularity | Economic | Service |
|---|---|---|---|
| kg CO₂e per unit | Return rate | Total logistics cost | Order fill rate % |
| Transport emissions | Recovery rate | Cost per unit | Delivery time |
| Energy per unit | Reuse rate | Inventory cost | Return turnaround time |
| Waste to landfill | Remanufacture rate | Facility utilisation | |
| Renewable energy % | Recycled content %; material circularity % | | |

**Final design objective** 📘: *"Create the lowest-cost network that delivers the required service while minimising environmental impact and maximising resource circularity."*

**The final framework** 📘: *"The sustainable supply chain is not a chain. It is a network of forward and reverse value loops."*

---

## 18. Case studies 📘 ⭐⭐⭐
**International**
- **IKEA (Sweden) — circular business model**: *"Why they WANT you to return your old furniture."* IKEA's circular agenda extends product life through **repair, buy-back, resale and recycling** (Buy Back & Resell, spare parts, as-is sections), with a goal to be a circular business by 2030.
- **Renault Refactory (Flins, France)**: a facility dedicated to the circular economy of mobility. Activities: **vehicle refurbishment, battery repair, parts remanufacturing, second-life applications, material recycling and industrial retrofitting.**

**Indian**
- **Mahindra CERO** (JV of Mahindra and MSTC Ltd., Government of India): India's first authorised **vehicle-recycling** facilities (end-of-life vehicles dismantled, materials recovered), relevant under India's Vehicle Scrappage Policy.
- **Tata Motors Prolife**: **remanufacturing** as part of a circular network (used aggregates such as engines and gearboxes are reconditioned and sold with warranty). *"An excellent example of remanufacturing rather than recycling by using used parts."*

---

## 19. The consumer-electronics network exercise (Lecture 8) 📘 ⭐⭐⭐
A consumer-electronics company has 3 suppliers, 2 plants, 4 regional DCs, 10,000 customers and 20% expected returns. It is considering one centralised recycling centre, two regional collection centres and one remanufacturing facility.

| Decision | Option A | Option B |
|---|---|---|
| Collection | Centralised | Regional |
| Transport | Road | Rail + road |
| Recovery | Recycle | Remanufacture |
| Warehouse | Conventional | Solar |
| Packaging | Single-use | Returnable |

*Evaluate cost, CO₂, recovery and service. Question: should the company select the cheapest network?* **Answer: no** — Option B usually costs more in facilities but recovers far more value (remanufactured units sell at a premium over scrap), cuts CO₂ through rail and solar, and meets EPR targets; the best sustainable network is not necessarily the cheapest. Full numbers: [P10](p3-network-logistics-numericals.md).

## 20. Key takeaways (Lecture 8) 📘 ⭐⭐⭐
- Green logistics reduces the environmental impact of movement.
- Reverse logistics brings products and materials back.
- The circular economy retains value and resources.
- Network design determines where these activities occur.
- Optimisation must balance **cost, carbon, circularity and service**.
- **The best sustainable network is not necessarily the cheapest network.**
- **Design the forward and reverse network together.**

---

## Quick exam answers ⭐⭐⭐
**Q1. Write the objective function of a sustainable network model and explain its terms.**
Minimise Z = C_total + λ·E_CO₂ + μ·W_waste, where C_total = facility + production + transport + inventory + collection + recovery + disposal cost, E_CO₂ is total emissions priced at λ, and W_waste is waste priced at μ. Decision variables xᵢⱼ (flows), yⱼ (open facility) and rᵢ (recovered quantity); constraints on demand, capacity, material balance, recovery and recycling targets.

**Q2. Distinguish strategic, tactical and operational network decisions.**
Strategic: where and how big facilities are (sets the network). Tactical: allocation of customers to DCs, returns to recovery sites, choice of modes (connects it). Operational: routing, collection frequency, consolidation, inventory allocation (makes it perform).

**Q3. Why does circularity need a different network?**
Because flows become multidirectional: collection, inspection and sorting, repair, remanufacturing and recycling nodes must be added, each needing different facilities, transport, skills, technology, inventory and information systems, and the network must be designed together with the product (disassembly, modularity, standard parts).
