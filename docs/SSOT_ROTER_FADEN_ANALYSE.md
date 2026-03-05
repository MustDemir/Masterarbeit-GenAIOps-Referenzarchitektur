# Analytischer Bericht: SSOT "Roter Faden" für die Masterarbeit

**Datum:** 2026-03-05
**Zweck:** IST-Analyse, Lücken-Identifikation, Konzept für ein persistentes Single-Source-of-Truth-System in Git
**Scope:** Alle Kapitel (1–8), Exposé, Workflow-Tools, Session-Management

---

## 1. IST-ANALYSE: Was existiert bereits?

### 1.1 Chapter-State-Dateien (8 Kapitel)

| Datei | Status | Reifegrad | Entscheidungen | Inhaltszusammenfassungen |
|-------|--------|-----------|----------------|--------------------------|
| `01_einleitung/chapter_state.yaml` | Entwurf, 10% | **Skelett** — kein `done`, kein `current_focus`, keine `decisions` | 0 | Nein |
| `02_rigor_theorie/chapter_state.yaml` | In Arbeit, 15% | **Skelett** — identisch leer | 0 | Nein |
| `03_methodik/chapter_state.yaml` | Review, 95% | **Ausgereift** — 25 done-Items, 4 review_comments, 2 decisions (D_SCOPE_ART25_RETIREMENT, D_KAP4_STRUKTUR_FUNKTIONAL), key_sources | 2 | Teilweise (done-Liste beschreibt Entscheidungen, aber keine Abschnittszusammenfassungen) |
| `04_anforderungen/chapter_state.yaml` | In Arbeit, 83% | **Am ausgereiftesten** — 43 done-Items, 14 decisions (D_4.5 bis D_KAP4_BUDGET_FLEX), chapter_structure mit Kern-Papers, page_budget, key_sources, open_questions, Zotero-Mapping | 14 | Indirekt (done-Items + session_summaries enthalten Kernthesen) |
| `05_architektur/chapter_state.yaml` | In Arbeit, 20% | **Skelett** | 0 | Nein |
| `06_evaluation/chapter_state.yaml` | Geplant, 0% | **Skelett** | 0 | Nein |
| `07_diskussion/chapter_state.yaml` | Geplant, 0% | **Skelett** | 0 | Nein |
| `08_fazit/chapter_state.yaml` | existiert | **Skelett** | 0 | Nein |

**Befund 1:** Nur Kap. 3 und Kap. 4 haben substantielle chapter_state-Dateien. Kap. 1, 2, 5–8 sind Skelette ohne Decisions, ohne key_sources, ohne Inhaltszusammenfassungen.

### 1.2 Session Summaries (Kap. 4)

7 YAML-Dateien in `04_anforderungsanalyse_RQ1/session_summaries/`, alle mit detailliertem `inhalt`-Feld:

| Summary | Abschnitt | Inhalt-Qualität |
|---------|-----------|-----------------|
| `20260304_003014_4-1-zielbild.yaml` | 4.1 | ✅ Vollständig (6 Architektur-Guidelines, Kernthese, 26 APA7) |
| `20260305_012416_strukturentscheidungen.yaml` | Kap. 4 gesamt | ✅ Vollständig (5 FINAL-Entscheidungen, Quellenabdeckung) |
| `20260305_050000_4-2-lifecycle.yaml` | 4.2 | ✅ Vollständig (Dreistufiges Modell, Konvergenz, Kernthese) |
| `20260305_050100_4-3-transformation.yaml` | 4.3 | ✅ Vollständig (4 Dekompositionsstrategien, Dreistufige Transformation) |
| `20260305_050200_4-4-kontrollmechanismen.yaml` | 4.4 | ✅ Vollständig (3 Mechanismen, RegOps-Integration, Kernthese) |
| `20260305_040042_4-5-human-oversight.yaml` | 4.5 | ✅ Vollständig (Sterz 4 Bedingungen, Laux, Deployer-Provider-Asymmetrie) |
| `20260305_220000_related-work-vergleich.yaml` | Kap. 4 (Quer) | Vorhanden |

**Befund 2:** Die MD-Fließtexte (4.1–4.5) sind NICHT in chapter_state.yaml zusammengefasst — aber die Session Summaries enthalten vollständige inhaltliche Zusammenfassungen aller 5 Abschnitte. Das ist de facto der "Roter Faden" für Kap. 4, verteilt über 7 YAML-Dateien.

### 1.3 Entscheidungsregister (.memory/entscheidungsregister.md)

