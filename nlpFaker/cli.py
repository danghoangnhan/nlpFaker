"""Command-line interface for nlpFaker."""

from __future__ import annotations

import argparse
import json
import sys

from nlpFaker.faker import NlpFaker


_FIELDS = [
    "name", "first_name", "last_name", "id_number", "mobile", "landline",
    "email", "address", "postal_code", "company", "job_title", "date",
    "date_roc", "time", "license_plate", "tax_id", "invoice",
    "credit_card", "bank_account", "username", "password", "profile",
]


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="nlpfaker",
        description="Generate fake Taiwanese data from the command line.",
    )
    parser.add_argument(
        "field",
        choices=_FIELDS,
        help="Type of data to generate.",
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Number of values to generate (default: 1).",
    )
    parser.add_argument(
        "-s", "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility.",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text).",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output file path (default: stdout).",
    )

    args = parser.parse_args(argv)
    fake = NlpFaker(seed=args.seed)

    if args.field == "profile":
        results = [fake.profile() for _ in range(args.count)]
        output = json.dumps(results, ensure_ascii=False, indent=2)
    else:
        method = getattr(fake, args.field)
        values = [method() for _ in range(args.count)]

        if args.format == "json":
            output = json.dumps(values, ensure_ascii=False, indent=2)
        else:
            output = "\n".join(values)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output + "\n")
    else:
        sys.stdout.write(output + "\n")


if __name__ == "__main__":
    main()
