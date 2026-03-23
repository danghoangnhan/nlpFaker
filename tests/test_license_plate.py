import re


def test_car_plate_format(fake):
    for _ in range(50):
        plate = fake.license_plate("car")
        assert re.match(r"^[A-Z]{3}-\d{4}$|^\d{4}-[A-Z]{2}$", plate), f"Bad car plate: {plate}"


def test_motorcycle_plate_format(fake):
    for _ in range(50):
        plate = fake.license_plate("motorcycle")
        assert re.match(r"^[A-Z]{2,3}-\d{4}$", plate), f"Bad motorcycle plate: {plate}"
