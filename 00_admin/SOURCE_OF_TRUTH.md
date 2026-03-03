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

Wichtig: `00_workspace` enthaelt Pointer/Regeln, keine redundanten Kopien von Primaerdokumenten.

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