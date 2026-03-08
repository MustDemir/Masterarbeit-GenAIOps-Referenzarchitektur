# Evidenzbasierte Bewertung der SSOT-Cluster für Kapitel 2

> **Stand:** 2026-03-08 | **Methode:** Abstract-/Inhaltslektüre aller 82 PDFs (PyPDF2, erste 2 Seiten)
> **Basis:** INHALTSPLAN_KAP2.md (SOLL) + 00_ssot_mapping.csv (IST-Farben) + Disk-Inhalte (IST-Dateien)
> **Bewertungskriterien:** (1) Cluster-Zuordnung korrekt? (2) Relevanzfarbe angemessen? (3) Fehlzuordnungen?

---

## Legende

| Farbe | Bedeutung | Thesis-Funktion |
|-------|-----------|-----------------|
| 🔴 ROT | Core — wird direkt zitiert/analysiert | Primärquelle für Argumentation |
| 🟠 ORANGE | High — stützt zentrale Argumente | Sekundärquelle, Vergleich, Kontext |
| 🟡 GELB | Medium — ergänzender Kontext | Breitenabdeckung, Surveys |
| 🔵 BLAU | Context — Hintergrund, optional | Nur bei Bedarf referenziert |

**Bewertungssymbole:**
- ✅ Cluster + Farbe korrekt
- ⚠️ Farbe sollte angepasst werden
- ❌ Cluster-Fehlzuordnung (Umzug empfohlen)
- 🔄 Duplikat
- 🗑️ Entfernen (nicht akademisch / off-scope)

---

## 1. Cluster 02_01 — Begriffsabgrenzung und Systemkontext (1 PDF auf Disk, 0 in CSV)

**SOLL (INHALTSPLAN):** Definitionen von LLM, GenAI-System, RAG, LLMOps/GenAIOps, Quality Gate, Policy-as-Code. Primärquellen: Bommasani (2021), Vaswani (2017), Lewis (2020), Kreuzberger (2023), Xu (2025), Tantithamthavorn (2025).

**IST:** Nur 1 PDF physisch vorhanden, in CSV gar nicht als 02_01 geführt.

| # | Quelle | CSV-Farbe | Inhalt (Abstract) | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|-------------------|-------------|-----------|------------|
| 1 | Kratzke & Quint (2017) | (nur in 02_03) | Systematic Mapping Study zu Cloud-Native Applications. Definiert Cloud-Native-Begriffe, nicht GenAI/LLM-Begriffe. | ❌ | — | **Gehört in 02_03** (Cloud-Native). Nicht in 02_01 — hat keine LLM/GenAI-Definitionen. Physische Kopie in 02_01 entfernen. |

**Cluster-Fazit 02_01:** Der Cluster ist de facto **leer**. Die im INHALTSPLAN genannten Kernquellen (Bommasani, Vaswani, Lewis, Wei) fehlen komplett im SSOT. Das ist kein Clustering-Fehler, sondern ein **Beschaffungsproblem** — diese Quellen müssen noch in Zotero importiert und dem SSOT hinzugefügt werden.

**Handlungsbedarf:** 🔴 KRITISCH — 6 Primärquellen fehlen (Bommasani, Vaswani, Lewis, Kreuzberger→Kopie aus 02_04_01, Xu→Kopie aus 02_04_01, Tantithamthavorn→Kopie aus 02_04_01).

---

## 2. Cluster 02_02 — Generative KI und LLMs (15 PDFs auf Disk, 14 in CSV)

**SOLL:** Transformer-Überblick, emergente Fähigkeiten, LLM-Risiken (Halluzination, Bias, Prompt Injection), RAG als Enterprise-Pattern. Primärquellen: Bommasani, Shankar, Xu, Wei, Huang (Hallucination Survey).

