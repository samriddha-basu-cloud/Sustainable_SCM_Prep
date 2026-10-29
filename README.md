# SSCM Prep — Sustainable Supply Chain Management

End-semester study site for **Sustainable Supply Chain Management** (MBA Operations Management, 2025–27). An **Exam Focus** tab follows the announced 40-mark pattern (CO3 and CO4 10 marks each, CO2 and CO5 7 marks each, CO1 and CO6 3 marks each) with exam-format questions and model answers. The site covers all ten syllabus topics, with full worked answers to every numerical in the course slides and extra practice problems:

- **CO2**: weighted scoring of suppliers (scorecards, TOPSIS, risk matrix, AHP, Kraljic, TCO)
- **CO3**: carbon accounting, Scope 1, 2 and 3 emissions (GWP, inventories, BRSR, carbon credits)
- **CO4**: sustainable distribution networks, logistics cost and distance criteria
- **CO5**: effective performance measurement systems (OTIF, OEE, dashboards, BSC, TAS)
- **CO1 & CO6**: 3-mark theory, plus a 170-question MCQ bank, a Q&A bank, case studies and a glossary with flashcards and a quiz

## Structure
- `notes/*.md`: the content, one Markdown file per page
- `build.py`: bundles the notes into `assets/notes.js` (run `python3 build.py` after editing a note)
- `index.html`, `assets/app.js`, `assets/style.css`: the static single-page app (uses marked v12, bundled)

## Run or deploy
Open `index.html` directly in a browser, or deploy the folder as a static site on Vercel (`vercel.json` is included, no build step needed).
