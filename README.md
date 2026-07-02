# Resume Shortlisting System

A Python-based resume screening tool that automates candidate shortlisting by comparing skills against job requirements. This project helps recruiters efficiently identify qualified candidates by calculating match percentages and ranking them based on skill alignment.

## 📋 Overview

Reviewing hundreds of resumes manually is time-consuming and error-prone. This tool streamlines the screening process by:
- Automatically analyzing candidate skills
- Comparing them against required job skills
- Calculating match percentages
- Ranking candidates for easy shortlisting

Perfect for recruiters, HR teams, and hiring managers looking to save time and improve candidate selection consistency.

## ✨ Features

- 📥 **Load Candidates**: Import multiple resumes from a CSV file
- 🔍 **Skill Matching**: Compare candidate skills with job requirements
- 📊 **Match Scoring**: Calculate match percentage for each candidate
- 🏆 **Ranking**: Automatically rank candidates by match score
- ✅ **Selection Management**: Mark candidates as Selected or Not Selected
- 📤 **Export Results**: Save shortlisted candidates to a CSV file
- ⚖️ **Weighted Matching**: Assign priority weights to important skills
- 🎮 **Multiple Modes**: Run in interactive CLI or demo mode
- 📄 **PDF Reports**: Generate LinkedIn-ready project reports

## 🛠️ Tech Stack

- **Python 3.10+**
- **CSV Handling** - Native Python CSV module
- **CLI** - `argparse` for command-line interface
- **PDF Generation** - `reportlab`, `Pillow`, `pypdf`

## 📁 Project Structure

```
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

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone or download this repository:
```bash
git clone https://github.com/Creator-Naren/Resume-Short-lister.git
cd Resume-Short-lister
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage - Interactive Mode
```bash
python resume_shortlisting_system.py --input sample_resumes.csv
```
This opens an interactive prompt where you can enter required skills and select matching candidates.

### Run Demo
```bash
python resume_shortlisting_system.py --demo
```
Demonstrates the system with pre-configured skills and sample resumes.

### Generate PDF Report
```bash
python generate_linkedin_pdf.py
```
Creates a LinkedIn-ready PDF report of the project, perfect for portfolio sharing.

## 📋 Input Format

The input CSV file should follow this format:

```csv
Name,Skills
Alice Johnson,"Python, SQL, Flask, Git, Docker"
Bob Smith,"Java, Spring, SQL, React"
Carol Lee,"Python, React, SQL, Docker"
```

**Required columns:**
- `Name` - Candidate name
- `Skills` - Comma-separated list of candidate skills

## 🧮 Matching Methods

### Basic Skill Matching
Compares each candidate's skills with required skills:

```
Match Percentage = (Matched Required Skills / Total Required Skills) × 100
```

**Example:**
- Required Skills: Python, React, SQL, Docker
- Candidate Skills: Python, SQL, Docker
- Match: 3/4 = **75%**

### Weighted Skill Matching
Assigns priority weights to important skills for more precise matching:

```
Python: 3
SQL: 2
React: 2
Docker: 1
```

This approach is ideal when some skills are more critical for the role than others.

## 📊 Sample Output

When running the demo, you'll see output like:

**Required Skills:** Python, React, SQL, Docker

**Shortlisted Candidates:**
```
1. Alice Johnson     - 75.00% ✓
2. Carol Lee         - 75.00% ✓
3. Farhan Ali        - 75.00% ✓
```

Results are exported to `shortlisted_candidates.csv` for further processing.

## 📄 Generated Reports

A comprehensive project report is included at:
```
docs/LinkedIn_Resume_Shortlisting_Project_Report.pdf
```

The report contains:
- Project overview and objectives
- System architecture and features
- Screenshot demonstrations
- Sample outputs and metrics
- Use cases and applications

Perfect for adding to your portfolio or sharing on LinkedIn!

## 🔮 Future Enhancements

- [ ] PDF and DOCX resume parsing
- [ ] Web-based user interface
- [ ] Database integration for candidate management
- [ ] NLP-based skill extraction and normalization
- [ ] Job description parsing (extract skills automatically)
- [ ] Embedded charts and visualizations in reports
- [ ] REST API for integration with ATS systems
- [ ] Multi-language support

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 👤 Author

**Narendra Borhade**
- GitHub: [@Creator-Naren](https://github.com/Creator-Naren)

## 💬 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

**Made with ❤️ for HR professionals and developers**
