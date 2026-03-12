# D_GATE_INCLUSION_RULE — Konsolidiertes Gate-Entscheidungsframework
**Version: 3.0 | Datum: 2026-03-12 | Status: ENTWURF zur Validierung**
**Kontext: Masterarbeit Kap. 5.2.2 — Gate-Spezifikation der Enterprise-Referenzarchitektur**
**Changelog v1.0→v2.0:** Elia 2023/2025 (QG4AI), Antiya/Rebbana/Alugunuri (empirische D2-Daten), Pourmajidi (Governance-Infrastruktur) integriert. GAP-D+G geschlossen, GAP-C+E+H gestärkt.
**Changelog v2.0→v3.0:** Laux & Ruschemeier (2025) → GAP-A gestärkt (Automation Bias = D3×D2-Override-Begründung). Sarathe (2025) → GAP-B geschlossen (PaC-Paradigma). Guldimann COMPL-AI (2025) → GAP-C 70-80% geschlossen, GAP-E 50-60%. Vollständiger 335-PDF-Scan abgeschlossen. 11 Deep Readings total.

---

## 0. Problemstellung

> "Wann wird ein regulatorisches Requirement ein eigenständiges Quality Gate, und wie entscheidet man das — reproduzierbar, quellenbasiert, generalisierbar?"

Die D_GATE_INCLUSION_RULE beantwortet diese Frage durch eine dreistufige Entscheidungslogik mit einer Querschnitt-Prüfung. Jede Dimension ist durch mindestens eine Primärquelle fundiert.

---

## 1. Entscheidungsdimensionen (Übersicht)

| Dim. | Name | Kernfrage | Primärquelle(n) |
|------|------|-----------|-----------------|
| **D1** | Gate-Eignung (Cooper-Dimension) | Hat das Requirement prüfbare Deliverables und definierbare Akzeptanzkriterien? | Cooper (2008, S. 215); Lucaj et al. (2025, S. 1649); Elia & Bauer (2023, S. 487) |
| **D2** | Automatisierbarkeit (Operationalisierungs-Dimension) | Ist der Gate-Check maschinenauswertbar, teilweise automatisierbar oder rein manuell? | Muhammad et al. (2026); Nweke & Yeng (2026); Kholkar & Ahuja (2025); Antiya (2020): 75% ISO-Controls automatisierbar |
| **D3** | Oversight-Typ (Laux-Dimension) | Erfordert das Requirement konstitutive (First-Degree) oder korrektive (Second-Degree) menschliche Aufsicht? | Laux (2024, S. 2857–2863) |
| **Q** | Querschnitt-Prüfung | Ist das Requirement phasenübergreifend wirksam statt punktuell prüfbar? | Lucaj et al. (2025); Nweke & Yeng (2026); Elia et al. (2025): Art. 17 QMS → 13 Requirements |

---

## 2. D1 — Gate-Eignung (Cooper-Dimension)

### Quellen
Cooper (2008): Gate = Deliverables + Criteria + Outputs (S. 215).
Lucaj et al. (2025): TechOps-Templates als konkrete Deliverable-Operationalisierung (S. 1649).
Elia & Bauer (2023): Quality Gates entlang des AI-Lifecycle (Data/Software/Model/Deployment/Maintenance) mit domänenspezifischen Kriterien (S. 487–493). **Bestätigt D1-Logik aus AI-Domäne:** Gate-Eignung = prüfbare Deliverables + Kriterien + Risk-basierte Akzeptanz.
Elia et al. (2025): MQG4AI erweitert auf 6 Lifecycle-Phasen (+ Conceptualization, Decommissioning). Unterscheidet Collection-QGs (Prozessorganisation) vs. Leaf-QGs (Design-Entscheidungen mit Input/Output/Evaluation/Risk-Layers).

### D1-Verstärkung durch Elia (v2.0)
Elia bestätigt die Cooper-basierte D1-Logik aus einer unabhängigen Richtung:
- **Lifecycle-Verankerung**: Gate-Eignung hängt auch von der Lifecycle-Phase ab (nicht nur vom Requirement-Inhalt)
- **Risk-Scaling**: Elia 2023 zeigt 6 Risiko-Dimensionen für Gate-Kriterien-Skalierung → Bestätigt GAP-D (Cooper Full/Lite/Express → Risk-Class-Scaling)
- **Elia 2025 Art. 17 QMS-Mapping**: 13 QMS-Requirements aus EU AI Act → prüfbare Gate-Deliverables ableiten

