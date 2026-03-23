import re

from nlpFaker.id_number import IDNumberGenerator


AREAS = IDNumberGenerator.AREAS
WEIGHTS = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]


def _validate_id(id_str: str) -> bool:
    """Verify checksum of a Taiwan National ID number."""
    if not re.match(r"^[A-Z][0-9]{9}$", id_str):
        return False
    area_num = AREAS.index(id_str[0]) + 10
    digits = [area_num // 10, area_num % 10] + [int(c) for c in id_str[1:]]
    total = sum(d * w for d, w in zip(digits, WEIGHTS))
    return total % 10 == 0


def test_id_format(fake):
    for _ in range(50):
        id_num = fake.id_number()
        assert re.match(r"^[A-Z][0-9]{9}$", id_num), f"Bad format: {id_num}"


def test_id_checksum(fake):
    for _ in range(100):
        id_num = fake.id_number()
        assert _validate_id(id_num), f"Invalid checksum: {id_num}"
