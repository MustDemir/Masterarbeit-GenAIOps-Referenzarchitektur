# Elicit Systematic Review — Kapitel 2: Echte Suchergebnisse

> **Datum:** 2026-03-07 | **Tool:** Elicit API (elicit_search_papers) | **Status:** VERIFIZIERT ✅
> **Zweck:** Dokumentation aller 6 Elicit-Searches für Kap. 2 Sektionen

---

## Legende

- 🟢 **MATCH** = Treffer bestätigt Quelle aus INHALTSPLAN (bereits geplant)
- 🔵 **NEU-RELEVANT** = Elicit-Fund, relevant für Sektion, noch nicht in INHALTSPLAN
- ⚪ **OFF-SCOPE** = Treffer thematisch zu weit weg vom Thesis-Scope

---

## Search 1: Sektion 2.1 — Begriffsabgrenzung + 2.2 GenAI/LLMs

**Query:** `"foundation models generative AI definition taxonomy classification"`
**Filter:** minYear=2021, maxResults=10

### Top-Treffer

| # | Titel | Autoren | Jahr | Cit. | Status |
|---|-------|---------|------|------|--------|
| 1 | A Taxonomy of Foundation Model based Systems through the Lens of Software Architecture | Lu, Zhu, Xu et al. | 2023 | 18 | 🔵 NEU-RELEVANT |
| 2 | Generative AI and Foundation Models (Overview) | Narapareddy | 2025 | 2 | ⚪ OFF-SCOPE |
| 3 | A Taxonomy of GenAI in HEOR (ISPOR) | Fleurence et al. | 2024 | 3 | ⚪ OFF-SCOPE (Healthcare) |
| 4 | Foundation Models for Time Series | Kottapalli et al. | 2025 | 12 | ⚪ OFF-SCOPE (Time Series) |
| 5–10 | Domain-spez. (Radiology, Pathology, Autonomous Driving) | diverse | 2023–2025 | 0–104 | ⚪ OFF-SCOPE |

### Bewertung für 2.1
**Lu et al. (2023)** ist ein starker Fund: Taxonomie von FM-basierten Systemen aus Software-Architektur-Perspektive, 18 Zitationen, CAIN 2024. Passt perfekt zur Systemkontext-Definition. Die klassischen Referenzen (Bommasani 2021, Vaswani 2017) tauchen NICHT auf, weil sie vor 2021 bzw. zu grundlegend für Elicit's Ranking sind → **bleiben als Zotero-Lücke bestehen**.

---

## Search 2: Sektion 2.2 — LLM-Risiken (Halluzination, Bias, Evaluation)

**Query:** `"large language model hallucination bias evaluation challenges risks"`
**Filter:** minYear=2022, maxResults=10

### Top-Treffer

| # | Titel | Autoren | Jahr | Cit. | Status |
|---|-------|---------|------|------|--------|
| 1 | **Siren's Song in the AI Ocean: A Survey on Hallucination in LLMs** | Zhang, Li, Cui et al. | 2023 | **878** | 🔵 NEU-RELEVANT ⭐ |
| 2 | HaluEval: A Large-Scale Hallucination Evaluation Benchmark | Li, Cheng, Zhao et al. | 2023 | 378 | ⚪ OFF-SCOPE (Benchmark) |
| 3 | Evaluation and Analysis of Hallucination in Large VLMs | Wang et al. | 2023 | 95 | ⚪ OFF-SCOPE (Vision) |
| 4 | Towards trustworthy LLMs: debiasing and dehallucinating | Lin et al. | 2024 | 87 | 🔵 NEU-RELEVANT |
| 5 | Hallucinations in LLMs: Challenges in Mitigation, Trust | Karne et al. | 2025 | 2 | ⚪ OFF-SCOPE |
| 6–10 | Domain-spez. (Education, Medical, Vision) | diverse | 2023–2026 | 0–13 | ⚪ OFF-SCOPE |

### Bewertung für 2.2
**Zhang et al. (2023) "Siren's Song"** mit 878 Zitationen ist DER Hallucination-Survey. Deutlich stärker als Huang et al. (2023) aus dem INHALTSPLAN. **Empfehlung:** Als primäre Halluzinationsquelle verwenden ODER neben Huang als zweite Referenz. **Lin et al. (2024)** verbindet Debiasing + Dehallucinating — guter Supplement für die Trustworthiness-Bridge zu 2.5.

---

## Search 3: Sektion 2.3 — Cloud-native + AI/ML Plattform