### Entscheidungslogik

```
D1.1: Kann das Requirement auf prüfbare Deliverables abgebildet werden?
      → Operationalisierung: Existiert ein TechOps-Template-Feld (Lucaj)
        oder ein anderes nachweisbares Artefakt?
      → JA → weiter zu D1.2
      → NEIN → D1 = NEIN → Kandidat für Q (Querschnitt)

D1.2: Sind Akzeptanzkriterien formulierbar?
      → Must-meet (Knockout/Checklist) ODER Should-meet (Scoring)?
      → Referenz: Cooper (2008, S. 215): "criteria against which the project
        is judged: must-meet criteria [...] and should-meet criteria"
      → JA → weiter zu D1.3
      → NEIN → D1 = NEIN → Q (Querschnitt)

D1.3: Führt das Gate-Ergebnis zu einer handlungsrelevanten Entscheidung?
      → Go/Kill/Hold/Recycle (Cooper) bzw. PASS/WARN/BLOCK (Muhammad)?
      → JA → D1 = JA (Requirement ist gate-geeignet)
      → NEIN → D1 = NEIN → Q (Querschnitt)
```

### D1-Ergebnis
- **D1 = JA**: Requirement hat Deliverables + Kriterien + handlungsrelevantes Ergebnis → Gate-Kandidat → weiter zu D2
- **D1 = NEIN**: Requirement ist nicht punktuell prüfbar → **Querschnittlich** (kein eigenständiges Gate, aber Compliance-Beitrag über Traceability sichergestellt)

---

## 3. D2 — Automatisierbarkeit (Operationalisierungs-Dimension)

### Quellen
Muhammad et al. (2026): Audit-as-Code Pipeline → PASS/WARN/BLOCK in CI/CD.
Nweke & Yeng (2026): OPA/Rego Policy Enforcement + OSCAL Evidence Packages.
Kholkar & Ahuja (2025): Policy-as-Prompt → LLM-basierte Classifier für Ambiguity-Erkennung.

### Entscheidungslogik

```
D2.1: Ist das Akzeptanzkriterium DETERMINISTISCH auswertbar?
      → Kann als OPA/Rego-Policy (Nweke) oder als Policy-Spec (Muhammad)
        formuliert werden?
      → JA → weiter zu D2.2
      → NEIN → weiter zu D2.3

D2.2: Ist die Evidence AUTOMATISCH sammelbar?
      → Lightweight Evidence Collectors (Muhammad) aus Pipeline-Artefakten?
      → JA → D2 = VOLL AUTOMATISIERBAR
      → TEILWEISE → D2 = HYBRID (Auto-Collection + manuelle Ergänzung)

D2.3: Ist das Kriterium TEILWEISE maschinenauswertbar?
      → Formale Aspekte (Existenz, Vollständigkeit, Format) automatisierbar,
        aber inhaltliche Qualität erfordert menschliches Urteil?
      → Referenz: Kholkar (2025): "flagging ambiguous cases for human review"
      → JA → D2 = HYBRID
      → NEIN → D2 = MANUELL (rein qualitative Bewertung)
```

### D2-Ergebniswerte
| D2-Wert | Beschreibung | Implementierungsmuster | Quelle |
|---------|-------------|----------------------|--------|
| **VOLL** | Deterministisch + automatische Evidence | Policy-as-Code Gate in CI/CD | Muhammad (2026); Nweke (2026) |
| **HYBRID** | Teilautomatisiert + Human Review | Auto-Check für Existenz/Format + manueller Inhalt-Review | Kholkar (2025); Muhammad (2026) |
| **MANUELL** | Rein qualitative Bewertung | Governance-Gate mit Gatekeeper-Entscheidung | Cooper (2008) |

