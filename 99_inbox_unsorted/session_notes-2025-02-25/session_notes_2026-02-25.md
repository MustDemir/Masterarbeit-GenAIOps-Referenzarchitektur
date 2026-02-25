# Session Notes — 2026-02-25
## Source: claude-ai (Masterarbeit GenAIOps)

### Thema
Related-Work-Analyse (4 Papers) + Vergleichsmatrix + Related-Work-Comparator-Skill erstellt

### Artefakte (final)
- **Related_Work_Vergleichsmatrix.xlsx** — 3-Sheet Excel: Feature-Matrix (7 Kategorien × 35 Dimensionen, farbkodiert ✓/◐/✗), Abgrenzungssätze (APA7), Lücken-Analyse (PD1/PD2/PD3)
- **related-work-comparator-skill/** — Custom Claude-Skill (SKILL.md + references/methodology.md + references/matrix_template.py) für systematischen Paper-Vergleich gegen eigene Arbeit

### Related-Work-Paper-Analyse (4 Papers bewertet)

**Paper #1: Nellutla (2025) "MLOps 2.0" — Preprints.org**
- DOI: 10.20944/preprints202511.2095.v1
- Bewertung: 🔴 HERABGESTUFT
- RED FLAGS: Nicht peer-reviewed, Single Author "Independent Researcher USA", erfundene DOI in Referenzen (Ref [5]: `10.1109/BD.2024.123456`), predatory journal (UGC CARE II), synthetische Daten
- Konzeptionell: CDV-Framework (Contract → Validation → Severity → Pipeline-Decision) + Severity Block/Warn/Audit
- Empfehlung: NICHT als Hauptquelle, maximal Fußnote Grau-Literatur
- Verwertbar: Policy-as-Code-Begriff im MLOps-Kontext

**Paper #2: Pourmajidi et al. (2025) "CNA Governance" — IEEE TCC**
- DOI: 10.1109/TCC.2025.3578557
- Bewertung: 🟢 EXZELLENT (akademische Qualität)
- Relevanz: MITTEL-HOCH (Kap. 2 Background + Abgrenzung)
- Affiliationen: Toronto Metropolitan + UMD + IBM Canada Lab
- Beiträge: 4-Stufen Continuous Governance (Code→CI→Pre-CD→Post-CD), Immutable Data Storage, XaC/IaC/GitOps, CCM Alignment
- Lücke (= Demir USP): Kein GenAI/LLM, kein EU AI Act, keine Quality Gates für Modell-Qualität, keine probabilistischen Checks, keine Policy-Engine (OPA/Rego)
- Elevator Pitch: "Pourmajidi zeigt embedded Governance in Cloud-Native funktioniert — meine Arbeit überträgt das auf GenAI mit Faithfulness-Scores, Hallucination-Detection und AI-Act-Conformity"

**Paper #3: Buscemi et al. (2025) "EU AI Act Verification" — arXiv**
- DOI: 10.48550/arXiv.2512.13907
- Bewertung: 🟢 GUT bis SEHR GUT
- Relevanz: SEHR HOCH — direkter Komplementär-Paper
- Affiliationen: LIST (Luxembourg) + RISE (Sweden), EU-gefördert
- Beiträge: 11 High-Level Requirements → 48 Sub-Requirements → 66 Verification Activities, Scania Automotive Case Study, ISO-Standards-Grounding
- Lücke (= Demir USP): Keine Automatisierung (alles manuell), keine CI/CD-Integration, keine Quality Gates, kein Evidence Store, keine GenAI-Metriken, kein DSR
- ENTSCHEIDEND: Buscemi = WAS (welche Verification Activities), Demir = WIE (Automatisierung als Policies in Pipeline)
- Elevator Pitch: "Buscemi hat das beste AI-Act-Mapping zu Verification Activities. Aber deren Output sind Tabellen — meiner sind ausführbare Policies in einer Pipeline"

**Paper #4: Mahr et al. (2024) "LLM Architecture" — IEEE SIITME**
- DOI: 10.1109/SIITME62556.2024.10806573
- Bewertung: 🟡 (Workshop-Paper)
- Relevanz: MITTEL (Kap. 2 Background)
- Beiträge: 5 vertikale Blöcke (Data Prep → Model Strategies → Evaluation → Deployment → Prompt Engineering)
- Lücke: MLOps Level 0, "evaluation at surface level", kein PoC, keine Quality Gates, kein AI Act
- Elevator Pitch: "Mahr endet bei 'Passed Evaluation' als binärer Entscheidung; mein Gate-Framework definiert die Entscheidungsstruktur selbst"

### Kernaussage der Matrix für Prof
Mahr = WAS (Komponenten), Pourmajidi = WIE (Cloud-Infra-Governance), Buscemi = WAS (AI Act Compliance-Mapping) — aber KEINER kombiniert alle drei in einer automatisierten GenAI-Architektur mit formalisierten Quality Gates. Das ist der USP.

### Related-Work-Comparator-Skill
- 4-Phasen-Prozess: Intake → Systematischer Vergleich → Output → Thesis-Einordnung
- Demir-Referenzprofil fest kodiert (4 Säulen, Quality Gates, Pipeline, Compliance)
- 7 Vergleichskategorien × 35+ Dimensionen
- Ampel-Qualitätsbewertung (🟢/🟡/🔴) mit RED FLAG Detection
- Output: L1-Zusammenfassung + Excel-Matrix + Abgrenzungssatz + Elevator Pitch + DOI
- Dateien: SKILL.md, references/methodology.md, references/matrix_template.py

### Abgrenzungsstrategie für Kap. 2
- Mahr (2024): "adressiert weder formalisierte Qualitätskontrollpunkte noch regulatorische Anforderungen"
- Pourmajidi (2025): "adressiert ausschließlich infrastrukturelle Governance, keine GenAI-Mechanismen"
- Buscemi (2025): "bleibt auf Ebene manueller Checklisten, keine technische Architektur zur Automatisierung"
- Synthese: "Drei Innovationsbeiträge: (1) Quality-Gate-Framework 3D, (2) Compliance-as-Code OPA/Rego, (3) Evidence Store für Audit-Trails"

### Offene Punkte
- [ ] Pourmajidis 4-Stufen-Modell explizit mit Gate-Framework vergleichen?
- [ ] Gate-Framework auf Buscemis R1–R11 mappen (Traceability-Nachweis)?
- [ ] Breck et al. (2017) "ML Test Score" als Quelle für Quality Gates in ML?
- [ ] Drittes Paper "Unified Framework EU AI Act" (ResearchGate) aufarbeiten?
- [ ] Related-Work-Comparator-Skill testen mit neuem Paper

### Tags
masterarbeit, related-work, paper-analyse, vergleichsmatrix, quality-gates, compliance, genaiops, pourmajidi, buscemi, mahr, nellutla, skill-creation, eu-ai-act
