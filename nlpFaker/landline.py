import random

from nlpFaker._base import BaseGenerator


class LandlineGenerator(BaseGenerator):
    """Generator for Taiwan landline phone numbers.

    Format: (0X) XXXX-XXXX or (0XX) XXX-XXXX depending on area code.
    """

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._area_codes: list[tuple[str, int]] = []
        for line in self._load_lines("landline.dat"):
            parts = line.split("\t")
            self._area_codes.append((parts[0], int(parts[1])))

    def generate(self) -> str:
        """Generate a Taiwan landline phone number."""
        area_code, digit_count = self._rng.choice(self._area_codes)
        number = "".join(str(self._rng.randint(0, 9)) for _ in range(digit_count))
        return f"({area_code}) {number}"
