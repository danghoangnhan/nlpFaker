# nlpFaker

Comprehensive fake data generator for Taiwanese (zh_TW) data. Zero dependencies.

## Installation

```bash
pip install nlpFaker
# or with uv
uv add nlpFaker
```

## Quick Start

```python
from nlpFaker import NlpFaker

fake = NlpFaker(seed=42)

fake.name()           # "陳怡君"
fake.id_number()      # "A123456789"
fake.mobile()         # "0912345678"
fake.address()        # "台北市大安區和平東路二段42號3樓"
fake.email()          # "ming.chen@gmail.com"
fake.company()        # "台灣科技股份有限公司"
```

## API Reference

### Personal

| Method | Description | Example |
|--------|-------------|---------|
| `name()` | Full name (last + first) | `陳怡君` |
| `first_name()` | First name (1-2 chars) | `怡君` |
| `last_name()` | Last name | `陳` |
| `id_number()` | National ID (valid checksum) | `A123456789` |
| `email()` | Email address | `ming.chen@gmail.com` |
| `username()` | Username | `coolstar42` |
| `password(length=12)` | Password (mixed chars) | `xK9#mP2qLf!3` |

### Contact

| Method | Description | Example |
|--------|-------------|---------|
| `mobile()` | Mobile phone (09XX) | `0912345678` |
| `landline()` | Landline phone | `(02) 27481234` |
| `address()` | Full address | `台北市大安區和平東路二段42號3樓` |
| `postal_code()` | Postal code (3-digit) | `106` |

### Business

| Method | Description | Example |
|--------|-------------|---------|
| `company()` | Company name | `台灣科技股份有限公司` |
| `job_title()` | Job title | `軟體工程師` |
| `tax_id()` | Unified Business Number (統一編號) | `12345670` |
| `invoice()` | Uniform Invoice number | `AB-12345678` |

### Finance

| Method | Description | Example |
|--------|-------------|---------|
| `credit_card(card_type=None)` | Luhn-valid credit card | `4111111111111111` |
| `bank_account()` | Bank account (code + number) | `812-1234567890` |
| `bank_code()` | Bank code | `812` |

### Date & Time

| Method | Description | Example |
|--------|-------------|---------|
| `date(start, end)` | Date (YYYY/MM/DD) | `2024/03/15` |
| `date_roc(start, end)` | ROC calendar date | `民國113年03月15日` |
| `time()` | Time (HH:MM:SS) | `14:30:22` |
| `datetime(start, end)` | Full datetime | `2024/03/15 14:30:22` |

### Vehicle

| Method | Description | Example |
|--------|-------------|---------|
| `license_plate(vehicle="car")` | License plate | `ABC-1234` |

### Composite

```python
# Generate a complete profile
profile = fake.profile()
# Returns dict with: name, id_number, email, mobile, landline,
# address, postal_code, company, job_title, birthday,
# credit_card, bank_account, username

# Batch generation
names = fake.batch("name", 100)  # list of 100 names
```

## Validation

```python
from nlpFaker import validate_id_number, validate_tax_id, validate_mobile, validate_credit_card

validate_id_number("A123456789")  # True/False
validate_tax_id("12345670")       # True/False
validate_mobile("0912345678")     # True/False
validate_credit_card("4111...")   # True/False (Luhn check)
```

## Export

```python
from nlpFaker import NlpFaker, Exporter

fake = NlpFaker(seed=1)
records = [fake.profile() for _ in range(1000)]

Exporter.to_json(records, "data.json")
Exporter.to_csv(records, "data.csv")
Exporter.to_sql(records, "people", "data.sql")
```

## CLI

```bash
nlpfaker name -n 10              # 10 random names
nlpfaker profile -n 5 -f json    # 5 profiles as JSON
nlpfaker id_number -s 42         # reproducible with seed
nlpfaker mobile -n 100 -o out.txt  # output to file
```

## Development

```bash
uv sync --group dev
uv run python -m pytest -v
```

## License

MIT
