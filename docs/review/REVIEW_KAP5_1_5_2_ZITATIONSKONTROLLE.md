# Zitations- und Inhaltskontrolle Kap. 5.1 + 5.2
**Datum:** 2026-03-11 | **Reviewer:** Claude (Post-Session-Kontrolle) | **Scope:** Fließtext + Prüfprotokolle + Tab. 5.1 + Tab. 5.2

---

## 1. CRITICAL FINDINGS (müssen vor nächster Session gefixt werden)

### F-01: R014 fehlt in Tab. 5.2 — keine Gate-Zuordnung

**Problem:** R014 ("Automatische Protokollierung muss aktiviert und auswertbar konfiguriert sein") hat in Tab. 5.2 weder ein Gate noch eine Fußnote (wie R004). Fließtext 5.2 Absatz 3 schreibt: "überführt die vierzehn Anforderungen aus Kapitel 4.6 in konkrete Gate-Spezifikationen", aber nur 12 unique R-xx erscheinen in der Tabelle (R001 und R006 je 2×, R004 als Fußnote → 13 adressiert, R014 = 0).

**MAPPING_LUCAJ zeigt:** R014 hat 2 Policy-Kandidaten (Conftest + Decision Logs) und ist dem Evidence Store + Model Versioning zugeordnet.

**Fließtext 5.1:** DP5 → R007, R013, **R014** — R014 ist explizit als DP5-Requirement gelistet.

**Lösungsoptionen:**
- **(A)** R014 in G-OPS-05 integrieren (Evidence-Completeness umfasst auch Protokollierung) → Fußnote oder Klammervermerk in Tab. 5.2
- **(B)** Eigenes Gate G-OPS-06 oder G-DEP-06 für R014 → erhöht Gate-Count auf 15
- **(C)** Fußnote analog R004: "R014 wird durch die Protokollierungsfunktion des Evidence Store (5.4) und der Decision Logs (5.3) querschnittlich adressiert"
- **Empfehlung:** Option (A) oder (C) — R014 ist eng mit R005 verwandt (Logging ⊂ Evidence-Persistierung). Fußnote + Anpassung des Fließtexts in 5.2 Absatz 3 ("dreizehn der vierzehn Anforderungen" oder R014-Fußnote).

---

### F-02: Governance-Dimension Terminologie-Inkonsistenz

**Problem:** Fließtext und Tab. 5.2 verwenden unterschiedliche Governance-Dimensionen.

