# Kapitel 1 — Einleitung (DRAFT)

**Stand:** 2026-03-06
**Status:** Kap. 1.1 ✅ | Kap. 1.2 ✅ | Kap. 1.3 ✅ | Kap. 1.4 ✅ | Kap. 1.5 ✅ | Kap. 1.6 ✅
**Seitenbudget Kap. 1:** 5–7 Seiten (~1.500–2.100 Wörter)
**Wörter bisher:** ~2.075 (≈6,9 Seiten) — KAPITEL 1 KOMPLETT

---

## 1.1 Einleitung

Generative Künstliche Intelligenz (GenAI) bezeichnet Verfahren, die auf Basis von Trainingsdaten scheinbar neue, bedeutungstragende Inhalte wie Text, Bilder oder Audio erzeugen (Feuerriegel et al., 2024, S. 111). Die zunehmende Integration solcher Systeme in unternehmenskritische Domänen hat eine evolutionäre Entwicklung operativer Paradigmen ausgelöst: Von Machine Learning Operations (MLOps) über spezialisierte Large Language Model Operations (LLMOps) hin zu GenAIOps als übergeordnetem Operationsparadigma, das die spezifischen Komplexitäten generativer KI-Systeme adressiert (Joshi, 2025, S. 7–8; Tantithamthavorn et al., 2025, S. 27).

Mit dem EU AI Act (VO 2024/1689) hat die Europäische Union einen verbindlichen Rechtsrahmen geschaffen, der Hochrisiko-KI-Systeme umfassenden Anforderungen an Risikomanagement, Datenqualität, Transparenz und menschliche Aufsicht unterwirft (Art. 9–15 EU AI Act). Die gestaffelte Inkrafttretensstruktur der Verordnung erzeugt unmittelbaren Handlungsdruck: Ab August 2026 gelten die Hochrisiko- und Transparenzpflichten für KI-Systeme nach Annex III, ab August 2027 die vollständige Geltung für KI-Systeme in regulierten Produkten (Art. 113 VO 2024/1689). Der Sanktionsrahmen sieht Geldbußen von bis zu 35 Millionen Euro oder 7 Prozent des weltweiten Jahresumsatzes vor (Art. 99 Abs. 3 VO 2024/1689). Verschärft wird die Compliance-Herausforderung durch die strategische Abhängigkeit europäischer Organisationen von außereuropäischen Cloud- und KI-Infrastrukturanbietern, die eine eigenständige regulatorische Steuerung zusätzlich erschwert (Blancato, 2024, S. 12). Die Übersetzung dieser abstrakten regulatorischen Vorgaben in messbare technische Anforderungen stellt Organisationen jedoch vor erhebliche Herausforderungen (Guldimann et al., 2025, S. 1). Zwischen den hochrangigen rechtlichen Pflichten und den konkreten Verifikationsaktivitäten, die zur Nachweisführung in der Praxis erforderlich sind, besteht eine persistente Lücke (Buscemi et al., 2025, S. 1).

Obwohl MLOps als operatives Fundament bewährte Prinzipien zur Automatisierung und Operationalisierung von ML-Produkten bereitstellt (Kreuzberger et al., 2023, S. 31866), fehlen bislang integrierte Ansätze, die Qualitätssicherung, regulatorische Compliance und Lifecycle-Management für generative KI-Systeme in einer einheitlichen Architektur zusammenführen. Die Forschung zu Quality-Management-Systemen für KI, die über wissenschaftliche Prototypen hinausgehen und die Umsetzung des AI Act operativ unterstützen, steht noch am Anfang (Elia et al., 2025, S. 3). Insbesondere existiert nach aktuellem Kenntnisstand kein vergleichbarer Ansatz, der Quality Gates entlang des gesamten KI-Lebenszyklus mit normativ-technischer Durchsetzung verbindet (Elia et al., 2025, S. 3).

Die vorliegende Arbeit adressiert diese dreifache Lücke — Lifecycle-Komplexität, Qualitätssicherungsdefizit und Compliance-Gap — durch die designwissenschaftliche Entwicklung einer cloud-nativen Referenzarchitektur mit integriertem Quality-Gate-Kontrollsystem. Die nachfolgenden Abschnitte präzisieren die Problemdimensionen, leiten die Forschungsfragen ab und verorten die methodische Vorgehensweise.

---

## PRÜFPROTOKOLL Kap. 1.1

### Absatz 1 — Ausgangslage

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| Feuerriegel et al., 2024, S. 111 | `MG9RVJ7N` | "The term generative AI refers to computational techniques that are capable of generating seemingly new, meaningful content such as text, images, or audio from training data" | "Verfahren, die auf Basis von Trainingsdaten scheinbar neue, bedeutungstragende Inhalte wie Text, Bilder oder Audio erzeugen" | ✅ |
| Joshi, 2025, S. 7–8 | `6RRBZAUF` | GenAIOps als "overarching operational paradigm to address the specific complexities of generative AI systems in enterprise environments" (v1-verifiziert) | "GenAIOps als übergeordnetem Operationsparadigma, das die spezifischen Komplexitäten generativer KI-Systeme adressiert" | ✅ |
| Tantithamthavorn et al., 2025, S. 27 | `C755FHJK` | "THE RISE OF machine learning operations (MLOps) represents a pivotal moment in the operationalization of machine learning" | "evolutionäre Entwicklung operativer Paradigmen" | ✅ |

### Absatz 2 — Regulatorischer Trigger

