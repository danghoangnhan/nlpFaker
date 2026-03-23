from __future__ import annotations

import datetime as dt
import random

from nlpFaker._base import BaseGenerator


class DateTimeGenerator(BaseGenerator):
    """Generator for dates and times, with ROC (民國) calendar support."""

    _DEFAULT_START = dt.date(1950, 1, 1)
    _DEFAULT_END = dt.date(2025, 12, 31)

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    def _random_date(
        self,
        start: dt.dt.date | None = None,
        end: dt.dt.date | None = None,
    ) -> dt.date:
        start = start or self._DEFAULT_START
        end = end or self._DEFAULT_END
        delta = (end - start).days
        return start + dt.timedelta(days=self._rng.randint(0, delta))

    def generate(self) -> str:
        """Generate a random date in YYYY-MM-DD format."""
        d = self._random_date()
        return d.isoformat()

    def date(
        self,
        start: dt.date | None = None,
        end: dt.date | None = None,
    ) -> str:
        """Generate a random date in YYYY/MM/DD format."""
        d = self._random_date(start, end)
        return f"{d.year}/{d.month:02d}/{d.day:02d}"

    def date_roc(
        self,
        start: dt.date | None = None,
        end: dt.date | None = None,
    ) -> str:
        """Generate a date in ROC calendar format (民國YYY年MM月DD日)."""
        d = self._random_date(start, end)
        roc_year = d.year - 1911
        return f"民國{roc_year}年{d.month:02d}月{d.day:02d}日"

    def time(self) -> str:
        """Generate a random time in HH:MM:SS format."""
        h = self._rng.randint(0, 23)
        m = self._rng.randint(0, 59)
        s = self._rng.randint(0, 59)
        return f"{h:02d}:{m:02d}:{s:02d}"

    def datetime(
        self,
        start: dt.date | None = None,
        end: dt.date | None = None,
    ) -> str:
        """Generate a random datetime in YYYY-MM-DD HH:MM:SS format."""
        return f"{self.date(start, end)} {self.time()}"
