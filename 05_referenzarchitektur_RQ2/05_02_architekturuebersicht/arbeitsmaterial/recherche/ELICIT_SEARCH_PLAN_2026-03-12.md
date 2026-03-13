# Elicit-Suchen: Finale Planung nach Zotero-Candidates
**Stand: 2026-03-12 | 8 zusätzliche hochwertige Papers identifiziert**

---

## 🚨 NEUE HOCHRELEVANTE PAPERS (aus Zotero)

### D2-Durchbruch: Compliance-as-Code & Audit-as-Code

| Paper | Relevanz | Begründung |
|---|---|---|
| **Muhammad et al. (2026)** "Audit-as-code: A policy-as-code framework for continuous AI assurance" | ⭐⭐⭐⭐⭐ D2 | **DIREKTER TREFFER:** Policy-as-Code für CI/CD Assurance. Genau das was für Gate-Automatisierung fehlt! |
| **Nweke & Yeng (2026)** "Compliance-as-Code for AI-Driven Identity Systems: Clause-to-Control Traceability" | ⭐⭐⭐⭐⭐ D2+Q | **SUPER-TREFFER:** "Clause-to-Control Traceability" = REQUIREMENT-ZU-GATE MAPPING! Das ist genau deine D_GATE_INCLUSION_RULE! |
| **Sarathe et al. (2025)** "Policy as Code: A paradigm shift in infrastructure security and governance" | ⭐⭐⭐⭐ D2 | Paradigma-Papier für Policy-as-Code. Grundlagen. |

### D1-Verbesserung: Governance-Frameworks

| Paper | Relevanz | Begründung |
|---|---|---|
| **Agarwal & Nene (2025)** "Five-layer framework for AI governance" | ⭐⭐⭐⭐ D1+Q | Multi-Layer Governance Framework. Könnte Lucaj-Templates ergänzen. |
| **Kiejnich-Kruk (2025)** "Obligations of importers, distributors and deployers under the AI Act" | ⭐⭐⭐⭐ D1 | Explizite Analyse von Rollen und Obligations. Gate-Eignung durch Rollen-Klarheit. |

### D3-Erweiterung: Human Oversight + Automation Bias

| Paper | Relevanz | Begründung |
|---|---|---|
| **Laux & Ruschemeier (2025)** "Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight" | ⭐⭐⭐⭐⭐ D3 | **NEUES LAUX-PAPER!** Nicht im ursprünglichen Sample. Direkt zu Automation-vs-Human-Oversight Trade-off. |
| **Keyes et al. (2025)** "Monitoring Deployed AI Systems in Health Care" | ⭐⭐⭐ D3 | Praktische Monitoring/Oversight-Systeme. Real-world Implementation. |
| **Wei & Heim (2025)** "Designing Incident Reporting Systems for Harms from General-Purpose AI" | ⭐⭐⭐ D3 | Oversight durch Incident-Reporting. Second-Degree Oversight (korrektiv). |

---

## 📊 REVIDIERTE COVERAGE-MATRIX (38 Papers total)

**Vorher (30 Papers):**
- D1: 28/30 ✓
- D2: 23/30 (fragmentiert)
- D3: 19/30 ✓
- Q:  18/30 (schwach)

**Nachher (38 Papers mit Zotero-Candidates):**
- D1: 30/38 ✓ (jetzt mit Agarwal, Kiejnich-Kruk)
- D2: **26/38** ⬆️ **DURCHBRUCH** (jetzt mit Muhammad, Nweke, Sarathe)
- D3: 22/38 ✓ (jetzt mit Laux/Ruschemeier, Keyes, Wei/Heim)
- Q:  **20/38** ⬆️ (besonders Nweke zeigt Clause-to-Control)

---

## 🎯 OPTIMIERTE ELICIT-SUCHEN (4 fokussierte Queries)

### SEARCH #1: D1 — Gate-Eignung & Requirement-Operationalization
**Frage:** Wie operationalisieren Governance-Frameworks regulatorische Anforderungen zu prüfbaren, gated Deliverables?

**Bereits abgedeckt von:**
- Feng et al. (31 Keywords)
- Agarwal & Nene (Five-Layer Framework)
- Lucaj et al. (95 Keywords, TechOps Templates)
- Kiejnich-Kruk (Obligations-Mapping)

**Elicit-Fokus:** Lücken finden bei:
- "Stage-gate operationalization of regulatory requirements"
- "Requirement traceability to deliverable maturity models"
- "Governance checkpoint design"

