import json

from nlpFaker.cli import main


def test_cli_name(capsys):
    main(["name", "-n", "3", "-s", "42"])
    output = capsys.readouterr().out.strip()
    lines = output.split("\n")
    assert len(lines) == 3


def test_cli_profile_json(capsys):
    main(["profile", "-n", "2", "-s", "42"])
    output = capsys.readouterr().out.strip()
    data = json.loads(output)
    assert len(data) == 2
    assert "name" in data[0]


def test_cli_json_format(capsys):
    main(["id_number", "-n", "2", "-f", "json", "-s", "1"])
    output = capsys.readouterr().out.strip()
    data = json.loads(output)
    assert len(data) == 2


def test_cli_output_file(tmp_path):
    out = str(tmp_path / "out.txt")
    main(["mobile", "-n", "5", "-o", out])
    with open(out) as f:
        lines = f.read().strip().split("\n")
    assert len(lines) == 5
