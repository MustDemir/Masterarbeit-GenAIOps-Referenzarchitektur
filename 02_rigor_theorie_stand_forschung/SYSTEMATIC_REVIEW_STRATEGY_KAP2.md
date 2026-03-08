# Systematic Review Strategy — Kapitel 2: Theoretische Grundlagen und Stand der Forschung

> **Stand:** 2026-03-07 | **Methode:** Elicit/Consensus/SemanticScholar Landscape Scan
> **Zweck:** Per-Section Arbeitsanweisung + Quellenverifikation + Gap-Identifikation

---

## Legende

- 🟢 **VORHANDEN** = Quelle bereits in Zotero/INHALTSPLAN
- 🟡 **SUPPLEMENT** = Elicit-Fund, ergänzt bestehende Quellen sinnvoll
- 🔴 **ZOTERO-LÜCKE** = Im INHALTSPLAN referenziert, aber noch nicht in Zotero importiert
- ⚪ **IRRELEVANT** = Elicit-Fund, passt nicht zum Scope

---

## 2.1 Begriffsabgrenzung und Systemkontext (~1,5 S. / ~450W)

### Was du schreiben musst
6 Arbeitsdefinitionen in je 2–3 Sätzen: LLM, GenAI-System, RAG, LLMOps/GenAIOps, Quality Gate, Policy-as-Code. Jede Definition mit einer Primärquelle belegt. Keine Tiefe — nur Orientierung für den Leser. Forward-References auf die Detailabschnitte (2.2, 2.4.1, 2.5, 2.6).

### Arbeitsschritte
1. Definitionsboxen für alle 6 Begriffe formulieren
2. Je 1 Primärquelle pro Definition (kein Multi-Sourcing nötig)
3. Explizite Forward-References einbauen: "→ siehe Abschnitt 2.X für Detailabhandlung"
4. Abgrenzungstabelle: GenAI-System vs. LLM vs. Foundation Model (1 Absatz oder Mini-Tabelle)

### Quellenlandschaft (Elicit-Ergebnis)

| Quelle | Status | Relevanz für 2.1 |
|--------|--------|-------------------|
| Bommasani et al. (2021) — Foundation Models | 🔴 ZOTERO-LÜCKE | KEY: Foundation Model + GenAI-System Definition |
| Vaswani et al. (2017) — Attention Is All You Need | 🔴 ZOTERO-LÜCKE | BASIS: LLM-Basisdefinition |
| Lewis et al. (2020) — RAG Paper | 🔴 ZOTERO-LÜCKE | KEY: RAG-Definition |
| Kreuzberger et al. (2023) [QY49ZYXB] | 🟢 VORHANDEN | MLOps-Definition → GenAIOps Abgrenzung |
| Tantithamthavorn et al. (2025) [C755FHJK] | 🟢 VORHANDEN | Taxonomie MLOps/LLMOps/FMOps |
| Bandi et al. (2023) — GenAI Review, 362 Cit. | 🟡 SUPPLEMENT | Taxonomie GenAI-Modelle + Requirements |
| Hagos et al. (2024) — GenAI+LLM Advances, 67 Cit. | 🟡 SUPPLEMENT | Überblick GenAI/LLM Landscape |

### Elicit-Bewertung
Die Landschaft bestätigt: Bommasani (2021) bleibt DIE Referenz für Foundation Models. Bandi et al. (2023) mit 362 Zitationen wäre ein starker Supplement für die GenAI-Taxonomie, ist aber nicht zwingend nötig wenn Bommasani + Vaswani + Lewis die Kernbegriffe abdecken.

---

## 2.2 Generative KI und LLMs (~1,5 S. / ~450W)

### Was du schreiben musst
Technische Grundlagen: Transformer-Überblick (KEIN Deep-Dive), emergente Fähigkeiten, LLM-spezifische Risiken (Halluzination, Bias, Prompt Injection, Stochastizität), warum klassische ML-Evaluation nicht reicht, RAG als Enterprise-Pattern.

