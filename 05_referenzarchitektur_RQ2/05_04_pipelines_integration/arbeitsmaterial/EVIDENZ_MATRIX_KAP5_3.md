# Elicit-Style Evidenz-Matrix — Kap. 5.3
## Pipeline-Integration und Policy Engine [S3]

**Erstellt:** 2026-03-13 | **Update v3:** 2026-03-13 (SSOT-Scan ROT_CORE + ORANGE_HIGH)
**Methode:** Evidence-Matrix-Builder Skill (Elicit Research Table Approach)
**Scope:** 8 Core Papers + 15 Elicit-Ergebnisse + 7 SSOT-Scan-1 + 2 SSOT-Scan-2 = **32 Quellen**
**Zeitraum:** 2016–2026 | **Fokus:** CI/CD-Pipeline, Policy-as-Code, Gate-Integration

---

## Spalten-Definitionen (Forschungsfragen)

| Q-ID | Forschungsfrage | Absatz-Link | Relevanz-Ebene |
|------|-----|----------|-----------|
| **Q1** | CI/CD-Pipeline mit Stage-Gate-Integration (Pre-Dep/Dep/Ops)? | 5.3.1, Abs. 1–2 | Core |
| **Q2** | Gate-Entscheidungslogik (Contract → Validation → Severity → Decision)? | 5.3.1, Abs. 3 | Core |
| **Q3** | Statische Policy-Prüfung in CI-Phasen (Conftest, OPA, Rego)? | 5.3.2, Abs. 4 | Core |
| **Q4** | Runtime Admission Control auf Kubernetes (Policy-as-Code im Cluster)? | 5.3.2, Abs. 5 | Core |
| **Q5** | Policy-Entscheidungen für Audit-Trails und Evidence-Persistierung? | 5.3.2, Abs. 6 | Core |
| **Q6** | Alternative Policy-Paradigmen (Policy-as-Prompt) und Abgrenzung? | 5.3 Cross-cutting | Differenzierung |
| **Q7** | 29 Policy-Kandidaten als erweiterbare Ausgangsbasis? | 5.3 Cross-cutting | Referenz |
| **Q8** | Gate/Policy-Trennung (1 Gate = mehrere Policies)? | 5.3 Cross-cutting | Klarheit |

---

## Bewertungsskala

| Symbol | Bedeutung | Kriterium |
|--------|-----------|-----------|
| **🟢** | Tiefgehend | Zentrales Thema, mehrere Absätze/Abschnitte |
| **🟠** | Moderat | Eigener Abschnitt oder mehrere Sätze |
| **🟡** | Erwähnt | 1–2 Sätze, oberflächlich |
| **⬛** | Nicht behandelt | Thema kommt nicht vor |

---

## TIER 1: CORE-Quellen (≥2 🟢 oder ≥3 🟠 in Q1–Q5)

| Paper | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Rolle | Tier |
|-------|----|----|----|----|----|----|----|----|-------|------|
| **Baqar et al. (2025)** — AI-Augmented CI/CD Pipelines | 🟢 | 🟢 | 🟢 | 🟡 | 🟠 | 🟡 | 🟡 | 🟢 | Decision Taxonomy, PaC Guardrails, Trust Tiers | ✅ CORE |
| **Garg et al. (2022)** — CI/CD für MLOps | 🟢 | 🟡 | 🟠 | 🟡 | ⬛ | ⬛ | ⬛ | ⬛ | Pipeline-Architektur (Pre/Dep), CI-Integration | ✅ CORE |
| **van Merode (2023)** — CI/CD Practical Guide | 🟢 | 🟡 | 🟠 | ⬛ | 🟡 | ⬛ | ⬛ | 🟡 | Stage-Gate-Konzepte, Pipeline-Design | ✅ CORE |
| **Sardana et al. (2024)** — Compliance-as-Code 2.0 | 🟡 | 🟠 | 🟠 | 🟠 | 🟢 | 🟡 | 🟡 | 🟠 | CAC-Framework, Agentic Policy Engine, Evidence | ✅ CORE |
| **Casimir (2026)** — Governance of Intelligence | 🟡 | 🟠 | 🟠 | 🟡 | 🟢 | 🟡 | ⬛ | 🟠 | Governance-by-Design, Autonomous Data Officer | ✅ CORE |
| **Butt et al. (2026)** ⭐ — GEAP-Framework | 🟢 | 🟢 | 🟠 | 🟡 | 🟢 | 🟡 | 🟡 | 🟠 | Governance as Evidence for AI Pipelines, 5 Gates, Evidence Backbone | ✅ CORE |
| **Nellutla (2025)** ⭐ — MLOps 2.0 Maturity | 🟢 | 🟠 | 🟡 | 🟡 | 🟠 | ⬛ | 🟡 | 🟡 | MLOps 2.0, CI/CD + CDV-Integration, Quality Gate Maturity | ✅ CORE |

