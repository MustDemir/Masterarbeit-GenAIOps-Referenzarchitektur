# Recherchebericht Kapitel 4 — Anforderungsanalyse (RQ1)

**Datum:** 2026-03-04
**Suchzeitraum:** 2023–2026
**Quellen:** Consensus API (200M+ Papers), Semantic Scholar, Wiley, ArXiv, ACM, SSRN
**Suchdurchläufe:** 12 Queries über 4 Tools (Consensus + Semantic Scholar)

---

## 1. Zusammenfassung

Die systematische Recherche identifizierte **19 relevante Quellen** (2023–2026), die die offenen Abschnitte 4.2–4.6 der Anforderungsanalyse fundieren können. Die wichtigsten Erkenntnisse:

- **Ein zentrales Review-Paper** (Ray, 2026) deckt Lifecycle-Governance, Policy-as-Code, TRiSM-Taxonomien und ModelOps ab — relevant für nahezu alle Abschnitte
- **Unified Control Framework** (Eisenberg et al., 2025) bietet 42 konkrete Controls mit Risk-Taxonomy und Regulatory Mapping — starker Kandidat für 4.6
- **Human Oversight** ist gut beforscht: Sterz et al. (2024, 43 Zitationen) + Enqvist (2023, 39 Zitationen) + Ooms et al. (2025) bilden konvergente Evidenzkette für Art. 14
- **Compliance-as-Code / Policy-as-Code** hat zunehmende Publikationsdichte, aber noch wenig AI-Act-spezifische Operationalisierung
- **Lücke:** Keine Publikation transformiert Art. 9–15 systematisch in einen vollständigen Requirements-Katalog mit Quality Gates — genau das ist der Beitrag deiner Arbeit

---

## 2. Paper-Übersicht nach Abschnitt

### 2.1 Abschnitt 4.3 — Transformationsmethodik (Norm → Requirement → Gate)

