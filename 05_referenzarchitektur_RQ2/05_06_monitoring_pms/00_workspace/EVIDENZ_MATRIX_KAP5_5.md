# Elicit-Style Evidenz-Matrix — Kap. 5.5
## Monitoring und Post-Market Surveillance

**Erstellt:** 2026-03-14 | **Methode:** Elicit Research Table Approach
**Scope:** 2 Zotero-Volltexte (Ray, Romeo) + 2 Elicit-Funde (Cuocolo, Khademi) + 2 Reuse-Quellen (Nweke, Muhammad) + D_5.5_CONTENT Decision

---

## Spalten-Definitionen (Forschungsfragen Q1–Q6)

| ID | Frage | Relevanz für Kap. 5.5 |
|----|-------|-----------------------|
| Q1 | Welche normativen Anforderungen stellt Art. 72 EU AI Act an Deployer im Post-Market Surveillance? | Abs. 1: Normative Basis PMS + Incident Reporting |
| Q2 | Wie wird Drift-Detection konzeptuell definiert und welche Methoden (PSI, Jensen-Shannon) werden eingesetzt? | Abs. 2: Drift-Detection Monitoring-Sidecar |
| Q3 | Welche Incident-Reporting-Pflichten ergeben sich aus Art. 26 Abs. 5 + Art. 73 für Deployer? | Abs. 3: Incident Reporting + Eskalationslogik |
| Q4 | Welche Monitoring-Architekturen/Sidecar-Pattern existieren für AI-Systeme in Production? | Abs. 2–3: Technische Umsetzung Monitoring |
| Q5 | Wie verbindet sich PMS/Monitoring mit dem Evidence Store (Monitoring-Window → Traceability)? | Abs. 4 (Bridge): PMS → Evidence Store → PoC |
| Q6 | Welche TRiSM-Frameworks strukturieren AI Governance inkl. Monitoring als Kernkomponente? | Abs. 1: Theoretische Einordnung + Taxonomy |

---

## Bewertungsskala

| Symbol | Bedeutung | Kriterium |
|--------|-----------|-----------|
| 🟢 | Tiefgehend | Zentrales Thema des Papers, mehrere Seiten, explizit |
| 🟠 | Moderat | Eigener Abschnitt oder mehrere Absätze |
| 🟡 | Erwähnt | 1–2 Sätze, oberflächlich |
| ⬛ | Nicht behandelt | Thema kommt nicht vor |

---

## Evidenz-Matrix

### Tier 1: CORE-Quellen

| Quelle | Zotero-Key | Q1 PMS-Norm | Q2 Drift | Q3 Incident | Q4 Monitoring-Arch | Q5 PMS→Evidence | Q6 TRiSM | Rolle |
|--------|-----------|-------------|----------|-------------|-------------------|-----------------|----------|-------|
| **Ray (2026)** Expert Systems | `AW3BMEEI` | 🟡 | 🟢 S.14 | ⬛ | 🟢 S.14 | 🟠 | 🟢 Abstract | Primärquelle TRiSM-Framework + Drift-Detection-Architektur. Section 3.6.3: PSI + Jensen-Shannon + Prometheus/Grafana/Datadog + Immutable Audit Logs |
| **Cuocolo et al. (2025)** Insights into Imaging | ❌ Zotero fehlt | 🟢 | 🟠 | 🟠 | 🟡 | 🟠 | ⬛ | Primärquelle Art. 72 PMS für Healthcare-Deployer. EU AI Act + MDR Deployer-Pflichten. Consensus-Empfehlungen ESR. Perfekt für Healthcare-PoC-Kontext |

### Tier 2: EMPFOHLENE Quellen

| Quelle | Zotero-Key | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Rolle |
|--------|-----------|----|----|----|----|----|----|-------|
| **Khademi et al. (2023)** arXiv | ❌ Zotero fehlt | ⬛ | 🟢 | ⬛ | 🟠 | ⬛ | ⬛ | PSI-Methodik für Drift-Detection. Stützt Ray 2026 Sekt. 3.6.3 konvergent. arXiv (Venue-Caveat nötig) |
| **Nweke & Yeng (2026)** IEEE Access | `XCM4Q2WP` | 🟠 | 🟡 | ⬛ | ⬛ | 🟢 | ⬛ | Reuse aus 5.4. "Monitoring-window semantics" = Brücke PMS→Evidence Store (S. 28258) |
| **Muhammad et al. (2026)** Sec. 1 | `IZVYTSTV` | ⬛ | ⬛ | ⬛ | 🟡 | 🟢 | ⬛ | Reuse aus 5.4. Assured Readiness Score + Traceability + Explainability als operative PMS-Metriken |

### Tier 3: RESERVIERT (andere Kapitel)