**Tier 1 — 7 CORE-Quellen:**
- Q1: 5× 🟢 → SEHR STARK | Q2: 3× 🟢 + 3× 🟠 → SEHR STARK
- Q5: 3× 🟢 (Sardana, Casimir, Butt) → SEHR STARK

---

## TIER 2: EMPFOHLENE Quellen (≥1 🟢 oder ≥2 🟠)

| Paper | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Rolle | Tier |
|-------|----|----|----|----|----|----|----|----|-------|------|
| **Sarathe (2025)** — Policy-as-Code Paradigma | 🟡 | 🟠 | 🟢 | 🟡 | 🟠 | 🟠 | 🟡 | 🟡 | PaC-Grundlage, D_CAC_AAC_DIFF Foundation | ✅ EMPF. |
| **Lucaj et al. (2025)** — TechOps Templates | 🟡 | 🟡 | 🟢 | ⬛ | 🟡 | ⬛ | 🟢 | 🟡 | 29 Policy-Kandidaten (D_LUCAJ_STARTING_BASIS) | ✅ EMPF. |
| **Turner et al. (2020)** — Decision Support, Audit | 🟡 | 🟠 | 🟡 | ⬛ | 🟢 | ⬛ | ⬛ | 🟡 | Decision-Mining, Audit-Trail-Konzepte | ✅ EMPF. |
| **Vaidyanathan (2025)** — Feature Store Governance | ⬛ | 🟠 | ⬛ | 🟡 | 🟢 | ⬛ | ⬛ | 🟠 | Governance-Modelle, Metadata-Audit | ✅ EMPF. |
| **Kasi (2025)** — Model Governance | 🟡 | 🟠 | 🟡 | 🟡 | 🟠 | ⬛ | ⬛ | 🟠 | Governance-Framework, Metadata-Systeme | ✅ EMPF. |
| **Muhammad (2026)** — Audit-as-Code | ⬛ | 🟡 | ⬛ | ⬛ | 🟢 | ⬛ | ⬛ | 🟡 | Assured Readiness Score, Evidence Bundles | ✅ EMPF. |
| **Kholkar & Ahuja (2025)** — Policy-as-Prompt | 🟡 | 🟠 | 🟠 | 🟡 | ⬛ | 🟢 | ⬛ | 🟠 | Alternative zu PaC, LLM-basierte Policies, Abgrenzung | ✅ EMPF. |
| **Atuhaire/Kimani (2025)** — AI Governance Pub. Sector | 🟡 | 🟠 | 🟡 | ⬛ | 🟠 | 🟡 | ⬛ | 🟡 | Governance Frameworks, Compliance Context | ✅ EMPF. |
| **AAGATE / Huang et al. (2025)** ⭐ — K8s Control Plane | 🟡 | 🟠 | 🟠 | 🟢 | 🟡 | 🟠 | ⬛ | 🟡 | **Q4-GAP GESCHLOSSEN**: K8s-native policy enforcement, explainable policy engine, zero-trust | ✅ EMPF. |
| **Adetayo Adeyinka (2023)** ⭐ — OPA Reference Arch. | 🟡 | 🟡 | 🟢 | 🟠 | 🟡 | 🟠 | ⬛ | 🟡 | OPA Reference Architecture, statische + Runtime Policy | ✅ EMPF. |
| **Rebbana (2025)** ⭐ — PaC Multi-Cloud | 🟡 | 🟡 | 🟢 | 🟡 | 🟠 | 🟠 | ⬛ | 🟡 | Policy-as-Code Enforcement Multi-Cloud, CI/CD Integration | ✅ EMPF. |
| **Antiya (2020)** ⭐ — Compliance as Code OPA | 🟡 | 🟡 | 🟢 | 🟠 | 🟡 | 🟡 | ⬛ | 🟡 | CaC mit OPA + AWS Config, ISO 27001/PCI DSS, 85% Automation-Rate | ✅ EMPF. |
| **Romeo et al. (2025)** ⭐ — ARPaCCino | ⬛ | 🟡 | 🟠 | 🟡 | 🟡 | 🟡 | ⬛ | ⬛ | Agentic-RAG + Rego in CI/CD, PaC Compliance-Checking | ✅ EMPF. |

