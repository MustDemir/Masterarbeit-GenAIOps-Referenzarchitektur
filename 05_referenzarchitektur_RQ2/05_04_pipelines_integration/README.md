# 5.3 Pipeline-Integration und Policy Engine [S3]

Dieser Ordner bildet Kap. 5.3 der Gliederung ab (Gliederungs-Nr. ≠ Verzeichnis-Nr.).

## Mapping
- **Gliederung 5.3.1** = CI/CD-Pipeline-Architektur (GitHub Actions, Stage-Gates)
- **Gliederung 5.3.2** = Policy-as-Code Integration (OPA/Rego, Conftest/Gatekeeper/Decision Logs)

## Artefakte
- `pipeline_blueprints/`: Konzeptionelle Pipeline-Diagramme, Stage-Gate-Mapping
- `workflow_specs/`: GitHub Actions Workflow-Spezifikationen, CDV-Flow
- `images/`: Section-spezifische Visuals (Abb. 5.x Pipeline-Architektur)

## Preflight + Evidenz
- Preflight: `docs/preflight/PREFLIGHT_KAP5_3_PIPELINE_POLICY_ENGINE.md` (v2.0)
- Evidenz-Matrix: `docs/preflight/EVIDENZ_MATRIX_KAP5_3.md` + `.html`
- Zotero-Import-Liste: `docs/preflight/ZOTERO_IMPORT_LISTE_KAP5_3.md`

## Bindende Decisions (12)
D_OPA_THREE_PILLAR, D_GATEKEEPER_STANDALONE, D_GATEKEEPER_SCOPE, D_LOG_BACKEND,
D_LUCAJ_STARTING_BASIS, D_POC_REGO_K8S, D_R002_SINGLE_GATE, R8/CDV-Framework,
D_CAC_AAC_DIFF, D_4.6_VS_5.3_SEPARATION, D_GATE_RULE_V3, D_KONSOLIDIERUNG_AUFGELOEST

## Budget: ~3 Seiten (~900W)
