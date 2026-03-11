# Workflow-Improvement: Entscheidungsregister in Preflight P4

**Datum:** 2026-03-11
**Anlass:** Bei Preflight Kap. 5 wurden 8 Architektur-Decisions (R1–R8) entdeckt, die NUR in `.memory/entscheidungsregister.md` standen und in keinem chapter_state dokumentiert waren.

## Problem

Der thesis-preflight Skill (P4) listet explizit:
- `docs/thesis_state.md`
- `docs/SSOT_ROTER_FADEN_ANALYSE.md`
- `docs/ENTSCHEIDUNGSPAPIER_KAP4.md` ← nur Kap. 4!
- `00_admin/SOURCE_OF_TRUTH.md`

**Fehlt:** `.memory/entscheidungsregister.md` und generalisierte Referenz auf ALLE Entscheidungspapiere.

## Konkrete Auswirkung

Ohne manuellen Check wären R1–R8 (Diagramm-Vorgaben, 3-Quellen-Verifikation, Payload/Telemetrie-Trennung, DP4 als Prüfdimensionen, Make-or-Buy-Ausschluss, 3D-Taxonomie, Cloud-agnostisch, CDV-Framework) verloren gegangen.

## Empfohlene Änderung im thesis-preflight SKILL.md

### P4 — Erweiterte Dateiliste:
```
- `docs/ENTSCHEIDUNGSPAPIER_KAP*.md` — ALLE Entscheidungspapiere (Glob)
- `.memory/entscheidungsregister.md` — PFLICHT: Zentrales Register
```

### P4 — Neue Prüffrage:
```
- Gibt es im Entscheidungsregister (.memory/) Decisions die in keinem chapter_state stehen? → Übernehmen!
```

### P4 — Decision-Precedence-Regel:
```
Kap. N chapter_state > Kap. N-1 > ... > Kap. 1 > .memory/entscheidungsregister.md
Neueste Decision gewinnt. Aber: Decisions die NUR im Register stehen und nirgends widerrufen wurden, bleiben gültig.
```

## Umsetzung

Das Plugin-Verzeichnis ist read-only. Optionen:
1. **Plugin-Customizer nutzen** (Skill `cowork-plugin-management:cowork-plugin-customizer`)
2. **Plugin neu bauen** mit geändertem SKILL.md
3. **Manuell:** Beim nächsten Preflight daran denken, `.memory/entscheidungsregister.md` explizit zu lesen

→ **Empfehlung:** Option 1 (Plugin-Customizer) bei nächster Gelegenheit.
