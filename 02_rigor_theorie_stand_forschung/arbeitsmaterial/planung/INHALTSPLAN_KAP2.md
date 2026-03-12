# Inhaltsplan Kapitel 2 — Theoretische Grundlagen und Stand der Forschung (Rigor Cycle)

> **Stand:** 2026-03-07 | **Status:** Entwurf — Freigabe durch User pending
> **Gesamtbudget:** ~14 Seiten (~4.200 Woerter) | **Gliederung:** 7+2 Abschnitte

---

## Funktion im DSR-Rahmen

Kap. 2 = **Rigor Cycle** nach Hevner et al. (2004): Wissensbasis aufbauen, die den Design Cycle (Kap. 4+5) fundiert.
Jeder Abschnitt muss eine **klare Bruecke** zum spaeter genutzten Wissen schlagen.
Kein Selbstzweck — nur was fuer Kap. 4-7 gebraucht wird.

---

## 2.1 Begriffsabgrenzung und Systemkontext (~1,5 Seiten / ~450W)

**Funktion:** Begriffliche Grundlagen fuer die gesamte Arbeit legen. Definiert 6 Kernbegriffe.
**Bruecke von Kap. 1:** Kap. 1.6 definiert Scope → 2.1 konkretisiert die zentralen Begriffe

**Inhalte:**
- LLM (Large Language Model) — Definition, Abgrenzung zu klassischem ML
- GenAI-System — als Oberbegriff (LLM + Infrastruktur + Serving + Monitoring)
- RAG (Retrieval-Augmented Generation) — Pattern, nicht Produkt
- LLMOps / GenAIOps — Arbeitsdefinition, Abgrenzung zu MLOps (Detailabhandlung → 2.4.1)
- Quality Gate — Arbeitsdefinition (Detailabhandlung → 2.5)
- Policy-as-Code — Arbeitsdefinition (Detailabhandlung → 2.6)

**Primaerquellen (Zotero):**
- Bommasani et al. (2021) — Foundation Models Report [KEY: manuell]
- Vaswani et al. (2017) — Transformer-Architektur [Basis]
- Lewis et al. (2020) — RAG Original-Paper
- Kreuzberger et al. (2023) [QY49ZYXB] — MLOps Definition
- Cardoso et al. / Xu et al. (2025) [P998PMS3] — RAGOps
- Tantithamthavorn et al. (2025) [C755FHJK] — MLOps/LLMOps/FMOps Taxonomie

**Negativ-Checklist:**
- ❌ Keine ausfuehrliche LLM-Architektur (→ 2.2)
- ❌ Keine EU AI Act Details (→ 2.4.2)
- ❌ Keine MLOps-Geschichte (→ 2.4.1)
- ❌ Nur Arbeitsdefinitionen — Tiefe in jeweiligen Abschnitten

---

## 2.2 Generative KI und LLMs (~1,5 Seiten / ~450W)

**Funktion:** Technische Grundlagen von GenAI-Systemen, die fuer die Architektur relevant sind.
**Bruecke von 2.1:** Arbeitsdefinitionen → jetzt technische Tiefe

**Inhalte:**
- Transformer-Architektur (nur Ueberblick — kein Deep Dive)
- Emergente Faehigkeiten und deren Implikationen fuer Qualitaetssicherung
- LLM-spezifische Risiken: Halluzination, Bias, Prompt Injection, Stochastizitaet
- Warum klassische ML-Evaluation nicht reicht → Motivation fuer spezielle Quality Gates
- RAG als Enterprise-Pattern: Architektur, Retrieval-Qualitaet als Gate-Kriterium

**Primaerquellen:**
- Bommasani et al. (2021) — Risiken und Capabilities
- Shankar et al. (2024) — LLM Evaluation Challenges
- Xu et al. (2025) [P998PMS3] — RAGOps Architektur
- Wei et al. (2022) — Emergent Abilities of LLMs
- Huang et al. (2023) — Survey Hallucination

**Negativ-Checklist:**
- ❌ Kein Transformer-Deep-Dive (Attention-Mechanismus etc.)
- ❌ Keine Trainings-Details (→ Out of Deployer-Scope)
- ❌ Kein Vergleich spezifischer Modelle (GPT-4 vs. LLaMA etc.)

---

## 2.3 Cloud-native: Fokus auf Plattformfaehigkeiten (~1,5 Seiten / ~450W)

