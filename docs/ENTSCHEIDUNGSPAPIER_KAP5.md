# Entscheidungspapier Kapitel 5 — Architektur-Decisions

**Datum:** 2026-03-11
**Status:** 10 Entscheidungen (4 aus Preflight 5.1 + 6 aus Preflight 5.2) + 8 übernommene Architektur-Decisions (R1–R8)
**Kontext:** Preflight Kap. 5 Referenzarchitektur (RQ2) — Klärung offener Design-Entscheidungen vor Schreibbeginn

---

## Gesamtübersicht

| # | Decision-ID | Thema | Status | Kern-Ergebnis |
|---|---|---|---|---|
| 1 | D_KAP5_SECTION_ORDER | Schreibreihenfolge Kap. 5 | ✅ FINAL | Sequentiell 5.1→5.2→5.3→5.4→5.5→5.6 |
| 2 | D_DP_NUMBERING | Designprinzipien-Nummerierung | ✅ FINAL | DP1–DP5 (Exposé-SSOT) + DP5.2/DP5.3 als Erweiterungen |
| 3 | D_GATE_ID_SCHEMA | Gate-ID-Format | ✅ FINAL | G-PRE-xx / G-DEP-xx / G-OPS-xx (Lifecycle-Phase-Präfix) |
| 4 | D_GATEKEEPER_STANDALONE | Gatekeeper-Deployment | ✅ FINAL | Standalone OPA Gatekeeper auf AKS, kein Azure Policy Add-on |
| 5 | D_ART11_DIFFERENZIERUNG | Art. 11 DP2/DP3 Abgrenzung | ✅ FINAL | DP2=Art.11 Abs.1 allgemein, DP3=Art.11+Annex IV spezifisch |
| 6 | D_GATE_COUNT | Gate-Anzahl aus R-xx | ✅ FINAL | ~13 Gates (4 PRE + 5 DEP + 4 OPS), R004=Fußnote |
| 7 | D_R005_GATE | R005 dediziertes Gate | ✅ FINAL | G-OPS-05 Evidence-Completeness & Audit-Trail-Integrität |
| 8 | D_R002_SINGLE_GATE | R002 Gate-Granularität | ✅ FINAL | 1 Gate, mehrere Policies; Trennung Gate/Policy in 5.3 |
| 9 | D_ANNEX_IV_INPUT | Annex IV Nutzung | ✅ FINAL | DP3 nutzt Annex IV als Input-Katalog, nicht juristisch |
| 10 | D_BUTT_KERN_PAPER | 5. Kern-Paper für 5.2 | ✅ FINAL | Butt et al. (2026) V6HKHA5B — 5 Gates, Evidence Backbone, C2AT |

---

## Entscheidung 1: D_KAP5_SECTION_ORDER

**Frage:** Sequentielle oder parallele Bearbeitung der Unterabschnitte?

**Entscheidung:** Strikt sequentiell: 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6

**Begründung:**
- 5.3 (Gate-System) benötigt 5.2 (Schichtenmodell) als Architekturrahmen
- 5.4 (Pipeline + PaC) benötigt 5.3 (Gate-Specs) als Input für Rego-Policies
- 5.5 (Evidence) benötigt 5.4 (Pipeline-Output) als Datenquelle
- 5.6 (PoC) instanziiert alle vorherigen Abschnitte

**Datum:** 2026-03-11

---

## Entscheidung 2: D_DP_NUMBERING

**Frage:** DP1–DP5 aus Exposé beibehalten oder auf DP1–DP7 erweitern (Hash-Chain, Immutability)?

**Entscheidung:** DP1–DP5 beibehalten. Hash-Chain und Immutability als DP5.2 und DP5.3 unter DP5 (Evidence-Persistierung) in Abschnitt 5.5 einführen.

**Begründung:**
- Exposé = SSOT für Designprinzipien, keine Umnummerierung
- Hash-Chain und Immutability sind Sub-Aspekte von DP5 (Evidence-Persistierung), keine eigenständigen Top-Level-Prinzipien
- Sub-Nummerierung (DP5.2/DP5.3) zeigt Erweiterungsbedarf ohne Exposé-Drift
- Konsistenz mit Kap. 3 (DSR-Artefaktbeschreibung referenziert DP1–DP5)

**Evidence:**
- Exposé v4: definiert DP1–DP5
- Evidence Store Architektur (eigenes Artefakt): nutzt DP-6/DP-7 → wird zu DP5.2/DP5.3 renummeriert

**Datum:** 2026-03-11

---

## Entscheidung 3: D_GATE_ID_SCHEMA

**Frage:** Welches ID-Format für Quality Gates?

**Optionen analysiert:**
- Option A: `G-PRE-xx`, `G-DEP-xx`, `G-OPS-xx` (Lifecycle-Phase als Präfix)
- Option B: `G-REG-xx`, `G-TECH-xx`, `G-STRAT-xx` (Governance-Dimension als Präfix)
- Option C: `G001`–`Gxxx` (flache Nummerierung)