- 192 Zeilen, 14 Sektionen
- Enthält: M1–M11 (Methodik), A1–A11 (Anforderungen), R1–R8 (Architektur), P1–P4 (Prozess)
- **VERALTET:** Kapitelstatus zeigt Kap. 4 bei 35% (real: 83%), 4.2–4.5 als "pending" (real: "done")
- **FEHLEND:** D_4.6_SCOPE, D_4.6_VS_5.3_SEPARATION, D_GOV_DIMENSIONS_HYBRID, D_NIST_CONVERGENCE, D_KONSOLIDIERUNG_AUFGELOEST, D_KAP4_BUDGET_FLEX (alle 6 neuen Decisions aus der letzten Session)

**Befund 3:** Das Entscheidungsregister ist eine wertvolle Ressource, aber manuell gepflegt und aktuell nicht synchron mit chapter_state.yaml. Es liegt in `.memory/` (gitignored!) und ist damit NICHT Teil des Git-SSOT.

### 1.4 Resume-Kontext (.memory/resume_context.txt)

- Generiert durch `resume.py` / `reindex.py`
- Zeigt Kapitelstatus, Requirements, Gates, letzte Session Summaries
- **VERALTET:** Kap. 4 Fokus zeigt "4.2-Entscheidungen FINAL" statt "4.1-4.5 fertig, 4.6 planen"
- Liegt in `.memory/` (gitignored!)

**Befund 4:** resume_context.txt ist veraltet und nicht in Git.

### 1.5 Workflow-Tools

| Tool | Funktion | SSOT-Relevanz |
|------|----------|---------------|
| `save.py` | Session-Summary erstellen + Index aktualisieren + Fortschritt-Update | **HOCH** — Erzeugt Session-YAMLs, aktualisiert chapter_state progress |
| `resume.py` | Index + Resume-Text generieren | **HOCH** — Generiert Kontext-Snapshot |
| `reindex.py` | Index + Resume + Azure Push | **HOCH** — Synchronisiert alles |
| `validate_structure.py` | Prüft Konventionen (Expose, Images, Summaries) | **MITTEL** — Strukturprüfung |
| `weekly_audit.py` | 13 Prüfungen + GitHub Issue | **HOCH** — Erkennt Stale-States, Traceability-Lücken |
| `scripts/update_progress.py` | README-Fortschrittsbalken aktualisieren | **MITTEL** — Visuell |
| `scripts/generate_diagrams.py` | Diagramm-Generierung | NIEDRIG |
| `extract_yamls.py` | YAML-Blöcke aus Chat extrahieren | **MITTEL** — Hilft bei Session-Rettung |
| `workflow_lib.py` | Shared Library für alle Scripts | **KERN** — Indexierung, Azure, Blob |

**Befund 5:** Die Tools existieren und sind gut strukturiert. ABER: `resume.py` und `reindex.py` schreiben nur nach `.memory/` (gitignored). Der generierte Kontext geht nach jedem `git clone` verloren.

### 1.6 Exposé-State

- Exposé v4 liegt als `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf`
- **KEIN** `docs/expose/chapter_state.yaml` oder Abweichungsprotokoll
- Differenzen D1–D7 und Lücken L1–L3 sind im Entscheidungsregister dokumentiert (Sektion 10) — aber das Register ist gitignored

**Befund 6:** Exposé-Abweichungen werden nirgends in Git getrackt.

---

## 2. LÜCKEN-ANALYSE

### 2.1 Kritische Lücken (🔴)

| # | Lücke | Auswirkung |
|---|-------|------------|
| G1 | **Entscheidungsregister in .memory/ (gitignored)** | Geht bei Clone/neuer Maschine verloren. Enthält 40+ Entscheidungen, Konsistenzanalyse, Prüfprotokoll |
| G2 | **resume_context.txt in .memory/ (gitignored)** | Session-Start ohne Kontext. Muss jedes Mal neu generiert werden |
| G3 | **Kap. 3 chapter_state hat KEINE Kap.-4-Implikationen** | D_4.6_VS_5.3_SEPARATION betrifft DSR-Methodik (RQ1/RQ2-Trennung), D_NIST_CONVERGENCE betrifft Rigor-Nachweis — beides in Kap. 3 unerwähnt |
| G4 | **6 neue Decisions NICHT im Entscheidungsregister** | Register zeigt veralteten Stand |
| G5 | **Chapter-State Kap. 4: next_steps veraltet** | Zeigt "4.2 schreiben" obwohl 4.2–4.5 done sind |
| G6 | **Exposé-Abweichungen nirgends in Git** | D1–D7 / L1–L3 nur in gitignored .memory/ |
| G7 | **Kap. 1, 2, 5–8 chapter_states sind Skelette** | Kein roter Faden für ungeschriebene Kapitel — Architektur-Entscheidungen (R1–R8) nicht in Kap. 5 state |

