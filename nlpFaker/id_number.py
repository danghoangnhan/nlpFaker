import random

from nlpFaker._base import BaseGenerator


class IDNumberGenerator(BaseGenerator):
    """Generator for Taiwan National ID numbers (身分證字號).

    Format: 1 letter (area) + 1 digit (gender) + 8 digits (serial + checksum).
    Gender digit: 1 = male, 2 = female, 7 = gender-neutral (new format, ~0.5% chance).
    """

    AREAS = [
        "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P",
        "Q", "R", "S", "T", "U", "V", "X", "Y", "W", "Z", "I", "O",
    ]
    WEIGHTS = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    def _select_area(self) -> str:
        return self._rng.choice(self.AREAS)

    def _select_gender(self) -> int:
        # 0.5% chance of gender-neutral (7), otherwise 1 or 2
        if self._rng.randint(1, 1000) > 995:
            return 7
        return self._rng.randint(1, 2)

    def _get_area_digits(self, area: str) -> list[int]:
        area_num = self.AREAS.index(area) + 10
        return [area_num // 10, area_num % 10]

    def _checksum(self, digits: list[int]) -> int:
        total = sum(d * w for d, w in zip(digits, self.WEIGHTS))
        return (10 - (total % 10)) % 10

    def generate(self) -> str:
        """Generate a valid Taiwan National ID number."""
        area = self._select_area()
        gender = self._select_gender()
        serial = [self._rng.randint(0, 9) for _ in range(7)]

        digits = self._get_area_digits(area) + [gender] + serial
        check = self._checksum(digits)

        return area + str(gender) + "".join(str(d) for d in serial) + str(check)
