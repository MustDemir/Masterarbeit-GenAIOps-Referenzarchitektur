#!/usr/bin/env python3
from workflow_lib import build_index, build_resume_text, write_index, write_resume_text


def main() -> int:
    index = build_index()
    write_index(index)
    text = build_resume_text(index)
    path = write_resume_text(text)

    print(text)
    print(f"\n(gespeichert in: {path})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
