# Thesis State — Single Source of Truth (Schicht 1)

> **Automatisch generiert:** 2026-03-13 22:43  
> **Generator:** `resume.py` → `workflow_lib.build_thesis_state()`  
> **Zweck:** KI-Kontext beim Session-Start. Nicht manuell editieren.

## Expose-Gliederung

→ **SSOT:** [`00_admin/gliederung_v3.md`](../00_admin/gliederung_v3.md)
→ **PDF:** `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf`

## Kapitelstatus

- **Kap. 1 — Einleitung**: Fertig (100%)
- **Kap. 2 — Theoretische Grundlagen und Stand der Forschung (Rigor Cycle)**: draft (100%) — Alle Abschnitte 2.1-2.7 geschrieben (~4062W). Review 4.1/5.0. Naechster Schritt: DOCX-Integration + Seitenverifizierung + Zotero-Eintraege
- **Kap. 3 — Methodik (DSR)**: review (95%) — Finale Review — 7 [MD]-Kommentare im Dokument aufloesen
- **Kap. 4 — Anforderungsanalyse (RQ1)**: done (100%) — Kap. 4 KOMPLETT. 4.6 Requirements-Katalog Fliesstext fertig (6/6 Absaetze, ~1.069W, 28 MATCH). Anhang A erstellt. Lucaj TechOps Templates geklont + R-xx Mapping erstellt. Naechster Schritt: Kap. 5 Preflight.
- **Kap. 5 — Referenzarchitektur (RQ2)**: in_progress (70%) — Kap. 5.1+5.2+5.2.2+5.2.3+5.3 FERTIG. Kap. 5.4 Preflight-Vorbereitung DONE. Naechster Schritt: Preflight Kap. 5.4 durchlaufen + GO.
- **Kap. 6 — Evaluation (RQ3)**: planned (0%)
- **Kap. 7 — Diskussion**: planned (0%)
- **Kap. 8 — Fazit & Ausblick**: planned (0%)
- **Expose v4 / Forschungsdesign**: Abgeschlossen (100%) — Abgeschlossen — Expose v4 FINAL eingereicht
- **PoC-Implementierung**: Geplant (0%) — Noch nicht gestartet — beginnt in Iteration 2

## lade_manifest (Kapitel-Abhängigkeiten)

### 01_einleitung
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 1 Einleitung.docx`, `01_einleitung/arbeitsmaterial/drafts/Kap1_Einleitung_DRAFT.md`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`
- **kontext** (chapter_state only): `03_forschungsdesign_methodik`, `04_anforderungsanalyse_RQ1`

### 02_rigor_theorie_stand_forschung
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 2 Theoretische Grundlagen.docx`, `02_rigor_theorie_stand_forschung/arbeitsmaterial/drafts/Kap2_Theoretische_Grundlagen_DRAFT.md`, `00_workspace/Fulltext_Kapitel/Kapitel 1 Einleitung.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`
- **kontext** (chapter_state only): `03_forschungsdesign_methodik`, `04_anforderungsanalyse_RQ1`

### 03_forschungsdesign_methodik
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`, `03_forschungsdesign_methodik/arbeitsmaterial/drafts/Kap3_Forschungsdesign_DRAFT.md`, `00_workspace/Fulltext_Kapitel/Kapitel 1 Einleitung.docx`
- **kontext** (chapter_state only): `04_anforderungsanalyse_RQ1`, `05_referenzarchitektur_RQ2`

### 04_anforderungsanalyse_RQ1
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 4 Anforderungen.docx`, `04_anforderungsanalyse_RQ1/KAPITEL_4_GESAMT_DRAFT.md`, `docs/ENTSCHEIDUNGSPAPIER_KAP4.md`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 2 Theoretische Grundlagen.docx`
- **kontext** (chapter_state only): `05_referenzarchitektur_RQ2`