| Zitation | Zotero-Key | BELEG | CLAIM | MATCH |
|---|---|---|---|---|
| EU AI Act VO 2024/1689, Art. 9–15 | Gesetzestext | Art. 9 Risikomanagement, Art. 10 Daten-Governance, Art. 13 Transparenz, Art. 14 Menschliche Aufsicht | "umfassenden Anforderungen an Risikomanagement, Datenqualität, Transparenz und menschliche Aufsicht" | ✅ |
| Guldimann et al., 2025, S. 1 | `QTQJ92VY` | "translating its broad regulatory requirements into measurable technical requirements" | "Übersetzung dieser abstrakten regulatorischen Vorgaben in messbare technische Anforderungen" | ✅ |
| Art. 113 VO 2024/1689 | Gesetzestext | Art. 113: gestaffelte Geltung — Aug 2026 Annex III + Transparenz, Aug 2027 Art. 6(1) regulierte Produkte | "Ab August 2026 gelten die Hochrisiko- und Transparenzpflichten für KI-Systeme nach Annex III, ab August 2027 die vollständige Geltung für KI-Systeme in regulierten Produkten" | ✅ |
| Art. 99 Abs. 3 VO 2024/1689 | Gesetzestext | Art. 99 Abs. 3: "administrative fines of up to 35 000 000 EUR or, if the offender is an undertaking, up to 7 % of its total worldwide annual turnover" | "Geldbußen von bis zu 35 Millionen Euro oder 7 Prozent des weltweiten Jahresumsatzes" | ✅ |
| Blancato, 2024, S. 12 | `2QUG2YAW` | "the EU is adopting a host of regulatory requirements and industrial policy tools [...] to counter the dominance of US vendors in the European cloud market" (Abstract) | "strategische Abhängigkeit europäischer Organisationen von außereuropäischen Cloud- und KI-Infrastrukturanbietern" | ✅ |
| Buscemi et al., 2025, S. 1 | `WXJEQWIH` | "a persistent gap remains between high-level legal requirements and the concrete verification activities needed to demonstrate compliance in practice" | "persistente Lücke" zwischen Pflichten und Verifikationsaktivitäten | ✅ |

### Absatz 3 — Forschungslücke

| Zitation | Zotero-Key | BELEG | CLAIM | MATCH |
|---|---|---|---|---|
| Kreuzberger et al., 2023, S. 31866 | `QY49ZYXB` | "it is highly challenging to automate and operationalize ML products [...] The paradigm of Machine Learning Operations (MLOps) addresses this issue" | "MLOps als operatives Fundament bewährte Prinzipien zur Automatisierung und Operationalisierung" | ✅ |
| Elia et al., 2025, S. 3 | `QRW95D4X` | "there is less research on designing and implementing a quality management system (QMS), [...] and no clear suggestion exists" | "Die Forschung zu QM-Systemen für KI [...] steht noch am Anfang" | ✅ |
| Elia et al., 2025, S. 3 | `QRW95D4X` | "To the best of our knowledge, no comparable approach to MQG4AI exists to date" | "existiert nach aktuellem Kenntnisstand kein vergleichbarer Ansatz" | ✅ |

### Absatz 4 — Transition

Keine Zitationen (Strukturabsatz). Terminologie konsistent mit Kap. 3/4.

---

## BILANZ Kap. 1.1

- **Wörter:** ~400 (≈1,3 Seiten)
- **Unique Quellen:** 7 + 3 Gesetzestexte (Art. 9–15, Art. 113, Art. 99)
- **Zitationen mit Seitenzahl:** 7/7 ✅ (Blancato S. 12 = Abstract/Intro)
- **Halluzinierte Quellen:** 0
- **Formale Überleitungen:** 0

---

## 1.2 Problemdimensionen

Die in Abschnitt 1.1 skizzierte dreifache Lücke lässt sich in drei interdependente Problemdimensionen differenzieren, die den Gestaltungsraum der vorliegenden Arbeit konstituieren.

**PD1: Fragmentierung bestehender Ansätze.** Die Operationalisierung von KI-Systemen wird durch eine Vielzahl konkurrierender methodischer Ansätze geprägt, denen es an konzeptioneller Integration mangelt. MLOps als grundlegendes Paradigma bleibt terminologisch unscharf — Kreuzberger et al. (2023, S. 31866) konstatieren, dass der Begriff weiterhin vage ist, obwohl die Automatisierung und Operationalisierung von ML-Produkten als zentrale Herausforderung anerkannt ist. Die Spezialisierung auf Large Language Models hat mit LLMOps zwar eine eigenständige Methodik hervorgebracht, doch ist dieser Begriff so rezent, dass die wissenschaftliche Literatur noch keine einheitliche Definition etabliert hat (Diaz-De-Arcaya et al., 2024, S. 1). Die evolutionäre Entwicklung von MLOps über LLMOps zu GenAIOps (Joshi, 2025, S. 7–8) dokumentiert einen Reifungsprozess, führt jedoch gleichzeitig zu einer Fragmentierung, bei der jede Ebene eigene Werkzeuge, Metriken und Prozesse definiert, ohne dass ein übergreifendes Integrationsmodell existiert.

**PD2: Inadäquanz konventioneller QA-Mechanismen für generative KI.** Konventionelle Qualitätssicherungsmechanismen adressieren primär algorithmische Metriken, vernachlässigen jedoch systemische Qualitätsdimensionen generativer KI-Systeme. Produktive ML-Systeme leiden unter einem persistenten blinden Fleck: Datenqualitätsdrift und inkonsistente Validierung, wobei die Mehrzahl produktiver Vorfälle nicht aus algorithmischen Fehlern, sondern aus Datenproblemen resultiert (Nellutla, 2025, S. 1). Auch auf normativer Ebene bleiben die Prinzipien vertrauenswürdiger KI häufig abstrakt und entbehren konkreter operativer Mandate (Billeter et al., 2024, S. 1). Die Forschung zu Qualitätsmanagementsystemen, die über wissenschaftliche Prototypen hinausgehen, steht noch am Anfang — nach aktuellem Kenntnisstand existiert kein vergleichbarer Ansatz, der Quality Gates systematisch entlang des gesamten KI-Lebenszyklus mit normativ-technischer Durchsetzung verbindet (Elia et al., 2025, S. 3).

