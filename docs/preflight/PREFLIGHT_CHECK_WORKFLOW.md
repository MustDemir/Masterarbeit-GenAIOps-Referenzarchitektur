# PRE-FLIGHT CHECK WORKFLOW — Thesis-Kapitelschreiben

> **Zweck:** Systematischer Prüf-Workflow, der VOR dem Schreiben jedes Kapitelabschnitts durchlaufen werden MUSS.
> **Erstellt:** 2026-03-06 | **Status:** Living Document
> **Kontext:** Mustafa Demir, Masterarbeit GenAIOps-Referenzarchitektur, SRH Fernhochschule

---

## Warum dieser Workflow existiert

Ohne systematische Prüfung vor dem Schreiben fehlen Inhalte (z. B. Artefakte, USPs, PoC-Details), Entscheidungen werden ignoriert, und die Konsistenz zwischen Kapiteln leidet. Dieser Workflow stellt sicher, dass jeder Abschnitt auf der **vollständigen Wissensbasis** aufbaut.

---

## Prüfinstanzen (in dieser Reihenfolge)

### P1 — Exposé + README

| Was prüfen | Dateipfad | Ziel |
|---|---|---|
| Exposé (SOT für Gesamtrahmen) | `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf` | Originalziel, Forschungsfragen, Scope, Methodik — Basis für Konsistenzcheck |
| README | `README.md` | Repo-Struktur, aktuelle Projektübersicht, Konventionen |

**Prüffragen:**
- Steht der geplante Abschnitt im Einklang mit dem Exposé?
- Gibt es im Exposé Formulierungen/Inhalte, die übernommen werden können?
- Hat sich der Scope seit dem Exposé verändert? → Wenn ja, wo ist die Änderung dokumentiert?

---

### P2 — Kapiteltexte (dynamisch: ALLE bereits geschriebenen + SOT-Kapitel)

> **Regel:** P2 ist nicht auf Kap. 3/4/5 beschränkt. JEDES bereits geschriebene Kapitel ist SOT für nachfolgende Abschnitte. Die untenstehende Tabelle zeigt die Kern-SOTs; zusätzlich MUSS der DRAFT des aktuellen Kapitels gelesen werden.

| Was prüfen | Dateipfad | Ziel |
|---|---|---|
| **DRAFT des aktuellen Kapitels** | `{kapitel_ordner}/Kap{N}_*_DRAFT.md` | **Kontinuität**: bisherige Absätze, Terminologie, offene Forward-Refs |
| Kap. 3 Forschungsdesign | `03_forschungsdesign_methodik/` (DOCX + MD) | DSR-Rahmen, Artefaktdefinition, Evaluationsstrategie |
| Kap. 4 Anforderungsanalyse | `04_anforderungsanalyse_RQ1/` (DOCX + MD) | Problemdimensionen, Requirements, Related Work |
| Kap. 5 Referenzarchitektur | `05_referenzarchitektur_RQ2/` (DOCX + MD) | S1–S4, Quality Gates, PoC |
| Gliederung v3 (SOT) | `00_admin/gliederung_v3.md` | Kapitelstruktur, Seitenbudgets, Subsystem-Zuordnung |
| Bereits geschriebene Kapitel | Alle `Kap*_DRAFT.md` mit Status ≥ "Entwurf" | Cross-chapter-Konsistenz, keine Widersprüche |

**Prüffragen:**
- Welche Begriffe/Definitionen aus bereits geschriebenen Kapiteln müssen in diesem Abschnitt verwendet werden?
- Gibt es Forward-References, die hier angekündigt werden müssen? → Ziel-Abschnitt existiert oder ist in Gliederung geplant?
- Stimmt die Argumentationslinie mit der Gliederung überein?
- **Kontinuität:** Liest sich der neue Abschnitt nahtlos nach dem bisherigen DRAFT?

---

### P3 — Session Summaries + chapter_state + relevante Dateien

