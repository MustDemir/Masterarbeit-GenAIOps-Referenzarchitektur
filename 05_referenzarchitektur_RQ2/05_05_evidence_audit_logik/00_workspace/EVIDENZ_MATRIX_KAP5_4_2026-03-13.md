# Evidenz-Matrix Kap. 5.4: Evidence- und Audit-Logik [S4 USP]

**Datum:** 2026-03-13
**Methode:** Zotero-Fulltext-Extraktion + Elicit Landscape-Check
**Extraktionsfragen:** Q1–Q7 (vom User approved)
**Quellen:** 9 von 10 (Sovrano deferred); Lucaj Fulltext nachträglich aus PDF extrahiert (Zotero-API 404, lokales PDF verfügbar)

---

## Extraktionsfragen (Q1–Q7)

| ID | Frage | Kürzel |
|---|---|---|
| Q1 | Immutable Evidence Storage (Append-Only, Write-Once) | IMMUT |
| Q2 | Hash-Chain / Tamper-Detection (kryptographische Integrität) | HASH |
| Q3 | Privacy / PII-Separation (Payload vs. Telemetry, DSGVO) | PRIV |
| Q4 | RBAC / Least-Privilege (Rollen-basierter Evidence Access) | RBAC |
| Q5 | Audit-Trail Traceability (R → DP → Gate → Evidence) | TRACE |
| Q6 | CAC/AAC-Differenzierung (Compliance-as-Code vs. Audit-as-Code) | CAC |
| Q7 | Schema / Data-Model (Evidence Record Struktur) | SCHEMA |

---

## Bewertungslegende

| Symbol | Bedeutung |
|---|---|
| ✅ | Explizit adressiert (mit konkretem Mechanismus/Konzept) |
| ⚠️ | Implizit/indirekt adressiert (konzeptionell, aber kein dedizierter Mechanismus) |
| ❌ | Nicht adressiert |
| 🔍 | Fulltext nicht verfügbar; Bewertung basiert auf Abstract/Metadaten |

---

## Hauptmatrix

| # | Quelle | Key | Q1 IMMUT | Q2 HASH | Q3 PRIV | Q4 RBAC | Q5 TRACE | Q6 CAC | Q7 SCHEMA | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Kholkar & Ahuja (2025)** | VLMNBUST | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 6/7 |
| 2 | **Muhammad et al. (2026)** | IZVYTSTV | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | 4+3⚠️/7 |
| 3 | **Burns et al. (2025)** | 2GGF93BE | ⚠️ | ❌ | ❌ | ✅ | ✅ | ⚠️ | ❌ | 2+2⚠️/7 |
| 4 | **Eisenberg et al. (2025)** | JUK36XAW | ⚠️ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | 5+1⚠️/7 |
| 5 | **Butt (2026)** | V6HKHA5B | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | 5+2⚠️/7 |
| 6 | **Pistilli et al. (2023)** | 3774R8Y6 | ❌ | ❌ | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | 1+2⚠️/7 |
| 7 | **Nweke & Yeng (2026)** | XCM4Q2WP | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 5+2⚠️/7 |
| 8 | **Lucaj et al. (2025)** | 5Y79UTJ9 | ⚠️ | ❌ | ⚠️ | ⚠️ | ✅ | ❌ | ✅ | 2+3⚠️/7 |
| 9 | **Golpayegani et al. (2024)** | 7BF458GD | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | 4/7 |

---

## Detailextraktion pro Quelle

### 1. Kholkar & Ahuja (2025) — Policy-as-Prompt [VLMNBUST]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ✅ | "complete provenance, traceability, and audit logging" — Audit Logging als explizites Framework-Feature |
| Q2 | ❌ | Keine Erwähnung von Hash-Chains, Merkle Trees oder kryptographischer Integritätssicherung |
| Q3 | ✅ | "enforce least privilege and data minimization" — Datenminimierung als Designprinzip |
| Q4 | ✅ | "Principle of Least Privilege" explizit; Agent kann nur innerhalb Policy-Grenzen agieren |
| Q5 | ✅ | "source-linked policy tree" mit vollständiger Provenance-Kette: Dokument → Policy → Regel → Klassifikation |
| Q6 | ✅ | "Policy-as-Code for agents" — Kernkonzept; Policies werden als executable Prompts kompiliert |
| Q7 | ✅ | Strukturierte Outputs: JSON-Klassifikation (ID/OOD) + Reasoning; 4-Kategorie-Taxonomie (ID-I, OOD-I, ID-O, OOD-O) |

