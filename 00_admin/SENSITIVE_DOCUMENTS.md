# Sensible Dokumente — Uebersicht & Workflow

> Letzte Aktualisierung: 2026-03-03

## Status-Uebersicht

### Verschluesselt im Repo (oeffentlich sichtbar, passwortgeschuetzt)

| Datei | Verschluesselung | Passwort bei |
|-------|-----------------|--------------|
| `docs/expose/Expose_v4_final_2026-02-28_encrypted.pdf` | AES-256 (qpdf) | Mustafa Demir |

### Aus Git entfernt, lokal vorhanden

Diese Dateien liegen nur auf deinem Rechner unter `docs/expose/legacy/`.
Sie sind per `.gitignore` geschuetzt und werden nicht mehr ins Repo gepusht.

| Datei | Typ | Ursprung |
|-------|-----|----------|
| `1. Expose .docx` | DOCX | Initiales Expose |
| `Expose_v3_2026-02-28.docx` | DOCX | Expose v3 |
| `Expose_v3_delta_2026-02-28.docx` | DOCX | Expose v3 Delta |
| `Expose_v3_final_2026-02-28.docx` | DOCX | Expose v3 Final |
| `Expose_v3_single_source_2026-02-25.txt` | TXT | Expose v3 Plaintext |
| `Expose_v3_single_source_2026-02-27.pdf` | PDF | Expose v3 PDF |
| `Expose_v3_single_source_2026-02-27.txt` | TXT | Expose v3 Plaintext |

### Aus Git-History bereinigt

| Datei | Grund |
|-------|-------|
| `docs/expose/Expose_v4_final_2026-02-28.pdf` | Unverschluesseltes Original — AUSSTEHEND |
| `docs/expose/legacy/*` | Alle Legacy-Expose-Dateien — AUSSTEHEND |

> **Hinweis:** Die Git-History-Bereinigung steht noch aus (siehe Abschnitt unten).

### .gitignore-Regeln fuer sensible Dokumente

```
# Sensible Dokumente (unverschluesselte Originale)
docs/expose/*.pdf
!docs/expose/*_encrypted.pdf
docs/expose/legacy/
```

---

## Workflow: Neue sensible PDF ins Repo hochladen

### Schritt 1 — PDF verschluesseln

```bash
qpdf --encrypt "DEIN_PASSWORT" "DEIN_PASSWORT" 256 -- \
  original.pdf \
  original_encrypted.pdf
```

- `256` = AES-256-Verschluesselung
- Beide Passwort-Argumente: erstes = User-Passwort, zweites = Owner-Passwort

### Schritt 2 — Dateiname-Konvention

```
[Name]_[Version]_[Datum]_encrypted.pdf
```

Beispiel: `Expose_v4_final_2026-02-28_encrypted.pdf`

**Wichtig:** Der Dateiname MUSS auf `_encrypted.pdf` enden, damit die `.gitignore`-Regel greift.

### Schritt 3 — Nur die verschluesselte Version committen

```bash
git add pfad/zur/datei_encrypted.pdf
git commit -m "docs: [Beschreibung] verschluesselt hinzufuegen"
git push
```

### Schritt 4 — Original lokal aufbewahren

Das unverschluesselte Original bleibt auf deinem Rechner.
Es wird durch `.gitignore` automatisch ignoriert, solange es NICHT auf `_encrypted.pdf` endet.

### Schritt 5 — Diese Liste aktualisieren

Trage die neue Datei oben in die Tabelle "Verschluesselt im Repo" ein.

---

## Workflow: Sensibles Dokument an jemanden weitergeben

1. Person laedt die `*_encrypted.pdf` aus dem GitHub-Repo herunter
2. Person kontaktiert dich fuer das Passwort
3. Passwort ueber sicheren Kanal senden (persoenlich, Signal, NICHT per E-Mail)

---

## Noch ausstehend

- [ ] Git-History bereinigen: `git filter-repo` ausfuehren um unverschluesselte Expose-Versionen aus der gesamten History zu entfernen
- [ ] Danach: Force-Push auf `origin/main`
- [ ] Alle Collaborators muessen ihr lokales Repo neu klonen