**Entscheidung:** Option A — Lifecycle-Phase als Präfix.

**Begründung — Literaturanalyse:**

| Quelle | Gate-Organisation | Ergebnis |
|---|---|---|
| Cooper (2008) Stage-Gate | Phase-Gates: Discovery → Launch | Lifecycle-Phase = primäres Ordnungsprinzip |
| Elia et al. (2025) MQG4AI | Lifecycle-Stages: Pre-Development → Post-Deployment | Lifecycle-Phase als Rahmen, Quality Dimensions als Attribute |
| Lucaj et al. (2025) TechOps | Template-Sektionen nach Lifecycle | Kein formales Gate-ID, aber implizit lifecycle-basiert |
| Kholkar et al. (2023) | Stage-Gates in CI/CD | Gates an Pipeline-Stages gebunden |

**Konsequenz:** Governance-Dimension (regulatorisch/technisch/strategisch) wird als Attribut im Gate-Template geführt, nicht im ID. Das ermöglicht:
- Sofortige Lifecycle-Zuordnung beim Lesen (G-PRE = Pre-Deployment)
- Multi-dimensionale Gates (ein Gate kann regulatorisch UND technisch sein)
- Konsistenz mit D_OPA_THREE_PILLAR (Conftest=PRE/DEP, Gatekeeper=DEP/OPS)

**Datum:** 2026-03-11

---

## Entscheidung 4: D_GATEKEEPER_STANDALONE

**Frage:** Azure Policy Add-on oder standalone OPA Gatekeeper auf AKS?

**Entscheidung:** Standalone OPA Gatekeeper.

**Begründung:**
- **R7 (Cloud-agnostisch):** Standalone Gatekeeper läuft identisch auf AKS, EKS, GKE, on-prem
- **Azure Policy Add-on:** Vendor-Lock-in, überschreibt eigene ConstraintTemplates, managed by Microsoft
- **Technische Details:** Helm-Installation, ConstraintTemplates in Rego, Constraints als CRDs
- **PoC-Impact:** Keine Azure-spezifischen Anpassungen nötig. Gleiche Config auf jedem K8s-Cluster

**Abgrenzung:** Azure Policy Add-on kann parallel existieren (für Azure-native Governance), aber die Thesis-Architektur nutzt den standalone Gatekeeper für die eigenen Compliance-Gates.

**Datum:** 2026-03-11

---

## Entscheidung 5: D_ART11_DIFFERENZIERUNG

**Frage:** DP2 und DP3 referenzieren beide Art. 11 EU AI Act in Tab. 5.1 — wie abgrenzen?

**Entscheidung:** DP2 = Art. 11 Abs. 1 allgemein (Nachvollziehbarkeit des gesamten Lifecycle). DP3 = Art. 11 iVm Annex IV (spezifische Dokumentationsinhalte als Input-Katalog für Gate-Attribute).

**Begründung:**
- Art. 11 Abs. 1 fordert eine technische Dokumentation, die den Nachweis der Konformität ermöglicht → DP2 (Traceability) adressiert diese allgemeine Nachweispflicht über R → DP → Gate → Evidence
- Annex IV listet 8 spezifische Dokumentationskategorien (Allgemeine Beschreibung, Datenmanagement, Überwachung etc.) → DP3 (Gate-Template) nutzt diese als strukturellen Input für die 7 Gate-Attribute
- DP3 interpretiert Annex IV als Input-Katalog für technische Gate-Attribute, NICHT als juristische Auslegung (Scope-Caveat PK-SC5)

**Evidence:**
- EU AI Act Art. 11 Abs. 1 + Annex IV §1-8
- Lucaj et al. (2025) TechOps Templates: Template-Sektionen korrespondieren mit Annex IV Kategorien

**Datum:** 2026-03-11

---

## Entscheidung 6: D_GATE_COUNT

**Frage:** Wie viele Gates ergeben sich aus der R-xx → G-xx Gruppierung?

**Entscheidung:** ~13 Gates: 4 Pre-Deployment + 5 Deployment + 4 Operations. R004 (Strategische Verankerung) ist organisatorische Governance → Fußnote in Tab. 5.2, kein technisches Gate.

**Begründung:**
- R001–R014 ergibt nach Clustering (thematische Zusammengehörigkeit + Lifecycle-Phase): 12 technisch prüfbare Gates + G-OPS-05 (R005 dediziert) = 13 Gates
- R004 hat kein Template-Feld in Lucaj TechOps (Coverage-Matrix: 0 Policies) → manueller/strategischer Check
- R002 wird als 1 Gate mit mehreren Policies modelliert (s. D_R002_SINGLE_GATE)
- Gate-Verteilung orientiert sich an Cooper (2008) Stage-Gate-Dichte und Elia (2025) Lifecycle-Stages