**Kernbeitrag für 5.4:** CAC-Operationalisierung (Policy → Executable Guardrail), Audit-Logging-Konzept, Least-Privilege-Enforcement

---

### 2. Muhammad et al. (2026) — Audit-as-Code [IZVYTSTV]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ✅ | "structured evidence regarding data, models, provenance, performance, decisions, and explanations" — Evidenz-Artefakte als First-Class-Objekte |
| Q2 | ⚠️ | "versioned policy specification" impliziert Versionierung, aber keine explizite kryptographische Integritätssicherung |
| Q3 | ⚠️ | Governance-Mapping berücksichtigt Responsible AI Prinzipien, aber keine explizite PII-Trennung |
| Q4 | ⚠️ | "predefined risk tiers" → Zugangssteuerung via Risiko-Schwellen, aber kein RBAC im engeren Sinne |
| Q5 | ✅ | Governance-Requirements → auditable Rules → Evidence Artifacts → Gate Decisions; "assured readiness score" als aggregierter Traceability-Indikator |
| Q6 | ✅ | **"Audit-as-Code"** als namensgebender Kernbeitrag; explizite Differenzierung: deterministic checks + gate decisions in CI/CD |
| Q7 | ✅ | Evidence-Artefakte-Struktur: Data, Models, Provenance, Performance, Decisions, Explanations; Readiness Score als Composite-Metrik |

**Kernbeitrag für 5.4:** AAC-Konzept (Audit-as-Code), Assured Readiness Score, Evidence-Artefakte-Taxonomie, CI/CD-Gate-Integration

---

### 3. Burns et al. (2025) — Dynamo/AIGA [2GGF93BE]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ⚠️ | AIGA Governance Tasks beinhalten "tracking, documenting, validating, and monitoring" — konzeptionell, aber kein technisches Evidence Store |
| Q2 | ❌ | Keine Erwähnung kryptographischer Mechanismen |
| Q3 | ❌ | Keine explizite PII-Trennung; Fokus auf High-Risk-Klassifikation |
| Q4 | ✅ | AIGA Kategorie F: "Accountability and ownership" → Rollen (Head of AI, AI System Owner) definiert |
| Q5 | ✅ | AIGA 8-Kategorie-Framework (A–H) mit Compliance-Checkpoints über AI-Lifecycle |
| Q6 | ⚠️ | Governance-Checklist als manuelles Compliance-Instrument, nicht code-basiert |
| Q7 | ❌ | Keine Schema-Definition; high-level Governance Tasks ohne Datenmodell |

**Kernbeitrag für 5.4:** AIGA-Governance-Lifecycle als Kontextrahmen; Rollen-Definition (DP4-relevant)

---

### 4. Eisenberg et al. (2025) — UCF [JUK36XAW]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ⚠️ | 42 Controls als Governance-Struktur; keine explizite Evidence-Store-Architektur |
| Q2 | ❌ | Keine kryptographischen Mechanismen |
| Q3 | ✅ | Comprehensive Risk Taxonomy inkludiert Privacy-/Data-Risiken |
| Q4 | ✅ | Controls umfassen Access-Management; "concrete implementation guidance" |
| Q5 | ✅ | Risk → Policy Requirements → 42 Controls; Multi-Regulation-Mapping (EU AI Act, Colorado AI Act) |
| Q6 | ✅ | "foundation for automation" — Controls als Basis für Policy-as-Code-Automatisierung |
| Q7 | ✅ | 42 Controls als strukturiertes Schema; Risk Taxonomy + Policy Requirements als Dreischichtmodell |

**Kernbeitrag für 5.4:** UCF als Multi-Regulation-Compliance-Framework; Risk → Control → Regulation-Traceability

---