| Quelle | Zotero-Key | Warum nicht 5.5 | Besser geeignet für |
|--------|-----------|----------------|---------------------|
| **Romeo et al. (2025) ARPaCCino** | `JNX3V8EF` | Policy-as-Code via Agentic-RAG für IaC — kein Monitoring, kein PMS | Kap. 5.3 (Policy Engine, Rego-Generierung) oder Related Work |

---

## Evidenzstärke pro Frage

| Frage | Abdeckung | Bewertung | Empfehlung |
|-------|-----------|-----------|------------|
| Q1 — Art. 72 PMS Norm | Cuocolo 🟢, Nweke 🟠, EU AI Act (normativ) | **MODERAT–STARK** | ✅ Ausreichend. Cuocolo hinzufügen (Zotero-Import) |
| Q2 — Drift-Detection | Ray 🟢 S.14, Khademi 🟢 | **STARK** | ✅ Gut abgedeckt |
| Q3 — Incident Reporting | Cuocolo 🟠 (PMCF/Incidents), sonst normativ | **MODERAT** | ⚠️ Nur Cuocolo + EU AI Act Text. Kein dediziertes Paper. Elicit-Suche optional oder Q3 in Q1 integrieren |
| Q4 — Monitoring-Architektur | Ray 🟢 S.14 (Prometheus/Grafana), Khademi 🟠 | **MODERAT** | ✅ Ray deckt ab. Deployment-Pattern (Sidecar) = Eigenleistung |
| Q5 — PMS→Evidence Store | Nweke 🟢, Muhammad 🟢 (Reuse) | **STARK** | ✅ Bridge-Funktion gut belegt |
| Q6 — TRiSM Framework | Ray 🟢 Abstract+Body | **MODERAT** | ⚠️ Single source. Ray ist aber 67-Seiten-Review — vertretbar |

---

## Gap-Analyse

### SCHWACH (Lücken):

**Q3 — Incident Reporting (Art. 26.5 + Art. 73):** Kein dediziertes Paper identifiziert.
→ **Empfehlung:** Q3 normativ behandeln (Art. 73 EU AI Act als Primärquelle) + Cuocolo (2025) als stützendes Paper für "serious incidents in medical AI".

**Q6 — Single-Source Risk (TRiSM):** Nur Ray (2026).
→ **Akzeptabel**, da 67-Seiten-Review mit eigener Taxonomie. Literaturlage für TRiSM in GenAI ist dünn.

### FEHLENDE Zotero-Einträge (vor GO hinzufügen):
- ❌ **Cuocolo et al. (2025)**: DOI: 10.1186/s13244-025-02146-8 — PDF verfügbar (Open Access)
- ❌ **Khademi et al. (2023)**: DOI: 10.48550/arXiv.2302.00775 — arXiv PDF frei

---

## Synthese: Quellen-Zuordnung zu Absätzen

| Absatz | Argumentativer Move | Primärquelle | Sekundärquelle |
|--------|---------------------|-------------|----------------|
| Abs. 1 | Art. 72 PMS als Deployer-Pflicht + TRiSM-Einordnung | Cuocolo et al. (2025) | Ray (2026), EU AI Act Art. 72 |
| Abs. 2 | Drift-Detection-Konzept: PSI + Jensen-Shannon + Monitoring-Sidecar-Pattern | Ray (2026, S. 14) | Khademi et al. (2023) |
| Abs. 3 | Incident Reporting Art. 26.5 + Art. 73 + Eskalationslogik | EU AI Act Art. 73 (normativ) | Cuocolo et al. (2025) |
| Abs. 4 | Bridge PMS → Evidence Store (Monitoring-Window-Semantik → quality_gate_results) | Nweke & Yeng (2026, S. 28258) | Muhammad et al. (2026, Sec. 1) |

**Bridge zu Abs. 5 (Brücke zu 5.6):**
"Die spezifizierte Monitoring-Architektur — bestehend aus Drift-Detection, Incident Reporting und Evidence-Store-Anbindung — wird in Abschnitt 5.6 am Azure-Stack (AKS, Prometheus, PostgreSQL) prototypisch instanziiert."

---

## Offene Fragen (vor GO)

1. **Cuocolo + Khademi in Zotero importieren?** → Ja, vor GO empfohlen (beide Open Access)
2. **Q3 Incident Reporting:** Elicit-Suche "AI serious incident reporting GenAI EU AI Act" nötig, oder normativ (Art. 73 EU AI Act als Primärquelle) ausreichend?
3. **Khademi (2023) Venue-Caveat:** arXiv-Preprint, Verwendung wie Joseph (2023) in 5.4 — transparent kennzeichnen?
4. **Monitoring-Sidecar-Pattern:** DSR-Eigenleistung (E5)? Ableitung aus Ray + Gatekeeper-Architektur aus 5.3?
