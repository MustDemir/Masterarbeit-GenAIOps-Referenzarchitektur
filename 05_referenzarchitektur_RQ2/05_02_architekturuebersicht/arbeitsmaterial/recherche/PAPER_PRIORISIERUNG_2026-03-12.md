# Paper-Priorisierung für D_GATE_INCLUSION_RULE
**Datum: 2026-03-12 | Update: 2026-03-12 (Elia-Papers + 02_06-Scan integriert)**
**Basis: Keyword-Scan Phase 1 + Zotero-Kandidaten + Deep Reading Phase 2 + Blindfleck-Aufklärung**

---

## Bewertungskriterien

Priorisierung nach: **Welchen GAP in D_GATE_INCLUSION_RULE v1.0 schließt das Paper?**

### Identifizierte Gaps (aus D_GATE_INCLUSION_RULE v1.0):
- **GAP-A**: D3×D2-Override fehlt Sekundärbeleg (nur Laux 2024)
- **GAP-B**: D2-Paradigma fehlt Grundlagen-Paper (Kholkar/Muhammad/Nweke sind Spezialfälle)
- **GAP-C**: Q (Querschnitt) ist schwächste Dimension — kein Paper behandelt explizit Regulation→Gate-Mapping
- **GAP-D**: D1-Skalierung nach Risikoklasse (Cooper Full/Lite/Express → High-Risk/Limited-Risk)
- **GAP-E**: Empirische Validierung eines Gate-Frameworks fehlt komplett
- **GAP-F**: Rolle der Akteure (Provider/Deployer/Importer) bei Gate-Zuordnung
- **GAP-G** *(NEU)*: Kein existierendes Quality-Gate-Framework für AI als direkter Vergleichspunkt
- **GAP-H** *(NEU)*: Empirische D2-Daten für Automatisierbarkeitsgrad fehlen (Quantifizierung)

---

## TIER 0: CRITICAL — DIREKTE QUALITY-GATE-PAPERS FÜR AI *(NEU)*

| # | Paper | Gap | Begründung | Status |
|---|-------|-----|-----------|--------|
| 0a | **Elia & Bauer (2023)** — Quality Gates for Certifiable AI in Medicine | GAP-D, GAP-E, GAP-G | **EINZIGES Paper das Quality Gates für AI definiert.** 5 Lifecycle-QGs (Data/Software/Model/Deployment/Maintenance) mit risk-basierten Kriterien. Direkte Cooper-Adaptation. Stakeholder-Inklusion + Domain-Embedding als Gate-Design-Prinzipien. ISO 13485 + MDR + EU AI Act Mapping. **Fundament für D1-Skalierung.** | ✅ DEEP READ |
| 0b | **Elia et al. (2025)** — MQG4AI: Towards Responsible High-Risk AI | GAP-C, GAP-D, GAP-E, GAP-G | **Evolution von Elia 2023 → generisches Framework.** Collection-QGs + Leaf-QGs Hierarchie. Information-Management-Integration. 6 Lifecycle-Phasen (+ Decommissioning). EU AI Act Art. 17 QMS-Mapping (13 Requirements!). Fidelity-Robustness-Score als konkrete Metrik. Risk-based scaling mit 8 Mechanismen. GitHub-Repo verfügbar. **Schließt GAP-G (direkter Vergleichspunkt) + stärkt GAP-C (Regulation→Gate) + GAP-D (Risk-Scaling) + GAP-E (Use-Case-Illustration).** | ✅ DEEP READ |

**Bewertung:** Diese beiden Papers sind für D_GATE_INCLUSION_RULE **wichtiger als alle TIER-1-Papers**, weil sie das EINZIGE existierende Quality-Gate-Framework für AI liefern. Sie definieren den direkten Related-Work-Vergleichspunkt und das Abgrenzungsziel.

**Kernunterschied Elia vs. Demir:** Elia = domänenspezifisch (Medizin) + QG als Wissensmanagement-Methodik. Demir = domänenübergreifend (Enterprise) + QG als CI/CD-Gate mit Policy-as-Code-Automatisierung + EU AI Act Compliance-Enforcement.