### 5. Butt (2026) — GEAP/C2AT [V6HKHA5B]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ✅ | "signed, content-addressed artifacts" — Jedes Gate emittiert signierte, inhaltsadressierte Artefakte |
| Q2 | ✅ | **"content-addressed"** = Hash-basierte Adressierung (CAS-Prinzip); stärkster Beleg für Q2 im gesamten Quellenkorpus |
| Q3 | ⚠️ | GEAP adressiert Regulatory Compliance allgemein; keine explizite Payload/Telemetrie-Trennung |
| Q4 | ⚠️ | 5-Gate-Promotion als implizite Zugangssteuerung; kein explizites RBAC-Modell |
| Q5 | ✅ | "clause-level traceability" über 5 Gates: Data → Training → Validation → Release → Operations |
| Q6 | ✅ | **"Governance as Code"** (GaC) — explizite Code-basierte Policy-Enforcement in Pipeline |
| Q7 | ✅ | GEAP-Architektur: 5 Gates, Conformity Assessment Toolkit (C2AT), Evidence Pipeline |

**Kernbeitrag für 5.4:** Content-Addressed Artifacts (Hash-Integrität), 5-Gate-Architektur, Governance-as-Code, C2AT

---

### 6. Pistilli et al. (2023) — Governance Synergies [3774R8Y6]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ❌ | Fokus auf konzeptionelle Governance, nicht auf technische Speicherung |
| Q2 | ❌ | Keine technischen Mechanismen |
| Q3 | ⚠️ | Ethical Charters berücksichtigen Privacy implizit |
| Q4 | ⚠️ | Stakeholder-Rollen (AI developers, designers) als Accountability-Mechanismus |
| Q5 | ✅ | "complementary notions of compliance" über Ethics × Law × Computer Science als Governance-Triade |
| Q6 | ❌ | Konzeptionelle Compliance-Synergien, nicht code-basiert |
| Q7 | ❌ | Keine Schema-Definition |

**Kernbeitrag für 5.4:** Governance-Triade (Ethics/Law/Tech) als Kontextrahmen für DP1 (Compliance-Lifecycle)

---

### 7. Nweke & Yeng (2026) — Compliance-as-Code [XCM4Q2WP]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ✅ | "machine-readable evidence"; "evidence completeness as an enforceable property via fixed monitoring" |
| Q2 | ⚠️ | Monitoring-enforced evidence integrity; keine explizite Hash-Chain, aber Integritäts-Enforcement |
| Q3 | ✅ | AI-driven Identity Systems → PII/Biometrie ist Kernanwendungsdomäne; Privacy-by-Design zentral |
| Q4 | ⚠️ | Regulatory Access-Control impliziert; kein explizites RBAC-Modell |
| Q5 | ✅ | **"clause-to-control traceability under policy/configuration evolution"** — Kernkonzept |
| Q6 | ✅ | **"Compliance-as-Code"** als Titel und Kernkonzept; operationalisiert CAC für ID-Systeme |
| Q7 | ✅ | Evidence-Record-Struktur; Monitoring-Punkte als Schema; Clause-to-Control-Mapping als Datenmodell |

**Kernbeitrag für 5.4:** CAC-Operationalisierung für AI-ID-Systeme, Clause-to-Control-Traceability, Evidence-Completeness-Enforcement

---

### 8. Lucaj et al. (2025) — TechOps Documentation [5Y79UTJ9] ✅ Fulltext verfügbar

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ⚠️ | "should be treated as an immutable artifact at a certain point" — Immutability erwähnt, aber kein dedizierter Mechanismus |
| Q2 | ❌ | Keine Erwähnung von Hash, Merkle, kryptographischer Integrität |
| Q3 | ⚠️ | Privacy (5×), GDPR (2×) erwähnt; "aligning documentation practices with core GDPR obligations" — aber keine PII-Trennung |
| Q4 | ⚠️ | "secure storage through encryption, role-based access" — RBAC einmal erwähnt, nicht ausgearbeitet |
| Q5 | ✅ | Traceability (6×), Provenance (4×), Audit Trail (1×): "ensuring traceability, reproducibility, and compliance" — Kernkonzept |
| Q6 | ❌ | Kein as-Code, CI/CD, Pipeline-Konzept; rein dokumentenbasiert |
| Q7 | ✅ | Templates (76×) als strukturierte Documentation Artifacts; Provenance-Felder, Lifecycle-Status, AI Act Annex IV Mapping |

**Kernbeitrag für 5.4:** Template-basierte Lifecycle-Dokumentation; "immutable artifact" Konzept; Provenance-Felder als Schema-Referenz für Evidence Records

---

### 9. Golpayegani et al. (2024) — AICat [7BF458GD]

