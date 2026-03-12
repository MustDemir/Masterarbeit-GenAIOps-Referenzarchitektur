# VALIDIERUNGSLAUF: D_GATE_INCLUSION_RULE v3.0 → R001–R014
**Datum: 2026-03-12 | Durchführung: Demir (mit KI-Unterstützung)**
**Zweck: Systematische Anwendung der D_GATE_INCLUSION_RULE auf alle 14 Deployer-Requirements**
**Methode: D1 → D3 → D2 → Override-Check → Gate-Typ-Zuordnung**
**Input: R001–R014 YAML-Files + D_GATE_INCLUSION_RULE v3.0**

---

## 0. Leitfrage des Durchlaufs

> "Welche Requirements können automatisiert als Quality Gate in der CI/CD-Pipeline
> geprüft werden — und wo zwingt uns die EU AI Act Oversight-Pflicht (Art. 14)
> zu menschlicher Beteiligung?"

**Stellhebel:** D3 (Oversight-Typ) bestimmt die Automatisierungsgrenze.
D3=FIRST-DEGREE → D2 ≤ HYBRID (Mensch muss beteiligt sein).
D3=SECOND-DEGREE → D2 kann VOLL sein (rein automatisiert möglich).

---

## 1. Ergebnis-Übersicht

| R_xx | Titel (kurz) | Phase | D1 | D3 | D2 | Override? | **Gate-Typ** |
|------|-------------|-------|----|----|----|----|-----------|
| R001 | Risikomanagement | Pre-Depl. | JA | FIRST | HYBRID | — | **HYBRID** |
| R002 | Techn. Dokumentation | Deployment | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R003 | Robustheit/Safety | Deployment | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R004 | Human Oversight (pre) | Pre-Depl. | JA | FIRST | HYBRID | — | **HYBRID** |
| R005 | Evidence-Persistierung | Operation | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R006 | Eingabedaten-Qualität | Deployment | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R007 | Nutzertransparenz | Deployment | JA | SECOND | HYBRID | — | **HYBRID** |
| R008 | Oversight-Wirksamkeit | Operation | JA | FIRST | HYBRID | — | **HYBRID** |
| R009 | Incident Reporting | Operation | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R010 | Drift-Monitoring/PMS | Operation | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R011 | CE/Konformität | Pre-Depl. | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R012 | FRIA (Grundrechte) | Pre-Depl. | JA | FIRST | HYBRID | — | **HYBRID** |
| R013 | Bias/Fairness-Monit. | Operation | JA | SECOND | VOLL | — | **AUTOMAT.** |
| R014 | Logging/Protokollierung | Deployment | JA | SECOND | VOLL | — | **AUTOMAT.** |

### Verteilung Gate-Typen:
- **AUTOMATISIERT:** 9/14 (64,3%) — R002, R003, R005, R006, R009, R010, R011, R013, R014
- **HYBRID:** 5/14 (35,7%) — R001, R004, R007, R008, R012
- **MANUELL:** 0/14 (0%)
- **QUERSCHNITTLICH:** 0/14 (0%)

---

## 2. Einzelbewertungen (Detailliert)

### R001 — Risikomanagement (Art. 9) → HYBRID GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: risk_assessment_report, mitigation_plan
  D1.2 Akzeptanzkriterien? → JA: "versioniert und dem Release zugeordnet",
                              "Mitigationsplan pro High-Risk-Risiko"
  D1.3 Handlungsrelevanz?  → JA: Kein Deployment ohne Risk Assessment → BLOCK
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → JA
    Risikobewertung beeinflusst KONSTITUTIV ob/wie System deployed wird.
    Mensch muss Risiken identifizieren, bewerten, Mitigationen festlegen.
    Kein Algorithmus kann "Angemessenheit" einer Risikominderung
    autonom beurteilen.
  → D3 = FIRST-DEGREE

D2-Prüfung:
  D2.1 Deterministisch?  → TEILWEISE
    - Report-Existenz: deterministisch (file exists?)
    - Versionierung: deterministisch (version tag present?)
    - Inhaltliche Vollständigkeit: NICHT deterministisch
      (sind ALLE relevanten Risiken identifiziert?)
    - Mitigations-Angemessenheit: NICHT deterministisch
      (qualitatives Urteil über Wirksamkeit)
  D2.3 Teilweise maschinenauswertbar? → JA
    Formale Aspekte automatisierbar, Inhalt erfordert Experten-Review
  → D2 = HYBRID