| # | Quelle | Jahr | Journal/Venue | Zitationen | DOI/Link | Kernbeitrag für Kap. 4.3 |
|---|--------|------|---------------|------------|----------|--------------------------|
| 1 | **Ray, P. P.** — TRiSM Frameworks Review | 2026 | Expert Systems, 43(3) | – | [10.1111/exsy.70213](https://doi.org/10.1111/exsy.70213) | Policy-as-Code Engines in CI/CD; Lifecycle Governance Controls; Pre-commit Hooks → Training Gates → Pre-Deployment Gates → Runtime Agents → Retirement Archives |
| 2 | **Sardana, Sethuraman & Kalyanasundaram** — Compliance-as-Code 2.0 | 2024 | JAIGS | 0 | [Consensus](https://consensus.app/papers/complianceascode-20-orchestrating-regulatory-sardana-sethuraman/f732c4b13d2156d9b838c669655cef04/) | NLP zur Interpretation regulatorischer Texte → executable Code; Agentic AI für Compliance-Orchestrierung; 74% Reduktion manueller Audits |
| 3 | **Rebbana, M.** — Automating Compliance with Policy-as-Code | 2025 | J Computer Science & Technology Studies | 0 | [Consensus](https://consensus.app/papers/automating-compliance-in-cloud-data-platforms-using-rebbana/b0c9e7b458375f14aade0f8d668dca94/) | PaC-Architektur: Policy Definition Languages, Enforcement Mechanisms, Attestation; 4-Phasen-Implementierung (Inventory → Engineering → Integration → Monitoring) |
| 4 | **Ravva, K.** — Automated Compliance Verification in MLOps Pipelines | 2025 | World J Advanced Research & Reviews | 0 | [Consensus](https://consensus.app/papers/automated-compliance-verification-for-ai-models-in-ravva/4f2c7baa394451a085acdf5f2c7f3498/) | Referenzarchitektur: Fairness/Explainability/Privacy/Robustness-Checks als mandatory Gates in CI/CD; Compliance als integraler Workflow-Bestandteil |
| 5 | **Gallina et al.** — Ontology for Process Compliance with Legislations | 2024 | J Software: Evolution & Process, 37(1) | – | [10.1002/smr.2728](https://doi.org/10.1002/smr.2728) | Ontologie zur Transformation von Legislation → Standards → interne Prozesse; Traceability über Argumentation Patterns; Divide-and-Conquer für Compliance-Komplexität |
| 6 | **Siddiki & Frantz** — Institutional Grammar 2.0 | 2023 | Regulation & Governance, 18(3), 674–687 | – | [10.1111/rego.12546](https://doi.org/10.1111/rego.12546) | Syntaktische + semantische Analyse von Regulatory Provisions; Systematische Extraktion von Akteuren, Handlungen, Kontexten aus Regulierungstext |
| 7 | **Damonte & Bazzan** — Rules as Data | 2024 | Regulation & Governance, 18(3), 657–673 | – | [10.1111/rego.12582](https://doi.org/10.1111/rego.12582) | Methodisches Framework: Legal Text → machine-readable Format; "Rules Retrieval" via NLP; 85% Accuracy bei shallow architectures + semantic parsing |

**Synthese 4.3:** Die Transformationsmethodik kann dreistufig fundiert werden: (1) Regulatorischer Text wird via Institutional Grammar / Ontologie-basierte Methoden in strukturierte Anforderungen überführt (Gallina; Siddiki & Frantz), (2) diese werden als Policy-as-Code kodifiziert (Ray; Rebbana), (3) und als mandatory Gates in CI/CD-Pipelines integriert (Ravva; Ray). Keine der Quellen macht dies spezifisch für den EU AI Act Art. 9–15 → Forschungslücke deiner Arbeit.

---

### 2.2 Abschnitt 4.6 — Requirements-Katalog (allgemein)

| # | Quelle | Jahr | Journal/Venue | Zitationen | DOI/Link | Kernbeitrag für Kap. 4.6 |
|---|--------|------|---------------|------------|----------|--------------------------|
| 8 | **Eisenberg, Gamboa & Sherman** — Unified Control Framework (UCF) | 2025 | ArXiv abs/2503.05937 | 1 | [Consensus](https://consensus.app/papers/the-unified-control-framework-establishing-a-common-eisenberg-gamboa/a35335388c6c5effbeba18c420cec687/) | **42 Controls** + Risk-Taxonomy + Policy Requirements aus Regulierungen; Validiert am Colorado AI Act; Reduktion von Governance-Duplizierung |
| 9 | **Nikiforova et al.** — Responsible AI Adoption Taxonomy | 2025 | ArXiv abs/2510.09634 | 0 | [Consensus](https://consensus.app/papers/responsible-ai-adoption-in-the-public-sector-a-datacentric-nikiforova-lnenicka/2492e2dcae3953678725afdaaba1a1ce/) | **13 Key Challenges** über 3 Dimensionen (technologisch, organisatorisch, environmental); Diagnostisches Tool für High-Risk AI Deployment |
| 10 | **Mentxaka et al.** — Trustworthy AI & Democracy: Dual Taxonomy | 2025 | ArXiv abs/2505.13565 | 0 | [Consensus](https://consensus.app/papers/aligning-trustworthy-ai-with-democracy-a-dual-taxonomy-of-mentxaka-rodríguez/72154299fcb95a96a5a68fb3a1c23df6/) | AIRD-Taxonomy (Risks) + AIPD-Taxonomy (Positive Contributions); 7 Trustworthy AI Requirements des HLEG als Basis; Mitigation Strategies aus EU-Frameworks |
| 1 | **Ray (2026)** — TRiSM Review *(siehe oben)* | 2026 | Expert Systems | – | [10.1111/exsy.70213](https://doi.org/10.1111/exsy.70213) | Drei alignierte Taxonomien: Trust Dimensions, Risk Categories, Security Controls; Toxizitäts-Taxonomie für GenAI |

**Synthese 4.6:** Das UCF (Eisenberg et al., 2025) ist der stärkste Vergleichskandidat — es bietet 42 Controls die Risiko und Compliance vereinen, validiert aber am Colorado AI Act, nicht am EU AI Act. Dein Requirements-Katalog R1–Rn kann als EU-AI-Act-spezifisches Pendant zum UCF positioniert werden, mit dem Zusatz von Lifecycle-Phasen-Zuordnung und Gate-Mapping.

---

### 2.3 Abschnitt 4.2 — Lifecycle-Modell

| # | Quelle | Jahr | Journal/Venue | Zitationen | DOI/Link | Kernbeitrag für Kap. 4.2 |
|---|--------|------|---------------|------------|----------|--------------------------|
| 1 | **Ray (2026)** — TRiSM Review | 2026 | Expert Systems | – | [10.1111/exsy.70213](https://doi.org/10.1111/exsy.70213) | ModelOps Lifecycle: Development → Deployment (Canary/Blue-Green) → Production (Monitoring) → Retirement; Policy-as-Code über alle Phasen |
| 11 | **Soyer et al.** — Adversarial Risk Analysis for AI Release | 2025 | Risk Analysis, 45(12), 4196–4212 | – | [10.1111/risa.17711](https://doi.org/10.1111/risa.17711) | Decision-Support-Framework für Release-Entscheidung (= Deployment Gate); Multi-Agent-Modell für Risiko-Abwägung |
| 12 | **Panda, S.** — Scalable AI Systems: MLOps & Governance | 2025 | (Book) | 1 | [Consensus](https://consensus.app/papers/scalable-artificial-intelligence-systems-cloudnative-panda/d83aa1950bb256c9a33422a6ce23f62f/) | MLOps Lifecycle Management; Governance-Integration über Cloud-Native + Edge-AI; Compliance & Fairness in Deployment |
| 13 | **Tripathi & Singh** — MLOps for AI: Tracking, Synthesizing, Monitoring | 2025 | IJRPS | 0 | [Consensus](https://consensus.app/papers/mlops-for-ai-tracking-synthesizing-and-monitoring-models-tripathi-singh/32f10b526d23522d8ecda0d486c11bde/) | Model Drift, Data Consistency, Version Control, Governance als Lifecycle-Challenges; Automatisierung von Development → Deployment → Monitoring |
| 14 | **Niazi & Basu Roy** — FDA Draft Guidance on AI | 2026 | J Chemistry, 2026(1) | – | [10.1155/joch/5202999](https://doi.org/10.1155/joch/5202999) | Adaptive AI Sandbox: 4-Phasen-Lifecycle mit Decision Points, Monitoring Mechanisms, Fail-Safe Triggers; Color-coded Gates für Human Intervention |

**Synthese 4.2:** Deine Dreiteilung (Pre-Deployment / Deployment / Operation) wird durch multiple Quellen gestützt. Ray (2026) liefert das technischste Modell (Development → Staging → Production → Retirement mit CI/CD-Integration). Das FDA-Sandbox-Modell (Niazi & Basu Roy, 2026) zeigt interessante Parallelen mit color-coded Gates und automatischer vs. menschlicher Intervention. Soyer et al. (2025) fundieren speziell den Deployment-Gate als formale Release-Entscheidung.

---

### 2.4 Abschnitt 4.4 — Kontrollmechanismen

| # | Quelle | Jahr | Journal/Venue | Zitationen | DOI/Link | Kernbeitrag für Kap. 4.4 |
|---|--------|------|---------------|------------|----------|--------------------------|
| 15 | **Sterz et al.** — Effectiveness in Human Oversight | 2024 | ACM FAccT 2024 | **43** | [Consensus](https://consensus.app/papers/on-the-quest-for-effectiveness-in-human-oversight-sterz-baum/ad0013396ec550a28c7202bd500b7023/) | 4 Bedingungen für effektive Human Oversight: (a) Causal Power, (b) Epistemic Access, (c) Self-Control, (d) Fitting Intentions; Analyse Art. 14 AI Act; Facilitators & Inhibitors |
| 16 | **Enqvist, L.** — Human Oversight in EU AI Act: What, When, By Whom? | 2023 | Law, Innovation & Technology, 15, 508–535 | **39** | [Consensus](https://consensus.app/papers/'-human-oversight-'-in-the-eu-artificial-intelligence-act-enqvist/c9fd9a3ad24555538b608226d657f4ed/) | Systematische Analyse Art. 14: What (Gegenstand), When (Zeitpunkt), By Whom (Akteur); Lücken und Implikationen; Provider-Vertrauen problematisiert |
| 17 | **Ooms et al.** — From Policy to Practice: Prototyping Art. 14 | 2025 | SSRN | 2 | [Consensus](https://consensus.app/papers/from-policy-to-practice-prototyping-the-eu-ai-acts-human-ooms-cools/0a52cee12020556bac179d31739dedf4/) | Prototypische Umsetzung der Human Oversight Requirements des AI Act |
| 18 | **Murikah, Nthenge & Musyoka** — Bias & Ethics in AI Auditing | 2024 | Scientific African | **64** | [Consensus](https://consensus.app/papers/bias-and-ethics-of-ai-systems-applied-in-auditing-a-murikah-nthenge/ff0ba4e0fe0a5d449db96bd399fcc0d7/) | 5 Bias-Quellen: Data Deficiencies, Demographic Homogeneity, Spurious Correlations, Improper Comparators, Cognitive Biases; Remedies: Causal Modeling, Representative Testing, Periodic Auditing |
| 19 | **Bai, Saradadevi & Preetha** — Transforming Software Testing with AI | 2025 | IJISRT | 0 | [Consensus](https://consensus.app/papers/transforming-software-testing-the-influence-of-bai-saradadevi/2349ade323fc599d862c842cbd18a55c/) | Metamorphic Testing, Differential Testing, Diversity-based Adequacy für GenAI; Oracle Problem bei GenAI; Human Oversight + Validation Techniques |

**Synthese 4.4:** Für Human Oversight (Art. 14) existiert eine starke Evidenzkette: Sterz et al. (2024) liefern theoretisches Framework (4 Bedingungen), Enqvist (2023) die juristische Analyse, Ooms et al. (2025) den Prototyping-Ansatz. Für automatisierte Kontrollen sind Murikah et al. (2024, 64 Zitationen) die meistzitierte Quelle zu Bias-Detection und AI-Auditing. Bai et al. (2025) adressieren speziell das GenAI-Testing-Problem (Oracle Problem, Metamorphic Testing).

---

## 3. Top-5 Empfehlungen (Lesepriorität)

| Prio | Quelle | Warum | Für Abschnitt |
|------|--------|-------|----------------|
| 🔴 1 | **Ray (2026)** — TRiSM Review | Umfassendstes Paper: Taxonomien, Lifecycle, Policy-as-Code, CI/CD-Gates — deckt 4.2, 4.3, 4.4, 4.6 ab | Alle |
| 🔴 2 | **Eisenberg et al. (2025)** — UCF | 42 Controls + Risk-Taxonomy = direkter Vergleichskandidat für deinen Requirements-Katalog | 4.6, 4.3 |
| 🔴 3 | **Sterz et al. (2024)** — Human Oversight | 43 Zitationen, 4 Effectiveness-Bedingungen, Art. 14 Analyse — Kernquelle für Art. 14 Kontrollmechanismus | 4.4 |
| 🟡 4 | **Gallina et al. (2024)** — Ontology for Compliance | Methodik: Legislation → Standards → Processes mit Traceability — stützt deine Transformationsmethodik | 4.3 |
| 🟡 5 | **Murikah et al. (2024)** — Bias & Ethics Auditing | 64 Zitationen, Systematic Review, 5 Bias-Quellen + Remedies — fundiert Bias-Gates | 4.4 |

---

## 4. Identifizierte Forschungslücke (= Beitrag deiner Arbeit)

Keine der identifizierten Publikationen leistet folgendes gleichzeitig:

1. **Systematische Transformation** aller relevanten AI-Act-Artikel (Art. 9–15) in technische Requirements
2. **Lifecycle-Phase-Zuordnung** (Pre-Deployment / Deployment / Operation) für jedes Requirement
3. **Quality-Gate-Mapping** mit automatisierten Checks (Policy-as-Code)
4. **Deployer-Perspektive** als architektonischen Scope (statt Provider)
5. **Traceability** RQ → R → DP → Gate als durchgängige Kette

Das **UCF** (Eisenberg et al., 2025) kommt am nächsten, validiert aber am Colorado AI Act und bietet keine Lifecycle-Phasen oder CI/CD-Gate-Architektur. **Ray (2026)** beschreibt die technische Infrastruktur (Policy-as-Code, ModelOps), aber ohne regulatorischen Mapping-Prozess.

→ Deine Arbeit schließt genau diese Lücke.

---

## 5. Suchprotokoll

| # | Query | Tool | Ergebnisse |
|---|-------|------|------------|
| 1 | "regulatory requirements operationalization AI systems policy-as-code compliance-as-code" | Consensus | 20 |
| 2 | "AI governance requirements taxonomy catalog framework high-risk AI" | Consensus | 20 |
| 3 | "EU AI Act regulatory requirements → technical requirements + quality gates" | Semantic Scholar | 15 |
| 4 | "Requirements catalogs or taxonomies for AI compliance and governance" | Semantic Scholar | 15 |
| 5 | "AI system lifecycle model phases deployment monitoring governance MLOps" | Consensus | 20 |
| 6 | "automated testing GenAI systems bias fairness robustness continuous monitoring" | Consensus | 20 |
| 7 | "AI governance lifecycle pre-deployment deployment post-deployment compliance checkpoints" | Semantic Scholar | 15 |
| 8 | "automated control mechanisms quality gates testing monitoring human oversight GenAI" | Semantic Scholar | 15 |
| 9 | "RegOps regulatory operations CI/CD pipeline AI compliance automation" | Consensus | 20 |
| 10 | "human oversight mechanisms Article 14 EU AI Act technical implementation" | Consensus | 20 |
| 11 | "regulatory compliance AI systems CI/CD pipelines automated policy checks quality gates" | Semantic Scholar | 10 |
| 12 | "transforming legal norms regulatory text machine-readable requirements software systems" | Semantic Scholar | 10 |

**Gesamt: 12 Queries, ~200 Papers gescreent, 19 als relevant identifiziert.**

---

## 6. Hinweise zur Verwendung

- ⚠ **Journal-Qualität prüfen:** Einige Quellen (JAIGS, IJISRT, JCST) sind nicht in etablierten Indices (Scopus/WoS). Nur als ergänzende Evidenz verwenden, nie als alleinige Quelle.
- ✅ **Hochwertige Quellen:** Ray (2026, Expert Systems/Wiley), Sterz et al. (2024, ACM FAccT), Enqvist (2023, Law Innovation & Technology), Murikah et al. (2024, Scientific African), Soyer et al. (2025, Risk Analysis/Wiley), Gallina et al. (2024, J Software Evolution & Process/Wiley) — alle in etablierten Journals.
- ⚠ **ArXiv-Papers** (Eisenberg et al., Nikiforova et al., Mentxaka et al.) sind Preprints — Peer-Review-Status beachten.
- 💡 **Konvergenz-Strategie:** Wie bei Jonnala et al. — nie als alleinige Evidenz, sondern immer in Triangulation mit Primärquellen (Normtext) und etablierten Publikationen.