| Was prüfen | Dateipfad | Ziel |
|---|---|---|
| chapter_state.yaml (Zielkapitel) | `{kapitel_ordner}/chapter_state.yaml` | Status, Entscheidungen, offene Punkte |
| chapter_state.yaml (abhängige Kapitel) | Alle relevanten `chapter_state.yaml` | Cross-chapter-Abhängigkeiten |
| Session Summaries (Zielkapitel) | `{kapitel_ordner}/session_summaries/*.yaml` | Alle bisherigen Diskussionen und Entscheidungen |
| Session Summaries (übergreifend) | `99_inbox/session_summaries/*.yaml` | Kapitelübergreifende Themen |
| USP-Analyse | `docs/positioning/USP_ANALYSE_EXPERTENBEWERTUNG.pdf` | 7 USPs, Positionierung |
| USP Session Summary | `05_referenzarchitektur_RQ2/session_summaries/20260302_034720_*.yaml` | USP-Zusammenfassung (Fallback wenn PDF verschlüsselt) |
| Related Work Vergleich | `04_anforderungsanalyse_RQ1/related_work_vergleich_kap4.md` | MQG4AI-Abgrenzung, Feature-Matrix |
| Pourmajidi Vergleich | `02_rigor_theorie_stand_forschung/Analyse_Pourmajidi_und_Gesamtvergleich.md` | 3-Way-Comparison, Positionierungsmatrix |

**Prüffragen:**
- Gibt es in Session Summaries Inhalte, die in diesen Abschnitt gehören?
- Sind alle chapter_state-Entscheidungen berücksichtigt?
- Welche USPs/Abgrenzungen müssen hier erwähnt werden?

---

### P4 — Entscheidungspapiere + Entscheidungsregister

| Was prüfen | Dateipfad | Ziel |
|---|---|---|
| thesis_state.md | `docs/thesis_state.md` | 16 Entscheidungen (D_SCOPE_* bis D_KAP4_*), Critical Definitions |
| SSOT Roter Faden | `docs/SSOT_ROTER_FADEN_ANALYSE.md` | Cross-chapter Impact, fehlende Entscheidungen |
| Entscheidungspapier Kap. 4 | `docs/ENTSCHEIDUNGSPAPIER_KAP4.md` | Kap. 4-spezifische Designentscheidungen |
| SOURCE_OF_TRUTH.md | `00_admin/SOURCE_OF_TRUTH.md` | SOT-Hierarchie, Datei-Zuordnungen |

**Prüffragen:**
- Welche Entscheidungen (D_xxx) betreffen diesen Abschnitt direkt?
- Gibt es offene Entscheidungen, die VOR dem Schreiben geklärt werden müssen?
- **Muss eine NEUE Entscheidung (D_xxx) getroffen werden?** → Wenn ja: Entscheidung dokumentieren BEVOR geschrieben wird
- Sind die Critical Definitions eingehalten (Enforcement ≠ Dokumentation, Deployer-Scope, etc.)?

---

### P5 — Quellen-Papers (Zotero + Uploads)

| Was prüfen | Dateipfad/Tool | Ziel |
|---|---|---|
| Zotero-Bibliothek | `zotero_search_items` | Relevante Quellen für den Abschnitt finden |
| Hochgeladene PDFs | `/sessions/.../mnt/uploads/` | Direkt verfügbare Volltexte |
| Bereits zitierte Quellen | Prüfprotokolle vorheriger Abschnitte | Konsistenz der Zitierweise |

**Prüffragen:**
- Welche Quellen MÜSSEN in diesem Abschnitt zitiert werden (laut Gliederung/Exposé)?
- Gibt es neue Quellen, die seit dem Exposé hinzugekommen sind?
- Sind alle Zitate APA7 mit Seitenangabe?
- Prüfprotokoll-Format eingehalten? `☑ (Autor, Jahr, S. X) → Key → BELEG: "exakter Satz" → CLAIM: [Paraphrase] → MATCH: ✅/⚠`