Override-Check: D3=FIRST + D2=HYBRID → kein Conflict, bleibt HYBRID
Begründung: Override wäre relevant wenn jemand versucht, Risk Assessment
  auf reinen Existenz-Check zu reduzieren (D2→VOLL). D3=FIRST verhindert das.

ERGEBNIS: R001 → HYBRID GATE
  Auto-Check: Report existiert, versioniert, Release-zugeordnet
  Human-Review: Vollständigkeit der Risikoidentifikation,
                Angemessenheit der Mitigationsmaßnahmen
```

### R002 — Technische Dokumentation (Art. 11) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: technical_documentation, model_card,
                              release_artifact_reference
  D1.2 Akzeptanzkriterien? → JA: "Doku verweist auf Modellversion",
                              "Log-Referenzen auffindbar"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne Doku
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Technische Dokumentation = Nachweisartefakt, beeinflusst nicht den
    AI-Output selbst. Auditierbarkeit = korrektive, ex-post Funktion.
  D3.2 Korrektive ex-post-Prüfung? → JA
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA
    - Doku vorhanden? → file exists
    - Model Card ausgefüllt? → Felder ≠ leer (Lucaj TechOps-Template)
    - Release-Referenz korrekt? → Version-Match
  D2.2 Evidence automatisch sammelbar? → JA
    Pipeline-Artefakte, CI/CD-Metadaten
  → D2 = VOLL

Override-Check: D3=SECOND → kein Override

ERGEBNIS: R002 → AUTOMATISIERTES GATE
  Impl.: Policy-as-Code → Prüfe TechOps-Template-Felder (Lucaj)
  Evidence: OSCAL-Package mit Doku-Referenzen
```

### R003 — Robustheit, Genauigkeit, Sicherheit (Art. 15) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: eval_metrics_report, safety_test_report
  D1.2 Akzeptanzkriterien? → JA: "Metriken über definierten Mindestwerten",
                              "fehlgeschlagene Safety-Checks → BLOCK"
  D1.3 Handlungsrelevanz?  → JA: BLOCK bei Safety-Failure
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Schwellenwertprüfung = deterministische Metrik-Auswertung.
    Kein konstitutiver menschlicher Einfluss auf den AI-Output.
  D3.2 Korrektive ex-post-Prüfung? → JA (Test nach Training)
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA (Metrik ≥ Threshold?)
  D2.2 Evidence automatisch? → JA (Pipeline-Metriken, Test-Reports)
  → D2 = VOLL

ERGEBNIS: R003 → AUTOMATISIERTES GATE
  Impl.: Threshold-Gate in CI/CD (Muhammad PASS/WARN/BLOCK)
  Evidence: Eval-Metriken + Safety-Test-Results
```

### R004 — Human Oversight Pre-Deployment (Art. 14) → HYBRID GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: oversight_roles_matrix, escalation_procedure
  D1.2 Akzeptanzkriterien? → JA: "Owner benannt und freigegeben",
                              "Eskalationsprozess versioniert"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne Oversight-Plan
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → JA
    Art. 14(4): "understand, interpret, override, interrupt"
    Oversight-Rollen beeinflussen konstitutiv, wie AI-Output behandelt wird.
    Mensch muss VOR Deployment festlegen, wer eingreifen kann/darf/muss.
  → D3 = FIRST-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → TEILWEISE
    - Oversight-Plan existiert? → deterministisch
    - Rollen zugewiesen? → deterministisch
    - Qualifikation der Oversight-Person? → qualitatives Urteil
    - Angemessenheit der Eskalationswege? → qualitatives Urteil
  D2.3 Teilweise maschinenauswertbar? → JA
  → D2 = HYBRID

Override-Check: D3=FIRST + D2=HYBRID → kein Conflict

ERGEBNIS: R004 → HYBRID GATE
  Auto-Check: Plan existiert, Rollen zugewiesen, Eskalationsdokument vorhanden
  Human-Review: Qualifikation prüfen, Eskalationswege bewerten
```

### R005 — Evidence-Persistierung (Art. 12, 15) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: immutable_storage_reference, audit_trail_entry
  D1.2 Akzeptanzkriterien? → JA: "Referenzen pro Gate-Lauf vorhanden",
                              "Änderungen technisch eingeschränkt"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne Audit-Trail
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Evidence-Ablage = Infrastruktur-Requirement. Beeinflusst nicht den
    AI-Output, sondern die Nachweisbarkeit von Gate-Entscheidungen.
  D3.2 Korrektive ex-post-Prüfung? → JA
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA
    - Storage-Referenz vorhanden? → deterministisch
    - Immutability-Flag gesetzt? → deterministisch
    - Audit-Trail-Eintrag erzeugt? → deterministisch
  D2.2 Evidence automatisch? → JA (Pipeline-Metadaten)
  → D2 = VOLL

