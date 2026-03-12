# Related-Work-Vergleich — Kap. 4 Argumentationsbausteine vs. ROT+ORANGE Paper

**Datum:** 2026-03-05
**Methode:** Related-Work-Comparator (Skill) + Elicit/Consensus/Scite Suche
**Scope:** 10 ungenutzte ROT+ORANGE Paper aus THEMENCLUSTER gegen Kap. 4.1–4.5 Bausteine
**Bewertung:** (a) Unterstützung, (b) Widerspruch, (c) Erweiterung, (d) Einsatzempfehlung

---

## Kapitel 4 — Argumentationsbausteine (Referenzprofil Demir 2026)

| ID | Baustein | Abschnitt | Kernaussage |
|----|----------|-----------|-------------|
| B1 | Deployer-Lifecycle | 4.2 | Dreistufiges Lifecycle-Modell: Pre-Deployment → Deployment → Operation |
| B2 | Dreistufige Transformation | 4.3 | Norm-Extraktion → Requirement-Spezifikation → Gate-Operationalisierung |
| B3 | Policy-as-Code | 4.3/4.4 | OPA/Rego als Enforcement-Mechanismus für regulatorische Requirements |
| B4 | Quality Gates | 4.6 (geplant) | Formalisierte Gates mit 3D-Dimensionen (Strategisch/Technisch/Compliance) |
| B5 | Continuous Monitoring | 4.4 | Automatisierte Post-Deployment-Überwachung + Drift Detection |
| B6 | Audit Trail | 4.4 | Evidence Store für Conformity Assessment (Annex VI/VII) |
| B7 | Human Oversight | 4.5 | Vier Wirksamkeitsbedingungen (Sterz) + Institutionalisiertes Misstrauen (Laux) |
| B8 | Traceability | 4.6 (geplant) | Normquelle → Requirement → Gate-ID → Evidenzartefakt |

---

## Paper-Vergleichsmatrix

### Legende
- **✅ STÜTZT** = Paper liefert konvergente Evidenz für unseren Baustein
- **⚠️ ERWEITERT** = Paper bringt neue Aspekte die unsere Argumentation ergänzen
- **❌ WIDERSPRICHT** = Paper vertritt eine gegenläufige Position
- **◐ TEILWEISE** = Paper adressiert den Baustein nur am Rande
- **✗ NICHT** = Paper adressiert diesen Baustein nicht

---

## 1. Elia et al. (2025) — MQG4AI ⭐⭐⭐

**Qualität:** 🟢 ArXiv-Preprint aber Elia-Gruppe hat Journal-Track (AI and Ethics 2025). GitHub-Repository verfügbar.
**Relevanz:** HOCH — **Hauptabgrenzungsquelle**

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | MQG4AI deckt kompletten AI Lifecycle ab; "continuous manner, addressing AI's evolutionary character" |
| B2 Transformation | ✅ STÜTZT | "bridges the gap between generic guidelines and use case-specific requirements" — fast identisch zu unserem Dreischritt |
| B3 Policy-as-Code | ✗ NICHT | Kein PaC/OPA-Bezug. Rein methodisch-konzeptionell, keine Automatisierung |
| B4 Quality Gates | ✅ STÜTZT | **Kernkonzept**: "Methodology based on Quality Gates" mit RAI Knowledge Linking. Template-Struktur auf GitHub |
| B5 Continuous Monitoring | ◐ TEILWEISE | Lifecycle-Kontinuität adressiert, aber kein konkretes Monitoring-Framework |
| B6 Audit Trail | ◐ TEILWEISE | "leaf-QG template information structure" als Dokumentationsansatz, aber kein Evidence Store |
| B7 Human Oversight | ✗ NICHT | XAI/Transparency-Fokus, Human Oversight nicht separat behandelt |
| B8 Traceability | ✅ STÜTZT | RAI Knowledge Linking = Traceability von Guidelines zu Use-Case-Requirements |

**Fundamentaler Unterschied:**
> MQG4AI liefert eine XAI/Medizin-fokussierte Quality-Gate-Methodik mit RAI Knowledge Linking, während Demir eine Deployer-generische Referenzarchitektur mit EU AI Act Art. 9–15 + Policy-as-Code-Automatisierung in CI/CD-Pipelines adressiert.

