# Quellenanalyse für Kap. 5.5 (Evidence und Audit Logik)
**Stand:** 2026-03-13  
**Cluster:** `/00_admin/Literatur/SSOT_GLIEDERUNG_CLUSTER_2026-03-07/04_Kap5_Referenzarchitektur_RQ2/05_05_Evidence_und_Audit_Logik_S4`

## 4 Gefundene Quellen – Abstrakts und Relevanzbeurteilung

### 🌟 **[CORE CANDIDATE #1]** Kholkar & Ahuja (2025): Policy-as-Prompt
**Status:** HIGHLY RELEVANT  
**PDF:** `Kholkar und Ahuja - 2025 - Policy-as-Prompt Turning AI Governance Rules into Guardrails for AI Agents.pdf`  
**Venue:** NeurIPS 2025 Workshop on Regulatable ML

**Abstract (gekürzt):**
> "Policy-as-Prompt" framework converts unstructured design artifacts (PRDs, TDDs, code) into verifiable runtime guardrails. The system reads policy documents and risk controls to build a source-linked policy tree, compiled into lightweight prompt-based classifiers for real-time runtime monitoring. Enforces least privilege, data minimization, and provides complete provenance, traceability, and audit logging with human-in-the-loop review. Generates auditable rationales aligned with AI governance frameworks.

**Warum relevant für Kap. 5.5:**
- ✅ **Policy-as-Code:** Direkt relevant für CAC (Compliance-as-Code)
- ✅ **Audit Logging & Traceability:** Kernkonzept für Evidence Store
- ✅ **Runtime Enforcement:** Brückenschlag zwischen statischen Policies (Kap. 5.4) und Audit Logs (Kap. 5.5)
- ✅ **Provenance & Rationales:** APA7 Belegung für Evidence-Backbone (Decision Logs)
- ✅ **Least-Privilege Automation:** Direkt zu DP5 (Cloud-native Integrierbarkeit)

**Kapitel-Zuordnung:** 5.5 (S4 Evidence/Audit) → Abs. 3–5 (CAC/AAC, Evidence Backbone, Immutability Triggers)

---

### 📋 **[CORE CANDIDATE #2]** Pistilli et al. (2023): Stronger Together
**Status:** MODERATELY RELEVANT  
**PDF:** `Pistilli - 2023 - Stronger Together on the Articulation of Ethical Charters Legal Tools and Technical Documentation in ML.pdf`  
**Venue:** FAccT'23 (ACM Conference on Fairness, Accountability, and Transparency)

**Abstract (gekürzt):**
> Addresses growing accountability needs by leveraging processes from ethics, law, and computer science. Details interdependencies between ethical, legal, and technical compliance frameworks. Focuses on roles of ethical charters, licenses, and technical documentation in governance. Identifies synergies between fields through mechanisms in open governance fora (workshops, licensing initiatives, regulatory frameworks). Argues for joint consideration of ethical, legal, and technical aspects in AI governance.

**Warum relevant für Kap. 5.5:**
- ✅ **Governance Frameworks Integration:** Verbindung zwischen Compliance, Legal, Technical
- ✅ **Technical Documentation as Governance:** Dokumentation als Kontrollartefakt
- ✅ **Collaborative Governance:** Menschliche + technische Überprüfung (Decision Logs)
- ⚠️ **Indirekte Relevanz:** Nicht direkt auf Evidence Stores/Audit Trails, aber auf Governance-Architektur

**Kapitel-Zuordnung:** 5.5 (S4 Evidence/Audit) → Abs. 2 (DP1: Compliance-Lifecycle) oder als Governance-Kontext

---

### 📊 **[SUPPLEMENTARY]** Golpayegani et al. (2024): AICat
**Status:** LOW-MODERATE RELEVANCE  
**PDF:** `Golpayegani et al. - 2024 - AICat AI Cataloguing for the EU AI Act.pdf`  
**Venue:** 32nd Irish Conference on AI and Cognitive Science, Dec 2024

**Abstract (gekürzt):**
> AICat is an extension of DCAT (Data Catalog Vocabulary) for representing catalogues of AI systems, providing consistency, machine-readability, searchability, and interoperability. Addresses EU AI Act requirements for easily-navigable, machine-readable databases of high-risk AI systems. Uses Semantic Web approaches to ensure transparency, traceability, and accountability beyond immediate compliance needs.

