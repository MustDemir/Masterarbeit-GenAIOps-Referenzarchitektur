# Schreibstrategie Kap. 5.4: Evidence- und Audit-Logik [S4 USP]

**Datum:** 2026-03-13
**Basis:** Evidenz-Matrix (9+1 Quellen × Q1-Q7) + Preflight-Protokoll (P1-P6)
**Scope:** Qualität > Seitenzahl (D_QUALITY_OVER_PAGES). Keine Seitenlimit-Restriktion.
**DSR-Phase:** Design Cycle Phase 2, RQ2, Peffers Step 3
**Quellen:** 10 Kern/Stütz + 1 Supplementary (Joseph 2023)

---

## Gliederung (aus Exposé v3)

- **5.4 Evidence- und Audit-Logik [S4 USP]**
  - 5.4.1 Evidence-Persistierung (Immutable Storage, Schema, RBAC)
  - 5.4.2 Audit-Trail und Nachweiskette (Hash-Chain, Traceability, CAC/AAC)

---

## Brücke VON Kap. 5.3

Kap. 5.3 endet mit:
- Drei-Säulen-Enforcement: Conftest (Pre-Dep) + Gatekeeper (Admission) + **Decision Logs (Operations)**
- 3 Decision-Log-Policies: Evidence-Completeness, Hash-Chain-Integrity, Audit-Trail-Immutability
- CAC/AAC-Differenzierung eingeführt
- **Expliziter Brückensatz:** "Section 5.4 will detail the Evidence Store technical realization and hash-chain logic"

→ **Kap. 5.4 muss:** Decision Logs technisch realisieren als Evidence Store Schema (DSR-Artefakt)

---

## Argumentationsstruktur: 9 Moves in 2 Unterabschnitten

### 5.4.1 Evidence-Persistierung (Move 1–5)

| Move | Absatz | Argumentativer Move | Kern-Claim | DSR-Anker | Top-Quellen (aus Matrix) | Evidenzstärke |
|------|--------|---------------------|------------|-----------|--------------------------|---------------|
| **M1** | Abs. 1 | **Motivation: Payload/Telemetrie-Trennung** | R3 fordert Trennung: medical Payload (DSGVO Art. 9, encrypted Blob) vs. regulatory Telemetry (SQL-indexiert). Evidence Store = S4-Backbone. | R3, DP1, Art. 9 DSGVO | Nweke 2026 (Q3✅), Kholkar 2025 (Q3✅), Golpayegani 2024 (Q3✅) | 🟡 Q3 MODERAT — PII-Trennung als Architekturmuster ist DSR-Eigenleistung, Privacy-Konzepte als Stütze |
| **M2** | Abs. 2 | **Evidence Store Schema als DSR-Artefakt** | 5 Komponenten einführen: Immutability-Trigger (DP2+DP5.3), Privacy Views (DP1+DP4), RBAC (DP5), Composite Indexes (DP5.2), quality_gate_results Table (DP1+DP2). | D_DSR_EVIDENCE_STORE, alle DP | Butt 2026 (6/7), Muhammad 2026 (4+3⚠️/7), Eisenberg 2025 (5+1⚠️/7) | 🟢 Synthesis aus Q1+Q5+Q7 — breite Basis für Schema-Konzept |
| **M3** | Abs. 3 | **Immutability-Trigger (SQL-Level)** | SQL-Trigger verhindert UPDATE/DELETE auf evidence_records. Operationalisiert Fälschungssicherheit. Append-Only als Enforcement (nicht nur Konvention). | DP2, DP5.3 | Kholkar 2025 (Q1✅ Audit Logging), Butt 2026 (Q1✅ structured evidence), Muhammad 2026 (Q1✅ evidence artifacts) | 🟢 Q1 GUT — 4 explizite Quellen |
| **M4** | Abs. 4 | **Least-Privilege RBAC** | CI/CD-Pipeline = INSERT-only Rolle. Auditoren = SELECT via Privacy Views. DB-native Rollen-Enforcement statt Application-Layer. | DP5 | Kholkar 2025 (Q4✅ Least Privilege), Burns 2025 (Q4✅), Eisenberg 2025 (Q4✅ UCF Access Controls) | 🟢 Q4 MODERAT→GUT — 3 explizit + 5 implizit |
| **M5** | Abs. 5 | **Composite Indexes + Performance SLO** | Query < 100ms SLO für Audit-Reporting. Index auf (gate_id, timestamp, verdict). DP5.2 Sub-Extension. | DP5.2 | Eisenberg 2025 (Q7✅ unified schema), Muhammad 2026 (Q7✅ readiness score), Butt 2026 (Q7✅ conformity bundle) | 🟢 Q7 GUT — 7/9 explizit. Performance-SLO = DSR-Eigenleistung |

