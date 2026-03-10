# Roter Faden Tracker — Kapiteluebergreifende Argumentationskette

> **SSOT fuer inhaltliche Konsistenz:** Dieses Dokument definiert fuer jedes Kapitel die
> Bruecke zum Vorgaenger, die Kernthese, die Bruecke zum Nachfolger und die Volltextquelle.
> Es ist die primaere Referenz fuer den `thesis-reviewer` Skill (R2) und den `thesis-preflight` Skill (P2).
>
> **Letzte Aktualisierung:** 2026-03-08

---

## Status-Enum (verbindlich fuer alle Artefakte)

```
planned → in_progress → draft → review → final
```

| Status | Bedeutung | Verwendung |
|--------|-----------|-----------|
| `planned` | Noch nicht begonnen | chapter_state, README, thesis_state |
| `in_progress` | Aktiv in Arbeit | chapter_state, README, thesis_state |
| `draft` | Erster Entwurf geschrieben, nicht reviewed | chapter_state, DRAFT-Dateien |
| `review` | Entwurf geschrieben, Review-Phase | chapter_state, README |
| `final` | Abgeschlossen und freigegeben | chapter_state, README |

---

## Kap. 1 — Einleitung

**Status:** `final` (100%)
**Volltextquelle:** `00_workspace/Fulltext_Kapitel/Kapitel 1 Einleitung.docx`

### Bruecke von: (kein Vorgaenger)
Kapitel 1 ist der Einstiegspunkt. Es stellt das Problem dar und motiviert die Arbeit.

### Kernthese:
Die rasante Adaption von GenAI stellt Unternehmen vor drei interdependente Problemdimensionen (PD1: Fragmentierung, PD2: methodische Inadaequanz, PD3: Compliance-Luecke). Der EU AI Act fordert lueckenlose Nachweisfuehrung, fuer die weder Frameworks noch automatisierte Kontrollmechanismen existieren. Die Arbeit entwickelt eine cloud-native Referenzarchitektur mit Quality-Gate-Kontrollsystem zur Operationalisierung regulatorischer Anforderungen.

### Bruecke zu Kap. 2:
Die drei Problemdimensionen erfordern theoretische Fundierung → Kap. 2 liefert die Wissensbasis (Rigor Cycle): GenAI-Grundlagen, Cloud-native, Operationalisierung, Quality Gates, Policy-as-Code → muendet in Forschungsluecke (2.7).

### Abhaengige Decisions:
- Deployer-Scope (Art. 26) etabliert
- RQ1–RQ3 definiert mit DSR-Cycle-Zuordnung

### Forward-References aus Kap. 1:
- RQ1 → Kap. 4
- RQ2 → Kap. 5
- RQ3 → Kap. 6
- DSR-Methodik → Kap. 3

---

## Kap. 2 — Theoretische Grundlagen und Stand der Forschung (Rigor Cycle)

**Status:** `draft` (100% — DRAFT komplett, DOCX-Integration ausstehend)
**Volltextquelle:** `00_workspace/Fulltext_Kapitel/Kapitel 2 Theoretische Grundlagen.docx`

### Bruecke von Kap. 1:
Die drei Problemdimensionen (PD1–PD3) begruenden den Bedarf an theoretischer Fundierung. Kap. 2 liefert die Wissensbasis des DSR Rigor Cycle.

### Kernthese:
Die Wissensbasis zeigt: (1) GenAI/LLMs stellen neuartige operative Herausforderungen (Halluzinationen, Promptabhaengigkeit), (2) Cloud-native Plattformfaehigkeiten sind Voraussetzung fuer Automatisierung, (3) MLOps/LLMOps decken GenAI-spezifische Risiken nicht ab, (4) Der EU AI Act fordert operationalisierbare Compliance, (5) Quality Gates und Policy-as-Code sind Kandidaten fuer die Loesung. Die Synthese (2.7) zeigt die dreifache Forschungsluecke und begruendet den Handlungsbedarf.

### Bruecke zu Kap. 3:
Die identifizierte Forschungsluecke (2.7) erfordert ein systematisches Forschungsdesign → Kap. 3 definiert DSR als Methodik, das Vorgehensmodell und die Evaluationsstrategie.

### Cross-Chapter-Dependencies (aus chapter_state):
- 2.1 → alle Kapitel: Begriffe muessen konsistent durchgehalten werden
- 2.2.3 → 2.3: Enterprise-Herausforderungen motivieren cloud-native Faehigkeiten
- 2.3 → 5.2/5.4: Cloud-native Plattformfaehigkeiten als Architektur-Grundlage
- 2.4.2 → 4.3: EU AI Act Grundlagen fuer Transformationsmethodik
- 2.5 → 5.3: Quality-Gate-Definition als Basis fuer Gate-Taxonomie
- 2.6 → 5.4.2: Policy-as-Code Konzepte fuer Pipeline-Integration
- 2.7 → USP-Analyse: Forschungsluecke muss USP-Positionierung stuetzen

