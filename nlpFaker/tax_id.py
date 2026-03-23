import random

from nlpFaker._base import BaseGenerator


class TaxIDGenerator(BaseGenerator):
    """Generator for Taiwan Unified Business Numbers (統一編號).

    Format: 8 digits with a checksum.
    Algorithm: multiply each digit by weights [1,2,1,2,1,2,4,1],
    sum the digits of each product, total must be divisible by 5
    (with special handling when the 7th digit multiplied by 4 produces a carry).
    """

    _WEIGHTS = [1, 2, 1, 2, 1, 2, 4, 1]

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    @staticmethod
    def _digit_sum(n: int) -> int:
        return n // 10 + n % 10

    def _is_valid(self, digits: list[int]) -> bool:
        total = sum(self._digit_sum(d * w) for d, w in zip(digits, self._WEIGHTS))
        if total % 5 == 0:
            return True
        # Special rule: if 7th digit * 4 >= 10, check with alternative sum
        if digits[6] * 4 >= 10:
            return (total - 1) % 5 == 0
        return False

    def generate(self) -> str:
        """Generate a valid Taiwan Unified Business Number (統一編號)."""
        while True:
            digits = [self._rng.randint(0, 9) for _ in range(8)]
            if digits[0] == 0:
                digits[0] = self._rng.randint(1, 9)
            if self._is_valid(digits):
                return "".join(str(d) for d in digits)