**Selbst-identifizierte Lücken (zitierfähig):**
- MQG4AI fokussiert auf "Explanation stage during model development" — kein Deployment/Operation-Scope
- Keine Pipeline-Integration (CI/CD/CT) oder Automatisierung
- Medizin-Use-Case → Generalisierung auf Enterprise GenAI nicht behandelt

**Bewertung: ✅ STÜTZT unsere Argumentation stark.**
- Konvergente Evidenz für Quality-Gate-Konzept als Lifecycle-Steuerungsinstrument
- Klare Abgrenzung: MQG4AI = XAI-Methodik, Demir = Deployer-Ops + PaC-Automatisierung
- **Einsatz:** 4.6 als Hauptvergleichsquelle + Kap. 2 Related Work Tabelle

---

## 2. Elia & Bauer (2023) — Quality Gates for Certifiable AI in Medicine ⭐⭐

**Qualität:** 🟡 Konferenzpaper, peer-reviewed. Vorgängerarbeit zu MQG4AI.
**Relevanz:** MITTEL — Historischer Vorläufer

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | "Quality Gates along the intelligent system's complete life cycle" |
| B2 Transformation | ✅ STÜTZT | "approach to translate partly more abstract concepts into concrete instructions" — Transformation legal→technical |
| B4 Quality Gates | ✅ STÜTZT | Explizite QG-Methodik für Zertifizierung |
| B3 Policy-as-Code | ✗ NICHT | Rein konzeptionell |
| B8 Traceability | ◐ TEILWEISE | QG-Kriterien mit Prüfmetriken verknüpft |

**Bewertung: ✅ STÜTZT — Konvergente Evidenz für Transformation Regulierung→Technik.**
- **Einsatz:** 4.6 als historische Referenz neben MQG4AI 2025

---

## 3. Lucaj et al. (2025) — TechOps ⭐⭐⭐

**Qualität:** 🟢 Peer-reviewed (AAAI 2025 Workshop). Open-Source-Templates.
**Relevanz:** HOCH — Dokumentations-Templates für AI Act

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | Templates decken "entire AI lifecycle" ab (Data, Models, Applications) |
| B2 Transformation | ⚠️ ERWEITERT | Bringt konkretes Template-System für Dokumentation als Zwischenschicht |
| B3 Policy-as-Code | ✗ NICHT | Dokumentations-fokussiert, keine Automatisierung |
| B4 Quality Gates | ◐ TEILWEISE | Templates als "certification"-Instrument, aber keine formalen Gates |
| B6 Audit Trail | ✅ STÜTZT | "sufficient documentation for AI Act certification" — Evidenzartefakt-Konzept konvergent |
| B8 Traceability | ✅ STÜTZT | Traceability über gesamten Lifecycle durch strukturierte Dokumentation |

**Fundamentaler Unterschied:**
> TechOps liefert Dokumentations-Templates (WAS muss dokumentiert werden), während Demir automatisierte Gate-Prüfungen definiert (WIE wird geprüft und erzwungen).

**Selbst-identifizierte Lücken:**
- "practitioners still need help applying documentation solutions consistently" — Automatisierungslücke
- "significant gap between legal and technical experts" — genau unser B2 Transformationsproblem

**Bewertung: ✅ STÜTZT + ⚠️ ERWEITERT unsere Argumentation.**
- TechOps-Templates können als **Evidenzartefakt-Definitionen** in Gate-Design übernommen werden
- Lücke "consistency" = Automatisierungsbedarf = unser PaC-Argument
- **Einsatz:** 4.6 für Evidenzartefakt-Definition, 4.3 als Stützquelle für Transformations-Gap

---

## 4. Nellutla (2025) — MLOps 2.0 ⭐⭐⭐

**Qualität:** 🟡 Preprint/Technical Report. Keine Peer-Review erkennbar. Methodik klar (Referenzarchitektur + CDV).
**Relevanz:** HOCH — Direkte Parallele zu Quality-Gate-Konzept

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | Referenzarchitektur mit Build→Test→Release→Run Stages |
| B2 Transformation | ◐ TEILWEISE | Implizit durch SLO-aligned Promotion Criteria |
| B3 Policy-as-Code | ⚠️ ERWEITERT | "data contracts" + "SLO-aligned promotion criteria" als Policy-Variante |
| B4 Quality Gates | ✅ STÜTZT | **Kernkonzept**: "data quality gates — schema, semantic, temporal, distributional — across build, test, release, and run stages" |
| B5 Continuous Monitoring | ✅ STÜTZT | "training/inference observability" + Drift Detection als CI/CD-integriertes Element |
| B6 Audit Trail | ◐ TEILWEISE | Observability-Daten als impliziter Audit Trail |
| B8 Traceability | ✅ STÜTZT | "escaped defects (silent drift, schema skew, target leakage)" — Trace von Gate zu Defekt |

