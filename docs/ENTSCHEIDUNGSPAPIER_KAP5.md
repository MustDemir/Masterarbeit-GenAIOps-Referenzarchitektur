# Entscheidungspapier Kapitel 5 — Architektur-Decisions

**Datum:** 2026-03-11
**Status:** 4 neue Entscheidungen + 8 übernommene Architektur-Decisions (R1–R8)
**Kontext:** Preflight Kap. 5 Referenzarchitektur (RQ2) — Klärung offener Design-Entscheidungen vor Schreibbeginn

---

## Gesamtübersicht

| # | Decision-ID | Thema | Status | Kern-Ergebnis |
|---|---|---|---|---|
| 1 | D_KAP5_SECTION_ORDER | Schreibreihenfolge Kap. 5 | ✅ FINAL | Sequentiell 5.1→5.2→5.3→5.4→5.5→5.6 |
| 2 | D_DP_NUMBERING | Designprinzipien-Nummerierung | ✅ FINAL | DP1–DP5 (Exposé-SSOT) + DP5.2/DP5.3 als Erweiterungen |
| 3 | D_GATE_ID_SCHEMA | Gate-ID-Format | ✅ FINAL | G-PRE-xx / G-DEP-xx / G-OPS-xx (Lifecycle-Phase-Präfix) |
| 4 | D_GATEKEEPER_STANDALONE | Gatekeeper-Deployment | ✅ FINAL | Standalone OPA Gatekeeper auf AKS, kein Azure Policy Add-on |

---

## Entscheidung 1: D_KAP5_SECTION_ORDER

**Frage:** Sequentielle oder parallele Bearbeitung der Unterabschnitte?

**Entscheidung:** Strikt sequentiell: 5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6

**Begründung:**
- 5.3 (Gate-System) benötigt 5.2 (Schichtenmodell) als Architekturrahmen
- 5.4 (Pipeline + PaC) benötigt 5.3 (Gate-Specs) als Input für Rego-Policies
- 5.5 (Evidence) benötigt 5.4 (Pipeline-Output) als Datenquelle
- 5.6 (PoC) instanziiert alle vorherigen Abschnitte

**Datum:** 2026-03-11

---

## Entscheidung 2: D_DP_NUMBERING

**Frage:** DP1–DP5 aus Exposé beibehalten oder auf DP1–DP7 erweitern (Hash-Chain, Immutability)?

**Entscheidung:** DP1–DP5 beibehalten. Hash-Chain und Immutability als DP5.2 und DP5.3 unter DP5 (Evidence-Persistierung) in Abschnitt 5.5 einführen.

**Begründung:**
- Exposé = SSOT für Designprinzipien, keine Umnummerierung
- Hash-Chain und Immutability sind Sub-Aspekte von DP5 (Evidence-Persistierung), keine eigenständigen Top-Level-Prinzipien
- Sub-Nummerierung (DP5.2/DP5.3) zeigt Erweiterungsbedarf ohne Exposé-Drift
- Konsistenz mit Kap. 3 (DSR-Artefaktbeschreibung referenziert DP1–DP5)

**Evidence:**
- Exposé v4: definiert DP1–DP5
- Evidence Store Architektur (eigenes Artefakt): nutzt DP-6/DP-7 → wird zu DP5.2/DP5.3 renummeriert

**Datum:** 2026-03-11

---

## Entscheidung 3: D_GATE_ID_SCHEMA

**Frage:** Welches ID-Format für Quality Gates?

**Optionen analysiert:**
- Option A: `G-PRE-xx`, `G-DEP-xx`, `G-OPS-xx` (Lifecycle-Phase als Präfix)
- Option B: `G-REG-xx`, `G-TECH-xx`, `G-STRAT-xx` (Governance-Dimension als Präfix)
- Option C: `G001`–`Gxxx` (flache Nummerierung)

**Entscheidung:** Option A — Lifecycle-Phase als Präfix.

**Begründung — Literaturanalyse:**

| Quelle | Gate-Organisation | Ergebnis |
|---|---|---|
| Cooper (2008) Stage-Gate | Phase-Gates: Discovery → Launch | Lifecycle-Phase = primäres Ordnungsprinzip |
| Elia et al. (2025) MQG4AI | Lifecycle-Stages: Pre-Development → Post-Deployment | Lifecycle-Phase als Rahmen, Quality Dimensions als Attribute |
| Lucaj et al. (2025) TechOps | Template-Sektionen nach Lifecycle | Kein formales Gate-ID, aber implizit lifecycle-basiert |
| Kholkar et al. (2023) | Stage-Gates in CI/CD | Gates an Pipeline-Stages gebunden |

**Konsequenz:** Governance-Dimension (regulatorisch/technisch/strategisch) wird als Attribut im Gate-Template geführt, nicht im ID. Das ermöglicht:
- Sofortige Lifecycle-Zuordnung beim Lesen (G-PRE = Pre-Deployment)
- Multi-dimensionale Gates (ein Gate kann regulatorisch UND technisch sein)
- Konsistenz mit D_OPA_THREE_PILLAR (Conftest=PRE/DEP, Gatekeeper=DEP/OPS)

