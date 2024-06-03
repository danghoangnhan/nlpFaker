from src.name import NameGenerator
from src.mobile import MobileGenerator
from src.id_number import IDNumberGenerator
from src.address import AddressGenerator

class DataGenerator:
    def __init__(self):
        self.Name = NameGenerator()
        self.Mobile = MobileGenerator()
        self.IDNumber = IDNumberGenerator()
        self.Address = AddressGenerator()