**Fundamentaler Unterschied:**
> MLOps 2.0 fokussiert auf Datenqualitäts-Gates in CI/CD mit CDV, während Demir dreidimensionale Gates (Strategisch/Technisch/Compliance) mit EU AI Act-Verankerung definiert.

**Bewertung: ✅ STÜTZT stark + ⚠️ ERWEITERT.**
- Konvergente Evidenz dass Quality Gates in CI/CD-Pipelines operationalisierbar sind
- CDV-Konzept (Continuous Data Validation) = Erweiterung über Art. 10 (Data Governance) hinaus
- **Einsatz:** 4.6 für Gate-Architektur-Vergleich, 4.4 als CI/CD-Stützquelle
- **WARNUNG:** Peer-Review-Status prüfen. Falls Grey Lit → nur als ergänzende Referenz, nicht als Kernquelle

---

## 5. Gonçalves & Correia (2025) — XAI-Compliance-by-Design ⭐⭐

**Qualität:** 🟢 Peer-reviewed Journal (Applied Sciences / MDPI, aber Q2-Bereich).
**Relevanz:** HOCH — Konvergent zu Dreischritt-Transformation

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | Dual-Flow: "Upstream Technical Pipeline + Downstream Governance Pipeline" |
| B2 Transformation | ✅ STÜTZT | "Technical-Regulatory Correspondence Matrix (GDPR + AI Act + ISO 42001)" — fast identisch zu unserem Dreischritt |
| B3 Policy-as-Code | ◐ TEILWEISE | "Compliance-by-Design Engine" konzeptionell, aber keine OPA/Rego-Implementierung |
| B4 Quality Gates | ◐ TEILWEISE | Decision Dossier mit "approve, reject, escalate" = Gate-artige Semantik |
| B6 Audit Trail | ✅ STÜTZT | "decision dossier as machine-readable artefact (JSON)" + "evidence bundle" |
| B7 Human Oversight | ◐ TEILWEISE | "approve, reject, escalate" impliziert HITL |
| B8 Traceability | ✅ STÜTZT | "technical-regulatory correspondence matrix" = Traceability Norm→Kontrolle |

**Fundamentaler Unterschied:**
> Gonçalves liefert ein Dual-Flow-Architekturkonzept mit Correspondence Matrix, während Demir die Automatisierung dieser Flows über OPA/Rego in CI/CD-Pipelines konkretisiert.

**Selbst-identifizierte Lücken:**
- "absence of standardised processes for generating, versioning, and maintaining compliance evidence"
- Kein CI/CD-Pipeline-Integration, keine Policy-Engine

**Bewertung: ✅ STÜTZT stark.**
- Konvergente Evidenz für Dual-Pipeline-Ansatz (Technik + Governance)
- Correspondence Matrix = strukturelle Parallele zu unserer Traceability-Tabelle
- **Einsatz:** 4.3 als konvergente Stützquelle für Transformationsmethodik, 4.4 für Evidence-Konzept

---

## 6. Finch & Butt (2025) — Gaps in AI-Compliant Governance ⭐⭐

**Qualität:** 🟢 Systematic Review, methodisch sauber (hybrid systematic-scoping).
**Relevanz:** MITTEL-HOCH — Stützt Deployer-Problematik

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ⚠️ ERWEITERT | "Compliance Asymmetry" — strukturelle Friktionen zwischen Regulierung und institutioneller Kapazität |
| B2 Transformation | ✅ STÜTZT | Identifiziert Gap: "significant gap between legal and technical experts" + "unclear definitions (fairness)" |
| B3 Policy-as-Code | ✗ NICHT | Nicht adressiert |
| B4 Quality Gates | ✗ NICHT | Nicht adressiert |
| B7 Human Oversight | ◐ TEILWEISE | ALTAI-Kritik berührt Human Oversight indirekt |

