# mini-file-audit
Short one-sentence description of the project.
Example: mini-file-audit is a Python CLI tool that scans a local folder and generates a simple CSV file audit report.
Objective
Explain what the project does and why it exists.
Example: This project is built as part of my backend Python roadmap.
The goal is to practice Linux terminal usage, Git workflow, Python script execution, and basic project documentation.
Features
Current features:
- Project structure initialized
- Python package created under `src/mini_file_audit`
- Placeholder modules created for CLI, orchestration, scanning and reporting
Planned features:
- Read a folder path from the command line
- Filter files by extension
- Generate a CSV report with file name, path and size
- Display a terminal summary
- Return clear exit codes
Installation
Installation instructions will be added when the project is ready to be cloned and executed.
Usage
python3 src/mini_file_audit/cli.py examples/sample-folder
with option : 
python3 src/mini_file_audit/cli.py examples/sample-folder --ext .txt --output output/report.csv

Example output
Scanned folder: ./data
Files found: 12
Total size: 3.4 MB
Project structure
mini-file-audit/
├── README.md
├── pyproject.toml
├── .gitignore
├── examples/
│   └── sample-folder/
├── output/
├── src/
│   └── mini_file_audit/
│       ├── __init__.py
│       ├── cli.py
│       ├── main.py
│       ├── scanner.py
│       └── report.py
└── tests/
Status
Project in progress.
Next steps
    • Add folder scanning 
    • Add extension filtering 
    • Generate a CSV report 
    • Add logs 