### Arbeitsschritte
1. Transformer nur als Architektur-Skizze (1 Absatz: Encoder-Decoder, Self-Attention, Skalierung)
2. Emergente Fähigkeiten: Wei et al. (2022) als Beleg → Implikation für QA
3. Risikoblock: Halluzination (Huang 2023), Bias, Prompt Injection → je 2-3 Sätze
4. Überleitung: "Diese Risiken erfordern spezialisierte Quality Gates" → Bridge zu 2.5
5. RAG-Pattern: Lewis (2020) + Xu/Cardoso (2025) → Retrieval-Qualität als Gate-Kriterium

### Quellenlandschaft (Elicit-Ergebnis)

| Quelle | Status | Relevanz für 2.2 |
|--------|--------|-------------------|
| Wei et al. (2022) — Emergent Abilities | 🔴 ZOTERO-LÜCKE | KEY: Emergente Fähigkeiten |
| Huang et al. (2023) — Hallucination Survey | 🔴 ZOTERO-LÜCKE | KEY: Halluzinationsrisiko |
| Shankar et al. (2024) — LLM Evaluation Challenges | 🔴 ZOTERO-LÜCKE | KEY: Evaluation-Problematik |
| Xu et al. (2025) [P998PMS3] — RAGOps | 🟢 VORHANDEN | RAG-Pattern |
| Bommasani et al. (2021) | 🔴 ZOTERO-LÜCKE | Risiken + Capabilities |
| Head et al. (2023) — LLM Applications for Evaluation | 🟡 SUPPLEMENT | Halluzinationsrisiko allgemein |
| Quan et al. (2025) — Test Selection for LLMs | ⚪ IRRELEVANT | Zu spezifisch (Test Selection) |

### Elicit-Bewertung
SemanticScholar bestätigt: Halluzination, Bias und Evaluation-Herausforderungen sind gut dokumentiert. Die meisten Treffer sind domain-spezifisch (Healthcare, Medical). Für 2.2 reichen die bereits geplanten Quellen (Wei, Huang, Shankar, Bommasani). Kein Supplement nötig — nur Zotero-Import sicherstellen.

---

## 2.3 Cloud-native: Fokus auf Plattformfähigkeiten (~1,5 S. / ~450W)

### Was du schreiben musst
Cloud-native NICHT als Infrastruktur-Lehrbuch, sondern als Enabler für GenAIOps. 4 Plattformfähigkeiten: Identity/Access (Zero Trust), Network (Service Mesh), Observability (LLM-Metriken), Policy Engine (OPA). IaC + GitOps als Operationalisierung.

### Arbeitsschritte
1. CNCF-Definition zitieren (Cloud-native Trail Map 2018)
2. 4 Capabilities in je 1 Absatz: Identity, Network, Observability, Policy
3. Pro Capability: Warum relevant für GenAI? (z.B. Observability → LLM-Latenz, Token-Usage, Drift)
4. IaC/GitOps-Absatz: Versionierung + Audit-Trail als Grundlage für Compliance-as-Code
5. Bridge: "Diese Plattformfähigkeiten bilden die Infrastruktur-Basis für die in 2.4.1 beschriebenen Ops-Praktiken"

### Quellenlandschaft (Elicit-Ergebnis)

| Quelle | Status | Relevanz für 2.3 |
|--------|--------|-------------------|
| CNCF (2018) — Cloud-native Definition | 🔴 ZOTERO-LÜCKE | KEY: Basisdefinition |
| Kratzke & Quint (2017) — Understanding CNA | 🔴 ZOTERO-LÜCKE | KEY: Akademische Fundierung |
| Burns et al. (2016) — Borg, Omega, K8s | 🔴 ZOTERO-LÜCKE | BASIS: Container-Orchestrierung |
| Pourmajidi et al. (2025) [2ZNT2H8W] | 🟢 VORHANDEN | CNA Governance Reference |
| Naayini (2025) — K8s AI Applications, 5 Cit. | 🟡 SUPPLEMENT | Kubernetes + MLOps Integration |
| Mistry (2025) — K8s eBPF Security | ⚪ IRRELEVANT | Zu spezifisch (Security) |
| Potluri (2025) — Zero Trust K8s | ⚪ IRRELEVANT | Zero Trust, aber zu Security-fokussiert |

