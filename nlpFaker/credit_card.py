import random

from nlpFaker._base import BaseGenerator


class CreditCardGenerator(BaseGenerator):
    """Generator for Luhn-valid credit card numbers.

    Supports Visa (4), Mastercard (51-55), and JCB (3528-3589) prefixes.
    """

    _PREFIXES = {
        "visa": ["4"],
        "mastercard": ["51", "52", "53", "54", "55"],
        "jcb": ["3528", "3529", "3530", "3589"],
    }

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    @staticmethod
    def _luhn_check_digit(digits: list[int]) -> int:
        """Compute the Luhn check digit for a list of digits (without check digit)."""
        total = 0
        # Process from rightmost digit, doubling every other
        for i, d in enumerate(reversed(digits)):
            if i % 2 == 0:  # even index from right = double (since check digit will be at pos 0)
                d *= 2
                if d > 9:
                    d -= 9
            total += d
        return (10 - (total % 10)) % 10

    def generate(self, card_type: str | None = None) -> str:
        """Generate a Luhn-valid credit card number.

        Args:
            card_type: "visa", "mastercard", "jcb", or None for random.
        """
        if card_type is None:
            card_type = self._rng.choice(["visa", "mastercard", "jcb"])

        prefix = self._rng.choice(self._PREFIXES[card_type])
        length = 16
        digits = [int(c) for c in prefix]
        remaining = length - len(digits) - 1  # -1 for check digit
        digits.extend(self._rng.randint(0, 9) for _ in range(remaining))
        check = self._luhn_check_digit(digits)
        digits.append(check)
        return "".join(str(d) for d in digits)
