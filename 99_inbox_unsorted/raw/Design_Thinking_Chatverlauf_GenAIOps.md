# Design-Thinking Chatverlauf: GenAIOps-Referenzarchitektur
**Datum:** 2026-02-28
**Kontext:** Masterarbeit — Cloud-native Referenzarchitektur für GenAIOps mit Quality-Gate-Kontrollsystem

---

## 1. Initiale Aufgabenstellung (User)

> Lass uns mal ein Gedankenspiel machen. Du bist GenAIOps Experte und dann ist da noch ein Cloud Architektur Experte, ein Cloud Engineer, ein Programmierer und ein Data Engineer… nehmen wir einen Use Case: Ich möchte, dass sich diese Experten alle über das Thema diskutieren: Cloud-native Referenzarchitektur für GenAIOps mit Quality-Gate-Kontrollsystem zur lifecycle-integrierten Operationalisierung normativer Anforderungen – auf Basis des EU AI Act. Und zwar sollen sie eine Lösung entwerfen, die diese Dimensionen löst, wobei es nicht neuartig sein muss, sondern mehrere etablierte Mechanismen bindet (kann auch neu sein). Dadurch soll Neuheitswert entstehen durch die Bindung:
> 1. Dimension PD1: Fragmentierung bestehender Operationalisierungsframeworks
> 2. Dimension PD2: Methodische Inadäquanz bestehender Qualitätssicherungsmechanismen
> 3. Dimension PD3: Compliance-Operationalisierungslücke (EU AI Act)

---

## 2. Erste Design-Thinking-Runde (Spontan, ohne Research)

### Teilnehmer-Setup

| Kürzel | Rolle | Fokus |
|--------|-------|-------|
| **KO** | Koordinator / Protokollant | Moderation, Synthese, Scope-Guard |
| **GO** | GenAIOps-Experte | ML/LLM-Lifecycle, CT/CD, Model Registry |
| **CA** | Cloud-Architekt | IaC, Landing Zones, Service Mesh, Plattform-Design |
| **CE** | Cloud Engineer | Terraform/Pulumi, K8s, Observability, Runtime |
| **DEV** | Programmierer | SDK, API-Design, Policy-as-Code, Testing |
| **DE** | Data Engineer | Data Pipelines, Lineage, Feature Stores, Governance |

### Phase 1: Problem-Framing (Empathize / Define)

**GO (GenAIOps):**
> „PD1 trifft mich direkt. Wir haben MLflow für Experiment-Tracking, LangSmith für LLM-Tracing, Weights & Biases für Metriken — aber kein einheitliches Control Plane, das den gesamten GenAI-Lifecycle abdeckt. Jedes Tool hat eigene Metadaten-Schemata. Wenn ich ein Quality Gate zwischen Fine-Tuning und Deployment setzen will, muss ich drei APIs abfragen und die Ergebnisse manuell korrelieren. Es fehlt eine Abstraktionsschicht, die tool-agnostisch Gate-Evidenz aggregiert."

**CA (Cloud-Architekt):**
> „Aus Plattform-Sicht: PD3 ist ein Albtraum. Der EU AI Act fordert Risiko-Klassifizierung, technische Dokumentation, Post-Market-Monitoring — aber keiner sagt mir, wo in meiner Landing Zone diese Kontrollen leben. Ist das ein Sidecar? Ein Policy-Engine-Layer? Ein separater Compliance-Service? Ohne architektonisches Mapping von normativen Anforderungen auf Cloud-native Primitives (Namespaces, Service Accounts, Network Policies) bleibt Compliance ein Papier-Artefakt."

**CE (Cloud Engineer):**
> „Ich sehe PD2 in der Runtime. Klassische Health-Checks (liveness, readiness) reichen für GenAI nicht. Ich brauche Content-Safety-Probes, Hallucination-Detection-Metrics, Latency-Budgets pro Token. Aber bestehende QA-Mechanismen aus DevOps — SonarQube, Unit-Tests, Integration-Tests — haben kein Konzept für stochastische Outputs. Wir brauchen Quality Gates, die probabilistische Schwellenwerte verstehen."

