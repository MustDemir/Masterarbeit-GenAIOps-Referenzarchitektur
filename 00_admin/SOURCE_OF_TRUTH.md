# Source of Truth

Dieses Dokument definiert verbindlich, welche Artefakte als primaere Wahrheit gelten und welche nur abgeleitet/legacy sind.

## Primaere Quellen

- Operativer Einstiegspunkt (Workspace):
  - `/Users/mustafademir/Projects/genaiops-thesis/00_workspace/`
- Expose (primaer):
  - `/Users/mustafademir/Projects/genaiops-thesis/98_onedrive_migration/1_masterarbeit/1. Expose v3.docx`
- Gliederung (primaer):
  - `/Users/mustafademir/Projects/genaiops-thesis/00_admin/gliederung_v3.md`
- Aktive Thesis-Inhalte (primaer):
  - Kapitelordner `01_*` bis `08_*` in diesem Repo.

Wichtig: `00_workspace` enthaelt Pointer/Regeln, keine redundanten Kopien von Primaerdokumenten.

## Session Summary Regeln

- `*/session_summaries/` enthaelt nur `*.yaml`.
- Rohmaterial (chat exports, zips, pdf) liegt unter:
  - `/Users/mustafademir/Projects/genaiops-thesis/99_inbox_unsorted/raw/`

## Expose Legacy

- Alte Expose-Versionen duerfen nur in Legacy liegen:
  - `/Users/mustafademir/Projects/genaiops-thesis/docs/expose/legacy/`

## Cloud/RAG Betriebsmodell

- Arbeitsrepo: `genaiops-thesis`
- Toolkit-Repo: `ai-context-vault`
- Blob ist getrennt per Container.
- Azure Search darf gemeinsam genutzt werden (bewusst), aber jede Summary fuehrt Metadaten:
  - `repo_scope`
  - `summary_type`
  - `source_repo`
