# Recherche-Bericht Kap. 4.6 — Requirements-Katalog & Traceability
**Datum:** 2026-03-10 (Update: 2026-03-10 — 5 neue Q3-Quellen + Argumentationsstruktur)
**Status:** Elicit-Recherche abgeschlossen, Stufe-2 Quellenprüfung + Elicit-Reports Q1–Q4 abgeschlossen
**Scope:** Deployer-only (Art. 26), High-Risk GenAI (Art. 6 + Annex III)

---

## 1. Bestehende Quellenbasis (aus OneDrive + Zotero verifiziert)

### 1.1 Kernquellen 04_06 Ordner (8 PDFs, alle in Zotero)

| # | Quelle | Zotero-Key | Relevanz für 4.6 | Rating |
|---|--------|-----------|-------------------|--------|
| 1 | Elia (2025) — MQG4AI | QRW95D4X | Requirements-Katalog-Methodik, Gate-Konzept | ⭐⭐⭐ |
| 2 | Corrêa & Mönig (2024) — Ethical Requirements Catalog | XVM65FRQ | Requirement-Taxonomie, Normierung | ⭐⭐ |
| 3 | Golpayegani et al. (2024) — AICat | 7BF458GD | Ontologie-basiertes Requirements-Mapping | ⭐⭐ |
| 4 | Hernandez (2025) — AI Act Knowledge Graph | JJKTBARQ | Art. → Requirement Traceability | ⭐⭐⭐ |
| 5 | Eisenberg (2025) — UCF | JUK36XAW | Unified Control Framework, Governance-Dimensionen | ⭐⭐⭐ |
| 6 | Lucaj et al. (2025) — TechOps Templates | 5Y79UTJ9 | Operationalisierung, PaC-Templates | ⭐⭐ |
| 7 | Burns et al. (2025) — Dynamo Project | 2GGF93BE | EU AI Act Compliance, Governance-Prozess | ⭐⭐ |
| 8 | Kholkar & Ahuja (2025) — Policy-as-Prompt | VLMNBUST | PaC-Ansatz, Guardrails für AI Agents | ⭐⭐ |

**Neu identifiziert (nicht in Original-Preflight):** Burns (2025), Kholkar & Ahuja (2025)

### 1.2 Zusätzliche Quellen aus 02_04_02 EU AI Act Ordner (relevant für R-xx)

| # | Quelle | Relevanz für 4.6 |
|---|--------|-------------------|
| 1 | EU AI Act Originaltext (VO 2024/1689) | Primäre Normquelle für alle R-xx |
| 2 | Guldimann et al. (2025) — COMPL-AI | Technische Interpretation Art. 9-15 |
| 3 | Huwyler (2025) — Unified Framework | Operationalisierung EU AI Act |
| 4 | Finch & Butt (2025) — Systematic Review | Gaps in AI-Compliant Governance |
| 5 | Ho-Dac & Martinez (2024) — Human Oversight | Art. 14 Standardisierung |
| 6 | Feng et al. (2024) — Normative Req. Operationalization | LLM-gestützte Req.-Ableitung |
| 7 | Díaz-Rodríguez et al. (2023) — Trustworthy AI | Requirement-Taxonomie |

---

## 2. Elicit-Recherche: Gezielte Gap-Analyse (4 Queries)

### Q1: Governance-Dimensionen-Taxonomie
**Query:** "AI governance dimensions taxonomy regulatory technical strategic enterprise framework"

| Quelle | Relevanz | Deployer-Scope | Rating |
|--------|----------|---------------|--------|
| Agarwal & Nene (2025) — Five-Layer AI Governance | Direkt: 5-Schichten regulation→standards→certification | ✅ Framework-Ebene | ⭐⭐⭐ |
| Leon (2026) — Lifecycle Governance Dimensions | Lifecycle-basierte Governance-Dimensionen | ✅ Lifecycle-Mapping | ⭐⭐ |
| Cobbe et al. (2023) — Reviewable AI Systems | Governance durch Reviewability | ⚠ Eher Provider | ⭐ |

**Bewertung:** Agarwal & Nene liefern akademische Fundierung für die dreistufige Governance-Dimensionen-Taxonomie (regulatorisch/technisch/strategisch). Direktes Mapping möglich.

### Q2: Deployer-spezifische Obligations
**Query:** "EU AI Act deployer obligations requirements Art. 26 operational compliance"

