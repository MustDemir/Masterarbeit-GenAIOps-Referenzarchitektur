# Thesis State — Single Source of Truth (Schicht 1)

> **Automatisch generiert:** 2026-03-05 20:54  
> **Generator:** `resume.py` → `workflow_lib.build_thesis_state()`  
> **Zweck:** KI-Kontext beim Session-Start. Nicht manuell editieren.

## Expose-Gliederung

→ **SSOT:** [`00_admin/gliederung_v3.md`](gliederung_v3.md)
→ **PDF:** `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf`

## Kapitelstatus

- **Kap. 1 — Einleitung**: Entwurf (10%)
- **Kap. 2 — Theorie & Grundlagen**: In Arbeit (15%)
- **Kap. 3 — Methodik (DSR)**: review (95%) — Finale Review — 7 [MD]-Kommentare im Dokument aufloesen
- **Kap. 4 — Anforderungsanalyse (RQ1)**: in_progress (83%) — 4.1-4.5 fertig (Entwuerfe geschrieben). Naechster Schritt: 4.6 Requirements-Katalog planen — Quellen lesen (Lucaj, Eisenberg, Goncalves, Elia), dann schreiben.
- **Kap. 5 — Referenzarchitektur (RQ2)**: In Arbeit (Evidence Store, Related Work) (20%)
- **Kap. 6 — Evaluation (RQ3)**: Geplant (0%)
- **Kap. 7 — Diskussion**: Geplant (0%)
- **Kap. 8 — Fazit & Ausblick**: Geplant (0%)
- **Expose v4 / Forschungsdesign**: Abgeschlossen (100%)
- **PoC-Implementierung**: Geplant (0%)

## Decisions (alle Kapitel)

| ID | Kapitel | Entscheidung | Rationale-Keyword |
|---|---|---|---|
| D_SCOPE_ART25_RETIREMENT | 03_forschungsdesign_methodik | Art. 25 Provider-Aufstieg als Scope-Grenze dokumentiert, Retirement explizit ausgeschlossen (Provider-Verantwortung Art. 16) | Methodische Scope-Klarstellung: Deployer-Perspektive endet b |
| D_KAP4_STRUKTUR_FUNKTIONAL | 03_forschungsdesign_methodik | Kap. 4 Anforderungsanalyse folgt funktional-logischer Struktur (Lifecycle → Transformation → Kontrolle → Oversight → Katalog) | DSR-Designentscheidung: Prozessorientierung bildet Deployer- |
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

## Critical Definitions (bindend fuer Cross-Chapter-Konsistenz)

- **[04_anforderungsanalyse_RQ1]** Enforcement ≠ Dokumentation: Architektur erzwingt Compliance technisch, nicht nur als Papierspur (4.1)
- **[04_anforderungsanalyse_RQ1]** Pre-Deployment = Datenkuration → Modellvalidierung; Deployment = Integration+Staging+Release; Operation = Monitoring+Audit+PMS (4.2)
- **[04_anforderungsanalyse_RQ1]** Dreistufige Transformation: Norm (Art. 9-15) → Requirement (R-xx) → Gate (G-xx) — keine Zwischenstufe, kein juristischer Kommentar (4.3)
- **[04_anforderungsanalyse_RQ1]** 3 Kontrollmechanismen: Policy-as-Code (praev.), Continuous Monitoring (reakt.), Audit Trails (retrospekt.) — exklusive Zuordnung pro Requirement (4.4)
- **[04_anforderungsanalyse_RQ1]** Human Oversight ≠ manuelle Pruefung: Institutionalised Distrust (Laux) + 4 Effektivitaetsbedingungen (Sterz) als Designprinzip (4.5)
- **[04_anforderungsanalyse_RQ1]** 4.6 = WAS (Requirements R-xx), 5.3 = WIE (Gate-Specs G-xx) — DSR-logische Trennung Design Cycle Phase 1 vs. Phase 2
- **[04_anforderungsanalyse_RQ1]** Deployer-Scope: nur Art. 26 Pflichten, Provider-Pflichten (Art. 16) explizit ausgeschlossen, Art. 25 = Scope-Trigger (4.2)
- **[04_anforderungsanalyse_RQ1]** Retirement-Phase: explizit Out-of-Scope (Provider-Verantwortung Art. 16 Abs. 1 lit. j)

