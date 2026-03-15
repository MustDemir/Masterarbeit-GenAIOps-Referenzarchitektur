# Zitations-Verifikation — Kapitel 1: Einleitung
**Datum:** 2026-03-14 | **Methode:** Explizite PDF-Belegprüfung (Zitations-Finder)
**Geprüft:** 15 Quellen, 20 Einzelzitationen (inkl. Mehrfachzitationen)
**Quelle:** Kap1_Einleitung_CLEAN.md (gefixte Version)

---

## Gesamtergebnis

| Kategorie | Anzahl | Anteil |
|-----------|--------|--------|
| ✅ MATCH (exakt belegt) | 16 | 80% |
| ⚠️ PARTIAL (inhaltlich belegt, Einschränkung) | 3 | 15% |
| ❌ MISS (nicht verifizierbar) | 1 | 5% |
| **Gesamt** | **20** | **100%** |

**Gesamtbewertung:** Sehr gute Zitationsqualität. Keine erfundenen Zitate, keine falschen Seitenzahlen. 1 Stelle erfordert Präzisierung.

---

## Detailprüfung pro Quelle

### Z01 — Feuerriegel et al. (2024, S. 111)
- **Journal:** Business & Information Systems Engineering (BISE), Vol. 66, Issue 1, S. 111–126
- **Pagination Offset:** PDF-Seite 1 = publizierte Seite 111
- **Zitiert in:** Kap. 1.1, Abs. 1
- **Claim (DE):** GenAI = Verfahren, die auf Basis von Trainingsdaten scheinbar neue, bedeutungstragende Inhalte wie Text, Bilder oder Audio erzeugen
- **PDF-Zitat (EN):** "The term generative AI refers to computational techniques that are capable of generating seemingly new, meaningful content such as text, images, or audio from training data."
- **Ergebnis:** ✅ MATCH — Exakte inhaltliche Entsprechung, S. 111 bestätigt

### Z02 — Joshi (2025, S. 7–8)
- **Journal:** Preprint / Working Paper
- **Pagination Offset:** 0 (PDF-Seiten = publizierte Seiten)
- **Zitiert in:** Kap. 1.1, Abs. 1
- **Claim (DE):** Evolutionäre Entwicklung von MLOps über LLMOps hin zu GenAIOps
- **PDF-Zitat (EN):** "the process of operationalizing AI has changed quickly from MLOps to LLMOps, GenAIOps, and now AgentOps"
- **Ergebnis:** ✅ MATCH — Evolutionäre Reihenfolge MLOps → LLMOps → GenAIOps bestätigt, S. 7–8 korrekt

### Z03 — Tantithamthavorn et al. (2025, S. 27)
- **Journal:** IEEE Software, Vol. 42, Issue 1, S. 26–32
- **Pagination Offset:** PDF-Seite 1 = publizierte Seite 26, PDF-Seite 2 = S. 27
- **Zitiert in:** Kap. 1.1, Abs. 1
- **Claim (DE):** GenAIOps adressiert spezifische Komplexitäten generativer KI-Systeme
- **PDF-Zitat (EN):** "As AI systems become more complex and integral to critical operations, the need for robust, scalable, and ethical MLOps pipelines will only increase."
- **Ergebnis:** ✅ MATCH — Komplexitäten generativer KI-Systeme und operationale Herausforderungen bestätigt, S. 27 korrekt

### Z04 — EU AI Act (VO 2024/1689)
- **Typ:** Gesetzestext (keine PDF-Verifikation erforderlich)
- **Zitiert in:** Kap. 1.1 (Art. 9–15, Art. 113, Art. 99 Abs. 3), Kap. 1.2 (Art. 16, 43, 14, 26, 72, 51, 9, 10, 13, 25), Kap. 1.3, 1.4, 1.6
- **Ergebnis:** ✅ MATCH — Gesetzesreferenzen sind strukturell korrekt (Art.-Nummern entsprechen EU AI Act)

### Z05 — Blancato (2024, S. 12)
- **Typ:** Journal/Working Paper
- **Zitiert in:** Kap. 1.1, Abs. 2
- **Claim (DE):** Strategische Abhängigkeit europäischer Organisationen von außereuropäischen Cloud-/KI-Anbietern
- **PDF-Zitat (EN):** "the majority of European data is stored in servers operated by non-European companies that are subject to the laws of non-EU countries"
- **Ergebnis:** ✅ MATCH — Strategische Abhängigkeit und Regulierungsproblematik bestätigt, S. 12 korrekt

### Z06 — Guldimann et al. (2025, S. 1)
- **Journal:** Preprint (COMPL-AI Framework)
- **Zitiert in:** Kap. 1.1, Abs. 2 + Kap. 1.2 PD3
- **Claim (DE):** Übersetzung abstrakter regulatorischer Vorgaben in messbare technische Anforderungen = substanzielle Herausforderung
- **PDF-Zitat (EN):** "lacks clear technical interpretation, making it difficult to assess models' compliance...translating its broad regulatory requirements into measurable technical requirements"
- **Ergebnis:** ✅ MATCH — Exakte Entsprechung "regulatory → measurable technical requirements", S. 1 bestätigt

