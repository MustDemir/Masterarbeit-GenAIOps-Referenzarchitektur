---
name: Quality Gate
about: Neues Quality Gate definieren oder bestehende Gate-Spezifikation verfeinern
title: "Gate: [Gate-Name]"
labels: S2-quality-gates
assignees: ''
---

## Gate-Spezifikation

**Gate-Name:** [Name]
**Dimension:** [Strategisch / Technisch / Compliance]
**Lifecycle-Phase:** [z.B. Pre-Deployment, Post-Deployment, Inference]

## Template

| Feld | Wert |
|------|------|
| **Trigger** | [Ausloesender Event / Pipeline-Stage] |
| **Kriterien** | [Pruefbare Bedingungen] |
| **Evidence** | [Erforderliche Artefakte / Metriken] |
| **Policy** | [Pruefregeln als Code — OPA/Rego, Kyverno, manuell] |
| **Decision** | [Pass / Fail / Waiver] |
| **Owner** | [Verantwortliche Rolle] |
| **Audit** | [Evidence-Log + Timestamp + Owner] |
| **Waiver** | [Waiver-Regelung, wenn zutreffend] |

## Traceability

- **Anforderung(en):** R-XX, R-YY
- **Design-Prinzip:** DP-X
- **EU AI Act Artikel:** [Art. X, wenn Compliance-Gate]

## Akzeptanzkriterien

- [ ] Gate-Template ist vollstaendig ausgefuellt
- [ ] Mindestens eine Anforderung ist zugeordnet
- [ ] Policy ist als Code formulierbar
- [ ] Evidenz-Artefakte sind spezifiziert
- [ ] Lifecycle-Phase ist korrekt zugeordnet
