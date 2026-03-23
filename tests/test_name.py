import re


def test_name_returns_string(fake):
    name = fake.name()
    assert isinstance(name, str)
    assert len(name) >= 2


def test_name_contains_chinese_characters(fake):
    name = fake.name()
    assert re.match(r"[\u4e00-\u9fff]+$", name)


def test_first_name_length(fake):
    for _ in range(50):
        fn = fake.first_name()
        assert 1 <= len(fn) <= 2


def test_last_name_length(fake):
    for _ in range(50):
        ln = fake.last_name()
        assert len(ln) >= 1


def test_batch_names(fake):
    names = fake.batch("name", 10)
    assert len(names) == 10
    assert all(isinstance(n, str) for n in names)