### Elicit-Bewertung
Naayini (2025) ist ein interessanter Supplement: zeigt konkret wie Kubeflow, MLflow, Argo auf Kubernetes laufen — genau die Schnittstelle Cloud-native ↔ MLOps. Könnte die Bridge zu 2.4.1 stärken. Aber: Priorität haben CNCF, Kratzke, Burns — die müssen erst in Zotero.

---

## 2.4.1 Von MLOps zu LLMOps (~2 S. / ~600W)

### Was du schreiben musst
Evolution MLOps → LLMOps → GenAIOps. Warum neue Ops-Praktiken nötig (kein klassisches Training, Prompt-Engineering, RAG-Pipelines). Taxonomie-Vergleich. CI/CD/CT für GenAI.

### Arbeitsschritte
1. MLOps-Definition + Kernprinzipien (Kreuzberger 2023, 1 Absatz)
2. Grenzen für LLMs aufzeigen (kein retraining, prompt-basiert, etc.)
3. LLMOps-Erweiterungen: Prompt Management, Embedding-Pipeline, Guardrails
4. GenAIOps = LLMOps + RAGOps + AgentOps (Joshi 2025, Cardoso/Xu 2025)
5. Vergleichstabelle: MLOps vs. LLMOps vs. FMOps vs. GenAIOps (Tantithamthavorn 2025)
6. CI/CD/CT-Absatz: Was ändert sich? (Evaluation Shift, Prompt-Testing, RAG-Validierung)

### Quellenlandschaft (Elicit — aus vorheriger Session)

| Quelle | Status | Relevanz für 2.4.1 |
|--------|--------|---------------------|
| Kreuzberger et al. (2023) [QY49ZYXB] | 🟢 VORHANDEN | KEY: MLOps-Basis |
| Pahune & Akhtar (2025) [M9LISHKG] | 🟢 VORHANDEN | KEY: MLOps→LLMOps |
| Tantithamthavorn et al. (2025) [C755FHJK] | 🟢 VORHANDEN | KEY: Taxonomie |
| Joshi (2025) [6RRBZAUF] | 🟢 VORHANDEN | KEY: LLMOps/AgentOps Survey |
| Xu et al. (2025) [P998PMS3] | 🟢 VORHANDEN | RAGOps |
| Mahr et al. (2024) | 🟢 VORHANDEN | LLM QA |
| Sinha et al. (2024) — DevOps meets GenAI | 🟡 SUPPLEMENT | Bereits bekannt, Consensus-Treffer |

### Elicit-Bewertung
✅ **Stärkste Sektion** — alle Kernquellen vorhanden, keine Lücken. Consensus-Suche hat ausschließlich bereits bekannte Quellen zurückgegeben. Das bestätigt: die INHALTSPLAN-Planung für 2.4.1 ist vollständig.

---

## 2.4.2 Der EU AI Act: Regulatorischer Rahmen (~2 S. / ~600W)

### Was du schreiben musst
Überblick EU AI Act (KEIN Rechtsgutachten). Risikoklassifizierung, Deployer-Pflichten (Art. 26), Art. 9-15 im Überblick. Technisch-organisatorische Implikationen. ACHTUNG: Redundanz-Dreieck mit Kap. 1 (~400W) und Kap. 4 (~3000W) beachten!

