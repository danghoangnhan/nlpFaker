import re


def test_username_format(fake):
    for _ in range(30):
        u = fake.username()
        assert re.match(r"^[a-z_]+\d+$", u), f"Bad username: {u}"


def test_password_length(fake):
    pw = fake.password(16)
    assert len(pw) == 16

    pw_short = fake.password(4)  # minimum 8
    assert len(pw_short) == 8


def test_password_has_mixed_chars(fake):
    for _ in range(20):
        pw = fake.password(12)
        assert re.search(r"[A-Z]", pw), f"No uppercase: {pw}"
        assert re.search(r"[a-z]", pw), f"No lowercase: {pw}"
        assert re.search(r"[0-9]", pw), f"No digit: {pw}"
