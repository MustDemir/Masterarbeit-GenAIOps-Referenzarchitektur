# Gliederung v3 (aus Expose)

**Titel (FINAL C4, Stand 2026-02-27):**
Cloud-native Referenzarchitektur für GenAIOps mit Quality-Gate-Kontrollsystem zur lifecycle-integrierten Operationalisierung normativer Anforderungen – auf Basis des EU AI Act

Single Source of Truth: `/Users/mustafademir/Projects/genaiops-thesis/98_onedrive_migration/1_masterarbeit/1. Expose v3.docx`
Synchronisierte Repo-Kopie: `docs/expose/Expose_v3_single_source_2026-02-25.txt`
Stand: 2026-02-27

## 1 Einleitung
1.1 Problemstellung und Relevanz  
1.2 Zielsetzung der Arbeit  
1.3 Forschungsfragen  
1.4 Aufbau der Arbeit  
1.5 PoC-Scope (EVAL -> DEPLOY -> PROD) explizit erwaehnen

## 2 Theoretische Grundlagen und Stand der Forschung (Rigor Cycle)
2.1 Begriffsabgrenzung und Systemkontext (LLM, GenAI-System, RAG, LLMOps, Quality Gate, Policy-as-Code)  
2.2 Generative KI und LLMs  
2.3 Cloud-native: Fokus auf Plattformfaehigkeiten (Identity, Network, Observability, Policy)  
2.4 Operationalisierung  
2.4.1 Von MLOps zu LLMOps: Operationalisierung von KI-Systemen  
2.4.2 Der EU AI Act: Regulatorischer Rahmen und technisch-organisatorische Anforderungen  
2.5 Quality Gates: Definition, Konzepte und Einordnung  
2.6 Compliance-as-Code und Policy-as-Code  
2.7 Synthese: Forschungsluecke und Handlungsbedarf

## 3 Forschungsdesign und Methodik
3.1 Design Science Research als Forschungsrahmen  
3.2 Vorgehensmodell (DSRM nach Peffers)  
3.3 Artefaktdefinition, Scope und Abgrenzung, Instanziierungsstrategie  
3.4 Technische Konstruktionsmethoden  
3.4.1 Architekturentwurf (Cloud-native Patterns, IaC)  
3.4.2 Quality-Gate-Framework (Policy-as-Code, Gate-Template)  
3.4.3 Pipeline-Integration (CI/CD/CT, GitOps)  
3.4.4 Compliance-Operationalisierung (Regulatory-to-Technical Mapping)  
3.5 Anforderungserhebung und -analyse  
3.6 Traceability-Ansatz  
3.7 Evaluationsdesign (Kriterien + Methodenmix)  
3.8 Interviewdesign und Auswertung

## 4 Anforderungsanalyse (Relevance Cycle, beantwortet RQ1)
4.1 Ableitungslogik fuer testbare Anforderungen (MUSS/SOLL, Format R1-Rn, Evidenz, Lifecycle-Phase, Bezug EU AI Act)  
4.2 Technische Anforderungen  
4.3 Organisatorische Anforderungen  
4.4 Regulatorische Anforderungen  
4.5 Konsolidierter Anforderungskatalog

## 5 Entwicklung der Referenzarchitektur (Design Cycle, beantwortet RQ2)
5.1 Design-Prinzipien (DP-1..DP-n, begruendet aus R1-Rn)  
5.2 Architekturuebersicht: Schichtenmodell, Module, Schnittstellen, Verantwortlichkeiten  
5.3 Quality-Gate-Framework  
5.4 Gate-Template (Trigger, Evidence, Policy, Decision, Owner, Audit Trail, Waiver)  
5.4.1 Strategische Gates (Lifecycle Governance)  
5.4.2 Technische Gates (Qualitaet/Performance/Safety-Evals, Monitoring)  
5.4.3 Compliance Gates (EU AI Act -> Policy-as-Code + Evidence)  
5.4.4 Gate-Katalog (Uebersichtstabelle ueber alle Gates)  
5.5 Integration in CI/CD/CT-Pipelines (Policy Engine, Evidence Store, Automation Points)

## 6 Evaluation (beantwortet RQ3)
6.1 Evaluationskriterien (z. B. Coverage, Automatisierbarkeit, Auditierbarkeit, Praxistauglichkeit)  
6.2 Requirements-Coverage-Check  
6.3 Szenario-basierter Walkthrough: Ambient AI Scribe  
6.4 PoC-Scope EVAL -> DEPLOY -> PROD + Azure sichtbar  
6.4.1 Technisches Quality Gate  
6.4.2 Compliance Gate (Policy-as-Code)  
6.5 Experteninterviews: Durchfuehrung und Ergebnisse  
6.6 Synthese der Evaluationsergebnisse

## 7 Diskussion
7.1 Beantwortung der Forschungsfragen  
7.2 Wissenschaftlicher Beitrag und Einordnung  
7.2.1 Design Knowledge: uebertragbare Muster und Prinzipien (DSR-Beitrag)  
7.3 Implikationen fuer die Praxis  
7.4 Limitationen  
7.5 Weiterer Forschungsbedarf

## 8 Fazit und Ausblick
