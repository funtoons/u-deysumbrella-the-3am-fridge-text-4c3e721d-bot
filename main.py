#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge would text its owner at 3am
to /output/entry.txt. Deterministic, offline, standard library only.

The line: a 3am check-in from an appliance that has been awake all
night — cold, honest, a little passive-aggressive, and done
pretending. Fresh angle (an expired yogurt, not milk/ice/a door
left open), one line, 122 characters.
"""

import os

LINE = (
    "3am check-in: I'm still cold, you're still awake, "
    "and the yogurt expired Tuesday. "
    "We're both just pretending. Go to sleep."
)


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back what was written: the file on disk must be exactly
    # the chosen line plus one trailing newline (123 bytes total).
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt does not match the line"


if __name__ == "__main__":
    main()
