import pytest

from nlpFaker import NlpFaker


@pytest.fixture
def fake():
    return NlpFaker(seed=42)