**Warum (weniger) relevant für Kap. 5.5:**
- ✅ **Cataloguing & Machine-Readability:** Relevant für Evidence Store Metadaten
- ⚠️ **Focus auf Katalogisierung, nicht Audit:** DCAT ist eher für Registry als für Audit Logs
- ⚠️ **Ergänzend, nicht kernhaft:** Könnte als Referenz für Metadaten-Schema dienen, aber nicht primär

**Kapitel-Zuordnung:** 5.5 (S4) → Optional für Abs. 4 (Decision Logs Schema), aber nicht essential

---

### 📝 **[SUPPLEMENTARY]** Sovrano et al. (2025): Simplifying software compliance
**Status:** LOW-MODERATE RELEVANCE  
**PDF:** `Sovrano et al. - 2025 - Simplifying software compliance AI technologies in drafting technical documentation for the AI Act.pdf`  
**Venue:** Empirical Software Engineering (Springer), Volume 30, Mar 2025

**Abstract (gekürzt):**
> Explores how AI technologies (ChatGPT, DoXpert) can aid software developers in creating technical documentation compliant with EU AI Act. Demonstrates how tools identify gaps in existing documentation. Evaluates alignment between tool-generated assessments and expert opinions using open-source high-risk AI systems as case studies. Shows moderate correlation between AI tools and expert judgments, indicating potential for AI to combine with human analysis to alleviate compliance burden.

**Warum (weniger) relevant für Kap. 5.5:**
- ✅ **Documentation Automation:** Relevant für technische Compliance
- ⚠️ **Focus auf Dokumenterstellung, nicht Audit:** DoXpert ist ein Compliance-Tool, nicht ein Evidence Store
- ⚠️ **Orthogonal zu Audit Logik:** Eher zu Kap. 5.3 oder 5.1 passend

**Kapitel-Zuordnung:** Eher zu Kap. 5.1/5.2 (Architektur-Dokumentation) als zu 5.5

---

## 📍 Relevanz-Matrix: Core vs. Supplementary

| Quelle | Kernkonzept | Relevanz für 5.5 | Priorität | Absatz-Zuordnung |
|---|---|---|---|---|
| **Kholkar & Ahuja 2025** | Policy-as-Prompt, CAC, Audit Logging | **SEHR HOCH** | 🔴 **MUST** | Abs. 3–5 (CAC/Decision Logs/Immutability) |
| **Pistilli 2023** | Governance Frameworks, Compliance Integration | **HOCH** | 🟡 **SHOULD** | Abs. 2 (DP1 Compliance-Lifecycle) |
| **Golpayegani 2024** | Metadaten-Katalogisierung, Semantic Web | **MITTEL** | 🟢 **NICE-TO-HAVE** | Optional: Abs. 4 (Decision Logs Schema) |
| **Sovrano 2025** | Dokumentationsautomation, Compliance Tooling | **NIEDRIG** | ⚪ **DEFER** | Nicht für 5.5; evtl. Kap. 5.1 |

---

## 🎯 **Preflight-Entscheidung: Core Candidates für Kap. 5.5**

### ✅ **AUFNAHME in Bibliographie**

1. **Kholkar & Ahuja (2025)** – Primary source for Policy-as-Code execution, runtime audit, and Decision Logs
2. **Pistilli et al. (2023)** – Secondary source for governance framework integration and compliance architecture

### ⚠️ **OPTIONAL / CONTEXT-ONLY**

3. **Golpayegani et al. (2024)** – Supplementary for metadata cataloguing (if schema details are needed)

### ❌ **DEFERRAL / OUT-OF-SCOPE**

4. **Sovrano et al. (2025)** – More relevant to earlier chapters; not essential for Evidence/Audit Logik

---

## 📋 Nächste Schritte

1. ✅ Core Candidates in Kap. 5.5 Preflight notieren (done)
2. 🔄 DSR Artifact Spezifikation (PostgreSQL Schema) bestätigen
3. 🔄 5-Seiten-Budget Assessment durchführen
4. 🔄 Preflight-Protokoll für Kap. 5.5 erstellen (nach DSR + Budget Entscheidung)