| Quelle | Dimensionen |
|---|---|
| 5.1 Absatz 2 (DP4) | regulatorisch, technisch, **strategisch** |
| 5.1 Absatz 3 (DP4) | regulatorisch, technisch, **strategisch** |
| 5.2 Absatz 2 | regulatorisch, technisch, **strategisch** |
| 5.2 Absatz 3 | regulatorisch, technisch, **strategisch** |
| **Tab. 5.2 (Gov.-Dim.)** | Regulatorisch, Technisch, **Compliance** |
| chapter_state critical_def | **strategisch**/technisch/**compliance** |

- "Strategisch" erscheint 4× im Fließtext, aber 0× in Tab. 5.2
- "Compliance" erscheint 1× in Tab. 5.2 (G-OPS-05), aber 0× in Fließtext-Definitionen
- R004 (=Human Oversight, organisatorisch verankert) hat kein Gate → "strategisch" hat kein Gate

**Lösungsoptionen:**
- **(A)** G-OPS-05 Gov.-Dim. auf "Regulatorisch" ändern (Evidence-Completeness ist regulatorisch getrieben)
- **(B)** Dimensionen auf {regulatorisch, technisch, compliance} vereinheitlichen und "strategisch" im Fließtext durch "compliance" ersetzen
- **(C)** Vierte Dimension "compliance" explizit einführen (dann DP4 → "vier Governance-Dimensionen")
- **Empfehlung:** Option (A) ist minimal-invasiv. "Compliance" bei G-OPS-05 ist sinnvoll, passt aber nicht zur 3-Dimensionen-Definition. Alternativ: Fließtext erweitern um "compliance" als Ausprägung von "regulatorisch" zu erklären.

---

## 2. MEDIUM FINDINGS (sollten gefixt werden)

### F-03: Prüfprotokoll-Labels in 5.1 stimmen nicht mit R-xx Originaltiteln überein

Die Prüfprotokolle in 5.1 verwenden **falsche** Kurzbezeichnungen für die R-xx:

| R-xx | Originalitel (Kap. 4) | PP-Label 5.1 | Korrekt? |
|---|---|---|---|
| R002 | Technische Dokumentation und Protokollierung | "Human-Oversight" | ❌ (das ist R004/R008) |
| R003 | Robustheit, Genauigkeit und Sicherheitschecks | "techn. Doku" | ❌ (das ist R002) |
| R004 | Human Oversight organisatorisch verankert | "strat. Gov" | ⚠ (interpretativ) |
| R005 | Evidence-Persistierung manipulationssicher | "Data-Gov" | ❌ (das ist R006) |
| R009 | Schwerwiegende Vorfälle erkannt/gemeldet | "Monitoring" | ⚠ (das ist eher R010) |

**Auswirkung:** Nicht im Fließtext, nur in Prüfprotokollen. Aber bei einem Review wäre das verwirrend.
**Fix:** PP-Labels an Originaltitel anpassen.

---

### F-04: Tab. 5.2 Gate-Kurztitel vs. R-xx Originaltitel — partielle Diskrepanz

| Gate-ID | R-xx | Gate-Kurztitel | R-xx Originaltitel | Match? |
|---|---|---|---|---|
| G-DEP-01 | R002 | Data Governance | Techn. Dokumentation + Protokollierung | ⚠ |
| G-PRE-02 | R012 | Zweckbestimmung | Grundrechte-Folgenabschätzung | ⚠ |
| G-PRE-04 | R006 | Security-Baseline | Eingabedaten-Qualität | ⚠ |

**Auswirkung:** Gate-Kurztitel reflektieren die *operationalisierte Funktion*, nicht den wörtlichen R-xx Titel. Das ist fachlich OK (ein Requirement kann anders operationalisiert werden als sein Titel suggeriert), aber ein Reviewer könnte die Zuordnung hinterfragen.
**Empfehlung:** Im Fließtext bei Absatz 3 kurz erklären, dass Gate-Kurztitel die operationalisierte Prüffunktion bezeichnen, nicht den wörtlichen Requirement-Titel.

---

## 3. MINOR FINDINGS (optional)

### F-05: 5.1 Absatz 5 (Vier-Säulen-Modell) ohne externe Zitation

Der gesamte Absatz 5 (~180W) referenziert nur eigene Konstrukte, Forward-References und Art. 72 EU AI Act (ohne formale Zitation). Als Synthese-/Überleitungsabsatz akzeptabel, aber ein strenger Reviewer könnte eine Quelle erwarten.
**Empfehlung:** Optional Art. 72 formal zitieren: "(Art. 72 Abs. 1 EU AI Act)".

### F-06: D_GATE_COUNT in chapter_state leicht veraltet

chapter_state sagt: `~13 Gates: 4 PRE + 5 DEP + 4 OPS. R004 = Fussnote`
Tatsächlich nach D_R005_GATE: 14 Gates (4 PRE + 5 DEP + **5** OPS).
**Fix:** D_GATE_COUNT auf "14 Gates: 4 PRE + 5 DEP + 5 OPS" aktualisieren.

---

## 4. ZITATIONS-VERIFIKATION (Ergebnis)

### Cooper (2008) — XU3I543D ✅
| Zitat im DRAFT | Im PDF bestätigt? |
|---|---|
| "Gates are where senior management meets to decide..." (S. 7) | ✅ Exakt im Fulltext |
| "Deliverables... must-meet criteria... should-meet criteria..." (S. 4) | ✅ Exakt im Fulltext |

### Butt et al. (2026) — V6HKHA5B ✅
| Zitat im DRAFT | Im PDF bestätigt? |
|---|---|
| "five gates—Data, Training, Validation, Release, Operations..." (S. 4) | ✅ Exakt |
| "unified schema to ensure consistent evidence structure..." (S. 7) | ✅ Exakt |
| "Three outcomes exist. A pass authorizes promotion..." (S. 7) | ✅ Exakt |
| "Data Gate determines eligibility for training..." (S. 13) | ✅ Exakt |
| "C2AT then derives clause coverage deterministically..." (S. 13) | ✅ Exakt |
| "Rules enforce: (i) a global discriminative minimum (AUROC ≥ 0.86)..." (S. 15) | ✅ Exakt |
| "OG enforces waiver expiry..." (S. 15) | ✅ Exakt |

### Lucaj et al. (2025) — 5Y79UTJ9 ⚠
Zotero-Fulltext nicht verfügbar (HTTP 404). Zitationen S. 3 und S. 6 **können nicht automatisch verifiziert werden**. Manuelle Prüfung gegen PDF erforderlich.

### Hevner et al. (2004) — YUERCAVB
Nicht in dieser Session via Zotero geprüft (wurde in früheren Sessions bestätigt).

### NIST AI RMF (2023) — 5765DKTD
Nicht in dieser Session via Zotero geprüft (wurde in früheren Sessions bestätigt).

### Huwyler (2025) — UE5LVI97
Nicht in dieser Session via Zotero geprüft (wurde in früheren Sessions bestätigt).

---

## 5. GESAMTBEWERTUNG

| Kategorie | Befund |
|---|---|
| **Zitationsabdeckung** | Hoch — alle wesentlichen Thesen belegt. 1 Lücke: Absatz 5 in 5.1 (akzeptabel) |
| **Zitationsgenauigkeit** | ✅ Alle geprüften Zitate (Cooper, Butt) wortgetreu im Original bestätigt |
| **Inhaltliche Konsistenz** | 2 CRITICAL Issues: R014-Lücke, Governance-Terminologie |
| **Prüfprotokolle** | 40 Einträge (5+35), alle ✅ PASSED — aber 5 PP-Labels in 5.1 fehlerhaft |
| **Forward-References** | Alle konsistent mit chapter_structure |
| **DSR-Verankerung** | Solide: Hevner + Peffers korrekt referenziert |
| **EU AI Act** | Art. 6, 9, 11, 14, 15, 72 korrekt eingebunden |

**Priorität nächste Session:** F-01 (R014) und F-02 (Governance-Dimension) vor Preflight 5.3 klären.
