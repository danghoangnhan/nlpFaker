import re


def test_mobile_format(fake):
    for _ in range(50):
        mobile = fake.mobile()
        assert re.match(r"^09\d{8}$", mobile), f"Bad format: {mobile}"


def test_mobile_length(fake):
    mobile = fake.mobile()
    assert len(mobile) == 10
