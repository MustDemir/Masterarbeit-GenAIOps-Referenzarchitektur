# Session-Bericht: Phase 1+2 Literaturarbeit für D_GATE_INCLUSION_RULE
**Datum: 2026-03-12 | Status: Phase 2 ABGESCHLOSSEN, Phase 3 AUSSTEHEND**

---

## Überblick: Was wurde gemacht, was steht aus?

### Phase 1: Keyword-Scan (ABGESCHLOSSEN)
- **53+ Papers** aus 5+ Ordnern gescannt (Abstract-Level)
- **30 PDFs** aus `/02_04_02_EU_AI_Act/` systematisch mit D1/D2/D3/Q-Keywords analysiert
- **Ergebnis:** Coverage-Matrix mit Top-20 Ranking → siehe `KEYWORD_COVERAGE_ANALYSE_2026-03-12.md`
- **Tiefe:** NUR Keyword-Zählung in Abstracts, KEINE inhaltliche Analyse

### Phase 2: Deep Reading (ABGESCHLOSSEN — 6 von ~14 relevanten Papers)
- **6 Papers** als Tiefenlektüre mit strukturierter D1/D2/D3-Extraktion
- **Ergebnis:** 6 DEEP_READING_*.md Dateien + konsolidierte D_GATE_INCLUSION_RULE v1.0

### Phase 3: Elicit-Suchen (AUSSTEHEND)
- 4 Queries formuliert in `ELICIT_SEARCH_PLAN_2026-03-12.md`
- NICHT ausgeführt

---

## DETAIL: Was wurde DEEP gelesen (Phase 2)?

| # | Paper | Dimension | Status | Datei |
|---|-------|-----------|--------|-------|
| 1 | **Cooper (2008)** — Stage-Gate Process | D1 FOUNDATIONAL | ✅ DEEP READ | DEEP_READING_COOPER_2008.md |
| 2 | **Laux (2024)** — Institutionalised Distrust | D3 PRIMARY | ✅ DEEP READ | DEEP_READING_LAUX_2024.md |
| 3 | **Kholkar & Ahuja (2025)** — Policy-as-Prompt | D2 HIGH | ✅ DEEP READ | DEEP_READING_KHOLKAR_2025.md |
| 4 | **Lucaj et al. (2025)** — TechOps Templates | D1+Q CENTRAL | ✅ DEEP READ | DEEP_READING_LUCAJ_2025.md |
| 5 | **Feng et al. (2024)** — Normative Requirements | D1 MEDIUM | ✅ DEEP READ | DEEP_READING_FENG_2024.md |
| 6 | **Muhammad (2026) + Nweke (2026)** — Audit/Compliance-as-Code | D2 CRITICAL | ✅ DEEP READ | DEEP_READING_MUHAMMAD_NWEKE_2026.md |

---

## DETAIL: Was wurde NICHT deep gelesen (nur Keyword-Scan oder Zotero-Identifikation)?

### A) Zotero-Kandidaten (identifiziert, NICHT deep gelesen)

| # | Paper | Dimension | Status | Key Findings (nur aus Titel/Abstract) |
|---|-------|-----------|--------|---------------------------------------|
| 7 | **Agarwal & Nene (2025)** — Five-layer AI governance framework | D1+Q | ❌ NICHT GELESEN | 5-Layer-Modell → potenzielle D1-Ergänzung für Governance-Schichten |
| 8 | **Keyes et al. (2025)** — Monitoring Deployed AI in Healthcare | D3 | ❌ NICHT GELESEN | Praktisches Monitoring → Second-Degree Oversight Operationalisierung |
| 9 | **Kiejnich-Kruk (2025)** — Obligations Importers/Distributors/Deployers | D1 | ❌ NICHT GELESEN | Rollen-Pflichten → Gate-Zuordnung nach Akteursrolle |
| 10 | **Laux & Ruschemeier (2025)** — Automation Bias in AI Act | D3 | ❌ NICHT GELESEN | Automation Bias → kritisch für D3×D2-Override-Begründung! |
| 11 | **Sarathe et al. (2025)** — Policy as Code: Paradigm Shift | D2 | ❌ NICHT GELESEN | Paradigma-Paper → D2 Grundlagen-Ergänzung |
| 12 | **Wei & Heim (2025)** — Incident Reporting Systems | D3 | ❌ NICHT GELESEN | Incident Reporting → Second-Degree Oversight Design |

### B) Phase-1-Papers mit hoher Keyword-Relevanz (nur Keyword-Scan, kein Deep Read)