**Evidence:**
- MAPPING_LUCAJ_TO_RXX.md: Coverage-Matrix zeigt R004 = 0 Policies
- Cooper (2008): Stage-Gate-Modell, 4-6 Gates typisch
- Elia et al. (2025): Pre-/During-/Post-Deployment Stages

**Datum:** 2026-03-11

---

## Entscheidung 7: D_R005_GATE

**Frage:** R005 (Evidence-Persistierung/Audit-Trail) als Querschnittsaspekt oder dediziertes Gate?

**Entscheidung:** R005 bekommt dediziertes Operations-Gate **G-OPS-05** (Evidence-Completeness & Audit-Trail-Integrität). R014 (Protokollierung) bleibt separat als G-DEP-06.

**Begründung — Literaturanalyse:**

| Quelle | Zotero-Key | Argument für dediziertes Gate |
|---|---|---|
| Muhammad et al. (2026) | — | "Assured Readiness Score" = quantifizierter Evidence-Completeness-Check, aktiver Prüfschritt |
| Butt et al. (2026) | V6HKHA5B | "Conformity Bundle" + "Adequacy Score 0.91" = Evidence-Vollständigkeit als eigenständiges Artefakt |
| Keyes et al. (2025) | — | Stanford RAIL: Integrity-Prinzip fordert "unaltered documentation audit trail" |
| Nweke et al. (2026) | — | OSCAL Assessment Plans + POA&M = formalisierte Evidenzlücken-Behandlung |
| EU AI Act Art. 12 | — | Abs. 1: "automatische Aufzeichnung von Ereignissen (Logging)" als eigenständige Pflicht |

**Konsequenz:**
- G-OPS-05 prüft: (a) Evidence-Vollständigkeit (alle G-xx haben Evidenzartefakte), (b) Audit-Trail-Integrität (Hash-Chain, keine Lücken), (c) Conformity-Bundle-Readiness
- Decision Logs (Säule 2) = Speichermechanismus. G-OPS-05 (Säule 1) = Prüfinstanz die Vollständigkeit verifiziert → verschiedene Ebenen
- Stärkt Kap. 6 PoC (Butt-Metrik "Adequacy Score" als Evaluationskriterium)

**Datum:** 2026-03-11

---

## Entscheidung 8: D_R002_SINGLE_GATE

**Frage:** R002 (Data Governance) hat 5 Policy-Kandidaten in MAPPING_LUCAJ — mehrere Gates oder eines?

**Entscheidung:** R002 = 1 Gate (z.B. G-PRE-02 Data-Governance-Check) mit mehreren Policies darunter. Trennung Gate vs. Policy-Granularität erfolgt erst in Kap. 5.3.

**Begründung:**
- Cooper (2008): Gates = Entscheidungspunkte auf hoher Ebene, nicht Policy-Granularität
- Gate-Template (DP3) abstrahiert: Prüfkriterien können mehrere Policies umfassen
- 5 Lucaj-Policies (provenance, lineage, preprocessing, license, annotation) gehören thematisch zusammen
- Kap. 5.3 definiert dann die Rego-Policy-Hierarchie unter dem Gate

**Datum:** 2026-03-11

---

## Entscheidung 9: D_ANNEX_IV_INPUT

**Frage:** Wie wird Annex IV EU AI Act in der Gate-Spezifikation verwendet?

**Entscheidung:** DP3 nutzt Annex IV als strukturellen Input-Katalog für Gate-Attribute. Die 8 Annex-IV-Kategorien informieren die Prüfkriterien und Evidenzartefakte der Gates, werden aber NICHT als juristische Interpretation verwendet.

**Begründung:**
- PK-SC5 (Scope-Caveat): "Annex IV als technischer Input-Katalog, keine juristische Auslegung"
- Lucaj et al. (2025): TechOps Template-Sektionen annotieren explizit "Art. 11, Annex IV §X" → technische Operationalisierung
- Akademische Redlichkeit: Thesis ist Informatik-Arbeit, keine Rechtswissenschaft

**Datum:** 2026-03-11

---

## Entscheidung 10: D_BUTT_KERN_PAPER

**Frage:** Welche Kern-Papers bilden die Evidenzbasis für Kap. 5.2?

**Entscheidung:** 5 Kern-Papers: Cooper (2008), Elia (2025), Lucaj (2025), Mahr (2024) + **Butt et al. (2026)** als 5. Paper.

**Begründung:**
- Butt et al. (2026) "From Policy to Pipeline" (Zotero V6HKHA5B) definiert:
  - 5 Pipeline-Gates (Data Validation → Model Validation → Pre-Deployment → Deployment → Post-Deployment)
  - "Evidence Backbone" als Konzept für signierte Evidence-Manifeste
  - "Conformity Assessment Toolkit (C2AT)" mit Adequacy Score 0.91
  - "Conformity Bundle" als Aggregationsartefakt
