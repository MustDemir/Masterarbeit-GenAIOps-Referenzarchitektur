# Cloud-native Referenzarchitektur fuer GenAIOps mit Quality-Gate-Kontrollsystem

**Zur lifecycle-integrierten Operationalisierung regulatorischer, technischer und strategischer Anforderungen — auf Basis des EU AI Act**

Masterarbeit | Mustafa Demir | SRH Fernhochschule — The Mobile University | 2026

[![Validate Structure](https://github.com/MustDemir/Masterarbeit-GenAIOps-Referenzarchitektur/actions/workflows/validate-structure.yml/badge.svg)](https://github.com/MustDemir/Masterarbeit-GenAIOps-Referenzarchitektur/actions/workflows/validate-structure.yml)

---

## Einleitung

Die rasante Adaption generativer KI (GenAI) und Large Language Models (LLMs) stellt Unternehmen vor operative Herausforderungen, die ueber den Wirkungsbereich etablierter MLOps-Verfahren hinausgehen. Bestehende CI/CD-Pipelines decken die spezifischen Risiken stochastischer Modelle — etwa Halluzinationen, Promptabhaengigkeit oder kontextabhaengige Qualitaetsschwankungen — nicht systematisch ab (Sinha et al., 2024). Zugleich fordert der EU AI Act (VO 2024/1689) fuer Hochrisiko-KI-Systeme eine lueckenlose Nachweisfuehrung entlang des gesamten Lebenszyklus, fuer die weder operativ integrierte Frameworks noch automatisierte Kontrollmechanismen existieren.

Dieser Befund laesst sich entlang dreier interdependenter Problemdimensionen konkretisieren.

## Problemdimensionen

| # | Dimension | Forschungsluecke |
|---|-----------|-----------------|
| PD1 | **Fragmentierung bestehender Operationalisierungsframeworks** | Luecke 1: Es fehlt eine integrierte Referenzarchitektur, die den GenAI-Lifecycle end-to-end abdeckt und phasenuebergreifende Kontrollmechanismen ermoeglicht. |
| PD2 | **Methodische Inadaequanz bestehender Qualitaetssicherungsmechanismen** | Luecke 2: Fuer generative KI-Systeme existieren keine formalisierten, automatisierbaren Kontrollpunkte (Quality Gates), die Phasenuebergaenge an pruefbare Qualitaetskriterien und nachweisbare Evidenz binden. |
| PD3 | **Compliance-Operationalisierungsluecke (EU AI Act)** | Luecke 3: Ein systematischer Ansatz, der AI-Act-spezifische Pflichten konsistent in Policy-/Compliance-as-Code ueberfuehrt und ueber den GenAI-Lifecycle als automatisierte Quality Gates orchestriert, ist in der bestehenden Literatur nicht dokumentiert. |

*Synthese:* Die dreifache Luecke — strukturell, methodisch, regulatorisch — begruendet den Bedarf an einer integrierten Enterprise-Referenzarchitektur, die cloud-native GenAIOps-Praktiken mit automatisierten Quality Gates verbindet und die Anforderungen des EU AI Act als pruefbare Kontrollmechanismen in CI/CD/CT-Pipelines operationalisiert.

## Zielsetzung

Ziel der Arbeit ist die Entwicklung einer cloud-nativen Referenzarchitektur fuer GenAIOps, die regulatorische, technische und strategische Anforderungen — unter besonderer Beruecksichtigung des EU AI Act (VO 2024/1689) — durch ein lifecycle-integriertes Quality-Gate-Kontrollsystem systematisch operationalisiert.

Die Architektur verfolgt den Ansatz **Accountability-by-Design**: Verantwortungsnachweisbarkeit wird nicht als nachgelagerter Dokumentationsprozess verstanden, sondern als technisch erzwungene Eigenschaft des Systems.

### Vier Saeulen des Artefakts

| Saeule | Bezeichnung | Kern |
|--------|-------------|------|
| S1 | Architekturelle Grundstruktur | Schichten- und Komponentenmodell, IaC-Integration |
| S2 | Quality-Gate-Kontrollsystem (USP) | Praeventive, detektive und evidenzbasierte Gate-Typen |
| S3 | Pipeline-Integration | CI/CD/CT-Einbettung, GitOps, Policy-as-Code |
| S4 | Evidence- und Audit-Logik (USP) | Lueckenlose Nachweisfuehrung, Immutable Storage |

### Design-Prinzipien (DP1–DP5)

- **DP1 — Compliance als kontrollierbarer Lifecycle-Prozess:** Normative Anforderungen werden nicht punktuell geprueft, sondern als durchgaengiger, Gate-basierter Kontrollprozess ueber den gesamten GenAI-Lifecycle operationalisiert.
- **DP2 — Lueckenlose Traceability-Kette:** Jede High-Risk-Anforderung wird in eine Policy uebersetzt, die automatisch oder manuell Evidenz erzeugt, die auditierbar verknuepft ist (R → DP → Gate → Evidence).
- **DP3 — Gate-Template als Standardisierungseinheit:** Jedes Quality Gate wird durch ein einheitliches Template formalisiert (Trigger, Kriterien, Evidenzartefakte, Entscheidung, Verantwortlichkeit, Audit Trail, Waiver-Regelung).
- **DP4 — Trennung von Governance-Ebenen, integrierte Entscheidung:** Strategische, technische und Compliance-Gates werden getrennt modelliert, aber ueber gemeinsame Artefakte und Entscheidungslogik gekoppelt.
- **DP5 — Cloud-native Integrierbarkeit:** Das Kontrollsystem muss in bestehende cloud-native CI/CD/CT-Toolchains integrierbar sein, ohne proprietaere Abhaengigkeiten zu erzeugen.

## Forschungsfragen

- **RQ1 (Relevance):** Welche regulatorischen, technischen und strategischen Anforderungen sind fuer eine verantwortungsnachweisbare Gestaltung von GenAI-Systemen im Enterprise-Kontext relevant und operationalisierbar?
- **RQ2 (Design):** Wie kann eine Referenzarchitektur fuer GenAIOps gestaltet werden, die die erhobenen Anforderungen durch ein lifecycle-integriertes Quality-Gate-Kontrollsystem systematisch operationalisiert? *(Nur Deployment- und Inference-Zyklus)*
- **RQ3 (Rigor):** Inwiefern ist die entwickelte Referenzarchitektur geeignet, regulatorische Anforderungen technisch durchzusetzen und auditierbar nachweisbar zu machen?

## Methodik

**Design Science Research** (DSR) mit drei kombinierten Rahmenwerken:

1. **Hevner et al. (2004)** — IS Research Framework mit drei Zyklen: Relevance, Design, Rigor
2. **Peffers et al. (2007)** — DSRM-Prozess (6 Schritte), problem-centered
3. **vom Brocke & Maedche (2019)** — DSR Grid zur systematischen Abdeckung aller DSR-Dimensionen

```
[1] Problem          [2] Objectives        [3] Design &         [4] Demonstration
 Identification  -->   Definition      -->   Development     -->  (Walkthrough +
                                              (Architektur)       PoC)

                                                              --> [5] Evaluation     --> [6] Communication
                                                                  (Coverage Check,       (Thesis +
                                                                   Expert Interviews)     Repository)
```

**Artefakttyp:** Model (Architektur) + Method (Gate-Systematik) + Instantiation (PoC)

**Zwei Iterationen:** Iteration 1 entwickelt das konzeptuelle Architekturmodell und die Gate-Systematik; Iteration 2 instanziiert die Architektur als Azure-basierten Proof-of-Concept.

**Evaluation (dreistufig):**
1. **Requirements-Coverage-Matrix:** Systematischer Abgleich R1–Rn gegen Architekturkomponenten
2. **PoC-Walkthrough:** Technische Demonstration im Azure-Stack (Ambient AI Scribe)
3. **Expert-Reviews (n>=4):** Leitfadengestuetzte Interviews mit Domaenenexperten aus MLOps/GenAIOps, Cloud-Architektur und KI-Governance

## Scope und Abgrenzung

Die Referenzarchitektur wird als **generisches Modell** entwickelt, das branchenunabhaengig anwendbar ist. Die prototypische Instanziierung (PoC) erfolgt in der **Healthcare-Domaene** am Beispiel eines **Ambient AI Scribe** — eines generativen KI-Systems zur automatisierten Transkription und Zusammenfassung medizinischer Gespraeche.

**Warum dieses Szenario:** (1) Hochrisiko-KI-System gemaess EU AI Act Annex III, (2) sensible Gesundheitsdaten unter DSGVO und KI-Regulierung, (3) hoechste Qualitaetsanforderungen an generative Outputs, (4) umfassende Nachweispflichten.

**PoC-Stack:** Microsoft Azure (AKS, Azure OpenAI Service, ArgoCD, OPA/Rego, Azure Monitor, Azure PostgreSQL, Blob Storage immutable)

**Hybrider Evidence Store:** Der Evidence Store trennt unstrukturierte Artefakte (Model Cards, Evaluierungsreports → Azure Blob Storage immutable) von strukturierten Quality-Gate-Metadaten (→ relationale SQL-Datenbank). Diese Trennung ermoeglicht performantes Compliance-Reporting ueber indizierte Abfragen und stellt durch datenbankgestuetzte Schutzmechanismen (Immutability-Trigger, View-basierte Zugriffskontrolle, Least-Privilege-Rollen) die Manipulationssicherheit der Audit-Nachweise sicher. Im Healthcare-Kontext wird dadurch die strikte Trennung zwischen medizinischer Payload (verschluesselte Transkripte) und regulatorischer Telemetrie (Compliance-Metadaten) gewaehrleistet — eine zentrale Voraussetzung nach DSGVO Art. 9.

**Explizit ausserhalb des Scope:** LLM-Training/Fine-Tuning, eigenstaendige Modellentwicklung, Optimierung von Data-Engineering-Pipelines, juristische Vollstaendigkeitsanalyse.

## Quality-Gate-Framework

Drei Dimensionen automatisierter Kontrollpunkte entlang des GenAI-Lebenszyklus:

**Strategische Gates** — Lifecycle Governance
- Phase-Transition-Approvals, Business-Impact-Assessment, Risk Classification

**Technische Gates** — Qualitaet, Performance, Safety
- Halluzinations-Rate, Retrieval Precision, Prompt-Injection-Tests, Latency SLOs, Toxicity Checks

**Compliance Gates** — EU AI Act als Policy-as-Code
- Art. 9 Risikomanagement | Art. 10 Daten-Governance | Art. 11 Technische Dokumentation
- Art. 12 Protokollierung | Art. 13 Transparenz | Art. 14 Menschliche Aufsicht | Art. 15 Robustheit

Jedes Gate folgt einem einheitlichen Template:

```
Gate:      [Name]
Trigger:   [Ausloesender Event / Pipeline-Stage]
Evidence:  [Erforderliche Artefakte / Metriken]
Policy:    [Pruefregeln als Code]
Decision:  [Pass / Fail / Waiver]
Audit:     [Evidence-Log + Timestamp + Owner]
```

## Traceability-Kette

Die durchgaengige Nachweiskette — ein zentrales USP der Arbeit — verknuepft jede regulatorische Anforderung bis zum auditierbaren Nachweis:

```
R (Requirement) --> DP (Design Principle) --> Gate (Quality Gate) --> Evidence (Audit Trail)
```

Jede High-Risk-Anforderung (R) wird ueber Design-Prinzipien (DP) zu konkreten Quality Gates und deren Evidenzartefakten zurueckverfolgbar gemacht. Die formale Abbildung erfolgt als Requirements-Traceability-Matrix in Kapitel 5.

## Tech Stack

| Bereich | Technologien |
|---|---|
| **Cloud-native Platform** | Kubernetes, Helm, ArgoCD (GitOps), Terraform (IaC) |
| **GenAI / LLM Operations** | LangChain, LlamaIndex, vLLM, Hugging Face, RAG Pipelines |
| **Evaluation & Testing** | DeepEval, RAGAS, Giskard, Promptfoo |
| **Policy-as-Code** | Open Policy Agent (OPA/Rego), Kyverno |
| **Observability** | OpenTelemetry, Prometheus, Grafana, Langfuse |
| **CI/CD/CT** | GitHub Actions, Tekton, Policy-Engine-Integration |
| **Security** | Vault (Secrets), Falco (Runtime), RBAC/ABAC |
| **Governance** | Evidence Store (Azure PostgreSQL + Blob Storage immutable), Audit Trail DB, Compliance Dashboard |
| **Programmierung** | Python, SQL, YAML, Rego, HCL |

## Architektur-Preview

![Methoden-Framework](03_forschungsdesign_methodik/images/work/Methoden-Framework:%20Forschungsmethode%20%C3%97%20Technische%20Konstruktionsmethoden%20%20.png)
![KI-Fabrik-Analogie](05_referenzarchitektur_RQ2/05_02_architekturuebersicht/images/work/Die%20KI-Fabrik:%20Referenzarchitektur%20als%20Analogie%20(PoC)%20%20.png)


## Repo-Struktur

```
.
|-- 00_workspace/              # Operativer Einstiegspunkt (Pointer auf Single-Truth-Quellen)
|-- 00_admin/
|   |-- gliederung_v3.md      # Verbindliche Kapitelstruktur (Single Source of Truth)
|   |-- asset_naming.md       # PNG-Naming/Versionierungsstandard (v01, v02, ...)
|   |-- SOURCE_OF_TRUTH.md    # SOT-Regeln
|-- 01_einleitung/
|-- 02_rigor_theorie_stand_forschung/
|-- 03_forschungsdesign_methodik/
|-- 04_anforderungsanalyse_RQ1/  # Design-getriebene Operationalisierung (Design Cycle Phase 1)
|-- 05_referenzarchitektur_RQ2/
|   |-- 05_03_quality_gates/
|   |-- 05_04_pipelines_integration/
|-- 06_evaluation_RQ3/
|-- 07_diskussion/
|-- 08_fazit_ausblick/
|-- 09_technische_infrastruktur/   # Workflow/Automation/Azure-Setup
|-- poc/                           # Proof-of-Concept (S1-S4 Instanziierung, ab Iter. 2)
|-- 90_sources_zotero/
|-- docs/expose/                   # Expose v4 (PDF, Single Source of Truth)
```

## Architektur-Dokumente (Source of Truth)

- [Aktuelle Gliederung v3](00_admin/gliederung_v3.md)
- [Architektur-Kapitel (RQ2)](05_referenzarchitektur_RQ2/)
- [Quality-Gate-Artefakte](05_referenzarchitektur_RQ2/05_03_quality_gates/)
- [Pipeline-Integration](05_referenzarchitektur_RQ2/05_04_pipelines_integration/)
- [Evaluation (RQ3)](06_evaluation_RQ3/)
- [Expose v4 FINAL (PDF, verschluesselt)](docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf)
- [Source-of-Truth Regeln](00_admin/SOURCE_OF_TRUTH.md)

## Fortschritt

> Fortschritt wird automatisch jeden Montag aktualisiert. Aendere `_status.yml` (oder starte Workflow mit save.py) im jeweiligen Kapitelordner, um den Fortschritt zu pflegen.

<!-- PROGRESS-START -->
> Gesamtfortschritt: `██████░░░░░░░░░░░░░░` **30%**

| Kapitel | Fortschritt | % | Status |
|---------|------------|---|--------|
| Expose v4 / Forschungsdesign | `████████████████████` | 100% | Abgeschlossen |
| Kap. 1 — Einleitung | `██░░░░░░░░░░░░░░░░░░` | 10% | Entwurf |
| Kap. 2 — Theorie & Grundlagen | `███░░░░░░░░░░░░░░░░░` | 15% | In Arbeit |
| Kap. 3 — Methodik (DSR) | `███████████████████░` | 95% | review |
| Kap. 4 — Anforderungsanalyse (RQ1) | `███████████░░░░░░░░░` | 55% | in_progress |
| Kap. 5 — Referenzarchitektur (RQ2) | `████░░░░░░░░░░░░░░░░` | 20% | In Arbeit (Evidence Store, Related Work) |
| Kap. 6 — Evaluation (RQ3) | `░░░░░░░░░░░░░░░░░░░░` | 0% | Geplant |
| Kap. 7 — Diskussion | `░░░░░░░░░░░░░░░░░░░░` | 0% | Geplant |
| Kap. 8 — Fazit & Ausblick | `░░░░░░░░░░░░░░░░░░░░` | 0% | Geplant |
| PoC-Implementierung | `░░░░░░░░░░░░░░░░░░░░` | 0% | Geplant |
<!-- PROGRESS-END -->

## Zitierung

Dieses Repository kann ueber die Datei [`CITATION.cff`](CITATION.cff) zitiert werden. GitHub zeigt automatisch einen "Cite this repository"-Button an.

## Lizenz

Dieses Repository steht unter der [CC-BY-NC-4.0](LICENSE) Lizenz. Siehe [`LICENSE`](LICENSE) fuer Details.

## Kontakt

**Mustafa Demir** — SRH Fernhochschule, M.Sc. Digital Management und Transformation

[![GitHub](https://img.shields.io/badge/GitHub-MustDemir-181717?style=flat&logo=github)](https://github.com/MustDemir)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mustafa%20Demir-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/mustafa-demir-331900202/)
[![Website](https://img.shields.io/badge/Website-mustafa--demir.com-4285F4?style=flat&logo=googlechrome&logoColor=white)](https://mustafa-demir.com)
[![E-Mail](https://img.shields.io/badge/E--Mail-kontakt%40mustafa--demir.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:kontakt@mustafa-demir.com)
