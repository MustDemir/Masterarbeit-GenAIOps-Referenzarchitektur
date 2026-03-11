# Anhang A — Requirements-Katalog (Tabelle 1)

**Referenz:** Kap. 4.6 Requirements-Katalog
**Scope:** Deployer (Art. 26 VO (EU) 2024/1689), High-Risk GenAI (Art. 6 + Anhang III)
**Systematik:** 14 Requirements (R001–R014), 3 Lifecycle-Phasen, 3 Governance-Dimensionen

---

## Tabelle 1: Deployer-Requirements-Katalog für High-Risk-GenAI-Systeme

| R-ID | Kurztitel | Lifecycle-Phase | Gov.-Dimension | Art.-Referenz | Priorität | Kontrollmechanismus |
|------|-----------|-----------------|----------------|---------------|-----------|---------------------|
| R001 | Risikomanagement-Operationalisierung | Pre-Deployment | Regulatorisch | Art. 9 | MUST | Policy-as-Code: Prüfung auf dokumentiertes Risiko-Assessment |
| R002 | Technische Dokumentation & Auditierbarkeit | Deployment | Regulatorisch | Art. 11 | MUST | Gate-Prüfung auf vollständige technische Doku und Log-Referenzen |
| R003 | Robustheit, Genauigkeit & Sicherheitschecks | Deployment | Technisch | Art. 15 | MUST | Automatisierte Schwellenwertprüfung für Qualitäts- und Safety-Metriken |
| R004 | Human-Oversight-Design | Pre-Deployment | Strategisch | Art. 14 | MUST | Go/No-Go Gate mit dokumentierter Verantwortlichkeit und Eskalationsweg |
| R005 | Evidence-Persistierung & Audit Trails | Operation | Regulatorisch | Art. 12, Art. 15 | MUST | Nachweisprüfung auf unveränderliche Ablage und referenzierbare Audit-Trail-Einträge |
| R006 | Datenqualitätssicherung | Deployment | Technisch | Art. 10, Art. 26 Abs. 4 | MUST | Automatisierte Datenvalidierung mit Schema- und Plausibilitätschecks |
| R007 | Transparenz & Informationspflichten | Deployment | Regulatorisch | Art. 13, Art. 26 Abs. 7, Art. 50 | MUST | Gate-Prüfung auf Transparenzdokumentation und Nutzerkennzeichnung |
| R008 | Operative Oversight-Wirksamkeit | Operation | Strategisch | Art. 14, Art. 26 Abs. 2 | MUST | Continuous Monitoring der vier Effektivitätsbedingungen (Sterz et al., 2024) |
| R009 | Incident Reporting | Operation | Regulatorisch | Art. 26 Abs. 5, Art. 73 | MUST | Automatisierte Incident-Detection mit eskalationsbasiertem Meldeworkflow |
| R010 | Post-Market Surveillance & Drift-Monitoring | Operation | Technisch | Art. 72, Art. 9 Abs. 2 | MUST | Continuous Monitoring mit Drift-Detection und Schwellenwert-Alerting |
| R011 | Konformitätsbewertung | Pre-Deployment | Regulatorisch | Art. 26 Abs. 1, Art. 47, Art. 48 | MUST | Pre-Deployment Gate auf gültige Konformitätsdokumentation |
| R012 | Grundrechte-Folgenabschätzung (FRIA) | Pre-Deployment | Strategisch | Art. 27 | MUST | Pre-Deployment Gate auf abgeschlossene FRIA-Dokumentation |
| R013 | Bias- & Fairness-Monitoring | Operation | Technisch | Art. 9 Abs. 2 lit. a, Art. 10 Abs. 2 lit. f, Art. 15 | SHOULD | Continuous Monitoring mit Bias-Detection und periodischer Fairness-Evaluation |
| R014 | Automatisierte Protokollierung | Deployment | Technisch | Art. 12, Art. 26 Abs. 3 | MUST | Gate-Prüfung auf korrekte Logging-Konfiguration und Log-Auswertbarkeit |

---

## Verteilung nach Lifecycle-Phase

| Lifecycle-Phase | Anzahl | Requirements |
|-----------------|--------|-------------|
| Pre-Deployment | 4 | R001, R004, R011, R012 |
| Deployment | 5 | R002, R003, R006, R007, R014 |
| Operation | 5 | R005, R008, R009, R010, R013 |

## Verteilung nach Governance-Dimension

| Governance-Dimension | Anzahl | Requirements |
|----------------------|--------|-------------|
| Regulatorisch | 6 | R001, R002, R005, R007, R009, R011 |
| Technisch | 5 | R003, R006, R010, R013, R014 |
| Strategisch | 3 | R004, R008, R012 |

## Verteilung nach Priorität

| Priorität | Anzahl | Requirements |
|-----------|--------|-------------|
| MUST | 13 | R001–R012, R014 |
| SHOULD | 1 | R013 |

---

**Hinweis:** Die Zuordnung zu Lifecycle-Phasen markiert die Phase, in der das entsprechende Quality Gate primär greift. Einzelne Requirements (z. B. R001 Risikomanagement) sind per Definition lifecycle-übergreifend. Die Operationalisierung der Requirements in Gate-Spezifikationen (G-xx) erfolgt in Kapitel 5.
