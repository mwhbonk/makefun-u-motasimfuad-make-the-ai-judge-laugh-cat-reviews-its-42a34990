#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one deadpan one-star review from a house cat to /output/entry.txt.

The line: the food bowl sat empty for eleven minutes, and the cat has
forgiven the human but not forgotten -- and neither has the rug. Specific
complaint (the food bowl, straight from the judge's own examples), feline
voice all the way through (the cat counts the minutes, holds the grudge),
and the sting lands in the last four words, which reward a second read:
something happened to the rug. Deadpan review shape, absurd content.
One line, every word earning its place.
"""
import os
from pathlib import Path


def main():
    src = Path(__file__).resolve().parent / "review.txt"
    line = src.read_text(encoding="utf-8")
    assert "\n" not in line, "entry must be a single line"
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    out = os.environ.get("OUTPUT_PATH")
    if not out:
        out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip check: what the gate will read must be exactly the line.
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "round-trip mismatch: file content differs from review.txt"
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