### D2-Empirische Stützung (v2.0)
Die D2-Einstufung ist keine bloße Taxonomie — sie wird durch empirische Befunde gestützt:
- **Antiya (2020):** 75% der ISO 27001 Controls (85/114) sind automatisierbar → analoges Potenzial für AI Act Controls. 70% Audit-Zeit-Reduktion, 83% Fehlerreduktion.
- **Alugunuri (2022):** OPA/Rego Policy-as-Code in CI/CD → 89% Compliance-Failure-Reduktion.
- **Rebbana (2025):** Compliance Gates als Präventionsmechanismus → 76% Governance-Overhead-Reduktion.
- **Pourmajidi et al. (2025):** 4-Stufen-Governance (Code→CI→Pre-CD→Post-CD) bestätigt D2-Stufen architektonisch, aber OHNE formalisiertes Gate-Template.
- **HYPOTHESE (zu validieren):** Wenn 75% der ISO-Controls automatisierbar sind (Antiya), ist eine ähnliche Quote für AI-Act-Requirements plausibel → D2=VOLL sollte Default sein, HYBRID/MANUELL sind die begründungspflichtigen Ausnahmen.

### D2-Paradigma-Verankerung durch Sarathe (v3.0) — GAP-B GESCHLOSSEN
Sarathe et al. (2025) liefern das übergeordnete Paradigma-Paper für D2:
- **Definition:** PaC = "Treating policy like any other code — being able to version it, review it, test it, and automate it" (S. 3400–3401)
- **3-Komponenten-Architektur:** Policy Store (Versionierung) + Policy Engine (Evaluation) + Integration Layer (CI/CD-Einbettung)
- **5 Enforcement-Stages:** Pre-Commit → PR-Review → Build → Deployment → Runtime → bestätigt D2-Stufen architektonisch
- **Maturity-Modell (DSOMM):** Manual → Automated Steps → Code → Mature Lifecycle → rahmt D2-Werte (MANUELL/HYBRID/VOLL) als Reifegradstufen
- **Empirisch:** 63.7% Reduktion Post-Deployment-Issues, 91% nutzen Deployment Gates, 83.7% graduated enforcement (= HYBRID als Praxis-Default)
- **Tooling-Dominanz:** OPA/Rego 64.7% Marktanteil → bestätigt Nweke (2026) OPA-Fokus
- **CAVEAT:** Sarathe grenzt PaC nicht explizit gegen Compliance-as-Code (Muhammad) oder Audit-as-Code ab → diese Abgrenzung muss Demir leisten
- **Position im Kanon:** Sarathe = Paradigma-Enabler, Muhammad/Nweke/Kholkar = Spezialanwendungen

---

## 4. D3 — Oversight-Typ (Laux-Dimension)

### Quellen
Laux (2024): First-Degree vs. Second-Degree Oversight (S. 2857–2858).
Laux & Ruschemeier (2025): Automation Bias im AI Act — empirische Begründung, warum First-Degree Oversight nicht automatisiert werden darf. **Schließt GAP-A als Sekundärbeleg.**

### D3-Verstärkung durch Laux & Ruschemeier (v3.0)
Der D3×D2-Override ist jetzt durch ZWEI Quellen fundiert:
- **Laux (2024):** Konzeptionelle Begründung — "counterfactual influence" erfordert menschliche Beteiligung per Definition
- **Laux & Ruschemeier (2025):** Empirische Begründung — Automation Bias macht automatisiertes Oversight kontraproduktiv:
  - "Awareness allein reicht nicht" → Designinterventionen nötig (= HYBRID, nicht VOLL)
  - Automatisierte Überwachung erzeugt neue Bias-Schichten → Endlosschleife
  - AI Act Art. 14 mandatiert Oversight, adressiert aber nicht die strukturellen Designfaktoren → Gate-Design muss das kompensieren
- **IMPLIKATION für Gate-Design:** Gates mit D3=FIRST müssen nicht nur "Human-in-the-Loop" sein, sondern aktiv Automation Bias mitigieren (z.B. kontrafaktische Alternativen anzeigen, nicht nur AI-Output + Bestätigungsbutton)

### Entscheidungslogik