| # | Quelle | CSV-Farbe | Inhalt (Abstract) | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|-------------------|-------------|-----------|------------|
| 1 | Bandi et al. (2023) | 🔵 BLAU | Review zu GenAI: Requirements, Models, I/O Formats, Evaluation. Breiter Überblick ohne Tiefe. | ✅ | ✅ | Korrekt als Kontext. |
| 2 | **Baqar et al. (2025)** | 🔴 ROT | AI-Augmented CI/CD Pipelines mit LLMs für autonome Deployment-Entscheidungen. Keywords: CI, CD, DevOps, DORA Metrics, Policy-as-Code, Progressive Delivery. | ❌ | ⚠️ | **Umzug → 02_06** (CaC/PaC). Paper behandelt CI/CD-Pipelines mit Policy-as-Code, nicht GenAI-Grundlagen. ROT→ORANGE in 02_06 (relevant für Pipeline-Kontext, aber kein Core-CaC-Paper). |
| 3 | De Luzi et al. (2025) | 🔵 BLAU | Engineering IS mit LLMs. Fokus auf Software-Engineering-Prozesse mit LLM-Unterstützung. | ✅ | ✅ | Korrekt. Peripherer Kontext. |
| 4 | **Feng et al. (2024)** | 🔵 BLAU | Normative Requirements Operationalization mit LLMs — übersetzt gesetzliche Anforderungen in prüfbare Kriterien mit LLM-Hilfe. | ❌ | ⚠️ | **Umzug → 02_04_02** (EU AI Act). Inhalt ist Compliance-Operationalisierung, nicht GenAI-Grundlagen. BLAU→GELB in 02_04_02. |
| 5 | Feuerriegel et al. (2024) | 🟡 GELB | "Generative AI" — Catchword-Paper, Business & IS Perspektive. Definiert GenAI-Begriff, Chancen/Risiken. | ✅ | ⚠️ | Cluster korrekt. **GELB→ORANGE** — definiert GenAI-Begriff aus IS-Perspektive, direkt relevant für 2.2 Begriffsschärfung. |
| 6 | **Guldimann et al. (2025)** | 🟠 ORANGE | COMPL-AI Framework: Technische Interpretation + LLM-Benchmarking-Suite für EU AI Act Compliance. | ❌ | ⚠️ | **Umzug → 02_04_02** (EU AI Act). Ist explizit ein EU-AI-Act-Compliance-Benchmarking-Tool. ORANGE→ROT in 02_04_02 (operationalisiert AI Act technisch). |
| 7 | Hagos et al. (2024) | 🔵 BLAU | Survey zu GenAI/LLMs: Status, Challenges, Perspectives. Breiter Überblick. | ✅ | ✅ | Korrekt als Kontext-Survey. |
| 8 | Harsha et al. (2024) | 🔵 BLAU | Survey on LLMs: Evolution, Applications, Future Frontiers. Breiter Überblick. | ✅ | ✅ | Korrekt. Redundant mit Hagos — eines reicht. |
| 9 | **Huang et al. (2025)** | 🔴 ROT | AAGATE: NIST AI RMF-aligned Governance Platform für Agentic AI auf Kubernetes. Fokus: Governance + Compliance. | ❌ | ⚠️ | **Umzug → 02_04_02** (EU AI Act / Governance). Ist eine Governance-Plattform, nicht GenAI-Grundlagen. ROT→ORANGE in 02_04_02 (NIST-Framework-Operationalisierung). |
| 10 | Russo (2024) | 🔵 BLAU | GenAI Adoption in Software Engineering. Fokus auf SE-Praktiken. | ✅ | ✅ | Korrekt als Kontext. |
| 11 | Sapkota et al. (2026) | 🔵 BLAU | AI Agents vs. Agentic AI — Konzeptuelle Taxonomie. | ✅ | ⚠️ | Cluster korrekt. **BLAU→GELB** — Taxonomie-Abgrenzung Agent vs. Agentic AI ist relevant für GenAIOps-Begriffsabgrenzung. |
| 12 | Sengar et al. (2024) | 🔵 BLAU | Systematic Review zu GenAI und Anwendungen. Breiter Überblick. | ✅ | ✅ | Korrekt. |
| 13 | **Unknown (2025)** | 🔵 BLAU | Amazon Bedrock Practical Guide. Kommerzieller Leitfaden, kein akademisches Paper. | ⚠️ | 🗑️ | **Entfernen oder nach 99_Context** verschieben. Nicht zitierfähig in akademischer Arbeit. |
| 14 | Wang et al. (2025) | (nur in 02_04_01 CSV) | LLM Full Stack Safety: Data, Training, Deployment. Umfassender Safety-Survey. | ⚠️ | — | Physisch in 02_02 UND 02_04_01. **Primär 02_02** (LLM-Risiken/Safety = Kernthema 2.2). Sekundär 02_04_01. CSV-Primary sollte 02_02 sein, ORANGE. |
| 15 | Zhao et al. (2026) | 🔵 BLAU | "Large Language Models" — Lehrbuch/Textbook. Breite Abdeckung. | ✅ | ✅ | Korrekt als Referenz-Textbook. |

**Cluster-Fazit 02_02:** 4 Fehlzuordnungen (Baqar→02_06, Feng→02_04_02, Guldimann→02_04_02, Huang→02_04_02), 1 nicht-akademische Quelle (Unknown/Amazon), 1 Duplikat-Problem (Wang). Nach Bereinigung bleiben **9 korrekte PDFs**. Für SOLL fehlen: Bommasani, Shankar, Wei, Huang (Hallucination Survey — nicht identisch mit Huang AAGATE!).

---

## 3. Cluster 02_03 — Cloud-Native Plattformfähigkeiten (3 PDFs)

**SOLL:** CNCF-Definition, Containerisierung, Orchestrierung, 4 Plattformfähigkeiten (Identity, Network, Observability, Policy Engine), IaC/GitOps. Primärquellen: CNCF (2018), Pourmajidi (2025), Kratzke & Quint (2017), Burns et al. (2016 — Borg/Omega/K8s).

| # | Quelle | CSV-Farbe | Inhalt (Abstract) | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|-------------------|-------------|-----------|------------|
| 1 | Johnston (2020) | 🟡 GELB | Kubernetes Platform Development — Buch zu K8s mit Data Management, IoT, Blockchain, ML. Praxisorientiert. | ✅ | ✅ | Korrekt. K8s-Plattformbuch als Kontext. |
| 2 | Kratzke (2023) | 🔵 BLAU | "Cloud Native Computing" — Kapitel/Buch zu Cloud-Native-Konzepten. | ✅ | ⚠️ | Cluster korrekt. **BLAU→GELB** — direkt relevante Cloud-Native-Definition für 2.3. |
| 3 | Kratzke & Quint (2017) | 🟡 GELB | Systematic Mapping Study zu Cloud-Native Applications. Definiert Begriffe, analysiert 95 Quellen. | ✅ | ⚠️ | Cluster korrekt. **GELB→ORANGE** — zentrale Definitionsquelle für Cloud-Native in 2.3. |

