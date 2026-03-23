import re


def test_company_is_chinese(fake):
    for _ in range(20):
        company = fake.company()
        assert re.search(r"[\u4e00-\u9fff]", company), f"No Chinese chars: {company}"


def test_company_ends_with_suffix(fake):
    suffixes = ("有限公司", "股份有限公司", "集團", "企業有限公司", "實業有限公司",
                "科技股份有限公司", "企業股份有限公司")
    for _ in range(30):
        company = fake.company()
        assert any(company.endswith(s) for s in suffixes), f"Bad suffix: {company}"
