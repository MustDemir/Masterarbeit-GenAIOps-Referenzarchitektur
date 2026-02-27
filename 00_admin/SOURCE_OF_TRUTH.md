# Source of Truth

Dieses Dokument definiert verbindlich, welche Artefakte als primaere Wahrheit gelten und welche nur abgeleitet/legacy sind.

## Primaere Quellen

- Operativer Einstiegspunkt (Workspace):
  - `/Users/mustafademir/Projects/genaiops-thesis/00_workspace/`
- Expose (primaer):
  - `docs/expose/Expose_v3_single_source_2026-02-27.pdf`
  - `docs/expose/Expose_v3_single_source_2026-02-27.txt` (Textextrakt)
- Gliederung (primaer):
  - `00_admin/gliederung_v3.md`
- Aktive Thesis-Inhalte (primaer):
  - Kapitelordner `01_*` bis `08_*` in diesem Repo.
- Kapitel 3 Methodik (verschluesselt):
  - `03_forschungsdesign_methodik/Kapitel_3_Forschungsdesign_und_Methodik.docx.enc`
  - Entschluesselung: `openssl enc -d -aes-256-cbc -pbkdf2 -in <datei>.enc -out <datei>.docx -pass pass:<pw>`

Wichtig: `00_workspace` enthaelt Pointer/Regeln, keine redundanten Kopien von Primaerdokumenten.

## Session Summary Regeln

- `*/session_summaries/` enthaelt nur `*.yaml`.
- Rohmaterial (chat exports, zips, pdf) liegt unter:
  - `/Users/mustafademir/Projects/genaiops-thesis/99_inbox_unsorted/raw/`

## Expose Legacy

- Alte Expose-Versionen duerfen nur in Legacy liegen:
  - `docs/expose/legacy/`

## Cloud/RAG Betriebsmodell

- Arbeitsrepo: `genaiops-thesis`
- Toolkit-Repo: `ai-context-vault`
- Blob ist getrennt per Container.
- Azure Search darf gemeinsam genutzt werden (bewusst), aber jede Summary fuehrt Metadaten:
  - `repo_scope`
  - `summary_type`
  - `source_repo`
