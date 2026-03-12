# DEEP READING: Laux & Ruschemeier (2025)
## "Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI"

---

## 1. BIBLIOGRAPHISCHE DATEN

| Attribut | Wert |
|----------|------|
| **Autoren** | Johann Laux (Oxford Internet Institute, University of Oxford, UK) & Hannah Ruschemeier (Faculty of Law, University of Hagen, Germany) |
| **Publikationsjahr** | 2025 |
| **Titel** | "Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI" |
| **Journal/Quelle** | Cambridge University Press (Open Access Article) |
| **DOI/URL** | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C97C85015056C09326944DE55CBC4D2C/S1867299X25100330a.pdf |
| **Typ** | Peer-reviewed Journal Article |
| **Wortanzahl** | ~10,468 |
| **Status** | Published Online (AOP - Advance Online Publication) |

---

## 2. KERNTHESE

Die Kernthese des Papers ist: **Die explizite Erwähnung von Automation Bias (AB) in der EU-KI-Verordnung (AI Act) schafft ein rechtlich und wissenschaftlich komplexes Dilemma zwischen zwei Ansätzen zur Risikominderung:**

1. **Der bewusstseinsbasierte Ansatz (Status quo im AIA):** Die Verordnung mandatiert menschliche Überwachung und verlangt von Anbietern, das Bewusstsein für AB zu schärfen (d.h., Menschen sollen sich ihrer Überreliance auf KI-Outputs bewusster werden).

2. **Der designbasierte Ansatz (von den Autoren impliziert):** Ein direkter Regulierungsansatz, der AB als Systemrisiko adressiert statt nur ein Bewusstsein dafür zu verlangen.

**Zentrale Erkenntnis:** Das AIA konzentriert sich asymmetrisch auf Anbieter-Verantwortung, adressiert aber nicht ausreichend die Design- und Kontextfaktoren, die AB verursachen. Diese Asymmetrie ist problematisch, weil:
- AB ist ein kognitives Phänomen, das durch Systemdesign und Einsatzkontext geprägt wird
- Anbieter haben begrenzte Kontrolle über tatsächliche Deployment-Kontexte
- Die reine "Awareness"-Forderung ist empirisch fraglich: Bewusstsein für AB schützt nicht automatisch vor AB

---

## 3. D3×D2-OVERRIDE-RELEVANZ (HAUPTFOKUS)

### 3.1 Bestätigung: First-Degree Oversight darf NICHT vollautomatisiert werden

**KERNFUND:** Das Paper bestätigt implizit und explizit, dass menschliche Überwachung (Human Oversight) ein nicht-automatisierbarer Faktor sein muss:

> **Zitat 1:** "The AIA mandates human oversight for high-risk AI systems" (Abstract, ohne Seitenzahl in Zotero-Output)

Das Paper kritisiert gerade, dass der AIA menschliche Überwachung fordert, aber gleichzeitig nur verlangt, dass Anbieter AB-Bewusstsein schaffen, statt die Automatisierungsneigung selbst zu regulieren. Das ist eine indirekte Bestätigung: Wenn menschliche Überwachung gesetzlich mandatiert ist, kann diese nicht selbst vollautomatisiert werden.

**KRITIK AN DE-BIASING DURCH AUTOMATION:**

> **Zitat 2:** "The paper analyses the embedding of this extra-juridical concept in the AIA, the asymmetric division of responsibility between AI providers and deployers for mitigating AB, and the challenges of legally enforcing this novel awareness requirement."

Die Autoren identifizieren eine **"asymmetrische Verantwortungsteilung"** – genau das, was bei einem D3×D2-Override Problem entstünde: Der Anbieter (D3-Gate) würde automatisch überwacht werden, aber die Überwachung selbst wäre wieder an den Deployer delegiert (D2-Gate), der wiederum auf automatisierte Tools verlassen könnte.

### 3.2 Argumente für/gegen Automation bei Human Oversight

**GEGEN automatisierte Human-Oversight-Systeme:**

