# Deep Reading: Feng et al. (2024) — Normative Requirements Operationalization with LLMs
**Relevance: D1 MEDIUM (Requirements Operationalisierung) + D2 LOW**
**Date: 2026-03-12 | Phase 2 Deep Reading**

## 1. Kernbeitrag

### RAINCOAT Framework
- Elicitation + Validation normative Requirements (SLEEC: Social, Legal, Ethical, Empathetic, Cultural)
- LLM-basierte Extraktion semantischer Relationen zwischen System-Capabilities
- Automatisierte Erkennung von Well-Formedness Issues (WFIs): Konflikte, Redundanzen, Insufficiency, Over-Restrictiveness
- SLEEC-Sprache: "when Trigger then Response" Pattern für normative Regeln

### SLEEC-Regelstruktur
```
when [Event] and [Condition] then [Response] within [Deadline]
  unless [Defeater] then [Alternative Response]
  otherwise [Fallback Response]
```

## 2. Relevanz für D_GATE_INCLUSION_RULE

### D1: Requirements-Formalisierung
- Zeigt WIE normative Requirements formalisiert werden können
- SLEEC = maschinenlesbare Sprache für SLEEC-Normen → Brücke zwischen Rechtstext und Code
- WFI-Erkennung: Konflikte zwischen Requirements automatisch identifizierbar
- ABER: Fokus auf NORMATIVE Requirements (Verhalten), nicht auf Dokumentations-/Compliance-Requirements

### D2: Teilweise relevant
- LLM-basierte Semantik-Extraktion → teilautomatisierbar
- Human-in-the-Loop: Stakeholder müssen Relationen validieren
- Automated Reasoning für Konflikterkennung

### Einordnung in unser Framework
| Feng-Konzept | Gate-Relevanz | Bewertung |
|-------------|--------------|-----------|
| SLEEC Rules | Formalisierung von Gate-Akzeptanzkriterien | INDIREKT — zu abstrahiert für direkte Gate-Checks |
| WFI Detection | Prüfung ob Requirements-Set widerspruchsfrei | NÜTZLICH für Requirements-Analyse (Kap. 4) |
| LLM-Semantik | Automatisierung semantischer Prüfungen | EXPERIMENTELL — keine produktionsreife Pipeline |

## 3. Fazit für D_GATE_INCLUSION_RULE
- **Beitrag**: Zeigt dass Requirements formalisiert und auf Konsistenz geprüft werden können
- **Gap**: Kein direkter Bezug zu Quality Gates oder CI/CD-Integration
- **Nutzung**: SEKUNDÄRQUELLE für Requirements-Formalisierung in Kap. 4, nicht primär für Gate-Entscheidung
- **Keine Schlüsselquelle für Section 5.2.2** — eher Hintergrund für Requirements Engineering

## 4. Schlüsselzitat
- "bridging the gap between the explicit formalization of NRs and the implicit understanding and assumptions of non-technical stakeholders" (S. 2)