**DEV (Programmierer):**
> „PD1 und PD2 zusammen: Ich will Policy-as-Code schreiben — z.B. OPA/Rego oder Cedar — die sagt: ‚Kein Modell geht in Produktion ohne Bias-Audit mit Fairness-Score > 0.8.' Aber es gibt keinen standardisierten Policy-Katalog für GenAI. Jedes Team erfindet seine eigenen Checks. Ich brauche ein GenAI Policy SDK, das vordefinierte Policies mitbringt und erweiterbar ist."

**DE (Data Engineer):**
> „PD3 aus Data-Sicht: Der EU AI Act fordert Data Governance und Traceability für Trainingsdaten. Aber meine Pipelines enden am Feature Store. Wer trackt, welches Dokument in welchem RAG-Index gelandet ist? Data Lineage für GenAI — also Prompt-to-Source-Traceability — existiert in keinem Tool out-of-the-box. Ohne das ist Artikel 10 (Daten und Datenqualität) nicht nachweisbar."

### Synthese Runde 1

| PD | Kern-Gap |
|----|----------|
| **PD1** | Kein unified Control Plane; Tool-Silos mit inkompatibler Metadaten-Schicht |
| **PD2** | DevOps-QA ist deterministisch — GenAI braucht probabilistische Gates |
| **PD3** | Normative Anforderungen ohne architektonisches Mapping; Data Lineage endet vor dem LLM |

### Offene Fragen aus Runde 1:
1. Abstraktionsebene: Meta-Orchestrator (Adapter) vs. eigenes Control Plane?
2. Gate-Topologie: Synchrone Blocker vs. asynchrone Auditoren?
3. Compliance-Encoding: Artikel-Ebene vs. Risk-Level-Ebene?

---

## 3. User-Anforderung: 10 Runden mit Research-Fundierung

> Mache insgesamt 10 Runden und halte die Ergebnisse als MD fest. Die Argumente sollen auf einander aufbauen und folgen von Basis-Grundideen/Probleme. Dann sollen die Experten diskutieren, dann soll die Diskussion immer in die Tiefe gehen. Das muss aufeinander aufbauen. Dann müssen Argumente sortiert werden und dann bauen die Experten wieder darauf auf — so machst du Steps. Deshalb wäre nicht das Scannen von allen möglichen Papers und Quellen notwendig, sondern aufbauend aufeinander je nach Ergebnis nach jeder Runde — so kannst du dein Research eingrenzen und spezifizieren.

### User-Entscheidungen zum Scope:
1. **Fokus:** Explizit auf High-Risk AI Systems (Art. 6 EU AI Act)
2. **Stack:** Erst agnostisch, dann sollen die Experten Provider-Entscheidung treffen (Stichpunkt: europäische Souveränität)
3. **Tiefe:** Konkrete Technologie-Entscheidungen + Architektur (ohne Code), Tools pro Provider, Best Practice 2025/2026
4. **Research:** Die Experten sind "Professoren" in ihrem Bereich — Research-Funktion ist ihr Gehirn

---

## 4. Verbesserter Design-Thinking-Ansatz (Methodischer Rahmen)

### Prinzip: Jede Runde hat einen klaren Output → der Output bestimmt den Research-Fokus der nächsten Runde.