```
D3.1: Erfordert das Requirement COUNTERFACTUAL INFLUENCE auf den AI-Output?
      → "Having counterfactual influence means that the initial output of an
        AI system could have been different due to human involvement"
        (Laux 2024, S. 2857)
      → Mensch muss VOR/WÄHREND der AI-Entscheidung eingreifen können
        (understand, interpret, override, interrupt — Art. 14(4) KI-VO)?
      → JA → D3 = FIRST-DEGREE (konstitutiv)
      → NEIN → weiter zu D3.2

D3.2: Genügt eine KORREKTIVE ex-post-Prüfung?
      → Audit, Review, Monitoring, Appeals nach Entscheidung?
      → "second-degree oversight is corrective" (Laux 2024, S. 2858)
      → JA → D3 = SECOND-DEGREE (korrektiv)
      → NEIN → Sonderfall prüfen (→ HYPOTHESE: alle Requirements
        fallen in eine der beiden Kategorien)
```

### D3-Ergebniswerte
| D3-Wert | Beschreibung | Gate-Implikation |
|---------|-------------|-----------------|
| **FIRST-DEGREE** | Konstitutiv, counterfactual influence | Gate muss menschliches Urteil einbeziehen → schränkt Automation ein (D2 ≤ HYBRID) |
| **SECOND-DEGREE** | Korrektiv, ex post | Gate kann voll automatisiert sein → D2 kann VOLL sein |

### Kritische Wechselwirkung D2 × D3
```
WENN D3 = FIRST-DEGREE → D2 wird auf max. HYBRID begrenzt
   Begründung: Counterfactual influence erfordert per Definition
   menschliche Beteiligung → voll automatisierte Entscheidung
   ausgeschlossen (Laux 2024, S. 2857)

WENN D3 = SECOND-DEGREE → D2 bleibt unbeschränkt
   Begründung: Korrektive Prüfung kann auch auf automatisch
   gesammelter Evidence basieren
```

---

## 5. Q — Querschnitt-Prüfung

### Quellen
Lucaj et al. (2025): Templates als phasenübergreifende Dokumentation.
Nweke & Yeng (2026): Clause-to-Control Traceability als übergreifende Eigenschaft.
Elia et al. (2025): MQG4AI Art. 17 QMS-Mapping → 13 Requirements als Querschnitt-Rahmen.

### Einordnung
Requirements, die D1 = NEIN ergeben, sind nicht gate-untauglich, sondern **phasenübergreifend wirksam**. Sie werden nicht als eigenständige Gates implementiert, sondern als:
- Traceability-Anforderungen (Clause-to-Control, OSCAL)
- Cross-Gate-Policies (z.B. Transparenzpflichten in JEDEM Gate)
- Continuous Monitoring Rules (nicht punktuell, sondern dauerhaft)

### Q-Verstärkung durch Elia (v2.0)
Elia et al. (2025) liefern eine konkrete Operationalisierung der Q-Dimension:
- **EU AI Act Art. 17 QMS** enthält 13 Requirements (Compliance, Risk, Data Governance, Logging, Monitoring, etc.)
- Diese 13 Requirements wirken phasenübergreifend als "Collection-QGs" (Elia-Terminologie)
- **Demir-Adaptation:** Q-Requirements können als OSCAL-basierte Cross-Gate-Policies implementiert werden, die in JEDEM Gate-Check als Precondition geprüft werden
- **Abgrenzung Elia vs. Demir:** Elia implementiert Q als Wissensmanagement-Template. Demir implementiert Q als Policy-as-Code in CI/CD → automatisierte Querschnitt-Prüfung

### Q-Verstärkung durch COMPL-AI (v3.0) — GAP-C 70-80% GESCHLOSSEN
Guldimann et al. (2025) liefern das fehlende Clause-to-Control-Mapping:
- **Systematische technische Interpretation:** 17 AI Act Artikel → konkrete Technical Requirements → 27+ Benchmarks
- **3-Ebenen-Ansatz:** Requirement → Technical Interpretation → Benchmarking → operationalisiert Q als messbare Pipeline
- **Empirisch auf 12 LLMs:** "All evaluated LLMs reveal shortcomings in robustness, safety, diversity, and fairness" → Q-Requirements sind NICHT automatisch erfüllt, Gates nötig
- **LIMITATION:** COMPL-AI deckt nur technische Benchmarks ab (Accuracy, Fairness, Safety) — keine Governance/Organizational Controls → Demir muss ergänzen
- **Komplementarität:** COMPL-AI (technisch) + Elia MQG4AI (methodisch) + Demir (CI/CD-operationalisiert) = vollständige Q-Abdeckung

