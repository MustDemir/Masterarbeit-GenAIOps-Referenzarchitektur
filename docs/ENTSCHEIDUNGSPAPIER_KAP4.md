# Entscheidungspapier Kapitel 4 — Finalisierte Method Decisions

**Datum:** 2026-03-04
**Status:** Alle 5 Entscheidungen ABGESCHLOSSEN
**Kontext:** Gegenprüfung des Prüfberichts MD1–MD14 (5 BEDINGT-Bewertungen)

---

## Gesamtübersicht

| # | Thema | Status | Kern-Ergebnis |
|---|---|---|---|
| 1 | Art. 10 Abs. 6 Scope | ✅ FINAL | Out-of-Scope, 3-stufige Evidenz, eigener Abschnitt Kap. 4.1 |
| 2 | RAG-Grauzone | ✅ FINAL | Art. 13/15, Sub-Decision MD13, Limitation Kap. 4.1 + 7 + Ausblick |
| 3 | Jonnala-Methodik | ✅ FINAL | Konvergente Quelle, nicht alleinig, Einschränkung Kap. 4 + 7 |
| 4 | Huwyler Zotero | ✅ FINAL | Nachimportieren in Zotero |
| 5 | DSR MD10/11 | ✅ FINAL | Rückverweis Kap. 3.5/3.6 + Traceability-Tabelle erstellen |

---

## Entscheidung 1: Art. 10 Abs. 6 Scope

**These:** Art. 10 Abs. 1–5 (Training-Data-Governance) ist für GenAI-Deployer nicht operationalisierbar → Out-of-Scope. Nur Abs. 6 (Testdaten) bleibt in Scope.

### Evidence-Chain

**E1 — Normtext (primär):**
- Art. 10 Abs. 1–5 adressiert den Provider (Anbieter), der Trainingsdaten kontrolliert
- Art. 10 Abs. 6 regelt Testdaten separat → für Deployer operationalisierbar
- Art. 3 Nr. 4: Deployer ≠ Entwickler des Foundation Models

**E2 — Blueprint (intern, NICHT zitieren):**
- D30: Art. 10 Training-Data-Governance = Out-of-Scope
- D28: OPA = Metadata-Enforcement, nicht Content-Verification
- D29: Custom Facets = Runtime-RAG-Lineage, nicht Training-Data-Governance
- W2/D34: "Art. 10 ist der schwächste Compliance-Punkt"
- ⚠ Blueprint = interne Schreibvorarbeit, kein Peer-Review. Nur als interne Design-Entscheidung referenzierbar.

**E3 — Literatur (extern, zitieren):**
- Jonnala et al. (2025): AI Act hat signifikante Lücken bei GenAI — Fairness/Bias + Misinformation
- Buscemi et al. (2025): Data Governance Verification setzt Trainingsdaten-Zugang voraus
- Kovac et al. (2025): RegOps adressiert nur eigene ML-Pipelines, nicht fremde Foundation Models

**E4 — Strukturelles Argument:**
- Foundation Models = proprietäre Black Box für Deployer
- Art. 10 Abs. 2(b–e): Deployer kennt weder Erhebungsprozesse noch Vorverarbeitungsvorgänge
- Nicht Scope-Wahl, sondern technische Unmöglichkeit

### Umsetzung
- Eigener Abschnitt Kap. 4.1 (vor Requirements)
- Dreistufige Argumentation: normativ → technisch → Limitation
- Limitation ehrlich benennen: Compliance-Lücke, kein gelöstes Problem

### E5 — Grey-Literature-Validierung (Industrie/Praxis, zusätzliche Stützung)

| Quelle | Typ | Kern-Aussage | Zitierfähig? |
|---|---|---|---|
| **EU-Kommission GPAI Guidelines (Juli 2025)** | Offiziell | Art. 25 verlangt Kooperation Provider↔Deployer. Training-Data-Governance bleibt Provider-Pflicht. | ✅ Ja (Grey Lit.) |
| **OpenAI — Primer on EU AI Act** | Provider-Statement | Unterscheidet explizit Provider-Pflichten (Art. 53: Training Data Summary) von Deployer-Pflichten | ⚠ Nur als Referenz |
| **AI Act Newsletter #86 (Aug 2025)** | Fachpresse | GPT-5 bei Release ohne Training Data Summary + Copyright Policy — selbst Provider noch non-compliant | ⚠ Nur als Referenz |
| **Latham & Watkins — Deployer Obligations** | Law Firm Analysis | Art. 10 Training-Data-Governance wird nicht als Deployer-Pflicht gelistet. Deployer = Input-Datenqualität. | ✅ Ja (Grey Lit.) |
| **Mayer Brown — GPAI Rules (Aug 2025)** | Law Firm Analysis | GPAI-Provider müssen Training Data Summary nach AI Office Template veröffentlichen — nicht der Deployer | ✅ Ja (Grey Lit.) |

