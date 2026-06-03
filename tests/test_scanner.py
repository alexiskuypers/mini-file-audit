import pytest
from pathlib import Path
from mini_file_audit.scanner import is_hidden_path, scan_folder


@pytest.mark.parametrize(
    "relative_path, expected",
    [
        ("dir_2/files.txt", False),
        (".dir_2/files.txt", True),
        ("dir_2/.files.txt", True),
    ]
)
def test_is_hidden_path(relative_path, expected):
    root = Path("dir")/ "dir_1"
    path = root/relative_path
    content = is_hidden_path(path, root)

    assert content is expected


def test_scan_folder_recursivity(tmp_path):
    folder = tmp_path
    sub_dir = folder/ "dir_1"/ "dir_2"
    sub_dir.mkdir(parents=True, exist_ok=True)
    file_test = sub_dir/ "text.txt"
    file_test.write_text("hello")

    with_recursivity = scan_folder(
        folder=folder,
        recursive=True,
        extensions=None,
        include_hidden=False,
        max_size=None
        )
    without_recursivity = scan_folder(
        folder=folder,
        recursive=False,
        extensions=None,
        include_hidden=False,
        max_size=None
        )

    assert with_recursivity == [file_test]
    assert without_recursivity == []

def test_scan_folder_filter_by_extensions(tmp_path):
    file_py = tmp_path / "file_1.py"
    file_txt = tmp_path / "file_2.txt"
    file_md = tmp_path / "file_3.md"

    file_py.write_text("hello")
    file_txt.write_text("hello")
    file_md.write_text("hello")

    content = scan_folder(
        folder=tmp_path,
        recursive=False,
        extensions=[".py"],
        include_hidden=False,
        max_size=None
        )

    assert content == [file_py]


def test_scan_folder_filter_hidden_files(tmp_path):
    file_hidden = tmp_path/ ".test.txt"
    visible_file = tmp_path/ "test.py"

    file_hidden.write_text("test")
    visible_file.write_text("test")

    result_with_hidden = scan_folder(
        folder=tmp_path,
        recursive=False,
        extensions=None,
        include_hidden=True,
        max_size=None
        )
    result_without_hidden = scan_folder(
        folder=tmp_path,
        recursive=False,
        extensions=None,
        include_hidden=False,
        max_size=None
        )

    assert result_with_hidden == [file_hidden,visible_file]
    assert result_without_hidden == [visible_file]

def test_scan_folder_filter_by_max_size(tmp_path):
    file_under_max_size = tmp_path/ "test_under.txt"
    file_over_max_size = tmp_path/ "test_over.txt"

    file_under_max_size.write_text("test")
    file_over_max_size.write_text("hello_world")

    result_max_6 = scan_folder(
        folder=tmp_path,
        recursive=False,
        extensions=None,
        include_hidden=False,
        max_size=6
        )
    result_max_20 = scan_folder(
        folder=tmp_path,
        recursive=False,
        extensions=None,
        include_hidden=False,
        max_size=20
        )

    assert result_max_6 == [file_under_max_size]
    assert result_max_20 == [file_over_max_size, file_under_max_size]


