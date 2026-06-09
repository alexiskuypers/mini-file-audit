# mini-file-audit

`mini-file-audit` is a small Python CLI tool that scans a folder and generates simple audit reports.

It can:

* scan files in a given folder;
* optionally scan recursively;
* filter files by extension;
* filter files by maximum size;
* generate a CSV report;
* generate a JSON summary;
* display a terminal summary;
* write simple execution logs.

This project was built as a first structured Python CLI project in my roadmap toward a Junior Backend Python Developer profile.

## Project goals

The goal of this project is not to build a complex production tool.

The goal is to practice core backend foundations:

* Python project structure with `src/`;
* CLI development with `argparse`;
* file handling with `pathlib`;
* CSV and JSON report generation;
* basic logging;
* automated tests with `pytest`;
* minimal packaging with `pyproject.toml`.

## Installation

Clone the repository:

```bash
git clone git@github.com:alexiskuypers/mini-file-audit.git
cd mini-file-audit
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode:

```bash
python3 -m pip install -e ".[dev]"
```

## Usage

Basic usage:

```bash
mini-file-audit examples/sample-folder
```

Recursive scan:

```bash
mini-file-audit examples/sample-folder --recursive
```

Filter by extension:

```bash
mini-file-audit examples/sample-folder --ext txt csv
```

Generate CSV and JSON reports:

```bash
mini-file-audit examples/sample-folder \
  --recursive \
  --csv-output output/report.csv \
  --json-output output/summary.json
```

Filter files by maximum size in bytes:

```bash
mini-file-audit examples/sample-folder --max-size 1000
```

Display help:

```bash
mini-file-audit --help
```

## Example output

```txt
Files found: 3
Total size: 1240 bytes
CSV report: output/report.csv
Summary report: output/summary.json
```

## Reports

The CSV report contains information about the scanned files.

The JSON summary contains a global summary of the audit, such as:

* number of files;
* total size;
* file extensions found;
* largest file;
* smallest file.

Generated reports are written to the `output/` folder when output paths are provided.

## Logs

The application writes simple execution logs in the `logs/` folder.

Logs are used to track:

* audit start;
* scan execution;
* report generation;
* successful completion;
* expected errors.

## Run tests

Install the development dependencies first:

```bash
python3 -m pip install -e ".[dev]"
```

Run the test suite:

```bash
python3 -m pytest
```

Run tests with verbose output:

```bash
python3 -m pytest -v
```

## Project structure

```txt
mini-file-audit/
├── src/
│   └── mini_file_audit/
│       ├── cli.py
│       ├── main.py
│       ├── scanner.py
│       ├── report.py
│       ├── summary.py
│       └── logging_config.py
├── tests/
├── examples/
├── pyproject.toml
├── README.md
└── .gitignore
```

## What this project demonstrates

This project demonstrates that I can:

* structure a small Python package;
* build a usable command-line interface;
* validate CLI inputs;
* work with files and folders using `pathlib`;
* generate CSV and JSON outputs;
* separate responsibilities across modules;
* write basic automated tests;
* configure simple application logs.

## Known limits

This is a Phase 1 learning project.

It does not include:

* a database;
* a REST API;
* Docker;
* CI/CD;
* advanced error handling;
* production-grade logging;
* complex business logic.

Those topics are planned for later projects in my backend roadmap.

## Roadmap context

This project belongs to the first phase of my backend learning roadmap: building a clean development workflow with Linux, Git, Python environments, project structure, CLI usage, tests and basic logs.

The next step is to move toward more robust Python engineering with a project focused on CSV data cleaning, validation, explicit errors and better test coverage.