**Quellen-URLs:**
- EU-Kommission: https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers
- OpenAI: https://openai.com/global-affairs/a-primer-on-the-eu-ai-act/
- AI Act Newsletter #86: https://artificialintelligenceact.substack.com/p/the-eu-ai-act-newsletter-86-concerns
- Mayer Brown: https://www.mayerbrown.com/en/insights/publications/2025/08/eu-ai-act-news-rules-on-general-purpose-ai-start-applying-guidelines-and-template-for-summary-of-training-data-finalized

**Gegenargument-Prüfung:** Kein Gegenargument gefunden. Das stärkste potenzielle Gegenargument (Deployer wird zum Provider bei "substantial modification", Art. 25 Abs. 2) greift nicht für API-basierte GenAI-Nutzung ohne Fine-Tuning. Alle Quellen konvergieren: Art. 10 Abs. 1–5 = Provider-Pflicht, nicht Deployer-Pflicht.

### Offener Punkt
- "Repräsentativ" für RAG-Testdaten (Art. 10 Abs. 6) → Quality-Gate-Kandidat → beim Gate-Entwurf klären

---

## Entscheidung 2: RAG-Grauzone

**These:** RAG-Retrieval-Daten = Inference-Input unter Art. 13/15, nicht Art. 10.

### Evidence
- **Normtext:** Art. 10 = Trainings-/Validierungs-/Testdaten. RAG ist keines davon. Art. 13 Abs. 3(b)(ii) + Art. 15 Abs. 4 decken Input- und Logging-Pflicht ab.
- **Buscemi (2025):** RAG fällt in Verification Space R6 (Transparency), nicht R4 (Data Governance)
- **Blueprint D29:** Custom Facets = Runtime-RAG-Lineage → bestätigt Runtime-Klassifizierung

### Umsetzung
- Sub-Decision unter MD13 (Scope-Präzisierung), keine eigene MD15
- Formulierung in MD13: "RAG-Retrieval-Daten werden als Inference-Input unter Art. 13/15 klassifiziert (Begründung: kein Training, sondern Runtime-Input; gestützt durch Buscemi R6-Zuordnung)"
- Interpretation als Limitation: Kap. 4.1 (Satz) + Kap. 7 (ausführlich) + Ausblick

### Risiko
- ⚠ Dies ist eine Interpretation, kein expliziter Normtext. Als Limitation kennzeichnen.

---

## Entscheidung 3: Jonnala-Methodik als Quelle

**These:** Jonnala et al. (2025) ist zitierfähig als konvergente Evidenzquelle, nicht als alleinige Quelle.

### Begründung
- **Pro:** Peer-reviewed, transparente Methodik (27 Rubrics, 4-Punkte-Skala), bestätigt Gaps die auch Normtext + Buscemi zeigen
- **Contra:** LLM-as-Evaluator methodisch umstritten, Rubric-Scores = Proxy-Werte

### Umsetzung
- In Kap. 4 als eine von drei konvergenten Quellen (neben Normtext + Buscemi)
- Nie als alleinige Evidenz
- Formulierung: "Jonnala et al. (2025) identifizieren mittels rubric-basierter Gap-Analyse signifikante Compliance-Lücken bei GenAI-Systemen [...]"
- Methodische Einschränkung (LLM-as-Evaluator): Kap. 4 + Kap. 7

---

## Entscheidung 4: Huwyler fehlt in Zotero

**These:** Organisatorisches Problem, kein inhaltliches.

### Umsetzung
- Huwyler (2024) in Zotero unter `02_RQ1` nachimportieren
- #1-Quelle für Kap. 4 laut Paper-Ranking (Gegenprüfung)

---

## Entscheidung 5: DSR-Begründung MD10/MD11

**These:** Requirements-Ableitung = Relevance→Design Übergang (Hevner), gestützt durch Peffers Phase 2.

### Was geändert werden muss

**1. Kap. 4 Einleitung — Rückverweis-Satz einfügen:**

> "Die nachfolgende Anforderungsanalyse operationalisiert den in Abschnitt 3.5 definierten Relevance Cycle und überführt normative Anforderungen gemäß der in Abschnitt 3.6 beschriebenen Traceability-Kette in technisch testbare Design Principles als Input für den Design Cycle (Peffers et al., 2007, Phase 2)."

**2. Kap. 4 Ende — Traceability-Tabelle erstellen:**