- Direkte Relevanz für G-OPS-05 (Evidence-Completeness) und Kap. 6 Evaluation
- Per D_2026: 2026-Quelle nur als konvergente Evidenz (0 Zitationen), nie als alleinige Stütze

**Evidence:**
- Elicit Report "Automating AI Compliance with Policy-as-Code" (2026-03-11)
- Zotero V6HKHA5B bestätigt

**Datum:** 2026-03-11

---

## Übernommene Architektur-Decisions R1–R8

> Quelle: `.memory/entscheidungsregister.md` Sektion 3 (aus Design-Thinking Sessions Feb/März 2026).
> Diese Decisions sind in keinem chapter_state dokumentiert und weiterhin gültig.

| ID | Datum | Entscheidung | Auswirkung auf Kap. 5 |
|---|---|---|---|
| R1 | 2026-02-24 | Diagramme: S/W, große Schrift (15–22pt), Times New Roman | 5.2 Architektur-Diagramm, 5.4 Pipeline-Diagramm |
| R2 | 2026-02-24 | 3-Quellen-Verifikation (Exposé × Diagramm × USPs) | QS-Maßnahme für jede Architekturentscheidung |
| R3 | 2026-02-26 | Harte Trennung: med. Payload (Blob, verschlüsselt) vs. regulat. Telemetrie (SQL) | 5.5 Evidence Store Architektur |
| R4 | 2026-02-28 | DP4 = thematische Prüfdimensionen (NICHT hierarchisch) | 5.1 Designprinzipien, 5.3 Gate-Taxonomie |
| R5 | 2026-02-28 | Make-or-Buy = vorgelagerte Governance-Entscheidung, KEIN Gate | 5.3 Negativ-Checklist |
| R6 | 2026-03-02 | 3D-Taxonomie + einheitliches Gate-Template (Trigger/Kriterien/Evidence/Decision/Owner/Audit/Waiver) | 5.3 Gate-Template-Definition |
| R7 | 2026-03-02 | Cloud-agnostisch portabel, Azure als PoC-Referenz | 5.2 + 5.6 |
| R8 | 2026-02-25 | CDV-Framework: Contract → Validation → Severity → Pipeline-Decision | 5.3 Gate-Decision-Logik |

---

## Decision-Precedence-Regel

Bei Konflikten zwischen Entscheidungsquellen gilt:

**Kap. 4 chapter_state > Kap. 3 chapter_state > Kap. 2 chapter_state > Kap. 1 chapter_state > .memory/entscheidungsregister.md**

Neueste Decision gewinnt immer. Das Entscheidungsregister (.memory/) ist veraltet (Stand 2026-03-05), enthält aber R1–R8 als einzige Quelle → diese bleiben gültig.

---

## Bindende Decisions aus Kap. 4 chapter_state (Referenz)

Diese Decisions aus Kap. 4 sind für Kap. 5 direkt bindend und werden NICHT hier wiederholt, sondern per Referenz eingebunden:

- D_4.6_VS_5.3_SEPARATION — WAS (R-xx) → WIE (G-xx)
- D_GOV_DIMENSIONS_HYBRID — Governance-Dimensionen durch NIST/ISO legitimieren
- D_NIST_CONVERGENCE — Konvergenz-Tabelle in 5.1
- D_KONSOLIDIERUNG_AUFGELOEST — Clustering → Gate-Taxonomie
- D_OPA_THREE_PILLAR — Conftest / Gatekeeper / Decision Logs
- D_GATEKEEPER_SCOPE — PoC: 2 Label + 1 technischer Constraint
- D_LOG_BACKEND — Decision Logs → PostgreSQL Evidence Store
- D_LUCAJ_STARTING_BASIS — TechOps Templates als Rego-Ausgangsbasis
- D_POC_REGO_K8S — Echter Rego-Code auf AKS

→ Details: `04_anforderungsanalyse_RQ1/chapter_state.yaml`

---

## Nächste Arbeitsschritte

1. ✅ Kap. 5 chapter_state initialisiert
2. ✅ Abschnitt 5.1 geschrieben (~980W, 5 Absätze + Tab. 5.1)
3. ✅ R1–R8 in chapter_state Kap. 5 übernommen
4. ✅ Entscheidungsregister mit D_1–D_4 synchronisiert (2026-03-11)
5. ✅ D_5–D_10 aus Preflight 5.2 eingetragen (2026-03-11)
6. ☐ Abschnitt 5.2 schreiben (Gate-Spezifikation, ~13 Gates, Tab. 5.2)
7. ☐ Kap. 5.3 Policy Engine + Rego
8. ☐ Kap. 5.4–5.6
