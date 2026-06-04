from pathlib import Path
from mini_file_audit.scanner import scan_folder
from mini_file_audit.report import write_csv_report, write_summary_report
from mini_file_audit.summary import build_summary


def run_audit(
    folder: Path,
    csv_output: Path,
    json_output: Path,
    recursive: bool = False,
    extensions: list[str] | None = None,
    include_hidden: bool = False,
    max_size: int | None = None,
) -> dict[str, object]:

    files = scan_folder(
        folder=folder,
        recursive=recursive,
        extensions=extensions,
        include_hidden=include_hidden,
        max_size=max_size
    )
    write_csv_report(files, csv_output)

    summary = build_summary(
        files,
        recursive=recursive,
        csv_output=csv_output,
        json_output=json_output
    )
    write_summary_report(summary, json_output)

    return summary