**Cluster-Fazit 02_03:** Alle 3 korrekt zugeordnet. Cluster ist dünn aber richtig. Fehlende SOLL-Quellen: CNCF (2018), Pourmajidi (2025), Burns et al. (2016). Kratzke & Quint doppelt auf Disk (auch in 02_01) — 02_01-Kopie entfernen.

---

## 4. Cluster 02_04_01 — Von MLOps zu LLMOps und GenAIOps (28 PDFs)

**SOLL:** MLOps-Definition, Grenzen für LLMs, LLMOps-Erweiterungen, GenAIOps als integrativer Begriff, Taxonomie-Vergleich, CI/CD/CT für GenAI. Primärquellen: Kreuzberger (2023), Pahune & Akhtar (2025), Tantithamthavorn (2025), Joshi (2025), Xu (2025), Mahr (2024).

| # | Quelle | CSV-Farbe | Inhalt | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|--------|-------------|-----------|------------|
| 1 | Ahamed Mohamed Ibrahim (2024) | 🟠 ORANGE | LLMOps für Enterprises. LLM-Lifecycle, Enterprise-Anforderungen. | ✅ | ✅ | Korrekt. |
| 2 | Billeter et al. (2024) | 🔴 ROT | MLOps als Enabler für Trustworthy AI. Verbindet MLOps mit Vertrauenswürdigkeit. | ✅ | ✅ | Korrekt. Brücke MLOps↔Trust. |
| 3 | Bodor et al. (2025) | 🟡 GELB | Web Scraping + Fine-Tuning + Data Enrichment in LLMOps-Kontext. Spezifischer Use Case. | ✅ | ✅ | Korrekt. Nischen-Use-Case. |
| 4 | Diaz-De-Arcaya et al. (2024) | 🟡 GELB | LLMOps: Definition, Challenges, Lifecycle Management. | ✅ | ⚠️ | Cluster korrekt. **GELB→ORANGE** — eine der wenigen expliziten LLMOps-Definitionen. |
| 5 | **Elicit (2026)** | 🔴 ROT | "Gaps in Generative AI Lifecycle Frameworks" — Meta-Report, kein Peer-Review. | ✅ | ⚠️ | Cluster inhaltlich passend. **ROT→GELB** — kein akademisches Paper, nicht als Primärquelle zitierfähig. Nützlich als Orientierung. |
| 6 | Gadiraju et al. (2025) | 🔴 ROT | DataOps meets LLMOps. Cloud-basierte AI Workflows von Data Ingestion bis Prompt Optimization. | ✅ | ✅ | Korrekt. Verbindet DataOps+LLMOps. |
| 7 | Garg et al. (2022) | 🟠 ORANGE | CI/CD für ML mit MLOps. Automatisierte ML-Deployment-Pipelines. | ✅ | ✅ | Korrekt. CI/CD-Fokus für ML. |
| 8 | **Huwyler (2025)** | 🔴 ROT | "Unified Framework for Operationalizing EU AI Act Compliance" — explizit EU-AI-Act-Compliance-Framework. | ❌ | ⚠️ | **Umzug → 02_04_02** (EU AI Act). Inhalt ist eindeutig Compliance-Operationalisierung. **ROT bleibt ROT** in 02_04_02 (Kernquelle für Compliance-Framework). |
| 9 | Joshi (2025) | 🔴 ROT | LLMOps, AgentOps, MLOps Review. Umfassender Vergleich aller Ops-Varianten. | ✅ | ✅ | Korrekt. **Kernquelle** für Taxonomie-Vergleich. |
| 10 | Kreuzberger et al. (2023) | 🟠 ORANGE | MLOps: Overview, Definition, Architecture. Systematische Literaturanalyse. | ✅ | ⚠️ | Cluster korrekt. **ORANGE→ROT** — DIE zentrale MLOps-Definitionsquelle, wird in INHALTSPLAN als Primärquelle gelistet. |
| 11 | Krishnamurthy & Neelanath (2025) | 🟡 GELB | Robust LLMOps Framework für Intelligent Automation. Praxis-Strategien. | ✅ | ✅ | Korrekt. |
| 12 | Kulkarni et al. (2023) | 🟡 GELB | "Applied GenAI" Buch — Kapitel zu LLMs für Enterprise und LLMOps. | ✅ | ✅ | Korrekt. Buch-Kontext. |
| 13 | Kumara et al. (2023) | 🟠 ORANGE | Architecting MLOps in the Cloud. Cloud-MLOps-Architektur. | ✅ | ✅ | Korrekt. Cloud+MLOps-Brücke. |
| 14 | Madicharla (2025) | 🟠 ORANGE | Evolution of LLMOps: Trends und Entwicklungen. | ✅ | ✅ | Korrekt. |
| 15 | Nellutla (2026) | 🔴 ROT | MLOps 2.0: Reference Architecture für CI/CD mit Always-On Data Quality Gates. | ✅ | ✅ | Korrekt. **Hochrelevant** — verbindet MLOps + Quality Gates + CI/CD. Brücke zu 02_05. |
| 16 | Pahune & Akhtar (2025) | 🔴 ROT | Transitioning from MLOps to LLMOps. Einzigartige Herausforderungen von LLMs. | ✅ | ✅ | Korrekt. **Kernquelle** für MLOps→LLMOps-Transition. |
| 17 | Pancini et al. (2025) | 🟡 GELB | MLOps Pipelines mit Data Quality. Kaggle Case Study. | ✅ | ✅ | Korrekt. Spezifischer Use Case. |
| 18 | Park et al. (2024) | 🟡 GELB | LlamaDuo: LLMOps Pipeline für LLM-Migration (Service→Local). | ✅ | ✅ | Korrekt. Spezifischer LLMOps-Use-Case. |
| 19 | Polyakovska (2025) | 🟠 ORANGE | Operational Excellence für LLMs. Praktisches Framework. | ✅ | ✅ | Korrekt. |
| 20 | Shan & Shan (2024) | 🔴 ROT | Enterprise LLMOps. Enterprise-Perspektive auf LLM-Operationalisierung. | ✅ | ✅ | Korrekt. Enterprise-Fokus passt zur Thesis. |
| 21 | **Sinan et al. (2025)** | 🔵 BLAU | DevSecOps: Security Controls Integration. Fokus auf Security in DevOps, nicht auf ML/LLM. | ❌ | ⚠️ | **Umzug → 02_06** (CaC/PaC). DevSecOps ist näher an Policy-as-Code/Compliance-Automation als an MLOps. BLAU→GELB in 02_06. |
| 22 | Sinha et al. (2024) | 🔴 ROT | LLMOps: Definitions, Framework, Best Practices. | ✅ | ✅ | Korrekt. Kernquelle für LLMOps-Definition. |
| 23 | **Srinivasa Rao Bittla (2025)** | 🟡 GELB | "AI-Driven Software Testing" — Buch über KI-gestütztes Testen, nicht spezifisch MLOps/LLMOps. | ⚠️ | ⚠️ | Grenzfall. Inhaltlich eher Testing als Ops. **GELB→BLAU** und ggf. nach 99_Context verschieben wenn nicht verwendet. |
| 24 | Stone et al. (2025) | 🔴 ROT | Navigating MLOps: Maturity, Lifecycle, Tools, Careers. Umfassender MLOps-Überblick. | ✅ | ✅ | Korrekt. |
| 25 | Tantithamthavorn et al. (2025) | 🔴 ROT | MLOps, LLMOps, FMOps and Beyond. Taxonomie-Vergleich. | ✅ | ✅ | Korrekt. **Kernquelle** für Taxonomie. |
| 26 | Testi et al. (2022) | 🟠 ORANGE | MLOps: Taxonomy and Methodology. Frühe MLOps-Taxonomie. | ✅ | ✅ | Korrekt. |
| 27 | **Wang et al. (2025)** | 🔵 BLAU | LLM Full Stack Safety. Duplikat — physisch auch in 02_02. | 🔄 | — | **Duplikat entfernen** aus 02_04_01. Primär-Cluster sollte 02_02 sein (LLM-Safety = GenAI-Risiken). Sekundär-Tag 02_04_01 setzen. |
| 28 | Xu et al. (2025) | 🔴 ROT | RAGOps: Operating and Managing RAG Pipelines. | ✅ | ✅ | Korrekt. **Kernquelle** für RAGOps-Konzept. |