**Quellen-Fallback-Kette (wenn Paper nicht sofort auffindbar):**
1. `zotero_search_items` → `zotero_item_fulltext` (Zotero-Bibliothek)
2. Uploads-Ordner: `/sessions/.../mnt/uploads/` (hochgeladene PDFs)
3. `elicit-research:search-papers` Skill (Elicit-Suche für neue Quellen)
4. `semanticSearch` MCP Tool (Semantic Scholar / akademische Datenbanken)
5. `mcp__2fd9a2cd-12ab-4bfc-9ee1-4de6cdb52d02__search` (Consensus API)
6. **Wenn nirgends auffindbar:** Quelle als ❌ markieren, Alternative suchen oder User fragen

---

### P6 — Uni-Anforderungen

| Was prüfen | Quelle | Ziel |
|---|---|---|
| Seitenbudget | `gliederung_v3.md` | Passt der Abschnitt ins Budget? |
| Formatvorgaben | SRH-Leitfaden | DGPs/APA, Nummerierung nur bis 2. Ebene, keine formalen Überleitungen |
| Inhaltliche Anforderungen | SRH-Leitfaden + Exposé | Was erwartet die Uni inhaltlich für diesen Abschnitt? |
| Zitationsdichte | Eigene Regel | Hohe Zitationsdichte, jede Behauptung belegt |

**Prüffragen:**
- Wie viele Wörter/Seiten sind für diesen Abschnitt vorgesehen?
- Sind Formatvorgaben eingehalten (Nummerierung, Überschriften, APA7)?
- Ist die Zitationsdichte ausreichend?

---

## Workflow-Ablauf

```
┌─────────────────────────────────────────────────┐
│  TRIGGER: Neuer Abschnitt soll geschrieben werden │
└───────────────────────┬─────────────────────────┘
                        ▼
              ┌─────────────────┐
              │   P1: Exposé +  │
              │   README prüfen │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  P2: Kap. 3/4/5 │
              │  Texte prüfen   │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  P3: Sessions + │
              │  chapter_state  │
              │  + USP/Related  │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ P4: Entscheid-  │
              │ ungspapiere     │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  P5: Quellen    │
              │  (Zotero/PDF)   │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ P6: Uni-Anford. │
              └────────┬────────┘
                       ▼
         ┌──────────────────────────┐
         │  SYNTHESE:               │
         │  1. Argumentationsstruktur│
         │     (logischer Fluss)    │
         │  2. Inhalts-Checklist    │
         │  3. Negativ-Checklist    │
         │  4. Pflicht-Zitate       │
         │  5. Offene Entscheidungen│
         │  6. Seitenbudget-Check   │
         └────────────┬─────────────┘
                      ▼
         ┌──────────────────────────┐
         │  OUTPUT: Preflight-      │
         │  Protokoll für Abschnitt │
         │  → User reviewt          │
         │  → "GO" → Schreiben      │
         └──────────────────────────┘
```

---

## Ausgabeformat des Preflight-Protokolls

Für jeden Abschnitt wird nach Durchlauf aller 6 Prüfinstanzen ein Protokoll erstellt:

