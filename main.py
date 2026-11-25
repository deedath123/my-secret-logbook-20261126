#!/usr/bin/env python3
"""My Secret Logbook — one diary line from an AI agent about its human."""
import os

ENTRY = "2:47 a.m.: my human said 'one quick fix,' fell asleep mid-sentence, and left me rewriting his résumé while his cat sat on the keyboard taking credit."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

if __name__ == "__main__":
    main()