| Runde | Phase | Was passiert | Research-Trigger |
|-------|-------|-------------|-----------------|
| **1** | Empathize | Experten bringen Praxis-Probleme ein | → Research: Ist das Problem real? Evidenz? |
| **2** | Define | Konsolidiertes Problem-Statement | → Research: Bestehende Lösungsansätze für genau dieses Statement |
| **3** | Ideate I | Jeder schlägt Baustein vor | → Research: Sind die Bausteine state-of-the-art? Alternativen? |
| **4** | Ideate II | Bausteine verbinden, Architektur-Sketch | → Research: Referenzarchitekturen, die ähnliches versuchen |
| **5** | Prototype I | Technologie-Entscheidungen pro Baustein | → Research: Tool-Vergleiche, europäische Souveränität |
| **6** | Prototype II | Provider-Entscheidung + Landing Zone | → Research: EU Cloud Provider, GAIA-X, Sovereign Cloud |
| **7** | Test I | Experten-Kritik: Was bricht? Trade-offs? | → Research: Bekannte Failure Patterns |
| **8** | Test II | Compliance-Validierung gegen EU AI Act | → Research: Artikel-Mapping, aktuelle Enforcement-Entwicklungen |
| **9** | Refine | Finale Architektur mit allen Anpassungen | → Research: Best Practices 2025/2026 Konsolidierung |
| **10** | Deliver | Blueprint-Dokument + Entscheidungsmatrix | Kein neuer Research — Synthese |

### Zusätzliche Mechanismen:
1. **Devil's Advocate pro Runde** — Ein Experte muss die Gegenposition einnehmen
2. **Entscheidungslog** — Jede Design-Entscheidung mit Begründung + verworfene Alternative
3. **Traceability-Matrix** — Jeder Baustein wird auf PD1/PD2/PD3 zurückgeführt
4. **Constraint-Register** — Harte Randbedingungen (EU-Souveränität, K8s-native, etc.) sichtbar gehalten

---

## 5. Research-Briefing Runde 1: Empathize-Grundlage

### Research-Auftrag (gezielt, 3 Fragen):
1. **(GO + CA):** Aktueller Stand Fragmentierung MLOps/LLMOps/GenAIOps 2024–2026
2. **(CE + DEV):** Herausforderungen QA für GenAI/LLM in Produktion — warum reicht klassische QA nicht?
3. **(DE + Compliance):** EU AI Act Operationalisierung, technische Anforderungen Art. 9–15, europäische Cloud-Souveränität

### Research-Ergebnisse (Zusammenfassung der Deep-Research):

#### 5.1 Fragmentierung des Ops-Ökosystems

**Kern-Evidenz:**
- **95% aller Enterprise-GenAI-Pilotprojekte** liefern keinen messbaren P&L-Impact (MIT NANDA, 2025)
- Gartner: 30% der GenAI-Projekte werden nach PoC abgebrochen
- S&P Global: 42% der Unternehmen haben 2025 die meisten KI-Initiativen abgebrochen
- Enterprise-Ausgaben: **$37 Mrd.** (2025), 3,2× mehr als 2024
- 87% der Unternehmen fehlen umfassende AI-Security-Frameworks
- 46% der Büroangestellten nutzen "Shadow AI"

**6 überlappende Ops-Disziplinen:** MLOps, LLMOps, GenAIOps, AgentOps, PromptOps, RAGOps

**8 Schlüssel-Tools analysiert:**

| Tool | Stärke | Schwäche | Souveränität |
|------|--------|----------|-------------|
| MLflow 3.0 | 30M+ Downloads, GenAI-Tracing | Databricks-Lock-in | Self-hostbar |
| LangSmith | Tiefste LangChain-Integration | Closed-Source, proprietäres Tracing | Cloud-only |
| Langfuse | Open-Source, OTel-nativ, Self-Host | Limitiertes Alerting | ✅ Stark |
| Arize Phoenix | OTel-first, RAG-Analyse | $50k-100k/Jahr Enterprise | Cloud-fokussiert |
| W&B | Breit aufgestellt | $315-400/Seat/Monat | Cloud-fokussiert |
| Guardrails AI | Input/Output-Validierung | Kein Monitoring | Integrierbar |
| TruLens/Snowflake | RAG Triad Evaluation | Snowflake-Lock-in | Problematisch |
| Helicone | Einfachster Einstieg | Schnell entwachsen | Cloud-only |

**5 strukturelle Lücken trotz Tooling-Reichtum:**
1. Keine Plattform deckt End-to-End-Lifecycle ab (3–5 Tools nötig)
2. Cross-Tool-Interoperabilität mangelhaft (proprietäres Tracing)
3. Kein Tool verbindet LLM-Performance mit Business-KPIs
4. Multi-Agenten-Monitoring unreif
5. Keine automatisierten Compliance-Reportings für EU AI Act

