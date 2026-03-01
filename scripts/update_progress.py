#!/usr/bin/env python3
"""Liest _status.yml aus jedem Kapitelordner und aktualisiert die
Fortschrittsbalken in der README.md automatisch."""

import pathlib
import re
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

# Reihenfolge der Kapitelordner (bestimmt Tabellenreihenfolge)
CHAPTER_DIRS = [
    "docs/expose",
    "01_einleitung",
    "02_rigor_theorie_stand_forschung",
    "03_forschungsdesign_methodik",
    "04_anforderungsanalyse_RQ1",
    "05_referenzarchitektur_RQ2",
    "06_evaluation_RQ3",
    "07_diskussion",
    "08_fazit_ausblick",
    "poc",
]

BAR_LENGTH = 20  # Anzahl Bloecke im Balken


def make_bar(percent: int) -> str:
    """Erzeugt einen Unicode-Fortschrittsbalken."""
    filled = round(percent / 100 * BAR_LENGTH)
    empty = BAR_LENGTH - filled
    return "\u2588" * filled + "\u2591" * empty


def load_status(chapter_dir: str) -> dict | None:
    """Liest _status.yml aus einem Kapitelordner."""
    path = REPO_ROOT / chapter_dir / "_status.yml"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_table(chapters: list[dict]) -> str:
    """Baut die Markdown-Fortschrittstabelle."""
    total = sum(c["progress"] for c in chapters)
    avg = round(total / len(chapters))
    overall_bar = make_bar(avg)

    lines = [
        f"> Gesamtfortschritt: `{overall_bar}` **{avg}%**",
        "",
        "| Kapitel | Fortschritt | % | Status |",
        "|---------|------------|---|--------|",
    ]
    for c in chapters:
        bar = make_bar(c["progress"])
        lines.append(
            f"| {c['kapitel']} | `{bar}` | {c['progress']}% | {c['status']} |"
        )
    return "\n".join(lines)


def update_readme(table: str) -> None:
    """Ersetzt den Fortschritts-Block in der README zwischen den Markern."""
    readme_path = REPO_ROOT / "README.md"
    content = readme_path.read_text(encoding="utf-8")

    marker_start = "<!-- PROGRESS-START -->"
    marker_end = "<!-- PROGRESS-END -->"

    pattern = re.compile(
        re.escape(marker_start) + r".*?" + re.escape(marker_end),
        re.DOTALL,
    )
    replacement = f"{marker_start}\n{table}\n{marker_end}"

    if pattern.search(content):
        new_content = pattern.sub(replacement, content)
    else:
        print("WARNUNG: Marker nicht gefunden — README nicht aktualisiert.")
        print(f"Bitte fuege '{marker_start}' und '{marker_end}' in die README ein.")
        return

    readme_path.write_text(new_content, encoding="utf-8")
    print(f"README aktualisiert — Gesamtfortschritt: {table.splitlines()[0]}")


def main() -> None:
    chapters = []
    for d in CHAPTER_DIRS:
        status = load_status(d)
        if status is None:
            print(f"WARNUNG: {d}/_status.yml nicht gefunden — uebersprungen.")
            continue
        chapters.append(status)

    if not chapters:
        print("Keine _status.yml Dateien gefunden.")
        return

    table = build_table(chapters)
    update_readme(table)


if __name__ == "__main__":
    main()