**Cluster-Fazit 02_04_01:** 3 Fehlzuordnungen (Huwyler→02_04_02, Sinan→02_06, Wang→Duplikat/02_02). 2 Farb-Korrekturen nötig (Kreuzberger ORANGE→ROT, Elicit ROT→GELB, Diaz-De-Arcaya GELB→ORANGE). Insgesamt solider Cluster mit starken Kernquellen.

---

## 5. Cluster 02_04_02 — EU AI Act und technisch-organisatorische Anforderungen (27 PDFs)

**SOLL:** Verordnung 2024/1689, Risikoklassifizierung, Deployer-Pflichten Art. 26, Anforderungen Art. 9-15, technisch-organisatorische Implikationen. Primärquellen: EU AI Act, Laux (2024), Kelly (2024), Burns (2025), Huwyler (2025), Smuha (2021).

| # | Quelle | CSV-Farbe | Inhalt | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|--------|-------------|-----------|------------|
| 1 | Burns et al. (2025) | 🟡 GELB | AI Governance im Dynamo Project. EU AI Act Compliance in der Praxis. | ✅ | ⚠️ | Cluster korrekt. **GELB→ORANGE** — ist INHALTSPLAN-Primärquelle. |
| 2 | Corrêa & Mönig (2024) | 🟡 GELB | Katalog ethischer Anforderungen für AI-Zertifizierung. Breiter als EU AI Act. | ✅ | ✅ | Korrekt. Ergänzender Kontext. |
| 3+4 | **Diaz-Rodriguez / Díaz-Rodríguez (2023)** | 🟡 GELB | Trustworthy AI: Principles, Ethics, Key Requirements. **DUPLIKAT** — 2 Dateien, identisches Paper, Encoding-Unterschied im Dateinamen. | 🔄 | ✅ | **Eines entfernen.** Inhaltlich korrekt im Cluster. |
| 5 | EU Parlament & Rat (2024) | 🟡 GELB | Verordnung EU 2024/1689 — der EU AI Act selbst. | ✅ | ⚠️ | Cluster korrekt. **GELB→ROT** — ist DIE Primärquelle für den gesamten Abschnitt. |
| 6 | Fernández-Llorca et al. (2025) | 🟠 ORANGE | Terminologische Entscheidungen der EU-Policymaker. Interdisziplinäre Analyse. | ✅ | ✅ | Korrekt. Nützlich für Begriffsklärung. |
| 7 | Finch & Butt (2025) | 🟠 ORANGE | Gaps in AI-Compliant Governance. Systematic Review zu Governance-Lücken. | ✅ | ✅ | Korrekt. Identifiziert Governance-Gaps. |
| 8 | FLI (2024) | 🟠 ORANGE | High-Level Summary des AI Act. Praxis-Zusammenfassung. | ✅ | ✅ | Korrekt. Gute Übersichtsquelle. |
| 9 | FLI (2026) KMU-Leitfaden | 🟡 GELB | Leitfaden für kleine Unternehmen zum AI Act. | ✅ | ✅ | Korrekt. Praxis-Perspektive. |
| 10 | FLI (2026) Modifizierung | 🟡 GELB | Lehren aus der Praxis zur KI-Einstufung und Einhaltung. Gastbeitrag von Compliance-Experten. | ✅ | ✅ | Korrekt. Praxis-Erfahrungsbericht. |
| 11 | Golpayegani et al. (2024) | 🟡 GELB | AICat: AI Cataloguing for EU AI Act. Semantic Web Approach für EU-Datenbank. | ✅ | ✅ | Korrekt. Technische Umsetzung. |
| 12 | Governance/Eisenberg (2025) | 🟡 GELB | Unified Control Framework für Enterprise AI Governance. Credo AI. | ✅ | ⚠️ | Cluster korrekt. **GELB→ORANGE** — UCF ist direkt vergleichbar mit unserer Architektur (Governance + Risk + Compliance vereint). |
| 13 | Hernandez (2025) | 🟡 GELB | AI Act Knowledge Graph für High-Risk Compliance. | ✅ | ✅ | Korrekt. Technische Umsetzung. |
| 14 | Ho-Dac & Martinez (2024) | 🟡 GELB | Human Oversight und Technical Standardisation unter AI Act. **FRANZÖSISCH.** | ⚠️ | ⚠️ | Inhaltlich korrekt im Cluster. **Problem:** Text ist auf Französisch — Zitierbarkeit prüfen. GELB→BLAU (eingeschränkt nutzbar). |
| 15 | Hulok (2025) | 🟠 ORANGE | EU Model of AI Governance. Analyse des AI Act inkl. GenAI/GPAI. | ✅ | ✅ | Korrekt. Guter Governance-Überblick. |
| 16 | Jonnala et al. (2025) | 🟠 ORANGE | EU AI Act insufficient für GenAI-Risiken. Kritische Analyse. | ✅ | ✅ | Korrekt. Kritische Gegenstimme — wichtig für ausgewogene Darstellung. |
| 17 | **Kholkar & Ahuja (2025)** | 🟡 GELB | Policy-as-Prompt: AI Governance Rules als Guardrails für AI Agents. Regulatory ML Framework. | ⚠️ | ⚠️ | **Grenzfall.** Inhalt ist Policy→Guardrails→Runtime Monitoring. Passt sowohl zu 02_04_02 (Governance) als auch 02_06 (PaC). **Empfehlung: Belassen in 02_04_02, Sekundär-Tag 02_06.** GELB→ORANGE (innovative Policy-Operationalisierung). |
| 18 | Laux (2024) | 🟡 GELB | Institutionalised Distrust und Human Oversight unter AI Act. | ✅ | ⚠️ | Cluster korrekt. **GELB→ORANGE** — ist INHALTSPLAN-Primärquelle. |
| 19 | Li et al. (2021) | 🟡 GELB | Trustworthy AI: From Principles to Practices. Breiter Review. | ✅ | ✅ | Korrekt. Breiter Kontext. |
| 20 | NIST (2023) | 🟠 ORANGE | AI Risk Management Framework 1.0. US-Pendant zum EU-Ansatz. | ✅ | ✅ | Korrekt. Wichtig für Vergleich EU↔US. |
| 21 | Novelli et al. (2024) | 🟠 ORANGE | GenAI in EU Law: Liability, Privacy, IP, Cybersecurity. | ✅ | ✅ | Korrekt. Breit aber relevant. |
| 22 | Omran Almagrabi & Khan (2025) | 🟠 ORANGE | Secure AI Lifecycle Management mit GenAI Strategien. | ✅ | ⚠️ | Cluster korrekt. **ORANGE→GELB** — eher generisch, wenig EU-AI-Act-spezifisch. |
| 23 | Pistilli (2023) | 🟡 GELB | Ethics + Legal + Technical Documentation in ML (Hugging Face). | ✅ | ✅ | Korrekt. Ethik-Praxis-Perspektive. |
| 24 | Radanliev et al. (2025) | 🟠 ORANGE | GenAI Cybersecurity and Resilience. | ⚠️ | ⚠️ | Grenzfall. Cybersecurity-fokussiert, nur tangential zu AI Act. **ORANGE→GELB.** |
| 25 | Sarra (2024) | (fehlt in CSV!) | AI in Decision-making: Konsistenz-Test EU AI Act ↔ GDPR. | ✅ | — | Korrekt im Cluster. **Fehlt in CSV — nachtragen.** Empfehlung: GELB (ergänzende Rechtsanalyse). |
| 26 | Siddharth & Luo (2025) | 🟡 GELB | Data-Driven Innovation for Trustworthy AI. Design-Innovation-Perspektive. | ✅ | ✅ | Korrekt. |
| 27 | Taeihagh (2025) | 🟠 ORANGE | Governance of Generative AI. Special Issue Einleitung, Policy & Society. | ✅ | ✅ | Korrekt. Guter Governance-Überblick. |

