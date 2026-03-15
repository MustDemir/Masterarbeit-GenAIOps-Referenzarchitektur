# Schreibstrategie Kap. 5.5 — Monitoring und Post-Market Surveillance
**Stand:** 2026-03-14 | **Budget:** ~2 Seiten / ~600–700W
**Preflight:** PREFLIGHT_KAP5_5_MONITORING_PMS_V1.md (BLOCKIERT → RESOLVED nach D_5.5_CONTENT)

---

## Argumentationsstruktur (4 Absätze)

| Abs. | Move | Primärquelle | Wörter (~) |
|------|------|-------------|------------|
| 1 | Art. 72 PMS Deployer-Pflicht + TRiSM-Einordnung | Cuocolo et al. (2025) + Ray (2026) | ~150W |
| 2 | Drift-Detection: PSI/Jensen-Shannon + Monitoring-Sidecar-Pattern | Ray (2026, S. 14) + Khademi (2023) | ~200W |
| 3 | Incident Reporting Art. 26.5 + Art. 73 + Eskalationslogik | EU AI Act Art. 73 + Cuocolo (2025) | ~150W |
| 4 | Bridge: PMS → Evidence Store (Monitoring-Window-Semantik → 5.6) | Nweke & Yeng (2026, S. 28258) | ~100W |

**Bridge von 5.4 (M9):** "Das konzeptuelle Schema bildet die Grundlage für die in Abschnitt 5.5 spezifizierte Monitoring-Architektur, die eine laufzeitnahe Auswertung der persistierten Evidence Records im Sinne von Art. 72 EU AI Act (Post-Market Surveillance) ermöglicht. Die prototypische Instanziierung der fünf Komponenten auf dem Azure-Stack erfolgt in Abschnitt 5.6."

**Bridge zu 5.6:** "Die spezifizierte Monitoring-Architektur — bestehend aus Drift-Detection (PSI/Jensen-Shannon), Incident Reporting (Art. 73) und Evidence-Store-Anbindung (Monitoring-Window) — wird in Abschnitt 5.6 am Azure-Stack (AKS, Prometheus, PostgreSQL) prototypisch instanziiert."

---

## Negativ-Checklist (Was NICHT hinein darf)

- ❌ Provider-Perspektive (Art. 16 — kein Scope)
- ❌ Retirement-Phase (PK-SC2)
- ❌ Juristische Auslegung Art. 72 (PK-SC5 — nur technisch-organisatorisch)
- ❌ Azure-Stack Code/Implementierung (→ 5.6 + Kap. 6.3)
- ❌ Evidence Store Schema Wiederholung (→ bereits 5.4)
- ❌ Romeo et al. (2025) ARPaCCino (→ gehört zu 5.3, nicht 5.5)
- ❌ Formale Überleitungen "Im Folgenden wird..." (PK-V1)

---

## DSR-Verankerung

- Peffers Step 3 (Design & Development): Monitoring-Architektur als Teil des Gesamtsystems
- 5 Säulen komplett nach 5.5: S1 (DP1-DP5) + S2 (Gates) + S3 (Pipeline) + S4 (Evidence) + S5 (Monitoring)
- Monitoring-Sidecar als DSR-Eigenleistung E5 (Synthese aus Ray-Architektur + Gatekeeper aus 5.3)

---

## Offene Punkte (vor GO)

- [ ] Cuocolo et al. (2025) in Zotero importieren: DOI 10.1186/s13244-025-02146-8
- [ ] Khademi et al. (2023) in Zotero importieren: DOI 10.48550/arXiv.2302.00775
- [ ] Romeo (2025) aus chapter_state 5.5 kern_papers entfernen
- [ ] Q3 Incident Reporting: Art. 73 normativ ausreichend (JA → GO möglich)