**PD3: Operationalisierungslücke zwischen regulatorischen Anforderungen und technischer Umsetzung.** Der EU AI Act (VO 2024/1689) differenziert die Compliance-Pflichten entlang einer Wertschöpfungskette mit getrennten Rollen: Der Provider trägt die primäre Konformitätslast (Art. 16, 43), während der Deployer im laufenden Betrieb den bestimmungsgemäßen Einsatz, die menschliche Aufsicht (Art. 14), die Input-Datenrelevanz (Art. 26 Abs. 4) und die Vorfallmeldung (Art. 72) sicherstellen muss. Im Kontext generativer KI-Systeme erzeugt diese Rollenverteilung eine strukturelle Asymmetrie: Ein Deployer, der ein General-Purpose AI Model (GPAI, Art. 51 ff.) über eine API bezieht und in eine domänenspezifische Anwendung integriert, verfügt typischerweise über keinen Zugang zu Modellgewichten, Trainingsdaten oder interner Architektur — gleichwohl muss er nachweisen, dass sein Gesamtsystem die Anforderungen an Risikomanagement (Art. 9), Datenqualität (Art. 10), Transparenz (Art. 13) und menschliche Aufsicht (Art. 14) erfüllt. Novelli et al. (2024, S. 10) bestätigen diese Dynamik: Die einschlägigen Haftungsrichtlinien verlagern die Beweislast auf Provider und Deployer, wobei Letztere relevante und verhältnismäßige Evidenz vorlegen müssen (Novelli et al., 2024, S. 14). Die Übersetzung dieser abstrakt formulierten Anforderungen in messbare technische Anforderungen erweist sich als substanzielle Herausforderung (Guldimann et al., 2025, S. 1), und zwischen den hochrangigen rechtlichen Pflichten und den konkreten Verifikationsaktivitäten persistiert eine strukturelle Lücke (Buscemi et al., 2025, S. 1). Diese Asymmetrie verschärft sich durch Art. 25: Nimmt der Deployer wesentliche Änderungen am System vor — etwa durch Fine-Tuning oder RAG-Integration, die den bestimmungsgemäßen Zweck verändert —, steigt er rechtlich zum Provider auf und übernimmt die vollständige Konformitätslast, ohne notwendigerweise über die dafür erforderlichen Einblicke in das Basismodell zu verfügen.

Die drei Problemdimensionen sind nicht isoliert, sondern interdependent: Die Fragmentierung operativer Ansätze (PD1) erschwert die Etablierung einheitlicher Qualitätssicherungsmechanismen (PD2), während das Fehlen adäquater QA-Instrumente die systematische Operationalisierung regulatorischer Anforderungen (PD3) verhindert. In ihrer Gesamtheit konstituieren sie ein Gestaltungsproblem, das einen integrativen, architekturbasierten Lösungsansatz erfordert.

---

## PRÜFPROTOKOLL Kap. 1.2

### PD1 — Fragmentierung

| # | Zitation | Zotero-Key | BELEG (exakter Satz) | CLAIM (Paraphrase) | MATCH |
|---|---|---|---|---|---|
| 1 | Kreuzberger et al. (2023, S. 31866) | `QY49ZYXB` | "MLOps is still a vague term" + "it is highly challenging to automate and operationalize ML products" | MLOps bleibt terminologisch unscharf | ✅ |
| 2 | Diaz-De-Arcaya et al. (2024, S. 1) | `T86QTBHU` | "This term is so recent that the scientific literature has not yet agreed on a common definition for it" | LLMOps ohne einheitliche Definition | ✅ |
| 3 | Joshi (2025, S. 7–8) | `6RRBZAUF` | "This paper shows how the evolution happened from operational methodologies in AI, from traditional Machine Learning Operations (MLOps) to finally specialized Large Language Model Operations (LLMOps) and then to Generative AI Operations (GenAIOps)" | Evolution MLOps→LLMOps→GenAIOps | ✅ |

### PD2 — Inadäquanz konventioneller QA

| # | Zitation | Zotero-Key | BELEG (exakter Satz) | CLAIM (Paraphrase) | MATCH |
|---|---|---|---|---|---|
| 1 | Nellutla (2025, S. 1) | `Q62UTCMW` | "production ML systems continue to suffer from a persistent blind spot: data quality drift and inconsistent validation" + "most ML production incidents stem not from algorithmic errors but from data issues" | Datenqualität als Hauptproblemquelle | ✅ |
| 2 | Billeter et al. (2024, S. 1) | `HEA5ZAKT` | "Despite their crucial role, these principles often remain abstract, lacking concrete operational mandates" | TAI-Prinzipien ohne operative Mandate | ✅ |
| 3 | Elia et al. (2025, S. 3) | `QRW95D4X` | "there is less research on designing and implementing a quality management system (QMS), [...] and no clear suggestion exists" + "To the best of our knowledge, no comparable approach to MQG4AI exists to date" | Forschungslücke bei QMS für KI | ✅ |

### PD3 — Operationalisierungslücke + Beweislast-Asymmetrie

| # | Zitation | Zotero-Key | BELEG (exakter Satz) | CLAIM (Paraphrase) | MATCH |
|---|---|---|---|---|---|
| 1 | EU AI Act VO 2024/1689, Art. 16, 26, 43 | Gesetzestext | Art. 16 Provider-Pflichten, Art. 26 Deployer-Pflichten, Art. 43 Konformitätsbewertung | Getrennte Compliance-Rollen | ✅ |
| 2 | Novelli et al. (2024, S. 10) | `YV4BV8CY` | "shifting the burden of proof to providers or deployers (AILD Articles 3 and 4; PLD Articles 8 and 9)" | Beweislast auf Deployer verlagert | ✅ |
| 3 | Novelli et al. (2024, S. 14) | `YV4BV8CY` | "the deployers and designers of a Generative AI model — must provide evidence that is both relevant and proportionate" | Deployer muss relevante Evidenz vorlegen | ✅ |
| 4 | Guldimann et al. (2025, S. 1) | `QTQJ92VY` | "translating its broad regulatory requirements into measurable technical requirements" | Übersetzung reg. → techn. Anforderungen | ✅ |
| 5 | Buscemi et al. (2025, S. 1) | `WXJEQWIH` | "a persistent gap remains between high-level legal requirements and the concrete verification activities needed to demonstrate compliance in practice" | Persistente Lücke Recht ↔ Praxis | ✅ |
| 6 | EU AI Act VO 2024/1689, Art. 25 | Gesetzestext | Art. 25: wesentliche Änderungen → Provider-Status | Deployer→Provider-Eskalation | ✅ |

## BILANZ Kap. 1.2

- **Wörter:** ~530 (≈1,8 Seiten)
- **Unique Quellen:** 9 + 2 Gesetzestextreferenzen
- **Zitationen mit Seitenzahl:** 7/7 ✅ (+ 2× Artikelverweise)
- **Halluzinierte Quellen:** 0
- **PD-Bezeichnungen SOT-konform:** ✅ (aus Kap. 3)
- **Beweislast-Asymmetrie gestützt durch:** Novelli (2024, S. 10, 14)
- **MQG4AI-Negativbeweis:** Verifiziert an Elia (2025, S. 1–5) — kein CI/CD, kein Evidence Store, kein Enforcement

## 1.3 Zielsetzung

