---
name: thesis-consistency
description: >
  Übergreifender Konsistenz-Check für die gesamte Masterarbeit. Scannt alle chapter_states,
  DRAFT-Dateien und Entscheidungsregister auf Widersprüche, Terminologie-Inkonsistenzen,
  Budget-Überschreitungen, tote Forward-References und Exposé-Drift.
  Trigger bei: "konsistenz prüfen", "cross-check", "terminologie check", "widersprüche finden",
  "alles konsistent?", "budget check", "gesamtübersicht", "forward references prüfen",
  "drift check", "ist alles stimmig", "kapitelübergreifend prüfen".
  Auch triggern wenn der User nach einem größeren Schreibblock (mehrere Abschnitte/Kapitel)
  eine Gesamtprüfung machen will oder vor einem Review-Meilenstein steht.
---

# Thesis Consistency Check — Kapitelübergreifende Qualitätssicherung

Dieser Skill deckt Inkonsistenzen auf, die innerhalb eines einzelnen Kapitels unsichtbar
bleiben: unterschiedliche Begriffe für dasselbe Konzept, widersprüchliche Designentscheidungen
zwischen Kapiteln, Seitenbudget-Überschreitungen, und Verweise ins Leere. Je mehr Kapitel
geschrieben sind, desto wichtiger wird dieser Check.

## Wann diesen Skill nutzen

- Nach Abschluss eines Kapitels (bevor das nächste beginnt)
- Vor Review-Meilensteinen (Betreuer-Feedback, Peer-Review)
- Wenn Unsicherheit besteht ob eine Entscheidung andere Kapitel betrifft
- Auf explizite Anfrage ("ist alles stimmig?")

## Die 6 Konsistenz-Dimensionen

### K1 — Terminologie-Konsistenz

Lade die Critical Definitions aus `docs/thesis_state.md` und prüfe alle Volltexte
(`00_workspace/Fulltext_Kapitel/*.docx`) sowie DRAFT-Dateien (Fallback):

**Pflicht-Prüfungen:**
- "Quality Gate" = automatisierter, evidenzbasierter Kontrollpunkt (nicht nur Dokumentation)
- "Enforcement" ≠ "Dokumentation" — werden diese Begriffe korrekt unterschieden?
- "Referenzarchitektur" = Enterprise-tauglich, cloud-native, CI/CD/CT-integriert
- Deployer-Scope (Art. 26) konsistent — nirgends Provider-Perspektive (Art. 16)?
- Retirement-Phase nirgends behandelt?

**Vorgehen:**
1. `docs/thesis_state.md` lesen → Critical Definitions extrahieren
2. Alle `Kap*_DRAFT.md` Dateien scannen
3. Für jeden Critical-Definition-Begriff: Wird er überall gleich verwendet?
4. Abweichungen als Tabelle ausgeben

**Ausgabe:**
```
| Begriff | Definition (SOT) | Kap. | Verwendung im Text | Status |
|---------|-------------------|------|-------------------|--------|
| Quality Gate | automatisiert, evidenzbasiert | 3.2 | "dokumentarischer Kontrollpunkt" | ⚠ Abweichung |
```

### K2 — Entscheidungs-Kohärenz

Prüfe ob Entscheidungen (D_xxx) über Kapitel hinweg konsistent sind:

1. `docs/thesis_state.md` → Alle D_xxx Entscheidungen laden
2. `docs/ENTSCHEIDUNGSPAPIER_KAP4.md` → Kap. 4-spezifische Decisions
3. `docs/SSOT_ROTER_FADEN_ANALYSE.md` → Cross-chapter Impacts
4. Alle `chapter_state.yaml` → `decisions` Feld prüfen

**Prüfungen:**
- Gibt es D_xxx die in mehreren Kapiteln referenziert werden mit unterschiedlicher Interpretation?
- Gibt es widersprüchliche Decisions (z.B. D_4.6 vs. D_5.3)?
- Sind alle Decisions die ein Kapitel betreffen auch in dessen chapter_state dokumentiert?
- Gibt es "verwaiste" Decisions (in thesis_state aber in keinem Kapitel referenziert)?

### K3 — Seitenbudget-Aggregation

Berechne die Gesamtseitenrechnung über alle Kapitel:

1. `00_admin/gliederung_v3.md` → Budget pro Kapitel (SOLL)
2. Alle DRAFT-Dateien → Wortanzahl pro Kapitel (IST)
3. Umrechnung: 1 Seite ≈ 300 Wörter

**Ausgabe:**
```
| Kapitel | Budget (Seiten) | IST (Wörter) | IST (Seiten) | Delta | Status |
|---------|----------------|-------------|-------------|-------|--------|
| Kap. 1 | 3 | 2.075 | ~6,9 | +3,9 | ⚠ Über Budget |
| Kap. 2 | 15 | 0 | 0 | -15 | ⬜ Nicht begonnen |
| GESAMT | 80 | ... | ... | ... | ... |
```

Warnung bei >10% Überschreitung pro Kapitel und bei Gesamtüberschreitung.

### K4 — Forward-Reference-Validation

Finde alle Querverweise in allen DRAFT-Dateien und prüfe ob die Ziele existieren:

**Muster suchen:**
- `(vgl. Kap. X.Y)` oder `(siehe Kap. X.Y)`
- `(vgl. Abschnitt X.Y)` oder `(s. Abschnitt X.Y)`
- Verweise auf Tabellen, Abbildungen, Anhänge