**Tier 2 — 13 EMPFOHLENE Quellen (+1 neu: Antiya):**
- Q3: 5× 🟢 (Sarathe, Lucaj, Adetayo, Rebbana, Antiya) → **SEHR STARK**
- Q4: 1× 🟢 (AAGATE) + 2× 🟠 (Adetayo, Antiya) → **MODERAT, GAP GESCHLOSSEN**
- Q6: 1× 🟢 (Kholkar) + 4× 🟠 → MODERAT-STARK

---

## TIER 3: RESERVIERT (für andere Kapitel)

| Paper | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Zielkapitel | Begründung |
|-------|----|----|----|----|----|----|----|----|-------------|-----------|
| **Park et al. (2024)** — LlamaDuo LLMOps | 🟡 | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | 2.4 MLOps | LLM MLOps, keine Policy-Relevanz |
| **Dingare (2022)** — CI/CD Jenkins | 🟡 | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | 2.4 CI/CD | Jenkins-spezifisch, kein PaC |
| **Pancini et al. (2025)** — Data Quality Gates | 🟡 | ⬛ | 🟡 | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | 4.2 Data Quality | Data Quality fokussiert |
| **Kováč et al. (2025)** — CERTAIN/RegOps | 🟠 | 🟡 | 🟠 | ⬛ | ⬛ | ⬛ | 🟡 | 🟡 | 5.5 PoC | Semantic MLOps, Ontologie-basiert |
| **Xu et al. (2025)** — RAGOps | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | ⬛ | 2.4 GenAIOps | RAG-spezifisch |
| **Mahr et al. (2025)** — Verification & Validation | 🟡 | 🟡 | 🟡 | ⬛ | 🟠 | ⬛ | ⬛ | ⬛ | 6.0 Evaluation | CDV-Abgrenzung, evaluations-fokussiert |
| **Alugunuri (2022)** — IaC + PaC Cloud-Native | 🟡 | ⬛ | 🟠 | 🟡 | ⬛ | 🟡 | ⬛ | ⬛ | 5.5 PoC | IaC+PaC konzeptuell, Q4 nur 🟡 |
| **Finch & Butt (2025)** ⭐ ORANGE — AI Compliance Gaps | 🟡 | 🟡 | ⬛ | ⬛ | 🟠 | 🟠 | ⬛ | ⬛ | 5.6 EU AI Act | EU AI Act compliance gaps; keine PaC/Pipeline-Details |
| **Elia (2023)** ⭐ CORE — Quality Gates Certifiable AI | ⬛ | 🟠 | ⬛ | ⬛ | 🟡 | 🟡 | 🟡 | 🟠 | 5.2 Quality Gates | Gate-Methodik allgemein; medizin-spezifisch, kein PaC |
| **Elia (2025) MQG4AI** ⭐ CORE — High-Risk AI Gates | ⬛ | 🟠 | ⬛ | ⬛ | 🟡 | 🟡 | 🟡 | 🟠 | 5.2 Quality Gates | RAI Quality Gates, Lifecycle; kein Pipeline/PaC |
| **Pourmajidi (2025)** ⭐ ORANGE — CNA Governance | 🟠 | ⬛ | 🟡 | 🟡 | ⬛ | 🟡 | ⬛ | ⬛ | 5.1 Arch-Überblick | Cloud-Native Governance RA, generisch; kein OPA/Gatekeeper |