| Rank | Paper | D1 | D2 | D3 | Q | Total | Status |
|------|-------|----|----|----|----|-------|--------|
| 2 | **Burns et al. (2025)** AI Governance | 67 | 2 | 2 | 22 | 93 | ❌ Nur Keywords |
| 3 | **Hernandez (2025)** AI Act Knowledge Graph | 50 | 2 | 7 | 13 | 72 | ❌ Nur Keywords |
| 4 | **Governance (2025)** Unified Control Framework | 40 | 2 | 3 | 12 | 57 | ❌ Nur Keywords |
| 5 | **Huwyler (2025)** Unified Framework | 30 | 1 | 8 | 10 | 49 | ❌ Nur Keywords |
| 6 | **Diaz-Rodriguez et al. (2023)** Connecting Ethics | 22 | 4 | 6 | 16 | 48 | ❌ Nur Keywords |
| 7 | **Finch & Butt (2025)** Gaps in Governance | 31 | 3 | 3 | 11 | 48 | ❌ Nur Keywords |
| 9 | **Pistilli (2023)** Stronger Together | 34 | 2 | 1 | 4 | 41 | ❌ Nur Keywords |
| 10 | **Guldimann et al. (2025)** COMPL-AI Framework | 21 | 1 | 0 | 18 | 40 | ❌ Nur Keywords |
| 11 | **Sarra (2024)** AI in Decision-making | 5 | 3 | 12 | 16 | 36 | ❌ Nur Keywords |

---

## Bewertung: Was fehlt für D_GATE_INCLUSION_RULE?

### Kritische Lücke 1: Laux & Ruschemeier (2025) — Automation Bias
- **Warum kritisch:** Begründet den D3×D2-Override (First-Degree → max. HYBRID)
- **Aktuell:** Override-Begründung stützt sich NUR auf Laux (2024). Das neuere Paper von Laux & Ruschemeier behandelt explizit Automation Bias → stärkt die Argumentation erheblich
- **Priorität:** ⭐⭐⭐⭐⭐ HÖCHSTE

### Kritische Lücke 2: Sarathe et al. (2025) — Policy-as-Code Paradigma
- **Warum kritisch:** D2-Grundlagen-Paper. Kholkar ist "Policy-as-Prompt" (Spezialfall), Muhammad ist "Audit-as-Code" (Pipeline). Sarathe liefert das übergeordnete Paradigma.
- **Aktuell:** D2 stützt sich auf 3 Papers, aber das Paradigma-Paper fehlt
- **Priorität:** ⭐⭐⭐⭐

### Moderate Lücke 3: Agarwal & Nene (2025) — Five-Layer Governance
- **Warum relevant:** Könnte D1-Schichten-Modell liefern (Governance Layer → Gate Layer)
- **Aktuell:** D1 stützt sich auf Cooper (Prozess) + Lucaj (Deliverables). Agarwal könnte die Governance-Perspektive ergänzen
- **Priorität:** ⭐⭐⭐

### Moderate Lücke 4: Burns et al. (2025) — AI Governance (93 Keywords!)
- **Warum relevant:** Höchster Keyword-Score nach Laux. 67 D1-Keywords → vermutlich sehr relevant für Gate-Eignung
- **Aktuell:** NUR Keyword-Zählung, KEIN inhaltlicher Beitrag extrahiert
- **Priorität:** ⭐⭐⭐

### Geringe Lücken (Nice-to-Have)
- Keyes (2025): Praktisches Monitoring-Beispiel für D3
- Wei & Heim (2025): Incident Reporting für Second-Degree
- Kiejnich-Kruk (2025): Rollenspezifische Obligations
- Hernandez (2025): Knowledge Graph → interessant aber nicht kritisch

---

## Artefakte dieser Session

| Artefakt | Pfad | Status |
|----------|------|--------|
| DEEP_READING_COOPER_2008.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt |
| DEEP_READING_LAUX_2024.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt |
| DEEP_READING_KHOLKAR_2025.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt |
| DEEP_READING_LUCAJ_2025.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt |
| DEEP_READING_FENG_2024.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt |
| DEEP_READING_MUHAMMAD_NWEKE_2026.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt |
| D_GATE_INCLUSION_RULE_2026-03-12.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt (v1.0 ENTWURF) |
| KEYWORD_COVERAGE_ANALYSE_2026-03-12.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt (vorherige Session) |
| ELICIT_SEARCH_PLAN_2026-03-12.md | /05_referenzarchitektur_RQ2/ | ✅ Erstellt (vorherige Session) |
| SESSION_BERICHT_PHASE1_2_2026-03-12.md | /05_referenzarchitektur_RQ2/ | ✅ Dieses Dokument |

---

## Empfehlung: Nächste Schritte

### Sofort (vor Elicit):
1. **Laux & Ruschemeier (2025)** deep lesen → D3×D2-Override stärken
2. **Sarathe et al. (2025)** deep lesen → D2-Paradigma fundieren

### Dann Phase 3:
3. **4 Elicit-Suchen** ausführen → Gaps identifizieren
4. **D_GATE_INCLUSION_RULE v2.0** mit allen Quellen konsolidieren

### Danach:
5. **Alle 15 Requirements** durch D_GATE_INCLUSION_RULE laufen lassen → Konsistenz-Check
6. **chapter_state.yaml** aktualisieren
7. **Section 5.2.2 Preflight + GO** → Schreiben

---

## Hinweis zur Vollständigkeit
Die D_GATE_INCLUSION_RULE v1.0 ist QUELLENBASIERT (6 Papers deep gelesen), aber NICHT VOLLSTÄNDIG validiert. Insbesondere:
- D3×D2-Override braucht Laux/Ruschemeier-Bestätigung
- D2-Paradigma braucht Sarathe-Grundlage
- Phase-1-Papers mit hohen Keywords (Burns, Hernandez, Huwyler) sind inhaltlich unerschlossen
- Elicit-Suchen können weitere relevante Papers aufdecken
