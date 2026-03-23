import random

from nlpFaker._base import BaseGenerator


class MobileGenerator(BaseGenerator):
    """Generator for Taiwan mobile phone numbers.

    Format: 09XX-XXXXXX (10 digits total).
    """

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._prefixes = self._load_lines("mobile.dat")

    def generate(self) -> str:
        """Generate a Taiwan mobile phone number."""
        prefix = self._rng.choice(self._prefixes)
        suffix = "".join(str(self._rng.randint(0, 9)) for _ in range(10 - len(prefix)))
        return prefix + suffix
