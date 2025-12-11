#!/usr/bin/env python3
"""
Sprint 2 version: Refined
"""

import sys
from decimal import Decimal, ROUND_HALF_UP


COIN_VALUES = {
    "penny":   Decimal("0.01"),
    "nickel":  Decimal("0.05"),
    "dime":    Decimal("0.10"),
    "quarter": Decimal("0.25"),
}

DENOM_ALIASES = {
    "penny": "penny",
    "pennies": "penny",
    "nickel": "nickel",
    "nickels": "nickel",
    "dime": "dime",
    "dimes": "dime",
    "quarter": "quarter",
    "quarters": "quarter",
}


def parse_phrase(phrase: str) -> Decimal:

    parts = phrase.strip().split()
    if len(parts) != 2:
        raise ValueError(f"Invalid coin phrase (expected 'N coin'): {phrase!r}")

    qty_str, denom_str = parts

    if not qty_str.isdigit():
        raise ValueError(f"Invalid quantity (expected numeral): {qty_str!r}")

    denom_key = denom_str.strip().lower()
    if denom_key not in DENOM_ALIASES:
        raise ValueError(f"Unknown coin denomination: {denom_str!r}")

    qty = int(qty_str)
    canon = DENOM_ALIASES[denom_key]

    return Decimal(qty) * COIN_VALUES[canon]


def convert_line(line: str) -> Decimal:

    phrases = [p.strip() for p in line.strip().split(" and ") if p.strip()]
    if not phrases:
        raise ValueError("Empty input line")

    total = Decimal("0.00")
    for phrase in phrases:
        total += parse_phrase(phrase)

    return total

def format_money(amount: Decimal) -> str:

    return str(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def main() -> None:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue

        try:
            total = convert_line(line)
            print(format_money(total))
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