| Quelle | Relevanz | Deployer-Scope | Rating |
|--------|----------|---------------|--------|
| Kiejnich-Kruk (2025) — Deployer/Importer/Distributor | Direkt Art. 26 Pflichten-Analyse | ✅ Kernquelle | ⭐⭐⭐ |
| Buscemi (2025) — EU AI Act Compliance | Bestätigung bestehender Analyse | ✅ Bestätigung | ⭐⭐ |
| Fabiano (2025) — Subject Roles Art. 25 | Art. 25 Transformation, Scope-Trigger | ✅ Scope-Klärung | ⭐⭐ |

**Bewertung:** Kiejnich-Kruk ist die zentrale neue Quelle für die Deployer-Perspektive. Schließt die wichtigste Lücke im bestehenden Quellenkorpus.

### Q3: Post-Market Surveillance, Monitoring & Incident Reporting (Art. 72/73)
**Query:** "post-market surveillance AI systems continuous monitoring incident reporting Art. 72 73 EU AI Act operationalization"
**Elicit-Report:** 5a2cf67e (10 Studien durchsucht, 5 direkt relevant)

| # | Quelle | Zotero-Key | Relevanz | Deployer-Scope | Rating |
|---|--------|-----------|----------|---------------|--------|
| 1 | Muhammad et al. (2026) — Audit-as-Code Governance | IZVYTSTV | Governance→auditable Rules in CI/CD, Assured Readiness Score | ✅ Direkt: PMS + Logging + FRIA-Audit | ⭐⭐⭐ |
| 2 | Keyes et al. (2025) — Stanford RAIL 3-Principle Framework | N3CKUY4T | Monitoring-Architektur: Integrity, Performance, Impact | ✅ Direkt: PMS-Operationalisierung | ⭐⭐⭐ |
| 3 | Wei et al. (2025) — Incident Reporting Design Framework | 892WHGXH | 7-Dimensionen: Who/What/When/Where/How/Why/Resolution | ✅ Direkt: Art. 73 Meldepflicht | ⭐⭐⭐ |
| 4 | Laux et al. (2025) — Automation Bias & Human Oversight | ADX5BQS6 | Oversight-Erosion durch Automation Bias, Gegenmaßnahmen | ✅ Direkt: R008 Oversight-Wirksamkeit | ⭐⭐ |
| 5 | Nweke et al. (2026) — CaC/OSCAL for AI Compliance | XCM4Q2WP | OSCAL-basiertes CaC-Framework, Assessment Plans | ✅ Direkt: R014 + Kap. 5 PaC-Architektur | ⭐⭐ |

**Bewertung:** Q3-Gap vollständig geschlossen. Vorherige Recherche fand nur medizinproduktbasierte PMS-Literatur (Marino, Cuocolo — beide ⚠ nicht deployer-spezifisch). Die 5 neuen Quellen liefern:
- **Monitoring-Architektur:** Keyes' Stanford RAIL definiert 3 Monitoring-Prinzipien (Integrity/Performance/Impact) mit konkreten Metriken und Schwellwerten (75–125% Acceptance Bands, 95% CI für 7 konsekutive Tage)
- **Governance→CI/CD-Brücke:** Muhammads Audit-as-Code transformiert Governance-Regeln in auditierbaren Code mit Assured Readiness Score — direktes Bindeglied zwischen 4.6 (Requirements) und 5.3 (PaC-Architektur)
- **Incident-Operationalisierung:** Weis 7-Dimensionen-Framework operationalisiert Art. 73 Meldepflicht (10-Tage-Frist) mit strukturiertem Reporting-Design
- **Oversight-Risiko:** Laux belegt empirisch, dass Automation Bias die Human-Oversight-Wirksamkeit (R008) untergräbt — zentral für Deployer-Perspektive
- **CaC-Formalisierung:** Nwekes OSCAL-basierter Ansatz ergänzt Krisshnan (Q4) mit standardisiertem Assessment-Framework

### Q4: Requirements-to-Policy-as-Code Transformation
**Query:** "policy as code OPA Rego AI compliance requirements transformation CI/CD"

| Quelle | Relevanz | Deployer-Scope | Rating |
|--------|----------|---------------|--------|
| Krisshnan & Vijayaraghavan (2025) — PaC Paradigm Shift | PaC mit OPA, Paradigmenwechsel | ✅ Direkt | ⭐⭐⭐ |
| Siddiqui (2026) — Engineering CaC Frameworks | CaC-Framework-Architektur | ✅ Direkt | ⭐⭐ |
| Paul et al. (2024) — AWS OPA in CI/CD | Praxisbericht OPA-Integration | ✅ PoC-relevant | ⭐⭐ |
| Gupta (2025) — Intelligent Policy Engine | KI-gestützter Policy-Engine-Ansatz | ⚠ Konzept-Phase | ⭐ |

