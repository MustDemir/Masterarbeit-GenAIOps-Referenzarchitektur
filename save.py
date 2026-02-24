#!/usr/bin/env python3
"""Create compact session summaries and refresh local context."""

from __future__ import annotations

import argparse
import sys

from workflow_lib import (
    build_index,
    build_resume_text,
    blob_configured,
    push_index_to_azure,
    push_summaries_to_blob,
    save_session_summary,
    write_index,
    write_resume_text,
)


def _read_input(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()
    if args.input:
        return args.input.read_text(encoding="utf-8", errors="replace").strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    raise SystemExit("Kein Input gefunden. Nutze --text, --input oder Pipe.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Pfad zu Session-Notizen/Text")
    parser.add_argument("--text", type=str, help="Direkter Session-Text")
    parser.add_argument(
        "--topic",
        type=str,
        default="auto",
        help="z. B. architektur, anforderungen, theorie, evaluation, methodik, auto",
    )
    parser.add_argument("--title", type=str, default="", help="Kurzer Titel der Session")
    parser.add_argument("--source", type=str, default="chat", help="Quelle, z. B. chatgpt/claude/manual")
    parser.add_argument("--tags", type=str, default="", help="Kommagetrennte Tags")
    parser.add_argument("--azure", action="store_true", help="Direkt nach Azure AI Search pushen")
    parser.add_argument("--blob", action="store_true", help="Direkt nach Blob syncen")
    parser.add_argument("--no-llm", action="store_true", help="Keine Azure-OpenAI-Summary, nur lokale Regeln")
    args = parser.parse_args()

    from pathlib import Path

    if args.input:
        args.input = Path(args.input)

    text = _read_input(args)
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    summary_path, payload = save_session_summary(
        text=text,
        topic=args.topic,
        title=args.title or None,
        source=args.source,
        tags=tags,
        use_llm=not args.no_llm,
    )

    index = build_index()
    index_path = write_index(index)
    resume = build_resume_text(index)
    resume_path = write_resume_text(resume)

    print(f"Summary gespeichert: {summary_path}")
    print(f"Topic-Routing: {payload.get('target_folder')}")
    print(f"Summary-Engine: {payload.get('summary_engine')}")
    print(f"Index aktualisiert: {index_path}")
    print(f"Resume aktualisiert: {resume_path}")

    if args.azure:
        ok, msg = push_index_to_azure(index)
        prefix = "Azure OK" if ok else "Azure FEHLER"
        print(f"{prefix}: {msg}")
        if not ok:
            return 2

    if args.blob or blob_configured():
        ok, msg = push_summaries_to_blob()
        prefix = "Blob OK" if ok else "Blob FEHLER"
        print(f"{prefix}: {msg}")
        if not ok:
            return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
