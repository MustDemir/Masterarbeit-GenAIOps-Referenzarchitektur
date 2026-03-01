**Titel (FINAL C4, Stand 2026-02-27):** Cloud-native Referenzarchitektur fuer GenAIOps mit Quality-Gate-Kontrollsystem zur lifecycle-integrierten Operationalisierung normativer Anforderungen — auf Basis des EU AI Act
**Single Source of Truth:** `docs/expose/Expose_v4_final_2026-02-28.pdf` | **Stand:** 2026-02-28

### 1 Einleitung
* 1.1 Einleitung (PD1-PD3)
* 1.2 Problemdimensionen
* 1.3 Zielsetzung
* 1.4 Forschungsfragen (RQ1-RQ3, DSR-Cycle-Zuordnung)
* 1.5 Forschungsmethodik
* 1.6 Scope und Abgrenzung

### 2 Theoretische Grundlagen und Stand der Forschung (Rigor Cycle)
* 2.1 Begriffsabgrenzung und Systemkontext (LLM, GenAI-System, RAG, LLMOps, Quality Gate, Policy-as-Code)
* 2.2 Generative KI und LLMs
* 2.3 Cloud-native: Fokus auf Plattformfaehigkeiten (Identity, Network, Observability, Policy)
* 2.4 Operationalisierung
  * 2.4.1 Von MLOps zu LLMOps: Operationalisierung von KI-Systemen
  * 2.4.2 Der EU AI Act: Regulatorischer Rahmen und technisch-organisatorische Anforderungen
* 2.5 Quality Gates: Definition, Konzepte und Einordnung
* 2.6 Compliance-as-Code und Policy-as-Code
* 2.7 Synthese: Forschungsluecke und Handlungsbedarf

### 3 Forschungsdesign und Methodik (~90% abgeschlossen)
* 3.1 DSR als Forschungsrahmen
* 3.2 Methodischer Rahmen und Vorgehensmodell (Hevner 3 Zyklen, Peffers DSRM, vom Brocke DSR Grid)
* 3.3 Operationalisierung des DSR-Prozesses (Peffers-Mapping, Iterationslogik)
* 3.4 Artefaktdefinition, Scope und Abgrenzung (S1-S4, Instanziierungsstrategie)
* 3.5 Anforderungserhebung und -analyse
* 3.6 Traceability-Ansatz (RQ -> R -> DP -> Gate -> Evidence)
* 3.7 Evaluationsdesign (3-stufig, Kriterien pro Gate-Dimension)
* 3.8 Interviewdesign und Auswertung

### 4 Design-getriebene Operationalisierung regulatorischer Anforderungen (Design Cycle Phase 1, beantwortet RQ1)
* 4.1 Zielbild des Kontrollsystems (Enforcement vs. Dokumentation, Accountability-by-Design)
* 4.2 Lifecycle-Modell (3 Phasen: Pre-Deployment, Deployment, Operation)
* 4.3 Transformationsmethodik (Norm → funktionaler Kontrollmechanismus, kein juristischer Kommentar)
* 4.4 Kontrollmechanismen (EU AI Act Art. 9-15 → technisch pruefbare Controls, Lifecycle-verortet)
* 4.5 Konsolidierung (Governance-Dimensionen, NIST AI RMF Harmonisierung, Clustering)
* 4.6 Requirements-Katalog (R1-Rn, Lifecycle-Phase, Governance-Dimension, AI-Act-Ref, MUSS/SOLL)

### 5 Entwicklung der Referenzarchitektur (Design Cycle, beantwortet RQ2)
* 5.1 Ueberblick und Designprinzipien (DP1-DP5, Architekturuebersicht)
* 5.2 Architekturelle Struktur (Schichten- und Komponentenmodell, IaC-Integration) [S1]
* 5.3 Quality-Gate-Kontrollsystem [S2 USP]
  * 5.3.1 Gate-Taxonomie und Lifecycle-Zuordnung
  * 5.3.2 Gate-Spezifikation und Template (Trigger, Kriterien, Evidence, Decision, Owner, Audit Trail, Waiver)
  * 5.3.3 Compliance-Mapping (Art. 9-15 -> Policies -> Gates -> Evidence)
* 5.4 Pipeline-Integration [S3]
  * 5.4.1 CI/CD-Pipeline-Architektur (GitHub Actions, Stage-Gates)
  * 5.4.2 Policy-as-Code Integration (OPA/Rego, Policy-Bundles)
* 5.5 Evidence- und Audit-Logik [S4 USP]
  * 5.5.1 Evidence-Persistierung (Immutable Storage, Versionierung, Retention)
  * 5.5.2 Audit-Trail und Nachweiskette (R -> DP -> Gate -> Evidence)
* 5.6 Prototypische Instanziierung PoC (Azure-Stack, Healthcare-Szenario, 2. Iteration)

### 6 Evaluation (beantwortet RQ3)
* 6.1 Evaluationsrahmen und Kriterien
* 6.2 Requirements-Coverage-Matrix (R1-Rn -> Architekturkomponenten)
* 6.3 PoC-Walkthrough (Szenarien-basierte Demonstration, Evidenzgenerierung)
* 6.4 Expert-Reviews (Leitfadeninterviews n>=4, qualitative Auswertung)
* 6.5 Synthese und Bewertung (Triangulation)

### 7 Diskussion
* 7.1 Beantwortung der Forschungsfragen
* 7.2 Wissenschaftlicher Beitrag und Einordnung
  * 7.2.1 Design Knowledge: uebertragbare Muster und Prinzipien (DSR-Beitrag)
* 7.3 Implikationen fuer die Praxis
* 7.4 Limitationen
* 7.5 Weiterer Forschungsbedarf

### 8 Fazit und Ausblick
