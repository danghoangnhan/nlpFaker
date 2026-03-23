import random
import string

from nlpFaker._base import BaseGenerator


class CredentialGenerator(BaseGenerator):
    """Generator for usernames and passwords."""

    _USERNAME_PARTS = [
        "cool", "super", "mega", "pro", "dark", "light", "fast", "big",
        "tiny", "red", "blue", "green", "neo", "max", "top", "sky",
        "star", "fire", "ice", "wild", "zen", "ace", "nova", "epic",
    ]

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    def username(self) -> str:
        """Generate a random username."""
        part1 = self._rng.choice(self._USERNAME_PARTS)
        part2 = self._rng.choice(self._USERNAME_PARTS)
        digits = self._rng.randint(1, 9999)
        sep = self._rng.choice(["", "_", ""])
        return f"{part1}{sep}{part2}{digits}"

    def password(self, length: int = 12) -> str:
        """Generate a random password with mixed character classes.

        Args:
            length: Password length (minimum 8).
        """
        length = max(length, 8)
        # Guarantee at least one of each class
        chars = [
            self._rng.choice(string.ascii_uppercase),
            self._rng.choice(string.ascii_lowercase),
            self._rng.choice(string.digits),
            self._rng.choice("!@#$%^&*()-_=+"),
        ]
        pool = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        chars.extend(self._rng.choices(pool, k=length - 4))
        self._rng.shuffle(chars)
        return "".join(chars)

    def generate(self) -> str:
        """Generate a username (default generate method)."""
        return self.username()
