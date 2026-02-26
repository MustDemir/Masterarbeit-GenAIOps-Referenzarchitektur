# Ambient AI Scribe - SQL Design Principles (Chapter 5.1)

## Context
Medical AI documentation is high-risk and requires strict separation between sensitive payload and compliance telemetry.

## DP-1 Privacy by Design
- No direct access to sensitive payload from compliance consumers.
- SQL views expose only required and masked fields.
- Goal: Minimize PII exposure in operational and audit contexts.

## DP-2 Immutable Compliance Evidence
- Audit-relevant gate results are append-only.
- BEFORE UPDATE/DELETE trigger blocks post-hoc tampering.
- Goal: Forensic-grade evidence chain.

## DP-3 Least Privilege for Automation
- CI/CD runners receive only INSERT rights on evidence tables.
- No UPDATE/DELETE rights for pipeline identities.
- Goal: Reduce blast radius and enforce policy by design.

## DP-4 Performance and Observability
- Composite indexes for auditor and dashboard queries.
- Query paths optimized for model and gate dimensions.
- Goal: Predictable reporting latency at scale.

## DP-5 Reproducibility and Traceability
- Mandatory metadata: model_version, run_id, pipeline_id.
- All gate decisions tied to execution context and timestamp.
- Goal: Defensible reproducibility under audit.

## DP-6 Schema Separation and RLS
- Separate schemas for payload (`medical`) and telemetry (`compliance`).
- Row-Level Security controls read/write behavior by role.
- Goal: Technical enforcement of privacy and access boundaries.

## DP-7 Tamper-Evident Hash Chain
- Each inserted evidence row stores `hash_value` and `previous_hash`.
- Hash is generated from execution metadata and previous chain state.
- Goal: Forensic integrity proof beyond simple trigger immutability.

## Mapping to Expose
- Chapter 5.1: principles and rationale
- Chapter 5.5: evidence-store integration
- Chapter 6.4: PoC implementation and proof