ERGEBNIS: R005 → AUTOMATISIERTES GATE
  Impl.: Policy-as-Code Check auf Evidence-Store-Konfiguration
  HINWEIS: R005 hat zusätzlich Q-Charakter (wirkt in JEDEM Gate),
    wird aber als eigenständiges Infrastruktur-Gate geprüft.
```

### R006 — Eingabedaten-Qualität (Art. 10, Art. 26/4) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: input_validation_report,
                              schema_conformance_check, data_quality_metrics
  D1.2 Akzeptanzkriterien? → JA: "Schema-Konformität",
                              "Plausibilitätschecks automatisch ausgeführt"
  D1.3 Handlungsrelevanz?  → JA: BLOCK bei Schema-Verletzung
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Schema-Validierung = deterministischer Eingabe-Check, kein
    konstitutiver menschlicher Einfluss auf AI-Entscheidung.
  D3.2 Korrektive ex-post-Prüfung? → JA (Validierung vor Inferenz,
    aber technisch-korrektiv, nicht konstitutiv)
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA (Schema-Match, Wertebereich-Check)
  D2.2 Evidence automatisch? → JA (Validierungsreports)
  → D2 = VOLL

ERGEBNIS: R006 → AUTOMATISIERTES GATE
  Impl.: Schema-Validation + Plausibilitäts-Rules in Pipeline
```

### R007 — Nutzertransparenz (Art. 13, Art. 50) → HYBRID GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: transparency_notice,
                              user_information_document,
                              ai_content_labeling_config
  D1.2 Akzeptanzkriterien? → JA: "sichtbar und verständlich",
                              "Informationspflichten dokumentiert",
                              "KI-generierte Inhalte gekennzeichnet"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne Transparenzhinweis
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Transparenzdokumentation informiert Nutzer über AI-Einsatz,
    beeinflusst aber nicht konstitutiv den AI-Output selbst.
  D3.2 Korrektive ex-post-Prüfung? → JA (informativ/korrektiv)
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → TEILWEISE
    - Transparenzhinweis existiert? → deterministisch
    - Labeling-Config aktiv? → deterministisch
    - "Verständlich"? → NICHT deterministisch (qualitatives Urteil)
    - Art. 50 Kennzeichnung korrekt? → teilweise deterministisch
  D2.3 Teilweise maschinenauswertbar? → JA
  → D2 = HYBRID

Override-Check: D3=SECOND → kein Override

ERGEBNIS: R007 → HYBRID GATE
  Auto-Check: Transparenzhinweis existiert, Labeling aktiv,
              Pflichtfelder ausgefüllt
  Human-Review: Verständlichkeit, sprachliche Angemessenheit,
                Vollständigkeit der Information
  BEGRÜNDUNG für HYBRID trotz D3=SECOND: D2 allein ergibt HYBRID
    wegen qualitativer "Verständlichkeit"-Bewertung (Art. 13).
```

### R008 — Operative Oversight-Wirksamkeit (Art. 14, Art. 26/2) → HYBRID GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: oversight_effectiveness_report,
                              sterz_conditions_assessment, intervention_log
  D1.2 Akzeptanzkriterien? → JA: "periodische Prüfung konfiguriert",
                              "Eingriffe protokolliert",
                              "Defizite → Eskalation"
  D1.3 Handlungsrelevanz?  → JA: Eskalation/BLOCK bei Wirksamkeitsdefizit
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → JA
    Dies IST das operative Oversight-Requirement. Die Bewertung der
    Sterz-Bedingungen (Causal Power, Epistemic Access, Self-Control,
    Fitting Intentions) bestimmt, ob menschliche Aufsicht wirksam ist.
    Defizite beeinflussen konstitutiv den Weiterbetrieb des Systems.
  → D3 = FIRST-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → TEILWEISE
    - Wirksamkeitsbericht existiert? → deterministisch
    - Intervention-Log vorhanden? → deterministisch
    - Sterz-Bedingungen erfüllt? → NICHT deterministisch
      (Causal Power, Epistemic Access = qualitatives Urteil)
  D2.3 Teilweise maschinenauswertbar? → JA
  → D2 = HYBRID

Override-Check: D3=FIRST + D2=HYBRID → kein Conflict

ERGEBNIS: R008 → HYBRID GATE
  Auto-Check: Reports existieren, Intervention-Log vorhanden,
              periodische Prüfung konfiguriert
  Human-Review: Sterz-Bedingungen-Assessment,
                Wirksamkeitsbewertung der Oversight-Maßnahmen
```

