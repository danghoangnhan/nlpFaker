"""Validation functions for Taiwan-specific data formats."""

from __future__ import annotations

import re

_ID_AREAS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P",
    "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "I", "O",
]
_ID_WEIGHTS = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]


def validate_id_number(id_str: str) -> bool:
    """Validate a Taiwan National ID number checksum."""
    if not re.match(r"^[A-Z][0-9]{9}$", id_str):
        return False
    area_num = _ID_AREAS.index(id_str[0]) + 10
    digits = [area_num // 10, area_num % 10] + [int(c) for c in id_str[1:]]
    total = sum(d * w for d, w in zip(digits, _ID_WEIGHTS))
    return total % 10 == 0


def validate_tax_id(tax_str: str) -> bool:
    """Validate a Taiwan Unified Business Number (統一編號) checksum."""
    if not re.match(r"^\d{8}$", tax_str):
        return False
    digits = [int(c) for c in tax_str]
    weights = [1, 2, 1, 2, 1, 2, 4, 1]

    def digit_sum(n: int) -> int:
        return n // 10 + n % 10

    total = sum(digit_sum(d * w) for d, w in zip(digits, weights))
    if total % 5 == 0:
        return True
    if digits[6] * 4 >= 10:
        return (total - 1) % 5 == 0
    return False


def validate_mobile(mobile_str: str) -> bool:
    """Validate a Taiwan mobile phone number format."""
    return bool(re.match(r"^09\d{8}$", mobile_str))


def validate_credit_card(card_str: str) -> bool:
    """Validate a credit card number using the Luhn algorithm."""
    if not re.match(r"^\d{13,19}$", card_str):
        return False
    digits = [int(c) for c in card_str]
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0
