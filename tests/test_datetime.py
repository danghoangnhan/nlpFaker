import re
from datetime import date


def test_date_format(fake):
    for _ in range(20):
        d = fake.date()
        assert re.match(r"^\d{4}/\d{2}/\d{2}$", d), f"Bad date: {d}"


def test_date_roc_format(fake):
    for _ in range(20):
        d = fake.date_roc()
        assert re.match(r"^民國\d+年\d{2}月\d{2}日$", d), f"Bad ROC date: {d}"


def test_date_roc_year_conversion(fake):
    d = fake.date(start=date(2024, 1, 1), end=date(2024, 12, 31))
    assert d.startswith("2024/")

    roc = fake.date_roc(start=date(2024, 6, 15), end=date(2024, 6, 15))
    assert "113年" in roc


def test_time_format(fake):
    for _ in range(20):
        t = fake.time()
        assert re.match(r"^\d{2}:\d{2}:\d{2}$", t), f"Bad time: {t}"


def test_datetime_format(fake):
    dt = fake.datetime()
    assert re.match(r"^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}$", dt), f"Bad datetime: {dt}"