### 2.2 Moderate Lücken (🟡)

| # | Lücke | Auswirkung |
|---|-------|------------|
| G8 | **Kein automatischer Konsistenz-Check zwischen chapter_states** | Entscheidung in Kap. 4 kann Kap. 3/5 widersprechen ohne Warnung |
| G9 | **Session Summaries als Inhalts-Surrogate statt chapter_state** | Inhaltszusammenfassungen nur in 7 einzelnen YAMLs, nicht konsolidiert |
| G10 | **Seitenbudget in chapter_state Kap. 4 aktualisiert (14-15), aber Entscheidungsregister zeigt 13** | Inkonsistenz zwischen den beiden "Wahrheitsquellen" |

---

## 3. KONZEPT: SSOT "ROTER FADEN"

### 3.1 Design-Prinzipien

1. **Git = einzige Wahrheit** — Alles Persistente muss committed sein, nichts nur in .memory/
2. **Minimaler Aufwand** — Kein neues Tool, sondern bestehende Strukturen erweitern
3. **Session-Start-Protokoll** — Eine einzige Datei, die den kompletten Stand zeigt
4. **Bidirektionale Traceability** — Entscheidung ↔ Kapitel ↔ Abschnitt ↔ Quelle

### 3.2 Vorgeschlagene Maßnahmen (priorisiert)

#### Maßnahme M1: Entscheidungsregister nach Git verschieben (🔴 Kritisch)

**IST:** `.memory/entscheidungsregister.md` (gitignored)
**SOLL:** `docs/entscheidungsregister.md` (committed)
**Aufwand:** 1 Minute (mv + git add)
**Wirkung:** 40+ Entscheidungen, Konsistenzanalyse, Prüfprotokoll = persistent

#### Maßnahme M2: Exposé-Abweichungsprotokoll erstellen (🔴 Kritisch)

**IST:** D1–D7 / L1–L3 nur im Entscheidungsregister Sektion 10
**SOLL:** Eigene Datei `docs/expose/expose_deltas.yaml` mit:
```yaml
expose_version: "v4_2026-02-28"
deltas:
  - id: D1
    beschreibung: "Kap. 4 funktional-logische Struktur"
    status: "ERLEDIGT — M11 in Kap. 3"
  - id: D2
    beschreibung: "Beweislast-Asymmetrie fehlt im Exposé"
    status: "IN ARBEIT — Kap. 1 Entwurf existiert"
    ziel_kapitel: "Kap. 1"
  # ...
```
**Aufwand:** 10 Minuten
**Wirkung:** Exposé-Abweichungen in Git getrackt, Gutachter-sicher

#### Maßnahme M3: chapter_state Kap. 4 next_steps aktualisieren (🔴 Kritisch)

**IST:** next_steps zeigen "4.2 schreiben" (veraltet)
**SOLL:** next_steps auf aktuellem Stand: "4.6 Requirements-Katalog planen, Quellen lesen"
**Aufwand:** 2 Minuten (YAML editieren)
**Wirkung:** Session-Start zeigt korrekten Fokus

#### Maßnahme M4: Kap. 3 chapter_state um Kap.-4-Implikationen erweitern (🟡 Wichtig)

**IST:** 2 decisions (M10, M11), keine Querverweise auf Kap. 4/5
**SOLL:** Neue Felder:
```yaml
cross_chapter_impacts:
  - source: "D_4.6_VS_5.3_SEPARATION"
    impact: "Bestätigt DSR-Trennung RQ1/RQ2 an Kapitelgrenze 4→5"
  - source: "D_NIST_CONVERGENCE"
    impact: "Rigor-Nachweis in 5.1 — konsistent mit Kap. 3 DSR-Grid"
  - source: "D_GOV_DIMENSIONS_HYBRID"
    impact: "4.6 Norm-Analyse + 5.1 Konvergenz = saubere DSR-Zuordnung"
```
**Aufwand:** 5 Minuten
**Wirkung:** Kapitelübergreifende Konsistenz nachvollziehbar

#### Maßnahme M5: Skelett-Chapter-States mit Kap.-4-Entscheidungen anreichern (🟡 Wichtig)

