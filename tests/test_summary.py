import pytest
from pathlib import Path
from mini_file_audit.summary import summarize_extensions, summarize_sizes, build_summary


def test_summarize_extensions():
    data: list[Path] = [
        Path("test.py"),
        Path("test.txt"),
        Path("test"),
        Path("name.py"),
    ]
    content = summarize_extensions(data)

    assert content == {
        "extension_count": 2,
        "files_by_extension": {
            ".py": 2,
            ".txt": 1,
            "no_extension": 1,
        }
    }


def test_summarizes_size(tmp_path):
    file_path_1 = tmp_path/"test.txt"
    file_path_2 = tmp_path/"test2.txt"
    file_path_3 = tmp_path /"test3.txt"
    file_path_1.write_text("test")
    file_path_2.write_text("test_2")
    file_path_3.write_text("")

    data: list[Path] = [
        file_path_1,
        file_path_2,
        file_path_3,
    ]

    content = summarize_sizes(data)

    assert content == {
        "total_files": 3,
        "total_size_bytes": 10,
        "average_file_size_bytes": 10 / 3,
        "largest_file": {
            "name": "test2.txt",
            "path": str(file_path_2),
            "size_bytes": 6
        },
        "smallest_file": {
            "name": "test3.txt",
            "path": str(file_path_3),
            "size_bytes": 0
        },
        "empty_files_count": 1,
    }

def test_summarizes_size_empty_list():

    data: list[Path] = []

    content = summarize_sizes(data)

    assert content == {
        "total_files": 0,
        "total_size_bytes": 0,
        "average_file_size_bytes": 0,
        "largest_file": None,
        "smallest_file": None,
        "empty_files_count": 0,
    }


def test_build_summary(tmp_path):
    path_file_1 = tmp_path/"text.txt"
    path_file_2 = tmp_path/"text2.txt"
    path_file_1.write_text("test")
    path_file_2.write_text("test2")

    data = [
        path_file_1,
        path_file_2
    ]
    csv_output = tmp_path/"csv_output"/"report.csv"
    json_output = tmp_path/"json_output"/"summary.json"

    content = build_summary(
    files=data,
    recursive=True,
    csv_output=csv_output,
    json_output=json_output,
)

    assert content["csv_report_path"] == str(csv_output)
    assert content["summary_report_path"] == str(json_output)
    assert content["total_files"] == 2
    assert content["files_by_extension"] == {".txt": 2}
    assert content["recursive"] is True
