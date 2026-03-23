import random
import string

from nlpFaker._base import BaseGenerator


class EmailGenerator(BaseGenerator):
    """Generator for email addresses with common Taiwanese domains."""

    _PATTERNS = ["word.word", "word_word", "wordNNN", "word.wordNN"]

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)
        self._domains = self._load_lines("email_domains.dat")

    def _random_word(self, min_len: int = 3, max_len: int = 8) -> str:
        length = self._rng.randint(min_len, max_len)
        return "".join(self._rng.choices(string.ascii_lowercase, k=length))

    def _random_digits(self, n: int) -> str:
        return "".join(str(self._rng.randint(0, 9)) for _ in range(n))

    def generate(self) -> str:
        """Generate a random email address."""
        pattern = self._rng.choice(self._PATTERNS)
        domain = self._rng.choice(self._domains)

        if pattern == "word.word":
            user = f"{self._random_word()}.{self._random_word()}"
        elif pattern == "word_word":
            user = f"{self._random_word()}_{self._random_word()}"
        elif pattern == "wordNNN":
            user = f"{self._random_word()}{self._random_digits(self._rng.randint(2, 4))}"
        else:
            user = f"{self._random_word()}.{self._random_word()}{self._random_digits(2)}"

        return f"{user}@{domain}"