```
## Preflight-Protokoll: Kap. X.Y — [Titel]

### Ergebnis P1 (Exposé): [✅ konsistent / ⚠ Abweichung: ...]
### Ergebnis P2 (Kapiteltexte): [Relevante Begriffe/Definitionen: ...]
### Ergebnis P3 (Sessions/Files): [Relevante Inhalte: ...]
### Ergebnis P4 (Entscheidungen): [Betroffene D_xxx: ...]
### Ergebnis P5 (Quellen): [Pflicht-Zitate: ...]
### Ergebnis P6 (Uni): [Seitenbudget: X Wörter / X Seiten]

### Synthese — Argumentationsstruktur für Kap. X.Y:

> Zeigt den logischen Fluss: Welcher argumentative "Move" pro Absatz,
> wie Absätze aufeinander aufbauen, und wie der Abschnitt sich in das Kapitel einfügt.

**Brücke von Kap. X.(Y-1):** [Wie endet der vorherige Abschnitt? Welche Erwartung wird geweckt?]

| Absatz | Argumentativer Move | Logik (Warum hier?) | Brücke zum nächsten |
|--------|---------------------|---------------------|---------------------|
| 1 | [z.B. Ziel definieren] | [Schließt an Problemstellung an] | [→ leitet über zu...] |
| 2 | [z.B. Lösung skizzieren] | [Ziel braucht konkretes Artefakt] | [→ leitet über zu...] |
| N | [z.B. Beitrag formulieren] | [Evaluation belegt Relevanz] | [→ Brücke zu X.(Y+1)] |

**Brücke zu Kap. X.(Y+1):** [Wie bereitet der letzte Satz den nächsten Abschnitt vor?]

### Synthese — Inhalts-Checklist für Kap. X.Y:
☐ Inhalt 1
☐ Inhalt 2
☐ ...

### Negativ-Checklist — Was darf NICHT in Kap. X.Y:
- ❌ [Inhalt der in anderes Kapitel gehört]
- ❌ [Doppelzitation vermeiden: ...]

### Offene Fragen (vor Schreiben klären):
- ...

→ Bereit für "GO"
```

---

## EBENE 2: Prüfprotokoll (akademische Belegprüfung — NACH dem Schreiben)

> **Zweck:** Jede Zitation im Fließtext wird gegen die Originalquelle geprüft.
> **Wann:** NACH jedem geschriebenen Absatz, BEVOR der nächste Absatz beginnt.
> **Wo:** Direkt unter dem jeweiligen Abschnitt in der DRAFT-Datei.

### Format des Prüfprotokolls

Für **jeden Absatz** wird eine Tabelle erstellt:

```
### Absatz N — [Thema]

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| (Autor, Jahr, S. X) | `KEY` | "exakter Satz aus der Quelle — Copy-Paste" | Paraphrase wie im Fließtext verwendet | ✅ / ⚠ |
```

### Prüfprotokoll-Regeln

1. **BELEG muss ein EXAKTER SATZ** aus dem Paper sein — kein Paraphrasieren der Quelle
2. **Seitenangabe ist Pflicht** — `(Autor, Jahr, S. X)`, nicht nur `(Autor, Jahr)`
3. **Zotero-Key** muss angegeben werden für Rückverfolgbarkeit
4. **MATCH-Bewertung:**
   - ✅ = Claim deckt sich inhaltlich mit Beleg
   - ⚠ = Claim weicht ab oder ist interpretativ → Anmerkung + ggf. Korrektur
   - ❌ = Kein Beleg gefunden → Zitation entfernen oder andere Quelle suchen
5. **Strukturabsätze ohne Zitationen** → Vermerk: "Keine Zitationen (Strukturabsatz). Terminologie konsistent mit Kap. X/Y."
   - **Forward-References prüfen:** Verweis auf Kap. X.Y → existiert der Abschnitt bereits oder ist er in gliederung_v3.md geplant? Keine verwaisten Verweise!
6. **Prüfprotokoll MUSS SICHTBAR** sein — wird nicht gelöscht, bleibt in der DRAFT-Datei
7. **Bei ⚠ oder ❌:** Absatz wird korrigiert BEVOR der nächste Absatz geschrieben wird

### Tools für Ebene 2

| Tool | Wann einsetzen | Zweck |
|------|---------------|-------|
| **Skill: `zitations-finder`** | Bei JEDER Zitation im Prüfprotokoll | Belegstellen im PDF finden, exakte Sätze extrahieren, APA7-Zitat mit Seitenangabe generieren |
| **Zotero MCP (`zotero_search_items`)** | Quelle in Bibliothek lokalisieren | Zotero-Key, Metadaten, Volltextzugriff |
| **Zotero MCP (`zotero_item_fulltext`)** | Volltext lesen für Belegprüfung | Exakte Passage im Paper finden |
| **Read Tool (Uploads)** | Hochgeladene PDFs direkt lesen | Wenn Quelle als Upload vorliegt statt in Zotero |