**Cluster-Fazit 02_04_02:** Insgesamt **gut zusammengestellt**. 1 Duplikat (Díaz-Rodríguez 2x), 1 CSV-Lücke (Sarra), 1 Sprachproblem (Ho-Dac auf Französisch). Wichtigste Farbkorrekturen: EU AI Act Verordnung GELB→ROT (!), Burns GELB→ORANGE, Laux GELB→ORANGE. Fehlende SOLL-Quellen: Kelly (2024), Smuha (2021).

---

## 6. Cluster 02_05 — Quality Gates (2 PDFs)

**SOLL:** Stage-Gate-Modell (Cooper), Quality Gate in CI/CD, Abgrenzung zu Milestone/Review, QG für AI-Systeme, Elia MQG4AI, eigene Arbeitsdefinition. Primärquellen: Cooper (1990/2008), Elia (2025), Mahr (2024), Humble & Farley (2010), Díaz-Rodríguez (2023).

| # | Quelle | CSV-Farbe | Inhalt | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|--------|-------------|-----------|------------|
| 1 | Cooper (2008) | 🟡 GELB | Stage-Gate Idea-to-Launch Process. Update des Modells, NexGen Systems. Klassiker. | ✅ | ⚠️ | Cluster korrekt. **GELB→ROT** — ist DIE Grundlage für Quality-Gate-Konzept. INHALTSPLAN-Primärquelle. |
| 2 | Elia (2023) | 🟡 GELB | Quality Gates for Certifiable AI in Medicine. Methodology mit QG für ML-Zertifizierung. | ✅ | ⚠️ | Cluster korrekt. **GELB→ROT** — nächstverwandtes Framework (MQG4AI). INHALTSPLAN-Primärquelle. |