---

## TIER 0b: CRITICAL — EMPIRISCHE D2-DATEN *(NEU aus 02_06)*

| # | Paper | Gap | Begründung | Status |
|---|-------|-----|-----------|--------|
| 0c | **Antiya (2020)** — Automating ISO 27001 Compliance | GAP-H, GAP-E | **75% der ISO 27001 Controls automatisierbar** (85/114). 70% Audit-Zeit-Reduktion. 83% Fehlerreduktion. Einzige quantifizierte empirische Basis für D2-Automatisierbarkeitsgrad. Übertragbar auf AI Act Controls. | ⚡ Abstract gelesen |
| 0d | **Rebbana (2025)** — Compliance Gates for Cloud Governance | GAP-E, GAP-D | **76% Governance-Overhead-Reduktion** durch Compliance-Gates. Prevention-fokussiert (= Gate als Präventionsmechanismus, nicht nur Prüfung). Direkte Gate-Terminologie! | ⚡ Abstract gelesen |
| 0e | **Alugunuri (2022)** — OPA/Rego in CI/CD | GAP-B, GAP-H | **89% Compliance-Failure-Reduktion** durch Policy-as-Code in CI/CD. OPA/Rego als konkretes Tooling. Stärkt D2-Paradigma mit empirischen Zahlen. | ⚡ Abstract gelesen |

**Bewertung:** Diese 3 Papers liefern die **fehlenden empirischen Zahlen** für D2-Automatisierbarkeit und Gate-Wirksamkeit. Antiya ist besonders wertvoll: eine Zahl wie "75% automatisierbar" macht D2-Argumentation sofort greifbar.

---

## TIER 1: MUST-READ (schließen kritische Gaps)

| # | Paper | Gap | Begründung | Quelle |
|---|-------|-----|-----------|--------|
| 1 | **Laux & Ruschemeier (2025)** — Automation Bias in the AI Act | GAP-A | Einziges Paper das D3×D2-Override empirisch fundiert. Automation Bias = WARUM First-Degree nicht voll automatisierbar sein darf. | Zotero |
| 2 | **Sarathe et al. (2025)** — Policy as Code: Paradigm Shift | GAP-B | Paradigma-Paper für gesamte D2-Dimension. Kholkar=Spezialfall (Prompt), Muhammad=Pipeline, Nweke=Traceability. Sarathe = übergeordnetes Konzept. | Zotero |
| 3 | **Guldimann et al. (2025)** — COMPL-AI Framework | GAP-C, GAP-E | 18 Q-Keywords. COMPL-AI = Compliance-Assessment-Framework für AI Act. Könnte den Q-Gap schließen: Wie mappt man Regulation → prüfbare Benchmarks? Ggf. auch empirische Validierung. | Ordner 02_04_02 |

**Erwarteter Beitrag:** Diese 3 Papers schließen die 3 kritischsten Gaps (A, B, C).

---

## TIER 2: SHOULD-READ (stärken existierende Dimensionen)

| # | Paper | Gap | Begründung | Keywords |
|---|-------|-----|-----------|----------|
| 4 | **Burns et al. (2025)** — AI Governance: Achieving EU AI Act Compliance | GAP-D, GAP-F | 93 Keywords total (67 D1!). Höchster Score nach Laux. "Achieving Compliance" suggeriert operationale Umsetzung. Könnte D1-Skalierung nach Risikoklasse + Akteursrollen liefern. | D1:67, Q:22 |
| 5 | **Agarwal & Nene (2025)** — Five-Layer Framework for AI Governance | GAP-C, GAP-D | 5-Layer-Modell → könnte die Governance-Schichten liefern die zwischen Regulation und Gate vermitteln. | Zotero |
| 6 | **Kiejnich-Kruk (2025)** — Obligations of Importers, Distributors, Deployers | GAP-F | Rollenspezifische Pflichten unter AI Act. Relevant für: WER ist Gatekeeper bei welchem Gate? Provider-Gate vs. Deployer-Gate. | Zotero |
| 7 | **Hernandez (2025)** — AI Act Knowledge Graph | GAP-C | 72 Keywords (50 D1). Knowledge Graph = maschinenlesbare Regulation-Struktur. Könnte Q-Dimension stärken (Clause→Control Mapping als Graph). | D1:50, Q:13 |

