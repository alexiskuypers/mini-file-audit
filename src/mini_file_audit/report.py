from pathlib import Path
import csv
import json
import logging


logger = logging.getLogger(__name__)

CSV_HEADERS = ["index", "name", "path", "extension", "size_bytes"]

def write_csv_report(files : list[Path], csv_output : Path ) -> Path:
    csv_output.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Writing CSV report to: %s", csv_output)

    with csv_output.open('w',encoding='utf-8', newline="") as report_file:
        csv_writer = csv.writer(report_file)

        csv_writer.writerow(CSV_HEADERS)

        for index, path in enumerate(files, start=1) :
            csv_writer.writerow([
                index,
                path.name,
                str(path),
                path.suffix,
                path.stat().st_size
            ])

    logger.info("CSV report written to: %s", csv_output)

    return csv_output

def write_summary_report(summary : dict[str, object], json_output : Path) -> Path:
    json_output.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Writing summary report to: %s", json_output)

    with json_output.open('w', encoding='utf-8') as report_file:
        json.dump(summary, report_file, indent=2, ensure_ascii=False)

    logger.info("Summary report written to: %s", json_output)

    return json_output




