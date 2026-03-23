import random
from abc import ABC, abstractmethod
from pathlib import Path


class BaseGenerator(ABC):
    _DATA_DIR = Path(__file__).resolve().parent / "raw_data"

    def __init__(self, rng: random.Random | None = None) -> None:
        self._rng = rng or random.Random()

    def _load_lines(self, filename: str) -> list[str]:
        """Load a data file as a list of stripped lines."""
        return (self._DATA_DIR / filename).read_text(encoding="utf-8").strip().splitlines()

    def _load_weighted(self, filename: str) -> tuple[list[str], list[int]]:
        """Load a space-separated 'value weight' file."""
        items: list[str] = []
        weights: list[int] = []
        for line in self._load_lines(filename):
            value, weight = line.split()
            items.append(value)
            weights.append(int(weight))
        return items, weights

    def _weighted_choice(self, items: list[str], weights: list[int]) -> str:
        """Select a random item using weighted probability."""
        return self._rng.choices(items, weights=weights, k=1)[0]

    @abstractmethod
    def generate(self) -> str:
        """Generate a single fake value."""
        ...