### R009 — Schwerwiegende Vorfälle / Incident Reporting (Art. 26/5, Art. 73) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: incident_detection_config,
                              incident_report, notification_timestamp_log
  D1.2 Akzeptanzkriterien? → JA: "Detection-Regeln konfiguriert und aktiv",
                              "Meldung innerhalb gesetzlicher Frist"
  D1.3 Handlungsrelevanz?  → JA: BLOCK bei fehlender Incident-Konfiguration
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Incident Detection = automatisierte Erkennung + Meldeworkflow.
    Ex-post, korrektiv. Kein konstitutiver Einfluss auf AI-Output.
  D3.2 Korrektive ex-post-Prüfung? → JA
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA
    - Detection-Regeln konfiguriert? → deterministisch
    - Frist eingehalten (Timestamp < Deadline)? → deterministisch
    - Reports versioniert? → deterministisch
  D2.2 Evidence automatisch? → JA (Timestamps, Config-Checks)
  → D2 = VOLL

ERGEBNIS: R009 → AUTOMATISIERTES GATE
  Impl.: Policy-as-Code Check auf Incident-Konfiguration + Frist-Monitoring
```

### R010 — Post-Market Surveillance / Drift-Monitoring (Art. 72, Art. 9/2) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: drift_monitoring_dashboard,
                              drift_alert_log, pms_periodic_report
  D1.2 Akzeptanzkriterien? → JA: "Metriken definiert und erhoben",
                              "Schwellenwert-Alerts dokumentiert"
  D1.3 Handlungsrelevanz?  → JA: WARN/BLOCK bei fehlender Konfiguration
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Drift-Monitoring = automatisierte, kontinuierliche Überwachung.
    Korrektive Funktion (ex post).
  D3.2 Korrektive ex-post-Prüfung? → JA
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA (Metriken-Thresholds, Alert-Konfiguration)
  D2.2 Evidence automatisch? → JA (Pipeline-Metriken, Logs)
  → D2 = VOLL

ERGEBNIS: R010 → AUTOMATISIERTES GATE
  Impl.: Continuous Monitoring mit automatisierter Drift-Detection
```

### R011 — Konformitätserklärung / CE-Kennzeichnung (Art. 26/1, 47, 48) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: conformity_declaration_check,
                              ce_marking_verification,
                              provider_documentation_receipt
  D1.2 Akzeptanzkriterien? → JA: "EU-Konformitätserklärung gültig",
                              "CE-Kennzeichnung vorhanden"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne Konformität
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    CE-Check = administrative Prüfung, ob Provider-Dokumentation vorliegt.
    Kein konstitutiver Einfluss auf AI-Output.
  D3.2 Korrektive ex-post-Prüfung? → JA (Eingangsprüfung)
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA
    - Erklärung vorhanden? → deterministisch
    - CE-Marking? → deterministisch
    - Gültigkeitsdatum? → deterministisch
  D2.2 Evidence automatisch? → JA (Dokument-Existenz + Metadaten)
  → D2 = VOLL

ERGEBNIS: R011 → AUTOMATISIERTES GATE
  Impl.: Policy-as-Code Eingangsprüfung vor Deployment