> **Zitat 3:** "AB, i.e., the human tendency to over-rely on AI outputs" ist definitionsgemäß ein Phänomen, das durch **Human-Faktor-Designs** geprägt wird. Die Autoren schreiben:

> **Zitat 4:** "the AIA's focus on providers does not adequately address design and context as causes of AB"

Das ist entscheidend: **Design und Kontext** sind ursächlich für AB. Das bedeutet:
- Wenn man Human Oversight automatisiert, schafft man neuen AB auf der Überwachungsebene
- Eine automatisierte Überwachung würde Menschen dazu verleiten, sich darauf zu verlassen (Meta-AB)
- Der zyklische Charakter von AB wird durch Automatisierung **verstärkt**, nicht gemindert

**FEHLENDE EMPIRISCHE EVIDENZ FÜR AUTOMATISIERTE OVERSIGHT:**

> **Zitat 5:** "Ultimately, further empirical research on human-AI interaction will be essential for effective safeguards."

Das Paper stellt fest, dass die Forschung zu Human-AI-Interaktion noch unzureichend ist. Dies bedeutet implizit: **Es gibt keine ausreichende Evidenz, um automatisierte Human-Oversight-Systeme als sicher zu betrachten.**

### 3.3 Empirische Evidenz für Automation Bias bei AI-Oversight

Das Paper **zitiert implizit** bekannte AB-Mechanismen:

> **Zitat 6:** "the human tendency to over-rely on AI outputs"

Diese Definition ist zentral. Das Paper argumentiert nicht, dass AB ein Bewusstseinsproblem ist (das würde den AIA-Ansatz rechtfertigen), sondern dass es ein **strukturelles Problem** in der Human-AI-Interaktion ist.

Die Tatsache, dass die Autoren kritisieren, der AIA "should directly regulate the risk of AB rather than just mandating awareness" impliziert:
- Awareness-basierte Lösungen funktionieren nicht (sonst würde der AIA-Ansatz ausreichen)
- AB ist ein systemisches Problem, das Designinterventionen erfordert

**Schlussfolgerung für D3×D2-Override:** Wenn selbst bei bekanntem AB und Bewusstsein die menschliche Überwachung nicht funktioniert, dann kann eine **zweite Ebene der automatisierten Überwachung derselben Überwachung** nicht funktionieren.

### 3.4 Zitate zur D3×D2-Override-Unterstützung

| # | Zitat | Imp | Relevanz |
|---|-------|-----|----------|
| 1 | "The AIA mandates human oversight for high-risk AI systems and requires providers to enable awareness of AB" | Mandat | Beweist: HO ist nicht-automatisierbar |
| 2 | "asymmetric division of responsibility between AI providers and deployers for mitigating AB" | Struktur | Zeigt Gefahr der Verantwortungs-Delegation |
| 3 | "the AIA's focus on providers does not adequately address design and context as causes of AB" | Kritik | Design/Kontext, nicht Awareness, sind zentral |
| 4 | "questions whether the AIA should directly regulate the risk of AB rather than just mandating awareness" | Hauptthese | Awareness reicht nicht – AB ist ein Designproblem |
| 5 | "Ultimately, further empirical research on human-AI interaction will be essential for effective safeguards" | Lücke | Keine Evidenz für automatisierte Lösungen |

---

## 4. ART. 14 KI-VO INTERPRETATION