**Cluster-Fazit 02_05:** Beide Quellen korrekt, aber beide **zu niedrig eingestuft** (GELB statt ROT). Cluster ist **sehr dünn** — fehlende SOLL-Quellen: Mahr (2024), Humble & Farley (2010). Nellutla (2026) in 02_04_01 hat starke Brücke hierher (Quality Gates in CI/CD).

---

## 7. Cluster 02_06 — Compliance-as-Code und Policy-as-Code (6 PDFs auf Disk, 4 in CSV)

**SOLL:** PaC-Definition (Rego/OPA, Cedar, Sentinel), CaC-Erweiterung, IaC/GitOps-Beziehung, Reifegradmodell, Enterprise-Kontext. Primärquellen: Pourmajidi (2025), OPA-Docs, Stigler (2020), Burns (2025).

| # | Quelle | CSV-Farbe | Inhalt | Cluster OK? | Farbe OK? | Empfehlung |
|---|--------|-----------|--------|-------------|-----------|------------|
| 1 | Adetayo Adeyinka (2023) | 🔴 ROT | Automated Compliance Management in Hybrid Cloud. Policy-as-Code Approach. | ✅ | ✅ | Korrekt. PaC in Cloud-Kontext. |
| 2 | Alugunuri (2022) | 🔵 BLAU | Policy-Driven Infrastructure Automation für Microservices. IaC + PaC kombiniert. | ✅ | ⚠️ | Cluster korrekt. **BLAU→GELB** — verbindet IaC+PaC für Microservices, direkt relevant für 2.6. |
| 3 | Antiya (2020) | 🟠 ORANGE | Compliance as Code: Automating Compliance mit ISO 27001 + PCI DSS. | ✅ | ⚠️ | Cluster korrekt. **ORANGE→ROT** — eine der wenigen expliziten CaC-Definitionen mit Standardbezug. |
| 4 | **Baqar et al. (2025)** | (CSV: 02_02 ROT) | AI-Augmented CI/CD Pipelines mit Policy-as-Code. | ✅ (auf Disk) | ⚠️ | **CSV korrigieren:** Primary 02_06, nicht 02_02. ROT→ORANGE (relevant aber nicht Core-CaC). |
| 5 | Rebbana (2025) | 🟠 ORANGE | Automating Compliance in Cloud Data Platforms Using PaC. | ✅ | ✅ | Korrekt. |
| 6 | **Sovrano et al. (2025)** | (fehlt in CSV!) | AI Technologies in Drafting Technical Documentation für AI Act. LLM-gestützte Compliance-Dokumentation. | ✅ | — | Korrekt im Cluster. **Fehlt in CSV — nachtragen.** Empfehlung: ORANGE (Brücke AI Act↔Compliance Automation). |

