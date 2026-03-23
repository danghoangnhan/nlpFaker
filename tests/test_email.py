import re


def test_email_format(fake):
    for _ in range(50):
        email = fake.email()
        assert re.match(r"^[a-z0-9._]+@[a-z0-9.]+\.[a-z.]+$", email), f"Bad email: {email}"


def test_email_has_at_sign(fake):
    email = fake.email()
    assert "@" in email
    assert email.count("@") == 1