### 05_referenzarchitektur_RQ2
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 5 Architectur Entwicklung.docx`, `docs/ENTSCHEIDUNGSPAPIER_KAP5.md`, `docs/ENTSCHEIDUNGSPAPIER_KAP4.md`, `00_workspace/Fulltext_Kapitel/Kapitel 4 Anforderungen.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`
- **kontext** (chapter_state only): `02_rigor_theorie_stand_forschung`, `01_einleitung`

### 06_evaluation_RQ3
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 5 Architectur Entwicklung.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 4 Anforderungen.docx`, `docs/ENTSCHEIDUNGSPAPIER_KAP5.md`, `docs/ENTSCHEIDUNGSPAPIER_KAP4.md`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`
- **kontext** (chapter_state only): `01_einleitung`, `02_rigor_theorie_stand_forschung`

### 07_diskussion
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 5 Architectur Entwicklung.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 4 Anforderungen.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 2 Theoretische Grundlagen.docx`, `docs/ENTSCHEIDUNGSPAPIER_KAP5.md`, `docs/ENTSCHEIDUNGSPAPIER_KAP4.md`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`
- **kontext** (chapter_state only): `01_einleitung`, `03_forschungsdesign_methodik`, `06_evaluation_RQ3`

### 08_fazit_ausblick
- **pflicht** (Volltext): `docs/uni_vorgaben/pruefkatalog.md`, `00_workspace/Fulltext_Kapitel/Kapitel 1 Einleitung.docx`, `00_workspace/Fulltext_Kapitel/Kapitel 3 Forschungsdesign_und_Methodik.docx`
- **kontext** (chapter_state only): `05_referenzarchitektur_RQ2`, `06_evaluation_RQ3`, `07_diskussion`

## Decisions (alle Kapitel)

| ID | Kapitel | Entscheidung | Rationale-Keyword |
|---|---|---|---|
| D_UNI_HINWEISE_SSOT | 02_rigor_theorie_stand_forschung | Verweis auf kapiteluebergreifende Decision in Kap. 3 chapter_state | docs/uni_vorgaben/ als bindende SSOT — Details siehe 03_fors |
| D_PDF_SEITENZAHLEN | 02_rigor_theorie_stand_forschung | Alle Zitationen verwenden PDF-Viewer-Seitenzahlen, nicht Journal-Seitenzahlen | Konsistenz und Nachpruefbarkeit — User kann direkt im PDF-Re |
| D_KAP2_2_SUBSTRUKTUR | 02_rigor_theorie_stand_forschung | Kap. 2.2 erhaelt Sub-Punkte 2.2.1-2.2.3 in Gliederung v3 | Foundation Models/Emergence als eigenstaendiger Absatz benoe |
| D_SCOPE_ART25_RETIREMENT | 03_forschungsdesign_methodik | Art. 25 Provider-Aufstieg als Scope-Grenze dokumentiert, Retirement explizit ausgeschlossen (Provider-Verantwortung Art. 16) | Methodische Scope-Klarstellung: Deployer-Perspektive endet b |
| D_KAP4_STRUKTUR_FUNKTIONAL | 03_forschungsdesign_methodik | Kap. 4 Anforderungsanalyse folgt funktional-logischer Struktur (Lifecycle → Transformation → Kontrolle → Oversight → Katalog) | DSR-Designentscheidung: Prozessorientierung bildet Deployer- |
| D_UNI_HINWEISE_SSOT | 03_forschungsdesign_methodik | docs/uni_vorgaben/ als bindende SSOT fuer alle Kapitel registriert: (1) Prof. Prinz Stilrichtlinien (Referenzierdichte, keine formalen Ueberleitungen, Blablameter-Check, Ergebnisse kontextualisieren), (2) SRH Masterarbeit_Vorbereitung (Bewertungskriterien 50/30/20, max. 4 Gliederungsebenen, 60-80 Textseiten) | Qualitaetssicherung: Universitaere Vorgaben muessen in allen |
| D_LADE_MANIFEST | 03_forschungsdesign_methodik | Per-chapter lade_manifest mit 2-Tier-System in chapter_state.yaml eingefuehrt: (1) pflicht = Volltext laden (DOCXs, DRAFTs, Entscheidungspapiere, Uni-Vorgaben), (2) kontext = nur chapter_state.yaml lesen. Universelle pflicht-Dateien fuer alle 8 Kapitel: Kap. 3 DOCX (DSR/Forschungsdesign) + docs/uni_vorgaben/pruefkatalog.md. Integration als Ergaenzung (nicht Ersatz) in alle 6 Workflow-Skills: Preflight (P0), Writer (Kontext-Sektion), Reviewer (Kontext-Setup), Consistency (Kontext-Setup), Post-Session (erweiterter B-Check), Session-Manager (erweiterter S3). | Kontextfokussierung fuer KI-gestuetzte Workflow-Skills: Gezi |
| D_4.5_STRUCTURE | 04_anforderungsanalyse_RQ1 | 4.5 Human Oversight bleibt eigener Abschnitt | 162 kumulative Zitationen (Laux 63 + Sterz 51 + Enqvist 48) |
| D_KAP4_PAGES | 04_anforderungsanalyse_RQ1 | Kap. 4 Zielbudget ~13 Seiten | 60-80 Seiten Gesamtthesis |
| D_MQG4AI_PLACEMENT | 04_anforderungsanalyse_RQ1 | Elia et al. (2025)/MQG4AI zitieren in Kap. 2 Related Work + Kurzreferenz Kap. 4.6 | Wissenschaftliche Redlichkeit |
| D_2026_SOURCES | 04_anforderungsanalyse_RQ1 | 2026-Quellen (Butt, Leon) nur als konvergente Evidenz | 0 Zitationen |
| D_ART25_DEPTH | 04_anforderungsanalyse_RQ1 | Art. 25 Provider-Aufstieg: 1-2 Absaetze innerhalb 4.2, KEIN eigener Sub-Abschnitt | Art |
| D_RETIREMENT_OUT | 04_anforderungsanalyse_RQ1 | Retirement-Phase explizit ausgeschlossen (nicht unter Operation subsumiert) | Model-Dekommissionierung = Provider-Verantwortung (Art |
| D_GATE_IDS_LOCATION | 04_anforderungsanalyse_RQ1 | Gate-IDs (G-PRE-01 etc.) erst in 4.6, in 4.2 nur konzeptionell | Saubere Traceability-Kette: 4 |
| D_4.6_SCOPE | 04_anforderungsanalyse_RQ1 | 4.6 Requirements-Katalog substanziell (~3-4 Seiten), zeigt systematische Anforderungsableitung | Kernbeitrag von Kap |
| D_4.6_VS_5.3_SEPARATION | 04_anforderungsanalyse_RQ1 | 4.6 = WAS geprüft werden muss (Requirements-Tabelle R-xx), 5.3 = WIE Gates technisch spezifiziert werden (Template, Trigger, Decision-Logik G-xx) | DSR-logisch: 4 |
| D_GOV_DIMENSIONS_HYBRID | 04_anforderungsanalyse_RQ1 | Governance-Dimensionen hybrid: 4.6 einfuehren als Ergebnis der Norm-Analyse, 5.1 Konvergenz-Nachweis mit NIST/ISO | 4 |
| D_NIST_CONVERGENCE | 04_anforderungsanalyse_RQ1 | NIST-Harmonisierung als Konvergenz-Argumentation in 5.1 (~1 Seite + Tabelle), nicht nur Mapping | Konvergenz NIST AI RMF + ISO 42001 + EU AI Act = Rigor-Nachw |
| D_KONSOLIDIERUNG_AUFGELOEST | 04_anforderungsanalyse_RQ1 | Alter Abschnitt 4.5 Konsolidierung wird aufgeloest: Governance-Dimensionen → 4.6, NIST-Harmonisierung → 5.1, Clustering → 5.3 | Konsolidierung war kein eigenstaendiger DSR-Beitrag |
| D_KAP4_BUDGET_FLEX | 04_anforderungsanalyse_RQ1 | Kap. 4 Seitenbudget flexibel auf ~14-15 Seiten erhoehen wenn noetig | 4 |
| D_4.6_BUDGET_OVERRIDE | 04_anforderungsanalyse_RQ1 | Kap. 4 Budget auf ~16-17 Seiten erhoeht, Requirements-Tabelle als Anhang (Tabelle 1) zaehlt nicht zum Seitenbudget | 14 Requirements (R001-R014) benoetigen substanzielle Tabelle |
| D_4.6_GRANULARITY_FULL | 04_anforderungsanalyse_RQ1 | Keine R-xx Limitierung. 14 Requirements (R001-R014), vollstaendige Art. 9-15 + Art. 26/27/50/72/73 Abdeckung | Systematische Anforderungsableitung erfordert lueckenlose Ar |
| D_4.6_TABLE_APPENDIX | 04_anforderungsanalyse_RQ1 | Requirements-Tabelle als Anhang (Tabelle 1) im APA7-Referenzstil, nicht im Fliesstext | Kompakte Darstellung aller 14 R-xx mit ID |
| D_R002_SPLIT | 04_anforderungsanalyse_RQ1 | R002 aufgeteilt: Art. 11 (Doku) bleibt R002, Art. 13 (Transparenz) → R007, Art. 12 (Logging) → R014 | Ein Mega-Requirement (3 Artikel) verletzt die 1:1-Traceabili |
| D_OPA_THREE_PILLAR | 04_anforderungsanalyse_RQ1 | Drei-Saeulen-Architektur: Conftest (Pre-Deployment/Deployment CI), Gatekeeper (Operations K8s Admission), OPA Decision Logs (Querschnitt Audit) | Lifecycle-Mapping: Conftest = statische Checks vor Deploymen |
| D_GATEKEEPER_SCOPE | 04_anforderungsanalyse_RQ1 | Gatekeeper-PoC: 2 Label-Constraints (eu-ai-act/risk-class, eu-ai-act/deployer-assessment) + 1 technischer Constraint (Monitoring-Sidecar required) | Minimaler PoC-Scope zeigt sowohl symbolische (Label) als auc |
| D_LOG_BACKEND | 04_anforderungsanalyse_RQ1 | OPA Decision Logs → bestehender Evidence Store (PostgreSQL compliance.quality_gate_results), kein separates Log-System | Wiederverwendung des Evidence Store mit Hash-Chain (DP-7) ve |
| D_LUCAJ_STARTING_BASIS | 04_anforderungsanalyse_RQ1 | Lucaj TechOps Templates (Application/Model/Data Documentation) als Ausgangsbasis fuer Rego-Policy-Ableitung | Templates bieten EU AI Act-annotierte Checklisten (Art |
| D_POC_REGO_K8S | 04_anforderungsanalyse_RQ1 | PoC implementiert echten Rego-Code auf K8s/AKS (Azure), nicht nur konzeptionell | Kolloquium-Demo zeigt: git push → Conftest CI → Gatekeeper A |
| D_KAP5_SECTION_ORDER | 05_referenzarchitektur_RQ2 | Sequentiell: 5.1→5.2→5.3→5.4→5.5→5.6 | Jede Section baut auf vorheriger auf; Reader-Flow + Traceabi |
| D_DP_NUMBERING | 05_referenzarchitektur_RQ2 | DP1-DP5 beibehalten (Expose = SSOT). Hash-Chain + Immutability als DP5.2/DP5.3 Sub-Extensions in 5.5 | Expose-SSOT nicht brechen; Sub-Extensions statt neuer DPs |
| D_GATE_ID_SCHEMA | 05_referenzarchitektur_RQ2 | Option A: G-PRE-xx, G-DEP-xx, G-OPS-xx (Lifecycle-Phase-Prefix) | Literaturanalyse: Cooper Stage-Gate |
| D_GATEKEEPER_STANDALONE | 05_referenzarchitektur_RQ2 | Standalone OPA Gatekeeper auf AKS (kein Azure Policy Add-on) | Cloud-agnostisch per R7 |
| D_ART11_DIFFERENZIERUNG | 05_referenzarchitektur_RQ2 | DP2=Art.11 Abs.1 allgemein (Lifecycle-Traceability), DP3=Art.11+Annex IV (Gate-Attribute Input-Katalog) | Annex IV = technischer Input |
| D_GATE_COUNT | 05_referenzarchitektur_RQ2 | 16 Gate-Instanzen: 5 PRE + 6 DEP + 5 OPS operationalisieren 14 Anforderungen. R001→2 Gates (G-PRE-01+G-PRE-03), R006→2 Gates (G-PRE-04+G-OPS-04). R004=HYBRID G-PRE-05, R014=G-DEP-06. | Cooper D1-Pruefung zeigt Gate-Eignung |
| D_R005_GATE | 05_referenzarchitektur_RQ2 | R005 → dediziertes G-OPS-05 (Evidence-Completeness & Audit-Trail-Integritaet) | Muhammad (2026) Assured Readiness Score |
| D_R002_SINGLE_GATE | 05_referenzarchitektur_RQ2 | R002 = 1 Gate mit mehreren Policies. Trennung Gate/Policy erst in 5.3 | Cooper: Gates = Entscheidungspunkte |
| D_ANNEX_IV_INPUT | 05_referenzarchitektur_RQ2 | DP3 nutzt Annex IV als Input-Katalog fuer Gate-Attribute (nicht juristisch) | PK-SC5 Scope-Caveat; Lucaj Templates annotieren Annex IV |
| D_BUTT_KERN_PAPER | 05_referenzarchitektur_RQ2 | Butt et al. (2026) V6HKHA5B als 5. Kern-Paper fuer 5.2 | 5 Gates |
| D_DSR_EVIDENCE_STORE | 05_referenzarchitektur_RQ2 | PostgreSQL Evidence Store Schema als DSR-Artefakt in Kap. 5.4 spezifiziert (5 Komponenten: Immutability-Trigger, Privacy Views, RBAC, Composite Indexes, quality_gate_results Table) | DDL ist formale testbare Spezifikation |
| D_QUALITY_OVER_PAGES | 05_referenzarchitektur_RQ2 | Qualitaet > Seitenzahl. Ueberschreitung des 15-18 Seiten Budgets fuer Kap. 5 erlaubt wenn inhaltlich begruendet. | User-Entscheidung: Lieber gruendlich als komprimiert |

## Critical Definitions (bindend fuer Cross-Chapter-Konsistenz)

- **[04_anforderungsanalyse_RQ1]** Enforcement ≠ Dokumentation: Architektur erzwingt Compliance technisch, nicht nur als Papierspur (4.1)
- **[04_anforderungsanalyse_RQ1]** Pre-Deployment = Datenkuration → Modellvalidierung; Deployment = Integration+Staging+Release; Operation = Monitoring+Audit+PMS (4.2)
- **[04_anforderungsanalyse_RQ1]** Dreistufige Transformation: Norm (Art. 9-15) → Requirement (R-xx) → Gate (G-xx) — keine Zwischenstufe, kein juristischer Kommentar (4.3)
- **[04_anforderungsanalyse_RQ1]** 3 Kontrollmechanismen: Policy-as-Code (praev.), Continuous Monitoring (reakt.), Audit Trails (retrospekt.) — exklusive Zuordnung pro Requirement (4.4)
- **[04_anforderungsanalyse_RQ1]** Human Oversight ≠ manuelle Pruefung: Institutionalised Distrust (Laux) + 4 Effektivitaetsbedingungen (Sterz) als Designprinzip (4.5)
- **[04_anforderungsanalyse_RQ1]** 4.6 = WAS (Requirements R-xx), 5.3 = WIE (Gate-Specs G-xx) — DSR-logische Trennung Design Cycle Phase 1 vs. Phase 2
- **[04_anforderungsanalyse_RQ1]** Deployer-Scope: nur Art. 26 Pflichten, Provider-Pflichten (Art. 16) explizit ausgeschlossen, Art. 25 = Scope-Trigger (4.2)
- **[04_anforderungsanalyse_RQ1]** Retirement-Phase: explizit Out-of-Scope (Provider-Verantwortung Art. 16 Abs. 1 lit. j)
- **[05_referenzarchitektur_RQ2]** 4.6 = WAS (Requirements R-xx), 5.3 = WIE (Gate-Specs G-xx) — DSR-logische Trennung (D_4.6_VS_5.3_SEPARATION)
- **[05_referenzarchitektur_RQ2]** Gate-ID-Schema: G-{PHASE}-{NN} mit PHASE ∈ {PRE, DEP, OPS} (D_GATE_ID_SCHEMA)
- **[05_referenzarchitektur_RQ2]** Drei-Saeulen-Architektur: Conftest (Pre-Dep/Dep CI) + Gatekeeper (Ops Admission) + Decision Logs (Audit) (D_OPA_THREE_PILLAR)
- **[05_referenzarchitektur_RQ2]** DP1-DP5 = Expose-SSOT, DP5.2 Hash-Chain + DP5.3 Immutability als Sub-Extensions (D_DP_NUMBERING)
- **[05_referenzarchitektur_RQ2]** Cloud-agnostisch portabel, Azure = PoC-Referenz (R7)
- **[05_referenzarchitektur_RQ2]** CDV-Framework: Contract → Validation → Severity → Pipeline-Decision (R8)
- **[05_referenzarchitektur_RQ2]** Governance-Dimensionen: regulatorisch/technisch/strategisch als Gate-Template-Attribute (nicht hierarchisch). R004 = HYBRID Gate G-PRE-05, R014 = G-DEP-06. 16 Gate-Instanzen (5+6+5) operationalisieren 14 R-xx. R001→2 Gates, R006→2 Gates (Doppelzuordnung begruendet). (D_GOV_DIMENSIONS_HYBRID, D_GATE_COUNT)
- **[05_referenzarchitektur_RQ2]** 29 Policy-Kandidaten aus MAPPING_LUCAJ_TO_RXX = initiale erweiterbare Ausgangsbasis (nicht Architektur-Konstante). Lucaj = Input-Katalog, Architektur = Enforcement-Framework

## Cross-Chapter Impacts

Noch keine cross_chapter_impacts in chapter_states definiert.

## Requirements (RQ1)

- R001: Risikomanagement fuer High-Risk GenAI muss nachweisbar operationalisiert sein [pre-deployment]
- R002: Technische Dokumentation und Protokollierung muessen auditierbar verfuegbar sein [deployment]
- R003: Robustheit, Genauigkeit und Sicherheitschecks muessen vor Promotion bestanden sein [deployment]
- R004: Human Oversight muss vor produktiver Nutzung organisatorisch verankert sein [pre-deployment]
- R005: Evidence-Persistierung muss manipulationssicher und rueckverfolgbar erfolgen [operation]
- R006: Eingabedaten-Qualitaet muss vor Verarbeitung durch das High-Risk-System geprueft sein [deployment]
- R007: Nutzertransparenz und Informationspflichten muessen vor Einsatz erfuellt sein [deployment]
- R008: Operative Oversight-Wirksamkeit muss kontinuierlich nachgewiesen werden [operation]
- R009: Schwerwiegende Vorfaelle muessen erkannt, dokumentiert und gemeldet werden [operation]
- R010: Post-Market Surveillance und Drift-Monitoring muessen operativ implementiert sein [operation]
- R011: Konformitaetserklaerung und CE-Kennzeichnung muessen vor Einsatz geprueft sein [pre-deployment]
- R012: Grundrechte-Folgenabschaetzung muss vor Einsatz durchgefuehrt und dokumentiert sein [pre-deployment]
- R013: Bias- und Fairness-Monitoring muss im laufenden Betrieb implementiert sein [operation]
- R014: Automatische Protokollierung muss aktiviert und auswertbar konfiguriert sein [deployment]

## Quality Gates (RQ2)

- GCOMP-001 [compliance]: Compliance Gate: EU AI Act Mindestnachweise vor Produktivsetzung
- GSTR-001 [strategic]: Strategic Gate: Human Oversight und Verantwortungsmodell
- GTECH-001 [technical]: Technical Gate: Qualitaets- und Robustheitskriterien

## Letzte Session-Summaries

### [anforderungen]
- 4.5 Human Oversight — Entwurf triple-verified: (ohne Stichpunkte)
- Kap4 Strukturentscheidungen + Recherche-Auswertung: (ohne Stichpunkte)
- 4.1 Zielbild des Kontrollsystems — Fliesstext mit APA7-Zitaten: (ohne Stichpunkte)

### [architektur]
- Session Summary: Architekturupdate: Wir haben den Blob-Sync in den Workflow integriert.
- Artifact Construction Diagramm + Tool-Verifikation + 3-Quellen-Abgleich: Session: Artifact Construction Diagramm v2 erstellt, Deep Research Tool-Verifikation, 3-Quellen-Abgleich, Prof-Gespraech-Vorbereitung.
- Blob Sync Test: Architekturupdate: Wir haben den Blob-Sync in den Workflow integriert.

### [einleitung]
- Kap1 Einleitung fertiggestellt: Kapitel 1 Einleitung komplett abgeschlossen. 6 Abschnitte (1.1-1.6), ~2.075 Wörter (~6,9 Seiten). Alle Prüfprotokolle verifiziert. Kap. 1.1: Urgency-Argumente eingefügt (Art. 113 Fristen, Art. 99 Sanktionen, Blancato...

### [general]
- Session Summary: (ohne Stichpunkte)
- Session Summary: (ohne Stichpunkte)
- Session Summary: Session: SSOT-Workflow Stabilisierung + Keyword-Audit

### [methodik]
- Expose-Deltas in Kapitel 3 ueberfuehrt: Session: Exposé-Deltas in Kapitel 3 überführen (2026-02-28)
- Expose v3 Single Source of Truth, Repo-Alignment, DOCX-Verschluesselung: Expose v3 (2026-02-27) als PDF + TXT in docs/expose/ aufgenommen, alte Version nach legacy verschoben.
- Session Summary: Session: Kapitel-3 Cowork-Nachbereitung — Dateien sortieren, YAML-Konsistenzprüfung

### [methodology]
- Kapitel 3 DSR – Peffers Positionierung, Accountability-by-Design, RQ-Schärfung: Session-Kontext: Fortsetzung nach YAML 20260227_011854_kapitel-3-dsr-hevner-peffers-mapping-poc-demonstration.yaml.
- Kapitel 3 DSR – Hevner/Peffers Mapping & PoC-Demonstration: Session-Ziel: Methodik für Kapitel 3 (Forschungsdesign & Methodik) stabilisieren, ohne Kapiteltext zu schreiben.
- DSR Kapitel 3 – Forschungsdesign & Methodik: Der Benutzer hat nach dem Thema DSR für Kapitel 3 seiner Masterarbeit gefragt und damit die methodische Fokussierung der Arbeit markiert.

### [theorie]
- Kap2 Zitationspruefung + Workflow-Cleanup: Session 2026-03-10: Systematische Zitationspruefung Kap. 2 gegen PDF-Quellen (67 Zitationen, 4 Agents parallel). 7 Seitenzahl-Korrekturen im DRAFT angewendet: Feuerriegel S.4→S.3-4, Billeter S.2→S.3, Novelli S.2→S.3,...
- Kap2 Review + PK-V1 Fixes: Session: Kap. 2 Volltext-Review mit thesis-reviewer Skill (6 Instanzen R1-R6). Ergebnis: 4.1/5.0 Gut. Bewertungsbericht gespeichert in docs/bewertung/BEWERTUNG_KAP2_2026-03-09.md. 2 PK-V1-Formulierungen bereinigt: 2.4...
- Kap 2.2 abgeschlossen - Generative KI und LLMs: Session 2026-03-08: Kap. 2.2 Generative KI und LLMs abgeschlossen. 3 Absaetze geschrieben: 2.2.1 Generative Modellierung und Abstraktionsebenen, 2.2.2 Foundation Models Emergence und Homogenisierung, 2.2.3 Enterprise-...


---

**3-Schichten-Kontextmodell:**
1. **Schicht 1** (dieses Dokument): Gesamtbild — Decisions, Definitionen, Status
2. **Schicht 2** (Session-Summary YAMLs): Inhaltliche Argumentation pro Session
3. **Schicht 3** (Kapitel-MDs/PDFs): Volltext — nur lesen wenn Schicht 1+2 nicht ausreichen

→ Wenn eine Decision oder Definition fuer den aktuellen Text relevant ist,
  ZUERST die Session-Summary YAML lesen (Schicht 2).
  Nur bei Unsicherheit den Volltext anfordern (Schicht 3).