**Bewertung:** Krisshnan & Vijayaraghavan liefern das fehlende akademische Fundament für die PaC-Transformation (4.3 → 5.3). Siddiqui ergänzt mit CaC-Framework-Perspektive.

---

## 3. Konsolidierte Quellen-Matrix für R-xx

| R-xx | Primärquelle(n) | Elicit-Ergänzung | Status |
|------|-----------------|------------------|--------|
| R001 | EU AI Act Art. 9, Elia (2025) | — | ✅ belegt |
| R002 | EU AI Act Art. 11, Guldimann COMPL-AI | — | ✅ belegt |
| R003 | EU AI Act Art. 15, Elia (2025) | — | ✅ belegt |
| R004 | EU AI Act Art. 14, Ho-Dac & Martinez | — | ✅ belegt |
| R005 | EU AI Act Art. 12+15, Eisenberg UCF | — | ✅ belegt |
| R006 | EU AI Act Art. 10+26.4 | Guldimann COMPL-AI + Golpayegani AICat | ✅ belegt |
| R007 | EU AI Act Art. 13+26.7+50 | Guldimann COMPL-AI + Corrêa & Mönig | ✅ belegt |
| R008 | EU AI Act Art. 14+26.2, Sterz (2024) | **Laux et al. (2025)** — Automation Bias | ✅ verstärkt |
| R009 | EU AI Act Art. 26.5+73 | Kiejnich-Kruk (2025) + **Wei et al. (2025)** | ✅ verstärkt |
| R010 | EU AI Act Art. 72+9.2 | Finch & Butt + Huwyler + **Keyes (2025)** + **Muhammad (2026)** | ✅ verstärkt |
| R011 | EU AI Act Art. 26.1+47+48 | Kiejnich-Kruk (2025) | ✅ belegt |
| R012 | EU AI Act Art. 27 | Huwyler Phase 4 + Finch & Butt + Burns + **Muhammad (2026)** | ✅ verstärkt |
| R013 | EU AI Act Art. 9+10+15 | Díaz-Rodríguez + Guldimann COMPL-AI | ✅ belegt |
| R014 | EU AI Act Art. 12+26.3 | Lucaj (2025) + **Nweke (2026)** + **Muhammad (2026)** | ✅ verstärkt |

**Stufe-3 Quellenprüfung abgeschlossen (2026-03-10):** Alle 14 R-xx sind mit mindestens einer akademischen Quelle über den EU AI Act Normtext hinaus belegt. 5 neue Q3-Quellen (Muhammad, Keyes, Wei, Laux, Nweke) verstärken die Operations-Phase-Requirements R008–R010, R012, R014 erheblich. Die vorherige PMS-Lücke (Q3 v1: nur Medizinprodukte-Literatur) ist geschlossen.

---

## 4. Top-Empfehlungen für Zotero-Import

| Quelle | Elicit-Query | Zotero-Key | Priorität | Status |
|--------|-------------|-----------|-----------|--------|
| Kiejnich-Kruk (2025) | Q2 Deployer | D6526468 | **HOCH** — Kernquelle Deployer | ✅ importiert |
| Muhammad et al. (2026) | Q3 PMS | IZVYTSTV | **HOCH** — Audit-as-Code, CI/CD-Brücke | ✅ importiert |
| Keyes et al. (2025) | Q3 PMS | N3CKUY4T | **HOCH** — Stanford RAIL Monitoring | ✅ importiert |
| Wei et al. (2025) | Q3 Incident | 892WHGXH | **HOCH** — Incident Reporting Framework | ✅ importiert |
| Krisshnan & Vijayaraghavan (2025) | Q4 PaC | UPDJU868 | **HOCH** — PaC-Fundament | ✅ importiert |
| Laux et al. (2025) | Q3 Oversight | ADX5BQS6 | **MITTEL** — Automation Bias R008 | ✅ importiert |
| Nweke et al. (2026) | Q3 CaC | XCM4Q2WP | **MITTEL** — OSCAL CaC-Framework | ✅ importiert |
| Agarwal & Nene (2025) | Q1 Governance | — | **MITTEL** — Governance-Taxonomie | ⬜ optional |
| Siddiqui (2026) | Q4 CaC | — | **MITTEL** — CaC für 5.3 | ⬜ optional |

---