### Abhaengige Decisions:
- D_UNI_HINWEISE_SSOT
- D_PDF_SEITENZAHLEN
- D_KAP2_2_SUBSTRUKTUR

---

## Kap. 3 — Forschungsdesign und Methodik (DSR)

**Status:** `review` (95%)
**Volltextquelle:** `00_workspace/Fulltext_Kapitel/Kapitel_3_Forschungsdesign_und_Methodik.docx`

### Bruecke von Kap. 2:
Die Forschungsluecke (2.7) begruendet den Bedarf an einem konstruktiven Forschungsansatz. Kap. 3 definiert DSR als methodischen Rahmen und legitimiert das Vorgehen.

### Kernthese:
Design Science Research (Hevner 3 Zyklen + Peffers DSRM + vom Brocke DSR Grid) als kombinierter Rahmen. Artefakttyp: Model (Architektur) + Method (Gate-Systematik) + Instantiation (PoC). Zwei Iterationen. Dreistufige Evaluation (Coverage-Matrix, PoC-Walkthrough, Expert-Reviews n>=4). Traceability-Ansatz: RQ → R → DP → Gate → Evidence.

### Bruecke zu Kap. 4:
Kap. 3 definiert Design Cycle Phase 1 (RQ1) → Kap. 4 fuehrt diese Phase durch: systematische Anforderungserhebung aus dem EU AI Act (Relevance Cycle → Design Cycle).

### Abhaengige Decisions:
- D_SCOPE_ART25_RETIREMENT
- D_KAP4_STRUKTUR_FUNKTIONAL
- D_UNI_HINWEISE_SSOT

### Cross-Chapter-Impacts (aus SSOT_ROTER_FADEN_ANALYSE):
- D_4.6_VS_5.3_SEPARATION: Bestaetigt DSR RQ1/RQ2-Trennung an Kapitelgrenze 4→5
- D_NIST_CONVERGENCE: Rigor-Nachweis in 5.1 konsistent mit DSR-Grid
- D_GOV_DIMENSIONS_HYBRID: 4.6 Norm-Analyse + 5.1 Konvergenz = DSR-Zuordnung

---

## Kap. 4 — Design-getriebene Operationalisierung regulatorischer Anforderungen (RQ1)

**Status:** `in_progress` (83%, 4.1–4.5 draft, 4.6 planned)
**Volltextquelle:** `00_workspace/Fulltext_Kapitel/Kapitel 4 Anforderungen.docx`

### Bruecke von Kap. 3:
DSR Design Cycle Phase 1 beginnt → systematische Anforderungserhebung aus dem EU AI Act. Methodik-Entscheidungen MD10/MD11 aus Kap. 3 legitimieren die funktional-logische Struktur.

### Kernthese:
Regulatorische Anforderungen (Art. 9–15 EU AI Act) werden durch dreistufige Transformation (Norm → Requirement R-xx → Gate G-xx) operationalisierbar gemacht. Fuenf aufeinander aufbauende Abschnitte: (4.1) Zielbild: Enforcement ≠ Dokumentation, Accountability-by-Design. (4.2) Lifecycle-Modell: Pre-Deployment/Deployment/Operation. (4.3) Transformationsmethodik: Norm → funktionaler Kontrollmechanismus. (4.4) Kontrollmechanismen: PaC (praev.) + Monitoring (reakt.) + Audit (retrospekt.). (4.5) Human Oversight: Institutionalised Distrust (Laux) + 4 Effektivitaetsbedingungen (Sterz). (4.6) Requirements-Katalog: WAS geprueft werden muss (R-xx).

### Bruecke zu Kap. 5:
4.6 definiert WAS (Requirements-Tabelle R-xx) → 5.3 spezifiziert WIE (Gate-Specs G-xx). D_4.6_VS_5.3_SEPARATION = DSR-logische Trennung Design Cycle Phase 1 → Phase 2.

### Abhaengige Decisions:
D_4.5_STRUCTURE, D_KAP4_PAGES, D_MQG4AI_PLACEMENT, D_2026_SOURCES, D_ART25_DEPTH, D_RETIREMENT_OUT, D_GATE_IDS_LOCATION, D_4.6_SCOPE, D_4.6_VS_5.3_SEPARATION, D_GOV_DIMENSIONS_HYBRID, D_NIST_CONVERGENCE, D_KONSOLIDIERUNG_AUFGELOEST, D_KAP4_BUDGET_FLEX

### Critical Definitions (bindend fuer alle folgenden Kapitel):
- Enforcement ≠ Dokumentation
- Dreistufige Transformation: Norm → Requirement → Gate
- 3 Kontrollmechanismen (PaC, Monitoring, Audit)
- Human Oversight ≠ manuelle Pruefung
- Deployer-Scope (Art. 26), Retirement Out-of-Scope

---

## Kap. 5 — Entwicklung der Referenzarchitektur (RQ2)

**Status:** `in_progress` (20%)
**Volltextquelle:** `00_workspace/Fulltext_Kapitel/Kapitel 5 Architectur Entwicklung.docx`