---

## 6. Konsolidierte Entscheidungsmatrix

```
┌─────────────────────────────────────────────────────────┐
│                  D_GATE_INCLUSION_RULE                    │
│                  (Entscheidungsfluss)                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Requirement R_xx                                        │
│       │                                                  │
│       ▼                                                  │
│  ┌─── D1: Gate-geeignet? ───┐                           │
│  │ Deliverables?             │                           │
│  │ Akzeptanzkriterien?       │                           │
│  │ Handlungsrelevanz?        │                           │
│  └──────┬──────────┬─────────┘                           │
│      JA │          │ NEIN                                │
│         ▼          ▼                                     │
│    ┌─── D3 ───┐   QUERSCHNITTLICH                       │
│    │ Oversight │   (kein eigenständiges Gate,            │
│    │   Typ?   │    Traceability + Cross-Gate-Policy)     │
│    └──┬────┬──┘                                          │
│  1st  │    │ 2nd                                         │
│  Degr.│    │ Degr.                                       │
│       ▼    ▼                                             │
│    ┌─── D2 ───────────┐                                  │
│    │ Automatisierbar?  │                                  │
│    └──┬─────┬──────┬──┘                                  │
│  VOLL │ HYB.│ MAN. │                                     │
│       ▼     ▼      ▼                                     │
│                                                          │
│  ════════════════════════════════════════                 │
│  ERGEBNIS-MATRIX (D1=JA):                                │
│  ════════════════════════════════════════                 │
│                                                          │
│  D2=VOLL + D3=2nd  → AUTOMATISIERTES GATE               │
│    (Policy-as-Code in CI/CD)                             │
│    Impl.: Muhammad Audit-as-Code + Nweke OPA/Rego       │
│    Ergebnis: PASS/WARN/BLOCK                             │
│                                                          │
│  D2=VOLL + D3=1st  → HYBRID GATE (D3 übersteuert D2)   │
│    Begründung: First-Degree erfordert counterfactual     │
│    influence → menschl. Beteiligung obligatorisch        │
│    Impl.: Auto-Existenzcheck + manueller Inhalt-Review  │
│                                                          │
│  D2=HYBRID + D3=*  → HYBRID GATE                        │
│    Impl.: Auto-Check (Existenz/Format/Threshold)        │
│           + Human Review (Qualität/Angemessenheit)       │
│                                                          │
│  D2=MANUELL + D3=* → MANUELLES GOVERNANCE-GATE          │
│    Impl.: Gatekeeper-Entscheidung mit Deliverable-      │
│           Vorlage nach Cooper (Go/Kill/Hold/Recycle)     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 7. Operationalisierungsmodi (Ergebnistypen)

| Modus | Bedingung | Implementierung | Gate-Ergebnis | Quellen |
|-------|-----------|----------------|---------------|---------|
| **AUTOMATISIERT** | D1=JA, D2=VOLL, D3=SECOND | Policy-as-Code Gate in CI/CD Pipeline | PASS/WARN/BLOCK | Muhammad (2026); Nweke (2026) |
| **HYBRID** | D1=JA, D2=HYBRID oder (D2=VOLL ∧ D3=FIRST) | Auto-Existenzcheck + manueller Inhalt-Review | PASS/FLAG→Review/BLOCK | Kholkar (2025); Laux (2024) |
| **MANUELL** | D1=JA, D2=MANUELL | Governance-Gate mit Gatekeeper-Entscheidung | Go/Kill/Hold/Recycle | Cooper (2008) |
| **QUERSCHNITTLICH** | D1=NEIN | Kein eigenständiges Gate; Traceability-Requirement | Continuous Compliance | Lucaj (2025); Nweke (2026) |

---

## 8. Beispiel-Anwendung: R004 (Human Oversight, Art. 14 KI-VO)

```
R004 → D1-Prüfung:
  D1.1: Deliverables? → JA (Human Oversight Plan = TechOps Application Template)
  D1.2: Akzeptanzkriterien? → JA (Must-meet: Plan existiert; Should-meet: Qualifikation dokumentiert)
  D1.3: Handlungsrelevant? → JA (Go/Kill: Deployment ohne Oversight-Plan = BLOCK)
  → D1 = JA