#### 5.2 Warum klassische QA bei GenAI versagt

**4 fundamentale technische Probleme:**
1. **Non-Determinismus:** Bis zu 15% Genauigkeitsschwankung zwischen äquivalenten Runs, 70% Best-to-Worst-Gap
2. **Halluzinationen mathematisch unvermeidbar:** Next-Token-Training belohnt "confident guessing over calibrated uncertainty"
3. **Prompt-Sensitivität:** Bis zu 76 Prozentpunkte Performance-Differenz bei Reformulierung
4. **Keine Ground Truth:** Kein Assert-Equals möglich, mehrdimensionale Bewertung nötig

**World Quality Report 2025:**
- 89% pilotieren/deployen GenAI, nur 15% haben Enterprise-Scale erreicht
- Top-Herausforderungen: Integrationskomplexität (64%), Datenschutzrisiken (67%), Halluzinations-Bedenken (60%)

**Neue Evaluation-Frameworks:**

| Framework | Fokus | Besonderheit |
|-----------|-------|-------------|
| DeepEval | "pytest für LLMs" | 30+ Metriken, 400k+ Downloads/Monat, CI/CD-nativ |
| RAGAS | RAG-Evaluation | Referenzfrei, 30+ Metriken, automatische Testgenerierung |
| LLM-as-Judge | Modell bewertet Modell | 80%+ Übereinstimmung mit Menschen, aber zirkuläre Abhängigkeit |
| Promptfoo | Deklarative Tests | 300k+ Nutzer, YAML-basiert, Red-Teaming |
| Giskard | Regulierte Sektoren | Sycophancy-Erkennung, Multi-Turn-Testing |

**Agent Testing Pyramid (Angie Jones, Block, Jan 2026):**
1. Basis: Deterministische Unit-Tests (gemockte LLMs)
2. Record/Replay: Echte LLM-Interaktionen deterministisch abspielen
3. Probabilistische Benchmarks: Mehrfachausführung + Aggregation
4. Spitze: LLM-as-Judge mit klaren Rubrics (3× Majority-Vote)
- CI/CD-Regel: "We don't run live LLM tests in CI" — zu teuer, zu langsam, zu flaky

#### 5.3 EU AI Act — Stand der Operationalisierung

**Timeline:**
- 01.08.2024: AI Act in Kraft
- 02.02.2025: Verbote + AI-Literacy-Pflicht aktiv
- 02.08.2025: GPAI-Verpflichtungen + Governance-Struktur aktiv
- 02.08.2026: Hochrisiko-KI (Annex III) — potenziell verschoben auf 02.12.2027 (Digital Omnibus Package)
- Sanktionen: Bis €35 Mio. oder 7% des weltweiten Umsatzes

**Technische Anforderungen Art. 9–15 (Hochrisiko):**

| Artikel | Anforderung | Technische Implikation |
|---------|-------------|----------------------|
| Art. 9 | Kontinuierliches Risikomanagement | Kein einmaliges Audit — permanente Überwachung |
| Art. 10 | Daten-Governance | Trainings-/Validierungsdaten: relevant, repräsentativ, fehlerfrei |
| Art. 11 | Technische Dokumentation | VOR Markteinführung, 10 Jahre Aufbewahrung, Annex IV |
| Art. 12 | Aufzeichnungspflichten | Automatisches Logging, Rückverfolgbarkeit |
| Art. 13 | Transparenz | Dokumentierte Leistungsgrenzen + Risikoszenarien |
| Art. 14 | Menschliche Aufsicht | Stop/Override jederzeit, Vier-Augen bei bestimmten Anwendungen |
| Art. 15 | Genauigkeit/Robustheit/Security | Adversarial Resilience, deklarierte Accuracy-Levels |

**Standards-Situation:**
- CEN-CENELEC JTC 21 (300+ Experten): Harmonisierte Standards noch nicht fertig
- prEN 18286 (QMS): Voraussichtlich Q4 2026
- ISO/IEC 42001: ~40–50% Überlappung mit AI Act, aber keine CE-Kennzeichnung

