# Thesis Workflow Operating Instructions

**Ziel:** Mit dem Thesis-Workflow arbeiten, ohne jedes Mal den ganzen Werkzeugkasten im Kopf zu haben.

## 1. Session starten

Wenn du eine neue Arbeitssession beginnst, starte mit einem der Trigger:

- `neue session`
- `resume`
- `wo waren wir`
- `weiter machen`

Dann sollte die KI:

1. den aktuellen Kontext laden
2. den Fortschritt zusammenfassen
3. den naechsten sinnvollen Abschnitt vorschlagen
4. pruefen, ob ein Preflight fehlt

Du musst dabei nur auf eines achten:
- Ist der vorgeschlagene Abschnitt wirklich der, an dem du jetzt arbeiten willst?

## 2. Vor dem Schreiben

Wenn ein neuer Abschnitt geschrieben werden soll, zuerst `thesis-preflight`.

Die KI soll dabei fuer dich pruefen:

1. Expose / Gliederung / vorhandene Kapitel
2. relevante Session Summaries
3. Decisions und Critical Definitions
4. Quellenlage
5. Seitenbudget, Scope und DSR-Einordnung

Du musst nur darauf achten:

1. Sind noch offene Fragen im Preflight?
2. Ist die Argumentationsstruktur plausibel?
3. Erst dann `GO` zum Schreiben geben

## 3. Beim Schreiben

Nach `GO` arbeitet `thesis-writer`.

Die KI soll:

1. absatzweise schreiben
2. pro Absatz ein Pruefprotokoll erzeugen
3. Belege, APA7 und Seitenangaben absichern
4. Terminologie konsistent halten
5. Seitenbudget im Blick behalten

Du musst dabei aktiv kontrollieren:

1. Gibt es `WARNUNG` oder `FAIL` im Pruefprotokoll?
2. Ist der Absatz fachlich wirklich korrekt?
3. Nur dann den naechsten Absatz freigeben

## 4. Session beenden

Wenn du fertig bist, triggert:

- `session ende`
- `fertig fuer heute`
- `save session`

Dann soll `thesis-post-session` durchlaufen.

Die KI soll pruefen:

1. DRAFT aktualisiert?
2. Pruefprotokolle sichtbar?
3. `chapter_state.yaml` aktualisiert?
4. neue Decisions dokumentiert?
5. Session Summary gespeichert?
6. Next-Session-Briefing erstellt?

## 5. Was automatisch gemacht wird

Automatisch oder stark gefuehrt:

1. Resume-Kontext laden
2. naechsten Abschnitt vorschlagen
3. Preflight-Protokoll strukturieren
4. absatzweises Schreiben mit Belegpruefung
5. Post-Session-Check
6. lokales Save + Index + Resume im `ai-context-vault`
7. Repo-Checks im Thesis-Repo (`validate_structure`, `weekly_audit`)

## 6. Was du bewusst entscheiden musst

Nicht automatisch entscheiden lassen:

1. Welcher Abschnitt jetzt wirklich dran ist
2. Ob der Preflight ausreicht, um zu starten
3. Ob ein Absatz fachlich freigegeben ist
4. Ob committed werden soll
5. Ob Cloud-Sync gewollt ist

## 7. Cloud-Sync-Regel

Im `ai-context-vault` gilt jetzt:

1. `save.py` speichert standardmaessig lokal
2. Blob-Sync nur explizit mit `--blob`
3. altes Auto-Verhalten nur mit `SAVE_AUTO_BLOB_SYNC=1`

Das ist gewollt, damit Speichern und Cloud-Publish sauber getrennt sind.

## 8. Praktische Standardroutine

Die einfachste alltagstaugliche Routine ist:

1. Session starten -> `resume`
2. Abschnitt festlegen -> `preflight`
3. Schreiben -> `GO`, absatzweise
4. Session beenden -> `post-session`
5. Optional committen

## 9. Die 4 Dinge, auf die du immer achten musst

Wenn du nur vier Dinge aktiv kontrollierst, reicht das:

1. Zielabschnitt stimmt
2. Preflight ist plausibel
3. Pruefprotokoll hat keine roten Luecken
4. Session-Ende ist sauber abgeschlossen

## 10. Minimalregel fuer gute Sessions

Nicht ohne Preflight in neue Abschnitte springen.  
Nicht ohne Pruefprotokoll weiterschreiben.  
Nicht ohne Post-Session-Check fuer den Tag aufhoeren.