### Arbeitsschritte
1. Regulatorischer Kontext: VO 2024/1689, 3 Sätze
2. Risikoklassifizierung: 4 Stufen, Fokus High-Risk (Mini-Tabelle oder 1 Absatz)
3. Deployer-Scope: Art. 26 vs. Art. 16 — KURZ (Details in Kap. 4.1)
4. Art. 9-15 Überblick: Welche Anforderungen? → NUR Nennung, keine Detailanalyse
5. Implikations-Absatz: "Diese normativen Anforderungen erfordern eine systematische Transformation in technisch prüfbare Kontrollmechanismen (→ Kap. 4.3)"
6. **REDUNDANZ-KONTROLLE:** Vor dem Schreiben Kap. 1.2 (PD2) und Kap. 4.1-4.2 gegenlesen!

### Quellenlandschaft (Elicit-Ergebnis)

| Quelle | Status | Relevanz für 2.4.2 |
|--------|--------|---------------------|
| EU AI Act (2024) — VO 2024/1689 | 🟢 VORHANDEN | PRIMÄRQUELLE |
| Laux et al. (2024) — Trustworthy AI | 🟢 VORHANDEN | Three Pillars |
| Kelly et al. (2024) [P5CWR6XL] | 🟢 VORHANDEN | Compliance-Methodologie |
| Burns et al. (2025) [2GGF93BE] | 🟢 VORHANDEN | AI Governance |
| Huwyler (2025) [UE5LVI97] | 🟢 VORHANDEN | Unified Framework |
| Smuha (2021) | 🔴 ZOTERO-LÜCKE | Risk-based Regulation |
| Sovrano et al. (2025) — AI Act Compliance, 4 Cit. | 🟡 SUPPLEMENT | AI-Tools für Compliance-Doku |
| Judijanto (2025) — Compliance Challenges | 🟡 SUPPLEMENT | Qualitative Review Challenges |
| Zanon Diaz et al. (2025) — Medical Device AI Act | ⚪ IRRELEVANT | Zu spezifisch (Medical Devices) |

### Elicit-Bewertung
Sovrano et al. (2025) ist relevant: zeigt die Herausforderung der technischen Dokumentation unter dem AI Act — passt zur Bridge nach Kap. 4.3. Judijanto (2025) bestätigt die fragmentierte Umsetzung in EU-Mitgliedstaaten. Beide sind Supplement, nicht zwingend nötig.

---

## 2.5 Quality Gates: Definition, Konzepte und Einordnung (~1,5 S. / ~450W)

### Was du schreiben musst
Quality-Gate-Konzept fundieren: SE-Herkunft (Cooper 1990), CI/CD-Kontext (Humble/Farley), Abgrenzungen, Erweiterung für AI. MQG4AI-Positionierung. Eigene Arbeitsdefinition.

### Arbeitsschritte
1. Stage-Gate-Modell (Cooper 1990): 1 Absatz, historischer Kontext
2. Quality Gates in CI/CD (Humble/Farley 2010): automatisierte Prüfpunkte
3. Abgrenzungs-Absatz: Gate ≠ Milestone ≠ Review ≠ Approval
4. AI-Erweiterung: Modellevaluation, Datenqualität, Compliance als neue Gate-Dimensionen
5. MQG4AI-Positionierung: Elia et al. (2025) → Abgrenzung zu eigener Arbeit (3 Dimensionen)
6. Eigene Arbeitsdefinition formulieren: "automatisierter, evidenzbasierter Kontrollpunkt..."

### Quellenlandschaft (Elicit — aus vorheriger Session)