**Fundamentaler Unterschied:**
> Finch & Butt diagnostizieren Governance-Lücken (Enforceability, Proportionality, Auditability), während Demir eine konkrete Architektur zur Schließung dieser Lücken liefert.

**Bewertung: ✅ STÜTZT + ⚠️ ERWEITERT.**
- "Compliance Asymmetry" = starkes Konzept für Problemdefinition PD3
- Identifiziert genau die Lücken die unsere Architektur schließt
- **Einsatz:** 4.1 (Zielbild) oder 4.6 als Problemevidenz, "Compliance Asymmetry" zitieren

---

## 7. Billeter et al. (2024) — MLOps as Enabler of Trustworthy AI ⭐⭐

**Qualität:** 🟢 IEEE-Konferenz (peer-reviewed).
**Relevanz:** MITTEL — TAI-MLOps Mapping

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | Mapping TAI-Prinzipien → MLOps Lifecycle → MLOps Practices |
| B2 Transformation | ◐ TEILWEISE | Implizite Transformation TAI→Practices, aber nicht regulatorisch |
| B4 Quality Gates | ◐ TEILWEISE | "automated feedback loops and metrics, ensuring continuous assessment of TAI principles" |
| B5 Continuous Monitoring | ✅ STÜTZT | Continuous Assessment als Kernprinzip |

**Fundamentaler Unterschied:**
> Billeter mapped TAI-Prinzipien generisch auf MLOps-Praktiken, während Demir spezifische EU AI Act-Artikel auf formalisierte Gate-Kriterien abbildet.

**Bewertung: ✅ STÜTZT.**
- Konvergent zu "Quality Gates als TAI-Enabler"-Argument
- Aber: Überlappung mit Ray (2026) TRiSM → als **ergänzende** Referenz, nicht als Hauptquelle
- **Einsatz:** 4.2 (Lifecycle) oder 4.4 als konvergente Stützquelle

---

## 8. Slupczynski et al. (2026) — CAPTURE ⭐⭐

**Qualität:** 🟢 Journal (Applied Sciences), validiert durch 5-Jahres-Case-Study + 10 Expert Interviews.
**Relevanz:** MITTEL — Decision Gates + Stakeholder-Alignment

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B1 Deployer-Lifecycle | ✅ STÜTZT | 7-Phasen: Consult→Articulate→Protocol→Terraform→Utilize→Reify→Evolve |
| B2 Transformation | ◐ TEILWEISE | "Articulate" + "Protocol" Phasen = Requirements Engineering |
| B4 Quality Gates | ⚠️ ERWEITERT | Formalisierte Gate-Score Θ mit gewichteten Kriterien (Observation, Interaction, KPI, Feedback) |
| B7 Human Oversight | ✅ STÜTZT | Stakeholder-Centered + iterative evaluation in authentic contexts |

**Fundamentaler Unterschied:**
> CAPTURE liefert ein stakeholder-zentriertes Framework mit quantitativen Gate-Scores (Θ), während Demir Compliance-zentrierte Gates mit Pass/Fail-Semantik und Policy-as-Code-Automatisierung definiert.

**Bewertung: ✅ STÜTZT + ⚠️ ERWEITERT.**
- Gate-Score Θ = interessante Erweiterung für quantitative Gate-Evaluierung
- 5-Jahres-Validierung stärkt generelle Gate-Akzeptanz
- **Einsatz:** 4.2 als konvergente Evidenz für Lifecycle-Phasen mit Gate-Übergängen

---

## 9. Adetayo Adeyinka (2023) — PaC in Hybrid Cloud ⭐⭐

**Qualität:** 🟡 Journal (nicht Top-Tier). Solide Methodik (OPA/Sentinel/Azure Policy Evaluation).
**Relevanz:** MITTEL — PaC-Referenzarchitektur

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B3 Policy-as-Code | ✅ STÜTZT | PaC-Referenzarchitektur + 4-Phasen (Inventory→Engineering→Integration→Monitoring) |
| B5 Continuous Monitoring | ✅ STÜTZT | Phase 4 = Continuous Compliance Monitoring |
| B6 Audit Trail | ✅ STÜTZT | "scalable auditable compliance strategies" |