Die vorliegende Arbeit verfolgt das Ziel, eine cloud-native Referenzarchitektur für GenAIOps zu entwickeln, die regulatorische, technische und strategische Anforderungen durch ein lifecycle-integriertes Quality-Gate-Kontrollsystem systematisch operationalisiert. Den methodischen Rahmen bildet Design Science Research (DSR) nach Hevner et al. (2004, S. 77) und Peffers et al. (2007, S. 54): Das angestrebte Artefakt umfasst ein Model (Referenzarchitektur), eine Method (Quality-Gate-Systematik mit Traceability-Logik) sowie eine Instantiation (Proof-of-Concept-Implementierung). Verantwortungsnachweisbarkeit wird dabei nicht als nachgelagerter Dokumentationsprozess, sondern als technisch erzwungene Systemeigenschaft konzipiert — Accountability-by-Design.

Die Architektur gliedert sich in vier Subsysteme: die architekturelle Grundstruktur (S1), ein formalisiertes Quality-Gate-Kontrollsystem (S2), die Pipeline-Integration in CI/CD/CT-Workflows (S3) sowie eine Evidence- und Audit-Logik (S4). Die Subsysteme S2 und S4 bilden den zentralen Forschungsbeitrag, indem sie Quality Gates entlang dreier Governance-Dimensionen — strategisch, technisch und regulatorisch — spezifizieren und eine dreistufige Transformation von normativen Anforderungen über formalisierte Requirements zu prüfbaren Gate-Kriterien vollziehen. Im Unterschied zu bestehenden Ansätzen wie Model Quality Gates for Artificial Intelligence (MQG4AI; Elia et al., 2025, S. 3), die eine Provider-Perspektive einnehmen und ohne automatisierte Durchsetzungsmechanismen operieren, verankert die vorliegende Architektur Compliance als Policy-as-Code mit maschinell auswertbarem Evidence Store.

Die Referenzarchitektur wird in einem Proof of Concept auf Microsoft Azure instanziiert, der ein Healthcare-Szenario (Ambient AI Scribe) als Hochrisiko-Anwendungsfall abbildet. Die Evaluation folgt einem dreistufigen Vorgehen (vgl. Kapitel 6).

Der angestrebte Beitrag ist zweifach: Auf wissenschaftlicher Ebene liefert die Arbeit übertragbares Design Knowledge in Form von Gestaltungsprinzipien und Architekturmustern für die Governance generativer KI-Systeme, mit Anschluss an internationale Rahmenwerke wie NIST AI RMF und ISO 42001. Auf praktischer Ebene stellt sie Deployer-Organisationen im Sinne des Art. 26 EU AI Act unmittelbar einsetzbare Gate-Templates und Compliance-Mechanismen bereit. Die nachfolgenden Forschungsfragen operationalisieren diese Zielsetzung.

---

## PRÜFPROTOKOLL Kap. 1.3

### Absatz 1 — Zielformulierung

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| Hevner et al. (2004, S. 77) | `YUERCAVB` | "The artifacts are constructs, models, methods, and instantiations. Purposeful artifacts are built to address heretofore unsolved problems." | "Das angestrebte Artefakt umfasst ein Model (Referenzarchitektur), eine Method (Quality-Gate-Systematik mit Traceability-Logik) sowie eine Instantiation" | ✅ Korrekte Zuordnung zu March/Smith-Taxonomie |
| Peffers et al. (2007, S. 54) | `Y24UGDM7` | "The DS process includes six steps: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication." | DSR als methodischer Rahmen benannt | ✅ DSRM-Prozess als Referenz |

### Absatz 2 — Artefaktskizze + USP

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| Elia et al. (2025, S. 3) | `QRW95D4X` | "To the best of our knowledge, no comparable approach to MQG4AI exists to date" + MQG4AI fokussiert auf XAI/Medizin, Provider-Perspektive | "Im Unterschied zu bestehenden Ansätzen wie MQG4AI [...], die eine Provider-Perspektive einnehmen und ohne automatisierte Durchsetzungsmechanismen operieren" | ✅ Abgrenzung (NICHT identischer Claim wie 1.2) |

### Absatz 3 — Instanziierung + Evaluation

Keine externen Zitationen (Eigenaussagen zur Methodik). Terminologie konsistent mit Kap. 3.7 (Evaluation) und Kap. 5.6 (PoC). Forward-Refs: Kap. 3.7 ✅ geplant | Kap. 5.6 ✅ geplant | Kap. 6.3–6.4 ✅ geplant.

### Absatz 4 — Beitrag + Anschluss

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| EU AI Act VO 2024/1689, Art. 26 | Gesetzestext | Art. 26: Pflichten der Deployer | "Deployer-Organisationen im Sinne des Art. 26 EU AI Act" | ✅ |

Verweis auf NIST AI RMF und ISO 42001 = Rahmenwerke (keine seitenspezifische Zitation nötig in Zielsetzung, Detail in Kap. 5.1).

---

## BILANZ Kap. 1.3

- **Wörter:** ~300 (≈1 Seite)
- **Unique Quellen:** 3 + 1 Gesetzestext + 2 Rahmenwerk-Verweise
- **Zitationen mit Seitenzahl:** 3/3 ✅ (Hevner S. 77, Peffers S. 54, Elia S. 3)
- **Halluzinierte Quellen:** 0
- **Elia-Doppelzitation:** ✅ Vermieden — Abgrenzungsclaim (Provider + kein Enforcement), NICHT identisch mit 1.2 (Forschungslücke)
- **Negativ-Checklist:** ✅ Keine DP1–DP5, keine Gate-Felder, keine Azure-Details, keine R-01 ff., keine formale Überleitung
- **Argumentationsstruktur:** Problem→Ziel→Artefakt→Beweis→Impact→Brücke zu 1.4 ✅

## 1.4 Forschungsfragen

Aus der identifizierten Forschungslücke und der formulierten Zielsetzung werden drei Forschungsfragen abgeleitet, die den drei Zyklen des Information Systems Research Framework nach Hevner et al. (2004, S. 80) zugeordnet sind. RQ1 adressiert den Relevance Cycle: Welche regulatorischen, technischen und strategischen Anforderungen sind für eine verantwortungsnachweisbare Gestaltung von GenAI-Systemen im Enterprise-Kontext relevant und operationalisierbar? RQ2 adressiert den Design Cycle: Wie kann eine Referenzarchitektur für GenAIOps gestaltet werden, die die erhobenen Anforderungen durch ein lifecycle-integriertes Quality-Gate-Kontrollsystem systematisch operationalisiert? RQ3 adressiert den Rigor Cycle: Inwiefern ist die entwickelte Referenzarchitektur geeignet, regulatorische Anforderungen technisch durchzusetzen und auditierbar nachweisbar zu machen?

