# Uni-Vorgaben — Workflow-Integration (D_UNI_HINWEISE_SSOT)

> **Decision:** D_UNI_HINWEISE_SSOT (registriert 2026-03-07 in Kap. 3 chapter_state)
> **Gilt fuer:** Alle Kapitel, alle Workflow-Skills

## Bindende Dokumente

1. **Prof. Prinz Stilrichtlinien** — `DRAFT_Hinweise für wissenschaftliche Veröffentlichungen und Abschlussarbeiten.docx`
2. **SRH Masterarbeit_Vorbereitung** — `Masterarbeit_Vorbereitung.pdf`

---

## Skill-spezifische Pruefpunkte

### Preflight (P6-Erweiterung)

Zusaetzlich zu den bestehenden P6-Checks MUESSEN folgende Punkte geprueft werden:

**Prof. Prinz Stilregeln (bindend):**
- ☐ Hohe Referenzierdichte geplant — jede Behauptung durch Quelle belegbar?
- ☐ Auf Wesentliches reduziert — keine unnötigen Ausfuehrungen/Hintergrundexkurse?
- ☐ Keine formalen Ueberleitungen geplant ("Im Folgenden wird...", "Abschliessend sei...", "Wie bereits erwaehnt...")
- ☐ Ergebnisse durch Vergleich/Abgrenzung kontextualisiert (nicht isoliert dargestellt)?
- ☐ Keine Redundanz zu anderen Kapiteln — was ist NEU in diesem Abschnitt?
- ☐ Blablameter-Verdacht: Gibt es Passagen die nur Fuelltext sind?

**SRH Bewertungskriterien (Optimierung auf 50/30/20):**
- ☐ Inhalt (50%): Problemdurchdringung, Ergebnisniveau, logischer Aufbau adressiert?
- ☐ Methodik (30%): DSR-Phase klar, Vorgehensweise transparent?
- ☐ Formalia (20%): APA7, Gliederungstiefe max. 4 Ebenen, Zitationsdichte?

**SRH Strukturvorgaben:**
- ☐ Einleitung ~10% des Gesamtumfangs (6-8 Seiten bei 60-80 Textseiten)
- ☐ Gliederung maximal 4 Ebenen tief (z.B. 2.4.1 OK, 2.4.1.1 NICHT)
- ☐ 60-80 Textseiten Gesamtbudget eingehalten?

### Writer (Negativ-Checklist-Erweiterung)

Bei JEDEM Absatz zusaetzlich pruefen:

**Stil-Verbote (Prof. Prinz):**
- ❌ "Im Folgenden wird..." / "Nachfolgend..." / "Abschliessend..."
- ❌ "Es ist allgemein bekannt, dass..." / "Bekanntlich..."
- ❌ Redundante Wiederholungen aus vorherigen Abschnitten
- ❌ Unnoetiger Hintergrund der nicht direkt zur Argumentation beitraegt
- ❌ Passive Formulierungen ohne klaren Akteur
- ❌ Floskelhafte Wendungen (Blablameter > 0.3 → ueberarbeiten)

**Stil-Gebote (Prof. Prinz):**
- ✅ Jeder Absatz traegt zur Argumentation bei (kein Fuelltext)
- ✅ Ergebnisse/Definitionen durch Abgrenzung/Vergleich kontextualisieren
- ✅ Komprimiert schreiben — auf das Wesentliche reduzieren
- ✅ Bei Definitionen: erst Quelle, dann eigene Einordnung/Abgrenzung

### Consistency (K7-Erweiterung: Stil-Compliance)

Neue Konsistenz-Dimension K7:

**K7 — Stil- und Formalia-Compliance:**
1. Alle DRAFT-Dateien scannen nach verbotenen Formulierungen (s. Writer Stil-Verbote)
2. Gliederungstiefe pruefen: max. 4 Ebenen in allen Kapiteln
3. Gesamt-Seitenbudget aggregieren: 60-80 Textseiten
4. Bewertungskriterien-Alignment: Inhalt (50%) > Methodik (30%) > Formalia (20%)
5. Zitationsdichte pro Kapitel: Mindestens 1 Zitation pro Absatz (Ausnahme: Strukturabsaetze)

**Ausgabe:**
```
| Kapitel | Verbotene Formulierungen | Gliederungstiefe | Zitationsdichte | Status |
|---------|-------------------------|-----------------|----------------|--------|
```

### Post-Session (G-Erweiterung: Stil-Check)

Neuer Pruefpunkt G — Stil-Compliance:

**G — Uni-Vorgaben-Compliance:**
- ☐ Keine verbotenen Formulierungen in neuen Absaetzen?
- ☐ Zitationsdichte ausreichend (mind. 1/Absatz)?
- ☐ Kein Blablameter-Verdacht in neuen Passagen?
- ☐ Gliederungstiefe eingehalten (max. 4 Ebenen)?
- ☐ Seitenbudget-Delta mit SRH 60-80 Seiten kompatibel?

---

## Verweise

- Decision: `D_UNI_HINWEISE_SSOT` in `03_forschungsdesign_methodik/chapter_state.yaml`
- SSOT-Referenz: `00_admin/SOURCE_OF_TRUTH.md` → Abschnitt "Universitaere Vorgaben und Stilrichtlinien"
- Gilt fuer: Alle Kapitel 1-8