**Betrifft:** Kap. 1 (Beweislast-Asymmetrie), Kap. 2 (MQG4AI-Abgrenzung), Kap. 5 (R1–R8, D_4.6_VS_5.3, D_NIST_CONVERGENCE, D_GOV_DIMENSIONS_HYBRID), Kap. 7 (Art. 25 Tiefenanalyse, CLOUD Act, DP3)
**Aufwand:** 15 Minuten (4 Dateien editieren)
**Wirkung:** Jedes Kapitel kennt seine Vorgaben, bevor es geschrieben wird

#### Maßnahme M6: Entscheidungsregister synchronisieren (🟡 Wichtig)

**IST:** 6 neue Decisions fehlen, Kapitelstatus veraltet
**SOLL:** D_4.6_SCOPE bis D_KAP4_BUDGET_FLEX nachtragen, Kap. 4 Status auf 83% korrigieren, 4.2–4.5 als done markieren
**Aufwand:** 10 Minuten
**Wirkung:** Entscheidungsregister = konsistenter SSOT

#### Maßnahme M7: Session-Start-Datei aus Git generierbar machen (🟢 Optional)

**IST:** `resume.py` schreibt nach `.memory/` (gitignored)
**SOLL:** Option `--git-output docs/thesis_state_snapshot.md` die einen committed Snapshot erzeugt
**Aufwand:** 20 Minuten (resume.py erweitern)
**Wirkung:** `git pull` genügt, um aktuellen Stand zu sehen — kein `resume.py` nötig

#### Maßnahme M8: weekly_audit.py um Cross-Chapter-Decision-Check erweitern (🟢 Optional)

**IST:** Prüft Struktur, Security, Artifacts, Traceability (R↔G)
**SOLL:** Neuer Check: Decisions in chapter_state Kap. X referenzieren Kap. Y → prüfen ob Y.chapter_state davon weiß
**Aufwand:** 30–45 Minuten
**Wirkung:** Automatische Inkonsistenz-Erkennung

---

## 4. KAPITEL-3-KONSISTENZ-PRÜFUNG

### Was Kap. 3 bereits weiß:
- D_SCOPE_ART25_RETIREMENT (Art. 25 + Retirement als Scope-Grenzen) ✅
- D_KAP4_STRUKTUR_FUNKTIONAL (funktional-logische Struktur als DSR-Entscheidung) ✅

### Was Kap. 3 noch NICHT weiß (aber wissen sollte):

| Decision | Relevanz für Kap. 3 | Handlung |
|----------|---------------------|----------|
| D_4.6_VS_5.3_SEPARATION | Bestätigt DSR RQ1/RQ2-Trennung an Kapitelgrenze | → `cross_chapter_impacts` |
| D_NIST_CONVERGENCE | Rigor-Nachweis: NIST+ISO+EU = Knowledge Base für DP1–DP5 | → `cross_chapter_impacts` |
| D_GOV_DIMENSIONS_HYBRID | 4.6 Norm + 5.1 Konvergenz = DSR-Zuordnung Design/Relevance | → `cross_chapter_impacts` |
| D_KAP4_BUDGET_FLEX | 14-15 statt 13 Seiten → Gesamtbudget prüfen | → `page_budget` Update |
| D_KONSOLIDIERUNG_AUFGELOEST | Gliederungsänderung ggü. Exposé | → `expose_deltas` |

**Ergebnis:** Kein WIDERSPRUCH zu Kap. 3 — aber 3 Decisions (D_4.6_VS_5.3, D_NIST_CONVERGENCE, D_GOV_DIMENSIONS_HYBRID) stärken die DSR-Argumentation und sollten als Querverweise aufgenommen werden.

---

## 5. EXPOSÉ-ABWEICHUNGEN (für expose_deltas.yaml)

| ID | Abweichung | Status | Begründung |
|----|-----------|--------|------------|
| D1 | Kap. 4 funktional-logische Struktur | ✅ ERLEDIGT (M11) | DSR-Designentscheidung |
| D2 | Beweislast-Asymmetrie nicht im Exposé | IN ARBEIT | → Kap. 1 Entwurf existiert |
| D3 | MQG4AI fehlt im Exposé | GEPLANT | → Kap. 2 + 4.6 |
| D4 | Human Oversight (4.5) nicht im Exposé | AKZEPTIERT | 162 kumul. Zit. |
| D5 | Post-Market Surveillance (Art. 72) fehlt | GEPLANT | → 4.6 R-PMS-01 |
| D6 | Seitenbudget nicht explizit im Exposé | AKZEPTIERT | Implizit |
| D7 | 19 Kern-Papers in Kap. 3.5 integrieren | IN ARBEIT | Literaturtabelle erweitern |
| D8 | **NEU:** Alter 4.5 Konsolidierung aufgelöst | AKZEPTIERT | → 4.6/5.1/5.3 |
| D9 | **NEU:** Kap. 4 Budget 14-15 statt 13 | AKZEPTIERT | Kernbeitrag nicht kürzen |
| D10 | **NEU:** NIST-Konvergenz als eigener Abschnitt in 5.1 | AKZEPTIERT | Rigor-Nachweis |

