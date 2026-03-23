import random
import string

from nlpFaker._base import BaseGenerator


class LicensePlateGenerator(BaseGenerator):
    """Generator for Taiwan license plate numbers.

    Formats:
    - Car (new): ABC-1234 (3 letters + 4 digits)
    - Car (old): 1234-AB (4 digits + 2 letters)
    - Motorcycle: ABC-1234 or AB-1234
    """

    # Excludes I and O to avoid confusion with 1 and 0
    _LETTERS = [c for c in string.ascii_uppercase if c not in ("I", "O")]

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    def _random_letters(self, n: int) -> str:
        return "".join(self._rng.choices(self._LETTERS, k=n))

    def _random_digits(self, n: int) -> str:
        return "".join(str(self._rng.randint(0, 9)) for _ in range(n))

    def generate(self, vehicle: str = "car") -> str:
        """Generate a Taiwan license plate number.

        Args:
            vehicle: "car" or "motorcycle".
        """
        if vehicle == "motorcycle":
            if self._rng.random() < 0.6:
                return f"{self._random_letters(3)}-{self._random_digits(4)}"
            return f"{self._random_letters(2)}-{self._random_digits(4)}"

        # Car: mostly new format
        if self._rng.random() < 0.8:
            return f"{self._random_letters(3)}-{self._random_digits(4)}"
        return f"{self._random_digits(4)}-{self._random_letters(2)}"