**Fundamentaler Unterschied:**
> Adeyinka liefert PaC für generische Cloud-Compliance (HIPAA, PCI-DSS), während Demir PaC spezifisch für EU AI Act-Compliance in GenAI-Pipelines einsetzt.

**Bewertung: ✅ STÜTZT.**
- Konvergent zu Sardana (2024) CaC 2.0 → stärkt PaC-Evidenzkette
- **Einsatz:** 4.3/4.4 als zusätzliche Stützquelle für PaC-Architektur

---

## 10. Rebbana (2025) — PaC for Cloud Data Platforms ⭐⭐

**Qualität:** 🟡 Technical Article (kein klassisches Peer-Review). Solide Architektur-Beschreibung.
**Relevanz:** MITTEL — PaC-Implementierungsdetails

| Baustein | Bewertung | Evidenz |
|----------|-----------|---------|
| B3 Policy-as-Code | ✅ STÜTZT | "Policy Definition Languages + Enforcement Mechanisms + Attestation" |
| B5 Continuous Monitoring | ✅ STÜTZT | 4-Phasen analog zu Adeyinka |
| B6 Audit Trail | ✅ STÜTZT | Attestation-Konzept = Evidenzartefakt für Compliance-Nachweis |

**Fundamentaler Unterschied:**
> Rebbana fokussiert auf Cloud Data Platforms (multi-cloud), während Demir PaC für AI-spezifische Compliance-Gates einsetzt.

**Bewertung: ✅ STÜTZT.**
- Stärkt PaC-Evidenzkette zusammen mit Adeyinka + Sardana
- **Einsatz:** 4.3 als ergänzende Stützquelle

---

## Gesamtübersicht: Baustein-Abdeckungsmatrix

| Paper | B1 Lifecycle | B2 Transform | B3 PaC | B4 Gates | B5 Monitor | B6 Audit | B7 Oversight | B8 Trace |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Elia/MQG4AI 2025 | ✅ | ✅ | ✗ | ✅ | ◐ | ◐ | ✗ | ✅ |
| Elia 2023 | ✅ | ✅ | ✗ | ✅ | ✗ | ✗ | ✗ | ◐ |
| Lucaj/TechOps 2025 | ✅ | ⚠️ | ✗ | ◐ | ✗ | ✅ | ✗ | ✅ |
| Nellutla/MLOps 2.0 | ✅ | ◐ | ⚠️ | ✅ | ✅ | ◐ | ✗ | ✅ |
| Gonçalves/XAI-CbD | ✅ | ✅ | ◐ | ◐ | ✗ | ✅ | ◐ | ✅ |
| Finch & Butt 2025 | ⚠️ | ✅ | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ |
| Billeter et al. 2024 | ✅ | ◐ | ✗ | ◐ | ✅ | ✗ | ✗ | ✗ |
| Slupczynski/CAPTURE | ✅ | ◐ | ✗ | ⚠️ | ✗ | ✗ | ✅ | ✗ |
| Adeyinka PaC 2023 | ✗ | ✗ | ✅ | ✗ | ✅ | ✅ | ✗ | ✗ |
| Rebbana PaC 2025 | ✗ | ✗ | ✅ | ✗ | ✅ | ✅ | ✗ | ✗ |

---

## Synthese: Bewertung gegen Kap. 4 Argumentation

### (a) UNTERSTÜTZUNG — Was bestätigt unseren Ansatz?

1. **Quality-Gate-Konzept validiert:** 4 von 10 Paper setzen explizit auf Quality Gates (Elia/MQG4AI, Elia 2023, Nellutla, Slupczynski). **Kein einziges Paper widerspricht dem Gate-Ansatz.** → Starke konvergente Evidenz für B4.

2. **Lifecycle-Phasenmodell konvergent:** 8 von 10 Paper verwenden ein phasiertes Lifecycle-Modell. → B1 durch breite Evidenzbasis gestützt.

3. **Transformations-Gap universell anerkannt:** Elia ("bridges gap between guidelines and requirements"), Lucaj ("gap between legal and technical experts"), Finch ("Compliance Asymmetry"), Gonçalves ("Correspondence Matrix") → **4 unabhängige Bestätigungen** für B2.

4. **PaC als Compliance-Enabler:** Adeyinka + Rebbana + Sardana (bereits in 4.3) = 3 konvergente Quellen. Kholkar (2025, neu aus Consensus) erweitert zu "Policy-as-Prompt". → B3 gut gestützt.