**Funktion:** Cloud-native nicht als Infrastruktur-Lehrbuch, sondern als Enabler fuer GenAIOps.
**Bruecke von 2.2:** LLM-Risiken erfordern Plattform-Capabilities → welche?

**Inhalte:**
- Cloud-native Definition (CNCF) — Containerisierung, Orchestrierung, Microservices
- 4 Plattformfaehigkeiten als Enabler:
  - Identity & Access (Zero Trust)
  - Network (Service Mesh, API Gateway)
  - Observability (Metriken, Logs, Traces — speziell fuer LLM-Inferenz)
  - Policy Engine (OPA, admission control — Vorgriff auf 2.6)
- IaC und GitOps als Operationalisierungsprinzipien
- Warum Cloud-native fuer GenAIOps essentiell ist (vs. on-premise)

**Primaerquellen:**
- CNCF (2018) — Cloud-native Definition
- Pourmajidi et al. (2025) [2ZNT2H8W] — CNA Governance Reference Architecture
- Kratzke & Quint (2017) — Cloud-native Understanding
- Burns et al. (2016) — Borg, Omega, Kubernetes

**Negativ-Checklist:**
- ❌ Kein Kubernetes-Tutorial
- ❌ Keine Cloud-Provider-Vergleiche (Azure vs. AWS vs. GCP)
- ❌ Nur Faehigkeiten die direkt in Kap. 5 Architektur genutzt werden

---

## 2.4.1 Von MLOps zu LLMOps: Operationalisierung von KI-Systemen (~2 Seiten / ~600W)

**Funktion:** Evolution MLOps → LLMOps → GenAIOps zeigen. Begruenden warum neue Ops-Praktiken noetig.
**Bruecke von 2.3:** Cloud-native Plattform → jetzt die Ops-Praktiken die darauf laufen

**Inhalte:**
- MLOps: Definition, Kernprinzipien, Lifecycle (Kreuzberger et al., 2023)
- Grenzen von MLOps fuer LLMs (kein klassisches Training, Prompt-Engineering, RAG-Pipelines)
- LLMOps: Erweiterungen (Prompt Management, Embedding-Pipeline, RAG-Ops, Guardrails)
- GenAIOps als integrativer Begriff: LLMOps + RAGOps + AgentOps (Joshi, 2025; Cardoso)
- Taxonomie-Vergleich: MLOps vs. LLMOps vs. FMOps vs. GenAIOps
- CI/CD/CT fuer GenAI — was aendert sich gegenueber klassischem ML?

**Primaerquellen:**
- Kreuzberger et al. (2023) [QY49ZYXB] — MLOps Ueberblick
- Pahune & Akhtar (2025) [M9LISHKG] — MLOps → LLMOps Transition
- Tantithamthavorn et al. (2025) [C755FHJK] — MLOps, LLMOps, FMOps and Beyond
- Joshi (2025) [6RRBZAUF] — LLMOps, AgentOps, MLOps Review
- Xu et al. (2025) [P998PMS3] — RAGOps
- Mahr et al. (2024) — LLM Quality Assurance (Vergleichsanalyse vorhanden)

**Negativ-Checklist:**
- ❌ Keine Tool-Reviews (MLflow, Weights&Biases etc.)
- ❌ Keine Implementierungsdetails (→ Kap. 5)
- ❌ Keine vollstaendige Ops-Geschichte

---

## 2.4.2 Der EU AI Act: Regulatorischer Rahmen (~2 Seiten / ~600W)

**Funktion:** Regulatorische Grundlagen legen, die in Kap. 4 (Transformationsmethodik) operationalisiert werden.
**Bruecke von 2.4.1:** Ops-Praktiken brauchen Governance → warum? → EU AI Act

**Inhalte:**
- Regulatorischer Kontext: Verordnung 2024/1689, Inkrafttreten, Uebergangsfristen
- Risikoklassifizierung (4 Stufen, Fokus: High-Risk)
- Deployer-Pflichten (Art. 26) — Abgrenzung zu Provider (Art. 16), Art. 25 Scope-Trigger
- Anforderungen Art. 9-15 im Ueberblick (Detaillierung → Kap. 4.3-4.5)
- Technisch-organisatorische Implikationen: Was bedeutet Compliance fuer den Betrieb?
- Abgrenzung: Kein Rechtsgutachten — technisch-organisatorische Perspektive

