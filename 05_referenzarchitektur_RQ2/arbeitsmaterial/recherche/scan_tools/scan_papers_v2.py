#!/usr/bin/env python3
"""
Systematic scan of all PDFs for D_GATE_INCLUSION_RULE relevance - Version 2.
Improved version with proper sorting and better output.
"""

import subprocess
import os
import re
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
SCAN_TOOLS_DIR = SCRIPT_PATH.parent
CHAPTER_DIR = SCRIPT_PATH.parents[3]
REPO_ROOT = SCRIPT_PATH.parents[4]
LITERATURE_BASE = REPO_ROOT / "00_admin" / "Literatur" / "SSOT_GLIEDERUNG_CLUSTER_2026-03-07"
RESULTS_FILE = SCAN_TOOLS_DIR / "scan_results_temp.txt"
OUTPUT_PATH = CHAPTER_DIR / "arbeitsmaterial" / "recherche" / "VOLLSTAENDIGER_PAPER_SCAN_2026-03-12.md"

# Define the papers that are already deep-read (skip these)
ALREADY_DEEP_READ = {
    "Cooper 2008", "Laux 2024", "Kholkar 2025", "Lucaj 2025", "Feng 2024",
    "Muhammad 2026", "Nweke 2026", "Elia 2023", "Elia 2025"
}

ALREADY_ABSTRACT_SCANNED = {
    "Antiya 2020", "Rebbana 2025", "Alugunuri 2022", "Adetayo 2023", "Sinan 2025"
}

GATE_KEYWORDS = {
    "quality_gates": ["quality gate", "gate", "checkpoint", "milestone"],
    "automation": ["automation", "automat", "policy-as-code", "policy as code", 
                   "compliance-as-code", "compliance as code"],
    "human_oversight": ["human oversight", "first-degree", "second-degree", "counterfactual"],
    "deliverables": ["deliverable", "acceptance criteria", "go/kill", "pass/fail"],
    "risk_based": ["risk-based", "risk based", "risk class", "high-risk"],
    "roles": ["provider", "deployer", "actor", "role"],
    "cross_cutting": ["cross-cutting", "cross cutting", "traceability", "OSCAL"]
}

def extract_paper_name(filepath):
    """Extract author/year from filename"""
    filename = os.path.basename(filepath)
    match = re.search(r'([A-Za-z\s]+?)\s*-\s*(\d{4})', filename)
    if match:
        author = match.group(1).strip()
        year = match.group(2)
        return f"{author} {year}"
    return filename

def should_skip(paper_name):
    """Check if paper should be skipped"""
    name_lower = paper_name.lower()
    for skip_name in ALREADY_DEEP_READ | ALREADY_ABSTRACT_SCANNED:
        if skip_name.lower() in name_lower:
            return True
    return False

def analyze_pdf(pdf_path):
    """Analyze single PDF for gate-relevant keywords"""
    paper_name = extract_paper_name(pdf_path)
    
    if should_skip(paper_name):
        return None
    
    try:
        result = subprocess.run(
            ['pdftotext', '-f', '1', '-l', '3', pdf_path, '-'],
            capture_output=True, text=True, timeout=10
        )
        
        if result.returncode != 0:
            return {
                'pdf': pdf_path, 'name': paper_name, 'relevance': 'ERROR',
                'matches': {}, 'error': 'PDF extraction failed'
            }
        
        text = result.stdout.lower()
        matches = {}
        for category, keywords in GATE_KEYWORDS.items():
            count = sum(text.count(kw.lower()) for kw in keywords)
            if count > 0:
                matches[category] = count
        
        total_matches = sum(matches.values())
        if total_matches >= 10:
            relevance = "CRITICAL"
        elif total_matches >= 5:
            relevance = "HIGH"
        elif total_matches >= 2:
            relevance = "MEDIUM"
        elif total_matches >= 1:
            relevance = "LOW"
        else:
            relevance = "IRRELEVANT"
        
        return {
            'pdf': pdf_path, 'name': paper_name, 'relevance': relevance,
            'matches': matches, 'total_matches': total_matches
        }
    except Exception as e:
        return {
            'pdf': pdf_path, 'name': paper_name, 'relevance': 'ERROR',
            'matches': {}, 'error': str(e)
        }

# Load previously saved results if they exist (to avoid re-scanning)
results_file = RESULTS_FILE
if os.path.exists(results_file):
    print("[INFO] Loading cached results...")
    with open(results_file, 'r') as f:
        import json
        results = json.load(f)
