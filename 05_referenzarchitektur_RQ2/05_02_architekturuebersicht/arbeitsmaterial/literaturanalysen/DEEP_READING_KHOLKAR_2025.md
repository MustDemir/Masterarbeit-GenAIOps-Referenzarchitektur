# Deep Reading: Kholkar & Ahuja (2025) — Policy-as-Prompt
**Relevance: D2 HIGH (Automatisierbarkeits-Dimension)**
**Date: 2026-03-12 | Phase 2 Deep Reading**

## 1. Kernbeitrag für D_GATE_INCLUSION_RULE

### Policy-as-Prompt Paradigma
- **Problem**: "policy-to-practice gap" — Regeln in natürlicher Sprache → schwer maschinenausführbar
- **Lösung**: End-to-End Pipeline: Unstrukturierte Artefakte (PRD, TDD, Code) → Policy Tree → Prompt-basierte Classifier → Runtime-Guardrails
- **Zwei Stufen**:
  1. POLICY-TREE-GEN: Dokumente parsen → Sicherheitsregeln extrahieren → 4 Kategorien (ID-I, OOD-I, ID-O, OOD-O)
  2. POLICY-AS-PROMPT-GEN: Policy Tree → Markdown-Prompts → LLM als "Judge" → ALLOW/BLOCK/ALERT

### Direkte D2-Relevanz
- **Automatisierbarkeit**: Zeigt konkreten Weg wie natürlichsprachliche Policies zu maschinenauswertbaren Checks werden
- **Least Privilege Enforcement**: Agent darf NUR was Policy explizit erlaubt → Default-Deny
- **Human-in-the-Loop Review**: Security Engineers prüfen generierte Policies → approve/reject/change
- **Accuracy**: GPT-4o erreicht 70-73% bei Input/Output Classification → "first-line defense"
- **SLMs für Enforcement**: Kleine Modelle (Qwen 1.7B, Gemma 1B) können Policies durchsetzen → low latency

### Key Design Decisions
- Input Classifier + Output Auditor als getrennte Komponenten
- JSON-Output mit binärer Klassifikation (ID/OOD) + Begründung
- Ambiguous cases → flagged for human review (→ HYBRID-Modus!)
- Provenance + Traceability + Audit Logging integriert

## 2. Implikationen für D_GATE_INCLUSION_RULE

### D2-Entscheidungslogik (abgeleitet von Kholkar)
```
WENN Requirement → maschinenauswertbare Regel formulierbar:
  UND Policy-Tree aus Requirement ableitbar:
  UND Akzeptanzkriterium binär (ALLOW/BLOCK/ALERT):
  → D2 = VOLL AUTOMATISIERBAR (Policy-as-Code/Policy-as-Prompt Gate)

WENN Requirement → teilweise maschinenauswertbar:
  UND einige Aspekte binär, andere qualitativ:
  → D2 = HYBRID (Auto-Check + Human Review für Ambiguous Cases)

WENN Requirement → rein qualitative Bewertung nötig:
  UND kein binäres Kriterium definierbar:
  → D2 = NICHT AUTOMATISIERBAR (Governance-Gate)
```

### Mapping auf unsere Architektur
| Kholkar-Konzept | Unser Gate-Konzept | Beispiel |
|----------------|-------------------|---------|
| Policy Tree → Prompt Classifier | Automated Gate Check | R003 Data Governance: Datenqualitäts-Checks |
| Human-in-the-Loop Review | Hybrid Gate | R004 Human Oversight: Existenz auto, Qualifikation manuell |
| Security Engineer Approval | Manual Gate | R001 Risk Management: Qualitative Risikobewertung |
| ALLOW/BLOCK/ALERT Actions | Gate-Ergebnis | Pass/Fail/Flag-for-Review |

## 3. Limitationen für unseren Kontext
- Evaluiert nur in HR/SOC Domänen, nicht AI-Act-spezifisch
- 70-73% Accuracy → für Safety-Critical Gates möglicherweise unzureichend
- Fokus auf Prompt-Injection/Toxicity, nicht auf regulatorische Conformity
- Keine Integration mit CI/CD Pipeline (nur Runtime)

## 4. Schlüsselzitate für Section 5.2.2
- "the 'policy-to-practice' gap: it's easy for a human to write a rule [...] incredibly hard to turn that simple English sentence into a machine-enforceable rule" (S. 1)
- "treats policies as executable prompts (a policy-as-code for agents)" (Abstract)
- "complete provenance, traceability, and audit logging, all integrated with a human-in-the-loop review process" (Abstract)
- "The system acts as a 'default-deny' guardrail [...] flagging ambiguous cases for human review" (S. 4)

## 5. Verbindung zu anderen Papers
- **Muhammad et al. (2026)**: Audit-as-Code ergänzt Policy-as-Prompt um CI/CD-Integration
- **Nweke & Yeng (2026)**: Compliance-as-Code liefert Clause-to-Control Mapping
- **Sarathe et al. (2025)**: Policy-as-Code als übergeordnetes Paradigma
- **Laux (2024)**: Human-in-the-Loop Review = First-Degree Oversight der Policy-Generierung
