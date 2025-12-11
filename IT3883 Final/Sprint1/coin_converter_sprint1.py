#!/usr/bin/env python3
"""
Sprint 1 version
"""

import sys

COIN_VALUES = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}


def normalize_denom(word: str) -> str:

    w = word.strip().lower()

    if w == "pennies":
        return "penny"

    if w.endswith("s"):
        w = w[:-1]

    return w


def convert_line(line: str) -> float:

    parts = [p.strip() for p in line.strip().split(" and ") if p.strip()]
    total = 0.0

    for phrase in parts:
        qty_str, denom_str = phrase.split()
        qty = int(qty_str)

        denom = normalize_denom(denom_str)
        value = COIN_VALUES[denom]

        total += qty * value

    return total


def main() -> None:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue

        total = convert_line(line)

        print(f"{total:.2f}")


if __name__ == "__main__":
    main()
