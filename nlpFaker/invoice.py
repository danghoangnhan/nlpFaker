import random
import string

from nlpFaker._base import BaseGenerator


class InvoiceGenerator(BaseGenerator):
    """Generator for Taiwan Uniform Invoice numbers (統一發票).

    Format: 2 uppercase letters + 8 digits (e.g., AB-12345678).
    """

    _LETTERS = string.ascii_uppercase

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    def generate(self) -> str:
        """Generate a Taiwan Uniform Invoice number."""
        letters = self._rng.choice(self._LETTERS) + self._rng.choice(self._LETTERS)
        digits = "".join(str(self._rng.randint(0, 9)) for _ in range(8))
        return f"{letters}-{digits}"