| Q | Bewertung | Evidenz aus Fulltext |
|---|---|---|
| Q1 | ❌ | Cataloguing-Ansatz; kein Evidence Storage |
| Q2 | ❌ | Keine kryptographischen Mechanismen |
| Q3 | ✅ | Non-public vs. public EU Database Sections; DCAT unterstützt Zugangsstufen |
| Q4 | ✅ | Art. 71: "different levels of accessibility" → Zugangssteuerung nach Rolle (Provider, Deployer, Public) |
| Q5 | ✅ | Metadata cross-referencing; DCAT-basierte Traceability über AI Value Chain |
| Q6 | ❌ | Semantic-Web-Cataloguing, nicht Code-basierte Compliance-Checks |
| Q7 | ✅ | **AICat RDF/OWL Schema**: aicat:Catalog, airo:AISystem, airo:AIModel als formale Ontologie |

**Kernbeitrag für 5.4:** DCAT/AICat als Referenz für Evidence-Metadaten-Schema; EU-Database-Zugangsstufen

---

## Aggregierte Abdeckungsmatrix

| Frage | ✅ Explizit | ⚠️ Implizit | ❌ Nicht | Abdeckung |
|---|---|---|---|---|
| **Q1 IMMUT** | 4 (Kholkar, Muhammad, Butt, Nweke) | 3 (Burns, Eisenberg, Lucaj) | 2 (Pistilli, Golpayegani) | 🟢 GUT |
| **Q2 HASH** | 1 (Butt) | 2 (Muhammad, Nweke) | 6 | 🔴 **LÜCKE** |
| **Q3 PRIV** | 3 (Kholkar, Nweke, Golpayegani) | 4 (Muhammad, Butt, Pistilli, Lucaj) | 2 (Burns, Eisenberg*) | 🟡 MODERAT |
| **Q4 RBAC** | 3 (Kholkar, Burns, Eisenberg) | 5 (Muhammad, Butt, Pistilli, Nweke, Lucaj) | 1 (Golpayegani*) | 🟡 MODERAT |
| **Q5 TRACE** | **9/9** | 0 | 0 | 🟢 **VOLLSTÄNDIG** |
| **Q6 CAC** | 5 (Kholkar, Muhammad, Butt, Eisenberg, Nweke) | 1 (Burns) | 3 (Pistilli, Lucaj, Golpayegani) | 🟢 GUT |
| **Q7 SCHEMA** | 7 (Kholkar, Muhammad, Eisenberg, Butt, Nweke, Lucaj, Golpayegani) | 0 | 2 (Burns, Pistilli) | 🟢 GUT |

*Eisenberg hat Privacy im Risk Taxonomy; Golpayegani hat Zugangsstufen → korrigiert in Detailextraktion

---

## Identifizierte Lücken

### 🔴 Kritische Lücke: Q2 — Hash-Chain / Tamper-Detection

**Befund:** Nur **Butt (2026)** adressiert kryptographische Integritätssicherung explizit ("content-addressed artifacts"). Muhammad und Nweke bieten schwache implizite Belege (Versionierung, Monitoring-Enforcement). Keine Quelle beschreibt dedizierte Hash-Chain- oder Merkle-Tree-Mechanismen für AI-Audit-Trails.

**Implikation für Kap. 5.4:**
- Hash-Chain-Immutability (DP5.3) ist **DSR-Eigenleistung** → muss als eigener Design-Beitrag argumentiert werden
- Butt's "content-addressed artifacts" als nächste Referenz nutzbar
- Elicit-Landscape-Check bestätigt Lücke (nur 2–3 Supplementary Papers: Joseph 2023, Kamimura 2026)

### 🟡 Moderate Lücke: Q3 — PII-Separation

**Befund:** Payload/Telemetrie-Trennung als explizites Architekturprinzip wird von keiner Quelle direkt beschrieben. PII wird konzeptionell (Kholkar: data minimization, Nweke: ID-Systeme) adressiert, aber die R3-spezifische Anforderung (encrypted Blob vs. SQL-Telemetry) ist DSR-Eigenleistung.

### 🟢 Stärken

- **Q5 (Traceability):** 9/9 Quellen → starke Evidenz-Basis
- **Q6 (CAC/AAC):** 5 explizite Quellen mit 3 verschiedenen Begriffen (Policy-as-Code, Audit-as-Code, Compliance-as-Code, Governance-as-Code) → ermöglicht differenzierte Begriffsklärung
- **Q7 (Schema):** 7/9 Quellen → Schema-Design hat breite Evidenz-Basis

