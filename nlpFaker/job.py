import random

from nlpFaker._base import BaseGenerator


class JobGenerator(BaseGenerator):
    """Generator for common Taiwanese job titles."""

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._titles = self._load_lines("job.dat")

    def generate(self) -> str:
        """Generate a random job title."""
        return self._rng.choice(self._titles)
