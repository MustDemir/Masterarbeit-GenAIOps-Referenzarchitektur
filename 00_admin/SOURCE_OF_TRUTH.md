# Source of Truth

Dieses Dokument definiert verbindlich, welche Artefakte als primaere Wahrheit gelten und welche nur abgeleitet/legacy sind.

## Primaere Quellen

- Operativer Einstiegspunkt (Workspace):
  - `/Users/mustafademir/Projects/genaiops-thesis/00_workspace/`
- Expose v4 (primaer):
  - `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf` (abgegebene Version, AES-256 verschluesselt, SOT im Repo)
  - Arbeitsversion (OneDrive): `OneDrive-SRHFernhochschule/1. Onedrive_Masterarbeit/Expose_v4_final_2026-02-28.docx`
- Kapitel 3 Methodik (primaer):
  - `03_forschungsdesign_methodik/Kapitel_3_Forschungsdesign_und_Methodik.pdf` (SOT im Repo)
  - Arbeitsversion (OneDrive): `OneDrive-SRHFernhochschule/1. Onedrive_Masterarbeit/3. Methodik/Kapitel_3_Forschungsdesign_und_Methodik.docx`
- Gliederung (primaer):
  - `00_admin/gliederung_v3.md`
- Kapitel 4 Method Decisions (primaer):
  - `04_anforderungsanalyse_RQ1/method_decisions_kapitel4.md` (MD1-MD14, Strukturentscheidungen)
  - Arbeitsversion (OneDrive): `OneDrive-SRHFernhochschule/1. Onedrive_Masterarbeit/4. Anforderungen/MD_Masterarbeit_v2_Sessionbericht.md`
- Aktive Thesis-Inhalte (primaer):
  - Kapitelordner `01_*` bis `08_*` in diesem Repo.

## Kapitelordner: Ordnungsregel

- Die Kapitelwurzel bleibt schlank. Dort liegen nur strukturtragende Elemente wie Abschnittsordner, `images/`, `session_summaries/`, `chapter_state.yaml` sowie kapitel-spezifische Stammordner wie `requirements/` oder `quellen_kap5/`.
- Lose Arbeitsdateien werden kapitel-lokal unter `arbeitsmaterial/` abgelegt. Dazu gehoeren insbesondere Drafts, Analysen, Rechercheartefakte, Forward-Refs, Session-Notizen und ad-hoc Hilfsskripte.
- Bereits korrekt einsortierte Dateien bleiben in ihren bestehenden Unterordnern. Die Ordnung wird durch zusaetzliche Unterordner innerhalb des betroffenen Kapitels erweitert, nicht durch das Herausziehen vorhandener Kapitelinhalte.

## Universitaere Vorgaben und Stilrichtlinien (bindend)

- Ordner: `docs/uni_vorgaben/`
- Enthaltene Dokumente:
  - `DRAFT_Hinweise für wissenschaftliche Veröffentlichungen und Abschlussarbeiten.docx` — **Prof. Prinz Stilrichtlinien (bindend fuer alle Kapitel)**
    - Kernanforderungen: Hohe Referenzierdichte, auf Wesentliches reduzieren, keine formalen Ueberleitungen ("im Folgenden wird..."), Ergebnisse durch Vergleich/Abgrenzung kontextualisieren, keine Redundanz, Blablameter-Check
    - Gilt fuer: Sprachstil, Absatzstruktur, Zitierpraxis, Argumentationstiefe in allen Kapiteln
  - `Masterarbeit_Vorbereitung.pdf` — **SRH Fernhochschule Thesis-Vorbereitung (bindend fuer Struktur und Formalia)**
    - Kernanforderungen: Gliederungstiefe max. 4 Ebenen, Einleitung (~10% Umfang), Problemstellung → Zielsetzung → Forschungsfrage → Methodik → Aufbau, Bewertungskriterien (Inhalt 50%, Methodik/Systematik 30%, Formalia 20%), APA 7, 60-80 Textseiten
    - Gilt fuer: Kapitelstruktur, Bewertungsoptimierung, formale Anforderungen, Seitenbudgets
- Verwendung:
  - **Preflight-Checks**: Beide Dokumente als Pruefinstanz (P6: Uni-Anforderungen)
  - **Writer-Skill**: Prof. Prinz Stilregeln als Negativ-Checklist bei jedem Absatz
  - **Consistency-Check**: Formalia-Abgleich gegen SRH-Bewertungskriterien
  - **Post-Session**: Stil-Compliance als Pruefpunkt
- Entscheidung: `D_UNI_HINWEISE_SSOT` (registriert in Entscheidungsregister)