## Cross-Chapter Impacts

Noch keine cross_chapter_impacts in chapter_states definiert.

## Requirements (RQ1)

- R001: (noch ohne Titel) [pre-deployment|deployment|operation]
- R002: (noch ohne Titel) [pre-deployment|deployment|operation]
- R003: (noch ohne Titel) [pre-deployment|deployment|operation]
- R004: (noch ohne Titel) [pre-deployment|deployment|operation]
- R005: (noch ohne Titel) [pre-deployment|deployment|operation]

## Quality Gates (RQ2)

- GCOMP-001 [strategic|technical|compliance]: (noch ohne Name)
- GSTR-001 [strategic|technical|compliance]: (noch ohne Name)
- GTECH-001 [strategic|technical|compliance]: (noch ohne Name)

## Letzte Session-Summaries

### [anforderungen]
- 4.5 Human Oversight — Entwurf triple-verified: (ohne Stichpunkte)
- Kap4 Strukturentscheidungen + Recherche-Auswertung: (ohne Stichpunkte)
- 4.1 Zielbild des Kontrollsystems — Fliesstext mit APA7-Zitaten: (ohne Stichpunkte)

### [architektur]
- Session Summary: Architekturupdate: Wir haben den Blob-Sync in den Workflow integriert.
- Artifact Construction Diagramm + Tool-Verifikation + 3-Quellen-Abgleich: Session: Artifact Construction Diagramm v2 erstellt, Deep Research Tool-Verifikation, 3-Quellen-Abgleich, Prof-Gespraech-Vorbereitung.
- Blob Sync Test: Architekturupdate: Wir haben den Blob-Sync in den Workflow integriert.

### [general]
- Session Summary: (ohne Stichpunkte)
- Session Summary: (ohne Stichpunkte)
- Session Summary: (ohne Stichpunkte)

### [methodik]
- Expose-Deltas in Kapitel 3 ueberfuehrt: Session: Exposé-Deltas in Kapitel 3 überführen (2026-02-28)
- Expose v3 Single Source of Truth, Repo-Alignment, DOCX-Verschluesselung: Expose v3 (2026-02-27) als PDF + TXT in docs/expose/ aufgenommen, alte Version nach legacy verschoben.
- Session Summary: Session: Kapitel-3 Cowork-Nachbereitung — Dateien sortieren, YAML-Konsistenzprüfung

### [methodology]
- Kapitel 3 DSR – Peffers Positionierung, Accountability-by-Design, RQ-Schärfung: Session-Kontext: Fortsetzung nach YAML 20260227_011854_kapitel-3-dsr-hevner-peffers-mapping-poc-demonstration.yaml.
- Kapitel 3 DSR – Hevner/Peffers Mapping & PoC-Demonstration: Session-Ziel: Methodik für Kapitel 3 (Forschungsdesign & Methodik) stabilisieren, ohne Kapiteltext zu schreiben.
- DSR Kapitel 3 – Forschungsdesign & Methodik: Der Benutzer hat nach dem Thema DSR für Kapitel 3 seiner Masterarbeit gefragt und damit die methodische Fokussierung der Arbeit markiert.


---

**3-Schichten-Kontextmodell:**
1. **Schicht 1** (dieses Dokument): Gesamtbild — Decisions, Definitionen, Status
2. **Schicht 2** (Session-Summary YAMLs): Inhaltliche Argumentation pro Session
3. **Schicht 3** (Kapitel-MDs/PDFs): Volltext — nur lesen wenn Schicht 1+2 nicht ausreichen

→ Wenn eine Decision oder Definition fuer den aktuellen Text relevant ist,
  ZUERST die Session-Summary YAML lesen (Schicht 2).
  Nur bei Unsicherheit den Volltext anfordern (Schicht 3).
