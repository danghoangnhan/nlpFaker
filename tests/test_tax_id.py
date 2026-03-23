from nlpFaker import validate_tax_id


def test_tax_id_format(fake):
    for _ in range(50):
        tid = fake.tax_id()
        assert len(tid) == 8
        assert tid.isdigit()
        assert tid[0] != "0"


def test_tax_id_checksum(fake):
    for _ in range(100):
        tid = fake.tax_id()
        assert validate_tax_id(tid), f"Invalid tax ID checksum: {tid}"