**Tier 3-Hinweise:**
- **Elia (2023/2025)**: Hochrelevant für **Kap. 5.2 Quality-Gate-Systematik** — dort Pflichtlektüre
- **Pourmajidi (2025)**: Für **5.1 (Architektur-Überblick)** als Cloud-Native-RA-Referenz nützlich
- **Finch & Butt (2025)**: Für **5.6 (EU AI Act / Compliance-Asymmetrie)** relevant

---

## Evidenzstärke-Analyse (v3, post SSOT-Scans 1+2)

| Frage | 🟢-Count | 🟠-Count | Status | Trend vs. v1 |
|-------|----------|----------|--------|-------------|
| **Q1: Pipeline-Architektur** | 5 | 3 | ✅ SEHR STARK | ↑ (+Butt, Nellutla) |
| **Q2: Gate-Entscheidungslogik** | 3 | 5 | ✅ SEHR STARK | ↑ (+Butt) |
| **Q3: Statische Policy-Prüfung** | 5 | 3 | ✅ SEHR STARK | ↑↑ (+Adetayo, Rebbana, Antiya) |
| **Q4: Runtime Admission Control** | 1 | 3 | ✅ MODERAT | ↑↑ (+AAGATE🟢, Adetayo🟠, Antiya🟠) |
| **Q5: Audit-Trails & Evidence** | 3 | 4 | ✅ SEHR STARK | ↑ (+Butt) |
| **Q6: Policy-Paradigmen** | 1 | 5 | ✅ MODERAT-STARK | = |
| **Q7: 29 Policy-Kandidaten** | 1 | 2 | ⚠️ MODERAT | = (Mapping-abhängig) |
| **Q8: Gate/Policy-Trennung** | 1 | 5 | ✅ MODERAT | = |

---

## Synthese: Quellen-Zuordnung zu Absätzen (v3)

### 5.3.1 — CI/CD-Pipeline-Architektur

| Absatz | Aussage | Primärquelle | Sekundärquelle |
|--------|---------|-------------|----------------|
| **Abs. 1** | Gates aus 5.2 → Pipeline-Stages verortet | Baqar (2025) | van Merode (2023) |
| **Abs. 1** | Pre-Dep/Dep/Ops Lifecycle | Garg (2022) | **Butt et al. (2026)** |
| **Abs. 1** | Cloud-agnostische Architektur (DP5, R7) | Baqar (2025) | Nellutla (2025) |
| **Abs. 2** | 3 Stages: conftest → gatekeeper → decision-log | Baqar (2025) | **Butt et al. (2026)** |
| **Abs. 2** | Policy-as-Code Guardrails je Stage | Baqar (2025) | Sarathe (2025) |
| **Abs. 3** | Contract → Validation → Severity → Decision (R8) | **Butt et al. (2026)** | Baqar (2025) |
| **Abs. 3** | MUST/SHOULD-Severity, Determinismus | Baqar (2025) | Nellutla (2025) |

### 5.3.2 — Policy-as-Code Integration

| Absatz | Aussage | Primärquelle | Sekundärquelle |
|--------|---------|-------------|----------------|
| **Abs. 4** | 22 Conftest-Policies aus MAPPING_LUCAJ | Lucaj et al. (2025) | **Adetayo Adeyinka (2023)** |
| **Abs. 4** | Rego-basiert, deklarativ, CI-integriert | Sarathe (2025) | **Rebbana (2025)** |
| **Abs. 4** | OPA als dezentrale Decision Engine | **Antiya (2020)** | **Adetayo Adeyinka (2023)** |
| **Abs. 5** | 4 Gatekeeper-Constraints auf K8s | Sardana (2024) | **AAGATE / Huang (2025)** |
| **Abs. 5** | Standalone OPA + Admission Webhook (D_GATEKEEPER_STANDALONE) | **AAGATE / Huang (2025)** | Adetayo Adeyinka (2023) |
| **Abs. 5** | Explainable Policy Engine, K8s-native | **AAGATE / Huang (2025)** | Sardana (2024) |
| **Abs. 6** | 3 Decision-Log-Policies → Evidence Store (D_LOG_BACKEND) | **Butt et al. (2026)** | Casimir (2026) |
| **Abs. 6** | CAC/AAC-Differenzierung (D_CAC_AAC_DIFF) | Sardana (2024) | Turner et al. (2020) |
| **Abs. 6** | Assured Readiness Score (Audit-as-Code) | Muhammad (2026) | **Butt et al. (2026)** |