Die drei Forschungsfragen spannen einen durchgängigen Designprozess auf: RQ1 erhebt die Anforderungsbasis (Kapitel 4), RQ2 überführt diese in das architektonische Artefakt (Kapitel 5) und RQ3 evaluiert dessen Eignung durch eine dreistufige Bewertung (Kapitel 6). Die Zuordnung zu den DSR-Zyklen stellt sicher, dass Problemrelevanz, Artefaktkonstruktion und wissenschaftliche Fundierung systematisch adressiert werden.

---

## PRÜFPROTOKOLL Kap. 1.4

### Absatz 1 — RQ-Formulierung + Cycle-Zuordnung

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| Hevner et al. (2004, S. 80) | `YUERCAVB` | Figure 2: "Information Systems Research Framework" — Environment (Relevance) ↔ IS Research ↔ Knowledge Base (Rigor); "Applicable Knowledge / Application in the Appropriate Environment / Relevance / Rigor / Additions to the Knowledge Base" | "drei Zyklen des Information Systems Research Framework nach Hevner et al. (2004, S. 80)" — Relevance/Design/Rigor-Zuordnung | ✅ Framework korrekt zugeordnet |

RQ-Formulierungen = Eigenformulierungen (keine Zitation nötig), konsistent mit Exposé v4 S. 6 ✅

### Absatz 2 — Kapitel-Mapping + DSR-Logik

Keine externen Zitationen (Strukturabsatz). Terminologie konsistent mit:
- Kap. 3 DOCX Tabelle 2 (DSRM-Mapping): RQ1→Kap. 4, RQ2→Kap. 5, RQ3→Kap. 6 ✅
- gliederung_v3.md: "4 Anforderungsanalyse (RQ1)" / "5 Referenzarchitektur (RQ2)" / "6 Evaluation (RQ3)" ✅
- Forward-Refs: Kap. 4 ✅ existiert | Kap. 5 ✅ existiert | Kap. 6 ✅ geplant

---

## BILANZ Kap. 1.4

- **Wörter:** ~150 (≈0,5 Seiten)
- **Unique Quellen:** 1 (Hevner 2004)
- **Zitationen mit Seitenzahl:** 1/1 ✅ (Hevner S. 80)
- **Halluzinierte Quellen:** 0
- **RQ-Formulierungen:** Identisch mit Exposé v4 S. 6 ✅
- **DSR-Cycle-Zuordnung:** Konsistent mit Kap. 3 DOCX Tabelle 2 ✅
- **Negativ-Checklist:** ✅ Keine Evaluationsdetails (→ Kap. 6), keine Methodenbeschreibung (→ 1.5), keine PD-Wiederholung
- **Argumentationsstruktur:** Forschungslücke→RQs→Cycle-Zuordnung→Kapitel-Mapping→Brücke zu 1.5 ✅

## 1.5 Forschungsmethodik

Die in Abschnitt 1.3 eingeführte designwissenschaftliche Ausrichtung wird durch die Kombination dreier komplementärer Rahmenwerke operationalisiert. Das Information Systems Research Framework nach Hevner et al. (2004, S. 80) bildet die Meta-Ebene und strukturiert die Arbeit über die drei Zyklen Relevance, Design und Rigor. Die Design Science Research Methodology (DSRM) nach Peffers et al. (2007, S. 54) liefert die Prozessebene durch ein sechsstufiges Vorgehensmodell — Problem Identification, Objectives, Design & Development, Demonstration, Evaluation und Communication —, das problem-centered durchlaufen wird. Das DSR Grid nach vom Brocke und Maedche (2019, S. 380) ergänzt die Planungsebene als Strukturierungswerkzeug und operationalisiert die Forschungsplanung entlang von sechs Dimensionen, die sich aus der Kreuzung dreier Bereiche — Problem, Solution und Evaluation — mit den Perspektiven Relevance und Rigor ergeben. Die drei Ebenen wirken komplementär: Hevner et al. definieren die normativen Qualitätsanforderungen an designwissenschaftliche Forschung, Peffers et al. strukturieren den Forschungsprozess in operationalisierbare Schritte, und das DSR Grid sichert die systematische Abdeckung aller relevanten Forschungsdimensionen. Erst die Kombination der drei Rahmenwerke gewährleistet, dass sowohl die Forschungsqualität als auch die Prozesslogik und die inhaltliche Vollständigkeit methodisch kontrolliert werden. Die sechs DSRM-Schritte werden auf die Kapitelstruktur der Arbeit abgebildet: Die Problemidentifikation fundiert die vorliegende Einleitung sowie die Verortung des Forschungsrahmens (Kapitel 1 und 3.1), die Definition der Lösungsziele erfolgt im methodischen Rahmen (Kapitel 3.2–3.3). Design & Development erstreckt sich über die normative Operationalisierung regulatorischer Anforderungen (Kapitel 4) und die Entwicklung der Referenzarchitektur (Kapitel 5). Die prototypische Instanziierung als Azure-basierter Proof of Concept dient der Demonstration (Kapitel 5.6), die dreistufige Evaluation — bestehend aus Requirements-Coverage, PoC-Walkthrough und Expert-Reviews — bildet Kapitel 6. Die Communication erfolgt in Diskussion und Fazit (Kapitel 7 und 8). Die Arbeit durchläuft dabei zwei Iterationen: Iteration 1 entwickelt das konzeptuelle Architekturmodell und die Quality-Gate-Systematik, Iteration 2 instanziiert die Architektur als Proof of Concept und verfeinert das Modell reflektiv. Die vollständige methodische Ausarbeitung einschließlich der detaillierten Operationalisierung dieses Mappings erfolgt in Kapitel 3.

---

## PRÜFPROTOKOLL Kap. 1.5

