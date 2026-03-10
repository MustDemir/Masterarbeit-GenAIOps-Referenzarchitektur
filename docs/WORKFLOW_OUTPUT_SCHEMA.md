# Workflow Output Schema — Was der Thesis-Workflow produziert

> **Erstellt:** 2026-03-08 | **Zweck:** Dokumentation aller Dateien, die von Scripts + Skills erzeugt werden
> **Referenziert von:** `00_admin/SOURCE_OF_TRUTH.md`, `.skills/SKILL_OVERVIEW.md`

---

## 1. Scripts (Python-Workflow)

### save.py — Session speichern

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Session Summary YAML | `{KK}_*/session_summaries/YYYYMMDD_HHMMSS_*.yaml` | .gitignore | ✅ Hoch | Strukturierte Session-Daten (topic, bullets, decisions, tags) |
| Index | `.memory/index.json` | .gitignore | ✅ Mittel | Datei-Manifest fuer RAG/Resume, automatisch regenerierbar |
| Resume-Kontext | `.memory/resume_context.txt` | .gitignore | ✅ Mittel | Kompakter Kontext fuer Session-Start, automatisch regenerierbar |
| chapter_state.yaml Update | `{KK}_*/chapter_state.yaml` | TRACKED | ✅ Hoch | Progress-Update (interaktiv, nur wenn User bestaetigt) |
| Azure Blob Sync | (remote) | — | ✅ Optional | Summaries nach Azure Blob (nur mit --blob Flag) |

### resume.py — Kontext regenerieren

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Index | `.memory/index.json` | .gitignore | ✅ Mittel | Regeneriert aus allen chapter_state.yaml + Summaries |
| Resume-Kontext | `.memory/resume_context.txt` | .gitignore | ✅ Mittel | Regeneriert |
| Thesis State | `docs/thesis_state.md` | TRACKED | ✅ Hoch | Schicht-1-SSOT: Decisions, Definitionen, Status aller Kapitel |

### reindex.py — Index neu bauen

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Index | `.memory/index.json` | .gitignore | ✅ Mittel | Regeneriert |
| Resume-Kontext | `.memory/resume_context.txt` | .gitignore | ✅ Mittel | Regeneriert |
| Azure Search Push | (remote) | — | ✅ Optional | Nur mit --azure Flag |
| Azure Blob Push | (remote) | — | ✅ Optional | Nur mit --blob Flag |

---

## 2. Skills (Claude-Workflow)

### thesis-preflight

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Preflight-Protokoll | `docs/preflight/PREFLIGHT_KAP{N}_{M}_{TITEL}.md` | TRACKED | ✅ Hoch | Argumentationsstruktur, Quellen-Zuordnung, Negativ-Checklist |

### thesis-writer

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| DRAFT Markdown | `{KK}_*/{N}_{M}_{thema}_DRAFT.md` | TRACKED | ✅ Hoch | Fliesstext-Entwurf mit Pruefprotokollen |
| DOCX Update | `00_workspace/Fulltext_Kapitel/*.docx` | TRACKED | ✅ Kritisch | Abgabe-Volltext (SSOT fuer Fliesstext) |

### thesis-reviewer

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Bewertungsbericht | `docs/bewertung/BEWERTUNG_KAP{N}_*.md` | TRACKED | ✅ Hoch | R1-R6 Scoring (Struktur, Roter Faden, Stil, Zitationen, Scope, Gutachter) |

### thesis-post-session

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Session-Zusammenfassung | `docs/bewertung/SESSION_*_ZUSAMMENFASSUNG.md` | TRACKED | ✅ Mittel | Tagesuebersicht: was gemacht, was offen |
| chapter_state.yaml Update | `{KK}_*/chapter_state.yaml` | TRACKED | ✅ Hoch | Status-Update nach Session |

### thesis-consistency

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| Konsistenz-Ueberblick | `{KK}_*/KONSISTENZ_UEBERBLICK_KAP{N}.md` | TRACKED | ✅ Hoch | Cross-Chapter-Analyse, Redundanz-Matrix |

### thesis-session-manager

| Output-Datei | Pfad-Muster | Git | Nuetzlich | Beschreibung |
|-------------|-------------|-----|-----------|-------------|
| (keine eigenen Dateien) | — | — | — | Liest chapter_state.yaml + resume_context.txt, erzeugt keine neuen Dateien |

---

## 3. Veraltete / Archivierte Dateien

| Datei | Pfad-Muster | Status | Ersetzt durch | Aktion |
|-------|-------------|--------|--------------|--------|
| **_status.yml** | `{KK}_*/_status.yml` (10 Dateien) | ❌ VERALTET | `chapter_state.yaml` | Archiviert 2026-03-08 |
| ~~.memory/sync_states~~ | `.memory/sync_states/` | ⚠ Intern | — | Bleibt (.gitignore), Azure-Sync-State |

### Vergleich _status.yml vs. chapter_state.yaml (Archivierungsgrund)

| Kapitel | _status.yml | chapter_state.yaml | Abweichung |
|---------|------------|-------------------|-----------|
| Kap. 1 | 10% | 100% | ❌ Massiv veraltet |
| Kap. 2 | 15% | 50% | ❌ Massiv veraltet |
| Kap. 3 | 95% | 95% | ✅ |
| Kap. 4 | 83% | 85% | ⚠ Minor |
| Kap. 5 | 20% | 20% | ✅ |
| Kap. 6-8 | 0% | 0% | ✅ |
| Expose | 100% | 100% | ✅ |
| PoC | 0% | 0% | ✅ |

---

## 4. Datei-Hierarchie (Nuetzlichkeit)

```
Kritisch (SSOT, Abgabe):
├── 00_workspace/Fulltext_Kapitel/*.docx     ← Abgabe-Texte
├── {KK}_*/chapter_state.yaml               ← Kapitel-Status + Decisions
├── docs/thesis_state.md                     ← Aggregierter Thesis-State (Schicht 1)
├── docs/roter_faden_tracker.md              ← Cross-Chapter-Argumentationskette
└── 00_admin/gliederung_v3.md                ← Kapitelstruktur + Seitenbudgets

Hoch (Qualitaetssicherung):
├── docs/preflight/PREFLIGHT_*.md            ← Preflight-Protokolle
├── docs/bewertung/BEWERTUNG_*.md            ← Reviewer-Bewertungen
├── {KK}_*/{N}_{M}_*_DRAFT.md               ← Working Drafts mit Pruefprotokollen
└── {KK}_*/KONSISTENZ_UEBERBLICK_*.md        ← Konsistenz-Analysen

Mittel (Kontext/RAG):
├── {KK}_*/session_summaries/*.yaml          ← Session-Daten (.gitignore)
├── .memory/index.json                       ← Datei-Manifest (.gitignore)
├── .memory/resume_context.txt               ← Session-Resume (.gitignore)
└── docs/bewertung/SESSION_*_ZUSAMMENFASSUNG.md

Veraltet (archiviert):
└── 99_inbox_unsorted/legacy/_status_yml_archiv/  ← 10 _status.yml (2026-03-08)
```

---

## 5. Wartungshinweise

- **`resume.py` nach jeder groesseren Aenderung ausfuehren** → aktualisiert `docs/thesis_state.md`
- **`docs/thesis_state.md` NICHT manuell editieren** → wird von `resume.py` ueberschrieben
- **`chapter_state.yaml` ist die einzige Status-Quelle** → `_status.yml` wurde entfernt
- **Plugin nach Skill-Aenderungen neu packen** → `.skills/` → `.plugin` (siehe SKILL_OVERVIEW.md)
