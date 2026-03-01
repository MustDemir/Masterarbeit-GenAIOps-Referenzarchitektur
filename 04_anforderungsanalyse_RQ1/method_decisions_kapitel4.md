
# Method Decisions (MD) – Ausführliche Entscheidungsdokumentation (Session-Bericht)

> Zweck: Diese Datei dokumentiert die in der Session getroffenen methodischen und konzeptionellen Entscheidungen (MD) inklusive Alternativen, Begründungen, Implikationen, Deltas zu Exposé/Methodik sowie Scope-Guardrails. Ziel ist Nachvollziehbarkeit gegenüber der Betreuung und eine stabile Grundlage für den Schreibstart in Kapitel 4.

---

## 1. Ausgangslage dieser Session
- Methodikteil als abgeschlossen markiert; Übergang in die inhaltliche Konstruktion von Kapitel 4 (RQ1) und Kapitel 5 (RQ2).
- Ziel: Eine konsistente Ableitungslogik von regulatorischen Anforderungen (EU AI Act Art. 9–15) zu technisch durchsetzbaren Quality Gates und zur Referenzarchitektur.

---

## 2. Entscheidungsraum: Strukturierung von RQ1 / Kapitel 4

### 2.1 Optionen
**Option A – Regulatorisch → Technisch → Strategisch**
- Pro: Sehr nachvollziehbar; entspricht der Wortwahl der RQ1-Formulierung.
- Contra: Silo-Struktur; nicht „gate-/lifecycle-nativ“; Traceability muss nachträglich ergänzt werden.

**Option B – Lifecycle-basiert**
- Pro: Direkte Gate-Ableitung; passt zu CI/CD, Enforcement und PoC-Story.
- Contra: EU AI Act ist nicht lifecycle-strukturiert; Mapping-Aufwand nötig.

**Option C – Governance-/Risikodimensionen**
- Pro: Nahe am EU AI Act; gut für Expertenreview und Coverage.
- Contra: Architektur- und Gate-Ableitung indirekter; Lifecycle-Mapping wird zweite Schleife.

### 2.2 Entscheidung
Keine „reine“ Option erfüllt gleichzeitig Relevance (AI Act), Design (Gates), Rigor (Fundierung) und PoC-Kohärenz → **Hybridansatz** wird erforderlich.

---

## 3. Strategische Zielklärung: Praxisprofil vs. Promotionsfähigkeit
- Praxis/Architekturperspektive: Lifecycle + Pipeline + Gates als dominante Ontologie.
- Forschung/Promotion: Governance-Dimensionen + Abstraktion + strukturierte Design Knowledge.

**Entscheidung:** Promotionsfähige Ausrichtung → Hybridmodell mit explizitem Mapping.

---

## 4. Hybridmodell – Definition und Begründung

### MD1 – Hybridstruktur der Anforderungsableitung
**Entscheidung:** Lifecycle-first als operative Primärstruktur; Governance-Dimensionen als konsolidierende Sekundärstruktur; explizites Mapping zwischen beiden Ebenen.  
**Begründung:** Lifecycle-first ist gate-kompatibel; Governance-Dimensionen sichern Relevance/Rigor und vereinfachen Coverage/Expert Review.  
**Implikation:** Requirements werden so formalisiert, dass sie sowohl lifecycle- als auch governance-zugeordnet sind.

---

## 5. Primär-/Sekundärrahmen: EU AI Act vs. NIST

### 5.1 Optionen
- A: EU AI Act als alleinige Struktur (artikelgetrieben)
- B: NIST AI RMF als Primärstruktur (framework-getrieben)
- C: EU AI Act primär, NIST sekundär (Harmonisierung)

### MD2 – Normative Primärquelle
**Entscheidung:** EU AI Act Art. 9–15 ist primärer Problemraum (Relevance).  
**Begründung:** Arbeitstitel/Exposé setzen AI Act als zentralen regulatorischen Referenzrahmen.  
**Scope:** Keine Erweiterung auf vollständigen AI Act.

