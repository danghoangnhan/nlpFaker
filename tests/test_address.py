import re


def test_address_contains_city(fake):
    addr = fake.address()
    assert re.search(r"(市|縣)", addr), f"No city/county found: {addr}"


def test_address_contains_number(fake):
    addr = fake.address()
    assert "號" in addr, f"No number found: {addr}"


def test_postal_code_format(fake):
    for _ in range(50):
        code = fake.postal_code()
        assert re.match(r"^\d{3}$", code), f"Bad postal code: {code}"
