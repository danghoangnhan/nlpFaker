from nlpFaker import validate_id_number, validate_mobile, validate_tax_id, validate_credit_card


def test_validate_id_number_valid(fake):
    for _ in range(50):
        assert validate_id_number(fake.id_number())


def test_validate_id_number_invalid():
    assert not validate_id_number("A000000000")
    assert not validate_id_number("12345")
    assert not validate_id_number("")


def test_validate_tax_id_valid(fake):
    for _ in range(50):
        assert validate_tax_id(fake.tax_id())


def test_validate_tax_id_invalid():
    assert not validate_tax_id("0000000")
    assert not validate_tax_id("abcdefgh")


def test_validate_mobile_valid(fake):
    for _ in range(30):
        assert validate_mobile(fake.mobile())


def test_validate_mobile_invalid():
    assert not validate_mobile("1234567890")
    assert not validate_mobile("091234567")  # too short


def test_validate_credit_card_valid(fake):
    for _ in range(50):
        assert validate_credit_card(fake.credit_card())


def test_validate_credit_card_invalid():
    assert not validate_credit_card("1234567890123456")
    assert not validate_credit_card("abc")