### Bruecke von Kap. 4:
Die Requirements (R-xx) aus 4.6 werden in Architekturkomponenten umgesetzt. D_4.6_VS_5.3_SEPARATION: WAS → WIE. Die Governance-Dimensionen aus 4.6 werden in 5.1 durch NIST/ISO-Konvergenz als international anerkannte Kategorien bestaetigt (D_GOV_DIMENSIONS_HYBRID).

### Kernthese (geplant):
Die Referenzarchitektur operationalisiert die erhobenen Anforderungen durch vier Saeulen: (S1) Architekturelle Grundstruktur, (S2) Quality-Gate-Kontrollsystem (USP), (S3) Pipeline-Integration, (S4) Evidence- und Audit-Logik (USP). Designprinzipien DP1–DP5 sind in der Knowledge Base verankert (NIST+ISO+EU AI Act Konvergenz). Prototypische Instanziierung als Azure-basierter PoC (Ambient AI Scribe).

### Bruecke zu Kap. 6:
Das konstruierte Artefakt (Architektur + Gate-System + PoC) wird systematisch evaluiert → Kap. 6 fuehrt die dreistufige Evaluation durch (RQ3).

### Abhaengige Decisions (von Kap. 4):
- D_4.6_VS_5.3_SEPARATION (WAS→WIE Grenze)
- D_GOV_DIMENSIONS_HYBRID (Konvergenz in 5.1)
- D_NIST_CONVERGENCE (Rigor-Nachweis in 5.1)
- D_KONSOLIDIERUNG_AUFGELOEST (Clustering → 5.3)

### Erwartete Inhalte:
- 5.1: Designprinzipien + NIST/ISO-Konvergenz (~1 Seite + Tabelle)
- 5.2: Schichten- und Komponentenmodell [S1]
- 5.3: Gate-Taxonomie, Gate-Template, Compliance-Mapping [S2 USP]
- 5.4: CI/CD-Pipeline + Policy-as-Code Integration [S3]
- 5.5: Evidence-Persistierung + Audit-Trail [S4 USP]
- 5.6: PoC Instanziierung (Azure, Healthcare)

---

## Kap. 6 — Evaluation (RQ3)

**Status:** `planned` (0%)
**Volltextquelle:** (noch nicht erstellt)

### Bruecke von Kap. 5:
Die fertige Referenzarchitektur mit PoC wird systematisch evaluiert. DSR Rigor Cycle: Artefakt muss gegen Wissensbasis und Praxisanforderungen geprueft werden.

### Kernthese (geplant):
Dreistufige Evaluation: (1) Requirements-Coverage-Matrix (R1–Rn gegen Architekturkomponenten), (2) PoC-Walkthrough (technische Demonstration im Azure-Stack), (3) Expert-Reviews (n>=4 leitfadengestuetzte Interviews). Triangulation der Ergebnisse zeigt Eignung der Architektur.

### Bruecke zu Kap. 7:
Evaluationsergebnisse werden in Kap. 7 diskutiert, interpretiert und in den Forschungskontext eingeordnet.

---

## Kap. 7 — Diskussion

**Status:** `planned` (0%)
**Volltextquelle:** (noch nicht erstellt)

### Bruecke von Kap. 6:
Die Evaluationsergebnisse werden interpretiert und kritisch reflektiert.

### Kernthese (geplant):
Beantwortung der Forschungsfragen (RQ1–RQ3). Wissenschaftlicher Beitrag (Design Knowledge). Praxisimplikationen. Limitationen (Art. 25 Tiefenanalyse, CLOUD Act/STACKIT → Diagnose #9/#10). Weiterer Forschungsbedarf.

### Bruecke zu Kap. 8:
Diskussion muendet in Fazit → zentrale Ergebnisse verdichtet, Ausblick auf zukuenftige Entwicklungen.

---

## Kap. 8 — Fazit und Ausblick

**Status:** `planned` (0%)
**Volltextquelle:** (noch nicht erstellt)

### Bruecke von Kap. 7:
Diskussionsergebnisse werden zu einem Gesamtfazit verdichtet.

### Kernthese (geplant):
Zusammenfassung der zentralen Ergebnisse. Beitrag der Arbeit zur Forschung und Praxis. Ausblick auf zukuenftige Entwicklungen (GenAIOps-Evolution, regulatorische Dynamik, EU AI Office).

### Bruecke zu: (kein Nachfolger)

---

## Traceability-Kette (Gesamtueberblick)

```
Kap. 1 (Problem) → Kap. 2 (Wissensbasis/Rigor) → Kap. 3 (Methodik/DSR)
    → Kap. 4 (Anforderungen/RQ1 = WAS) → Kap. 5 (Architektur/RQ2 = WIE)
    → Kap. 6 (Evaluation/RQ3) → Kap. 7 (Diskussion) → Kap. 8 (Fazit)
```

```
RQ1 (Relevance) → R-xx (Requirements) → DP1–DP5 (Design Principles)
    → G-xx (Quality Gates) → Evidence (Audit Trail)
```
