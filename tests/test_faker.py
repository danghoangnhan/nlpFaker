import pytest

from nlpFaker import NlpFaker


def test_seed_reproducibility():
    a = NlpFaker(seed=123)
    b = NlpFaker(seed=123)
    assert a.name() == b.name()
    assert a.id_number() == b.id_number()


def test_batch_returns_correct_count(fake):
    assert len(fake.batch("name", 5)) == 5
    assert len(fake.batch("mobile", 20)) == 20


def test_batch_invalid_field(fake):
    with pytest.raises((AttributeError, ValueError)):
        fake.batch("nonexistent_field", 5)