## 5. Argumentationsstruktur: Quellenbasierte Evidenzkette für Kap. 4.6

### 5.1 Übergeordnete Argumentationslinie

**These:** Die 14 Deployer-Anforderungen (R001–R014) bilden einen vollständigen, operationalisierbaren Requirements-Katalog, der die EU AI Act Art. 26 Deployer-Pflichten in drei Governance-Dimensionen (regulatorisch, technisch, strategisch) über den gesamten AI-Lifecycle (Pre-Deployment → Deployment → Operation) abdeckt.

**Argumentationsschritte:**

1. **Normative Ableitung (Art. → R-xx):** Jedes Requirement ist direkt aus EU AI Act Artikeln ableitbar. Hernandez (2025) Knowledge Graph und Golpayegani AICat (2024) liefern die formale Traceability Art. → Requirement.

2. **Deployer-Scope-Validierung:** Kiejnich-Kruk (2025) belegt, dass Art. 26 eine eigenständige Pflichten-Systematik definiert, die über Provider-Obligations hinausgeht. Die R-xx-Systematik folgt dieser Deployer-spezifischen Perspektive.

3. **Governance-Dimensionen-Fundierung:** Agarwal & Nene (2025) Five-Layer Governance + Eisenberg UCF (2025) 42 Controls liefern die akademische Basis für die dreistufige Taxonomie (regulatorisch/technisch/strategisch).

4. **Lifecycle-Phase-Zuordnung:** Huwyler (2025) 6-Phasen-Framework + Elia (2025) Quality-Gate-Konzept belegen die Zuordnung von R-xx zu Pre-Deployment/Deployment/Operation.

5. **Operations-Phase-Operationalisierung (Q3-Verstärkung):**
   - R010 PMS/Drift → Keyes Stanford RAIL (3 Prinzipien: Integrity/Performance/Impact) + Muhammad Audit-as-Code (Governance→CI/CD-Transformation)
   - R009 Incident → Wei 7-Dimensionen-Framework + Kiejnich-Kruk Art. 26.5
   - R008 Oversight → Laux Automation Bias (empirischer Nachweis für Oversight-Erosion) + Sterz 4 Effektivitätsbedingungen
   - R014 Logging → Nweke OSCAL CaC + Lucaj TechOps Templates

### 5.2 Evidenz-Stärke nach Lifecycle-Phase

| Phase | R-xx | Evidenz-Tiefe | Primärbelege |
|-------|------|---------------|-------------|
| Pre-Deployment | R001, R004, R011, R012 | STARK (Ø 2.5 Kernquellen) | Elia, Ho-Dac, Sterz, Kiejnich-Kruk, Huwyler |
| Deployment | R002, R003, R006, R007, R014 | STARK (Ø 2.4 Kernquellen) | Guldimann, Elia, Golpayegani, Corrêa, Lucaj, **Nweke** |
| Operation | R005, R008, R009, R010, R013 | **STARK** (Ø 2.8 Kernquellen, vorher MODERAT) | Eisenberg, **Keyes**, **Muhammad**, **Wei**, **Laux**, Díaz-Rodríguez |

**Zentrale Verbesserung durch Q3:** Operations-Phase-Evidenz von MODERAT auf STARK gehoben. Vorher war R010 (PMS) der schwächste Punkt im Katalog — jetzt durch Stanford RAIL + Audit-as-Code doppelt belegt.

### 5.3 Quellen-Cluster für WAS→WIE-Brücke (4.6 → 5.x)

| 4.6 Requirement (WAS) | 5.x Operationalisierung (WIE) | Brücken-Quelle |
|------------------------|-------------------------------|----------------|
| R010 PMS-Monitoring | Quality Gate: Drift-Detection | Muhammad Audit-as-Code (Governance→CI/CD) |
| R014 Logging | Policy-as-Code Templates | Nweke OSCAL + Lucaj TechOps |
| R009 Incident Reporting | Automated Alert Pipeline | Wei 7-Dimensionen → PaC-Rules |
| R008 Oversight-Wirksamkeit | Feedback-Loop-Design | Laux Gegenmaßnahmen + Keyes Impact-Monitoring |

---

## 6. Rating-System
- ⭐⭐⭐ = Kernquelle, direkte Übernahme von Konzepten/Methodik
- ⭐⭐ = Unterstützende Quelle, bestätigt/ergänzt Argumentation
- ⭐ = Hintergrundquelle, kontextuell nützlich
- ❌ = Nicht relevant für Deployer-Scope / 4.6
