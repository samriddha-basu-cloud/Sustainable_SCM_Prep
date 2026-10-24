"""Bundle notes/*.md into assets/notes.js so the site works on Vercel and when index.html is opened directly.

Run after editing any note:  python3 build.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
NOTES = ROOT / "notes"

# Sidebar order and short labels. Any new .md file not listed here is appended at the end.
ORDER = [
    # (slug, sidebar label, tag, group)
    ("README", "About these notes & syllabus", "", "start"),
    ("rapid-revision", "Rapid Revision", "★", "start"),
    ("p1-supplier-selection-numericals", "CO2 Supplier Weighted Scoring", "P1", "focus"),
    ("p2-carbon-accounting-numericals", "CO3 Carbon Accounting (Scope 1-2-3)", "P2", "focus"),
    ("p3-network-logistics-numericals", "CO4 Networks, Logistics Cost & Distance", "P3", "focus"),
    ("p4-performance-measurement-numericals", "CO5 Performance Measurement", "P4", "focus"),
    ("p5-lca-energy-numericals", "LCA & Energy Numericals", "P5", "focus"),
    ("ch01-sscm-business-performance", "SSCM & Business Performance", "01", "chapters"),
    ("ch02-lca-carbon-footprints", "LCA & Carbon Footprints", "02", "chapters"),
    ("ch03-sustainable-procurement", "Sustainable Procurement", "03", "chapters"),
    ("ch04-sustainable-manufacturing", "Sustainable Manufacturing", "04", "chapters"),
    ("ch05-technology-quality-tools", "Technology & Quality Tools", "05", "chapters"),
    ("ch06-sustainable-logistics", "Sustainable Logistics", "06", "chapters"),
    ("ch07-network-design", "Designing the Sustainable Network", "07", "chapters"),
    ("ch08-performance-measurement", "Measuring SSCM Performance", "08", "chapters"),
    ("ch09-energy-sector", "Energy-Sector Supply Chain", "09", "chapters"),
    ("ch10-sscm-best-practices", "SSCM Best Practices", "10", "chapters"),
    ("case-studies", "Case Studies", "Case", "practice"),
    ("exam-questions-qna", "Exam Q&A Bank", "Q&A", "practice"),
    ("mcq-bank", "MCQ Bank", "MCQ", "practice"),
    ("glossary", "Glossary A–Z", "A–Z", "practice"),
]


def first_heading(md: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else fallback


def main() -> None:
    files = {p.stem: p for p in NOTES.glob("*.md")}
    entries = []
    for slug, label, tag, group in ORDER:
        if slug in files:
            md = files.pop(slug).read_text(encoding="utf-8")
            entries.append({"slug": slug, "label": label, "tag": tag, "group": group, "title": first_heading(md, label), "md": md})
    for slug, path in sorted(files.items()):
        md = path.read_text(encoding="utf-8")
        title = first_heading(md, slug)
        entries.append({"slug": slug, "label": title, "tag": "", "group": "practice", "title": title, "md": md})

    out = ROOT / "assets" / "notes.js"
    out.write_text("window.NOTES = " + json.dumps(entries, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} with {len(entries)} notes")


if __name__ == "__main__":
    main()
