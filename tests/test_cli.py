import pytest
from mini_file_audit.cli import (
    normalize_extensions,
    CliInputError,
    validate_max_size,
    validate_folder,
    create_parser,
    print_summary,
)


#Test for normalize_extension
@pytest.mark.parametrize(
        "a, expected",
        [
            ([".py", ".txt"], [".py", ".txt"]),
            (["PY", " .tXt "], [".py", ".txt"]),
            (["PY", "py "], [".py"])
        ]
)
def test_normalize_extensions(a, expected):
    assert normalize_extensions(a) == expected

@pytest.mark.parametrize(
        "extension",
        [
            [""],
            [","],
            ["."],
        ]
)
def test_normalize_extensions_rejects_invalid_extensions(extension):
    with pytest.raises(CliInputError):
        normalize_extensions(extension)

# Test for validate_max_size
@pytest.mark.parametrize(
        "entry, expected",
        [
            (0, 0),
            (10_000, 10_000),
            (None, None)
        ]
)
def test_validate_max_size(entry, expected):
    assert validate_max_size(entry) == expected

@pytest.mark.parametrize(
    "entry",
    [
        -1,
        -10_000
    ]
)
def test_validate_max_size_reject_negative_values(entry):
    with pytest.raises(CliInputError):
        validate_max_size(entry)

# Test for validate_folder
def test_validate_folder_accept_existing_folder(tmp_path):
    result = validate_folder(str(tmp_path))
    assert result == tmp_path

def test_validate_folder_rejects_missing_folder(tmp_path):
    missing_folder = tmp_path/"does_not_exist"
    with pytest.raises(CliInputError):
        validate_folder(str(missing_folder))

def test_validate_folder_rejects_existing_file_path(tmp_path):
    files_path = tmp_path/"file.txt"
    files_path.write_text("hello")
    with pytest.raises(CliInputError):
        validate_folder(str(files_path))


# Test create_parser
def test_create_parser_parses_required_folder():
    parser = create_parser()
    args = parser.parse_args(["some-folder"])

    assert args.folder == "some-folder"

def test_create_parser_uses_default_values():
    parser = create_parser()
    args = parser.parse_args(["some-folder"])

    assert args.folder == "some-folder"
    assert args.csv_output == "output/report.csv"
    assert args.json_output == "output/summary.json"
    assert args.recursive is False
    assert args.extensions is None
    assert args.include_hidden is False
    assert args.max_size is None

def test_create_parser_parses_options():
    parser = create_parser()
    args = parser.parse_args([
        "some-folder",
        "--recursive",
        "--include-hidden",
        "--ext", ".py", ".txt",
        "--max-size", "10_000"
    ])

    assert args.folder == "some-folder"
    assert args.recursive is True
    assert args.include_hidden is True
    assert args.extensions == [".py", ".txt"]
    assert args.max_size == 10_000

# Test print_summary
def test_summary_outputs(capsys):
    summary = {
        "total_files": 3,
        "total_size_bytes": 1500,
        "csv_report_path": "output/report.csv",
        "summary_report_path": "output/summary.json",
}
    print_summary(summary)

    captured = capsys.readouterr()

    assert "Files found: 3" in captured.out
    assert "Total size: 1500 bytes" in captured.out
    assert "CSV report: output/report.csv" in captured.out
    assert "Summary report: output/summary.json" in captured.out