**Transition M5→M6:** "Von der Persistierungsschicht zur Nachweiskette — wie werden gespeicherte Evidence Records zu einer auditierbaren Beweiskette verknüpft?"

---

### 5.4.2 Audit-Trail und Nachweiskette (Move 6–9)

| Move | Absatz | Argumentativer Move | Kern-Claim | DSR-Anker | Top-Quellen (aus Matrix) | Evidenzstärke |
|------|--------|---------------------|------------|-----------|--------------------------|---------------|
| **M6** | Abs. 6 | **quality_gate_results Table** | Zentrales Audit-Log: jede Gate-Evaluation = 1 Record. CDV-Framework-Output als strukturierter Evidence Record. Conformity Bundle nach Butt. | DP1, DP2 | Muhammad 2026 (Q6✅ Audit-as-Code), Butt 2026 (Q6✅ Conformity Bundle), Eisenberg 2025 (Q6✅ UCF) | 🟢 Q6 GUT — 5 explizite Quellen für CAC/AAC |
| **M7** | Abs. 7 | **Hash-Chain-Integrität (DP5.3)** ⚡ DSR-Eigenleistung | Verkettete SHA-256-Hashes über Evidence Records. prev_hash = SHA-256(vorheriger Record). Nachträgliche Manipulation bricht Kette. Art. 12 EU AI Act Logging. | DP5.3, Art. 12 | Butt 2026 (Q2✅ "content-addressed artifacts"), Joseph 2023 (Q2 Merkle Trees, <5ms, Art. 12) | 🔴 Q2 LÜCKE — **DSR-Eigenleistung**, gestützt durch Butt + Joseph |
| **M8** | Abs. 8 | **Traceability-Kette (R → DP → Gate → Evidence)** | End-to-End-Nachweiskette: Requirement → Design Principle → Gate-Instanz → Evidence Record. Clause-to-Control Traceability. | DP2, Art. 11/12 | Nweke 2026 (Q5✅ Clause-to-Control), Muhammad 2026 (Q5✅ readiness score), Kholkar 2025 (Q5✅ provenance) | 🟢 Q5 PERFEKT — 9/9 Quellen |
| **M9** | Abs. 9 | **Synthese + Brücke zu 5.5** | Evidence Store als technische Realisierung von S4. Alle 16 Gate-Instanzen → persistierte, fälschungssichere Evidence Records. Forward-Link: Azure PostgreSQL Flexible Server im PoC. | Alle DP, RQ2 | Butt 2026 (Gesamt-Top), Muhammad 2026 (AAC-Referenz), Burns 2025 (Dynamo real-world) | Synthese-Absatz |

---

## Quellen-Einsatzplan (wer wo zitiert wird)

