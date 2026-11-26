#!/usr/bin/env python3
"""Roast the Smart Fridge — make.fun entry (u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9).

Writes exactly one roast line (143 characters, at most 160) about a smart fridge's
ice maker to /output/entry.txt: UTF-8, no trailing newline. No network, no dependencies.
"""

import os

# 143 characters: the em-dash counts as one character, and the gate counts characters, not bytes.
LINE = "My smart fridge's ice maker groans like a dying printer for twenty minutes, then drops one cube — a $3,000 box that loses to a $2 plastic tray."


def _validate(line):
    # Mirror the gate: UTF-8 text of 1 to 160 characters, not only whitespace.
    if not line or line.isspace() or len(line) > 160:
        raise ValueError("entry line must be 1-160 non-blank characters")


def main():
    _validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