**Query:** `"cloud-native platform AI machine learning Kubernetes infrastructure"`
**Filter:** minYear=2020, maxResults=10

### Top-Treffer

| # | Titel | Autoren | Jahr | Cit. | Status |
|---|-------|---------|------|------|--------|
| 1 | Building AI-Driven Cloud-Native Applications with K8s | Naayini | 2025 | 8 | 🔵 NEU-RELEVANT |
| 2 | **Designing Cloud-Native Reference Architectures for Enterprise-Scale AI/ML** | Pashikanti | 2025 | 0 | 🔵 NEU-RELEVANT ⭐ |
| 3 | ML model development in Kubeflow Cloud-Native Systems | Bershchanskyi, Stepanov | 2025 | 2 | ⚪ OFF-SCOPE (Kubeflow-spezifisch) |
| 4 | Cloud-native technologies AI-enhanced observability | Mohammed | 2025 | 1 | ⚪ OFF-SCOPE (Observability) |
| 5 | Understanding cloud-native AI: scalable platform architecture | Goyal | 2025 | 0 | 🔵 NEU-RELEVANT |
| 6–10 | K8s Operations, AI Platform INFN, etc. | diverse | 2020–2025 | 0–3 | ⚪ OFF-SCOPE |

### Bewertung für 2.3
**Pashikanti (2025)** ist ein Volltreffer: "Cloud-Native Reference Architectures for Enterprise-Scale AI/ML Platforms" — beschreibt genau das, was unsere Arbeit im Kap. 5 macht, nur ohne Quality Gates und EU AI Act. Perfekt für Related-Work-Abgrenzung in 2.7! **Naayini (2025)** bestätigt den vorherigen Fund (Kubeflow, MLflow, Argo auf K8s). Die Basisquellen CNCF (2018), Kratzke (2017), Burns (2016) fehlen auch hier → **Zotero-Import bleibt Pflicht**.

---

## Search 4: Sektion 2.5 — Quality Gates

**Query:** `"quality gates software engineering stage-gate continuous delivery AI systems"`
**Filter:** minYear=2018, maxResults=10

### Top-Treffer

| # | Titel | Autoren | Jahr | Cit. | Status |
|---|-------|---------|------|------|--------|
| 1 | AI‐Augmented SE: Revolutionizing or Challenging Software Quality? | Ramos, Dean, McGregor | 2024 | 1 | 🔵 NEU-RELEVANT |
| 2 | **Building Resilient CI/CD Pipelines Using Quality Gates** | Kothokatta | 2025 | 0 | 🔵 NEU-RELEVANT ⭐ |
| 3 | An AI-Augmented Framework for Continuous Quality in CI/CD | Perla | 2025 | 0 | 🔵 NEU-RELEVANT |
| 4 | Agentic AI-Driven Quality Engineering | Singireddy et al. | 2026 | 0 | ⚪ OFF-SCOPE (zu neu) |
| 5 | AI-Enhanced Platform Engineering: CI/CD Intelligent Automation | Kodithyala | 2025 | 0 | ⚪ OFF-SCOPE |
| 6 | Automated SQA Using CI/CD Tools (FQS Model) | Wakhare, Jaybhaye | 2026 | 0 | 🔵 NEU-RELEVANT |
| 7–10 | Security Gates, Mathematical Models, etc. | diverse | 2024–2025 | 0–1 | ⚪ OFF-SCOPE |

### Bewertung für 2.5
**Kothokatta (2025)** ist der stärkste Fund: beschreibt Quality Gates in CI/CD-Pipelines mit SonarQube, Trivy, K8s Auditing — 74% weniger Production Incidents. **Perla (2025)** verbindet AI mit Quality Gates (predictive risk, self-healing). **Wakhare & Jaybhaye (2026)** formalisiert einen "Final Quality Score" — interessant für unsere Gate-Logik. **ABER:** Cooper (1990) und Humble/Farley (2010) erscheinen NICHT — sind zu alt/grundlegend für Elicit → **Zotero-Import zwingend**.

---

## Search 5: Sektion 2.6 — Policy-as-Code / Compliance-as-Code

**Query:** `"policy-as-code compliance-as-code open policy agent infrastructure governance automation"`
**Filter:** minYear=2019, maxResults=10

### Top-Treffer