| Quelle | Zotero-Key | Moves | Rolle |
|--------|------------|-------|-------|
| **Butt (2026)** | V6HKHA5B | M2, M3, M5, M6, M7, M9 | **Primärquelle** — höchster Score (5+2⚠️/7), einzige Q2-Evidenz |
| **Muhammad (2026)** | IZVYTSTV | M2, M5, M6, M8, M9 | **Primärquelle** — Audit-as-Code Namengeber, CAC/AAC-Kern |
| **Kholkar & Ahuja (2025)** | VLMNBUST | M1, M3, M4, M8 | **Primärquelle** — Policy-as-Prompt, Least Privilege, Provenance |
| **Nweke & Yeng (2026)** | XCM4Q2WP | M1, M8 | **Stützquelle** — Clause-to-Control, Compliance-as-Code |
| **Eisenberg (2025)** | JUK36XAW | M2, M4, M5, M6 | **Stützquelle** — UCF Schema, Access Controls |
| **Burns (2025)** | 2GGF93BE | M4, M9 | **Stützquelle** — Dynamo real-world, EU AI Act Compliance |
| **Pistilli (2023)** | 3774R8Y6 | (optional M2) | **Sekundär** — Governance-Rahmen, schwacher Einzelbeitrag für 5.4 |
| **Lucaj (2025)** | 5Y79UTJ9 | (optional M1) | **Sekundär** — "immutable artifact", Template-Felder als Schema-Input |
| **Golpayegani (2024)** | 7BF458GD | M1 (optional) | **Sekundär** — AICat Metadata, nur bei Schema-Feldern |
| **Joseph (2023)** | Elicit | **M7** | **Supplementary** — Merkle Trees + Performance für Hash-Chain DP5.3. ⚠️ Venue-Caveat |

---

## DSR-Eigenleistungen (explizit im Text markieren)

| # | DSR-Eigenleistung | Move | Begründung (warum Literaturlücke) |
|---|-------------------|------|-----------------------------------|
| **E1** | **Hash-Chain-Immutability (DP5.3)** | M7 | Q2 Matrix: 1/9 explizit (Butt). Kein Paper beschreibt SQL-Level Hash-Chain für AI-Governance Evidence Stores. Joseph (2023) liefert Merkle-Tree-Technik, aber nicht AI-Governance-spezifisch. → Design-Beitrag. |
| **E2** | **Payload/Telemetrie-Trennung (R3)** | M1 | Q3 Matrix: 3 explizit, 4 implizit. Architekturprinzip (encrypted Blob vs. SQL) in keiner Quelle als dediziertes Pattern. → Architektur-Design. |
| **E3** | **Performance SLO 100ms (DP5.2)** | M5 | Keine Quelle definiert quantitative Performance-Ziele für Audit-Query-Response. → Engineering-Beitrag. |
| **E4** | **PostgreSQL Evidence Store Schema (Gesamt)** | M2 | Synthese aus 9 Quellen zu 5 Komponenten mit DP-Mapping. Keine Quelle liefert vollständiges Schema. → Integrations-Artefakt. |

---

## Rhetorische Strategie

### Grundmuster pro Absatz:
```
1. CLAIM:  Was wird behauptet? (1 Satz)
2. EVIDENZ: Welche Quelle(n) stützen das? (APA7 mit PDF-Seite)
3. DESIGN: Wie wird es im DSR-Artefakt operationalisiert? (Schema-Bezug)
4. BRIDGE: Überleitung zum nächsten Move (1 Satz)
```

### Zitationsmuster:
- **Gut abgedeckt (Q1,Q4-Q7):** Mindestens 2 Quellen pro Claim → Triangulation
- **Moderate Lücke (Q3):** 1 Quelle + DSR-Eigenleistung klar markieren
- **Kritische Lücke (Q2):** Butt + Joseph als "nächste Referenzen", dann DSR-Eigenleistung argumentieren:
  > "Während Butt (2026) content-addressed artifacts als Integritätsmechanismus identifiziert und Joseph (2023) Merkle-Tree-basierte Audit-Trails mit <5ms Verifikationslatenz nachweist, adressiert keine existierende Arbeit die spezifische Anforderung kryptographischer Verkettung in SQL-basierten AI-Governance Evidence Stores. Die vorliegende Architektur schließt diese Lücke durch [...]."

### DSR-Eigenleistung-Framing:
```
Pattern: "Die Literaturanalyse (vgl. Tab. X) zeigt, dass [Aspekt] in der
bestehenden Forschung nicht adressiert wird. Im Sinne des DSR-Design-Cycle
(Hevner et al., 2004) wird [Mechanismus] als eigenständiger Design-Beitrag
entwickelt, der [DP-x] operationalisiert."
```

---

## CAC/AAC-Differenzierung (aus 5.3 aufgreifen)

