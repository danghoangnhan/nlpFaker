# nlpFaker

[![PyPI version](https://img.shields.io/pypi/v/nlpFaker.svg)](https://pypi.org/project/nlpFaker/)
[![Python](https://img.shields.io/pypi/pyversions/nlpFaker.svg)](https://pypi.org/project/nlpFaker/)
[![CI](https://github.com/danghoangnhan/nlpFaker/actions/workflows/ci.yml/badge.svg)](https://github.com/danghoangnhan/nlpFaker/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A comprehensive fake data generator built specifically for **Taiwan (zh_TW)**. Zero dependencies.

## Features

- **16 generators** covering personal, contact, business, finance, date/time, and vehicle data
- **Taiwan-specific**: National IDs with valid checksums, 統一編號, ROC calendar dates, 09XX mobile numbers, real city/district/road addresses
- **Checksum validation**: generated IDs, tax IDs, and credit cards pass real validation algorithms
- **Reproducible**: seed support for deterministic output
- **Zero dependencies**: stdlib only, installs in seconds
- **CLI included**: generate data from the command line
- **Export**: JSON, CSV, SQL INSERT out of the box

## Architecture

```mermaid
classDiagram
    class BaseGenerator {
        <<abstract>>
        +_rng: Random
        +_load_lines(filename) list~str~
        +_load_weighted(filename) tuple
        +_weighted_choice(items, weights) str
        +generate()* str
    }

    class NlpFaker {
        +_rng: Random
        +name() str
        +id_number() str
        +mobile() str
        +address() str
        +email() str
        +company() str
        +landline() str
        +date() str
        +date_roc() str
        +credit_card() str
        +profile() dict
        +batch(field, n) list
    }

    BaseGenerator <|-- NameGenerator
    BaseGenerator <|-- IDNumberGenerator
    BaseGenerator <|-- MobileGenerator
    BaseGenerator <|-- AddressGenerator
    BaseGenerator <|-- EmailGenerator
    BaseGenerator <|-- CompanyGenerator
    BaseGenerator <|-- LandlineGenerator
    BaseGenerator <|-- DateTimeGenerator
    BaseGenerator <|-- LicensePlateGenerator
    BaseGenerator <|-- TaxIDGenerator
    BaseGenerator <|-- InvoiceGenerator
    BaseGenerator <|-- CreditCardGenerator
    BaseGenerator <|-- BankAccountGenerator
    BaseGenerator <|-- JobGenerator
    BaseGenerator <|-- CredentialGenerator

    NlpFaker --> NameGenerator : lazy init
    NlpFaker --> IDNumberGenerator : lazy init
    NlpFaker --> MobileGenerator : lazy init
    NlpFaker --> AddressGenerator : lazy init
    NlpFaker --> EmailGenerator : lazy init
    NlpFaker --> CompanyGenerator : lazy init
    NlpFaker --> LandlineGenerator : lazy init
    NlpFaker --> DateTimeGenerator : lazy init
    NlpFaker --> LicensePlateGenerator : lazy init
    NlpFaker --> TaxIDGenerator : lazy init
    NlpFaker --> InvoiceGenerator : lazy init
    NlpFaker --> CreditCardGenerator : lazy init
    NlpFaker --> BankAccountGenerator : lazy init
    NlpFaker --> JobGenerator : lazy init
    NlpFaker --> CredentialGenerator : lazy init

    class Exporter {
        +to_json(records, path)$
        +to_csv(records, path)$
        +to_sql(records, table, path)$
    }

    class Validators {
        +validate_id_number(id_str)$ bool
        +validate_tax_id(tax_str)$ bool
        +validate_mobile(mobile_str)$ bool
        +validate_credit_card(card_str)$ bool
    }
```

## Installation

```bash
pip install nlpFaker
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
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
fake.date_roc()       # "民國113年03月15日"
fake.credit_card()    # "4539123456789012"
```

## API Reference

### Personal & Identity

| Method | Description | Example |
|--------|-------------|---------|
| `name()` | Full name (last + first) | `陳怡君` |
| `first_name()` | First name (1-2 chars) | `怡君` |
| `last_name()` | Last name | `陳` |
| `id_number()` | National ID with valid checksum | `A123456789` |
| `username()` | Random username | `coolstar42` |
| `password(length=12)` | Mixed-character password | `xK9#mP2qLf!3` |

### Contact

| Method | Description | Example |
|--------|-------------|---------|
| `mobile()` | Mobile phone (09XX format) | `0912345678` |
| `landline()` | Landline with area code | `(02) 27481234` |
| `email()` | Email with TW domains | `ming.chen@gmail.com` |
| `address()` | Full Taiwan address | `台北市大安區和平東路二段42號3樓` |
| `postal_code()` | 3-digit postal code | `106` |

### Business

| Method | Description | Example |
|--------|-------------|---------|
| `company()` | Company name | `台灣科技股份有限公司` |
| `job_title()` | Job title | `軟體工程師` |
| `tax_id()` | 統一編號 with valid checksum | `12345670` |
| `invoice()` | 統一發票 number | `AB-12345678` |

### Finance

| Method | Description | Example |
|--------|-------------|---------|
| `credit_card(card_type=None)` | Luhn-valid (Visa/MC/JCB) | `4539123456789012` |
| `bank_account()` | Bank code + account number | `812-1234567890` |
| `bank_code()` | 3-digit bank code | `812` |

### Date & Time

| Method | Description | Example |
|--------|-------------|---------|
| `date(start, end)` | Date (YYYY/MM/DD) | `2024/03/15` |
| `date_roc(start, end)` | ROC calendar (民國) | `民國113年03月15日` |
| `time()` | Time (HH:MM:SS) | `14:30:22` |
| `datetime(start, end)` | Full datetime | `2024/03/15 14:30:22` |

### Vehicle

| Method | Description | Example |
|--------|-------------|---------|
| `license_plate(vehicle="car")` | TW license plate | `ABC-1234` |

## Profile & Batch Generation

```python
# Complete fake person profile
profile = fake.profile()
# {'name': '陳怡君', 'id_number': 'A123456789', 'email': '...',
#  'mobile': '...', 'landline': '...', 'address': '...',
#  'postal_code': '...', 'company': '...', 'job_title': '...',
#  'birthday': '...', 'credit_card': '...', 'bank_account': '...',
#  'username': '...'}

# Batch generation
names = fake.batch("name", 100)
ids = fake.batch("id_number", 50)
```

## Validation

Validate real or generated Taiwan data:

```python
from nlpFaker import validate_id_number, validate_tax_id, validate_mobile, validate_credit_card

validate_id_number("A123456789")  # True/False — checksum verification
validate_tax_id("12345670")       # True/False — 統一編號 checksum
validate_mobile("0912345678")     # True/False — format check
validate_credit_card("4539...")   # True/False — Luhn algorithm
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
nlpfaker name -n 10                    # 10 random names
nlpfaker profile -n 5 -f json          # 5 profiles as JSON
nlpfaker id_number -s 42               # reproducible with seed
nlpfaker mobile -n 100 -o phones.txt   # output to file
```

## Development

```bash
git clone https://github.com/danghoangnhan/nlpFaker.git
cd nlpFaker
uv sync --group dev
uv run python -m pytest -v
uv run ruff check nlpFaker/
```

## License

MIT

---

<details>
<summary><h2>中文說明</h2></summary>

### 簡介

**nlpFaker** 是一個專為 **台灣 (zh_TW)** 設計的假資料產生器，零外部相依套件。

提供 16 種產生器，涵蓋個人資料、聯絡方式、商業、金融、日期時間及車輛資訊，所有產生的身分證字號、統一編號、信用卡號碼皆通過真實的校驗演算法驗證。

### 特色

- **台灣專屬**：身分證字號（含檢查碼）、統一編號、民國年曆、09XX 手機號碼、真實縣市/區/路名地址
- **16 種產生器**：姓名、身分證、手機、地址、電子郵件、公司名稱、市話、日期時間、車牌、郵遞區號、統一編號、統一發票、信用卡、銀行帳號、職稱、帳號密碼
- **可重現**：支援 seed 參數，輸出結果可重現
- **零相依**：僅使用 Python 標準函式庫
- **內建 CLI**：可從命令列直接產生資料
- **匯出功能**：支援 JSON、CSV、SQL INSERT

### 快速開始

```python
from nlpFaker import NlpFaker

fake = NlpFaker(seed=42)

fake.name()           # 產生姓名，例如 "陳怡君"
fake.id_number()      # 產生身分證字號（含有效檢查碼）
fake.mobile()         # 產生手機號碼，例如 "0912345678"
fake.address()        # 產生完整地址
fake.company()        # 產生公司名稱
fake.date_roc()       # 產生民國日期，例如 "民國113年03月15日"
fake.tax_id()         # 產生統一編號（含有效檢查碼）
fake.credit_card()    # 產生信用卡號碼（通過 Luhn 演算法）

# 產生完整個人資料
profile = fake.profile()

# 批次產生
names = fake.batch("name", 100)  # 產生 100 個姓名
```

### 驗證功能

```python
from nlpFaker import validate_id_number, validate_tax_id

validate_id_number("A123456789")  # 驗證身分證字號檢查碼
validate_tax_id("12345670")       # 驗證統一編號檢查碼
```

### 命令列工具

```bash
nlpfaker name -n 10              # 產生 10 個隨機姓名
nlpfaker profile -n 5 -f json    # 產生 5 筆完整個人資料（JSON 格式）
nlpfaker id_number -s 42         # 使用固定種子產生身分證字號
```

</details>
