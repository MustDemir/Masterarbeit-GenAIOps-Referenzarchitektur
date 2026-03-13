# Deep Reading: Cooper (2008) — Stage-Gate Idea-to-Launch Process
**Relevance: D1 FOUNDATIONAL (Gate-Eignungs-Dimension)**
**Date: 2026-03-12 | Phase 2 Deep Reading**

## 1. Kernbeitrag für D_GATE_INCLUSION_RULE

### Stage-Gate Grundstruktur (D1-Fundament)
- **Stage**: Informationssammlung + Analyse durch cross-funktionales Team
- **Gate**: Go/Kill/Hold/Recycle Entscheidungspunkt

### Gate-Struktur (3 Elemente) — ZENTRAL FÜR D1
| Element | Beschreibung | D1-Implikation |
|---------|-------------|----------------|
| **Deliverables** | Was das Team zum Gate mitbringt (Ergebnisse abgeschlossener Aktivitäten) | → Requirement muss prüfbare Deliverables definieren können |
| **Criteria** | Must-meet (Checklist/Knockout) + Should-meet (Scoring/Punktesystem) | → Requirement muss Akzeptanzkriterien haben |
| **Outputs** | Go/Kill/Hold/Recycle + Action Plan + Deliverables für nächstes Gate | → Gate-Ergebnis muss handlungsrelevant sein |

### D1-Entscheidungslogik (direkt aus Cooper)
```
WENN Requirement → definierbare Deliverables hat:
  UND Akzeptanzkriterien formulierbar (must-meet ODER should-meet):
  UND Gate-Ergebnis zu Go/Kill/Hold/Recycle führt:
  → D1 = JA (Gate-geeignet nach Cooper)

WENN Requirement → keine klaren Deliverables:
  ODER keine messbaren/prüfbaren Kriterien:
  → D1 = NEIN → Querschnittlich (kein eigenständiges Gate)
```

### Cooper's Gate-Prinzipien (für unsere Architektur relevant)
1. **Gates with Teeth**: "projects really do get killed" — nicht nur Rubber-Stamp
2. **Lean Gates**: Nicht überbürokratisieren — minimale aber effektive Prüfung
3. **Cross-functional Gates**: Kein einzelnes Department besitzt ein Gate
4. **Scalable System**: Verschiedene Gate-Intensitäten für verschiedene Projekttypen (Full/Lite/Express)
5. **Flexibility**: Nicht alle Projekte durchlaufen alle Gates; Deliverables können angepasst werden
6. **Incremental Commitment**: Jede Stage kostet mehr → Risiko wird schrittweise reduziert

### Wichtige Abgrenzungen
- Stage-Gate ≠ Phased-Review (linear, funktional) → parallel, cross-funktional
- Stage-Gate ≠ Rigid Lock-Step → anpassbar, Detours möglich
- Stage-Gate ≠ Project Control Mechanism → Enabler für Teams
- Stage-Gate ≠ Data Entry System → Aktivitäten, nicht Formulare

## 2. Implikationen für D_GATE_INCLUSION_RULE

### Mapping Cooper → GenAI-Referenzarchitektur
| Cooper-Konzept | Unsere Adaption | Beispiel |
|---------------|----------------|---------|
| Stage = Information Gathering | Pipeline-Phase (PRE/DEP/OPS) | PRE = Vor Deployment |
| Gate = Go/Kill Decision | Quality Gate mit Pass/Fail | G-PRE-01: Risk Assessment Gate |
| Deliverables | Gate-Artefakte (Checklisten, Reports, Evidence) | FMEA-Dokument, Bias-Report |
| Must-meet Criteria | Mandatory Checks (Policy-as-Code) | Datenqualität ≥ Threshold |
| Should-meet Criteria | Advisory Checks (Scoring) | Model Card Vollständigkeit |
| Scalable (Full/Lite/Express) | Gate-Intensität nach Risikoklasse | High-Risk → Full, Limited → Lite |

### Cooper's "Gates with Teeth" → Unsere Architektur
- **Definierte Gatekeepers**: Wer entscheidet? (→ Laux D3: First vs. Second-Degree)
- **Klare Kriterien**: Vorher definiert, nicht ad hoc (→ Policy-as-Code)
- **Konsequenzen**: Kill ≠ nur Delay → echte Blockade wenn nicht bestanden
- **Ressourcen-Commitment**: Gate-Passage = Freigabe für nächste Investition

## 3. Schlüsselzitate für Section 5.2.2
- "Gates serve as quality-control check points, go/kill and prioritization decision points" (S. 215)
- "Deliverables: what the project leader and team bring to the decision point [...] visible, based on a standard menu" (S. 215)
- "Criteria against which the project is judged: must-meet criteria or knock-out questions (a checklist) [...] and should-meet criteria that are scored" (S. 215)
- "Outputs: a decision (Go/Kill/Hold/Recycle), along with an approved action plan" (S. 215)
- "Gates with teeth: projects really do get killed" (→ gate governance)

## 4. Verbindung zu anderen Papers
- **Laux (2024)**: Gatekeepers = First-Degree (Go/Kill = counterfactual influence) oder Second-Degree (Audit/Review)
- **Kholkar (2025)**: Must-meet Criteria → Policy-as-Prompt automatable; Should-meet → needs human scoring
- **Angelov (2012)**: Reference Architecture Design → Stages als architekturelle Schichten
- **Lucaj (2025)**: Deliverables = TechOps Templates → concrete Gate artifacts
