import re


def test_bank_account_format(fake):
    for _ in range(30):
        acc = fake.bank_account()
        assert re.match(r"^\d{3}-\d{10,14}$", acc), f"Bad bank account: {acc}"


def test_bank_code(fake):
    for _ in range(20):
        code = fake.bank_code()
        assert re.match(r"^\d{3}$", code)