| RQ | Requirement | Design Principle | Gate |
|---|---|---|---|
| RQ1 | R1–R7 | DP1–DP12 | (zuzuordnen) |
| RQ2 | (aus Kap. 5) | (aus Kap. 5) | (zuzuordnen) |

⚠ **Tabelle noch nicht erstellt** — offener Arbeitsschritt nach Finalisierung der Requirements.

---

## Quellenverzeichnis — Was Mustafa lesen/bearbeiten muss

### A. Hauptquellen (bereits genutzt, hohe Priorität)

| # | Quelle | Zotero-Key | Rolle in Kap. 4 | Status |
|---|---|---|---|---|
| 1 | **Huwyler (2024)** — Deployment-Governance | ❌ Fehlt in Zotero | #1 Quelle: Lifecycle-Governance, Gate-Systematik, Deployment-Fokus | **NACHIMPORTIEREN** |
| 2 | **Buscemi et al. (2025)** — Verification Space | `WXJEQWIH` | #2 Quelle: Verification Methods, R1–R8 Requirements-Mapping | ✅ Gelesen |
| 3 | **EU AI Act (VO 2024/1689)** — Art. 9–15 | (Primärquelle) | Regulatorische Basis für alle Requirements | ✅ Gelesen |
| 4 | **NIST AI RMF 1.0** | (Primärquelle) | GOVERN/MAP/MEASURE/MANAGE Funktionsbereiche | ✅ Gelesen |

### B. Sekundärquellen (genutzt, konvergente Evidenz)

| # | Quelle | Zotero-Key | Rolle in Kap. 4 | Status |
|---|---|---|---|---|
| 5 | **Kovac et al. (2025)** — CERTAIN/RegOps | `58TTZUHJ` | RegOps-Konzept, CI/CD-Compliance-Pipelines | ✅ Gelesen |
| 6 | **Jonnala et al. (2025)** — Gap Analysis | `CQQSAPY2` | Konvergente Evidenz für AI Act Gaps bei GenAI (mit Einschränkung LLM-Methodik) | ✅ Gelesen |
| 7 | **Burns et al. (2025)** — AIGA Framework | `L7KGSC7Z` | 8 Governance-Kategorien, zu superficial für technische Operationalisierung | ✅ Gelesen |

### C. Zotero-Bibliothek `02_RQ1` — Weitere relevante Papers zum Lesen

| # | Quelle | Zotero-Key | Warum relevant | Lesepriorität |
|---|---|---|---|---|
| 8 | **Bommasani et al. (2022)** — Foundation Models Report | `B8YQRFPF` | Standardreferenz für Foundation Model Risiken, stützt Art. 10 Out-of-Scope Argument (Black-Box-Charakter) | 🔴 HOCH |
| 9 | **Liang et al. (2023)** — HELM Benchmark | `DWPRSST8` | Holistic Evaluation of Language Models, relevant für Evaluation-Gates (Kap. 5/6) | 🟡 MITTEL |
| 10 | **Shneiderman (2022)** — Human-Centered AI | `X63PTJAP` | Konzeptioneller Rahmen für Art. 14 (Human Oversight), stützt Gate-Design | 🟡 MITTEL |
| 11 | **Jobin et al. (2019)** — Global AI Ethics Landscape | `BRLHV4SS` | Meta-Analyse zu AI-Governance-Prinzipien, Rigor-Cycle Referenz | 🟢 NIEDRIG |
| 12 | **Floridi et al. (2018)** — AI4People | `KQK5YH8F` | Ethische Rahmenbedingungen, ergänzend für Governance-Dimension | 🟢 NIEDRIG |

### D. Empfohlene Lesereihenfolge

1. **Huwyler (2024)** — nachimportieren + lesen (Kernquelle, noch nicht in Zotero)
2. **Bommasani et al. (2022)** — stützt Art. 10 Argument (Foundation Model = Black Box)
3. **Buscemi (2025)** nochmal gezielt Abschnitt zu R4 (Data Governance) vs. R6 (Transparency)
4. **Liang/HELM (2023)** — wenn du an Evaluation-Gates arbeitest
5. **Shneiderman (2022)** — wenn du an Art. 14 Human Oversight Gates arbeitest

---

## Nächste Arbeitsschritte

1. ☐ Huwyler (2024) in Zotero nachimportieren
2. ☐ Bommasani et al. (2022) lesen (Art. 10 Evidenz)
3. ☐ Kap. 4.1 Scope-Abschnitt schreiben (Art. 10 + RAG-Klassifizierung)
4. ☐ Rückverweis-Satz Kap. 4 Einleitung einfügen
5. ☐ Traceability-Tabelle RQ → R → DP → Gate erstellen
6. ☐ MD13 um RAG Sub-Decision erweitern