R004 → D3-Prüfung:
  D3.1: Counterfactual influence nötig? → JA
    Art. 14(4): "understand, interpret, override, interrupt"
    = konstitutiver Einfluss auf AI-Output
  → D3 = FIRST-DEGREE

R004 → D2-Prüfung:
  D2.1: Deterministisch? → TEILWEISE
    - Existenz Oversight-Plan: deterministisch prüfbar (file exists? → PASS/BLOCK)
    - Qualifikation der Oversight-Person: NICHT deterministisch (qualitatives Urteil)
  D2.3: Teilweise maschinenauswertbar? → JA
  → D2 = HYBRID

  D3-Override: D3=FIRST ∧ D2=HYBRID → bleibt HYBRID (kein Conflict)

ERGEBNIS: R004 → HYBRID GATE (G-PRE-05)
  Auto-Check: Oversight-Plan existiert, Rollenzuweisung vorhanden
  Human-Review: Qualifikation der Oversight-Person, Angemessenheit der Maßnahmen
```

---

## 9. Beispiel-Anwendung: R010 (Post-Market Monitoring, Art. 72 KI-VO)

```
R010 → D1-Prüfung:
  D1.1: Deliverables? → JA (Monitoring-Plan, Incident-Reports)
  D1.2: Akzeptanzkriterien? → JA (Must-meet: Plan vorhanden; Should-meet: KPIs definiert)
  D1.3: Handlungsrelevant? → JA (WARN bei fehlenden KPIs, BLOCK bei fehlendem Plan)
  → D1 = JA

R010 → D3-Prüfung:
  D3.1: Counterfactual influence? → NEIN
    Post-Market = ex post, korrektiv, kein Einfluss auf initialen Output
  → D3 = SECOND-DEGREE

R010 → D2-Prüfung:
  D2.1: Deterministisch? → JA (Plan-Existenz, KPI-Thresholds)
  D2.2: Evidence automatisch sammelbar? → JA (Pipeline-Metriken, Logs)
  → D2 = VOLL

  D3-Override: D3=SECOND → D2 bleibt VOLL (kein Override)

ERGEBNIS: R010 → AUTOMATISIERTES GATE (G-OPS-04)
  Impl.: Policy-as-Code Check in CI/CD → PASS/WARN/BLOCK
  Evidence: OSCAL-Package mit Monitoring-Plan + KPI-Thresholds