---

## Pflicht-Zitat-Status (Update v3)

| Pflicht-Zitat | Tier | Im Repo | Zotero-Status | Q-Abdeckung |
|--------------|------|---------|--------------|------------|
| Sardana et al. (2024) | ✅ CORE | Ja | HNRC4AVQ | Q2, Q4, Q5 |
| Kováč et al. (2025) | ⚠️ TIER 3 | Nein (arXiv:2510.00084) | ❌ Import ausstehend | Q1, Q3 |
| Kholkar & Ahuja (2025) | ✅ TIER 2 | Nein | ❌ Import ausstehend | Q6 |
| Sarathe (2025) | ✅ TIER 2 | Ja | SWTTU6V2 | Q2, Q3, Q6 |
| Lucaj et al. (2025) | ✅ TIER 2 | Ja | In Zotero | Q7 |
| Muhammad (2026) | ✅ TIER 2 | Ja | V6HKHA5B | Q5 |
| Butt et al. (2026) ⭐ | ✅ CORE | Ja (SSOT) | ⚠️ Zotero-Key fehlt | Q1, Q2, Q5 |
| AAGATE / Huang (2025) ⭐ | ✅ TIER 2 | Ja (SSOT) | ⚠️ Zotero-Key fehlt | Q4 |

---

## GO/NO-GO für Schreiben (v3 — FINAL)

| Frage | Status v1 | Status v3 | Schreibbar? |
|-------|----------|----------|-----------|
| Q1 Pipeline-Architektur | ✅ STARK | ✅ SEHR STARK | **GO** |
| Q2 Gate-Entscheidungslogik | ✅ STARK | ✅ SEHR STARK | **GO** |
| Q3 Statische Policies | ⚠️ MODERAT | ✅ SEHR STARK | **GO** |
| Q4 Runtime Admission | ❌ SCHWACH | ✅ MODERAT | **GO** *(war: NO-GO)* |
| Q5 Audit-Trails | ✅ MOD-STARK | ✅ SEHR STARK | **GO** |
| Q6 Policy-Paradigmen | ✅ MODERAT | ✅ MOD-STARK | **GO** |
| Q7 29 Policy-Kandidaten | ⚠️ MODERAT | ⚠️ MODERAT | **GO** (Mapping-Referenz) |
| Q8 Gate/Policy-Trennung | ✅ MODERAT | ✅ MODERAT | **GO** |

**⬛ CONDITIONAL → ✅ FULL GO**

Alle 8 Fragen auf GO. Blockers:
1. ❌ **Zotero-Import**: Kováč + Kholkar + Butt et al. + AAGATE/Huang → vor Abs. 4/5 schreiben
2. ⚠️ Q7 bleibt MODERAT — schreibbar via MAPPING_LUCAJ_TO_RXX.md-Referenz

---

## SSOT-Scan-Protokoll

| Scan | Ordner | Keywords | Findings |
|------|--------|----------|---------|
| **Scan 1** | `04_Kap5_.../05_04_Pipeline_Integration_S3/` + `SSOT-Cluster` | PaC, OPA, Kubernetes, Gate, Pipeline, Evidence | Butt(→T1), Nellutla(→T1), AAGATE(→T2), Adetayo(→T2), Rebbana(→T2), Romeo(→T2), Alugunuri(→T3) |
| **Scan 2** | `98_Taglogik_Relevanz/REL_ORANGE_HIGH/` + `REL_ROT_CORE/` | Policy, Compliance, Governance, Cloud-Native, Gate, CI/CD, OPA | Antiya(→T2), Pourmajidi(→T3), Elia×2(→T3/Kap5.2), Finch&Butt(→T3/Kap5.6) |

---

**Stand:** Evidence-Matrix v3 (nach SSOT-Scan 1+2) | **32 Quellen** (war: 23 → 30 → 32)
**Datum:** 2026-03-13 | **Author:** Claude (Evidence-Matrix-Builder Skill)