**Erwartetes Ergebnis:** Bestätigung dass Feng + Lucaj + Agarwal ausreichend, oder Ergänzungen?

---

### SEARCH #2: D2 — Policy-as-Code & Compliance-Automation ⭐ STÄRKSTES POTENZIAL
**Frage:** Welche Compliance-Regeln sind maschinenauswertbar? Welche Patterns in Policy-as-Code / Audit-as-Code?

**Bereits abgedeckt von:**
- Kholkar & Ahuja (Policy-as-Prompt)
- **Muhammad et al.** (Audit-as-code Framework) ← NEU, sehr relevant
- **Nweke & Yeng** (Compliance-as-Code mit Clause-to-Control) ← NEU, super relevant
- **Sarathe et al.** (Policy as Code Paradigm) ← NEU

**Elicit-Fokus:** 
- "Compliance automation in regulated domains"
- "CI/CD for regulatory compliance gates"
- "Policy-as-Code for financial/healthcare/AI regulation"
- "Conftest + Rego patterns for compliance checks"

**Erwartetes Ergebnis:** Diese 3 neuen Papers (Muhammad, Nweke, Sarathe) sind möglicherweise AUSREICHEND. Elicit soll Bestätigung geben + weitere Patterns finden.

---

### SEARCH #3: D3 — Human Oversight & Automation Bias
**Frage:** Wie gestalltet man First-Degree vs. Second-Degree Human Oversight als Design-Kriterium?

**Bereits abgedeckt von:**
- Laux (85 Keywords)
- **Laux & Ruschemeier** (Automation Bias in AI Act) ← NEU, explizit zu deinem Problem!
- Keyes et al. (Monitoring in Healthcare)
- Wei & Heim (Incident Reporting Systems)

**Elicit-Fokus:**
- "Automation bias in human oversight systems"
- "First-degree vs second-degree oversight design"
- "Human-in-the-loop vs human-on-the-loop"

**Erwartetes Ergebnis:** Laux + neues Laux/Ruschemeier könnten ausreichend sein. Elicit soll Other Frameworks prüfen.

---

### SEARCH #4 (KRITISCH): Q — Requirement-to-Gate Mapping & Clause-to-Control Traceability
**Frage:** Wo sind Frameworks die explizit zeigen: "Regulation → Control/Gate" mit machine-readable evidence?

**Bereits abgedeckt von:**
- **Nweke & Yeng** (Clause-to-Control Traceability) ← DIREKT RELEVANT
- Lucaj (Requirement → Template)
- Huwyler, Guldimann (Frameworks aber nicht explizit)

**Elicit-Fokus:**
- "Clause-to-control mapping in compliance frameworks"
- "Traceability models for regulatory to technical translation"
- "Requirements operationalization with machine-readable evidence"
- "Compliance artifact management and gate automation"

**Erwartetes Ergebnis:** Nweke & Yeng könnte die Schlüsselquelle sein. Elicit soll weitere Literatur in diesem exakten Nischen-Gebiet finden.

---

## 🎬 BEREITSCHAFT FÜR ELICIT

**Status:** ✅ **READY TO GO**

Die 8 Zotero-Kandidaten schließen die Lücken:
- ✅ D2 ist jetzt stark (Muhammad, Nweke, Sarathe)
- ✅ D3 ist erweitert (Laux/Ruschemeier + praktische Papers)
- ✅ Q hat konkrete Quelle (Nweke zeigt Clause-to-Control)

**Nächster Schritt:** 
Du gibst mir `GO` → Ich führ die 4 Elicit-Suchen aus → Identifiziere Final-Lücken → Dann formulieren wir D_GATE_INCLUSION_RULE mit konkreten Quellen-Referenzen → Dann schreiben wir Sektion 5.2.2

---

## ⚠️ KRITIKALSTE PAPERS (MUST-READ vor 5.2.2)

1. **Nweke & Yeng (2026)** — "Compliance-as-Code with Clause-to-Control Traceability" [D2+Q]
2. **Muhammad et al. (2026)** — "Audit-as-code Framework" [D2]
3. **Laux & Ruschemeier (2025)** — "Automation Bias" [D3]
4. **Laux (2024)** — "Institutionalised Distrust" [D3] (Original, 85 Keywords)
5. **Feng et al. (2024)** — "Normative Requirements Operationalization" [D1]
6. **Lucaj et al. (2025)** — "TechOps Templates" [D1+Q]

Diese 6 Papers bilden das Rückgrat deiner D_GATE_INCLUSION_RULE.