```

### R012 — Grundrechte-Folgenabschätzung / FRIA (Art. 27) → HYBRID GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: fria_document, stakeholder_impact_assessment
  D1.2 Akzeptanzkriterien? → JA: "FRIA abgeschlossen und versioniert",
                              "Grundrechte identifiziert und bewertet"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne FRIA
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → JA
    FRIA = konstitutive Bewertung VOR dem Einsatz. Die Grundrechte-
    Folgenabschätzung bestimmt, OB und WIE das System eingesetzt
    werden darf. Mensch muss Grundrechtseingriffe bewerten — das ist
    per Definition nicht algorithmisch lösbar.
  → D3 = FIRST-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → TEILWEISE
    - FRIA-Dokument existiert? → deterministisch
    - Versioniert? → deterministisch
    - Alle relevanten Grundrechte identifiziert? → NICHT deterministisch
    - Mitigationsmaßnahmen angemessen? → NICHT deterministisch
  D2.3 Teilweise maschinenauswertbar? → JA
  → D2 = HYBRID

Override-Check: D3=FIRST + D2=HYBRID → kein Conflict.
  ABER: D3-Override hätte Wirkung wenn jemand D2→VOLL argumentiert
  (z.B. "FRIA = Checklist, Existenz reicht"). D3=FIRST verhindert das:
  Grundrechte-Bewertung DARF NICHT auf Existenz-Check reduziert werden.

ERGEBNIS: R012 → HYBRID GATE
  Auto-Check: FRIA existiert, versioniert, Stakeholder-Gruppen benannt
  Human-Review: Vollständigkeit der Grundrechte-Identifikation,
                Angemessenheit der Mitigationen,
                Bewertung der Verhältnismäßigkeit
```

### R013 — Bias- und Fairness-Monitoring (Art. 9/2, Art. 10/2, Art. 15) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: bias_metrics_report,
                              fairness_evaluation_log,
                              alert_and_remediation_log
  D1.2 Akzeptanzkriterien? → JA: "Metriken definiert und erhoben",
                              "Schwellenwerte konfiguriert",
                              "Alerts dokumentiert"
  D1.3 Handlungsrelevanz?  → JA: WARN/BLOCK bei Schwellenwertüberschreitung
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Bias-MONITORING = kontinuierliche, automatisierte Metriken-Erhebung.
    Korrektive Funktion (erkennt Abweichungen ex post).
    ABGRENZUNG: Die initiale DEFINITION von Fairness-Metriken (WAS
    ist fair?) wäre D3=FIRST, aber das ist in R001 (Risikomanagement)
    verortet, nicht hier. R013 prüft nur: läuft das Monitoring?
  D3.2 Korrektive ex-post-Prüfung? → JA
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA (Metriken konfiguriert? Thresholds gesetzt?)
  D2.2 Evidence automatisch? → JA (Monitoring-Logs, Alert-Historie)
  → D2 = VOLL

ERGEBNIS: R013 → AUTOMATISIERTES GATE
  Impl.: Policy-as-Code Check auf Monitoring-Konfiguration + Threshold-Alerting
  HINWEIS: R013 ist SHOULD (nicht MUST) → Gate-Ergebnis = WARN statt BLOCK
```

### R014 — Automatische Protokollierung / Logging (Art. 12, Art. 26/3) → AUTOMATISIERTES GATE

```
D1-Prüfung:
  D1.1 Deliverables?    → JA: logging_config_verification,
                              log_retention_policy, log_accessibility_test
  D1.2 Akzeptanzkriterien? → JA: "Logging aktiviert",
                              "Aufbewahrungsfrist gesetzeskonform",
                              "Logs zugänglich und auswertbar"
  D1.3 Handlungsrelevanz?  → JA: BLOCK ohne Logging
  → D1 = JA

D3-Prüfung:
  D3.1 Counterfactual influence? → NEIN
    Logging = Infrastruktur-Requirement, kein konstitutiver Einfluss
    auf AI-Output. Korrektiv/nachweisend.
  D3.2 Korrektive ex-post-Prüfung? → JA
  → D3 = SECOND-DEGREE

D2-Prüfung:
  D2.1 Deterministisch? → JA (Logging aktiv? Retention ≥ 6 Monate?)
  D2.2 Evidence automatisch? → JA (Config-Check, Retention-Policy)
  → D2 = VOLL

ERGEBNIS: R014 → AUTOMATISIERTES GATE
  Impl.: Policy-as-Code Check auf Logging-Konfiguration (Lucaj TechOps-Template)