**Erwarteter Beitrag:** Stärken D1+Q+Akteurs-Dimension. Burns und Hernandez haben hohe Keyword-Scores.

---

## TIER 3: NICE-TO-HAVE (bestätigen/ergänzen, keine neuen Gaps)

| # | Paper | Potenzial | Keywords | Einschätzung |
|---|-------|-----------|----------|-------------|
| 8 | **Huwyler (2025)** — Unified Framework | Q:10, D1:30 | Unified = integriertes Framework, aber vermutlich keine Gate-spezifische Logik |
| 9 | **Diaz-Rodriguez et al. (2023)** — Connecting Ethics & Regulation | Q:16, D1:22 | Ethik→Regulation-Brücke. Relevant für Grundlagen, nicht für Gate-Entscheidung |
| 10 | **Finch & Butt (2025)** — Gaps in Governance | D1:31, Q:11 | Governance-Gaps identifizieren → bestätigt unsere Q-Lücke, liefert aber vermutlich keine Lösung |
| 11 | **Sarra (2024)** — AI in Decision-making | D3:12, Q:16 | Decision-making + Oversight → bestätigt Laux, vermutlich keine neuen D3-Einsichten |
| 12 | **Pistilli (2023)** — Stronger Together (Ethical Charters) | D1:34 | Ethical Charters → eher Kap. 2/4 Material, nicht Gate-Entscheidung |
| 13 | **Keyes et al. (2025)** — Monitoring Deployed AI in Healthcare | D3 | Praktisches Beispiel für Second-Degree Oversight → schön aber nicht gap-schließend |
| 14 | **Wei & Heim (2025)** — Incident Reporting Systems | D3 | Incident Reporting = Second-Degree → bestätigt Laux-Taxonomie |
| 15 | **Ho-Dac & Martinez (2024)** — Human Oversight | D3:8 | Human Oversight allgemein → Laux ist stärker |
| 16 | **Golpayegani et al. (2024)** — AICat | D2:5, D1:6 | AI Cataloguing → Deliverable-Katalog, aber Lucaj ist konkreter |
| 17 | **Taeihagh (2025)** — Governance of GenAI | D1:20, D2:5 | Governance-Überblick, vermutlich keine Gate-spezifischen Insights |
| 18 | **Novelli et al. (2024)** — GenAI in EU Law | D1:20 | Rechtliche Analyse, nicht operationalisierbar |
| 19 | **Radanliev et al. (2025)** — GenAI Cybersecurity | D1:12, D2:4 | Security-Fokus, tangential |
| 20 | **Li et al. (2021)** — Trustworthy AI | D1:3 | Grundlagen, nicht spezifisch genug |

---

## TIER 4: NICHT RELEVANT für D_GATE_INCLUSION_RULE

Restliche Papers aus Phase-1-Scan mit <20 Keywords total oder ohne Gate-Bezug.
→ Können für andere Kapitel relevant sein (Kap. 2 Grundlagen, Kap. 4 Anforderungsanalyse), aber nicht für 5.2.2.

---

## Zusätzliche Papers aus Ordner 04_Kap5 (NICHT im Keyword-Scan)

Folgende Papers liegen im Kap5-Ordner, waren aber NICHT im Phase-1-Keyword-Scan (der nur 02_04_02 abdeckte):

