---
name: thesis-preflight
description: >
  Systematischer Pre-Flight-Check VOR dem Schreiben eines Thesis-Abschnitts. Durchläuft 6 Prüfinstanzen
  (Exposé, Kapiteltexte, Sessions/States, Entscheidungen, Quellen, Uni-Anforderungen) und erstellt ein
  Preflight-Protokoll mit Argumentationsstruktur, Inhalts-Checklist und Negativ-Checklist.
  Trigger bei: "preflight", "neuer abschnitt", "kap X.Y schreiben", "GO vorbereiten", "prüf erstmal",
  "was muss ich beachten für", "vorbereitung für kapitel", "checklist für abschnitt".
  Auch triggern wenn der User einen neuen Abschnitt beginnen will ohne explizit "preflight" zu sagen —
  jeder Schreibauftrag für einen neuen Thesis-Abschnitt sollte mit diesem Skill starten.
---

# Thesis Preflight Check

Dieser Skill stellt sicher, dass Claude VOR dem Schreiben eines Thesis-Abschnitts die gesamte
Wissensbasis systematisch durchgeht. Ohne diesen Check fehlen Inhalte, Entscheidungen werden
ignoriert, und die Konsistenz zwischen Kapiteln leidet.

## Warum das wichtig ist

Die Masterarbeit hat eine komplexe Abhängigkeitsstruktur: Entscheidungen in Kap. 4 beeinflussen
Kap. 5, das Exposé definiert den Rahmen, die Gliederung gibt Seitenbudgets vor, und
Critical Definitions müssen konsistent durchgehalten werden. Ein einziger vergessener Check
kann zu Widersprüchen führen, die später aufwändig korrigiert werden müssen.

## Workflow: 6 Prüfinstanzen in Reihenfolge

Identifiziere zuerst den **Zielabschnitt** (z.B. "Kap. 2.1") aus dem User-Input oder dem
`chapter_state.yaml` des Zielkapitels (Feld `next_steps`).

Dann durchlaufe die 6 Prüfinstanzen in dieser Reihenfolge. Für jede Instanz: die angegebenen
Dateien lesen, die Prüffragen beantworten, und Ergebnisse sammeln.

### P1 — Exposé + README

Lese diese Dateien:
- `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf` (primäre Exposé-Quelle im Repo)
- optional lokal: `00_admin/Expose_v4_final_2026-02-28.docx` (Arbeitskopie, falls vorhanden)
- `README.md` (Projektübersicht)

Beantworte:
- Steht der geplante Abschnitt im Einklang mit dem Exposé?
- Gibt es im Exposé Formulierungen/Inhalte, die übernommen werden können?
- Hat sich der Scope seit dem Exposé verändert? Wo ist die Änderung dokumentiert?

### P2 — Kapiteltexte + Volltexte (SOT-Hierarchie)

Die SOT-Hierarchie bestimmt, welche Quellen bei Widersprüchen gewinnen:
`gliederung_v3.md > Kap. 3 DOCX > Kap. 4 DOCX > Entscheidungsregister > Exposé`

Lese diese Dateien:
- **Volltext des aktuellen Kapitels** — `00_workspace/Fulltext_Kapitel/Kapitel {N} *.docx` (primaer!)
- **Volltext des Vorgaengerkapitels** — `00_workspace/Fulltext_Kapitel/Kapitel {N-1} *.docx` (Roter Faden!)
- Fallback: `{kapitel_ordner}/{N}_{M}_{thema}_DRAFT.md` (falls DOCX nicht lesbar)
- `docs/roter_faden_tracker.md` — Bruecken-Definitionen und Kernthesen
- `00_admin/gliederung_v3.md` — Kapitelstruktur, Seitenbudgets
- `03_forschungsdesign_methodik/` — DSR-Rahmen, Artefaktdefinition
- `04_anforderungsanalyse_RQ1/` — Problemdimensionen, Requirements
- `05_referenzarchitektur_RQ2/` — S1–S4, Quality Gates, PoC
- Alle anderen Volltexte mit Status ≥ "draft"

Beantworte:
- Welche Begriffe/Definitionen aus bereits geschriebenen Kapiteln müssen verwendet werden?
- Gibt es Forward-References? Existiert das Ziel oder ist es in der Gliederung geplant?
- Stimmt die Argumentationslinie mit der Gliederung überein?
- **Roter Faden rueckwaerts:** Lese den VOLLTEXT des Vorgaengerkapitels — wie endet es inhaltlich? Welche Erwartung wird geweckt? Knuepft der neue Abschnitt nahtlos an?
- **Roter Faden vorwaerts:** Was erwartet das Nachfolgerkapitel (aus chapter_state/roter_faden_tracker)? Bereitet der geplante Abschnitt darauf vor?
- **Konsistenz:** Widersprechen geplante Inhalte bestehenden Volltexten?

### P3 — Session Summaries + chapter_state + relevante Dateien

Lese diese Dateien:
- `{kapitel_ordner}/chapter_state.yaml` (Zielkapitel)
- Alle relevanten `chapter_state.yaml` (abhängige Kapitel)
- `{kapitel_ordner}/session_summaries/*.yaml` (bisherige Diskussionen)
- `99_inbox_unsorted/session_summaries/*.yaml` (kapitelübergreifend)

Prüfe außerdem ob die chapter_state "Definition of Ready" erfüllt ist:
- Hat das Zielkapitel ausgefüllte Felder (done, current_focus, key_sources)?
- Wenn nicht: **WARNUNG** — chapter_state muss zuerst initialisiert werden.