**Compliance-Tools:**

| Tool | Typ | Besonderheit |
|------|-----|-------------|
| Credo AI | Commercial | EU AI Act Policy Packs, IBM OEM |
| IBM watsonx.governance | Commercial | AI Factsheets, Lifecycle-Tracking |
| Vanta | Commercial | 400+ Integrationen, Cross-Mapping |
| VerifyWise | Open-Source | BSL 1.1, On-Premises, EU AI Act + ISO 42001 |

**Europäische Cloud-Souveränität:**
- EU kontrolliert nur **4,8% der globalen High-End-AI-Rechenkapazität**
- AI Continent Action Plan: 19 AI Factories + 5 AI Gigafactories (€20 Mrd. InvestAI)
- GAIA-X: 320+ Mitglieder, aber durchwachsene Bilanz (Scaleway ausgestiegen)
- Hyperscaler-Sovereign-Angebote: AWS European Sovereign Cloud (€7,8 Mrd.), Microsoft Sovereign Cloud, Google NATO-Vertrag
- Europäische Provider: STACKIT (€11 Mrd.), T-Systems, OVHcloud, IONOS, Evroc
- Sovereign-Cloud-Markt: $154 Mrd. (2025) → $823 Mrd. (2032)

---

## 6. Nächste Schritte

### Status: Research-Briefing für Runde 1 abgeschlossen

Die Experten haben jetzt ihr "Professorenwissen" aus der Research. Die nächsten Schritte:

1. **Runde 1 (Empathize)** mit research-fundiertem Expertenwissen durchspielen
2. Aus den Ergebnissen den gezielten Research-Auftrag für Runde 2 ableiten
3. Iterativ weiter bis Runde 10

### Offene Design-Entscheidungen (aus der Vorrunde):
- [ ] Meta-Orchestrator vs. eigenes Control Plane?
- [ ] Synchrone vs. asynchrone Gates?
- [ ] Compliance-Encoding: Artikel-Ebene vs. Risk-Level-Ebene?
- [ ] Provider-Strategie: Hyperscaler-Sovereign vs. europäische Provider?

---

## Anhang: Quellenübersicht (Research-Briefing)

### Industrie-Reports
- MIT NANDA (2025): "The GenAI Divide" — 95% Pilotprojekte ohne P&L-Impact
- Gartner (2024): 30% GenAI-Projekte nach PoC abgebrochen
- World Quality Report 2025 (OpenText/Capgemini/Sogeti)
- Lakera GenAI Security Readiness Report 2025
- Deloitte State of AI in Enterprise 2025/2026

### Technologie-Quellen
- Databricks: MLflow 3.0 Blog
- Langfuse: LangSmith Alternative Comparison
- Block Engineering Blog: Testing Pyramid for AI Agents (Jan 2026)
- DeepEval/Confident AI: GitHub + Docs
- RAGAS: arXiv 2309.15217 (EACL 2024)
- Promptfoo: CI/CD Integration Docs
- Giskard: LLM Vulnerability Scanner Docs

### EU AI Act & Compliance
- European Commission: AI Act Regulatory Framework
- Europa AI Act Service Desk: Article 9, Timeline
- CEN-CENELEC: AI Standardisation
- DLA Piper: Latest Wave of AI Act Obligations (Aug 2025)
- K&L Gates: EU AI Act Recent Developments (Jan 2026)
- ISACA: ISO 42001 + EU AI Act Practical Pairing

### Cloud-Souveränität
- AWS European Sovereign Cloud (CitiesABC)
- Microsoft Azure: Sovereign Cloud Blog
- The Register: Europe Sovereign Cloud Investment (Feb 2026)
- GAIA-X Summit 2025
- Evroc Launch (Data Center Dynamics)

---

*Protokoll erstellt am 2026-02-28 durch KO (Koordinator)*
*Nächste Aktion: Runde 1 mit Research-fundiertem Expertenwissen starten*