### (b) WIDERSPRUCH — Was steht gegen unseren Ansatz?

**→ KEIN direkter Widerspruch identifiziert.** Keine der 10 Quellen argumentiert gegen:
- Quality Gates als Governance-Instrument
- Automatisierung von Compliance-Checks
- Deployer-zentriertes Lifecycle-Modell

**Hypothese:** Die Abwesenheit von Widerspruch kann daran liegen, dass unser Ansatz eine Synthese bestehender Einzelkonzepte ist, die jeweils isoliert akzeptiert sind. Die Innovation liegt in der Integration.

### (c) ERWEITERUNG — Was bringen die Paper Neues?

1. **Nellutla → CDV (Continuous Data Validation):** Vier Datenqualitäts-Dimensionen (Schema, Semantic, Temporal, Distributional) als Gate-Kriterien. → **Erweiterung für Art. 10 Data Governance Gates.**

2. **Slupczynski → Gate-Score Θ:** Quantitative Gewichtung von Gate-Kriterien statt binärer Pass/Fail. → **Design-Alternative für unsere Gate-Semantik.**

3. **Gonçalves → Correspondence Matrix:** Strukturierte Zuordnung Regulierung→Artefakt als JSON. → **Operationalisierungsidee für Traceability-Tabelle.**

4. **Lucaj → TechOps Templates:** Konkrete Dokumentationsvorlagen für AI Act. → **Evidenzartefakt-Definitionen direkt übernehmbar.**

5. **Finch & Butt → "Compliance Asymmetry":** Konzept für strukturelle Friktionen in Compliance-Ökosystemen. → **Problemdefinition PD3 verstärken.**

6. **Kholkar (2025, NEU) → "Policy-as-Prompt":** PaC-Erweiterung für LLM/Agent-Systeme — Policies als Prompt-Classifier. → **GenAI-spezifische PaC-Variante, relevant für Kap. 5/6.**

### (d) EINSATZEMPFEHLUNG — Wo in Kap. 4 einsetzen?

| Paper | Abschnitt | Einsatzart | Priorität |
|-------|-----------|------------|-----------|
| Elia/MQG4AI 2025 | **4.6** | Hauptvergleichsquelle, Abgrenzungssatz | MUSS |
| Elia 2023 | **4.6** | Historische Referenz neben MQG4AI | MUSS |
| Lucaj/TechOps 2025 | **4.6** + 4.3 | Evidenzartefakt-Definition | MUSS |
| Nellutla/MLOps 2.0 | **4.6** + 4.4 | Gate-Architektur-Vergleich (CDV) | SOLL (wenn peer-reviewed) |
| Gonçalves/XAI-CbD | 4.3 + 4.4 | Konvergente Stützquelle (Dual-Flow) | SOLL |
| Finch & Butt 2025 | 4.1 oder 4.6 | Problemevidenz (Compliance Asymmetry) | SOLL |
| Slupczynski/CAPTURE | 4.2 | Konvergente Evidenz (Decision Gates) | KANN |
| Billeter et al. 2024 | 4.2 oder 4.4 | Stützquelle (TAI→MLOps) | KANN |
| Adeyinka PaC 2023 | 4.3/4.4 | PaC-Evidenzkette | KANN |
| Rebbana PaC 2025 | 4.3 | PaC-Evidenzkette | KANN |

---

## Kritische Fragen

1. **Nellutla (2025) Peer-Review-Status:** Kein Journal/Konferenz identifizierbar. Falls Grey Literature → in 4.6 nur als "ergänzend" verwenden, nicht als Kernquelle. Sollen wir via Zotero/Google Scholar den Venue prüfen?

2. **Gonçalves Platzierung 4.3 vs. 4.6:** Das Dual-Flow-Konzept passt sowohl als konvergente Evidenz in 4.3 (Transformation) als auch als Vergleichsquelle in 4.6 (Requirements). Empfehlung: **4.3 als Stützquelle** (1 Satz), **4.6 als Vergleich** (1 Absatz).

3. **Kholkar "Policy-as-Prompt" (2025):** Neues Paper aus Consensus-Suche — behandelt PaC für LLM-Agents. Für Kap. 4 zu spezifisch, aber **Kap. 5/6 (Architekturentwurf)** relevant. Sollen wir es vormerken?