Beantworte:
- Gibt es in Session Summaries Inhalte, die in diesen Abschnitt gehören?
- Sind alle chapter_state-Entscheidungen berücksichtigt?

### P4 — Entscheidungspapiere + Entscheidungsregister

Lese diese Dateien:
- `docs/thesis_state.md` — Alle D_xxx Entscheidungen, Critical Definitions
- `docs/SSOT_ROTER_FADEN_ANALYSE.md` — Cross-chapter Impact
- `docs/ENTSCHEIDUNGSPAPIER_KAP4.md` — Kap. 4-spezifische Designentscheidungen
- `00_admin/SOURCE_OF_TRUTH.md` — SOT-Hierarchie

Beantworte:
- Welche Entscheidungen (D_xxx) betreffen diesen Abschnitt direkt?
- Gibt es offene Entscheidungen, die VOR dem Schreiben geklärt werden müssen?
- Muss eine NEUE Entscheidung getroffen werden? → Dokumentieren BEVOR geschrieben wird
- Sind die Critical Definitions eingehalten? (Enforcement ≠ Dokumentation, Deployer-Scope, etc.)

### P5 — Quellen-Papers

Nutze diese Tools in dieser Reihenfolge (Fallback-Kette):
1. `zitations-finder` Skill — Belegstellen im PDF finden und verifizieren
2. `zotero_search_items` → `zotero_item_fulltext` (Zotero-Bibliothek)
3. Uploads: `/sessions/.../mnt/uploads/` (hochgeladene PDFs)
4. `elicit-research` Skill (Elicit-Suche)
5. `semanticSearch` MCP Tool (Semantic Scholar)
6. `mcp__claude_ai_Consensus__search` (Consensus API)
7. Wenn nirgends auffindbar: ❌ markieren, Alternative suchen

Beantworte:
- Welche Quellen MÜSSEN in diesem Abschnitt zitiert werden (laut Gliederung/Exposé)?
- Gibt es neue Quellen seit dem Exposé?
- Sind alle Zitate APA7 mit Seitenangabe?

### P6 — Uni-Anforderungen + DSR-Verankerung

Prüfe:
- **Seitenbudget:** gliederung_v3.md Budget vs. bisherige Wortanzahl im Kapitel
- **Formatvorgaben:** Nummerierung nur bis 2. Ebene, keine formalen Überleitungen
- **SRH-Leitfaden:** "Formales Vorgehen NICHT explizit beschreiben"
- **Zitationsdichte:** Hohe Zitationsdichte, jede Behauptung belegt
- **DSR-Phasen-Mapping:** In welcher DSR-Phase (Hevner/Peffers) befindet sich der Abschnitt?
- **Scope-Drift-Detection:** Geplanter Inhalt vs. Exposé-Erwartung — Drift vorhanden?

---

## Ausgabeformat: Preflight-Protokoll

Nach Durchlauf aller 6 Prüfinstanzen, erstelle das Protokoll in diesem Format:

```
## Preflight-Protokoll: Kap. X.Y — [Titel]

### Ergebnis P1 (Exposé): [✅ konsistent / ⚠ Abweichung: ...]
### Ergebnis P2 (Kapiteltexte): [Relevante Begriffe/Definitionen: ...]
### Ergebnis P3 (Sessions/Files): [Relevante Inhalte: ...]
### Ergebnis P4 (Entscheidungen): [Betroffene D_xxx: ...]
### Ergebnis P5 (Quellen): [Pflicht-Zitate: ...]
### Ergebnis P6 (Uni): [Seitenbudget: X Wörter / X Seiten]

### Synthese — Argumentationsstruktur für Kap. X.Y:

**Brücke von Kap. X.(Y-1):** [Wie endet der vorherige Abschnitt?]

| Absatz | Argumentativer Move | Logik | Brücke zum nächsten |
|--------|---------------------|-------|---------------------|
| 1 | [z.B. Ziel definieren] | [Schließt an Problemstellung an] | [→ leitet über zu...] |
| N | [z.B. Beitrag formulieren] | [Evaluation belegt Relevanz] | [→ Brücke zu X.(Y+1)] |

**Brücke zu Kap. X.(Y+1):** [Wie bereitet der letzte Satz den nächsten Abschnitt vor?]

### Inhalts-Checklist:
☐ Inhalt 1
☐ Inhalt 2

### Negativ-Checklist — Was darf NICHT in Kap. X.Y:
- ❌ [Inhalt der in anderes Kapitel gehört]
- ❌ [Deployer-Scope beachten: keine Provider-Perspektive (Art. 16)]

### Pflicht-Zitate:
- (Autor, Jahr) — für [Thema]

### Offene Fragen (vor Schreiben klären):
- ...

→ Bereit für "GO"
```

Speichere das Preflight-Protokoll als `docs/preflight/PREFLIGHT_KAP{X}_{Y}_{TITEL}.md`.

---

## Zusätzliche Regeln

- Kein Fließtext ohne "GO" oder "FINAL" — der Skill endet mit dem Preflight-Protokoll
- Default Output-Level: L1 (10–15 Bullets + max. 3 kritische Fragen)
- Deployer-Scope (Art. 26) — nicht Provider (Art. 16), kein Retirement
- Wenn User "bitte lese die Entscheidungspapier genau durch" sagt: P4 besonders gründlich