**Workflow pro Zitation:**
1. Claim im Fließtext identifizieren
2. `zitations-finder` Skill aufrufen → PDF durchsuchen → exakte Belegstelle finden
3. Falls nicht in Uploads: `zotero_search_items` → `zotero_item_fulltext` → Passage suchen
4. BELEG (exakter Satz) + Seitenangabe in Prüfprotokoll-Tabelle eintragen
5. MATCH bewerten (✅/⚠/❌)

### Workflow-Integration

```
┌─────────────────────────────────────────────────────────────┐
│  EBENE 1: Preflight-Check (P1–P6)                          │
│  → Ergebnis: Inhalts-Checklist + Pflicht-Zitate            │
│  → User gibt "GO"                                           │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  SCHREIBEN: Absatz für Absatz                               │
│                                                             │
│  Für jeden Absatz:                                          │
│    1. Absatz schreiben (Fließtext)                          │
│    2. EBENE 2: Prüfprotokoll erstellen                     │
│       → Zotero-Key + BELEG + CLAIM + MATCH                 │
│    3. Bei ⚠/❌ → Absatz korrigieren                        │
│    4. Nächster Absatz                                       │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  ABSCHLUSS: Abschnitt in DRAFT-Datei speichern             │
│  → Fließtext + Prüfprotokolle sichtbar                     │
│  → chapter_state.yaml aktualisieren                         │
└─────────────────────────────────────────────────────────────┘
```

---

## EBENE 3: Post-Session-Verifikation (NACH jeder Session)

> **Zweck:** Sicherstellen, dass alle Repo-Artefakte nach einer Session konsistent und vollständig sind.
> **Wann:** AM ENDE jeder Session, BEVOR die Session geschlossen wird.
> **Warum:** Ohne diesen Check entstehen Lücken: chapter_state veraltet, Entscheidungen fehlen, Session Summaries nicht gespeichert.

### Prüf-Checklist Post-Session

```
## Post-Session-Check: [Datum] — [Thema der Session]

### A — Geschriebene Artefakte
☐ DRAFT-Datei aktualisiert und gespeichert (z.B. Kap1_Einleitung_DRAFT.md)
☐ Prüfprotokolle zu allen neuen Absätzen vorhanden und sichtbar
☐ Wortanzahl / Seitenbudget aktualisiert

### B — chapter_state.yaml
☐ Zielkapitel chapter_state.yaml aktualisiert:
   ☐ progress (%-Wert korrekt?)
   ☐ status (Entwurf / In Arbeit / Review / Done?)
   ☐ done-Liste (neue fertige Abschnitte hinzugefügt?)
   ☐ next_steps (was kommt als nächstes?)
   ☐ decisions (neue D_xxx Entscheidungen aus dieser Session?)
   ☐ key_sources (neue Quellen hinzugefügt?)
   ☐ open_questions (offene Fragen aktualisiert?)
☐ Abhängige Kapitel-States geprüft:
   ☐ Cross-chapter-Impacts dokumentiert? (cross_chapter_impacts)
   ☐ Gibt es Widersprüche zu anderen chapter_states?

### C — Session Summary
☐ Session Summary YAML erstellt (via save.py oder manuell)
☐ Inhalt-Feld enthält Kernargumente, nicht nur Stichpunkte
☐ Entscheidungen der Session im Summary dokumentiert
☐ Im richtigen Kapitelordner gespeichert

### D — Entscheidungsregister
☐ Neue Entscheidungen (D_xxx) in thesis_state.md vorhanden?
☐ Critical Definitions aktualisiert wenn nötig?
☐ SSOT_ROTER_FADEN_ANALYSE.md — neue Lücken identifiziert?
☐ Entscheidungspapiere (z.B. ENTSCHEIDUNGSPAPIER_KAP4.md) konsistent?

### E — Konsistenz-Vergleich (Diff)
☐ Vorher-Nachher-Vergleich:
   ☐ Was war der Stand VOR der Session? (Preflight-Protokoll)
   ☐ Was ist jetzt NEU? (Delta)
   ☐ Stimmt das Delta mit dem Preflight-Plan überein?
☐ Cross-Check Terminologie:
   ☐ Neue Begriffe konsistent mit Critical Definitions?
   ☐ Neue Zitationen APA7 mit Seitenangabe?
☐ Keine verwaisten Forward-References?
   ☐ Verweis auf Abschnitt X.Y → existiert dieser bereits oder ist er geplant?

### F — Exposé-Abweichungen
☐ Neue Abweichungen vom Exposé in dieser Session?
   ☐ Wenn ja → im Post-Session-Protokoll dokumentieren (Feld "Exposé-Delta")
   ☐ Relevante Entscheidung (D_xxx) anlegen oder bestehende aktualisieren
☐ Bestehende Abweichungen — in thesis_state.md oder Preflight-Protokollen konsistent?
```