| Quelle | Status | Relevanz für 2.5 |
|--------|--------|-------------------|
| Cooper (1990/2008) | 🔴 ZOTERO-LÜCKE | KEY: Stage-Gate Basis |
| Humble & Farley (2010) | 🔴 ZOTERO-LÜCKE | KEY: Gates in CD |
| Elia et al. (2025) [QRW95D4X] | 🟢 VORHANDEN | KEY: MQG4AI |
| Mahr et al. (2024) | 🟢 VORHANDEN | LLM QA Reference |
| Díaz-Rodríguez et al. (2023) [NWJFNALE] | 🟢 VORHANDEN | Trustworthy AI |
| Ray (2026) — TRiSM Review | 🟡 SUPPLEMENT | Trust/Risk/Security Framework |
| Gudigantala et al. (2025) — ML Workflows | 🟡 SUPPLEMENT | Quality in ML Pipelines |
| Pancini et al. (2025) — MLOps Pipelines | 🟡 SUPPLEMENT | Pipeline QA |

### Elicit-Bewertung
Ray (2026) TRiSM-Review ist der stärkste Supplement-Fund: beschreibt Policy-as-Code in MLOps-Pipelines, verknüpft Trust/Risk/Security mit Lifecycle Governance. Exakt die Schnittmenge unserer Arbeit. Allerdings erst Jan 2026 publiziert — Verfügbarkeit prüfen.

---

## 2.6 Compliance-as-Code und Policy-as-Code (~1,5 S. / ~450W)

### Was du schreiben musst
PaC/CaC als technischen Mechanismus definieren. OPA/Rego, Cedar, Sentinel erwähnen. Beziehung zu IaC/GitOps. Reifegradmodell. Enterprise-Kontext für regulierte GenAI-Systeme.

### Arbeitsschritte
1. Policy-as-Code Definition: maschinenlesbare Regeln, die Compliance prüfbar machen
2. OPA/Rego als De-facto-Standard: 2-3 Sätze, keine Implementierung
3. Compliance-as-Code = PaC + Evidence + Audit Trail
4. Reifegradmodell: Manuell → Semi-automatisiert → Vollautomatisiert (1 Absatz)
5. IaC/GitOps-Verknüpfung: Versionierung, Reproducibility, Audit-Trail
6. Bridge: "Die Kombination aus Quality Gates (2.5) und Policy-as-Code bildet das konzeptionelle Fundament für das in Kap. 5.3-5.4 entwickelte Kontrollsystem"

### Quellenlandschaft (Elicit-Ergebnis)

| Quelle | Status | Relevanz für 2.6 |
|--------|--------|-------------------|
| Pourmajidi et al. (2025) [2ZNT2H8W] | 🟢 VORHANDEN | KEY: XaC Governance |
| Stigler (2020) | 🔴 ZOTERO-LÜCKE | KEY: PaC-Konzept |
| Burns et al. (2025) [2GGF93BE] | 🟢 VORHANDEN | AI Governance Automation |
| OPA Dokumentation | 🟢 VORHANDEN | Referenz |
| Sinan et al. (2025) — DevSecOps SLR | 🟡 SUPPLEMENT | Compliance-as-Code in DevSecOps |
| Ray (2026) — TRiSM (s. 2.5) | 🟡 SUPPLEMENT | Policy-as-Code in AI TRiSM |

### Elicit-Bewertung
Sinan et al. (2025) ist ein starker Fund: Systematic Literature Review zu Security Controls in DevSecOps, behandelt explizit Compliance-as-Code, IaC und automated enforcement. 45 Primärstudien ausgewertet. Guter Supplement für den DevSecOps→CaC-Brückenschlag. Ray (2026) beschreibt explizit Policy-as-Code in MLOps-Pipelines mit OPA.

---

## 2.7 Synthese: Forschungslücke und Handlungsbedarf (~2,5 S. / ~750W)

### Was du schreiben musst
Alle 6 Themenfelder bündeln. Forschungslücke identifizieren. Related-Work-Positionierung (Mahr, Pourmajidi, Elia, Kreuzberger, Joshi). USP der eigenen Arbeit. Ableitung Handlungsbedarf → RQ1/RQ2/RQ3.

