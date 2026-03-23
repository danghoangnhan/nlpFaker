import random

from nlpFaker._base import BaseGenerator


class CompanyGenerator(BaseGenerator):
    """Generator for Taiwanese company names."""

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._prefixes: list[str] = []
        self._middles: list[str] = []
        self._suffixes: list[str] = []
        self._parse_data()

    def _parse_data(self) -> None:
        section = ""
        for line in self._load_lines("company.dat"):
            line = line.strip()
            if not line:
                continue
            if line == "# prefixes":
                section = "prefix"
                continue
            elif line == "# middles":
                section = "middle"
                continue
            elif line == "# suffixes":
                section = "suffix"
                continue

            if section == "prefix":
                self._prefixes.append(line)
            elif section == "middle":
                self._middles.append(line)
            elif section == "suffix":
                self._suffixes.append(line)

    def generate(self) -> str:
        """Generate a Taiwanese company name."""
        prefix = self._rng.choice(self._prefixes)
        middle = self._rng.choice(self._middles)
        suffix = self._rng.choice(self._suffixes)
        return f"{prefix}{middle}{suffix}"