**Primaerquellen:**
- EU AI Act (2024) — Verordnung 2024/1689 (Primaerquelle)
- Laux et al. (2024) — Trustworthy AI, Three Pillars
- Kelly et al. (2024) [P5CWR6XL / GSBRDTW5] — Compliance-Methodologie
- Burns et al. (2025) [2GGF93BE] — AI Governance / Dynamo Project
- Huwyler (2025) [UE5LVI97] — Unified Framework EU AI Act
- Smuha (2021) — Risk-based AI Regulation

**Negativ-Checklist:**
- ❌ Keine juristische Detailanalyse einzelner Artikel (→ Kap. 4.3)
- ❌ Keine Kontrollmechanismen (→ Kap. 4.4)
- ❌ Keine Human-Oversight-Tiefe (→ Kap. 4.5)
- ❌ Deployer-Scope beachten: keine Provider-Perspektive (Art. 16)

---

## 2.5 Quality Gates: Definition, Konzepte und Einordnung (~1,5 Seiten / ~450W)

**Funktion:** Quality-Gate-Konzept als Kernmechanismus der Arbeit fundieren.
**Bruecke von 2.4.2:** EU AI Act fordert Nachweise → Quality Gates als Kontrollpunkte

**Inhalte:**
- Quality Gate im Software Engineering: Definition, Historie (Stage-Gate Modell, Cooper 1990)
- Quality Gate in CI/CD: Automatisierte Pruefpunkte in Pipelines
- Abgrenzung: Quality Gate ≠ Milestone ≠ Review ≠ Approval
- Quality Gate fuer AI-Systeme: Erweiterungen (Modellevaluation, Datenqualitaet, Compliance)
- Elia et al. (2025) MQG4AI als naechstverwandtes Framework → Abgrenzung Demir (D_MQG4AI_PLACEMENT)
- Eigene Arbeitsdefinition: "automatisierter, evidenzbasierter Kontrollpunkt" (Critical Definition)

**Primaerquellen:**
- Cooper (1990/2008) — Stage-Gate Model
- Elia et al. (2025) [QRW95D4X / NSV9MZIA] — MQG4AI
- Mahr et al. (2024) — LLM QA Reference Architecture
- Humble & Farley (2010) — Continuous Delivery (Gates in Pipelines)
- Díaz-Rodríguez et al. (2023) [NWJFNALE] — Trustworthy AI Principles

**Negativ-Checklist:**
- ❌ Keine Gate-Spezifikation (→ Kap. 5.3)
- ❌ Keine Gate-IDs (G-PRE-01 etc.) — erst in Kap. 4.6 (D_GATE_IDS_LOCATION)
- ❌ Keine vollstaendige MQG4AI-Analyse (nur Positionierung + Abgrenzung)

---

## 2.6 Compliance-as-Code und Policy-as-Code (~1,5 Seiten / ~450W)

**Funktion:** Policy-as-Code als technischen Mechanismus fuer Compliance-Automatisierung einfuehren.
**Bruecke von 2.5:** Quality Gates brauchen pruefbare Policies → wie?

**Inhalte:**
- Policy-as-Code: Definition und Abgrenzung (Rego/OPA, Cedar, Sentinel)
- Compliance-as-Code: Erweiterung — Policies + Evidence + Audit Trail
- Beziehung zu IaC und GitOps (Versionierung, Auditierbarkeit)
- Reifegradmodell: Manuell → Semi-automatisiert → Vollautomatisiert
- Enterprise-Kontext: Warum PaC fuer regulierte GenAI-Systeme?
- Abgrenzung zu traditionellem GRC (Governance, Risk, Compliance)

**Primaerquellen:**
- Pourmajidi et al. (2025) [2ZNT2H8W] — XaC, End-to-End Governance
- Open Policy Agent Dokumentation — OPA/Rego Referenz
- Stigler (2020) — Policy-as-Code Concept
- HashiCorp Sentinel / AWS Cedar — als Beispiele (nicht detailliert)
- Burns et al. (2025) [2GGF93BE] — AI Governance Compliance Automation

**Negativ-Checklist:**
- ❌ Kein OPA/Rego-Tutorial (→ Kap. 5.4.2)
- ❌ Keine Pipeline-Integration (→ Kap. 5.4)
- ❌ Keine Tool-Vergleiche (OPA vs. Sentinel vs. Cedar → nur erwaehnen)

---

## 2.7 Synthese: Forschungsluecke und Handlungsbedarf (~2,5 Seiten / ~750W)

