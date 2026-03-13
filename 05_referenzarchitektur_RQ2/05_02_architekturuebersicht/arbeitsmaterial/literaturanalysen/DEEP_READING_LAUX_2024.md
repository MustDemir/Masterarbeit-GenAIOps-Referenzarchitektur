# Deep Reading: Laux (2024) — Institutionalised Distrust and Human Oversight of AI
**Relevance: D3 PRIMARY (Oversight-Typ-Dimension)**
**Date: 2026-03-12 | Phase 2 Deep Reading**

## 1. Kernbeitrag für D_GATE_INCLUSION_RULE

### First-Degree vs. Second-Degree Oversight (→ D3)
| Merkmal | First-Degree | Second-Degree |
|---------|-------------|---------------|
| Einfluss | Counterfactual influence auf Output | Kein counterfactual influence |
| Timing | VOR/WÄHREND Entscheidung | NACH Entscheidung (ex post) |
| Funktion | Constitutive (konstitutiv) | Corrective (korrektiv) |
| Beispiele | Arzt mit AI-Diagnose, Content-Moderator | Audits, Reviews, Appeals, Oversight Board |
| Art. 14 AIA | Deployer führt Oversight aus | Conformity Assessment, Notified Bodies |
| Automation | Teilautomatisiert (AI=Decision Support) | Auch bei voll automatisierten Systemen |

### 2x2-Matrix (Table 1, S. 2857)
|  | First-Degree | Second-Degree |
|--|-------------|---------------|
| **Fully automated** | *AI Development (case-by-case) | Reviews, Audits, Appeals |
| **Partially automated** | *AI Development + AI as Decision Support | Reviews, Audits, Appeals |

### 2x2 Challenges (Table 2, S. 2860)
|  | First-Degree | Second-Degree |
|--|-------------|---------------|
| **Lack of competence** | A | B |
| **Wrong incentives** | C | D |

## 2. Sechs Prinzipien Institutionalisierten Misstrauens (Sect. 5.2)

| # | Prinzip | Adressiert (A/B/C/D) | Kern |
|---|---------|---------------------|------|
| 1 | **Justification** | A, B, C, D | Empirischer Nachweis der Oversight-Effektivität. Kompetenz muss belegt werden. |
| 2 | **Periodical Mandates** | D (B negativ*) | Auditor-Rotation gegen Capture. ABER: untergräbt Kompetenzaufbau → Trade-off |
| 3 | **Collective Decisions** | A*, B*, C, D | Art. 14(5) AIA: Biometrik → min. 2 Personen. Diversity verbessert Urteil. |
| 4 | **Limited Competence** | B*, D | Separation of Powers. Vertikale Kontrolle zwischen 2nd-Degree Overseers. |
| 5 | **Justiciability & Accountability** | A, B, C, D | Beschwerderechte (Art. 63(11)), Haftung, Appeals als Accountability-Mechanismus |
| 6 | **Transparency** | A, B, C, D | Oversight-Design + Performance öffentlich. AI-assisted Oversight offenlegen. |

### Results-Matrix (Table 3, S. 2863)
- Alle Prinzipien adressieren C+D (wrong incentives) positiv
- A+B (competence) unsicherer — Periodical Mandates sogar negativ für B
- Prinzipien 2+4 gelten NUR für Second-Degree Oversight

## 3. Direkte Implikationen für D_GATE_INCLUSION_RULE

### D3-Entscheidungslogik (abgeleitet)
```
WENN Requirement → counterfactual influence auf AI-Output nötig:
  → First-Degree Oversight → Gate muss VOR Deployment prüfen
  → Beispiel: Art. 14(4) AIA "understand, interpret, override, interrupt"
  → Gate-Modus: HYBRID oder MANUELL (menschliches Urteil konstitutiv)

WENN Requirement → nur corrective/ex-post Prüfung:
  → Second-Degree Oversight → Gate kann POST-Deployment sein
  → Beispiel: Conformity Assessment, Monitoring, Audit
  → Gate-Modus: kann AUTOMATISIERT sein (Audit-Trail-Check)
```

### Schlüsselzitate für Section 5.2.2
- "Having counterfactual influence means that the initial output of an AI system could have been different due to human involvement" (S. 2857)
- "first-degree oversight is constituent to the outcome [...] second-degree oversight is corrective" (S. 2857-2858)
- Art. 14(1) AIA*Parliament: "thorough investigation after the fact" → Second-Degree
- Art. 14(4) AIA: "understand, interpret, override, interrupt" → First-Degree
- Recital 48 AIA: "necessary competence, training and authority"
- "Periodical mandates may undermine the competence of auditors" → Trade-off für Gate-Design

### Mapping auf unsere Requirements
| Requirement | Oversight-Typ | Begründung |
|-------------|--------------|------------|
| R004 (Human Oversight) | First-Degree | Art. 14(4): Override/Interrupt = counterfactual influence |
| R014 (Post-Market Monitoring) | Second-Degree | Ex post, corrective, kein Einfluss auf initialen Output |
| R001 (Risk Management) | First-Degree | Konstitutiv für System-Design-Entscheidungen |
| R010 (Conformity Assessment) | Second-Degree | Audit = corrective review |
| R013 (Incident Reporting) | Second-Degree | Reaktiv, nach Vorfall |

## 4. Offene Fragen / Gaps

1. **Operationalisierung fehlt**: Laux liefert normative Prinzipien, aber KEINE konkreten technischen Checks oder Policy-as-Code-Umsetzung → Gap für D2
2. **Qualifikationsstandards undefiniert**: "AIA demands competence but is underdefined on HOW" → unsere Architektur muss das schließen
3. **Shared Responsibility Provider/Deployer**: Art. 14 teilt Verantwortung → Gate muss beide Rollen adressieren
4. **AI-Augmented Oversight**: Laux fragt ob Oversight selbst AI nutzen darf → relevant für Automatisierungsentscheidung (D2)