### Absatz 1 — Methodische Verortung + 3 Rahmenwerke + Integration + DSRM-Kapitel-Mapping + Iterationen

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| Hevner et al. (2004, S. 80) | `YUERCAVB` | Figure 2: "Information Systems Research Framework" — Environment (Relevance) ↔ IS Research ↔ Knowledge Base (Rigor) | "Meta-Ebene [...] drei Zyklen Relevance, Design und Rigor" | ✅ |
| Peffers et al. (2007, S. 54) | `Y24UGDM7` | "The DS process includes six steps: problem identification and motivation, definition of the objectives for a solution, design and development, demonstration, evaluation, and communication." (S. 54) + "We identified four possible research entry points [...] a **problem-centered** approach" (S. 56) | "sechsstufiges Vorgehensmodell [...] das problem-centered durchlaufen wird" | ✅ Schritte korrekt + Entry Point belegt |
| vom Brocke & Maedche (2019, S. 380) | `E3XS3V6X` | Paper S. 379–380: 6 Dimensionen als Grid; Kap. 3 DOCX (SOT) interpretiert als "Kreuzung von drei Bereichen (Problem, Lösung, Evaluation) mit zwei Perspektiven (Relevanz, Rigor)" (vom Brocke & Maedche, 2019, S. 380) | "Strukturierungswerkzeug [...] sechs Dimensionen [...] Kreuzung dreier Bereiche [...] mit den Perspektiven Relevance und Rigor" | ✅ Konsistent mit Kap. 3 DOCX SOT + Exposé S. 7 |

**Neue Claims (Integrationssätze):**

| CLAIM | Typ | Beleg |
|---|---|---|
| "Hevner et al. definieren die normativen Qualitätsanforderungen" | Paraphrase | ✅ Hevner (2004, S. 80): Guidelines G1–G7 = normative Anforderungen |
| "Peffers et al. strukturieren den Forschungsprozess in operationalisierbare Schritte" | Paraphrase | ✅ Peffers (2007, S. 54): 6 sequentielle Schritte = Prozessstruktur |
| "DSR Grid sichert die systematische Abdeckung aller relevanten Forschungsdimensionen" | Paraphrase | ✅ Exposé S. 7: "sichert die systematische Abdeckung"; vom Brocke (2019, S. 380): Grid-Logik |
| "Kombination [...] gewährleistet [...] Forschungsqualität [...] Prozesslogik [...] inhaltliche Vollständigkeit" | Eigenaussage (Synthese) | ✅ Logische Folge aus 3 Ebenen — kein Einzelbeleg nötig, da Synthese der drei Quellen |

**Neue Claims (DSRM-Kapitel-Mapping):**

| CLAIM (im Text) | Beleg (Kap. 3 DOCX Tabelle 2) | MATCH |
|---|---|---|
| "Problemidentifikation [...] Kapitel 1 und 3.1" | Tabelle 2: "1 Problem ID → 1 + 3.1" | ✅ |
| "Definition der Lösungsziele [...] Kapitel 3.2–3.3" | Tabelle 2: "2 Objectives → 3.2 + 3.3" | ✅ |
| "Design & Development [...] Kapitel 4 [...] Kapitel 5" | Tabelle 2: "3 Design & Dev. → 4, 5" | ✅ |
| "Demonstration (Kapitel 5.6)" | Tabelle 2: "4 Demonstration → 5.x" | ✅ |
| "dreistufige Evaluation [...] Kapitel 6" | Tabelle 2: "5 Evaluation → 6" + Gliederung: 6.2 Coverage, 6.3 Walkthrough, 6.4 Expert-Reviews | ✅ |
| "Communication [...] Kapitel 7 und 8" | Tabelle 2: "6 Communication → 7, 8" | ✅ |

Iterationslogik (Iter. 1/Iter. 2) = Eigenaussage, konsistent mit:
- Exposé v4 S. 7: "Die Arbeit durchläuft zwei Iterationen: Iteration 1 [...] konzeptuelles Modell + Gate-Systematik, Iteration 2 [...] Azure-PoC + reflektive Verfeinerung" ✅
- Kap. 3 DOCX G6: "Zwei Iterationen: Iter. 1 Konzept → Iter. 2 PoC + Refinement" ✅
- Forward-Ref Kap. 3: ✅ existiert (03_forschungsdesign_methodik/)

---

## BILANZ Kap. 1.5

- **Wörter:** ~280 (≈0,9 Seiten)
- **Unique Quellen:** 3 (Hevner 2004, Peffers 2007, vom Brocke & Maedche 2019)
- **Zitationen mit Seitenzahl:** 3/3 ✅
- **Halluzinierte Quellen:** 0
- **Neue Quelle:** vom Brocke & Maedche (2019, S. 380) ✅ Erstmalig in Kap. 1
- **Negativ-Checklist:** ✅ Keine Artefakttypen (→1.3), keine 7 Guidelines im Detail (→3.1), keine DSRM-6-Schritte im Detail (→3.2.2), keine DSR-Grid-Dimensionen im Detail (→3.2.3), keine formale Überleitung (Uni-Leitfaden: "Formales Vorgehen NICHT explizit beschreiben")
- **Neu ggü. v1:** +problem-centered, +Strukturierungswerkzeug, +2 Integrationssätze, +DSRM-Kapitel-Mapping (6 Schritte → Kapitelstruktur, konsistent mit Kap. 3 Tabelle 2), alle Exposé-Deltas geschlossen
- **Argumentationsstruktur:** Rückverweis 1.3→3 Rahmenwerke (Meta/Prozess/Planung)→Integration (Wozu zusammen?)→DSRM-Kapitel-Mapping→Iterationen→Forward-Ref Kap. 3 ✅
- **Uni-Konformität:** Kein separates "Aufbau der Arbeit"-Kapitel; stattdessen inhaltlich begründetes DSRM-Mapping (SRH-Leitfaden: "Lieber auf inhaltlicher Ebene beschreiben und begründen") ✅

## 1.6 Scope und Abgrenzung

