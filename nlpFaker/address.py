import random

from nlpFaker._base import BaseGenerator


class AddressGenerator(BaseGenerator):
    """Generator for Taiwan addresses.

    Uses address.dat with rows: postal_code<TAB>city<TAB>district<TAB>road
    Then appends random lane/alley/number/floor components.
    """

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._roads: list[dict[str, str]] = []
        for line in self._load_lines("address.dat"):
            parts = line.split("\t")
            if len(parts) >= 4:
                self._roads.append({
                    "postal": parts[0],
                    "city": parts[1],
                    "district": parts[2],
                    "road": parts[3],
                })

    def _random_lane(self) -> str:
        if self._rng.random() < 0.3:
            return f"{self._rng.randint(1, 30)}巷"
        return ""

    def _random_alley(self) -> str:
        if self._rng.random() < 0.15:
            return f"{self._rng.randint(1, 20)}弄"
        return ""

    def _random_number(self) -> str:
        num = self._rng.randint(1, 500)
        if self._rng.random() < 0.1:
            return f"{num}之{self._rng.randint(1, 5)}號"
        return f"{num}號"

    def _random_floor(self) -> str:
        if self._rng.random() < 0.5:
            return f"{self._rng.randint(1, 24)}樓"
        return ""

    def generate(self) -> str:
        """Generate a complete Taiwan address."""
        road = self._rng.choice(self._roads)
        parts = [
            road["city"],
            road["district"],
            road["road"],
            self._random_lane(),
            self._random_alley(),
            self._random_number(),
            self._random_floor(),
        ]
        return "".join(parts)

    def postal_code(self) -> str:
        """Generate a Taiwan postal code."""
        road = self._rng.choice(self._roads)
        return road["postal"]
