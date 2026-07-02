# Resume Shortlisting System

A Python-based resume screening tool that helps shortlist candidates by comparing their skills with a job's required skills. The project reads candidate data from a CSV file, calculates match percentages, ranks candidates, and exports shortlisted results.

## Overview

Recruiters often need to scan many resumes against a fixed set of job requirements. This project automates a simple version of that workflow by checking candidate skills against required skills and marking candidates as `Selected` or `Not Selected` based on a configurable threshold.

## Features

- Load multiple candidate resumes from a CSV file
- Match candidate skills with required job skills
- Calculate match percentage for every candidate
- Rank candidates from highest to lowest match
- Mark candidates as `Selected` or `Not Selected`
- Export shortlisted candidates to a CSV file
- Support weighted skill matching for priority skills
- Run in interactive CLI mode or demo mode
- Generate a LinkedIn-ready project report PDF

## Tech Stack

- Python 3.10+
- CSV file handling
- Command-line interface with `argparse`
- PDF/report generation with:
  - `reportlab`
  - `Pillow`
  - `pypdf`

## Project Structure

```text
resume-shortlisting-system/
├── docs/
│   ├── images/
│   └── LinkedIn_Resume_Shortlisting_Project_Report.pdf
├── generate_linkedin_pdf.py
├── resume_shortlisting_system.py
├── sample_resumes.csv
├── shortlisted_candidates.csv
├── requirements.txt
├── LICENSE
└── README.md
```

## CSV Input Format

The input CSV file must contain these columns:

```csv
Name,Skills
Alice Johnson,"Python, SQL, Flask, Git, Docker"
Bob Smith,"Java, Spring, SQL, React"
```

## Installation

Clone or download the project, then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the interactive resume shortlisting system:

```bash
python resume_shortlisting_system.py --input sample_resumes.csv
```

Run the built-in demo:

```bash
python resume_shortlisting_system.py --demo
```

Generate the LinkedIn project report PDF:

```bash
python generate_linkedin_pdf.py
```

## Matching Methods

### Basic Skill Matching

Basic matching compares each candidate's skills with the required skills and calculates a percentage:

```text
Match Percentage = Matched Required Skills / Total Required Skills * 100
```

### Weighted Skill Matching

Weighted matching lets important skills carry more value. For example:

```text
python:3, sql:2, react:2, docker:1
```

This is useful when some skills are more important than others for a role.

## Sample Demo

The demo uses these required skills:

```text
Python, React, SQL, Docker
```

Example shortlisted candidates:

```text
Alice Johnson - 75.00%
Carol Lee - 75.00%
Farhan Ali - 75.00%
```

Selected candidates are exported to:

```text
shortlisted_candidates.csv
```

## Report

A project report PDF is included here:

```text
docs/LinkedIn_Resume_Shortlisting_Project_Report.pdf
```

It contains a summary of the project, screenshots, charts, and output examples suitable for sharing on LinkedIn or adding to a portfolio.

## Future Improvements

- Add PDF and DOCX resume parsing
- Add a web interface
- Store candidate data in a database
- Add natural language processing for smarter skill extraction
- Support job descriptions as input
- Add charts directly in the CLI report workflow

## Author

Narendra Borhade

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