```

---

## 10. Quellenregister

| Kürzel | Vollzitat | Dimension |
|--------|----------|-----------|
| Cooper (2008) | Cooper, R. G. (2008). The Stage-Gate Idea-to-Launch Process—Update, What's New and NexGen Systems. *Journal of Product Innovation Management*, 25(3), 213–232. | D1 |
| Lucaj et al. (2025) | Lucaj, L., et al. (2025). TechOps: Technical Documentation Templates for the AI Act. *Proceedings of the ACM on Human-Computer Interaction*, 9(CSCW1), 1–38. | D1, Q |
| Laux (2024) | Laux, J. (2024). Institutionalised Distrust and Human Oversight of Artificial Intelligence. *Digital Society*, 3, 54. | D3 |
| Muhammad et al. (2026) | Muhammad, A., et al. (2026). Audit-as-Code for AI: Integrating Automated Governance Checks into AI System Pipelines. *Frontiers in Artificial Intelligence*, 9, 1759211. | D2 |
| Nweke & Yeng (2026) | Nweke, L. O. & Yeng, P. K. (2026). Compliance-as-Code: Automating AI Governance for Identity Systems Under Regulatory Frameworks. *IEEE Access*, 14, 28258–28281. | D2, Q |
| Kholkar & Ahuja (2025) | Kholkar, D. & Ahuja, K. (2025). Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents. Preprint. | D2 |
| Feng et al. (2024) | Feng, S., et al. (2024). Normative Requirements Operationalization with Large Language Models. *RE 2024*. | Sekundär (D1) |
| Elia & Bauer (2023) | Elia, M. & Bauer, B. (2023). A Methodology Based on Quality Gates for Certifiable AI in Medicine. *ICSOFT 2023*, 486–493. https://doi.org/10.5220/0012121300003538 | D1, D_GATE |
| Elia et al. (2025) | Elia, M., et al. (2025). MQG4AI: Towards Responsible High-risk AI – Illustrated for Transparency Focusing on Explainability Techniques. Preprint. | D1, Q, D_GATE |
| Antiya (2020) | Antiya, V. (2020). Automating ISO 27001 Compliance. [Thesis/Report]. | D2 (empirisch) |
| Alugunuri (2022) | Alugunuri, S. (2022). OPA/Rego in CI/CD Pipelines. [Thesis/Report]. | D2 (empirisch) |
| Rebbana (2025) | Rebbana, N. (2025). Compliance Gates for Cloud Governance. [Publication details TBD]. | D2 (empirisch) |
| Pourmajidi et al. (2025) | Pourmajidi, W., et al. (2025). A Reference Architecture for Governance of Cloud Native Applications. [Publication details TBD]. | Q (Infrastruktur) |
| Laux & Ruschemeier (2025) | Laux, J. & Ruschemeier, H. (2025). Automation Bias in the AI Act. *Cambridge University Press* (Open Access). | D3 (Sekundärbeleg) |
| Sarathe et al. (2025) | Sarathe, K., et al. (2025). Policy as Code: A Paradigm Shift in Infrastructure Security and Governance. *World Journal of Advanced Research and Reviews*, 26(1), 3399–3405. https://doi.org/10.30574/wjarr.2025.26.1.1441 | D2 (Paradigma) |
| Guldimann et al. (2025) | Guldimann, P., et al. (2025). COMPL-AI Framework: A Technical Interpretation and LLM Benchmarking Suite for the EU AI Act. arXiv:2410.07959v2. | Q, E (Benchmarks) |

---

## 11. Offene Fragen / Gaps (v3.0 — aktualisiert 2026-03-12)

### GESCHLOSSEN seit v1.0:
- ~~**GAP-D (Risk-Scaling)**~~: Elia 2023 (6 Risiko-Dimensionen) + Elia 2025 (8 Scaling-Mechanismen) liefern Risk-Class-Scaling-Logik
- ~~**GAP-G (QG-Vergleichspunkt)**~~: Elia 2023+2025 = einziges existierendes Quality-Gate-Framework für AI

### GESCHLOSSEN seit v3.0:
- ~~**GAP-B (D2-Paradigma)**~~ 🟢: Sarathe et al. (2025) liefert übergeordnetes PaC-Paradigma mit 3-Komponenten-Architektur (Store/Engine/Integration), 5 Enforcement-Stufen und DSOMM-Maturity-Modell. Empirisch: 63.7% Reduktion Post-Deployment-Issues, OPA 64.7% Marktanteil. **Caveat**: Sarathe unterscheidet nicht explizit CAC vs. AAC — Demir muss diese Differenzierung als eigene Erweiterung argumentieren.

### DEUTLICH GESTÄRKT (v3.0):
- **GAP-A (D3×D2-Override)** 🟡→🟢⁻: Jetzt ZWEI Quellen — Laux (2024) konzeptionell + Laux & Ruschemeier (2025) empirisch (Automation Bias: "awareness alone insufficient" → Design-Interventionen nötig). **Verbleibend**: Kein Paper formuliert den Override explizit als Gate-Kaskade D3→D2. Demir muss diesen Schritt als eigene Design-Entscheidung (DSR) deklarieren.
- **GAP-C (Regulation→Gate)** 🟡→🟢⁻: Elia 2025 Art. 17 QMS-Mapping (13 Reqs) + COMPL-AI Clause-to-Control-Mapping (17 Artikel → 27+ Benchmarks auf 12 LLMs getestet). **Verbleibend**: Demir-spezifische Synthese Regulation→D1/D2/D3-Bewertung→Gate-Typ als formalisierte Entscheidungsregel.
- **GAP-E (Empirische Validierung)** 🟡: Antiya 75% + Rebbana 76% + Alugunuri 89% + Sarathe 63.7% + COMPL-AI 12-LLM-Evaluation ("all reveal shortcomings"). **Verbleibend**: Eigene Validierung der D_GATE_INCLUSION_RULE auf R001–R014 + Expert Review.

### WEITERHIN OFFEN:
1. **GAP-F: Akteurs-Rollen** 🟡 — Elia 2025 hat active/consulting/passive Stakeholder-Rollen + Laux/Ruschemeier asymmetrische Provider/Deployer-Verantwortung, aber kein vollständiges Akteurs-Mapping auf Gate-Ebene. → **Kiejnich-Kruk (2025) SHOULD-READ** oder **Elicit Q4**
2. **GAP-H: D2-Schwellenwerte** 🟡 — Ab welcher Accuracy gilt "VOLL"? Kholkar 70-73%, Sarathe nennt DSOMM-Level aber keine konkreten Accuracy-Thresholds für Safety-Critical. → **Elicit Q2** oder eigene Design-Entscheidung mit Begründung
3. **D3 Grenzfälle** 🟡 — Requirements mit First- UND Second-Degree-Aspekten → **Elicit Q3** oder argumentative Lösung über "dominant oversight mode"

### BEIBEHALTENE FRAGE (seit v2.0):
4. **Elia-Abgrenzung als Related Work**: Wissenschaftlich präzise Formulierung:
   - Elia = domänenspezifisch (Medizin) + QG als Wissensmanagement-Methodik (Information Management)
   - Demir = domänenübergreifend (Enterprise) + QG als CI/CD-Gate mit Policy-as-Code-Automatisierung
   - Elia hat KEINE Automatisierungsdimension (D2), KEINE Oversight-Taxonomie (D3), KEIN CI/CD-Integration-Muster
   - → Demir's USP: D2+D3+CI/CD-Operationalisierung + EU AI Act Compliance-Enforcement + formalisierte D_GATE_INCLUSION_RULE
   - → Elia's Stärke: Lifecycle-Granularität + Information-Management-Integration + Risk-Ontologie

---

## 12. Meta-Information (v3.0)

- **Generalisierbarkeit**: Die D_GATE_INCLUSION_RULE ist regulierungsagnostisch formuliert. D1/D2/D3 sind auf beliebige Regulierungen anwendbar; die EU-AI-Act-Anwendung ist ein Instanziierungsfall.
- **DSR-Verankerung**: Design Principle → "Gate-Entscheidungen müssen reproduzierbar, quellenbasiert und nachvollziehbar getroffen werden" (Hevner et al., 2004: Rigor Cycle)
- **Related Work Position**: MQG4AI (Elia et al., 2025) ist der direkteste Vergleichspunkt. Demir erweitert Elia um: (1) D2-Automatisierungsdimension mit PaC-Paradigma nach Sarathe, (2) D3-Oversight-Taxonomie nach Laux + Automation-Bias-Beleg nach Laux/Ruschemeier, (3) CI/CD-Integration via Policy-as-Code, (4) formalisierte Entscheidungsregel statt methodischem Rahmen, (5) COMPL-AI-kompatible Benchmark-Integration für Q-Dimension.
- **Quellenabdeckung v3.0**: 16 Quellen, davon 11 deep-read. 3+1 Dimensionen mit jeweils ≥2 unabhängigen Belegen. D3×D2-Override durch 2 Quellen gestützt (Laux 2024 + Laux/Ruschemeier 2025).
- **Nächster Schritt**: (1) Validierung durch Anwendung auf alle 14 Requirements (R001–R014) → Konsistenz-Check. (2) Elicit-Suchen für GAP-F (Akteurs-Rollen), GAP-H (D2-Schwellenwerte), D3-Grenzfälle. (3) chapter_state.yaml aktualisieren.