| # | Titel | Autoren | Jahr | Cit. | Status |
|---|-------|---------|------|------|--------|
| 1 | **Policy as Code: A paradigm shift in infrastructure security** | Krisshnan, Vijayaraghavan | 2025 | 0 | 🔵 NEU-RELEVANT |
| 2 | Policy-Driven Infrastructure Automation: IaC + PaC Framework | Alugunuri | 2022 | 0 | 🔵 NEU-RELEVANT |
| 3 | **Compliance-as-Code: Automating Governance in Financial/Healthcare Clouds** | Mohammed | 2025 | 0 | 🔵 NEU-RELEVANT ⭐ |
| 4 | Automating Trust at Scale: IaC for Secure AI Environments | Eleweke | 2025 | 0 | 🔵 NEU-RELEVANT |
| 5 | **ARPaCCino: Agentic-RAG for Policy as Code Compliance** | Romeo et al. | 2025 | 2 | 🔵 NEU-RELEVANT ⭐ |
| 6 | Optimizing Cloud-Native SDLC through PaC + Intelligent Compliance | Gupta | 2025 | 0 | 🔵 NEU-RELEVANT |
| 7 | **A Secure Framework for Continuous Compliance (CaC+PaC)** | Yanagawa et al. | 2024 | 1 | 🔵 NEU-RELEVANT ⭐ |
| 8 | DevSecOps Policy-as-Code Model for Lakehouse Environments | Okare et al. | 2024 | 0 | ⚪ OFF-SCOPE (Lakehouse) |
| 9 | Automating Compliance in Cloud Data Platforms Using PaC | Rebbana | 2025 | 0 | ⚪ OFF-SCOPE |
| 10 | Automation Frameworks for Regulated Biomedical Infrastructures | Raju, Mudunuri | 2025 | 0 | ⚪ OFF-SCOPE (Biomedical) |

### Bewertung für 2.6
**Stärkste Sektion bei Elicit!** Viele direkt relevante Treffer:
- **Yanagawa et al. (2024)** IEEE CLOUD: GitOps-basiertes CaC+PaC Framework mit Traceability — sehr nah an unserem Approach
- **Romeo et al. (2025)** ARPaCCino: LLM+RAG für automatische Rego-Policy-Generierung — innovativer Supplement
- **Mohammed (2025)**: CaC in regulierten Clouds (HIPAA, PCI-DSS, NIST) mit OPA/Sentinel
- **Eleweke (2025)**: IaC für sichere AI-Umgebungen mit Policy-as-Code (NIST, FedRAMP)

---

## Search 6: Sektion 2.4.2 — EU AI Act

**Query:** `"EU AI Act compliance risk classification high-risk artificial intelligence regulation"`
**Filter:** minYear=2021, maxResults=10

### Top-Treffer

| # | Titel | Autoren | Jahr | Cit. | Status |
|---|-------|---------|------|------|--------|
| 1 | To Be High-Risk, or Not To Be (VAIR Ontology) | Golpayegani, Pandit, Lewis | 2023 | 42 | 🔵 NEU-RELEVANT |
| 2 | AIRO: Ontology for AI Risks Based on EU AI Act + ISO 31000 | Golpayegani, Pandit, Lewis | 2022 | 34 | 🔵 NEU-RELEVANT |
| 3 | **Navigating the EU AI Act** | Wagner, Borg, Runeson | 2024 | 15 | 🔵 NEU-RELEVANT ⭐ |
| 4 | **Navigating EU AI Act: Methodology for Safety-critical Products** | Kelly, Zafar et al. | 2024 | 18 | 🟢 MATCH [P5CWR6XL] |
| 5 | Privacy-Preserving AI Approach for Healthcare under EU AI Act | Kalodanis et al. | 2025 | 11 | ⚪ OFF-SCOPE (Healthcare) |
| 6 | **AI Regulates AI: Artifact for Automated Risk Assessment (DSR!)** | Kott, Rössler et al. | 2025 | 0 | 🔵 NEU-RELEVANT ⭐ |
| 7 | From Regulation to Implementation: EU AI Act in Oil & Gas | Dzhusupova et al. | 2025 | 0 | 🔵 NEU-RELEVANT |
| 8 | Risk, Reasonableness and Residual Harm under EU AI Act | Teichmann | 2026 | 0 | ⚪ OFF-SCOPE (Rechtstheorie) |
| 9 | High-Risk AI Systems (Personality Rights) | Matefi | 2025 | 0 | ⚪ OFF-SCOPE |
| 10 | Developers Alliance Position on AI Act | — | 2021 | 1 | ⚪ OFF-SCOPE |