Die Arbeit nimmt ausschließlich die Perspektive des Deployers im Sinne des Art. 26 EU AI Act (VO 2024/1689) ein. Provider-Pflichten nach Art. 16 liegen explizit außerhalb des Scope; die Eskalation zur Provider-Rolle nach Art. 25 markiert die Scope-Grenze der vorliegenden Untersuchung. Der architekturelle Fokus liegt auf dem Deployment- und Inference-Zyklus — von der Bereitstellung eines fertig trainierten Modells bis zur überwachten Produktionsfreigabe. Nicht adressiert werden LLM-Training, Fine-Tuning, eigenständige Modellentwicklung sowie Data-Engineering-Pipelines; die Retirement-Phase fällt als Provider-Verantwortung (Art. 16 Abs. 1 lit. j) ebenfalls nicht in den Scope. Aus der Deployer-Perspektive ergibt sich eine differenzierte Behandlung von Art. 10, der die Daten-Governance für Hochrisiko-Systeme regelt. Art. 10 Abs. 1–5 adressiert die Governance von Trainings-, Validierungs- und Testdatensätzen und setzt damit voraus, dass der Akteur die Daten kontrolliert, mit denen das KI-System entwickelt wird; Art. 10 Abs. 6 schränkt ein, dass bei Systemen ohne Modelltraining lediglich die Anforderungen an Testdatensätze gelten. Für Deployer, die proprietäre Foundation Models über API-Schnittstellen beziehen und weder Zugang zu Trainingsdaten noch die Möglichkeit eines Modelltrainings besitzen, sind die Abs. 1–5 folglich nicht anwendbar — die Data-Governance-Maßnahmen des Art. 10 sind primär auf Anbieter von GPAI-Modellen zugeschnitten (Novelli et al., 2024, S. 9). Art. 10 Abs. 2 lit. b–e setzt die Kenntnis über Erhebungsprozesse, Vorverarbeitungsvorgänge und Datenannotation voraus — Informationen, über die ein API-basierter Deployer bei proprietären Foundation Models strukturell nicht verfügt; die Nichtanwendbarkeit ergibt sich somit nicht aus einer freiwilligen Scope-Wahl, sondern aus einer technischen Unmöglichkeit. Lediglich Art. 10 Abs. 6 (Testdaten) bleibt als Deployer-relevante Anforderung adressierbar. Ein für generative KI-Systeme relevanter Sonderfall betrifft Retrieval-Augmented-Generation-Architekturen (RAG): Die dabei zur Inferenzzeit dynamisch abgerufenen Kontextdaten verändern das Modell nicht, sondern gehen als Eingabedaten im Sinne des Art. 3 Nr. 33 in den Prompt ein. Sie fallen daher nicht unter den Trainingsdatenbegriff des Art. 10, sondern unter die Transparenz- und Robustheitspflichten der Art. 13 und 15 sowie die Pflicht des Deployers zur Sicherstellung der Eingabedatenrelevanz nach Art. 26 Abs. 4; Buscemi et al. (2025, S. 7–8) ordnen die resultierenden Prüfpflichten entsprechend dem Transparenz-Requirement zu. Da der EU AI Act RAG-Architekturen nicht explizit adressiert, stellt diese Zuordnung eine normativ begründete Interpretation dar, die als methodische Limitation in Abschnitt 4.1 und Kapitel 7 diskutiert wird. Ethische Fragestellungen werden nur insoweit berücksichtigt, als sie sich in technisch operationalisierbare Anforderungen übersetzen lassen; die rechtliche Analyse beschränkt sich auf die für Hochrisiko-Systeme relevanten Art. 9–15 aus Deployer-Perspektive und erhebt keinen Anspruch auf juristische Vollständigkeit. Die Referenzarchitektur ist als generisches, cloud-provider-agnostisches Modell konzipiert; die Healthcare-Domäne (Ambient AI Scribe) dient im PoC als exemplarischer Anwendungsfall und begrenzt nicht den Architektur-Scope. Die Azure-basierte Instanziierung dient ausschließlich der Demonstration und Evaluation (DSRM-Schritte 4 und 5), nicht der Produktivstellung.

---

## PRÜFPROTOKOLL Kap. 1.6

### Absatz 1 — Scope-Grenzen + Abgrenzung

| Zitation | Zotero-Key | BELEG (exakt aus Quelle) | CLAIM (im Text) | MATCH |
|---|---|---|---|---|
| EU AI Act VO 2024/1689, Art. 26 | Gesetzestext | Art. 26: "Obligations of deployers of high-risk AI systems" | "Perspektive des Deployers im Sinne des Art. 26" | ✅ |
| EU AI Act VO 2024/1689, Art. 16 | Gesetzestext | Art. 16: "Obligations of providers of high-risk AI systems" | "Provider-Pflichten nach Art. 16 [...] außerhalb des Scope" | ✅ |
| EU AI Act VO 2024/1689, Art. 25 | Gesetzestext | Art. 25: "Conditions under which the deployer is also to be treated as a provider" | "Eskalation zur Provider-Rolle nach Art. 25 markiert die Scope-Grenze" | ✅ Konsistent mit D_SCOPE_ART25_RETIREMENT |
| EU AI Act VO 2024/1689, Art. 16 Abs. 1 lit. j | Gesetzestext | Art. 16(1)(j): Provider-Pflicht zur Stilllegung/Rücknahme | "Retirement-Phase [...] Provider-Verantwortung (Art. 16 Abs. 1 lit. j)" | ✅ |
| EU AI Act VO 2024/1689, Art. 9–15 | Gesetzestext | Art. 9–15: Requirements for high-risk AI systems | "Art. 9–15 aus Deployer-Perspektive [...] keinen Anspruch auf juristische Vollständigkeit" | ✅ |
| EU AI Act VO 2024/1689, Art. 10 Abs. 1–5 | Gesetzestext | Art. 10(1): "Hochrisiko-KI-Systeme, in denen Techniken eingesetzt werden, bei denen KI-Modelle mit Daten trainiert werden, werden mit Trainings-, Validierungs- und Testdatensätzen entwickelt" | "Art. 10 Abs. 1–5 adressiert die Governance von Trainings-, Validierungs- und Testdatensätzen und setzt damit voraus, dass der Akteur die Daten kontrolliert" | ✅ |
| EU AI Act VO 2024/1689, Art. 10 Abs. 6 | Gesetzestext | Art. 10(6): "Bei Hochrisiko-KI-Systemen, in denen keine Techniken eingesetzt werden, bei denen KI-Modelle trainiert werden, gelten die Absätze 2 bis 5 nur für Testdatensätze" | "bei Systemen ohne Modelltraining lediglich die Anforderungen an Testdatensätze gelten" | ✅ |
| Novelli et al. (2024, S. 9) | `YV4BV8CY` | "the data governance measures of Article 10 are primarily tailored to providers of GPAI models" | "Data-Governance-Maßnahmen des Art. 10 sind primär auf Anbieter von GPAI-Modellen zugeschnitten (Novelli et al., 2024, S. 9)" | ✅ |
| EU AI Act VO 2024/1689, Art. 3 Nr. 33 | Gesetzestext | Art. 3(33): Definition "Eingabedaten" = Daten, die einem KI-System als Input zugeführt werden | "Eingabedaten im Sinne des Art. 3 Nr. 33" | ✅ |
| EU AI Act VO 2024/1689, Art. 13, 15, 26 Abs. 4 | Gesetzestext | Art. 13: Transparenz; Art. 15: Genauigkeit/Robustheit; Art. 26(4): Eingabedatenrelevanz | "Transparenz- und Robustheitspflichten der Art. 13 und 15 sowie [...] Art. 26 Abs. 4" | ✅ |
| Buscemi et al. (2025, S. 7–8) | `WXJEQWIH` | R4: "Transparency [...] model explainability, data and process traceability" + R4.2: "Model & Data Traceability" | "Buscemi et al. (2025, S. 7–8) ordnen die resultierenden Prüfpflichten entsprechend dem Transparenz-Requirement zu" | ✅ |

