import re


def test_landline_format(fake):
    for _ in range(50):
        phone = fake.landline()
        assert re.match(r"^\(0\d{1,2}\) \d{6,8}$", phone), f"Bad landline: {phone}"


def test_landline_has_area_code(fake):
    phone = fake.landline()
    assert phone.startswith("(0")
