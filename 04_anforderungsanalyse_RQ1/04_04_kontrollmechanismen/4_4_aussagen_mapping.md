# 4.4 Aussagen-Quellen-Mapping — Kontrollmechanismen

## Qualitätsbewertung der Quellen

| Quelle | Venue | Indexierung | Rolle |
|--------|-------|-------------|-------|
| Ray (2026) | Expert Systems w/ Applications, Wiley | Scopus/WoS | **Primär-Anker** |
| Buscemi et al. (2025) | Preprint, aber 2D Verification Space | — | Sekundär (Methodik-Konvergenz) |
| Kovac et al. (2025) | arXiv, Position Paper, CERTAIN-Projekt | — | Konvergent (RegOps-Konzept) |
| Romeo et al. (2025) | arXiv, ARPaCCino | — | Konvergent (PaC-Implementierung) |
| Sardana et al. (2024) | JAIGS (nicht Scopus/WoS) | — | Nur ergänzend, nie alleinig |
| EU AI Act (2024) | Normtext | — | Normative Grundlage |

## Aussagen-Mapping

### These 1: Policy-as-Code als Kontrollmechanismus
**Behauptung**: Policy-as-Code (PaC) kodiert regulatorische Anforderungen als maschinenlesbare, automatisch durchsetzbare Regeln in CI/CD-Pipelines.
- **Primär**: Ray (2026), S. [Zeile 346]: "AI TRiSM integrates policy-as-code engines directly into CI/CD workflows, automating checks for bias thresholds, privacy guardrail enforcement, and completeness of documentation prior to any production release"
- **Konvergent**: Romeo et al. (2025), ARPaCCino: LLM+RAG generiert Rego-Regeln aus natürlicher Sprache für OPA-Integration
- **Konvergent**: Ray (2026), S. [Zeile 264]: "Policy-as-code frameworks—such as Open Policy Agent—codify organisational rules"

### These 2: RegOps als CI/CD-analoge Compliance-Pipelines
**Behauptung**: Regulatory Operations (RegOps) überträgt DevOps-Prinzipien auf Compliance-Workflows und ermöglicht kontinuierliche, automatisierte Konformitätsprüfungen.
- **Primär**: Kovac et al. (2025): "regulatory operations (RegOps) workflows to operationalize compliance requirements" + "CI/CD-like compliance pipelines"
- **Konvergent**: Ray (2026), S. [Zeile 693]: "Policy-as-code repositories codify governance rules, automatically validating artefacts during CI/CD pipelines"
- **Konvergent**: Sardana et al. (2024): "Compliance-as-Code 2.0" — NLP für Regulierungstext-Parsing → ausführbaren Code

### These 3: Continuous Monitoring für Drift und Compliance
**Behauptung**: Kontinuierliches Monitoring erfasst Modell-Drift, Performance-Degradation und Compliance-Abweichungen in Echtzeit.
- **Primär**: Ray (2026), S. [Zeile 250]: "Continuous Observability Integrates With Prometheus, Grafana [...] to Monitor Both Infrastructure Metrics and Model-Specific KPIs"
- **Primär**: Buscemi et al. (2025), S. [Zeile 82]: "continuous monitoring and post-deployment evaluation rather than reliance on [static assessment]"
- **Normativ**: EU AI Act Art. 9 Abs. 2 lit. b → Risikomanagement als iterativer Prozess

### These 4: Audit Trails und Evidenzartefakte
**Behauptung**: Manipulationssichere Audit Trails schaffen die Evidenzbasis für interne Audits und externe Konformitätsbewertungen.
- **Primär**: Buscemi et al. (2025), M1.7: "Audit trails — Ensure that system actions and decisions are recorded in tamper-evident logs for traceability"
- **Primär**: Ray (2026), S. [Zeile 346]: "Centralised registries store Model Cards, Data Sheets, audit trails, and versioned artefacts"
- **Konvergent**: Kovac et al. (2025): "ontology-driven data lineage tracking to ensure traceability and accountability"

### These 5: Automatisierung reduziert Audit-Aufwand
**Behauptung**: Automatisierte Kontrollmechanismen reduzieren den manuellen Audit-Aufwand signifikant.
- **Primär**: Ray (2026), S. [Zeile 346]: "significantly reducing manual audit overhead"
- **Konvergent**: Sardana et al. (2024): "74% manual audit reduction" — ACHTUNG: JAIGS, Zahl nur als Illustration, nicht als harte Evidenz verwenden
- **Konvergent**: Kovac et al. (2025): "compliance assessment models that automate validation"

## Entscheidungen-Check
- D_2026: Ray (2026) = Wiley/peer-reviewed, KEIN Preprint → nicht unter D_2026 (betrifft Butt/Leon). ABER: Sardana nur konvergent. ✓
- D_GATE_IDS_LOCATION: Keine Gate-IDs in 4.4, nur konzeptionell → ✓
- Sardana (JAIGS): Nie alleinige Quelle, immer mit Ray oder Buscemi kombiniert → ✓
- Romeo (arXiv): Nur als konvergente Implementierungs-Evidenz → ✓