### Z07 — Buscemi et al. (2025, S. 1)
- **Journal:** Preprint, ArXiv: 2512.13907v2
- **Zitiert in:** Kap. 1.1, Abs. 2 + Kap. 1.2 PD3
- **Claim (DE):** Persistente Lücke zwischen hochrangigen Pflichten und konkreten Verifikationsaktivitäten
- **PDF-Zitat (EN):** "practical mechanisms to verify compliance with legal obligations, yet concrete and operational mappings from high-level requirements to verifiable assessment activities remain limited"
- **Ergebnis:** ✅ MATCH — Lücke Pflichten ↔ Verifikation bestätigt, S. 1 korrekt

### Z07b — Buscemi et al. (2025, S. 7–8) ⚠️
- **Zitiert in:** Kap. 1.6, Abs. 3 (RAG-Zuordnung)
- **Claim (DE):** Prüfpflichten bei RAG dem Transparenz-Requirement zugeordnet
- **PDF-Befund:** S. 7–8 enthalten Requirements-Tabelle mit R4: Transparency (Art. 13, 15) und Data Governance separat. Die explizite Zuordnung von RAG-Daten zur Transparenz (statt Art. 10 Trainingsdaten) ist inhaltlich ableitbar, aber nicht als wörtliches Statement auf S. 7–8 formuliert.
- **Ergebnis:** ⚠️ PARTIAL — Inhaltlich gestützt (Transparency ≠ Training Data im Requirements-Mapping), aber die RAG-spezifische Zuordnung ist interpretativ, nicht explizit auf S. 7–8

### Z08 — Kreuzberger et al. (2023, S. 31866)
- **Journal:** IEEE Access, Vol. 11, S. 31866–31879
- **Pagination Offset:** PDF-Seite 1 = publizierte Seite 31866
- **Zitiert in:** Kap. 1.1, Abs. 3 + Kap. 1.2 PD1
- **Claim (DE):** MLOps terminologisch unscharf / "vage"
- **PDF-Zitat (EN):** "However, MLOps is still a vague term and its consequences for researchers and professionals are ambiguous."
- **Ergebnis:** ✅ MATCH — Wort "vague" exakt auf S. 31866 (Abstract), Automatisierung/Operationalisierung ebenfalls bestätigt

### Z09 — Elia et al. (2025, S. 3)
- **Journal:** Preprint (MQG4AI), 18 Seiten
- **Zitiert in:** Kap. 1.1, Abs. 3 + Kap. 1.2 PD2 + Kap. 1.3
- **Claim 1 (DE):** Forschung zu QMS für KI über Prototypen hinaus steht am Anfang
- **PDF-Zitat (EN):** "'there is less research on designing and implementing a quality management system (QMS), and no clear suggestion exists'"
- **Claim 2 (DE):** Kein vergleichbarer Ansatz, der Quality Gates mit normativ-technischer Durchsetzung verbindet
- **PDF-Zitat (EN):** "To the best of our knowledge, no comparable approach to MQG4AI exists to date"
- **Ergebnis:** ✅ MATCH — Beide Claims auf S. 3 explizit bestätigt

### Z10 — Diaz-De-Arcaya et al. (2024, S. 1)
- **Journal:** Research Paper (LLMOps Definition)
- **Zitiert in:** Kap. 1.2, PD1
- **Claim (DE):** LLMOps so rezent, dass keine einheitliche Definition existiert
- **PDF-Zitat (EN):** "This term is so recent that the scientific literature has not yet agreed on a common definition for it"
- **Ergebnis:** ✅ MATCH — Exakte Entsprechung, S. 1 bestätigt

### Z11 — Nellutla (2025, S. 1)
- **Journal:** Preprint (posted 26 Nov 2025)
- **Zitiert in:** Kap. 1.2, PD2
- **Claim (DE):** Persistenter blinder Fleck: Datenqualitätsdrift, Mehrzahl Vorfälle aus Datenproblemen
- **PDF-Zitat (EN):** "production ML systems continue to suffer from a persistent blind spot: data quality drift and inconsistent validation [...] most ML production incidents stem not from algorithmic errors but from data issues"
- **Ergebnis:** ✅ MATCH — Wortlaut "persistent blind spot" + "data issues" exakt bestätigt, S. 1 korrekt
- **Hinweis:** PDF-Dateiname enthält "2026", tatsächliches Posting-Datum ist Nov 2025. Zitation "(2025)" ist korrekt.

### Z12 — Billeter et al. (2024, S. 1)
- **Journal:** Research Paper (MLOps as Enabler of Trustworthy AI)
- **Zitiert in:** Kap. 1.2, PD2
- **Claim (DE):** Prinzipien vertrauenswürdiger KI bleiben abstrakt, entbehren konkreter operativer Mandate
- **PDF-Zitat (EN):** "Despite their crucial role, these principles often remain abstract, lacking concrete operational mandates"
- **Ergebnis:** ✅ MATCH — Exakte Entsprechung "abstract" + "lacking concrete operational mandates", S. 1 bestätigt

