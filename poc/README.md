# Proof of Concept

Prototypische Implementierung zur Evaluation der Referenzarchitektur (RQ3).

## Komponenten

### technical-gate/
Technisches Quality Gate: Automatisierte Evaluation von GenAI-Outputs
- Halluzinations-Erkennung
- Retrieval-Quality-Metriken (RAGAS)
- Safety/Toxicity Checks
- Latency SLO Validation

### compliance-gate/
Compliance Gate: EU AI Act als Policy-as-Code
- OPA/Rego Policies fuer Art. 9-15
- Evidence Collection und Audit Trail
- Automatisierte Compliance-Checks in CI/CD

### infrastructure/
Cloud-native Infrastruktur (deployment-agnostisch)
- Kubernetes Manifeste
- Terraform Module
- GitOps Konfiguration (ArgoCD)