| Paper | Potenzielle Relevanz |
|-------|---------------------|
| **Angelov** — Framework for Analysis & Design of Software Reference Architectures | Meta-Methodik für Referenzarchitektur-Design → DSR-Verankerung |
| **Baqar et al.** — AI-Augmented CI/CD Pipelines | D2: CI/CD-Integration von AI-Checks |
| **Garg et al.** — CI/CD for MLOps | D2: MLOps Pipeline-Patterns |
| **Mahr et al.** — Reference Architecture for Deploying LLM Applications | Vergleichsarchitektur → Related Work |
| **Pourmajidi et al.** — Reference Architecture for Governance of Cloud Native Apps | Q: Governance-Architektur als Cloud-Native Pattern |
| **Sovrano et al.** — Simplifying Software Compliance with AI Technologies | D2+Q: Compliance-Vereinfachung durch AI |

**Hinweis:** Diese wurden WEDER keyword-gescannt NOCH deep-gelesen!

---

## Ordner 02_06 (Compliance-as-Code) — ✅ GESCANNT

Ordner `02_06_Compliance_as_Code_und_Policy_as_Code` wurde in dieser Session gescannt:
- **9 PDFs** gefunden, davon **5 neue** (nicht in anderen Ordnern)
- **3 als CRITICAL eingestuft**: Antiya (2020), Rebbana (2025), Alugunuri (2022) → jetzt TIER 0b
- **2 als HIGH eingestuft**: Adetayo (2023), Sinan (2025)
- **4 Duplikate** aus anderen Ordnern: Baqar, Di Martino, Pourmajidi, Sovrano

### Weitere 02_06-Papers (HIGH, nicht CRITICAL):

| Paper | Relevanz | Status |
|-------|----------|--------|
| **Adetayo (2023)** — Policy-as-Code for Hybrid Cloud | D2: 70% Audit-Zeit-Reduktion, konkrete PaC-Implementierung | ⚡ Abstract |
| **Sinan (2025)** — 10 Security Control Types | D2: Left-Shift-Automation-Patterns, Control-Taxonomie | ⚡ Abstract |

---

## Ordner Pourmajidi — ✅ BESTEHENDE ANALYSE VORHANDEN

Analyse bereits vorhanden in: `02_rigor_theorie_stand_forschung/Analyse_Pourmajidi_und_Gesamtvergleich.md`
- **Key Finding für D_GATE:** Pourmajidi hat "Pre-CD Checkpoint" aber KEIN formalisiertes Gate-Template
- **Abgrenzung:** "Pourmajidi liefert die Governance-Infrastruktur, Demir liefert die Governance-Logik für GenAI"
- **4-Stufen:** Code-level → CI-level → Pre-CD → Post-CD Governance
- **Kein Deep Reading nötig** — bestehende Analyse ist ausreichend für Gate-Relevanz

---

## Empfohlene Lesereihenfolge (AKTUALISIERT)

### ✅ ABGESCHLOSSEN (Deep Read):
- Cooper (2008) — D1 Foundational
- Laux (2024) — D3 Primary
- Kholkar (2025) — D2 High
- Lucaj (2025) — D1+Q Central
- Feng (2024) — D1 Medium
- Muhammad (2026) + Nweke (2026) — D2 Critical
- **Elia & Bauer (2023) — D1+D_GATE CRITICAL** *(NEU)*
- **Elia et al. (2025) MQG4AI — D1+Q+D_GATE CRITICAL** *(NEU)*

### Runde 1 (nächste Priorität — vor Elicit):
1. **Laux & Ruschemeier (2025)** → GAP-A schließen (D3×D2-Override)
2. **Sarathe et al. (2025)** → GAP-B schließen (D2-Paradigma)
3. **Guldimann et al. (2025)** → GAP-C+E prüfen (Regulation→Benchmark)

### Runde 2 (TIER 0b empirische Daten — Deep Read oder gezielte Extraktion):
4. **Antiya (2020)** → GAP-H: 75% Automatisierbarkeit quantifizieren
5. **Rebbana (2025)** → GAP-E: 76% Overhead-Reduktion + Gate-als-Prävention
6. **Alugunuri (2022)** → GAP-B+H: OPA/Rego + 89% Failure-Reduktion