else:
    all_pdfs = []
    
    for root, dirs, files in os.walk(LITERATURE_BASE):
        for file in files:
            if file.endswith(".pdf"):
                all_pdfs.append(os.path.join(root, file))
    
    print(f"[INFO] Found {len(all_pdfs)} PDFs")
    
    results = []
    skipped = 0
    
    for idx, pdf_path in enumerate(all_pdfs):
        if idx % 50 == 0:
            print(f"[PROGRESS] {idx}/{len(all_pdfs)}")
        
        if should_skip(extract_paper_name(pdf_path)):
            skipped += 1
            continue
        
        result = analyze_pdf(pdf_path)
        if result:
            results.append(result)
    
    print(f"[INFO] Skipped: {skipped}, Analyzed: {len(results)}")
    
    # Cache results
    import json
    with open(results_file, 'w') as f:
        json.dump(results, f)

# Sort results properly
relevance_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "IRRELEVANT": 4, "ERROR": 5}
results.sort(key=lambda x: (relevance_order.get(x['relevance'], 6), -x.get('total_matches', 0)))

# Count by relevance
stats = {r: 0 for r in relevance_order}
for r in results:
    stats[r['relevance']] += 1

# Write output file
with open(OUTPUT_PATH, 'w') as f:
    f.write("# Vollständiger Systematischer Paper Scan\n")
    f.write("## D_GATE_INCLUSION_RULE Relevanzanalyse\n\n")
    f.write(f"**Scan-Datum:** 2026-03-12\n")
    f.write(f"**Gesamte PDFs gefunden:** {len(all_pdfs) if 'all_pdfs' in locals() else '335'}\n")
    f.write(f"**Übersprungen (bereits gelesen/gescannt):** {len(ALREADY_DEEP_READ) + len(ALREADY_ABSTRACT_SCANNED)}\n")
    f.write(f"**Neu gescannt:** {len(results)}\n\n")
    
    f.write("## Zusammenfassung nach Relevanz\n\n")
    for rel, count in [("CRITICAL", stats["CRITICAL"]), ("HIGH", stats["HIGH"]),
                       ("MEDIUM", stats["MEDIUM"]), ("LOW", stats["LOW"]),
                       ("IRRELEVANT", stats["IRRELEVANT"]), ("ERROR", stats["ERROR"])]:
        pct = (count / len(results) * 100) if results else 0
        f.write(f"- **{rel}:** {count} Papers ({pct:.1f}%)\n")
    f.write("\n")
    
    f.write("## CRITICAL Papers (höchste Priorität)\n\n")
    critical_papers = [r for r in results if r['relevance'] == 'CRITICAL']
    if critical_papers:
        for r in critical_papers:
            f.write(f"### {r['name']}\n")
            f.write(f"- **Matches:** {r['total_matches']} total\n")
            f.write(f"- **Path:** `{r['pdf']}`\n")
            if r.get('matches'):
                f.write(f"- **Categories:** {', '.join(r['matches'].keys())}\n")
            f.write("\n")
    else:
        f.write("Keine CRITICAL Papers gefunden.\n\n")
    
    f.write("## HIGH Papers\n\n")
    high_papers = [r for r in results if r['relevance'] == 'HIGH']
    if high_papers:
        for r in high_papers[:20]:  # Show first 20
            f.write(f"### {r['name']}\n")
            f.write(f"- **Matches:** {r['total_matches']} total\n")
            f.write(f"- **Path:** `{r['pdf']}`\n")
            if r.get('matches'):
                f.write(f"- **Categories:** {', '.join(r['matches'].keys())}\n")
            f.write("\n")
        if len(high_papers) > 20:
            f.write(f"... und {len(high_papers) - 20} weitere HIGH Papers\n\n")
    else:
        f.write("Keine HIGH Papers gefunden.\n\n")
    
    f.write("## Alle gescannten PDFs (sortiert nach Relevanz)\n\n")
    f.write("| # | Paper | Relevanz | Matches | Kategorien |\n")
    f.write("|---|-------|----------|---------|------------|\n")
    for idx, r in enumerate(results, 1):
        cats = ', '.join(r['matches'].keys()) if r.get('matches') else '-'
        matches_str = r.get('total_matches', 0) if r['relevance'] != 'ERROR' else 'N/A'
        f.write(f"| {idx} | {r['name'][:30]} | {r['relevance']} | {matches_str} | {cats[:30]} |\n")

print(f"[SUCCESS] Written {OUTPUT_PATH}")
print(f"[STATS] CRITICAL: {stats['CRITICAL']}, HIGH: {stats['HIGH']}, MEDIUM: {stats['MEDIUM']}, "
      f"LOW: {stats['LOW']}, IRRELEVANT: {stats['IRRELEVANT']}")
