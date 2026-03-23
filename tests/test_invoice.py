import re


def test_invoice_format(fake):
    for _ in range(50):
        inv = fake.invoice()
        assert re.match(r"^[A-Z]{2}-\d{8}$", inv), f"Bad invoice: {inv}"