### Arbeitsschritte
1. Synthese-Absatz: "Die Analyse zeigt, dass...  [6 Felder zusammenführen]"
2. Gap-Statement: "Keine bestehende Arbeit integriert GenAIOps + Quality Gates + EU AI Act Compliance in einem cloud-nativen Framework"
3. Related-Work-Tabelle: 5 Kernarbeiten vs. eigene Arbeit (Feature-Matrix)
4. USP-Positionierung: Was macht DEINE Arbeit einzigartig? (3 Differenzierungsmerkmale)
5. Handlungsbedarf → direkte Überleitung zu Kap. 3 (Methodik) und Kap. 4 (Anforderungen)
6. **NUTZE:** Vergleich_Demir_vs_Mahr.md + Analyse_Pourmajidi_und_Gesamtvergleich.md

### Quellenlandschaft
Alle Quellen aus 2.1-2.6 (Rückverweis). Keine neuen Quellen nötig — nur Synthese.

---

## Gesamtbilanz der Elicit-Suche

### Quellenpool-Status

| Kategorie | Anzahl |
|-----------|--------|
| 🟢 VORHANDEN (Zotero + INHALTSPLAN) | ~22 Quellen |
| 🔴 ZOTERO-LÜCKE (manuell importieren) | 13 Quellen |
| 🟡 SUPPLEMENT (potenziell ergänzend) | ~8 Quellen |
| ⚪ IRRELEVANT | ~12 Quellen |

### 13 Zotero-Lücken — Importliste (PRIORITÄT!)

1. **Bommasani et al. (2021)** — On the Opportunities and Risks of Foundation Models
2. **Vaswani et al. (2017)** — Attention Is All You Need
3. **Lewis et al. (2020)** — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
4. **Wei et al. (2022)** — Emergent Abilities of Large Language Models
5. **Huang et al. (2023)** — A Survey on Hallucination in Large Language Models
6. **Shankar et al. (2024)** — Who Validates the Validators? LLM Evaluation Challenges
7. **CNCF (2018)** — Cloud Native Definition v1.0
8. **Kratzke & Quint (2017)** — Understanding Cloud-Native Applications after 10 Years of CNA Research
9. **Burns et al. (2016)** — Borg, Omega, and Kubernetes
10. **Cooper (1990/2008)** — Stage-Gate Model
11. **Humble & Farley (2010)** — Continuous Delivery
12. **Stigler (2020)** — Policy-as-Code
13. **Smuha (2021)** — From a Race to AI to a Race to AI Regulation

### Top-3 Supplement-Empfehlungen (optional, stärken die Argumentation)

1. **Ray (2026)** — TRiSM Review → Für 2.5 + 2.6: Verknüpft Trust/Risk/Security mit Policy-as-Code in AI Lifecycle
2. **Sinan et al. (2025)** — DevSecOps SLR → Für 2.6: Compliance-as-Code in CI/CD-Pipelines (45 Studien)
3. **Bandi et al. (2023)** — GenAI Review, 362 Cit. → Für 2.1: Taxonomie GenAI-Modelle + Evaluation-Metriken

### Kernbefund
Die Elicit-Suche bestätigt: **Dein INHALTSPLAN ist solide.** Die geplanten Quellen decken die Themen gut ab. Die 13 Zotero-Lücken sind bekannte, hochzitierte Standardwerke — Import ist Pflicht. Die Supplements sind nice-to-have, nicht must-have.

---

## Empfohlene Schreibreihenfolge (bestätigt: Option A)

```
2.1 → 2.2 → 2.3 → 2.4.1 → 2.4.2 → 2.5 → 2.6 → 2.7
```

**VOR dem Schreiben jedes Abschnitts:**
1. Preflight-Skill triggern
2. Relevante Quellen in Zotero verifizieren
3. Negativ-Checklist aus INHALTSPLAN gegenlesen
4. REDUNDANZ-CHECK gegen Kap. 1 und Kap. 4
