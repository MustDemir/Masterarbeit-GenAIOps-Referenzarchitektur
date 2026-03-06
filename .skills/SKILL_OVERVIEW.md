# Thesis-Writing Skills — Übersicht

> Erstellt: 2026-03-06 | Status: v1.0 — bereit für Live-Test

## Architektur

```
Session Start → thesis-session-manager (S1–S5)
                  ↓
              thesis-preflight (P1–P6)
                  ↓ User: "GO"
              thesis-writer (Absatz für Absatz)
                  ↓ User: "fertig"
              thesis-post-session (A–F)
                  ↓
Session Ende → thesis-session-manager (E1–E4)

Bei Bedarf:  → thesis-consistency (K1–K6)
```

## 5 Skills im Detail

| # | Skill | Trigger | Zeilen | References | Evals |
|---|-------|---------|--------|-----------|-------|
| 1 | **thesis-preflight** | "preflight", "kap X.Y schreiben", "prüf erstmal" | 172 | checklist_template.md, critical_definitions.md | 3 |
| 2 | **thesis-writer** | "GO", "FINAL", "schreib absatz", "weiter schreiben" | 142 | pruefprotokoll_format.md, apa7_rules.md | 2 |
| 3 | **thesis-post-session** | "session ende", "fertig für heute", "save session" | 144 | post_session_template.md | 2 |
| 4 | **thesis-consistency** | "konsistenz prüfen", "cross-check", "terminologie check" | 181 | terminology_register.md | — |
| 5 | **thesis-session-manager** | "neue session", "wo waren wir", "resume" | 185 | — | — |

## Standort

Alle Skills liegen in: `genaiops-thesis/.skills/`

## Nächste Schritte

1. **Live-Test bei nächster Schreib-Session** — Kap. 2 Preflight triggern
2. **Iteration nach Feedback** — Skills basierend auf Erfahrung verbessern
3. **Optional:** Description-Optimization für besseres Triggering
4. **Optional:** Scripts für deterministische Checks (Wortanzahl, Forward-Refs)