### Workflow-Integration Ebene 3

```
┌─────────────────────────────────────────────────────────────┐
│  EBENE 1: Preflight (P1–P6)           [VOR dem Schreiben]   │
│  → Inhalts-Checklist + "GO"                                 │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  EBENE 2: Schreiben + Prüfprotokoll   [WÄHREND Session]     │
│  → Absatz → BELEG/CLAIM/MATCH → nächster Absatz             │
└───────────────────────┬─────────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  EBENE 3: Post-Session-Verifikation   [NACH Session]        │
│                                                             │
│  A. DRAFT gespeichert + Prüfprotokolle sichtbar?            │
│  B. chapter_state.yaml aktualisiert?                        │
│  C. Session Summary YAML erstellt?                          │
│  D. Entscheidungsregister synchron?                         │
│  E. Konsistenz-Diff (Vorher ↔ Nachher)?                    │
│  F. Exposé-Abweichungen dokumentiert?                       │
│                                                             │
│  → Ergebnis: Post-Session-Protokoll                         │
│  → Bei ❌: Fix BEVOR Session endet                          │
└─────────────────────────────────────────────────────────────┘
```

### Ausgabeformat Post-Session-Protokoll

```
## Post-Session-Protokoll: [Datum] — [Thema]

### Geschriebene Abschnitte: Kap. X.Y, X.Z
### Neue Entscheidungen: D_xxx, D_yyy
### chapter_state Updates: [✅ aktualisiert / ❌ fehlt noch]
### Session Summary: [✅ gespeichert / ❌ fehlt noch]
### Entscheidungsregister: [✅ synchron / ⚠ X Decisions fehlen]
### Exposé-Delta: [✅ keine neue Abweichung / ⚠ Dx neu]
### Konsistenz-Check: [✅ keine Widersprüche / ⚠ Issue: ...]

### Nächste Session — Startpunkt:
- Nächster Abschnitt: Kap. X.Y
- Offene Fragen: ...
- Preflight bereits vorhanden: [ja/nein]
```

---

## Zusätzliche Regeln (aus Session-Historie)

1. **Kein Fließtext ohne "GO" oder "FINAL"** — Workflow endet mit Preflight-Protokoll
2. **APA7 mit Seitenangabe** — Jedes Zitat braucht `(Autor, Jahr, S. X)`
3. **Prüfprotokoll nach jedem Absatz** — Format: BELEG → CLAIM → MATCH (siehe Ebene 2)
4. **Nummerierung nur bis 2. Ebene** — Sub-Headings als **Fettdruck**
5. **MD-Datei nach jedem Abschnitt speichern** — `Kap1_Einleitung_DRAFT.md`
6. **Default Output-Level: L1** — Kein L3 ohne explizite Anforderung
7. **Deployer-Scope** — Art. 26, nicht Provider (Art. 16), kein Retirement
8. **Critical Definitions binding** — Enforcement ≠ Dokumentation, etc.
