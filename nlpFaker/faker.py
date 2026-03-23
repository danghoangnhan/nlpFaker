from __future__ import annotations

import datetime as dt
import random
from functools import cached_property

from nlpFaker.name import NameGenerator
from nlpFaker.address import AddressGenerator
from nlpFaker.mobile import MobileGenerator
from nlpFaker.id_number import IDNumberGenerator
from nlpFaker.email import EmailGenerator
from nlpFaker.company import CompanyGenerator
from nlpFaker.landline import LandlineGenerator
from nlpFaker.datetime_gen import DateTimeGenerator
from nlpFaker.license_plate import LicensePlateGenerator
from nlpFaker.tax_id import TaxIDGenerator
from nlpFaker.invoice import InvoiceGenerator
from nlpFaker.credit_card import CreditCardGenerator
from nlpFaker.bank_account import BankAccountGenerator
from nlpFaker.job import JobGenerator
from nlpFaker.credential import CredentialGenerator


class NlpFaker:
    """Unified facade for generating fake Taiwanese data.

    Usage:
        fake = NlpFaker(seed=42)
        fake.name()          # "陳怡君"
        fake.id_number()     # "A123456789"
        fake.mobile()        # "0912345678"
        fake.address()       # "台北市大安區和平東路二段42號3樓"
        fake.email()         # "ming.chen@gmail.com"
        fake.company()       # "台灣科技股份有限公司"
        fake.profile()       # dict with all fields
    """

    def __init__(self, seed: int | None = None) -> None:
        self._rng = random.Random(seed)

    # --- Lazy-init generators ---

    @cached_property
    def _name(self) -> NameGenerator:
        return NameGenerator(self._rng)

    @cached_property
    def _address(self) -> AddressGenerator:
        return AddressGenerator(self._rng)

    @cached_property
    def _mobile(self) -> MobileGenerator:
        return MobileGenerator(self._rng)

    @cached_property
    def _id_number(self) -> IDNumberGenerator:
        return IDNumberGenerator(self._rng)

    @cached_property
    def _email(self) -> EmailGenerator:
        return EmailGenerator(self._rng)

    @cached_property
    def _company(self) -> CompanyGenerator:
        return CompanyGenerator(self._rng)

    @cached_property
    def _landline(self) -> LandlineGenerator:
        return LandlineGenerator(self._rng)

    @cached_property
    def _datetime(self) -> DateTimeGenerator:
        return DateTimeGenerator(self._rng)

    @cached_property
    def _license_plate(self) -> LicensePlateGenerator:
        return LicensePlateGenerator(self._rng)

    @cached_property
    def _tax_id(self) -> TaxIDGenerator:
        return TaxIDGenerator(self._rng)

    @cached_property
    def _invoice(self) -> InvoiceGenerator:
        return InvoiceGenerator(self._rng)

    @cached_property
    def _credit_card(self) -> CreditCardGenerator:
        return CreditCardGenerator(self._rng)

    @cached_property
    def _bank_account(self) -> BankAccountGenerator:
        return BankAccountGenerator(self._rng)

    @cached_property
    def _job(self) -> JobGenerator:
        return JobGenerator(self._rng)

    @cached_property
    def _credential(self) -> CredentialGenerator:
        return CredentialGenerator(self._rng)

    # --- Name ---

    def name(self) -> str:
        """Generate a full Taiwanese name."""
        return self._name.generate()

    def first_name(self) -> str:
        """Generate a Taiwanese first name."""
        return self._name.first_name()

    def last_name(self) -> str:
        """Generate a Taiwanese last name."""
        return self._name.last_name()

    # --- Contact ---

    def address(self) -> str:
        """Generate a Taiwan address."""
        return self._address.generate()

    def postal_code(self) -> str:
        """Generate a Taiwan postal code."""
        return self._address.postal_code()

    def mobile(self) -> str:
        """Generate a Taiwan mobile phone number."""
        return self._mobile.generate()

    def landline(self) -> str:
        """Generate a Taiwan landline phone number."""
        return self._landline.generate()

    def email(self) -> str:
        """Generate an email address."""
        return self._email.generate()

    # --- Identity ---

    def id_number(self) -> str:
        """Generate a valid Taiwan National ID number."""
        return self._id_number.generate()

    def tax_id(self) -> str:
        """Generate a valid Taiwan Unified Business Number (統一編號)."""
        return self._tax_id.generate()

    # --- Business ---

    def company(self) -> str:
        """Generate a Taiwanese company name."""
        return self._company.generate()

    def job_title(self) -> str:
        """Generate a job title."""
        return self._job.generate()

    def invoice(self) -> str:
        """Generate a Taiwan Uniform Invoice number."""
        return self._invoice.generate()

    # --- Finance ---

    def credit_card(self, card_type: str | None = None) -> str:
        """Generate a Luhn-valid credit card number."""
        return self._credit_card.generate(card_type)

    def bank_account(self) -> str:
        """Generate a Taiwan bank account number."""
        return self._bank_account.generate()

    def bank_code(self) -> str:
        """Generate a Taiwan bank code."""
        return self._bank_account.bank_code()

    # --- Date/Time ---

    def date(self, start: dt.date | None = None, end: dt.date | None = None) -> str:
        """Generate a random date in YYYY/MM/DD format."""
        return self._datetime.date(start, end)

    def date_roc(self, start: dt.date | None = None, end: dt.date | None = None) -> str:
        """Generate a date in ROC calendar format (民國YYY年MM月DD日)."""
        return self._datetime.date_roc(start, end)

    def time(self) -> str:
        """Generate a random time in HH:MM:SS format."""
        return self._datetime.time()

    def datetime(self, start: dt.date | None = None, end: dt.date | None = None) -> str:
        """Generate a random datetime string."""
        return self._datetime.datetime(start, end)

    # --- Vehicle ---

    def license_plate(self, vehicle: str = "car") -> str:
        """Generate a Taiwan license plate number."""
        return self._license_plate.generate(vehicle)

    # --- Credentials ---

    def username(self) -> str:
        """Generate a random username."""
        return self._credential.username()

    def password(self, length: int = 12) -> str:
        """Generate a random password."""
        return self._credential.password(length)

    # --- Composite ---

    def profile(self) -> dict:
        """Generate a complete fake person profile."""
        return {
            "name": self.name(),
            "id_number": self.id_number(),
            "email": self.email(),
            "mobile": self.mobile(),
            "landline": self.landline(),
            "address": self.address(),
            "postal_code": self.postal_code(),
            "company": self.company(),
            "job_title": self.job_title(),
            "birthday": self.date(
                start=dt.date(1950, 1, 1),
                end=dt.date(2005, 12, 31),
            ),
            "credit_card": self.credit_card(),
            "bank_account": self.bank_account(),
            "username": self.username(),
        }

    # --- Utility ---

    def batch(self, field: str, n: int) -> list[str]:
        """Generate n values for the given field.

        Args:
            field: Method name (e.g., "name", "id_number", "mobile").
            n: Number of values to generate.
        """
        method = getattr(self, field)
        if not callable(method):
            raise ValueError(f"Unknown field: {field}")
        return [method() for _ in range(n)]
