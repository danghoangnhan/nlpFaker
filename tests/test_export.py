import json
import csv
from pathlib import Path

from nlpFaker import NlpFaker, Exporter


def test_to_json(tmp_path):
    fake = NlpFaker(seed=1)
    records = [fake.profile() for _ in range(3)]
    out = tmp_path / "data.json"
    Exporter.to_json(records, out)

    loaded = json.loads(out.read_text(encoding="utf-8"))
    assert len(loaded) == 3
    assert "name" in loaded[0]


def test_to_csv(tmp_path):
    fake = NlpFaker(seed=1)
    records = [fake.profile() for _ in range(3)]
    out = tmp_path / "data.csv"
    Exporter.to_csv(records, out)

    with open(out, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 3
    assert "name" in rows[0]


def test_to_sql(tmp_path):
    fake = NlpFaker(seed=1)
    records = [fake.profile() for _ in range(2)]
    out = tmp_path / "data.sql"
    Exporter.to_sql(records, "people", out)

    content = out.read_text(encoding="utf-8")
    assert "INSERT INTO people" in content
    assert content.count("INSERT") == 2