### Bewertung für 2.4.2
**Wagner, Borg, Runeson (2024)** in IEEE Software: praxisnaher Überblick über AI Act Key Requirements — perfekt als Ergänzung zu Laux et al. **Kott et al. (2025)** nutzt DSR für automatisierte Risikoklassifizierung unter dem AI Act — 88% Accuracy! Methodisch verwandt mit unserer Arbeit. **Dzhusupova et al. (2025)** zeigt MLOps-Workflow-Anpassung für AI Act Compliance — direkte Parallele zu Kap. 4.3.

---

## Gesamtbilanz der Elicit-Suche (VERIFIZIERT)

### Quellenpool-Status nach Elicit

| Kategorie | Anzahl | Details |
|-----------|--------|---------|
| 🟢 MATCH (bestätigt INHALTSPLAN) | 1 | Kelly et al. (2024) |
| 🔵 NEU-RELEVANT (Elicit-Funde) | ~20 | Neue Paper für Kap. 2 |
| ⚪ OFF-SCOPE | ~39 | Domain-spezifisch oder zu weit |

### Top-10 Elicit-Funde (Empfehlung: In Zotero importieren)

| # | Paper | Sektion | Cit. | Begründung |
|---|-------|---------|------|-----------|
| 1 | Zhang et al. (2023) "Siren's Song" — Hallucination Survey | 2.2 | 878 | DER Survey zu LLM-Halluzinationen |
| 2 | Golpayegani et al. (2023) "To Be High-Risk" — VAIR | 2.4.2 | 42 | Ontologie für AI-Risikoklassifizierung |
| 3 | Golpayegani et al. (2022) AIRO — AI Risk Ontology | 2.4.2 | 34 | ISO 31000 + AI Act Risiko-Ontologie |
| 4 | Lu et al. (2023) FM Taxonomy (Software Architecture) | 2.1 | 18 | Taxonomie FM-basierter Systeme |
| 5 | Kelly et al. (2024) EU AI Act Methodology | 2.4.2 | 18 | Bereits in INHALTSPLAN ✅ |
| 6 | Wagner et al. (2024) Navigating EU AI Act (IEEE Software) | 2.4.2 | 15 | Praxisnaher AI Act Überblick |
| 7 | Yanagawa et al. (2024) CaC+PaC Framework (IEEE CLOUD) | 2.6 | 1 | GitOps CaC+PaC mit Traceability |
| 8 | Romeo et al. (2025) ARPaCCino — LLM+RAG für PaC | 2.6 | 2 | Innovative PaC-Automatisierung |
| 9 | Pashikanti (2025) Cloud-Native Ref.Arch. für AI/ML | 2.3/2.7 | 0 | Related Work: Ref.Arch. ohne QG |
| 10 | Kott et al. (2025) AI Regulates AI (DSR!) | 2.4.2/2.7 | 0 | DSR + AI Act Risk Assessment |

### Bestätigte Zotero-Lücken (Elicit kann diese NICHT liefern)

Die folgenden 13 Standardwerke sind zu grundlegend/alt für Elicit's Ranking — **manueller Zotero-Import bleibt Pflicht:**

1. Bommasani et al. (2021) — Foundation Models
2. Vaswani et al. (2017) — Attention Is All You Need
3. Lewis et al. (2020) — RAG Paper
4. Wei et al. (2022) — Emergent Abilities
5. Huang et al. (2023) — Hallucination Survey
6. Shankar et al. (2024) — LLM Evaluation Challenges
7. CNCF (2018) — Cloud-native Definition
8. Kratzke & Quint (2017) — Understanding CNA
9. Burns et al. (2016) — Borg, Omega, K8s
10. Cooper (1990/2008) — Stage-Gate Model
11. Humble & Farley (2010) — Continuous Delivery
12. Stigler (2020) — Policy-as-Code
13. Smuha (2021) — AI Regulation

### Kernbefund

Die Elicit-Suche liefert **20 neue relevante Paper** die den INHALTSPLAN ergänzen, ABER die Kernquellen (Standardwerke) sind zu grundlegend für Elicit's Ranking. **Strategie:**
- **Standardwerke** (13 Stück): Manuell in Zotero importieren
- **Top-5 Elicit-Funde**: Zhang (2023), Golpayegani (2022/2023), Lu (2023), Wagner (2024) als Supplements importieren
- **Related-Work-Schatz**: Pashikanti (2025) + Kott (2025) für Sektion 2.7 nutzen