### MD3 – Rigor-Harmonisierung durch NIST AI RMF
**Entscheidung:** NIST AI RMF dient ausschließlich als strukturierende Harmonisierungsebene, nicht als Primärstruktur.  
**Begründung:** Vermeidet framework-getriebene Verzerrung; stärkt Rigor ohne Primäranker zu verschieben.

### MD4 – Reihenfolge: Erst AI Act analysieren, dann NIST harmonisieren
**Entscheidung:** Zuerst AI Act extrahieren/transformieren, anschließend NIST als Filter zur Harmonisierung.  
**Begründung:** Wahrung des Relevance-Cycle-Primats; Vermeidung eines NIST-getriebenen Artefakts.

---

## 6. Operationalisierungslogik: juristisch vs. funktional

### 6.1 Optionen
- A: Juristische Einzelanalyse (Artikel-Kommentar)
- B: Funktionale Transformation in technisch prüfbare Controls

### MD5 – Funktionale Transformation statt juristische Kommentierung
**Entscheidung:** Anforderungen werden funktional in technisch prüfbare Kontrollmechanismen transformiert.  
**Begründung:** Artefakt ist ein Quality-Gate-Kontrollsystem; Zweck ist Durchsetzung/Evidence, nicht Rechtskommentar.

---

## 7. Transformationsstrategie: artikelweise vs. erst transformieren, dann clustern

### 7.1 Optionen
- 1: Artikel nacheinander transformieren
- 2: Alle Artikel zerlegen → transformieren → clustern

### MD6 – Clustering-Strategie
**Entscheidung:** Zuerst vollständige Transformation in Kontrollmechanismen, danach Clustering.  
**Begründung:** Vermeidet artikelgetriebene Silo-Struktur; erzeugt konsolidierte Architektur-ableitbare Struktur.

---

## 8. Granularität: kleinste Einheit der Ableitung

### 8.1 Optionen
- A: Jede normative Aussage (zu granular)
- B: Funktionsgruppen (zu grob)
- C: Kontrollmechanismus (gate-fähig)

### MD7 – Granularität: Kontrollmechanismus-Level
**Entscheidung:** Kleinste Einheit ist der technisch prüfbare Kontrollmechanismus.  
**Begründung:** Gates prüfen Mechanismen, nicht Paragraphen; erhöht Operationalisierbarkeit.

---

## 9. Lifecycle-first Ableitung und Lifecycle-Granularität

### MD8 – Lifecycle-first Ableitung von Kontrollmechanismen
**Entscheidung:** Kontrollmechanismen werden primär entlang des Lifecycles abgeleitet; AI-Act-Referenz und Governance-Dimension als Attribute.  
**Begründung:** Maximale Gate- und PoC-Kohärenz; Enforcement-Logik wird direkt abbildbar.

### 9.1 Optionen Lifecycle-Granularität
- A: 5-Phasen-Modell (feiner, aber PoC/Evaluation-Risiko)
- B: 3-Phasen-Modell (scope-stabil)

### MD9 – 3-Phasen-Lifecycle-Modell
**Entscheidung:** Drei Phasen: Pre-Deployment, Deployment, Operation (Inference + Monitoring).  
**Begründung:** Entspricht Exposé-Scope (Deployment & Inference), bleibt PoC-kohärent und vermeidet Scope-Expansion.  
**Hinweis:** Staging/Post-Deployment werden innerhalb „Deployment“ modelliert (als Übergänge/Promotion-Schritte).

---

## 10. Artefaktbeginn und Kapitel-Identität

### 10.1 Optionen Artefaktbeginn
- A: Artefakt beginnt erst in Kapitel 5 (Architektur)
- B: Artefakt beginnt bereits in Kapitel 4 (Transformation/Mechanismen)

### MD10 – Artefaktbeginn bei Kontrollmechanismen
**Entscheidung:** Artefakt beginnt bereits bei der funktionalen Transformation in lifecycle-verortete Kontrollmechanismen.  
**Begründung:** Transformation erzeugt preskriptives Designwissen (Method-Anteil des Artefakts).

