# GenAIOps Thesis - Workflow Playbook (Projektgedaechtnis)

## Ziel
Kompakte, strukturierte Session-Summaries speichern (statt Vollchat),
damit jedes KI-Modell schnell dort weitermachen kann, wo du aufgehoert hast.

## Prinzip
- Source of Truth = Dateien im Repo.
- Keine langen Chat-Logs als Dauerkontext.
- Jede Session endet mit kurzer Summary in YAML + Reindex.

## End-of-Session Workflow
```bash
python3 save.py --input 99_inbox_unsorted/session_notes.txt --source chatgpt
# oder: echo "...deine Stichpunkte..." | python3 save.py --source claude

git add -A && git commit -m "save session"
python3 reindex.py
```

## Neue Session starten
```bash
python3 resume.py
```
Dann den Output in den neuen Chat einfuegen.

## Topic-Routing (automatisch)
`save.py` erkennt Thema automatisch (`--topic auto`) und speichert in:
- Architektur -> `05_referenzarchitektur_RQ2/session_summaries/`
- Anforderungen -> `04_anforderungsanalyse_RQ1/session_summaries/`
- Evaluation -> `06_evaluation_RQ3/session_summaries/`
- Sonstiges -> `99_inbox_unsorted/session_summaries/`

## Azure RAG Reindex
`reindex.py` macht immer lokalen Index + Resume neu.
Azure Push passiert, wenn Konfiguration vorhanden ist oder mit `--azure`:
- `AZURE_SEARCH_ENDPOINT`
- `AZURE_SEARCH_ADMIN_KEY` (oder `AZURE_SEARCH_KEY`)
- `AZURE_SEARCH_INDEX_NAME` (oder `AZURE_SEARCH_INDEX`)
- optional: `AZURE_SEARCH_KEY_FIELD` (default `id`)
- optional: `AZURE_SEARCH_CONTENT_FIELD` (default `content`)
- optional: `AZURE_SEARCH_INSECURE_TLS=1` nur falls lokales Python SSL-Truststore kaputt ist

Blob Sync passiert, wenn Konfiguration vorhanden ist oder mit `--blob`:
- `AZURE_STORAGE_ACCOUNT`
- `AZURE_STORAGE_KEY`
- optional: `AZURE_BLOB_CONTAINER` (default `session-summaries`)

Budget-Schutz:
- Blob-Sync laedt nur neue/geaenderte Summary-Dateien hoch (Hash-Vergleich).
- Sync-Status liegt lokal in `.memory/blob_sync_state.json`.

## Hinweis
Wenn dein Azure-Index andere Feldnamen hat, setze `AZURE_SEARCH_KEY_FIELD` und
`AZURE_SEARCH_CONTENT_FIELD` passend, sonst kann der Push fehlschlagen.

## Azure OpenAI Summary (optional aktiv)
`save.py` nutzt automatisch Azure OpenAI, wenn gesetzt:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_KEY` (oder `AZURE_OPENAI_API_KEY`)
- `AZURE_OPENAI_DEPLOYMENT`
- optional: `AZURE_OPENAI_API_VERSION` (default `2024-10-21`)
- optional Kostenbremse: `AZURE_OPENAI_MAX_INPUT_CHARS` (default `6000`), `AZURE_OPENAI_MAX_OUTPUT_TOKENS` (default `300`)

Bei Bedarf lokal erzwingen:
```bash
python3 save.py --no-llm ...
```
