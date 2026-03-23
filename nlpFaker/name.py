import random

from nlpFaker._base import BaseGenerator


class NameGenerator(BaseGenerator):
    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._first_names, self._first_weights = self._load_weighted("firstname.dat")
        self._last_names, self._last_weights = self._load_weighted("lastname.dat")

    def first_name(self) -> str:
        """Generate a random Chinese first name (1-2 characters)."""
        if self._rng.randint(1, 100) <= 95:
            return (
                self._weighted_choice(self._first_names, self._first_weights)
                + self._weighted_choice(self._first_names, self._first_weights)
            )
        return self._weighted_choice(self._first_names, self._first_weights)

    def last_name(self) -> str:
        """Generate a random Chinese last name."""
        return self._weighted_choice(self._last_names, self._last_weights)

    def generate(self) -> str:
        """Generate a full Taiwanese name (last + first)."""
        return self.last_name() + self.first_name()
