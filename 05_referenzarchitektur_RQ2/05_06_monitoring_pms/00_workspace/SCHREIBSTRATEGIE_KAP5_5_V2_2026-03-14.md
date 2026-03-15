# Schreibstrategie V2 Kap. 5.5 — Monitoring und Post-Market Surveillance
**Stand:** 2026-03-14 | **Budget:** ~800–900W (D_QUALITY_OVER_PAGES)
**Preflight:** PREFLIGHT_KAP5_5_MONITORING_PMS_V2.md ✅ GO-BEREIT
**Evidenz:** 4 CORE + 3 REUSE + 2 normative = 9 Quellen

---

## Argumentationsstruktur (4 Absätze)

| Abs. | Move | Primärquelle | Sekundärquelle | ~W |
|------|------|-------------|----------------|-----|
| 1 | Art. 72 PMS Deployer-Pflicht → Evidence Store muss laufzeitnah ausgewertet werden. TRiSM-Einordnung. G-OPS Gates als operative PMS-Instanzen. | Cuocolo et al. (2025) NWJ7SY5I | Ray (2026) AW3BMEEI, EU AI Act Art. 72 | ~200 |
| 2 | Drift-Detection: PSI + Jensen-Shannon. Monitoring-Sidecar-Pattern (DSR E5). 3-Quellen-Konvergenz. | Ray (2026, S. 14) AW3BMEEI | Khademi (2023) ILFAR2R2, Eck (2022) 7HUZPNSK | ~250 |
| 3 | Incident Reporting: Art. 26.5 + Art. 73. Agarwal-Typology AI Incidents. Eskalationslogik Drift→Threshold→Incident→Reporting. Evidence Store Partial Index (decision='FAIL'). | Agarwal & Nene (2026) GY5P52BE | Cuocolo (2025) NWJ7SY5I, EU AI Act Art. 73 | ~200 |
| 4 | Synthese: Monitoring-Window-Semantik → Evidence Store. S1–S5 komplett. Bridge zu 5.6 PoC. | Nweke & Yeng (2026, S. 28258) XCM4Q2WP | Muhammad (2026) IZVYTSTV | ~150 |

---

## Bridge von 5.4 (M9):
> "Das konzeptuelle Schema bildet die Grundlage für die in Abschnitt 5.5 spezifizierte Monitoring-Architektur, die eine laufzeitnahe Auswertung der persistierten Evidence Records im Sinne von Art. 72 EU AI Act (Post-Market Surveillance) ermöglicht. Die prototypische Instanziierung der fünf Komponenten auf dem Azure-Stack erfolgt in Abschnitt 5.6."

## Bridge zu 5.6:
> "Die spezifizierte Monitoring-Architektur — bestehend aus Drift-Detection (PSI/Jensen-Shannon), Incident Reporting (Art. 73) und Evidence-Store-Anbindung (Monitoring-Window) — wird in Abschnitt 5.6 am Azure-Stack (AKS, Prometheus, PostgreSQL) prototypisch instanziiert."

---

## Gate-Mapping (für Abs. 1):

| R-xx | Gate | Phase | Bezug |
|------|------|-------|-------|
| R010 | G-OPS-03 | Operation | Drift-Monitoring (Abs. 2) |
| R009 | G-OPS-04 | Operation | Incident Reporting (Abs. 3) |
| R005 | G-OPS-05 | Operation | Evidence-Completeness (Abs. 4) |

---

## DSR-Verankerung

- Peffers Step 3 (Design & Development): Monitoring = letzte Architekturkomponente S5
- Fünf-Säulen-Modell komplett: S1 (DP1-DP5) + S2 (Gates) + S3 (Pipeline) + S4 (Evidence) + **S5 (Monitoring)**
- DSR-Eigenleistung **E5**: Monitoring-Sidecar-Pattern (Synthese Ray TRiSM + Gatekeeper aus 5.3)
- Limitation **L4** (neu): Kein Real-Time-Stream-Processing im PoC (Batch-basiert)

---

## Negativ-Checklist
- ❌ Provider-Perspektive (Art. 16)
- ❌ Retirement (PK-SC2)
- ❌ Juristische Auslegung Art. 72/73 (PK-SC5)
- ❌ Azure-Code (→ 5.6)
- ❌ Evidence Store Schema wiederholen (→ 5.4)
- ❌ Requirements wiederholen (→ 4.6)
- ❌ Drift-Detection-Konzept aus 4.4 wiederholen
- ❌ Romeo ARPaCCino (→ 5.3)
- ❌ Formale Überleitungen (PK-V1)

---

## Venue-Caveats
- Khademi et al. (2023): arXiv → "methodisch detailliert, wenngleich als Preprint publiziert"
- Eck et al. (2022): IEEE Big Data → kein Caveat nötig

## Zotero-Keys Komplett-Referenz
| Quelle | Key | Tier |
|--------|-----|------|
| Ray (2026) | AW3BMEEI | CORE |
| Cuocolo et al. (2025) | NWJ7SY5I | CORE |
| Khademi et al. (2023) | ILFAR2R2 | CORE |
| Agarwal & Nene (2026) | GY5P52BE | CORE |
| Eck et al. (2022) | 7HUZPNSK | EMPF |
| Nweke & Yeng (2026) | XCM4Q2WP | REUSE |
| Muhammad et al. (2026) | IZVYTSTV | REUSE |
