from pathlib import Path
import argparse
from mini_file_audit.main import run_audit


class CliInputError(Exception):
    """Raised when CLI input is invalid or unusable."""


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description ="Audit a folder and generate CSV and JSON reports."
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

def validate_folder(folder: str) -> Path:
    folder_path = Path(folder)

    if not folder_path.exists():
        raise CliInputError(f"folder does not exist: {folder_path}")

    if not folder_path.is_dir():
        raise CliInputError(f"path is not a folder: {folder_path}")

    return folder_path

def validate_max_size(max_size: int) -> int:
    if max_size is not None and max_size < 0:
        raise CliInputError(f"max size {max_size} under 0")
    return max_size

def normalize_extensions(extensions: list[str] | None) -> list[str] | None:
    if extensions is None:
        return None

    normalized_extensions = []

    for extension in extensions:
        extension = extension.strip().lower()

        if extension in {"","."}:
            raise CliInputError(f"Invalid extension: {extension!r}")

        if not extension.startswith("."):
            extension = f".{extension}"

        normalized_extensions.append(extension)

    return sorted(set(normalized_extensions))




def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    try:
        folder = validate_folder(args.folder)
        max_size = validate_max_size(args.max_size)
        extensions = normalize_extensions(args.extensions)

        summary = run_audit(
            folder=folder,
            csv_output=Path(args.csv_output),
            json_output=Path(args.json_output),
            recursive=args.recursive,
            extensions=extensions,
            include_hidden=args.include_hidden,
            max_size=max_size,
        )
    except CliInputError as error:
        print(f"Error: {error}")
        return 1
    except OSError as error:
        print(f"Error: {error}")
        return 1

    print_summary(summary)
    return 0


def print_summary(summary: dict[str, object]) -> None:
    print(f"Files found: {summary['total_files']}")
    print(f"Total size: {summary['total_size_bytes']} bytes")
    print(f"CSV report: {summary['csv_report_path']}")
    print(f"Summary report: {summary['summary_report_path']}")

if __name__ == "__main__":
    raise SystemExit(main())
