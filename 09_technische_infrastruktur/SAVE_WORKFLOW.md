# save.py - Kurzreferenz

## Zweck
`save.py` speichert das Ende einer Session als kompakte YAML-Summary.

## Was passiert bei `save.py`
1. Text einlesen (`--input`, `--text` oder stdin)
2. Thema erkennen (`--topic auto`) und Zielordner waehlen
3. Summary speichern als `session_summaries/*.yaml`
4. lokalen Index und Resume aktualisieren
5. optional Azure Search pushen (`--azure`)
6. Blob-Sync ausfuehren (wenn konfiguriert)

## Beispiel
```bash
python3 save.py --input 99_inbox_unsorted/session_notes.txt --source chatgpt --topic auto --title "Session Ende"
```

## Nuetzliche Flags
- `--no-llm` : nur lokale Summary-Regeln, kein AOAI-Call
- `--azure` : Search-Push explizit ausfuehren
- `--blob` : Blob-Sync explizit ausfuehren

## Output
- YAML-File in passendem `session_summaries/`-Ordner
- aktualisierte Dateien:
  - `.memory/index.json`
  - `.memory/resume_context.txt`
