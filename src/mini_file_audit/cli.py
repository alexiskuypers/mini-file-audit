from pathlib import Path
import argparse
from mini_file_audit.main import run_audit


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description = "Audit a folder and generate CSV and JSON reports."
    )

    parser.add_argument(
        "folder",
        help="folder to audit"
    )

    parser.add_argument(
        "--csv-output",
        default="output/report.csv",
        help="Path of the csv report"
    )

    parser.add_argument(
        "--json-output",
        default="output/summary.json",
        help="Path of the json report"
    )

    parser.add_argument(
        "--recursive",
        action="store_true",
        help="add recursivity in scan"
        )

    parser.add_argument(
        "--ext",
        dest="extensions",
        nargs="+",
        default=None,
        help="filter with extension")

    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="True add include hidden")

    parser.add_argument(
        "--max-size",
        type=int,
        default=None,
        help="maximal files syze in bytes")

    return parser

def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    summary = run_audit(
        folder=Path(args.folder),
        csv_output=Path(args.csv_output),
        json_output=Path(args.json_output),
        recursive=args.recursive,
        extensions=args.extensions,
        include_hidden=args.include_hidden,
        max_size=args.max_size,
    )
    print_summary(summary)
    return 0

def print_summary(summary: dict[str, object]) -> None:
    print(f"Files found: {summary['total_files']}")
    print(f"Total size: {summary['total_size_bytes']} bytes")
    print(f"CSV report: {summary['csv_report_path']}")
    print(f"Summary report: {summary['summary_report_path']}")

if __name__== "__main__":
    raise SystemExit(main())
