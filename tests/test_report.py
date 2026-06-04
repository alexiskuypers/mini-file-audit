import pytest
import json
import csv
from mini_file_audit.report import CSV_HEADERS, write_csv_report, write_summary_report


def test_write_csv_report_output(tmp_path):
    file_path = tmp_path/"test.txt"
    file_path.write_text("hello")

    csv_output = tmp_path/"output"/"report.csv"
    result = write_csv_report([file_path], csv_output)

    with csv_output.open(encoding="utf-8", newline="") as report_file:
        rows = list(csv.reader(report_file))

    assert result == csv_output
    assert csv_output.exists()
    assert rows[0] == CSV_HEADERS
    assert rows[1] == [
        "1",
        "test.txt",
        str(file_path),
        ".txt",
        "5"
    ]


def test_write_summary_report_output(tmp_path):
    summary: dict[str, object] = {
        "test": 1
    }

    json_output = tmp_path/"output"/"summary.json"
    result = write_summary_report(summary, json_output)
    data = json.loads(json_output.read_text(encoding="utf-8"))

    assert result == json_output
    assert json_output.exists()
    assert data == summary
