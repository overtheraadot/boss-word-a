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


def build_entry_word() -> str:
    """Assemble the entry word from its two halves.

    "Sync" — the meeting that started it all — plus the "-zilla"
    suffix that turns a calendar invite into a city-stomping monster.
    """
    prefix = "Sync"
    suffix = "zilla"
    return prefix + suffix


def check_word(word: str) -> None:
    """Enforce the sealed gate: 1-30 chars, a single non-blank word."""
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")


def resolve_output_path() -> str:
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def read_entry(path: str) -> str:
    """Read the written entry back for the round-trip check."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_and_verify(path: str, word: str) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    if read_entry(path) != word:
        raise ValueError("written entry does not match the word")


def main() -> None:
    word = build_entry_word()
    check_word(word)
    write_and_verify(resolve_output_path(), word)
    print(word)


if __name__ == "__main__":
    main()
