# 5.5 Monitoring und Post-Market Surveillance

**Kapitel:** 5.5 | **Status:** in_progress (Preflight abgeschlossen)
**Decision:** D_5.5_CONTENT (2026-03-14)

---

## Inhalt dieses Abschnitts

Art. 72 EU AI Act verpflichtet Deployer zur Post-Market Surveillance (PMS).
Abschnitt 5.5 spezifiziert die Monitoring-Architektur, die den Evidence Store (5.4)
operational macht: Drift-Detection (PSI/Jensen-Shannon), Incident Reporting (Art. 26.5+73)
und die Monitoring-Window-Semantik als Brücke zur prototypischen Instanziierung (5.6).

## Ordnerstruktur

- `arbeitsmaterial/drafts/` — DRAFT-Datei (Kap5_5_Monitoring_PMS_DRAFT.md)
- `artefakte/` — abschnittsbezogene Nachweis- und Kontrollartefakte
- `00_workspace/` — Arbeitsdokumente: Quellen-Analyse, Schreibstrategie, Preflight
- `images/final/` — finale Diagramme (Monitoring-Sidecar-Architektur)
- `images/work/` — Entwurfsdiagramme
- `quellen_kap5_5/` — kuratierte Quellen-PDFs für 5.5

## Kern-Quellen

| Quelle | Zotero-Key | Tier | Rolle |
|--------|-----------|------|-------|
| Ray (2026) — TRiSM Review | `AW3BMEEI` | CORE | Drift-Detection S.14, TRiSM-Framework |
| Cuocolo et al. (2025) — ESR AI PMS | ❌ Import nötig | CORE | Art. 72 PMS Healthcare-Deployer |
| Khademi et al. (2023) — PSI Drift | ❌ Import nötig | Empfohlen | PSI-Methodik |
| Nweke & Yeng (2026) | `XCM4Q2WP` | Empfohlen | Monitoring-Window-Semantik (Reuse) |
| Muhammad et al. (2026) | `IZVYTSTV` | Empfohlen | Assured Readiness Score (Reuse) |

## Preflight + Evidenz-Matrix

- `docs/preflight/PREFLIGHT_KAP5_5_MONITORING_PMS_V1.md`
- `docs/preflight/EVIDENZ_MATRIX_KAP5_5.md`
- `docs/preflight/EVIDENZ_MATRIX_KAP5_5.html`

## Bridge-Sätze

**Von 5.4:** "Das konzeptuelle Schema bildet die Grundlage für die in Abschnitt 5.5
spezifizierte Monitoring-Architektur..."

**Nach 5.6:** "Die spezifizierte Monitoring-Architektur wird in Abschnitt 5.6
am Azure-Stack prototypisch instanziiert."

## Gliederung-Mapping

| Sektion | Entscheidung | SSOT |
|---------|-------------|------|
| D_5.5_CONTENT | 5.5 = Monitoring/PMS, 5.6 = PoC | chapter_state.yaml + gliederung_v3.md |