**Datum:** 2026-03-11

---

## Entscheidung 4: D_GATEKEEPER_STANDALONE

**Frage:** Azure Policy Add-on oder standalone OPA Gatekeeper auf AKS?

**Entscheidung:** Standalone OPA Gatekeeper.

**Begründung:**
- **R7 (Cloud-agnostisch):** Standalone Gatekeeper läuft identisch auf AKS, EKS, GKE, on-prem
- **Azure Policy Add-on:** Vendor-Lock-in, überschreibt eigene ConstraintTemplates, managed by Microsoft
- **Technische Details:** Helm-Installation, ConstraintTemplates in Rego, Constraints als CRDs
- **PoC-Impact:** Keine Azure-spezifischen Anpassungen nötig. Gleiche Config auf jedem K8s-Cluster

**Abgrenzung:** Azure Policy Add-on kann parallel existieren (für Azure-native Governance), aber die Thesis-Architektur nutzt den standalone Gatekeeper für die eigenen Compliance-Gates.

**Datum:** 2026-03-11

---

## Übernommene Architektur-Decisions R1–R8

> Quelle: `.memory/entscheidungsregister.md` Sektion 3 (aus Design-Thinking Sessions Feb/März 2026).
> Diese Decisions sind in keinem chapter_state dokumentiert und weiterhin gültig.

| ID | Datum | Entscheidung | Auswirkung auf Kap. 5 |
|---|---|---|---|
| R1 | 2026-02-24 | Diagramme: S/W, große Schrift (15–22pt), Times New Roman | 5.2 Architektur-Diagramm, 5.4 Pipeline-Diagramm |
| R2 | 2026-02-24 | 3-Quellen-Verifikation (Exposé × Diagramm × USPs) | QS-Maßnahme für jede Architekturentscheidung |
| R3 | 2026-02-26 | Harte Trennung: med. Payload (Blob, verschlüsselt) vs. regulat. Telemetrie (SQL) | 5.5 Evidence Store Architektur |
| R4 | 2026-02-28 | DP4 = thematische Prüfdimensionen (NICHT hierarchisch) | 5.1 Designprinzipien, 5.3 Gate-Taxonomie |
| R5 | 2026-02-28 | Make-or-Buy = vorgelagerte Governance-Entscheidung, KEIN Gate | 5.3 Negativ-Checklist |
| R6 | 2026-03-02 | 3D-Taxonomie + einheitliches Gate-Template (Trigger/Kriterien/Evidence/Decision/Owner/Audit/Waiver) | 5.3 Gate-Template-Definition |
| R7 | 2026-03-02 | Cloud-agnostisch portabel, Azure als PoC-Referenz | 5.2 + 5.6 |
| R8 | 2026-02-25 | CDV-Framework: Contract → Validation → Severity → Pipeline-Decision | 5.3 Gate-Decision-Logik |

---

## Decision-Precedence-Regel

Bei Konflikten zwischen Entscheidungsquellen gilt:

**Kap. 4 chapter_state > Kap. 3 chapter_state > Kap. 2 chapter_state > Kap. 1 chapter_state > .memory/entscheidungsregister.md**

Neueste Decision gewinnt immer. Das Entscheidungsregister (.memory/) ist veraltet (Stand 2026-03-05), enthält aber R1–R8 als einzige Quelle → diese bleiben gültig.

---

## Bindende Decisions aus Kap. 4 chapter_state (Referenz)

Diese Decisions aus Kap. 4 sind für Kap. 5 direkt bindend und werden NICHT hier wiederholt, sondern per Referenz eingebunden:

- D_4.6_VS_5.3_SEPARATION — WAS (R-xx) → WIE (G-xx)
- D_GOV_DIMENSIONS_HYBRID — Governance-Dimensionen durch NIST/ISO legitimieren
- D_NIST_CONVERGENCE — Konvergenz-Tabelle in 5.1
- D_KONSOLIDIERUNG_AUFGELOEST — Clustering → Gate-Taxonomie
- D_OPA_THREE_PILLAR — Conftest / Gatekeeper / Decision Logs
- D_GATEKEEPER_SCOPE — PoC: 2 Label + 1 technischer Constraint
- D_LOG_BACKEND — Decision Logs → PostgreSQL Evidence Store
- D_LUCAJ_STARTING_BASIS — TechOps Templates als Rego-Ausgangsbasis
- D_POC_REGO_K8S — Echter Rego-Code auf AKS

→ Details: `04_anforderungsanalyse_RQ1/chapter_state.yaml`

---

## Nächste Arbeitsschritte

1. ☐ Kap. 5 chapter_state initialisieren (decisions, key_sources, next_steps)
2. ☐ Abschnitt 5.1 schreiben (Designprinzipien + Konvergenz)
3. ☐ R1–R8 in chapter_state Kap. 5 übernehmen
4. ☐ Entscheidungsregister (.memory/) mit neuen D_-IDs synchronisieren (Post-Session)