---

## Top-3 Quellen pro Absatz (Schreib-Priorisierung)

| Absatz in 5.4 | Thema | Primärquelle | Sekundär | Tertiär |
|---|---|---|---|---|
| Abs. 1 (Intro) | Evidence Store als Backbone | Butt 2026 | Muhammad 2026 | Nweke 2026 |
| Abs. 2 (DP1 Compliance-Lifecycle) | Governance-Triade | Pistilli 2023 | Burns 2025 | Eisenberg 2025 |
| Abs. 3 (CAC-Execution) | Policy-as-Code → CAC | Kholkar 2025 | Muhammad 2026 | Nweke 2026 |
| Abs. 4 (Decision Logs) | Conformity Bundle + Schema | Butt 2026 | Muhammad 2026 | Eisenberg 2025 |
| Abs. 5 (Hash-Chain) | Immutability DP5.3 | Butt 2026 (content-addr.) | **DSR-Eigenleistung** | — |
| Abs. 6 (Payload-Trennung) | R3 PII/Telemetry | Nweke 2026 | Kholkar 2025 | **DSR-Eigenleistung** |

---

## Elicit-Supplementary-Kandidaten (aus Landscape-Check + Verifikation)

| Quelle | Jahr | Venue | Relevanz für Q2-Lücke | Venue-Qualität | Empfehlung |
|---|---|---|---|---|---|
| Joseph (2023): "Trust, but Verify" | 2023 | World J. Adv. Eng. Tech. Sci. | Hash-Chains + Merkle Trees für Clinical AI Audit; <5ms Latenz, 100% Tamper-Detection, Art. 12 EU AI Act | ⚠️ Niedrig (0 Zitationen, kein Top-Venue) | ✅ **AUFGENOMMEN** — Stütz-Evidenz für Abs. 5 (DP5.3), Venue-Caveat im Text |
| Kamimura (2026): CAP Framework | 2026 | SSRN Preprint | Hash-Chains + Merkle Proofs + Digital Signatures für Creative AI; EU AI Act aligned | ⚠️ Niedrig (Preprint, 0 Zitationen) | 🟡 **OPTIONAL** — Framework-Level relevant, aber Preprint-Status limitiert Zitierbarkeit |
| Kadambala (2025): Auditable AI Pipelines | 2025 | Innovative J. Applied Sci. | Cryptographic Hashes + optional Blockchain in MLOps; regulatory compliance focus | ⚠️ Niedrig (1 Zitation) | 🟢 **VERWENDEN** — MLOps-Fokus passt besser als Blockchain-Paper |
| Kulothungan (2025): Blockchain AI Audit | 2025 | IoT Journal (MDPI) | Blockchain-Audit für IoT-AI; 13 Zitationen | 🟡 Moderat (MDPI, 13 Zit.) | ❌ **NICHT VERWENDEN** — Blockchain ≠ Hash-Chain, IoT-Scope zu weit |

### Venue-Qualitäts-Caveat
⚠️ **Alle Q2-Supplementary-Kandidaten haben schwache Venue-Qualität.** Dies bestätigt die Literaturlücke und stärkt das DSR-Eigenleistung-Argument: Kryptographische Evidence-Integrität in AI-Governance ist ein unterforschtes Feld. Joseph (2023) liefert dennoch den besten technischen Beleg (Merkle Trees + Performance-Daten) und kann als „nächste Referenz" für DP5.3 dienen.

---

## Fazit

Die Matrix zeigt eine **solide Quellenbasis** für Kap. 5.4 mit folgender Verteilung:
- **6 Fragen (Q1, Q3–Q7):** Ausreichend bis gut abgedeckt durch 3–9 Quellen
- **1 Frage (Q2):** Kritische Lücke → DSR-Eigenleistung (Hash-Chain-Immutability)

Die **DSR-Argumentationsstrategie** muss die Hash-Chain-Lücke als bewussten Design-Beitrag framen:
> "Existing literature addresses traceability (Q5) and code-based compliance enforcement (Q6) comprehensively, but lacks dedicated mechanisms for cryptographic evidence integrity. Our Evidence Store Schema closes this gap through SQL-level immutability triggers and optional hash-chain extensions (DP5.3)."