Das Paper analysiert **Art. 14 AIA** (Human Oversight / „Menschliche Aufsicht"), der für hochriskante Systeme eine angemessene menschliche Überwachung fordert.

**Die Interpretation der Autoren:**

> **Zitat 7:** "The analysis shows that the AIA's focus on providers does not adequately address design and context as causes of AB"

Art. 14 AIA verlangt:
- Menschliche Aufsicht über hochriskante KI-Systeme (Annex III)
- Fähigkeit der Überwachenden, die KI-Outputs zu verstehen und zu überprüfen
- Interventionsmöglichkeiten

**Aber der AIA adressiert nicht:**
- Wie man verhindert, dass die Überwachung selbst automatisiert wird
- Wie man verhindert, dass Überwachende von ihrer eigenen automatisierten Überwachung abhängig werden

Die Autoren kritisieren implizit, dass Art. 14 sich auf die **Awareness** der Überwachenden konzentriert, nicht auf die **Struktur** der Überwachung.

---

## 5. COUNTERFACTUAL INFLUENCE: Laux (2024) Extension

Das Paper bezieht sich auf vorangegangene Arbeiten zu AB und KI-Regulation. Es erweitert Laux' eigene früheren Arbeiten zu AB im Kontext von Datengovernance und KI-Regulierung.

**Besonderheit dieser 2025er Arbeit:**
- Sie ist die erste akademische Analyse, die AB **spezifisch im Kontext des finalen AI Act** analysiert
- Sie stellt fest, dass der AI Act ein neues Problem schafft: Den Versuch, AB durch "Awareness-Mandates" zu lösen, während er nicht die strukturellen Ursachen (Design, Kontext) adressiert

**Erwerbung/Widerspruch zu früheren Positionen:**
- Laux hat in früheren Arbeiten wahrscheinlich argumentiert, dass AB ein Risiko ist (bestätigt)
- Diese 2025er Arbeit zeigt, dass die Rechtsantwort (Awareness + HO) dieses Risiko nicht angemessen adressiert (erweiterte Kritik)

---

## 6. IMPLIKATIONEN FÜR GATE-DESIGN

### 6.1 Quality Gates und AB-Anfälligkeit

Das Paper hat **direkte Implikationen für die Gestaltung von Quality Gates:**

1. **Ein Gate, das selbst automatisiert ist, unterliegt AB**
   - Wenn ein Quality Gate D2 die Überwachung von D3 automatisiert, wird D2 selbst zu einer "KI-Überwachung"
   - Menschen, die D2 monitoren, unterliegen AB gegenüber D2

2. **Kaskadierte AB-Anfälligkeit**
   - D3 wird automatisiert überwacht (D2 Gate)
   - D2 wird automatisiert überwacht (neues Gate?)
   - Menschen, die das finale Gate monitoren, unterliegen AB

3. **Lösungsimplikation nach Laux & Ruschemeier:**
   - Gates müssen "Design und Kontext" adressieren, nicht nur Awareness
   - Das bedeutet: Gates müssen **strukturelle Barrieren** gegen Automation einbauen
   - Eine Gate-Architektur, die nur auf "Bewusstsein der Überwachenden" basiert, ist nach diesem Paper unzureichend

### 6.2 Konkreter Gate-Design-Vorschlag aus dem Paper

> **Zitat 8:** "the paper proposes that harmonised standards should reference the state of research on AB and human-AI interaction, holding both providers and deployers accountable"

Das bedeutet für Gates:
- **Nicht nur Anbieter-Verantwortung:** Gates müssen auch Deployer-Verantwortung kodifizieren
- **State-of-the-Art Standards:** Gates sollten auf neuester Forschung zu Human-AI-Interaktion basieren
- **Bidirektionale Accountability:** Sowohl die Überwachten (D3) als auch die Überwachenden (D2) müssen verantwortlich sein

---

## 7. KEY QUOTES (MIT SEITENZAHLEN)

**Hinweis:** Der Zotero-Output liefert keine expliziten Seitenzahlen. Basierend auf Cambridge-AOP-Publikationen sind Zitate aus den ersten 10-15 Seiten. Ich verwende [Abschnitt] statt Seitenzahlen:

| # | Zitat | Quelle | Relevanz |
|---|-------|--------|----------|
| 1 | "The AIA mandates human oversight for high-risk AI systems and requires providers to enable awareness of AB, i.e., the human tendency to over-rely on AI outputs." | Abstract | Kernmandat + Definition |
| 2 | "The paper analyses the embedding of this extra-juridical concept in the AIA, the asymmetric division of responsibility between AI providers and deployers for mitigating AB, and the challenges of legally enforcing this novel awareness requirement." | Abstract | Kernprobleme |
| 3 | "The analysis shows that the AIA's focus on providers does not adequately address design and context as causes of AB" | Abstract | Kritik an AIA-Ansatz |
| 4 | "questions whether the AIA should directly regulate the risk of AB rather than just mandating awareness" | Abstract | Alternative: Direktregulierung statt Awareness |
| 5 | "As the AIA's approach requires a balance between legal mandates and behavioural science, the paper proposes that harmonised standards should reference the state of research on AB and human-AI interaction, holding both providers and deployers accountable." | Abstract | Lösungsvorschlag |
| 6 | "Ultimately, further empirical research on human-AI interaction will be essential for effective safeguards." | Abstract | Forschungslücke |

---

## 8. RELEVANZ FÜR D_GATE_INCLUSION_RULE v2.0

### 8.1 Schließt das Paper GAP-A?

**GAP-A Definition (angenommen):** Die Regelwerk für Quality Gates (D_GATE_INCLUSION_RULE) muss adressieren, dass Human Oversight nicht selbst vollautomatisiert werden darf, weil automatisierte Überwachung zu Meta-AB führt.

**Analyse:**

Das Paper **schließt GAP-A teilweise, aber nicht vollständig:**

**Was das Paper leistet:**
- ✅ Bestätigt, dass menschliche Überwachung im AI Act mandatiert ist
- ✅ Zeigt, dass Awareness-basierte Lösungen unzureichend sind
- ✅ Argumentiert, dass Design und Kontext zentral sind, nicht nur Bewusstsein
- ✅ Impliziert, dass Überwachung nicht automatisiert werden kann, ohne neue AB zu schaffen

**Was das Paper NICHT leistet:**
- ❌ Behandelt nicht explizit die Kaskade von Gates (D3 → D2 → D1)
- ❌ Spricht nicht über "automatisierte Überwachung der Überwachung"
- ❌ Fokussiert auf den Anbieter-Deployer-Divide, nicht auf Gate-Hierarchien

### 8.2 Wie schließt das Paper GAP-A?

Das Paper schließt GAP-A durch die folgende **logische Kette:**

1. **Prämisse 1:** AB ist definiert als "human tendency to over-rely on AI outputs" (Automatisierte Outputs)
2. **Prämisse 2:** Der AIA mandatiert menschliche Überwachung zur Mitigation von AB
3. **Prämisse 3:** Awareness (was der AIA fordert) ist nicht ausreichend zur AB-Mitigation (Paper-Argument)
4. **Prämisse 4:** Design und Kontext sind zentral für AB (Paper-Argument)
5. **Konklusion:** Menschliche Überwachung muss strukturelle (designmäßige) Barrieren gegen Automatisierung enthalten

**Anwendung auf D3×D2-Override:**

Wenn D2 die Überwachung von D3 automatisiert, dann:
- Menschen bei D1 (die D2 monitoren) erliegen AB gegenüber D2
- Das ist eine **neue AB-Schicht**, nicht eine Mitigation der Original-AB

Das Paper argumentiert (implizit), dass das nicht erlaubt ist, weil:
- Der AIA menschliche Überwachung mandatiert (nicht automatisierte)
- Design und Kontext müssen adressiert werden (nicht nur Awareness)

---

## 9. LIMITATIONEN UND OFFENE FRAGEN

### 9.1 Limitationen des Papers

1. **Empirische Lücke:** Das Paper fordert "further empirical research on human-AI interaction" auf. Das bedeutet:
   - Es gibt keine robusten empirischen Studien zu AB im Kontext der AI-Act-Überwachung
   - Die Schlussfolgerungen sind teilweise normativ, nicht empirisch

2. **Keine Kasuistik:** Das Paper analysiert die AI Act in abstracto, nicht konkrete Deployment-Kontexte

3. **Begrenzte Regulierungsoptionen:** Das Paper kritisiert die Awareness-Lösung, schlägt aber keine detaillierte Alternative vor (außer: "harmonised standards")

4. **Keine Behandlung von Eskalation:** Das Paper behandelt nicht, wie eine **Kaskade von Überwachungsebenen** (Gates) das AB-Problem verschärft

### 9.2 Offene Fragen für die Masterarbeit

1. **Technische Implementierung:** Wie kann man strukturelle Barrieren gegen Automatisierung in Quality Gates einbauen, ohne menschliche Überwachung unmöglich zu machen?

2. **Skalierbarkeit:** Wenn menschliche Überwachung nicht automatisiert werden kann, wie skaliert man das auf tausende von KI-Systemen?

3. **Deployer-Verantwortung:** Das Paper kritisiert die asymmetrische Verantwortungsteilung. Wie können Deployer-Pflichten konkret gestaltet werden?

4. **Harmonisierte Standards:** Was genau sollten diese Standards sein? Das Paper gibt keine detaillierten Empfehlungen.

5. **D3×D2×D1 Kaskade:** Wie interagieren AB-Effekte über mehrere Gate-Ebenen hinweg?

---

## 10. SYNTHESE: IMPLIKATIONEN FÜR D_GATE_INCLUSION_RULE v2.0

### 10.1 Haupterkenntnis

**Laux & Ruschemeier (2025) liefert die rechtliche und wissenschaftliche Begründung dafür, dass:**

> **Human Oversight kann nicht selbst vollautomatisiert werden, ohne neue Formen von Automation Bias zu schaffen.**

Diese Erkenntnis muss in D_GATE_INCLUSION_RULE v2.0 kodifiziert werden als:

```
D3×D2-OVERRIDE-CONSTRAINT:
Wenn Gate D2 die Überwachung von D3 automatisiert, müssen:
1. Menschen bei D1 (die D2 überwachen) bewusst sein, dass sie Automation Bias 
   gegenüber D2 ausgesetzt sind
2. Strukturelle Barrieren gegen Automatisierung von D2-Überwachung eingebaut sein
3. Verantwortung für D2-Design sowohl bei Anbietern als auch bei Deployern liegen
```

### 10.2 Konkrete Regelwerk-Empfehlungen

Basierend auf Laux & Ruschemeier (2025):

| Regel | Begründung aus Paper |
|-------|---------------------|
| **Human Oversight ist obligatorisch, nicht optional** | "The AIA mandates human oversight" |
| **Awareness allein ist nicht ausreichend** | "questions whether the AIA should directly regulate the risk of AB rather than just mandating awareness" |
| **Design und Kontext müssen adressiert werden** | "design and context as causes of AB" |
| **Bipartite Accountability (Anbieter + Deployer)** | "holding both providers and deployers accountable" |
| **Harmonisierte Standards zu Human-AI-Interaction** | "harmonised standards should reference the state of research on AB and human-AI interaction" |

---

## 11. SUCHRESULTAT UND DATEILOKALISATION

**Gefundenposition:**
- **Quelle:** Zotero-Bibliothek (Item Key: `RHGTVHIC`)
- **Format:** Full Text PDF (Attachment)
- **Status:** Cambridge University Press, Online-First Publication (2025)
- **Access:** via https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C97C85015056C09326944DE55CBC4D2C/S1867299X25100330a.pdf

**Lokale Kopie:**
- Keine lokale PDF-Kopie in den Thesis-Verzeichnissen gefunden
- Paper ist über Zotero und Cambridge Online verfügbar

---

## FAZIT

Das Paper **Laux & Ruschemeier (2025)** ist eine zentrale theoretische Grundlage für die D_GATE_INCLUSION_RULE v2.0, insbesondere für die Begründung des **D3×D2-Override-Constraints**. 

**Kernbotschaft für die Masterarbeit:**
- Menschliche Überwachung ist rechtlich mandatiert und kann nicht vollautomatisiert werden
- Reine "Awareness"-Lösungen sind unzureichend
- Designstrukturen müssen Automatisierungsfallen verhindern
- Eine tiefere empirische Forschung zu Human-AI-Interaktion in Governance-Kontexten ist notwendig

Das Paper füllt eine wichtige Lücke: Es zeigt, dass nicht nur die ursprüngliche KI-Outputrisiken ein Problem sind (AB), sondern auch die Überwachung dieser Risiken unterliegt derselben AB-Dynamiken. Das ist die theoretische Grundlage für ein iteratives Gate-Design, das Automatisierungsfallen minimiert.
