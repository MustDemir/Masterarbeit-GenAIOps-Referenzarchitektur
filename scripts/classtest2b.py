#!/usr/bin/env python3
"""
Classification Regression Test for SSOT Inbox Workflow.
Tests 7 known Inbox PDFs against expected cluster + relevance color.

Usage (from Mac terminal):
    cd ~/Projects/genaiops-thesis
    python3 scripts/classtest2b.py

Requires:
    - ~/.codex/skills/literatur-ssot-workflow/scripts/process_literatur_ssot_inbox.py
    - ~/.codex/skills/literatur-ssot-workflow/config/ssot_workflow.json
    - OneDrive Inbox PDFs present
"""

import sys, os, json
from pathlib import Path

# --- Paths ---
SKILL_DIR = Path.home() / ".codex" / "skills" / "literatur-ssot-workflow"
SCRIPT_DIR = SKILL_DIR / "scripts"
CONFIG_PATH = SKILL_DIR / "config" / "ssot_workflow.json"

# OneDrive inbox
ONEDRIVE_BASE = Path.home() / "Library" / "CloudStorage" / "OneDrive-SRHFernhochschule"
INBOX_DIR = ONEDRIVE_BASE / "1. Onedrive_Masterarbeit" / "2. Literatur" / "Inbox" / "Meine Bibliothek" / "files"
CSV_PATH = ONEDRIVE_BASE / "1. Onedrive_Masterarbeit" / "2. Literatur" / "01_Literaturquellen" / "SSOT_GLIEDERUNG_CLUSTER_2026-03-07" / "00_ssot_mapping.csv"

# Add script dir to path so we can import the module
sys.path.insert(0, str(SCRIPT_DIR))

# --- Expected results (ground truth from manual assessment) ---
EXPECTED = {
    "Bommasani et al. - 2021 - On the Opportunities and Risks of Foundation Models.pdf": {
        "cluster": "02_01", "color": "ROT"
    },
    "Burns et al. - 2016 - Borg, Omega, and Kubernetes.pdf": {
        "cluster": "02_03", "color": "ORANGE"
    },
    "Huang et al. - 2025 - AAGATE An NIST AI Risk Management Framework-Ali.pdf": {
        "cluster": "02_04_02", "color": "ORANGE"
    },
    "Latona et al. - 2025 - The AI Review Lottery Widespread AI-Assisted Peer.pdf": {
        "cluster": "02_01", "color": "ROT"
    },
    "Lewis et al. - 2020 - Retrieval-Augmented Generation for Knowledge-Inten.pdf": {
        "cluster": "02_01", "color": "ORANGE"
    },
    "Vaswani et al. - 2017 - Attention Is All You Need.pdf": {
        "cluster": "02_01", "color": "ROT"
    },
    "Wei et al. - 2022 - Emergent Abilities of Large Language Models.pdf": {
        "cluster": "02_02", "color": "ORANGE"
    },
}


def main():
    # --- Validate paths ---
    for label, p in [("Script dir", SCRIPT_DIR), ("Config", CONFIG_PATH),
                     ("Inbox", INBOX_DIR), ("CSV", CSV_PATH)]:
        if not p.exists():
            print(f"FEHLER: {label} nicht gefunden: {p}")
            sys.exit(1)

    # --- Import module ---
    try:
        import process_literatur_ssot_inbox as mod
    except ImportError as e:
        print(f"FEHLER: Import fehlgeschlagen: {e}")
        sys.exit(1)

    # --- Load config + CSV ---
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    import csv
    with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter=";"))

    used_names = {}  # MUST be dict, not set

    # --- Find test PDFs ---
    inbox_pdfs = []
    for name in EXPECTED:
        pdf_path = INBOX_DIR / name
        if pdf_path.exists():
            inbox_pdfs.append((name, pdf_path))
        else:
            # Try fuzzy match
            found = False
            for f in INBOX_DIR.glob("*.pdf"):
                if name[:30] in f.name:
                    inbox_pdfs.append((name, f))
                    found = True
                    break
            if not found:
                print(f"  WARNUNG: {name} nicht in Inbox gefunden — überspringe")

    print(f"\n{'='*70}")
    print(f"SSOT Classification Regression Test")
    print(f"{'='*70}")
    print(f"Config: {CONFIG_PATH}")
    print(f"Inbox:  {INBOX_DIR}")
    print(f"PDFs:   {len(inbox_pdfs)} / {len(EXPECTED)} gefunden")
    print(f"{'='*70}\n")

    # --- Classify each PDF ---
    cluster_ok = 0
    color_ok = 0
    total = len(inbox_pdfs)

    for name, pdf_path in inbox_pdfs:
        exp = EXPECTED[name]

        # Use detect_format() like main() does
        kind = mod.detect_format(pdf_path)

        try:
            row, cname = mod.classify_candidate(pdf_path, kind, cfg, rows, used_names)
        except Exception as e:
            print(f"  ❌ FEHLER bei {name}: {e}")
            continue

        actual_cluster = row.get("primary_cluster", "???")
        actual_color = row.get("relevance_color", "???")

        # Extract cluster short name (e.g. "02_01" from full path)
        cluster_short = ""
        for part in actual_cluster.split("/"):
            if part.startswith("0") and "_" in part:
                cluster_short = part
                break

        c_match = exp["cluster"] in actual_cluster
        f_match = actual_color == exp["color"]

        if c_match:
            cluster_ok += 1
        if f_match:
            color_ok += 1

        status_c = "✅" if c_match else "❌"
        status_f = "✅" if f_match else "❌"

        short_name = name[:55]
        print(f"  {status_c} Cluster: {cluster_short:15s}  (erwartet: {exp['cluster']:10s})  |  "
              f"{status_f} Farbe: {actual_color:8s} (erwartet: {exp['color']:8s})  |  {short_name}")

        # Show score details on mismatch
        if not c_match or not f_match:
            score = row.get("score", "?")
            rationale = row.get("rationale", "?")
            print(f"       → score={score}, rationale={rationale}")
            if row.get("secondary_clusters"):
                print(f"       → secondary: {row['secondary_clusters']}")

    # --- Summary ---
    print(f"\n{'='*70}")
    print(f"ERGEBNIS: Cluster {cluster_ok}/{total}, Farbe {color_ok}/{total}")
    if cluster_ok == total and color_ok == total:
        print("✅ ALLE TESTS BESTANDEN — Workflow ist stabil!")
    else:
        print("⚠️  Regressionen erkannt — Details oben prüfen")
    print(f"{'='*70}\n")

    return 0 if (cluster_ok == total and color_ok == total) else 1


if __name__ == "__main__":
    sys.exit(main())
