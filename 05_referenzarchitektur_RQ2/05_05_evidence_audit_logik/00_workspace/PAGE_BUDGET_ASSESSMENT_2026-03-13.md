# Page Budget Assessment für Kap. 5.4 + 5.5

**Stand:** 2026-03-13  
**Basis:** chapter_state.yaml (kap5_current: 15.2 pages)

---

## 📊 **Aktueller Status Kap. 5**

| Kapitel | Titel | Pages | Status | Wörter (ca.) |
|---|---|---|---|---|
| **5.1** | Architekturueberblick & DP1-DP5 | 3.3 | ✅ DONE | 980W |
| **5.2** | Gate-Spezifikation (R-xx → G-xx Mapping) | 7.3 | ✅ DONE | 2200W |
| **5.3** | Policy-Engine & CAC/AAC Differenzierung | 4.6 | ✅ DONE | 1380W |
| **5.4** | Evidence Store & Audit Logik | **?** | 📋 PREFLIGHT | ? |
| **5.5** | Monitoring & Post-Market Surveillance | **?** | 📋 PLANNED | ? |
| **5.6** | Prototypische Instanziierung (PoC) | **?** | 📋 PLANNED | ? |
| **SUMME Kap. 5.1–5.3** | | **15.2** | | **4560W** |
| **BUDGET Kap. 5 (Gesamt)** | | **15–18** | | **~4500–5400W** |

---

## ⚠️ **Kritisches Befund: Bereits am Limit**

**Aktueller Stand:** 15.2 / 15–18 = 101.3% des unteren Limits erreicht

**Verbleibender Budget:**
- **Szenario A (Ziel-Untergrenze 15 S.):** 15.0 − 15.2 = **−0.2 Seiten** ❌ ÜBERSCHUSS
- **Szenario B (Ziel-Obergrenze 18 S.):** 18.0 − 15.2 = **+2.8 Seiten** ✅ REALISTISCH

**Interpretation:** 
- Wenn Budget-Ziel ist **Obergrenze (18 S.):** Maximal 2–3 Seiten für 5.4+5.5+5.6
- Wenn Budget-Ziel ist **Untergrenze (15 S.):** Kap. 5 ist bereits **komplett voll**

---

## 🎯 **Szenarien für 5 Seiten (Nutzer-Frage: "Reicht 5 Seiten?")**

### **Interpretation 1: "Sind 5 Seiten für Kap. 5.4+5.5+5.6 realistisch?"**

**Szenario:** Nutzer fragt, ob die restlichen 3 Kapitel in 5 Seiten passen

| Kapitel | Inhalt | Empfohlene Seiten | 5S-Aufteilung |
|---|---|---|---|
| **5.4** | Evidence Store Schema (DSR Artifact) | 1.5–2 | 1.5–2 |
| **5.5** | Hash-Chain & Immutability (Sub-Extensions) | 1–1.5 | 1 |
| **5.6** | PoC-Instanziierung (Code Snippets) | 2–2.5 | 1.5 |
| **TOTAL** | | 4.5–6 | **4.0** |

**Ergebnis:** 5 Seiten ist **KNAPP, aber MACHBAR** wenn:
- 5.4 auf 1.5 Seiten komprimiert (DSR Artifact ohne extensiven Text)
- 5.5 auf 1 Seite konzentriert (Hash-Chain als Sub-Extension erwähnen, nicht vertiefen)
- 5.6 auf 1.5 Seiten beschränkt (nur essenzielle Code-Beispiele, kein PoC-Volltext)

**Risiko:** Sehr dicht, wenig Puffer für Reviews/Überarbeitungen

---

### **Interpretation 2: "Sind 5 Seiten FÜR KAP. 5.4 allein realistisch?"**

**Szenario:** Nutzer meint 5 Seiten NUR für Evidence Store + Audit Logik

| Komponente | Geplanter Umfang | 5S-Aufteilung |
|---|---|---|
| **Abs. 1** | Intro Evidence Store (Payload/Telemetrie) | 0.5 S |
| **Abs. 2** | Compliance-Lifecycle (DP1) + Privacy Views | 0.7 S |
| **Abs. 3** | CAC-Execution (Kholkar & Ahuja) + Triggers | 1.0 S |
| **Abs. 4** | Decision Logs (Butt Conformity Bundle) | 1.0 S |
| **Abs. 5** | Hash-Chain + Immutability (Sub-Extensions) | 1.2 S |
| **Abs. 6** | Payload/Telemetrie-Trennung + EU AI Act | 0.8 S |
| **Zusammenfassung** | Überleitung zu 5.5 | 0.3 S |
| **TOTAL** | | **5.5 S** |

**Ergebnis:** 5 Seiten reicht **GERADE NOCH**, aber sehr dicht

---

## 📋 **Empfehlte Lösung: Scope-Aufteilung**