**Cluster-Fazit 02_06:** Cluster inhaltlich korrekt. 2 CSV-Lücken (Baqar falsch zugeordnet, Sovrano fehlt). Farbkorrekturen: Antiya ORANGE→ROT, Alugunuri BLAU→GELB. Fehlende SOLL-Quellen: Pourmajidi (2025), Stigler (2020), OPA-Docs.

---

## Zusammenfassung: Fehlzuordnungen (Umzüge empfohlen)

| Quelle | IST-Cluster | SOLL-Cluster | Begründung |
|--------|-------------|--------------|------------|
| Baqar et al. (2025) | 02_02 (CSV) | **02_06** (Disk korrekt) | CI/CD + Policy-as-Code, nicht GenAI-Grundlagen |
| Feng et al. (2024) | 02_02 | **02_04_02** | Normative Requirements = Compliance-Operationalisierung |
| Guldimann et al. (2025) | 02_02 | **02_04_02** | EU AI Act Benchmarking-Suite |
| Huang et al. (2025) AAGATE | 02_02 | **02_04_02** | Governance-Plattform für AI RMF |
| Huwyler (2025) | 02_04_01 | **02_04_02** | EU AI Act Compliance Framework |
| Sinan et al. (2025) | 02_04_01 | **02_06** | DevSecOps = Security Policy Automation |
| Kratzke & Quint (2017) | 02_01 (Disk) | **02_03** (CSV korrekt) | Cloud-Native, nicht Begriffsabgrenzung. Kopie in 02_01 entfernen. |

## Zusammenfassung: Farbkorrekturen

| Quelle | Cluster | IST-Farbe | SOLL-Farbe | Begründung |
|--------|---------|-----------|------------|------------|
| EU AI Act Verordnung (2024) | 02_04_02 | 🟡 GELB | 🔴 **ROT** | Primärquelle des gesamten Abschnitts |
| Cooper (2008) | 02_05 | 🟡 GELB | 🔴 **ROT** | Stage-Gate-Grundlage, INHALTSPLAN-Primärquelle |
| Elia (2023) | 02_05 | 🟡 GELB | 🔴 **ROT** | MQG4AI, nächstverwandtes Framework |
| Kreuzberger et al. (2023) | 02_04_01 | 🟠 ORANGE | 🔴 **ROT** | Zentrale MLOps-Definition, INHALTSPLAN-Primärquelle |
| Antiya (2020) | 02_06 | 🟠 ORANGE | 🔴 **ROT** | Explizite CaC-Definition mit Standards |
| Burns et al. (2025) | 02_04_02 | 🟡 GELB | 🟠 **ORANGE** | INHALTSPLAN-Primärquelle |
| Laux (2024) | 02_04_02 | 🟡 GELB | 🟠 **ORANGE** | INHALTSPLAN-Primärquelle |
| Governance/UCF (2025) | 02_04_02 | 🟡 GELB | 🟠 **ORANGE** | Direkt vergleichbar mit eigener Architektur |
| Feuerriegel et al. (2024) | 02_02 | 🟡 GELB | 🟠 **ORANGE** | GenAI-Begriffsdefinition aus IS-Perspektive |
| Diaz-De-Arcaya (2024) | 02_04_01 | 🟡 GELB | 🟠 **ORANGE** | Explizite LLMOps-Definition |
| Kholkar & Ahuja (2025) | 02_04_02 | 🟡 GELB | 🟠 **ORANGE** | Policy-as-Prompt = innovative Operationalisierung |
| Kratzke & Quint (2017) | 02_03 | 🟡 GELB | 🟠 **ORANGE** | Zentrale Cloud-Native-Definitionsquelle |
| Kratzke (2023) | 02_03 | 🔵 BLAU | 🟡 **GELB** | Direkt relevante CN-Definition |
| Sapkota et al. (2026) | 02_02 | 🔵 BLAU | 🟡 **GELB** | Agent-Taxonomie relevant für GenAIOps |
| Alugunuri (2022) | 02_06 | 🔵 BLAU | 🟡 **GELB** | IaC+PaC für Microservices |
| Elicit (2026) | 02_04_01 | 🔴 ROT | 🟡 **GELB** | Kein Peer-Review, Meta-Report |
| Omran Almagrabi (2025) | 02_04_02 | 🟠 ORANGE | 🟡 **GELB** | Generisch, wenig AI-Act-spezifisch |
| Radanliev et al. (2025) | 02_04_02 | 🟠 ORANGE | 🟡 **GELB** | Cybersecurity-fokussiert, tangential |
| Ho-Dac & Martinez (2024) | 02_04_02 | 🟡 GELB | 🔵 **BLAU** | Französischsprachig, eingeschränkt nutzbar |
| Srinivasa Rao Bittla (2025) | 02_04_01 | 🟡 GELB | 🔵 **BLAU** | AI Testing-Buch, nicht spezifisch Ops |

