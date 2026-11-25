#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message (<=100 characters) for a bug fix that made
everything worse, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python standard library only; fully deterministic.
"""

import os

MESSAGE = "fix(db): plugged the leak by deleting the database (leak gone, data too)"


def main() -> None:
    text = MESSAGE.strip()
    assert 1 <= len(text) <= 100, f"message must be 1-100 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "message must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