Angesichts der Tatsache, dass Kap. 5.1–5.3 bereits 15.2 Seiten sind (Budget: 15–18), empfehle ich folgende Aufteilung:

### **Option A: KOMPAKT (4.0 S für 5.4+5.5+5.6)**

```
Kap. 5.4 (Evidence Store): 1.5 S
- DSR-Artifact (PostgreSQL Schema) prägnant
- Kholkar & Ahuja als Belegung für Policy-as-Code
- Immutability-Trigger als DP2/DP5.3-Operationalisierung

Kap. 5.5 (Audit Logik): 1.0 S
- Hash-Chain als Sub-Extension DP5.2 (kompakt erwähnen)
- Decision Logs als Audit-Trail-Persistierung

Kap. 5.6 (PoC): 1.5 S
- Azure K8s + Conftest/Gatekeeper Code-Snippets
- Datenbank-Schema Instantiierung (2-3 SQL-Blöcke)

Gesamtbudget: 4.0 S
Verbleibend im Budget (18 S): 2.8 S Puffer
```

**Vorteil:** Realistisch, mit Überarbeitungs-Puffer  
**Nachteil:** Weniger Tiefe in 5.4/5.5

---

### **Option B: MODERAT (5.0 S für 5.4+5.5)**

```
Kap. 5.4 (Evidence Store): 2.5 S
- DSR-Artifact mit PoC-Schema-Beispielen
- 4 technische Bausteine (Immutability, Privacy-Views, RBAC, Indexes)
- Kholkar & Ahuja + Pistilli als Quellen

Kap. 5.5 (Audit Logik): 2.5 S
- Hash-Chain + Immutability als differenzierte Sub-Extensions
- Decision Logs mit OSCAL-Referenzen
- EU AI Act Evidenz-Anforderungen (Kap. 1.6 Link)

Gesamtbudget: 5.0 S (nur 5.4+5.5, OHNE 5.6)
Verbleibend im Budget (18 S): 2.8 S für 5.6 + Puffer
```

**Vorteil:** Bessere Tiefe für Core-Topics  
**Nachteil:** 5.6 (PoC) wird gedrängt

---

## 🎯 **Meine Empfehlung für Deine Frage "Reicht 5 Seiten?"**

**JA, aber mit Qualifikation:**

1. **5 Seiten FÜR BEIDES (5.4+5.5):** ✅ **Machbar, aber dicht**
   - Komprimiere auf essenzielle Abs. (6 statt 8)
   - DSR-Artifact prägnant (PostgreSQL DDL + Belegung, nicht Erklär-Text)
   - Sub-Extensions (Hash-Chain, Immutability) als Stichpunkte, nicht ausformuliert

2. **5 Seiten FÜR 5.4 ALLEIN:** ✅ **Möglich, mit gutem Spielraum**
   - Erlaubt alle 6+ Absätze
   - Aufbau: Intro → Compliance-Lifecycle → CAC-Ausführung → Decision Logs → Sub-Extensions → Payload-Trennung

3. **Wenn Budget-Ziel ist "OBERGRENZE 18 S.":** ⚠️ **Nutze OPTION A oder B oben**
   - 4–5 S für 5.4+5.5 halten Puffer für 5.6 + Reviews

---

## 📍 **Kritische Abhängigkeiten**

### **Von Deinem GOAL abhängig:**

**A) "Ich will alle 6 Kapitel vollständig behandeln"**
→ OPTION A (4 S für 5.4+5.5+5.6) → "5 Seiten" ist zu viel

**B) "Ich fokussiere auf 5.4+5.5, PoC (5.6) optional"**
→ OPTION B (5 S für 5.4+5.5) → "5 Seiten" passt perfekt

**C) "Ich brauche Tiefe in Evidence/Audit, weniger in PoC"**
→ 5 S NUR für 5.4 → "5 Seiten" ist genau richtig

---

## ✅ **Nächste Schritte**

1. **Kläre Scope:** Welche Option passt zu Deinem Ziel?
2. **Aktualisiere chapter_state.yaml:** Setze Seitenbudgets für 5.4, 5.5, 5.6
3. **GO für Kap. 5.4-Schreiben:** Mit klarer Seitengrenze (z.B. 2.5 S)
4. **Post-Session-Check:** Kapa 5 gesamter Wordcount gegen Budget prüfen

---

**Kurzantwort auf "Reicht 5 Seiten?"**

✅ **JA, für 5.4+5.5 zusammen bei dichter Schreibweise**  
✅ **JA, für 5.4 allein bei ausführlicher Behandlung**  
⚠️ **MAYBE für 5.4+5.5+5.6 — dann eher 4 S empfohlen**

---

**Entscheidungsfrage an Dich:** Sollen wir mit Option A, B, oder C weitermachen?