**Funktion:** Alle Straenge buendeln → Forschungsluecke identifizieren → Handlungsbedarf = Motivation fuer Kap. 4+5.
**Bruecke von 2.6:** Alle Konzepte eingefuehrt → jetzt: was fehlt in der Literatur?

**Inhalte:**
- Synthese der 6 Themenfelder (2.1-2.6) — Was ist Stand der Forschung?
- Identifikation der Forschungsluecke: "Keine integrierte Architektur die GenAIOps + Quality Gates + EU AI Act Compliance in einem Framework verbindet"
- Positionierung gegenueber Related Work:
  - Mahr et al. (2024): WAS, nicht WIE/WANN (Vergleichsanalyse vorhanden)
  - Pourmajidi et al. (2025): CNA Governance, aber nicht GenAI-spezifisch
  - Elia et al. (2025): Quality Gates fuer AI, aber nicht cloud-native/CI/CD-integriert
  - Kreuzberger et al. (2023): MLOps, nicht LLMOps/GenAIOps
  - Joshi (2025): Survey, kein Artefakt
- USP-Positionierung der eigenen Arbeit (→ USP_ANALYSE_EXPERTENBEWERTUNG.pdf)
- Ableitung des Handlungsbedarfs → direkte Bruecke zu RQ1/RQ2/RQ3

**Primaerquellen:**
- Alle in 2.1-2.6 zitierten Kernquellen (Rueckverweis)
- USP-Analyse (docs/positioning/)
- Vergleich_Demir_vs_Mahr.md (vorhanden)
- Analyse_Pourmajidi_und_Gesamtvergleich.md (vorhanden)

**Negativ-Checklist:**
- ❌ Keine Wiederholung der Grundlagen — nur Synthese und Luecke
- ❌ Kein Vorgriff auf die eigene Architektur (→ Kap. 5)
- ❌ Keine wertenden Urteile ohne Beleg

---

## Budget-Uebersicht

| Abschnitt | Seiten | Woerter | Quellen (geschaetzt) |
|-----------|--------|---------|---------------------|
| 2.1 | ~1,5 | ~450 | 5-6 |
| 2.2 | ~1,5 | ~450 | 4-5 |
| 2.3 | ~1,5 | ~450 | 3-4 |
| 2.4.1 | ~2,0 | ~600 | 5-6 |
| 2.4.2 | ~2,0 | ~600 | 5-6 |
| 2.5 | ~1,5 | ~450 | 4-5 |
| 2.6 | ~1,5 | ~450 | 4-5 |
| 2.7 | ~2,5 | ~750 | 6-8 (+ Rueckverweise) |
| **GESAMT** | **~14** | **~4.200** | **~40 unique** |

---

## Empfohlene Schreibreihenfolge

**Option A (sequenziell):** 2.1 → 2.2 → 2.3 → 2.4.1 → 2.4.2 → 2.5 → 2.6 → 2.7
- Vorteil: Natuerlicher Lesefluss, Bruecken ergeben sich organisch
- Nachteil: 2.7 Synthese erst am Ende, Positionierung erst spaet sichtbar

**Option B (thematische Klammern):**
1. 2.1 (Begriffe) → 2.2 (GenAI) → 2.4.1 (Ops-Evolution) = Technische Klammer
2. 2.3 (Cloud-native) → 2.6 (PaC) = Plattform-Klammer
3. 2.4.2 (EU AI Act) → 2.5 (Quality Gates) = Compliance-Klammer
4. 2.7 (Synthese) = Abschluss

**Empfehlung:** Option A (sequenziell) — einfacher fuer Bruecken-Konsistenz,
Prof. Prinz Stilregel "keine formalen Ueberleitungen" wird leichter eingehalten
wenn der natuerliche Argumentationsfluss stimmt.

---

## Offene Fragen (vor Schreiben klaeren)

1. **Budget-Verteilung:** Sind ~14 Seiten fuer Kap. 2 angemessen? (Gesamtbudget 60-80 S.)
2. **Tiefe 2.7:** Ausfuehrliche Gap-Analyse MIT Feature-Matrix (aus vorhandenen Vergleichsanalysen) oder kompakter Brueckenschlag?
3. **Quellen die fehlen:** Bommasani et al. (2021), Vaswani (2017), Lewis (2020), Wei (2022), Cooper (1990), Huang (2023) — in Zotero nicht gefunden, muessen manuell verifiziert werden
4. **Schreibreihenfolge:** Option A oder B?
