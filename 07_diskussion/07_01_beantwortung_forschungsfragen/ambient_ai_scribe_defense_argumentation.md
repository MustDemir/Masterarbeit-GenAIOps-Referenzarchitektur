# Defense Argumentation - Ambient AI Scribe (Chapter 7.1)

## Core Position
A hybrid evidence architecture (Blob + SQL) is required for high-risk medical GenAI operations.

## Why not only Blob or default logs?
- Blob stores unstructured payload well but does not provide relational compliance telemetry for efficient audit reporting.
- Audit use cases require indexed, queryable, and policy-controlled metadata.

## Why SQL evidence telemetry?
- Composite indexes support scalable compliance reporting.
- Trigger-based immutability protects evidence against tampering.
- Views and least-privilege rights reduce exposure and misuse.
- RLS and schema separation enforce privacy boundaries at database level.
- Hash-chain fields provide tamper-evident integrity for audit defense.

## Regulatory fit
- EU AI Act: supports logging and accountability obligations for high-risk systems.
- GDPR context: supports strict separation between sensitive payload and compliance metadata.

## Reproducibility fit
- model_version, run_id, pipeline_id provide execution-level traceability.
- Decisions can be reproduced and defended in expert review and audit scenarios.

## Examiner challenge: \"Why not only Azure Monitor?\"
- Azure Monitor is strong for technical observability, but not sufficient as relational compliance evidence layer.
- High-risk audit needs structured, indexed, role-controlled, and tamper-evident metadata.
- Hybrid design (Blob payload + SQL telemetry) meets privacy, performance, and forensic requirements together.
