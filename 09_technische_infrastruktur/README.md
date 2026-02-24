# Technische Infrastruktur (nicht Thesis-Inhalt)

Stand: 2026-02-24

Dieses Verzeichnis dokumentiert technische Arbeiten am Workflow und an Azure,
die nicht direkt inhaltlicher Teil der Masterarbeit sind.

## Was umgesetzt wurde

1. Projektkonsolidierung
- Doppelten Arbeitsstand zusammengefuehrt.
- Aktiver Hauptordner: `genaiops-thesis/`.
- Backup erstellt unter `../backups/`.

2. Session-Workflow aufgebaut
- `save.py`: erstellt kompakte Session-Summaries als YAML.
- `resume.py`: erzeugt den Kurzkontext fuer neue Chats.
- `reindex.py`: aktualisiert lokalen Index + optional Azure Search/Blob.
- `workflow_lib.py`: zentrale Logik (Topic-Routing, Sync, Index).

3. Topic-Routing fuer Summaries
- Automatische Ablage in passende Ordner, z. B.:
  - `05_referenzarchitektur_RQ2/session_summaries/`
  - `04_anforderungsanalyse_RQ1/session_summaries/`
  - Fallback: `99_inbox_unsorted/session_summaries/`

4. Blob-Sync mit Budget-Schutz
- Summaries werden in Blob gespiegelt.
- Nur neue/geaenderte Dateien werden hochgeladen (Hash-Vergleich).
- Sync-Status lokal: `.memory/blob_sync_state.json`.

5. Azure AI Search Migration (Kosten)
- Alter kostenpflichtiger Service entfernt.
- Neuer Free-Service aktiv: `srch-genaiops-free-20260`.
- Indizes migriert:
  - `genaiops-thesis`
  - `thesis-artifacts`
- `.env` auf neuen Search-Endpoint/Key aktualisiert.

6. Budget-Limit in Azure gesetzt
- Budgetname: `genaiops-thesis-quarterly-30eur`
- Limit: 30 EUR pro Quartal
- Alerts: 80% (actual), 100% (actual), 100% (forecast)
- Empfaenger: `kontakt@mustafa-demir.com`

7. Azure OpenAI vorbereitet
- AOAI-Unterstuetzung in `save.py` implementiert (mit Fallback auf lokale Summary).
- Aktivierung aktuell blockiert wegen Quota/Feature (kein nutzbares Chat-Deployment im Abo).

## Aktueller operativer Ablauf

```bash
python3 save.py --input 99_inbox_unsorted/session_notes.txt --source chatgpt
git add -A && git commit -m "save session"
python3 reindex.py
python3 resume.py
```

## Wichtige Dateien
- `save.py`
- `reindex.py`
- `resume.py`
- `workflow_lib.py`
- `00_admin/WORKFLOW_PLAYBOOK.md`
- `.memory/blob_sync_state.json`

## Hinweis
Diese Doku ist ein technisches Betriebsprotokoll und nicht Teil der wissenschaftlichen Argumentation.
