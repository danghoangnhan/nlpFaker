import random

from nlpFaker._base import BaseGenerator


class BankAccountGenerator(BaseGenerator):
    """Generator for Taiwan bank account numbers.

    Produces a bank code (3 digits) and account number (10-14 digits).
    """

    # Common Taiwan bank codes: code -> name (for reference)
    _BANK_CODES = [
        "004",  # 台灣銀行
        "005",  # 土地銀行
        "006",  # 合作金庫
        "007",  # 第一銀行
        "008",  # 華南銀行
        "009",  # 彰化銀行
        "011",  # 上海商銀
        "012",  # 台北富邦
        "013",  # 國泰世華
        "017",  # 兆豐銀行
        "021",  # 花旗銀行
        "048",  # 王道銀行
        "050",  # 台灣企銀
        "052",  # 渣打銀行
        "053",  # 台中銀行
        "081",  # 匯豐銀行
        "103",  # 新光銀行
        "108",  # 陽信銀行
        "118",  # 板信銀行
        "147",  # 三信銀行
        "700",  # 中華郵政
        "803",  # 聯邦銀行
        "805",  # 遠東銀行
        "806",  # 元大銀行
        "807",  # 永豐銀行
        "808",  # 玉山銀行
        "809",  # 凱基銀行
        "810",  # 星展銀行
        "812",  # 台新銀行
        "816",  # 安泰銀行
        "822",  # 中國信託
    ]

    def __init__(self, rng: random.Random | None = None) -> None:
        super().__init__(rng)

    def generate(self) -> str:
        """Generate a Taiwan bank account number (bank_code-account)."""
        bank_code = self._rng.choice(self._BANK_CODES)
        length = self._rng.choice([10, 11, 12, 13, 14])
        account = "".join(str(self._rng.randint(0, 9)) for _ in range(length))
        return f"{bank_code}-{account}"

    def bank_code(self) -> str:
        """Generate a Taiwan bank code."""
        return self._rng.choice(self._BANK_CODES)
