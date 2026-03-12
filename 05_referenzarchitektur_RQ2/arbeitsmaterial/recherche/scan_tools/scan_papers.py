#!/usr/bin/env python3
"""
Systematic scan of all PDFs for D_GATE_INCLUSION_RULE relevance.
Scans first 3 pages of each unread PDF for gate-relevant keywords.
"""

import subprocess
import os
import re
from pathlib import Path

SCRIPT_PATH = Path(__file__).resolve()
CHAPTER_DIR = SCRIPT_PATH.parents[3]
REPO_ROOT = SCRIPT_PATH.parents[4]
LITERATURE_BASE = REPO_ROOT / "00_admin" / "Literatur" / "SSOT_GLIEDERUNG_CLUSTER_2026-03-07"
OUTPUT_PATH = CHAPTER_DIR / "arbeitsmaterial" / "recherche" / "VOLLSTAENDIGER_PAPER_SCAN_2026-03-12.md"

# Define the papers that are already deep-read (skip these)
ALREADY_DEEP_READ = {
    "Cooper 2008",
    "Laux 2024",
    "Kholkar 2025",
    "Lucaj 2025",
    "Feng 2024",
    "Muhammad 2026",
    "Nweke 2026",
    "Elia 2023",
    "Elia 2025"
}

# Already abstract-scanned (can skip)
ALREADY_ABSTRACT_SCANNED = {
    "Antiya 2020",
    "Rebbana 2025",
    "Alugunuri 2022",
    "Adetayo 2023",
    "Sinan 2025"
}

# Gate-relevant keywords/patterns
GATE_KEYWORDS = {
    "quality_gates": ["quality gate", "gate", "checkpoint", "milestone"],
    "automation": ["automation", "automat", "policy-as-code", "policy as code", "compliance-as-code", "compliance as code"],
    "human_oversight": ["human oversight", "first-degree", "second-degree", "counterfactual"],
    "deliverables": ["deliverable", "acceptance criteria", "go/kill", "pass/fail"],
    "risk_based": ["risk-based", "risk based", "risk class", "high-risk"],
    "roles": ["provider", "deployer", "actor", "role"],
    "cross_cutting": ["cross-cutting", "cross cutting", "traceability", "OSCAL"]
}

def extract_paper_name(filepath):
    """Extract author/year from filename"""
    filename = os.path.basename(filepath)
    # Pattern: "Author - YYYY - Title"
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
        # Extract first 3 pages with pdftotext
        result = subprocess.run(
            ['pdftotext', '-f', '1', '-l', '3', pdf_path, '-'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            return {
                'pdf': pdf_path,
                'name': paper_name,
                'relevance': 'ERROR',
                'matches': {},
                'error': 'PDF extraction failed'
            }
        
        text = result.stdout.lower()
        
        # Count keyword matches by category
        matches = {}
        for category, keywords in GATE_KEYWORDS.items():
            count = sum(text.count(kw.lower()) for kw in keywords)
            if count > 0:
                matches[category] = count
        
        # Determine relevance based on match count
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
            'pdf': pdf_path,
            'name': paper_name,
            'relevance': relevance,
            'matches': matches,
            'total_matches': total_matches
        }
    except Exception as e:
        return {
            'pdf': pdf_path,
            'name': paper_name,
            'relevance': 'ERROR',
            'matches': {},
            'error': str(e)
        }

def main():
    # Find all PDFs in literature folder
    all_pdfs = []
    
    for root, dirs, files in os.walk(LITERATURE_BASE):
        for file in files:
            if file.endswith(".pdf"):
                all_pdfs.append(os.path.join(root, file))
    
    print(f"[INFO] Found {len(all_pdfs)} PDFs in literature folder")
    
    # Analyze all PDFs
    results = []
    skipped = 0
    
    for idx, pdf_path in enumerate(all_pdfs):
        if idx % 50 == 0:
            print(f"[PROGRESS] Analyzing {idx}/{len(all_pdfs)}")
        
        paper_name = extract_paper_name(pdf_path)
        
        if should_skip(paper_name):
            skipped += 1
            continue
        
        result = analyze_pdf(pdf_path)
        if result:
            results.append(result)
    
    print(f"[INFO] Skipped {skipped} already-read/abstract-scanned papers")
    print(f"[INFO] Analyzed {len(results)} new PDFs")
    
    # Sort by relevance
    relevance_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "IRRELEVANT": 4, "ERROR": 5}
    results.sort(key=lambda x: (relevance_order.get(x['relevance'], 6), x.get('total_matches', 0)), reverse=True)
    
    # Save results to file
    with open(OUTPUT_PATH, 'w') as f:
        f.write("# Vollständiger Paper Scan für D_GATE_INCLUSION_RULE\n\n")
        f.write(f"**Scan-Datum:** 2026-03-12\n")
        f.write(f"**Gesamte PDFs gefunden:** {len(all_pdfs)}\n")
        f.write(f"**Bereits deep-gelesen (übersprungen):** {len(ALREADY_DEEP_READ)}\n")
        f.write(f"**Bereits abstract-gescannt (übersprungen):** {len(ALREADY_ABSTRACT_SCANNED)}\n")
        f.write(f"**Neu gescannt:** {len(results)}\n\n")
        
        # Summary statistics
        crit_count = sum(1 for r in results if r['relevance'] == 'CRITICAL')
        high_count = sum(1 for r in results if r['relevance'] == 'HIGH')
        med_count = sum(1 for r in results if r['relevance'] == 'MEDIUM')
        low_count = sum(1 for r in results if r['relevance'] == 'LOW')
        irrel_count = sum(1 for r in results if r['relevance'] == 'IRRELEVANT')
        error_count = sum(1 for r in results if r['relevance'] == 'ERROR')
        
        f.write("## Zusammenfassung\n\n")
        f.write(f"- **CRITICAL:** {crit_count} Papers\n")
        f.write(f"- **HIGH:** {high_count} Papers\n")
        f.write(f"- **MEDIUM:** {med_count} Papers\n")
        f.write(f"- **LOW:** {low_count} Papers\n")
        f.write(f"- **IRRELEVANT:** {irrel_count} Papers\n")
        f.write(f"- **ERROR:** {error_count} Papers\n\n")
        
        # Detailed results
        f.write("## Detaillierte Scan-Ergebnisse\n\n")
        
        for result in results:
            f.write(f"### {result['name']}\n\n")
            f.write(f"**Pfad:** `{result['pdf']}`\n\n")
            f.write(f"**Relevanz:** {result['relevance']}\n\n")
            
            if result.get('error'):
                f.write(f"**Fehler:** {result['error']}\n\n")
            elif result.get('matches'):
                f.write(f"**Keyword-Matches ({result.get('total_matches', 0)} total):**\n\n")
                for category, count in sorted(result['matches'].items(), key=lambda x: x[1], reverse=True):
                    f.write(f"- {category}: {count} matches\n")
                f.write("\n")
        
        # Appendix: All PDF paths
        f.write("## Appendix A: Alle gescannten PDF-Dateien\n\n")
        for idx, result in enumerate(results, 1):
            f.write(f"{idx}. `{result['pdf']}`\n")
    
    print(f"[SUCCESS] Results saved to {OUTPUT_PATH}")
    return results

if __name__ == '__main__':
    main()
