#!/usr/bin/env python3
"""Validate repository structure conventions for thesis workflow."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

CHAPTER_DIRS = [
    "01_einleitung",
    "02_rigor_theorie_stand_forschung",
    "03_forschungsdesign_methodik",
    "04_anforderungsanalyse_RQ1",
    "05_referenzarchitektur_RQ2",
    "06_evaluation_RQ3",
    "07_diskussion",
    "08_fazit_ausblick",
]

REQUIRED_DOCS = [
    "docs/thesis_state.md",
    "docs/roter_faden_tracker.md",
    "docs/SSOT_ROTER_FADEN_ANALYSE.md",
]

REQUIRED_ADMIN = [
    "00_admin/SOURCE_OF_TRUTH.md",
    "00_admin/gliederung_v3.md",
]

REQUIRED_DECISION_PAPERS = [
    "docs/ENTSCHEIDUNGSPAPIER_KAP4.md",
    "docs/ENTSCHEIDUNGSPAPIER_KAP5.md",
]


def check_chapter_dirs() -> list[str]:
    issues: list[str] = []
    for name in CHAPTER_DIRS:
        d = ROOT / name
        if not d.is_dir():
            issues.append(f"Chapter directory missing: {name}/")
    return issues


def check_required_files(paths: list[str], label: str) -> list[str]:
    issues: list[str] = []
    for rel in paths:
        if not (ROOT / rel).exists():
            issues.append(f"{label} missing: {rel}")
    return issues


def check_expose_dir() -> list[str]:
    warnings: list[str] = []
    expose_dir = ROOT / "docs" / "expose"
    if not expose_dir.is_dir():
        warnings.append("docs/expose/ directory not found (informational)")
    return warnings


def check_session_summaries() -> list[str]:
    issues: list[str] = []
    for d in ROOT.rglob("session_summaries"):
        if not d.is_dir():
            continue
        for p in d.rglob("*"):
            if p.is_dir():
                issues.append(f"Directory inside session_summaries not allowed: {p.relative_to(ROOT)}")
                continue
            if p.name in {".DS_Store", ".gitkeep"}:
                continue
            if p.suffix.lower() != ".yaml":
                issues.append(f"Non-YAML in session_summaries: {p.relative_to(ROOT)}")
    return issues


def check_final_images() -> list[str]:
    issues: list[str] = []
    pattern = re.compile(r"_v\d{2}\.png$", re.IGNORECASE)
    for p in ROOT.rglob("images/final/*.png"):
        if not pattern.search(p.name):
            issues.append(f"Final image missing _vNN suffix: {p.relative_to(ROOT)}")
    return issues


def main() -> int:
    issues: list[str] = []
    warnings: list[str] = []

    issues.extend(check_chapter_dirs())
    issues.extend(check_required_files(REQUIRED_DOCS, "Docs file"))
    issues.extend(check_required_files(REQUIRED_ADMIN, "Admin file"))
    issues.extend(check_required_files(REQUIRED_DECISION_PAPERS, "Entscheidungspapier"))
    issues.extend(check_session_summaries())
    issues.extend(check_final_images())
    warnings.extend(check_expose_dir())

    if issues:
        print("Structure validation FAILED:\n")
        for i in issues:
            print(f"- {i}")
        if warnings:
            print("\nWarnings:\n")
            for w in warnings:
                print(f"- {w}")
        return 1

    if warnings:
        print("Structure validation OK (with warnings):\n")
        for w in warnings:
            print(f"- {w}")
        return 0

    print("Structure validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
