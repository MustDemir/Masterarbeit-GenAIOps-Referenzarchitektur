---
name: thesis-post-session
description: >
  Post-Session-Verifikation nach dem Schreiben von Thesis-Abschnitten. Prüft ob alle
  Repo-Artefakte konsistent und vollständig sind: DRAFT gespeichert, Prüfprotokolle sichtbar,
  chapter_state aktualisiert, Session Summary erstellt, Entscheidungsregister synchron,
  Konsistenz-Diff erstellt, Exposé-Abweichungen dokumentiert.
  Trigger bei: "session ende", "post-session", "abschluss check", "fertig für heute",
  "save session", "wir sind fertig", "session schließen", "repo aktualisieren",
  "fortschritt updaten", "häckchen machen".
  Auch triggern wenn der User signalisiert dass die Arbeit für heute/diese Session beendet ist.
---

# Thesis Post-Session Check

Dieser Skill stellt sicher, dass am Ende jeder Schreib-Session alle Artefakte im Repo
konsistent und vollständig sind. Ohne diesen Check entstehen Lücken: chapter_state veraltet,
Entscheidungen fehlen, Session Summaries nicht gespeichert — und die nächste Session
startet mit unvollständigem Kontext.

## Die 6 Prüfpunkte (A–F)

Durchlaufe alle 6 Punkte und erstelle am Ende ein Post-Session-Protokoll.

### A — Geschriebene Artefakte

Prüfe:
- ☐ DRAFT-Datei aktualisiert und gespeichert (`{kapitel_ordner}/Kap{N}_*_DRAFT.md`)
- ☐ Prüfprotokolle zu ALLEN neuen Absätzen vorhanden und sichtbar
- ☐ Keine ❌ oder ⚠ MATCH-Bewertungen offen (alle korrigiert?)
- ☐ Wortanzahl / Seitenbudget im Header und BILANZ aktualisiert
- ☐ Status-Emojis im Header korrekt (✅/🔄/⬜)

### B — chapter_state.yaml

Prüfe und aktualisiere:
- ☐ `progress` (%-Wert korrekt? basierend auf fertiggestellten Abschnitten)
- ☐ `status` (Entwurf / In Arbeit / Review / Fertig)
- ☐ `done` (neue fertige Abschnitte zur Liste hinzugefügt?)
- ☐ `next_steps` (was kommt als nächstes?)
- ☐ `key_sources` (neue Quellen hinzugefügt?)
- ☐ `open_questions` (offene Fragen aktualisiert?)

Prüfe auch abhängige Kapitel:
- ☐ Cross-chapter-Impacts aus dieser Session? → In betroffenen chapter_states dokumentieren
- ☐ Keine Widersprüche zu anderen chapter_states?

### C — Session Summary

Erstelle eine Session Summary via `save.py` aus dem **ai-context-vault** Repo:

```bash
cd ../ai-context-vault
python3 scripts/save.py --topic [kapitelthema] --text "[Summary-Text]" --title "[Titel]" --tags "[tags]" --no-llm
```

**save.py Verhalten (aktuelle Version):**
- Summary-Engine: 3-Tier-Fallback (Anthropic Claude → Azure OpenAI → local_rules)
- `--no-llm` deaktiviert LLM-Engines, nutzt nur lokale Extraktion
- Topic-Routing: auto | architecture | requirements | evaluation | methodology | general
- Blob-Sync: OPT-IN via `--blob` Flag oder `SAVE_AUTO_BLOB_SYNC=1`
- Azure Search Push: OPT-IN via `--azure` Flag
- Index + Resume werden automatisch aktualisiert (kein separater reindex nötig)

Der Summary-Text sollte enthalten:
- Welche Abschnitte geschrieben/bearbeitet wurden
- Wichtigste Quellen die verwendet wurden
- Entscheidungen die getroffen wurden
- Wortanzahl-Stand

### D — Entscheidungsregister

Prüfe:
- ☐ Neue Entscheidungen (D_xxx) → in `docs/thesis_state.md` eingetragen?
- ☐ Critical Definitions aktualisiert wenn nötig?
- ☐ `docs/SSOT_ROTER_FADEN_ANALYSE.md` — neue Lücken identifiziert?
- ☐ Entscheidungspapiere konsistent?

### E — Konsistenz-Diff

Erstelle einen Vorher-Nachher-Vergleich:
- ☐ Was war der Stand VOR der Session? (aus Preflight-Protokoll)
- ☐ Was ist jetzt NEU? (Delta)
- ☐ Stimmt das Delta mit dem Preflight-Plan überein?
- ☐ Neue Begriffe konsistent mit Critical Definitions?
- ☐ Alle neuen Zitationen APA7 mit Seitenangabe?
- ☐ Keine verwaisten Forward-References? (Verweis auf X.Y → existiert?)

Nutze `git diff` um die tatsächlichen Änderungen zu sehen:
```bash
git diff --stat
git diff {kapitel_ordner}/
```

### F — Exposé-Abweichungen

Prüfe:
- ☐ Neue Abweichungen vom Exposé in dieser Session?
  - Wenn ja: im Post-Session-Protokoll als "Exposé-Delta" dokumentieren
  - Relevante Entscheidung (D_xxx) anlegen oder bestehende aktualisieren
- ☐ Bestehende Abweichungen konsistent mit thesis_state.md?

---

## Ausgabeformat: Post-Session-Protokoll

```markdown
## Post-Session-Protokoll: [Datum] — [Thema]

### Geschriebene Abschnitte: Kap. X.Y, X.Z
### Wortanzahl-Delta: +[N] Wörter (Gesamt: [M] Wörter)
### Neue Entscheidungen: D_xxx, D_yyy (oder: keine)
### chapter_state Updates: [✅ aktualisiert / ❌ fehlt noch: ...]
### Session Summary: [✅ gespeichert als [Dateiname] / ❌ fehlt noch]
### Entscheidungsregister: [✅ synchron / ⚠ X Decisions fehlen]
### Exposé-Delta: [✅ keine neue Abweichung / ⚠ Dx neu: ...]
### Konsistenz-Check: [✅ keine Widersprüche / ⚠ Issue: ...]
### Git-Status: [✅ committed / ⬜ uncommitted changes]

### Nächste Session — Startpunkt:
- Nächster Abschnitt: Kap. X.Y
- Offene Fragen: ...
- Preflight bereits vorhanden: [ja/nein]
```

---

## Git-Commit Vorbereitung

Falls der User committen will, bereite einen Commit vor:
- Stage nur relevante Dateien (DRAFT, chapter_state, session_summary, thesis_state)
- Commit-Message im Format: `feat(kapitel): Kap. X.Y [Titel] — [kurze Beschreibung]`
- Nicht automatisch pushen — erst User fragen

---

## Next-Session Briefing

Generiere am Ende eine kompakte Zusammenfassung für die nächste Session:

```
Nächste Session starten mit:
1. chapter_state.yaml lesen: {kapitel_ordner}/chapter_state.yaml
2. Nächster Abschnitt: Kap. X.Y — [Titel]
3. Preflight-Status: [vorhanden/fehlt]
4. Offene Fragen: [Liste]
5. Verbleibendes Seitenbudget: [N] Wörter / [M] Seiten
```