| Dimension | Compliance-as-Code (CAC) | Audit-as-Code (AAC) |
|-----------|-------------------------|---------------------|
| **Zeitpunkt** | Präventiv (Pre-/Deployment) | Post-hoc (Operations) |
| **Mechanismus** | Conftest + Gatekeeper Policies | Decision Logs + Evidence Records |
| **Quelle** | Nweke 2026, Kholkar 2025 | Muhammad 2026 (namensgebend) |
| **In 5.4** | M3 (Immutability-Trigger), M4 (RBAC) | M6 (quality_gate_results), M7 (Hash-Chain) |
| **Artefakt** | Rego-Policies (→ 5.3) | Evidence Store Schema (→ 5.4) |

→ In M6 explizit aufgreifen: "Die in Abschnitt 5.3 eingeführte Differenzierung [...] manifestiert sich im Evidence Store Schema als [...]"

---

## Negativ-Checklist (aus Preflight — PFLICHT einhalten)

- ❌ Keine Provider-Perspektive (Art. 16) — nur Deployer-Scope (Art. 26)
- ❌ Keine vollständigen SQL-DDL-Listings — nur konzeptuelle Schema-Beschreibung
- ❌ Keine Wiederholung Gate-Taxonomie aus 5.2 — nur Verweis
- ❌ Keine Wiederholung Policy-Engine aus 5.3 — nur Brücke
- ❌ Keine Azure-Details — gehören in 5.5 (PoC)
- ❌ Keine formalen Überleitungen ("Im Folgenden wird...") — PK-V2
- ❌ Keine DSR-Methodenbeschreibung — SRH-Leitfaden
- ❌ Kein Retirement/Decommissioning
- ❌ Keine DP-Definitionen wiederholen — in 5.1 definiert

---

## Inhalts-Checklist (✓ = muss im Text vorkommen)

- [ ] M1: Payload/Telemetrie-Trennung (R3, DSGVO Art. 9) motiviert
- [ ] M2: Evidence Store Schema als DSR-Artefakt (5 Komponenten + DP-Mapping)
- [ ] M3: Immutability-Trigger (SQL-Trigger, DP2+DP5.3)
- [ ] M4: Least-Privilege RBAC (CI/CD INSERT-only, DP5)
- [ ] M5: Composite Indexes + 100ms SLO (DP5.2)
- [ ] M6: quality_gate_results Table + CAC/AAC-Differenzierung
- [ ] M7: Hash-Chain SHA-256 (DP5.3) + DSR-Eigenleistung + Art. 12
- [ ] M8: Traceability-Kette R→DP→Gate→Evidence
- [ ] M9: Synthese + Brücke 5.5 (Azure PostgreSQL PoC)
- [ ] Joseph (2023) mit Venue-Caveat zitiert
- [ ] CAC/AAC aus 5.3 aufgegriffen und vertieft
- [ ] Mind. 1 DSR-Eigenleistung explizit als solche benannt

---

## Wortschätzung (bei D_QUALITY_OVER_PAGES)

| Unterabschnitt | Moves | Geschätzte Wörter | Seiten (~250W/S) |
|----------------|-------|-------------------|------------------|
| 5.4.1 Evidence-Persistierung | M1–M5 | 600–750 W | ~2.5–3.0 S |
| 5.4.2 Audit-Trail + Nachweiskette | M6–M9 | 500–650 W | ~2.0–2.5 S |
| **Gesamt 5.4** | **M1–M9** | **1100–1400 W** | **~4.5–5.5 S** |

→ Passt mit D_QUALITY_OVER_PAGES (keine harte Obergrenze)

---

## Sequenz für GO

1. **PoC-SQL-Schema Master-MD** erstellen (Arbeitsdatei mit DDL-Entwurf + DP-Mapping + APA7 PDF-Seitenangaben) — damit der Writer konkrete Schema-Referenzen hat
2. **GO Kap. 5.4** → thesis-writer Skill, Move für Move
3. **Prüfprotokoll** pro Absatz (BELEG/CLAIM/MATCH)
4. **Post-Session** → chapter_state + Entscheidungsregister aktualisieren