### MD11 – Kapitel 4 als Artefaktkonstruktion I
**Entscheidung:** Kapitel 4 wird explizit als Teil der Artefaktkonstruktion positioniert (Design Cycle – Phase 1).  
**Titel:** „Design-getriebene Operationalisierung regulatorischer Anforderungen“.

---

## 11. Blueprint-Entscheidung (1-Seiter) + DSR-Zyklen + Übergang zu Kapitel 5

### MD12 – Integrierter Blueprint über Kapitel 4 und 5
**Entscheidung:** Ein horizontaler Blueprint bildet die Ableitungslogik von Kapitel 4 bis Kapitel 5 ab und wird mit Hevner-Zyklen (Relevance, Design, Rigor) überlagert.  
**Blueprint-Kette:**  
EU AI Act (Art. 9–15) → funktionale Transformation → Kontrollmechanismen → Lifecycle-Zuordnung (3 Phasen) → Governance-Konsolidierung (NIST harmonisiert) → Requirements-Katalog → Design-Prinzipien → Quality Gates → Referenzarchitektur → PoC

---

## 12. Deltas zu Exposé und Methodik (später anzupassen)

### 12.1 Delta im Exposé: Lifecycle/PoC
- Exposé-Pfad: „Model Registry → Pre-Deployment Gate → Staging → Post-Deployment Gate → Production“  
- Neues Lifecycle-Kernmodell: „Pre-Deployment / Deployment / Operation“  
**Anpassung:** Klarstellen, dass Staging und Post-Deployment Gate innerhalb der Phase „Deployment“ verortet sind; Production entspricht „Operation“.

### 12.2 Delta in Methodik/Kapitel 3
**Anpassungen:**
1) Explizit machen, dass Kapitel 4 bereits Artefaktkonstruktion ist (Artefaktbeginn bei Kontrollmechanismen).  
2) Lifecycle-Modell konsistent als 3-Phasen referenzieren.  
3) Terminologie konsistent halten (regulatorisch/technisch/strategisch; „normativ“ nicht als Leitbegriff).

---

## 13. Scope-Guardrails und Qualitätsfaktoren (Kapitel 4)

### MD13 – Scope-Guardrails
**Bindend:**
- Fokus Art. 9–15  
- Fokus Deployment & Inference/Operation  
- Kein Training Lifecycle / Fine-Tuning / Data Engineering  
- Keine neue Governance-Theorie  
- Keine juristische Vollauslegung

### MD14 – Schreib-Disziplin
**Regel:** Struktur vor Umfang. Pro Block: Ziel, Logik, Output. Keine „10 Seiten pro Element“.  

### Qualitätsfaktoren für ein starkes Kapitel 4
- Transformationsregeln (Template) explizit halten (Trigger/Kriterium/Evidence/Owner).  
- Jeder Kontrollmechanismus muss lifecycle-verortet sein.  
- NIST nur zur Harmonisierung, nicht zum Aufbau.  
- Output-orientiert enden: Requirements-Katalog als Input für Kapitel 5 (R → DP → Gate → Evidence).

---

# Mini-Checkliste (Schreibstart Kapitel 4)

## 4.1 Zielbild des Kontrollsystems
- Enforcement vs. Dokumentation klar?
- Accountability-by-Design greifbar?
- Bezug zum Lifecycle sichtbar?

## 4.2 Lifecycle-Modell
- Drei Phasen klar abgegrenzt?
- Mapping des PoC-Pfads (Staging/Post-Deploy innerhalb Deployment) erklärt?
- Scope stabil?

## 4.3 Transformationsmethodik
- Kein juristischer Kommentar
- Norm → Kontrollmechanismus (technisch prüfbar)
- Gate-Fähigkeit (Trigger/Kriterium/Evidence/Owner) erkennbar?

## 4.4 Kontrollmechanismen & 4.5 Konsolidierung
- Lifecycle-Zuordnung vollständig?
- Clustering nachvollziehbar?
- NIST-Harmonisierung plausibel, nicht dominierend?

## 4.6 Requirements-Katalog
- R-ID, Lifecycle, Governance, AI-Act-Ref, Kontrollmechanismus vorhanden?
- Klarer Übergang zu Kapitel 5?
