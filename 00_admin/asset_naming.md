# Asset Naming Standard (PNG) - Thesis

## Ziel
Einheitliche, versionierte Abbildungen fuer Thesis, GitHub und spaetere Nachvollziehbarkeit.

## Ordnerkonvention
- Kapitelweit: `0X_*/images/work` und `0X_*/images/final`
- Abschnittsnah (bei Bedarf): `0X_*/0X_YY_*/images/work` und `.../images/final`

## Dateinamen
Format:
`<kapitel>_<abschnitt>_<typ>_<kurztitel>_vNN.png`

Regeln:
- `vNN` immer zweistellig (`v01`, `v02`, `v03`, ...)
- nur lowercase, `_` oder `-`, keine Leerzeichen
- sprechender Kurztitel (max. ~40 Zeichen)

Beispiele:
- `05_02_architektur_layered-overview_v01.png`
- `05_03_gateframework_compliance-flow_v02.png`
- `06_04_poc_pipeline-overview_v03.png`

## Arbeitsweise
1. Entwurf nach `images/work`
2. Freigegebene Version nach `images/final`
3. Neue Aenderung = neue Versionsnummer (nie ueberschreiben)

## Referenz in Markdown/Thesis
- Immer auf `images/final/..._vNN.png` verweisen
- Optional: zusaetzlich ein stabiler Alias ohne Version (nur fuer finale PDF-Phase)

## Nicht einchecken
- temporaere Exporte/Backup-Dateien (`*.tmp.png`, `*.bak.png` etc.)