### Runde 3 (nach Elicit, wenn Gaps bleiben):
7. **Burns et al. (2025)** → D1-Skalierung + Akteure
8. **Agarwal & Nene (2025)** → Governance-Schichten
9. **Hernandez (2025)** → Knowledge-Graph für Q
10. **Kiejnich-Kruk (2025)** → Akteurs-Rollen

### Runde 4 (nur bei spezifischem Bedarf):
11+ TIER-3-Papers → nur wenn Elicit-Suchen Lücken aufzeigen

---

## Zusammenfassung (v3.0 — AKTUALISIERT 2026-03-12)

| Kategorie | Anzahl | Status |
|-----------|--------|--------|
| DEEP gelesen | **11** | ✅ (+2 Elia + Laux/Ruschemeier + Sarathe + Guldimann) |
| TIER 0b (empirische D2-Daten) | 3 | ⚡ Abstract gelesen, Deep Read ausstehend |
| TIER 1 (MUST-READ) | 3 | ✅ ALLE GELESEN (Laux/Ruschemeier, Sarathe, Guldimann) |
| TIER 2 (SHOULD-READ) | 4 | ❌ Ausstehend |
| TIER 3 (NICE-TO-HAVE) | 13 | ❌ Optional |
| Kap5-Ordner | 6 | ❌ Nicht deep gelesen |
| Ordner 02_06 | 5 neue | ✅ Abstract-Scan, 3 als CRITICAL eingestuft |
| Pourmajidi | 1 | ✅ Bestehende Analyse ausreichend |
| **TOTAL relevant für D_GATE_INCLUSION_RULE** | **~22 Papers** | **11 deep gelesen, 3 abstract-gescannt, 8 ausstehend** |

---

## NEU: Gap-Coverage nach Update

| Gap | Beschreibung | Abgedeckt durch | Status v3.0 |
|-----|-------------|-----------------|-------------|
| GAP-A | D3×D2-Override Sekundärbeleg | Laux 2024 (konzeptionell) + **Laux/Ruschemeier 2025** (Automation Bias, empirisch) | 🟢⁻ Gestärkt, eigene Design-Entscheidung nötig |
| GAP-B | D2-Paradigma Grundlagen-Paper | **Sarathe 2025** (PaC-Paradigma, 3-Komp., 5 Stufen, DSOMM, 63.7%) | 🟢 GESCHLOSSEN (Caveat: CAC/AAC-Differenzierung eigene Erweiterung) |
| GAP-C | Q-Dimension: Regulation→Gate-Mapping | **Elia 2025** (Art.17 → 13 QMS-Reqs) + **COMPL-AI** (17 Art. → 27+ Benchmarks) | 🟢⁻ 70-80% (Demir-Synthese noch nötig) |
| GAP-D | D1-Skalierung nach Risikoklasse | **Elia 2023** (Risk-Dimensions) + **Elia 2025** (8 Scaling-Mechanismen) | 🟢 GESCHLOSSEN |
| GAP-E | Empirische Validierung Gate-Framework | Antiya 75% + Rebbana 76% + Alugunuri 89% + Sarathe 63.7% + **COMPL-AI** 12-LLM-Eval | 🟡 50-60% (eigene Validierung R001-R015 ausstehend) |
| GAP-F | Akteurs-Rollen Provider/Deployer | Elia 2025 (active/consulting/passive) + Laux/Ruschemeier (asymm. Provider/Deployer) | 🟡 Teilweise (kein vollständiges Gate-Level-Mapping) |
| GAP-G | Direkter QG-Vergleichspunkt für AI | **Elia 2023 + 2025** = einziges existierendes QG4AI-Framework | 🟢 GESCHLOSSEN |
| GAP-H | Empirische D2-Quantifizierung | Antiya 75%, Alugunuri 89%, Rebbana 76%, Sarathe DSOMM-Level | 🟡 Zahlen vorhanden, Safety-Critical-Schwelle offen |