**Für jede Referenz prüfen:**
- Existiert der Zielabschnitt in der Gliederung (`gliederung_v3.md`)?
- Existiert bereits ein DRAFT dafür?
- Wenn nicht: Ist er als "geplant" in einem chapter_state markiert?

**Ausgabe:**
```
| Quelle | Verweis auf | Ziel existiert? | Status |
|--------|-----------|----------------|--------|
| Kap. 1.3, Abs. 2 | Kap. 4.2 | ✅ DRAFT vorhanden | OK |
| Kap. 3.1, Abs. 5 | Kap. 7.3 | ⬜ Geplant (chapter_state) | Warnung |
| Kap. 4.1, Abs. 3 | Kap. 5.4 | ❌ Nicht in Gliederung | Fehler |
```

### K5 — Exposé-Drift-Monitor

Vergleiche den aktuellen Stand der Arbeit mit dem Exposé:

1. `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf` → Geplanter Umfang/Struktur
2. optional lokal: `00_admin/Expose_v4_final_2026-02-28.docx` (Arbeitskopie)
3. `00_admin/gliederung_v3.md` → Aktuelle Struktur
4. Alle bisherigen Kapitel → Tatsächlicher Inhalt

**Prüfungen:**
- Kapitelstruktur: Stimmt die Gliederung noch mit dem Exposé überein?
- Forschungsfragen: Werden RQ1 und RQ2 wie im Exposé adressiert?
- Methodischer Rahmen: DSR wie im Exposé beschrieben?
- Scope: Wurde der Scope erweitert oder eingeschränkt?

**Kumulative Drift-Tabelle:**
```
| Aspekt | Exposé | Aktuell | Drift | Dokumentiert? |
|--------|--------|---------|-------|---------------|
| Scope | Deployer + Provider | Nur Deployer | Einschränkung | ✅ D_xxx |
```

Jede undokumentierte Abweichung erzeugt eine Warnung mit Empfehlung, eine Decision (D_xxx) anzulegen.

### K6 — DSR-Kohärenz

Prüfe ob der Design-Science-Research-Rahmen konsistent durchgehalten wird:

- Werden Hevner (2004), Peffers et al. (2007) und vom Brocke et al. (2020) konsistent zitiert?
- Ist jedes Kapitel korrekt einer DSR-Phase zugeordnet?
- Stimmen die Rigor-Cycle-Referenzen (Wissensbasis) mit den tatsächlichen Quellen überein?
- Relevance-Cycle: Ist die Praxisrelevanz in jedem Kapitel erkennbar?

---

## Ausgabeformat: Konsistenz-Report

```markdown
## Konsistenz-Report: [Datum]

### K1 Terminologie: [✅ konsistent / ⚠ X Abweichungen]
[Tabelle mit Abweichungen]

### K2 Entscheidungen: [✅ kohärent / ⚠ X Konflikte]
[Tabelle mit Konflikten]

### K3 Seitenbudget: [✅ im Rahmen / ⚠ X Kapitel über Budget]
[Budget-Tabelle]

### K4 Forward-References: [✅ alle valide / ❌ X tote Verweise]
[Referenz-Tabelle]

### K5 Exposé-Drift: [✅ kein neuer Drift / ⚠ X Abweichungen]
[Drift-Tabelle]

### K6 DSR-Kohärenz: [✅ konsistent / ⚠ Issues]
[Findings]

### Zusammenfassung:
- Kritische Issues (sofort beheben): ...
- Warnungen (vor nächstem Kapitel klären): ...
- Empfehlungen (bei Gelegenheit): ...
```

---

### K7 — Stil- und Formalia-Compliance (Uni-Vorgaben)

Lade den Pruefkatalog aus `docs/uni_vorgaben/pruefkatalog.md` und pruefe alle Volltexte:

1. Alle Volltexte in `00_workspace/Fulltext_Kapitel/*.docx` scannen nach:
   - Verbotene Formulierungen (PK-V1 bis PK-V6)
   - Gliederungstiefe max. 4 Ebenen (PK-F2)
   - Zitationsdichte pro Absatz (PK-Z3)
2. Gesamt-Seitenbudget aggregieren: 60–80 Textseiten (PK-F3)
3. SRH 50/30/20 Bewertungskriterien-Alignment pruefen

**Ausgabe:**
```
| Kapitel | Verbotene Formulierungen | Gliederungstiefe | Zitationsdichte | Seitenbudget | Status |
|---------|-------------------------|-----------------|----------------|-------------|--------|
```

---

## Zusaetzliche Regeln

- Dieser Skill produziert KEINEN Fliesstext — nur den Konsistenz-Report
- **Primaeres Pruefobjekt:** Volltexte in `00_workspace/Fulltext_Kapitel/*.docx`
- Fallback: `Kap*_DRAFT.md` Dateien
- SOT-Hierarchie beachten: `gliederung_v3.md > Kap. 3 > Kap. 4 > Entscheidungsregister > Expose`
- Bei Widerspruechen: hoeherrangige Quelle gewinnt, Abweichung dokumentieren
- Roter Faden pruefen via `docs/roter_faden_tracker.md`
- Report speichern als `docs/consistency/CONSISTENCY_REPORT_[DATUM].md`