- Kapitel-Volltexte (primaer, Abgabe-Texte):
  - `00_workspace/Fulltext_Kapitel/*.docx` — Die tatsaechlichen Fliesstext-Dateien aller Kapitel
  - Bei Abweichungen zwischen DRAFT.md und DOCX gilt die DOCX
  - Verfuegbar: Kap. 1, 2, 3, 4, 5, Expose
- Roter Faden Tracker (primaer):
  - `docs/roter_faden_tracker.md` — Bruecken-Definitionen, Kernthesen, Cross-Chapter-Abhaengigkeiten
- Pruefkatalog Uni-Vorgaben (primaer):
  - `docs/uni_vorgaben/pruefkatalog.md` — Maschinenlesbare Checkliste aller Uni-Regeln (PK-Codes)

## Fortschritts- und Tracking-Artefakte

| Kategorie | Pfad-Muster | Zweck | Git-Status |
|-----------|-------------|-------|-----------|
| **chapter_state.yaml** | `{KK}_*/chapter_state.yaml` (10 Dateien) | Detaillierter Kapitel-Status: progress, done, next_steps, decisions, key_sources, cross_chapter_dependencies | TRACKED |
| **Preflight-Protokolle** | `docs/preflight/PREFLIGHT_KAP{N}_*.md` | Argumentationsstruktur, Quellen-Zuordnung, Negativ-Checklisten pro Abschnitt | TRACKED |
| **Bewertungsberichte** | `docs/bewertung/BEWERTUNG_KAP{N}_*.md` | Fachliche Reviews mit R1-R6 Scoring (Struktur, Roter Faden, Stil, Zitationen, Scope, Gutachter) | TRACKED |
| **Session-Zusammenfassungen** | `docs/bewertung/SESSION_*_ZUSAMMENFASSUNG.md` | Tagesuebersicht: was gemacht, was offen, Konventionen | TRACKED |
| **Session Summaries** | `{KK}_*/session_summaries/*.yaml` (33 Dateien) | Per-Session YAML mit topic, bullets, decisions, tags — erzeugt durch save.py | .gitignore |
| **Requirements** | `04_*/requirements/R*.yaml` (5 Dateien) | Strukturierte Requirement-Specs (lifecycle_phase, evidence, gates) | TRACKED |
| **Quality Gates** | `05_*/05_03_quality_gates/*/*.yaml` (3 Dateien) | Gate-Specs (trigger, policy_checks, decision, waiver) | TRACKED |
| **.memory/** | `.memory/` (index.json, entscheidungsregister.md, resume_context.txt, sync_states) | Lokaler Session-Cache, Datei-Manifest, Blob-Sync | .gitignore |
| **~~_status.yml~~** | `{KK}_*/_status.yml` (10 Dateien) | **VERALTET — NICHT VERWENDEN.** Redundant mit chapter_state.yaml, Werte nicht aktuell | TRACKED (legacy) |

## Status-Enum (verbindlich fuer alle Artefakte)

Einheitliche Status-Werte fuer chapter_state.yaml, README, thesis_state.md:
```
planned → in_progress → draft → review → final
```

Wichtig: `00_workspace` enthaelt Pointer/Regeln und die Kapitel-Volltexte als primaere Abgabe-Texte.

## Kommunikationsartefakte

- USP-Analyse & Positionierung (primaer):
  - `docs/positioning/USP_ANALYSE_EXPERTENBEWERTUNG.md` (Living Document, SOT im Repo)
  - Verwendung: Kap. 2.7 (Forschungsluecke), Kap. 5.1 (Designprinzipien), Kap. 7.2 (Wiss. Beitrag), Kap. 6.4 (Expert-Review-Leitfaden), Betreuungsgespraeche
  - Erstellt: 2026-03-02 via Copilot Repo-Tiefenanalyse + Design-Thinking-Session
- Design-Thinking Rohdaten (Archiv):
  - `99_inbox_unsorted/raw/Design_Thinking_Chatverlauf_GenAIOps.md`
  - Nicht primaer — Rohmaterial fuer USP-Analyse

## Legacy / Historische Backups

- `docs/expose/legacy/` — Alle Expose v1-v3 Versionen (lokal, aus Git entfernt per .gitignore)
- `03_forschungsdesign_methodik/Kapitel_3_*.docx.enc` — Historisches Backup (verschluesselt, Stand 2026-02-27)

## Session Summary Regeln

- `*/session_summaries/` enthaelt nur `*.yaml`.
- Rohmaterial (chat exports, zips, pdf) liegt unter:
  - `99_inbox_unsorted/raw/`

## Cloud/RAG Betriebsmodell

- Arbeitsrepo: `genaiops-thesis`
- Toolkit-Repo: `ai-context-vault`
- Blob ist getrennt per Container.
- Azure Search darf gemeinsam genutzt werden (bewusst), aber jede Summary fuehrt Metadaten:
  - `repo_scope`
  - `summary_type`
  - `source_repo`
