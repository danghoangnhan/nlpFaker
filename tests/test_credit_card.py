from nlpFaker import validate_credit_card


def test_credit_card_length(fake):
    for _ in range(50):
        cc = fake.credit_card()
        assert len(cc) == 16
        assert cc.isdigit()


def test_credit_card_luhn(fake):
    for _ in range(100):
        cc = fake.credit_card()
        assert validate_credit_card(cc), f"Luhn check failed: {cc}"


def test_credit_card_types(fake):
    visa = fake.credit_card("visa")
    assert visa.startswith("4")

    mc = fake.credit_card("mastercard")
    assert mc[:2] in ("51", "52", "53", "54", "55")

    jcb = fake.credit_card("jcb")
    assert jcb[:4] >= "3528" and jcb[:4] <= "3589"
