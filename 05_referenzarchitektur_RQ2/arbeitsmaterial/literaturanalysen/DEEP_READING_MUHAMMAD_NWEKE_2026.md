# Deep Reading: Muhammad et al. (2026) + Nweke & Yeng (2026) — D2 Core Papers
**Date: 2026-03-12 | Phase 2 Deep Reading**

---

## A. Muhammad et al. (2026) — Audit-as-Code
**Relevance: D2 CRITICAL (Automatisierbarkeits-Dimension)**
**Quelle**: Frontiers in Artificial Intelligence, 9, 1759211. DOI: 10.3389/frai.2026.1759211

### Kernbeitrag
- **Audit-as-Code**: Governance Requirements → technically-auditable rules → CI/CD gate decisions
- **Pipeline**: Policy Specification (versioned) → Evidence Collectors (lightweight) → Gate Evaluation → PASS/WARN/BLOCK
- **Assured Readiness Score**: Quantifiziert Governance-Risiko + Traceability + Explainability
- **Fix-It Guidance**: Bei WARN/BLOCK → maschinenlesbare Remediation-Hinweise

### Direkte D2-Relevanz (HÖCHSTE ALLER PAPERS)
| Muhammad-Konzept | Gate-Mapping | D2-Bewertung |
|-----------------|-------------|-------------|
| Versioned Policy Specification | Gate-Akzeptanzkriterien als Code | VOLL AUTOMATISIERBAR |
| Lightweight Evidence Collectors | Artefakt-Sammlung aus Pipeline | VOLL AUTOMATISIERBAR |
| Non-interactive Gate in CI/CD | Quality Gate als Pipeline-Stage | VOLL AUTOMATISIERBAR |
| PASS/WARN/BLOCK Output | Gate-Ergebnis (Go/Hold/Kill) | VOLL AUTOMATISIERBAR |
| Fix-It Guidance | Remediation bei Fail | HYBRID (Auto-Suggestion + Human Fix) |
| Assured Readiness Score | Quantitative Deployment-Entscheidung | AUTOMATISIERT mit Risk-Tier |

### Zentrale Erkenntnis für D_GATE_INCLUSION_RULE
Muhammad liefert den **konkreten Beweis** dass regulatorische Gate-Entscheidungen in CI/CD automatisierbar sind:
- "turning requirements into deterministic checks and gate decisions integrated in operational workflows"
- "governance regulations mapped from theoretical/in-principle guidelines to ad-hoc quantifiable interpretations"
- 3 Entscheidungs-Ergebnisse: **PASS** (proceed) / **WARN** (needs attention) / **BLOCK** (cannot proceed)
  → Direkte Analogie zu Cooper's Go/Hold/Kill!

### Gap: Keine EU-AI-Act-spezifische Evaluation (generisches Framework)

---

## B. Nweke & Yeng (2026) — Compliance-as-Code
**Relevance: D2 HIGH + Q HIGH (Querschnitt: Traceability)**
**Quelle**: IEEE Access, 14, 28258-28281. DOI: 10.1109/ACCESS.2026.3665991

### Kernbeitrag
- **Compliance-as-Code** für AI-Driven Identity Systems
- **Clause-to-Control Traceability**: Regulatorische Klausel → Technischer Control → Evidence
- **OSCAL-native** Packages: Component Definition, System Security Plan, Assessment Results, POA&M
- **Technologie-Stack**: OPA/Rego (Policy-as-Code), Conftest (CI Testing), Evidence Graph

### 3 Schlüsseleigenschaften
1. **Clause-to-Control Traceability** unter Policy-Evolution
2. **Evidence Completeness** als enforceable Property (Silence = Non-ambiguous)
3. **OSCAL-Export** mit hash-linked Evidence Resources

### Direkte Relevanz für D_GATE_INCLUSION_RULE
| Nweke-Konzept | Gate-Mapping | Dimension |
|-------------|-------------|-----------|
| Clause-to-Control | R_xx → Gate-Check Mapping | Q (Querschnitt-Traceability) |
| OPA/Rego Policies | Automatisierte Policy-Checks | D2 (voll automatisierbar) |
| Evidence Graph | Audit-Trail mit Hashes | D2 + Q |
| OSCAL Packages | Standardisierte Compliance-Dokumentation | Q (übergreifend) |
| POA&M (auto-generated) | Remediation bei Gaps | D2 (HYBRID) |

### Zentrale Erkenntnis
Nweke löst das **Traceability-Problem**: Wie verbindet man regulatorische Klauseln mit technischen Controls UND machine-readable Evidence? → OSCAL als Standard-Format

---

## C. Synthese: Muhammad + Nweke für D_GATE_INCLUSION_RULE

### D2-Entscheidungslogik (konsolidiert)
```
WENN Requirement → Policy-as-Code formulierbar (OPA/Rego):
  UND Evidence automatisch sammelbar (Collectors):
  UND Akzeptanzkriterium deterministisch (PASS/WARN/BLOCK):
  → D2 = VOLL AUTOMATISIERBAR
  → Implementierung: Muhammad's Audit-as-Code Gate in CI/CD
  → Evidence: Nweke's OSCAL-Package mit Clause-to-Control Traceability

WENN Requirement → Policy teilweise formulierbar:
  UND Evidence-Sammlung nur teilweise automatisch:
  → D2 = HYBRID
  → Implementierung: Auto-Check + Human Review (Fix-It Guidance)
  
WENN Requirement → keine maschinenauswertbare Policy:
  → D2 = NICHT AUTOMATISIERBAR
  → Implementierung: Manuelles Governance-Gate
```

### Mapping: Muhammad/Nweke → Cooper → Laux
| Muhammad | Cooper | Laux | Unser Framework |
|----------|--------|------|----------------|
| PASS | Go | Second-Degree (corrective OK) | Gate bestanden |
| WARN | Hold | Hybrid: Auto-Flag + Human Review | Gate bedingt bestanden |
| BLOCK | Kill | First-Degree nötig (counterfactual) | Gate nicht bestanden |
| Evidence Bundle | Deliverables | Transparency Principle | Gate-Artefakte |
| Readiness Score | Should-meet Scoring | Justification Principle | Quantitative Bewertung |
| Fix-It Guidance | Action Plan | Accountability Principle | Remediation |
