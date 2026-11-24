#!/usr/bin/env python3
"""One Word for the Boss — entry program.

The word is what the whole team whispers when the boss's "quick sync"
invite lands: Synczilla. A fifteen-minute meeting that eats the whole
afternoon, summoned by a boss who treats everyone's calendar as his own
personal whiteboard. One word, no caption, no explanation — it lands on
its own.

Writes the single word to /output/entry.txt. Deterministic: the same
word, byte for byte, on every run.
"""

import os

WORD = "Synczilla"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(WORD) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if not WORD.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in WORD):
        raise ValueError("entry must be a single word with no spaces")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError("written entry does not match the word")
    print(WORD)


if __name__ == "__main__":
    main()