---

## 6. MD-INHALTE IN CHAPTER_STATE — PRÜFERGEBNIS

**Frage:** Sind die Inhalte der 5 MD-Fließtexte (4.1–4.5) als Zusammenfassung in chapter_state.yaml erfasst?

**Antwort: TEILWEISE — über zwei Ebenen verteilt.**

| MD-Datei | In chapter_state.yaml? | In Session Summary? |
|----------|----------------------|---------------------|
| 4.1 Zielbild | `done`-Liste enthält Kern-Stichpunkte, aber keine strukturierte Zusammenfassung | ✅ `20260304_003014` — vollständige Argumentation |
| 4.2 Lifecycle | `chapter_structure` enthält nur Kern-Papers, nicht die Argumentation | ✅ `20260305_050000` — Dreistufiges Modell, Konvergenz |
| 4.3 Transformation | `chapter_structure` enthält nur Kern-Papers | ✅ `20260305_050100` — 4 Strategien, Dreistufige Transformation |
| 4.4 Kontrollmechanismen | `chapter_structure` enthält nur Kern-Papers | ✅ `20260305_050200` — PaC/Monitoring/Audit, RegOps |
| 4.5 Human Oversight | `done`-Liste erwähnt Sterz/Laux, aber kein Argument-Detail | ✅ `20260305_040042` — Sterz 4 Bedingungen, Laux, Mapping |

**Empfehlung:** Die Session Summaries SIND de facto die Inhaltszusammenfassungen. Sie müssen NICHT redundant in chapter_state kopiert werden — aber chapter_state sollte auf sie VERWEISEN:
```yaml
content_summaries:
  "4.1": "session_summaries/20260304_003014_abschnitt-4-1-zielbild-kontrollsystem-fliesstext-mit-apa7-zitaten.yaml"
  "4.2": "session_summaries/20260305_050000_4-2-lifecycle-modell-entwurf.yaml"
  "4.3": "session_summaries/20260305_050100_4-3-transformationsmethodik-entwurf.yaml"
  "4.4": "session_summaries/20260305_050200_4-4-kontrollmechanismen-entwurf.yaml"
  "4.5": "session_summaries/20260305_040042_4-5-human-oversight-abgeschlossen-triple-verified.yaml"
```

---

## 7. ZUSAMMENFASSUNG DER EMPFEHLUNGEN

### Sofort umsetzen (< 30 Min, hoher Impact):
1. **M1:** Entscheidungsregister → `docs/` (mv + git add)
2. **M2:** `docs/expose/expose_deltas.yaml` erstellen
3. **M3:** chapter_state Kap. 4 next_steps aktualisieren
4. **M6:** Entscheidungsregister synchronisieren (6 neue Decisions)

### Diese Woche umsetzen (< 1 Std):
5. **M4:** Kap. 3 chapter_state um cross_chapter_impacts erweitern
6. **M5:** Skelett-Chapter-States anreichern (Kap. 1, 2, 5, 7)
7. **Kap. 4 chapter_state:** `content_summaries`-Mapping hinzufügen

### Optional (nächste Session):
8. **M7:** resume.py um `--git-output` erweitern
9. **M8:** weekly_audit.py um Cross-Chapter-Decision-Check erweitern

---

## 8. BESTEHENDE BEST PRACTICES (beibehalten)

- ✅ Chapter-State-Dateien pro Kapitel als Statusträger
- ✅ Session Summaries mit `inhalt`-Feld als Argumentationssicherung
- ✅ `save.py` → `reindex.py` Workflow für Persistenz
- ✅ `weekly_audit.py` für automatisierte Strukturprüfung
- ✅ `validate_structure.py` für Konventionsprüfung
- ✅ YAML-basiertes Session-Management mit Topic-Routing
- ✅ Verschlüsselte PDFs für Fließtext (kein Plaintext-Leak)
- ✅ Konsistenz-Prüfprotokoll (Sektion 14 im Entscheidungsregister)

---

*Dieser Bericht ist eine Analyse — keine Umsetzung. Maßnahmen werden erst nach Freigabe implementiert.*