```

---

## 3. Synthese: Zentrale Ergebnisse

### 3.1 D1-Ergebnis: Alle 14 Requirements sind gate-geeignet
Kein Requirement fällt in die Kategorie QUERSCHNITTLICH (D1=NEIN).
Jedes der 14 Deployer-Requirements hat:
- Prüfbare Deliverables (YAML: evidence_expected)
- Formulierbare Akzeptanzkriterien (YAML: acceptance_criteria)
- Handlungsrelevante Gate-Entscheidung (PASS/WARN/BLOCK)

**Implikation:** Die Referenzarchitektur benötigt 14 Quality Gates, keine
Querschnitt-Policies als Ersatz. (Einzelne Requirements wie R005 haben
ZUSÄTZLICH Q-Charakter, sind aber trotzdem als eigenes Gate prüfbar.)

### 3.2 D3-Ergebnis: 4 Requirements erfordern First-Degree Oversight
| D3=FIRST-DEGREE (4) | D3=SECOND-DEGREE (10) |
|---------------------|----------------------|
| R001 Risikomanagement | R002 Techn. Doku |
| R004 Human Oversight (pre) | R003 Robustheit/Safety |
| R008 Oversight-Wirksamkeit (ops) | R005 Evidence-Persistierung |
| R012 FRIA (Grundrechte) | R006 Eingabedaten-Qualität |
| | R007 Nutzertransparenz |
| | R009 Incident Reporting |
| | R010 Drift-Monitoring |
| | R011 CE/Konformität |
| | R013 Bias-Monitoring |
| | R014 Logging |

**Muster:** FIRST-DEGREE korreliert mit STRATEGISCHER governance_dimension
oder explizitem Art. 14-Bezug. Requirements mit rein technischer oder
regulatorisch-administrativer Natur sind SECOND-DEGREE.

### 3.3 D2-Ergebnis: 64% vollautomatisierbar
- **D2=VOLL:** 9 Requirements (R002,R003,R005,R006,R009,R010,R011,R013,R014)
- **D2=HYBRID:** 5 Requirements (R001,R004,R007,R008,R012)
- **D2=MANUELL:** 0 Requirements

**Validierung gegen Antiya (2020):** 64,3% VOLL automatisierbar vs.
Antiyas 75% für ISO 27001. Die niedrigere Quote ist PLAUSIBEL:
AI-Act-Requirements haben stärkere Oversight-Pflichten als ISO-Controls.
Die Differenz (75% vs. 64%) lässt sich durch D3-FIRST-DEGREE erklären.

### 3.4 D3×D2-Override: Sicherheitsnetz, kein akuter Eingriff
In diesem Durchlauf greift der Override NICHT aktiv ein:
Alle D3=FIRST-Requirements haben bereits D2=HYBRID (wegen qualitativer
Akzeptanzkriterien). Der Override wirkt als **SICHERHEITSNETZ**:
Er verhindert, dass zukünftige Instanziierungen die Gate-Checks auf
reine Existenzprüfungen (D2→VOLL) reduzieren.

**Beispiel:** Ohne Override könnte ein Deployer R001 (Risikomanagement)
als "Report exists? → PASS" implementieren. D3=FIRST verhindert das:
Die inhaltliche Bewertung MUSS menschlich erfolgen.

→ **DSR-Argument:** Der Override ist kein theoretisches Konstrukt,
sondern eine notwendige Design-Entscheidung gegen Automation Bias
(Laux & Ruschemeier, 2025).

### 3.5 Kernaussage für Kap. 5.2.2

> Die D_GATE_INCLUSION_RULE ergibt für die 14 EU-AI-Act-Deployer-Requirements
> eine **9:5-Verteilung** (AUTOMATISIERT:HYBRID). Die Automatisierungsgrenze
> wird NICHT durch technische Limitationen bestimmt (alle Requirements haben
> automatisierbare Aspekte), sondern durch die **Oversight-Pflicht (Art. 14)**:
> Wo der EU AI Act konstitutive menschliche Beteiligung fordert (D3=FIRST),
> DARF das Gate nicht vollautomatisiert werden — auch wenn es technisch
> möglich wäre (D2=VOLL). Der D3×D2-Override formalisiert diese regulatorische
> Grenze als architektonische Designregel.

---

## 4. D3×D2-Override-Analyse (Detail)

### 4.1 Wo der Override als Sicherheitsnetz wirkt

| R_xx | D3 | D2 (ohne Override) | D2 (mit Override) | Override aktiv? |
|------|----|--------------------|-------------------|----------------|
| R001 | FIRST | HYBRID | HYBRID | Nein (schon HYBRID) |
| R004 | FIRST | HYBRID | HYBRID | Nein (schon HYBRID) |
| R008 | FIRST | HYBRID | HYBRID | Nein (schon HYBRID) |
| R012 | FIRST | HYBRID | HYBRID | Nein (schon HYBRID) |

### 4.2 Kontrafaktische Analyse: Wann WÜRDE der Override greifen?

Szenario: Ein Deployer reduziert Akzeptanzkriterien auf reine Existenzprüfungen.

| R_xx | Reduziertes D2 | D3-Override | Konsequenz |
|------|---------------|-------------|------------|
| R001 | "Risk Report exists?" → D2=VOLL | D3=FIRST → max. HYBRID | **Override verhindert Automatisierung** |
| R004 | "Oversight Plan exists?" → D2=VOLL | D3=FIRST → max. HYBRID | **Override verhindert Automatisierung** |
| R008 | "Effectiveness Report exists?" → D2=VOLL | D3=FIRST → max. HYBRID | **Override verhindert Automatisierung** |
| R012 | "FRIA document exists?" → D2=VOLL | D3=FIRST → max. HYBRID | **Override verhindert Automatisierung** |

→ Der Override schützt vor "Compliance Theater": formale Existenzprüfungen
  ohne inhaltliche Bewertung.

---

## 5. Phasen-Verteilung der Gate-Typen

| Phase | AUTOMAT. | HYBRID | Total |
|-------|----------|--------|-------|
| **Pre-Deployment** | R011 (1) | R001, R004, R012 (3) | 4 |
| **Deployment** | R002, R003, R006, R014 (4) | R007 (1) | 5 |
| **Operation** | R005, R009, R010, R013 (4) | R008 (1) | 5 |
| **Gesamt** | **9** | **5** | **14** |

**Muster:** Pre-Deployment ist HYBRID-dominiert (3 von 4 = 75%).
Deployment und Operation sind AUTOMATISIERT-dominiert (80%).
→ Je näher am strategischen Entscheidungspunkt (Deploy?), desto mehr
menschliche Beteiligung nötig.

---

## 6. Zweiter Validierungsdurchlauf (Re-Validierung)

**Zweck:** Kritische Überprüfung aller 14 Bewertungen auf versteckte D3-Grenzfälle und übersehene D2-HYBRID-Aspekte.

### 6.1 Re-Validierung Ergebnis

| R_xx | Erstbewertung | Re-Validierung | Änderung? | Prüfpunkt |
|------|--------------|----------------|-----------|-----------|
| R001 | HYBRID | HYBRID | ✅ Keine | D3=FIRST unstrittig |
| R002 | AUTOMAT. | AUTOMAT. | ✅ Keine | ⚠️ Geprüft: Art. 11 "verständlich" → Gate prüft Template-Vollständigkeit, nicht Prosa-Qualität. D2=VOLL korrekt |
| R003 | AUTOMAT. | AUTOMAT. | ✅ Keine | Threshold = Paradebeispiel D2=VOLL |
| R004 | HYBRID | HYBRID | ✅ Keine | D3=FIRST unstrittig (Art. 14 direkt) |
| R005 | AUTOMAT. | AUTOMAT. | ✅ Keine | D1=JA bestätigt trotz Q-Charakter (D_VAL_R005_DUAL) |
| R006 | AUTOMAT. | AUTOMAT. | ✅ Keine | Schema-Validierung deterministisch |
| R007 | HYBRID | HYBRID | ✅ Keine | ⚠️ Geprüft: D3=SECOND bestätigt (D_R007_D3_SECOND). HYBRID aus D2, nicht D3 |
| R008 | HYBRID | HYBRID | ✅ Keine | D3=FIRST unstrittig (Sterz-Bedingungen) |
| R009 | AUTOMAT. | AUTOMAT. | ✅ Keine | ⚠️ Geprüft: Gate = Konfiguration vorhanden? Nicht: Ist Incident schwerwiegend? |
| R010 | AUTOMAT. | AUTOMAT. | ✅ Keine | Monitoring-Konfiguration deterministisch |
| R011 | AUTOMAT. | AUTOMAT. | ✅ Keine | Dokument-Existenz deterministisch |
| R012 | HYBRID | HYBRID | ✅ Keine | D3=FIRST unstrittig (Grundrechte) |
| R013 | AUTOMAT. | AUTOMAT. | ✅ Keine | ⚠️ Geprüft: Gate = Monitoring konfiguriert? Metrik-Definition → R001. Alert-Triage = separater Prozess |
| R014 | AUTOMAT. | AUTOMAT. | ✅ Keine | Logging-Konfiguration deterministisch |

### 6.2 Ergebnis der Re-Validierung

**0 Änderungen.** Die 9:5-Verteilung (AUTOMATISIERT:HYBRID) ist stabil.

4 Requirements wurden vertieft geprüft (R002, R009, R013, R007):
- **R002:** Art. 11 "Verständlichkeit" betrifft Doku-Qualität, nicht Gate-Check-Kriterium
- **R009:** Gate prüft Incident-Detection-KONFIGURATION, nicht Incident-BEWERTUNG
- **R013:** Gate prüft Monitoring-KONFIGURATION, nicht Metrik-DEFINITION oder Alert-TRIAGE
- **R007:** D3=SECOND bestätigt (Transparenz ≠ Counterfactual Influence)

### 6.3 Zusätzliche Erkenntnisse aus Re-Validierung

1. **Muster "Konfiguration vs. Inhalt":** Bei R002, R009, R013, R014 gilt:
   Das Gate prüft ob die INFRASTRUKTUR korrekt konfiguriert ist (deterministisch),
   NICHT ob die INHALTE angemessen sind (qualitativ). Diese Trennung ist der
   Schlüssel zur D2=VOLL-Klassifikation.

2. **Muster "Alert-Triage als separater Prozess":** R009 und R013 erzeugen
   im Betrieb Alerts, deren Bewertung menschliches Urteil erfordert.
   Aber: Diese Bewertung ist NICHT Teil des Gate-Checks, sondern ein
   nachgelagerter operativer Prozess. → Wichtig für Kap. 5.3 (Gate-Lifecycle).

3. **Korrektur D_GATE_COUNT:** 14 Gates bestätigt (nicht ~13).
   R004 = vollwertiges HYBRID GATE mit Deliverables und Akzeptanzkriterien.

---

## 7. Bekannte Limitationen

1. **Einzelbewerter-Bias:** Durchlauf durch eine Person (Demir + KI).
   Re-Validierung reduziert Bias, ersetzt aber nicht Expert Review (→ Kap. 6).
2. **Binäre D3-Klassifikation:** R007 (Transparenz) = dokumentierter Grenzfall.
   Entscheidung SECOND mit Begründung (D_R007_D3_SECOND).
3. **R005 Doppelcharakter:** Gate + Q-Infrastruktur (D_VAL_R005_DUAL).
4. **R013 SHOULD:** Gate-Default = WARN, Override→BLOCK bei High-Risk (D_R013_SHOULD_WARN).
5. **Konfiguration-vs-Inhalt-Trennung:** Designentscheidung, dass Gates
   Infrastruktur-Korrektheit prüfen, nicht Content-Qualität.
   Muss in Kap. 5.2.2 explizit begründet werden.
6. **D_GATE_INCLUSION_RULE Beispiel-Fehler:** Section 9: "R014" → R010 (D_EXAMPLE_FIX).

---

## 8. Entscheidungen aus diesem Durchlauf (→ Entscheidungsregister)

| ID | Entscheidung | Begründung |
|----|-------------|-----------|
| D_VAL_9_5 | 9:5 Verteilung AUTOMAT.:HYBRID (bestätigt in Re-Validierung) | 2× Durchlauf, 0 Änderungen |
| D_VAL_D1_ALL | Alle 14 = D1=JA | 14 eigenständige Gates, 0 Querschnitt |
| D_VAL_D3_PATTERN | D3=FIRST korreliert mit strategisch/Art.14 | 4 FIRST = R001, R004, R008, R012 |
| D_VAL_OVERRIDE_NET | Override = Sicherheitsnetz | Verhindert Reduktion auf Existenz-Checks |
| D_VAL_NO_MANUAL | 0 rein manuelle Gates | Jedes Requirement hat automatisierbare Aspekte |
| D_VAL_R005_DUAL | R005 = Gate + Q-Charakter | Dual-Klassifikation dokumentiert |
| D_VAL_PHASE_PATTERN | Pre-Depl.=75% HYBRID, Depl.+Ops=80% AUTO | Architektonisches Muster |
| D_R007_D3_SECOND | R007 = D3=SECOND beibehalten | Art. 13 ≠ Counterfactual Influence |
| D_GATE_COUNT_14 | 14 Gates (überschreibt ~13) | R004 = vollwertiges HYBRID GATE |
| D_R013_SHOULD_WARN | R013 SHOULD → WARN (Default) + BLOCK (High-Risk) | Risk-Scaling-Prinzip |
| D_EXAMPLE_FIX | Section 9: R014→R010 korrigieren | Verwechslung PMS/Logging |
| D_VAL_CONFIG_CONTENT | Muster: Gate prüft Konfiguration, nicht Inhalt | Schlüssel für D2=VOLL bei R002,R009,R013,R014 |