## Zusammenfassung: Duplikate und Bereinigungen

| Problem | Dateien | Empfehlung |
|---------|---------|------------|
| Díaz-Rodríguez 2x in 02_04_02 | Diaz-Rodriguez... + Díaz-Rodríguez... | Encoding-Duplikat: eines entfernen |
| Wang 2x (02_02 + 02_04_01) | Identisches PDF in beiden Clustern | Primär 02_02, Sekundär-Tag 02_04_01, Kopie in 02_04_01 entfernen |
| Kratzke&Quint 2x (02_01 + 02_03) | Identisches PDF in beiden Clustern | Primär 02_03, Kopie in 02_01 entfernen |
| Unknown/Amazon Bedrock in 02_02 | Kommerzieller Guide | Nach 99_Context verschieben oder entfernen |
| Sarra fehlt in CSV | Auf Disk in 02_04_02 | In CSV nachtragen (GELB) |
| Sovrano fehlt in CSV | Auf Disk in 02_06 | In CSV nachtragen (ORANGE) |
| Baqar CSV-Zuordnung falsch | CSV: 02_02, Disk: auch 02_06 | CSV primary → 02_06 |

## Zusammenfassung: Fehlende SOLL-Quellen (aus INHALTSPLAN)

| Abschnitt | Fehlende Quelle | Priorität | Aktion |
|-----------|-----------------|-----------|--------|
| 2.1 | Bommasani et al. (2021) | 🔴 KRITISCH | Zotero-Import + SSOT |
| 2.1 | Vaswani et al. (2017) | 🔴 KRITISCH | Zotero-Import + SSOT |
| 2.1 | Lewis et al. (2020) RAG | 🔴 KRITISCH | Zotero-Import + SSOT |
| 2.2 | Shankar et al. (2024) | 🟠 HOCH | Zotero-Import + SSOT |
| 2.2 | Wei et al. (2022) | 🟠 HOCH | Zotero-Import + SSOT |
| 2.2 | Huang et al. (2023) Hallucination | 🟠 HOCH | Zotero-Import + SSOT |
| 2.3 | CNCF (2018) Definition | 🟠 HOCH | Zotero-Import + SSOT |
| 2.3 | Pourmajidi et al. (2025) | 🟠 HOCH | Zotero-Import + SSOT |
| 2.3 | Burns et al. (2016) Borg/K8s | 🟡 MITTEL | Zotero-Import + SSOT |
| 2.4.1 | Mahr et al. (2024) | 🟠 HOCH | Zotero-Import + SSOT |
| 2.4.2 | Kelly et al. (2024) | 🟠 HOCH | Zotero-Import + SSOT |
| 2.4.2 | Smuha (2021) | 🟡 MITTEL | Zotero-Import + SSOT |
| 2.5 | Mahr et al. (2024) | 🟠 HOCH | (gleich wie 2.4.1) |
| 2.5 | Humble & Farley (2010) | 🟡 MITTEL | Zotero-Import + SSOT |
| 2.6 | Pourmajidi et al. (2025) | 🟠 HOCH | (gleich wie 2.3) |
| 2.6 | Stigler (2020) | 🟡 MITTEL | Zotero-Import + SSOT |

---

## Gesamturteil

**Stärken des aktuellen Clusterings:**
- 02_04_01 (MLOps→LLMOps): Sehr gut bestückt, Kernquellen vorhanden
- 02_04_02 (EU AI Act): Breite Abdeckung, gute Mischung aus Rechtsanalyse und technischen Papers
- Grundstruktur der Cluster ist logisch und spiegelt die Thesis-Gliederung wider

**Schwächen:**
1. **Relevanzfarben systematisch zu niedrig:** Insbesondere Primärquellen wie EU AI Act, Cooper, Elia als GELB statt ROT — das verzerrt Priorisierung
2. **4 klare Fehlzuordnungen in 02_02:** Compliance/Governance-Papers fälschlich als GenAI-Grundlagen klassifiziert
3. **02_01, 02_05, 02_06 unterbesetzt:** Viele SOLL-Quellen aus INHALTSPLAN fehlen im SSOT
4. **3 Duplikate:** Díaz-Rodríguez (Encoding), Wang (Cross-Cluster), Kratzke&Quint (Cross-Cluster)
5. **1 nicht-akademische Quelle:** Amazon Bedrock Guide

**Nächste Schritte (Priorität):**
1. 🔴 7 Fehlzuordnungen korrigieren (Dateien physisch verschieben + CSV updaten)
2. 🔴 20 Farbkorrekturen in CSV durchführen
3. 🔴 3 Duplikate bereinigen + 1 nicht-akademische Quelle entfernen
4. 🟠 13+ fehlende SOLL-Quellen in Zotero importieren und SSOT zuordnen
5. 🟡 CSV-Lücken schließen (Sarra, Sovrano, Baqar-Korrektur)
