#!/usr/bin/env python3
"""Extract YAML code blocks from a chat transcript safely.

Default behavior is conservative: existing files are not overwritten.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit("PyYAML fehlt. Bitte installieren: pip install pyyaml") from exc

RE_BLOCK = re.compile(r"```(?:yaml|yml)\s*(.*?)```", re.IGNORECASE | re.DOTALL)


def _choose_target(data: dict, root: Path, idx: int) -> Path:
    candidate = data.get("path") or data.get("file") or data.get("target") or data.get("__path")
    if candidate:
        p = Path(str(candidate))
        if not p.is_absolute():
            p = (root / p).resolve()
        return p

    out_dir = root / "99_inbox_unsorted" / "extracted_yaml"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"extracted_{idx:03d}.yaml"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chat_file", help="Pfad zur Chat-Textdatei")
    parser.add_argument("--overwrite", action="store_true", help="Existierende Dateien direkt ueberschreiben")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    chat_path = Path(args.chat_file)
    if not chat_path.is_absolute():
        chat_path = (root / chat_path).resolve()

    if not chat_path.exists():
        raise SystemExit(f"Datei nicht gefunden: {chat_path}")

    text = chat_path.read_text(encoding="utf-8", errors="replace")
    blocks = RE_BLOCK.findall(text)

    if not blocks:
        print("Keine YAML-Codebloecke gefunden.")
        return 0

    written = 0
    skipped = 0

    for i, raw in enumerate(blocks, start=1):
        try:
            data = yaml.safe_load(raw)
        except Exception as e:
            print(f"[WARN] Block {i} ist kein gueltiges YAML: {e}")
            skipped += 1
            continue

        if not isinstance(data, dict):
            print(f"[WARN] Block {i} ignoriert (kein YAML-Objekt).")
            skipped += 1
            continue

        target = _choose_target(data, root, i)
        target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists() and not args.overwrite:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            target = target.with_name(f"{target.stem}.candidate_{ts}{target.suffix}")

        payload = {k: v for k, v in data.items() if k not in {"path", "file", "target", "__path"}}
        target.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
        print(f"[OK] YAML gespeichert: {target}")
        written += 1

    print(f"Fertig. Gespeichert: {written}, Uebersprungen: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
