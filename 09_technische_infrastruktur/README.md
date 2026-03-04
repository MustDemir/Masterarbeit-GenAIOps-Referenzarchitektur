# Technische Infrastruktur (nicht Thesis-Inhalt)

Stand: 2026-03-04

Dieses Verzeichnis dokumentiert die technische Infrastruktur des Repos
(Skripte, Workflows, Azure-Anbindung). Fachlicher Thesis-Inhalt liegt in
den jeweiligen Kapitel-Ordnern.

---

## Skripte-Uebersicht

### Root-Skripte

| Skript | Zweck | Aufruf | Abhaengigkeiten |
|---|---|---|---|
| `save.py` | Session-Ende speichern (YAML + Index + optional Azure) | `python save.py --input <file> --source chatgpt` | `workflow_lib.py`, `pyyaml` |
| `resume.py` | Neuen Chat starten (Index + Resume-Text) | `python resume.py` | `workflow_lib.py` |
| `reindex.py` | Vollstaendiger Reindex mit Azure-Optionen | `python reindex.py [--azure] [--blob]` | `workflow_lib.py`, `pyyaml` |
| `workflow_lib.py` | Zentrale Bibliothek (Topic-Routing, Azure, Blob, Index) | Import — kein Direktaufruf | `pyyaml`, `certifi` |
| `extract_yamls.py` | YAML-Bloecke aus Chat-Exports extrahieren | `python extract_yamls.py <input>` | `pyyaml` |
| `validate_structure.py` | Repo-Strukturvalidierung (CI) | `python validate_structure.py` | `pyyaml` |

### scripts/

| Skript | Zweck | Aufruf | Abhaengigkeiten |
|---|---|---|---|
| `scripts/generate_diagrams.py` | Diagramme programmatisch generieren | `python scripts/generate_diagrams.py` | `pyyaml` |
| `scripts/update_progress.py` | README-Fortschrittsbalken aktualisieren | `python scripts/update_progress.py` | `pyyaml` |
| `scripts/weekly_audit.py` | Woechentlicher Repo-Audit (GitHub Issue) | `python scripts/weekly_audit.py` | `pyyaml` |

---

## Topic-Routing

`workflow_lib.py` ordnet Sessions automatisch dem passenden Kapitel-Ordner zu.

| Topic | Zielordner | Schluesselwoerter |
|---|---|---|
| `architektur` | `05_referenzarchitektur_RQ2/session_summaries/` | architektur, architecture, rq2, quality gate |
| `anforderungen` | `04_anforderungsanalyse_RQ1/session_summaries/` | anforderung, requirement, rq1, muss, soll |
| `evaluation` | `06_evaluation_RQ3/session_summaries/` | evaluation, rq3, interview, validierung, coverage |
| `methodik` | `03_forschungsdesign_methodik/session_summaries/` | methodik, dsr, forschungsdesign, design science |
| `theorie` | `02_rigor_theorie_stand_forschung/session_summaries/` | theorie, rigor, literatur, stand der forschung |
| `einleitung` | `01_einleitung/session_summaries/` | einleitung, problemstellung, motivation |
| `diskussion` | `07_diskussion/session_summaries/` | diskussion, limitation, kritik |
| `fazit` | `08_fazit_ausblick/session_summaries/` | fazit, ausblick, conclusion |
| `general` (Fallback) | `99_inbox_unsorted/session_summaries/` | — |

---

## Azure-Integration

| Dienst | Ressource | Status |
|---|---|---|
| Azure AI Search (Free) | `srch-genaiops-free-20260` | Aktiv |
| Azure Blob Storage | Summaries-Sync (Hash-basiert) | Aktiv |
| Azure OpenAI | Chat-Deployment fuer LLM-Summaries | Blockiert (Quota) |

- Indizes: `genaiops-thesis`, `thesis-artifacts`
- Blob-Sync-Status lokal: `.memory/blob_sync_state.json`
- Budget: 30 EUR/Quartal (`genaiops-thesis-quarterly-30eur`), Alerts bei 80%/100%

---

## GitHub Actions

| Workflow | Datei | Trigger | Funktion |
|---|---|---|---|
| Validate Repo Structure | `.github/workflows/validate-structure.yml` | push, pull_request | `python validate_structure.py` |
| Update Progress Bars | `.github/workflows/update-progress.yml` | Montag 06:00 UTC, manuell | `python scripts/update_progress.py` → commit |
| Weekly Audit | `.github/workflows/weekly-audit.yml` | Sonntag 07:00 UTC, manuell | `python scripts/weekly_audit.py` → GitHub Issue |

---

## Operativer Ablauf

```
Session starten        python resume.py
                       → liest .memory/index.json
                       → gibt Resume-Kontext aus

Arbeiten               Thesis-Inhalt bearbeiten, Notizen in
                       99_inbox_unsorted/session_notes.txt

Session speichern      python save.py --input 99_inbox_unsorted/session_notes.txt \
                         --source chatgpt --topic auto
                       → YAML in passendem session_summaries/-Ordner
                       → Index + Resume aktualisiert
                       → optional: --azure (Search-Push), --blob (Blob-Sync)

Commit                 git add -A && git commit -m "save session"

Reindex (bei Bedarf)   python reindex.py [--azure] [--blob]
```

### save.py Flags

| Flag | Wirkung |
|---|---|
| `--no-llm` | Nur lokale Summary-Regeln, kein Azure-OpenAI-Call |
| `--azure` | Search-Push explizit ausfuehren |
| `--blob` | Blob-Sync explizit ausfuehren |
| `--topic auto` | Automatische Topic-Erkennung |
| `--title "..."` | Titel fuer die Summary |

---

## Lokale Dateien

| Pfad | Inhalt |
|---|---|
| `.memory/index.json` | Lokaler Datei-Index |
| `.memory/resume_context.txt` | Resume-Text fuer neue Chats |
| `.memory/blob_sync_state.json` | Hash-State fuer Blob-Sync |
| `.env` | Azure-Keys und Endpoints (nicht committed) |

---

## requirements.txt

```
pyyaml>=6.0
certifi>=2023.0
```

---

## Hinweis

Diese Doku ist ein technisches Betriebsprotokoll und nicht Teil der
wissenschaftlichen Argumentation.