**Weitere Claims (ohne externe Zitation):**

| CLAIM | Typ | Beleg |
|---|---|---|
| "Deployment- und Inference-Zyklus" als Fokus | Eigenaussage | ✅ Konsistent mit Kap. 3.4 DOCX: "Phase vom fertig trainierten Modell bis zur überwachten Produktionsfreigabe" |
| "LLM-Training, Fine-Tuning [...] nicht adressiert" | Eigenaussage | ✅ Konsistent mit Exposé S. 8 + Kap. 3.4.3 DOCX |
| "proprietäre Foundation Models über API-Schnittstellen [...] weder Zugang zu Trainingsdaten noch Möglichkeit eines Modelltrainings" | Eigenaussage (strukturell) | ✅ Kap. 4.1 DOCX: "proprietäre Foundation Models über API-Schnittstellen nutzen" + ENTSCHEIDUNGSPAPIER_KAP4 E4: "Foundation Models = proprietäre Black Box für Deployer" |
| "Art. 10 Abs. 2 lit. b–e setzt die Kenntnis über Erhebungsprozesse, Vorverarbeitungsvorgänge und Datenannotation voraus [...] technische Unmöglichkeit" | Normtext + ENTSCHEIDUNGSPAPIER_KAP4 E4 | ✅ Art. 10 Abs. 2(b): Erhebungsprozesse; (c): Vorverarbeitung; (d): Etikettierung; (e): Datenannotation — ENTSCHEIDUNGSPAPIER E4: "Deployer kennt weder Erhebungsprozesse noch Vorverarbeitungsvorgänge" + "Nicht Scope-Wahl, sondern technische Unmöglichkeit" |
| "RAG [...] Kontextdaten verändern das Modell nicht, sondern gehen als Eingabedaten [...] in den Prompt ein" | Eigenaussage | ✅ Kap. 4.1 DOCX: "RAG-Kontextdaten werden zum Zeitpunkt der Inferenz dynamisch bereitgestellt und gehen als Eingabedaten in den Prompt ein, ohne das Modell selbst zu verändern" |
| "RAG-Zuordnung = normativ begründete Interpretation [...] Limitation in Abschnitt 4.1 und Kapitel 7" | Eigenaussage + ENTSCHEIDUNGSPAPIER_KAP4 Entsch. 2 | ✅ ENTSCHEIDUNGSPAPIER Entsch. 2 Risiko: "Dies ist eine Interpretation, kein expliziter Normtext. Als Limitation kennzeichnen." + Umsetzung: "Interpretation als Limitation: Kap. 4.1 (Satz) + Kap. 7 (ausführlich) + Ausblick" |
| "cloud-provider-agnostisches Modell" | Eigenaussage | ✅ DP5 (Kap. 3.4.2): "Cloud-native Integrierbarkeit" ohne proprietäre Abhängigkeiten |
| "Healthcare [...] exemplarischer Anwendungsfall [...] nicht den Architektur-Scope" | Eigenaussage | ✅ Exposé S. 8: "Healthcare als exemplarischer Anwendungsfall für die PoC-Validierung, nicht als Architektur-Scope" + Kap. 3.4.3 |
| "Demonstration und Evaluation (DSRM-Schritte 4 und 5)" | Eigenaussage | ✅ Kap. 3.4.3 DOCX: "PoC dient ausschließlich der Demonstration [...] (DSRM-Schritt 4) und der Evaluation (DSRM-Schritt 5)" |

---

## BILANZ Kap. 1.6

- **Wörter:** ~415 (≈1,4 Seiten)
- **Unique Quellen:** 3 (EU AI Act VO 2024/1689, Novelli et al. 2024, Buscemi et al. 2025) + ENTSCHEIDUNGSPAPIER_KAP4 (Entsch. 1+2)
- **Zitationen mit Seitenzahl:** Novelli S. 9 ✅ | Buscemi S. 7–8 ✅ | Gesetzestext (Artikelnummern) ✅
- **Halluzinierte Quellen:** 0
- **Neue Quellen in 1.6:** Novelli et al. (2024, S. 9) — Provider-Fokus Art. 10; Buscemi et al. (2025, S. 7–8) — Transparenz-Requirement R4
- **Novelli-Doppelzitation:** ✅ Vermieden — 1.2 (S. 10, 14) = Beweislast-Asymmetrie; 1.6 (S. 9) = Art. 10 Provider-Zuordnung → unterschiedliche Claims
- **Buscemi-Doppelzitation:** ✅ Vermieden — 1.1 (S. 1) = persistente Lücke; 1.6 (S. 7–8) = R4 Transparenz-Requirement → unterschiedliche Claims
- **Negativ-Checklist:** ✅ Keine S1–S4-Wiederholung (→1.3), keine Evaluationsdetails (→1.3/6), keine DP-Auflistung (→3.4/5.1), keine Healthcare-Begründung (→Exposé/3.4.3), kein Azure-Stack-Detail (→5.6), keine formale Überleitung
- **Delta zu 1.3:** 1.3 = WAS gebaut wird (positiver Scope); 1.6 = WAS NICHT drin ist (negativer Scope) + regulatorische Grenzen + Lifecycle-Fokus → komplementär, keine Redundanz ✅
- **SOT-Konsistenz:** Alle Claims gegen Exposé S. 8, Kap. 3.4 DOCX, Kap. 4.1 DOCX und D_SCOPE_ART25_RETIREMENT geprüft ✅
- **Argumentationsstruktur:** Deployer-Perspektive→Provider-Grenze→Lifecycle-Fokus→Out-of-Scope-Liste→**Art. 10 Differenzierung (Normtext→Novelli→Black Box/techn. Unmöglichkeit)**→**RAG-Klassifizierung (Art. 3 Nr. 33→Art. 13/15→Buscemi R4→Limitation als Interpretation)**→Ethik/Recht-Limitation→PoC-Abgrenzung ✅