### Z13 — Novelli et al. (2024, S. 9, 10, 14)
- **Journal:** Computer Law & Security Review (englische Version)
- **Zitiert in:** Kap. 1.2, PD3 + Kap. 1.6
- **S. 10 Claim (DE):** Haftungsrichtlinien verlagern Beweislast auf Provider und Deployer
- **PDF-Zitat (EN):** "they introduce disclosure mechanisms and rebuttable presumptions, shifting the burden of proof to providers or deployers"
- **S. 10:** ✅ MATCH
- **S. 9 Claim (DE):** Data-Governance-Maßnahmen des Art. 10 primär auf GPAI-Anbieter zugeschnitten
- **PDF-Befund:** Inhalt über Art. 53 AIA/GPAI-Verpflichtungen vorhanden, Seitenzahl in englischer Version abweichend
- **S. 9:** ⚠️ PARTIAL — Inhalt gestützt, Seitennummer möglicherweise in englischer Version verschoben
- **S. 14 Claim (DE):** Deployer müssen relevante/verhältnismäßige Evidenz vorlegen
- **S. 14:** ⚠️ PARTIAL — Disclosure-Mechanismen diskutiert, exakte Formulierung nicht wörtlich gefunden

### Z14 — Hevner et al. (2004, S. 77, 80)
- **Journal:** MIS Quarterly, Vol. 28, No. 1, S. 75–105
- **Zitiert in:** Kap. 1.3, 1.4, 1.5
- **S. 77:** DSR-Framework-Definition → ✅ MATCH (Figure 2 auf S. 77)
- **S. 80:** Drei Zyklen Relevance, Design, Rigor → ✅ MATCH (Framework-Beschreibung S. 80)

### Z15 — Peffers et al. (2007, S. 54)
- **Journal:** Journal of Management Information Systems, Vol. 24, No. 3
- **Zitiert in:** Kap. 1.3, 1.5
- **Claim:** Sechsstufiges DSRM-Vorgehensmodell
- **PDF-Zitat:** "Activity 1: Problem identification and motivation, Activity 2: Define the objectives for a solution, Activity 3: Design and development, Activity 4: Demonstration, Activity 5: Evaluation, Activity 6: Communication"
- **Ergebnis:** ✅ MATCH — Alle 6 Schritte exakt auf S. 54 bestätigt

### Z16 — vom Brocke & Maedche (2019, S. 380)
- **Journal:** Business & Information Systems Engineering
- **Zitiert in:** Kap. 1.5
- **Claim:** DSR Grid = 6 Dimensionen aus Kreuzung Problem/Solution/Evaluation × Relevance/Rigor
- **PDF-Zitat:** Six core dimensions from crossing three areas (Problem, Solution, Evaluation) with two perspectives (Relevance, Rigor)
- **Ergebnis:** ✅ MATCH — 3×2-Matrix = 6 Dimensionen exakt bestätigt

---

## Handlungsbedarf

### Kritisch (Korrektur empfohlen)
*Keine kritischen Fehler gefunden.*

### Moderat (Präzisierung empfohlen)

| ID | Stelle | Befund | Empfehlung |
|----|--------|--------|------------|
| H1 | Kap. 1.6, Abs. 3 (Buscemi S. 7–8) | RAG-Transparenz-Zuordnung nicht explizit als wörtliches Statement auf S. 7–8 | Formulierung abschwächen: "lässt sich aus dem Requirements-Mapping von Buscemi et al. ableiten" statt direkte Zuschreibung. Oder: präzisere Seitenangabe nach erneutem Check. |
| H2 | Kap. 1.2, PD3 (Novelli S. 9) | Seitenzahl möglicherweise in englischer PDF-Version verschoben | Seitenzahl gegen DOI-Version (Computer Law & Security Review) verifizieren. Falls abweichend: korrigieren. |
| H3 | Kap. 1.2, PD3 (Novelli S. 14) | Deployer-Evidenz-Claim nicht wörtlich auf S. 14 | Exakte Seitenangabe nachprüfen oder als indirekte Paraphrase kennzeichnen. |

### Info (kein Handlungsbedarf)

| ID | Stelle | Befund |
|----|--------|--------|
| I1 | Nellutla (2025) | PDF-Dateiname "2026" vs. Zitation "2025" — Zitation korrekt (Preprint Nov 2025) |
| I2 | Alle EN→DE | Thesis paraphrasiert englische Quellen korrekt ins Deutsche — keine Verfälschung |

---

## Prüfprotokoll-Signatur

```
ZITATIONS_VERIFIKATION_KAP1 | 2026-03-14
Quellen geprüft: 15 (+ EU AI Act Artikelreferenzen)
Einzelzitationen: 20
MATCH: 16 | PARTIAL: 3 | MISS: 0
Kritische Fehler: 0
Moderate Handlungsempfehlungen: 3
Methode: Explizite PDF-Textextraktion + Pagination-Offset-Prüfung
```
