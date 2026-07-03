# Resume Shortlisting System

A lightweight Python web app and CLI tool that automates resume screening by extracting candidate skills from CSV files, comparing them with job requirements, and generating ranked shortlists of qualified candidates. Ideal for recruiters, HR professionals, and hiring teams who need to process multiple resumes quickly and objectively.

**Live Demo:** [Try the browser-based demo](https://raw.githack.com/Creator-Naren/Resume-Short-lister/main/docs/index.html)

---

## 📋 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Interactive CLI Mode](#interactive-cli-mode)
  - [Demo Mode](#demo-mode)
  - [Programmatic Usage](#programmatic-usage)
- [Matching Algorithms](#matching-algorithms)
  - [Basic Skill Matching](#basic-skill-matching)
  - [Weighted Skill Matching](#weighted-skill-matching)
- [Input & Output Formats](#input--output-formats)
  - [CSV Input Format](#csv-input-format)
  - [CSV Output Format](#csv-output-format)
- [Configuration](#configuration)
- [Examples](#examples)
- [Documentation](#documentation)
- [Future Improvements](#future-improvements)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Author](#author)

---

## ✨ Features

- **📂 CSV-based Resume Processing** - Load candidate data from CSV files with flexible skill lists
- **🎯 Skill Matching** - Two algorithms for comparing candidate skills with job requirements:
  - Basic matching for equal-weight skills
  - Weighted matching for priority-based skill valuation
- **📊 Candidate Ranking** - Automatic ranking by match percentage (highest to lowest)
- **✅ Selection Classification** - Mark candidates as "Selected" or "Not Selected" based on threshold
- **💾 CSV Export** - Export shortlisted candidates with metadata to CSV format
- **🌐 Browser Demo** - Interactive web interface powered by GitHub Pages
- **📝 Report Generation** - Generate professional project reports (PDF included)
- **⚙️ Customizable Thresholds** - Set selection thresholds per job requirement
- **🖥️ Interactive CLI** - Menu-driven command-line interface for easy interaction
- **📋 Batch Processing** - Process 8+ sample candidates in seconds

---

## 🚀 Quick Start

### For CLI Users

```bash
# Clone the repository
git clone https://github.com/Creator-Naren/Resume-Short-lister.git
cd Resume-Short-lister

# Install dependencies
pip install -r requirements.txt

# Run the demo
python resume_shortlisting_system.py --demo

# Or use your own CSV file
python resume_shortlisting_system.py --input your_resumes.csv
```

### For Browser Users

Visit the [live demo](https://raw.githack.com/Creator-Naren/Resume-Short-lister/main/docs/index.html) in any modern web browser—no installation required.

---

## 🛠 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Language** | Python | 3.10+ |
| **CSV Processing** | Standard `csv` module | Built-in |
| **CLI Framework** | `argparse` | Built-in |
| **PDF Generation** | `reportlab` | 4.0.0+ |
| **Image Handling** | `Pillow` | 10.0.0+ |
| **PDF Manipulation** | `pypdf` | 4.0.0+ |

### Dependencies
- `reportlab>=4.0.0` - Report and document generation
- `Pillow>=10.0.0` - Image processing for PDF assets
- `pypdf>=4.0.0` - PDF manipulation and merging

---

## 📁 Project Structure

```
Resume-Short-lister/
├── resume_shortlisting_system.py    Main application (CLI + core logic)
├── sample_resumes.csv                Sample data with 8 candidate profiles
├── shortlisted_candidates.csv         Output from demo run
├── requirements.txt                   Python package dependencies
├── LICENSE                            MIT License
├── README.md                          This file
└── docs/
    ├── index.html                     Browser-based interactive demo
    ├── .nojekyll                      GitHub Pages configuration
    ├── images/                        Images for documentation
    └── LinkedIn_Resume_Shortlisting_Project_Report.pdf  
                                       Professional project report
```

### How It Works

**Runtime Flow:**
1. User launches the CLI or opens the browser demo
2. Application loads candidate resumes from CSV file
3. User specifies required skills (and optional weights)
4. System matches candidate skills against requirements using chosen algorithm
5. Results ranked by match percentage
6. User selects candidates to export to CSV output file

**Data Flow:**
- **Input:** `sample_resumes.csv` (Name + Skills columns)
- **Processing:** String normalization → Skill parsing → Intersection calculation → Percentage computation
- **Output:** `shortlisted_candidates.csv` (Rank, Name, Match%, Matched Skills)

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git (for cloning)

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/Creator-Naren/Resume-Short-lister.git
cd Resume-Short-lister

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Verify installation
python resume_shortlisting_system.py --help
```

---

## 🎮 Usage

### Interactive CLI Mode

Run the program with your own resume file:

```bash
python resume_shortlisting_system.py --input your_resumes.csv
```

**Menu Options:**

```
=== Resume Shortlisting System ===
1. Basic Skill Matching
2. Weighted Skill Matching (Bonus)
3. Exit
```

#### Option 1: Basic Skill Matching

All required skills have equal importance.

```
Choose an option (1/2/3): 1
Enter required skills (comma-separated): Python, SQL, Docker
Enter selection threshold percentage (default 60): 75
```

**Output:**
```
=== Candidate Ranking ===
Rank  Name                 Match %    Status         Matched Skills
----  ----                 -------    ------         ---------------
1     Alice Johnson        75.00      Selected       Docker, Python, Sql
2     Carol Lee            75.00      Selected       Python, React, Sql
3     Farhan Ali           75.00      Selected       Python, React, Sql
4     Bob Smith            33.33      Not Selected   Sql
...
```

**Export Option:**
```
Export selected candidates to CSV? (y/n): y
Exported 3 selected candidates to shortlisted_candidates.csv
```

#### Option 2: Weighted Skill Matching

Assign importance weights to skills (bonus feature).

```
Choose an option (1/2/3): 2
Enter weighted skills (skill:weight comma-separated): python:3, sql:2, react:2, docker:1
Enter selection threshold percentage (default 60): 60
```

Each skill contributes its weight to the total score. Higher weights = more important skills.

```
Export selected candidates to CSV? (y/n): y
Exported 4 selected candidates to shortlisted_candidates_weighted.csv
```

### Demo Mode

Run a pre-configured demo with sample data:

```bash
python resume_shortlisting_system.py --demo
```

**Demo Settings:**
- Required Skills: `Python, React, SQL, Docker`
- Threshold: 60%
- Input: `sample_resumes.csv` (8 sample candidates)
- Output: `shortlisted_candidates.csv`

**Expected Output:**
```
Running demo with required skills: Python, React, SQL, Docker

=== Candidate Ranking ===
Rank  Name                 Match %    Status         Matched Skills
----  ----                 -------    ------         ---------------
1     Alice Johnson        75.00      Selected       Docker, Python, Sql
2     Carol Lee            75.00      Selected       Python, React, Sql
3     Farhan Ali           75.00      Selected       Python, React, Sql
```

### Programmatic Usage

Import and use the module in your own Python scripts:

```python
from pathlib import Path
from resume_shortlisting_system import (
    load_resumes, 
    basic_match, 
    weighted_match, 
    export_selected,
    parse_skills
)

# Load resumes from CSV
resumes = load_resumes(Path("sample_resumes.csv"))

# Define required skills
required_skills = parse_skills("Python, SQL, Docker")

# Run basic matching
results = basic_match(resumes, required_skills, threshold=60.0)

# Export results
export_selected(results, Path("my_shortlist.csv"))

# Access individual results programmatically
for result in results:
    print(f"{result.name}: {result.match_percentage}%")
```

---

## 🔍 Matching Algorithms

### Basic Skill Matching

**Formula:**
```
Match % = (Matched Skills ÷ Total Required Skills) × 100
```

**Example:**
```
Required: Python, SQL, Docker (3 skills)
Candidate has: Python, SQL (2 matches)
Match % = (2 ÷ 3) × 100 = 66.67%
```

**Use Case:** All skills are equally important for the role.

### Weighted Skill Matching

**Formula:**
```
Match % = (Sum of Matched Skill Weights ÷ Total Weight) × 100
```

**Example:**
```
Skill Weights: python:3, sql:2, docker:1 (total weight = 6)
Candidate has: python, sql
Matched Weight = 3 + 2 = 5
Match % = (5 ÷ 6) × 100 = 83.33%
```

**Use Case:** Some skills are more critical than others.

**Weight Assignment Tips:**
- **Critical skills:** Weight 3–4 (must-have)
- **Important skills:** Weight 2 (highly preferred)
- **Nice-to-have skills:** Weight 1 (preferred)

---

## 📥 Input & Output Formats

### CSV Input Format

**Required Columns:** `Name`, `Skills`

**Format:**
```csv
Name,Skills
Alice Johnson,"Python, SQL, Flask, Git, Docker"
Bob Smith,"Java, Spring, SQL, React"
Carol Lee,"Python, React, SQL, AWS, Git"
```

**Requirements:**
- First row must contain headers: `Name` and `Skills`
- Skills must be comma-separated
- Each row must have both Name and Skills
- Skills are case-insensitive (normalized internally)

**Valid Example:**
```csv
Name,Skills
John Doe,"Python, JavaScript, React"
Jane Smith,"Java, Spring Boot, SQL"
```

**Invalid Example:**
```csv
Name,Skills
John Doe,  # Missing skills
Jane Smith,"Java, Spring Boot"  # Missing "Name" column header
```

### CSV Output Format

**Columns:** `Rank`, `Name`, `MatchPercentage`, `MatchedSkills`

**Format:**
```csv
Rank,Name,MatchPercentage,MatchedSkills
1,Alice Johnson,75.00,"Docker, Python, Sql"
2,Carol Lee,75.00,"Python, React, Sql"
3,Farhan Ali,75.00,"Python, React, Sql"
```

**Features:**
- Candidates ranked from highest to lowest match percentage
- Match percentage formatted to 2 decimal places
- Matched skills shown in title case, alphabetically sorted

---

## ⚙️ Configuration

### Selection Threshold

The **selection threshold** determines the minimum match percentage required to mark a candidate as "Selected".

**Default:** 60%

**Example:**
```
Threshold: 75%
Match %: 75.00% → Selected ✓
Match %: 74.99% → Not Selected ✗
```

**When to Adjust:**
- **High threshold (80–100%):** Strict filtering, only top candidates
- **Default threshold (60%):** Balanced approach
- **Low threshold (40–50%):** Inclusive, more candidates advance

### Skill Normalization

All skills are automatically normalized:
- **Whitespace:** Leading/trailing spaces removed
- **Case:** Converted to lowercase for matching
- **Uniqueness:** Duplicate skills removed

**Examples:**
- `" Python "` → `python`
- `"REACT"` → `react`
- `"Docker, docker, DOCKER"` → Treated as one unique skill

---

## 💡 Examples

### Example 1: Basic Job Screening

**Scenario:** You need to shortlist Python developers with SQL experience.

```
Input CSV:
Name,Skills
Alice,"Python, SQL, Flask"
Bob,"Python, JavaScript"
Carol,"SQL, C++"

Required Skills: Python, SQL
Threshold: 60%

Results:
Alice: 100% ✓ (Selected)
Bob: 50% ✗ (Not Selected)
Carol: 50% ✗ (Not Selected)
```

### Example 2: Weighted Skill Filtering

**Scenario:** You're hiring a Full-Stack Developer where skills have different importance.

```
Weighted Skills: react:3, node:3, sql:2, git:1
Total Weight: 9

Candidate A has: React, Node, SQL
Matched Weight: 3 + 3 + 2 = 8
Match %: (8 ÷ 9) × 100 = 88.89%

Candidate B has: Git, SQL
Matched Weight: 1 + 2 = 3
Match %: (3 ÷ 9) × 100 = 33.33%
```

### Example 3: Custom Threshold

```
Default Threshold: 60%
Custom Threshold: 70%

Alice: 75% → Selected (above 70%)
Bob: 66% → Not Selected (below 70%)
Carol: 70% → Selected (meets 70%)
```

---

## 📚 Documentation

### Additional Resources

- **Project Report:** See `docs/LinkedIn_Resume_Shortlisting_Project_Report.pdf` for a detailed professional summary with screenshots
- **Live Demo:** Visit the [interactive web demo](https://raw.githack.com/Creator-Naren/Resume-Short-lister/main/docs/index.html)
- **Sample Data:** View `sample_resumes.csv` for example input format

### Code Documentation

The main module `resume_shortlisting_system.py` is fully documented with docstrings:

```python
def basic_match(
    resumes: Sequence[Dict[str, str]],
    required_skills: Set[str],
    threshold: float = 60.0,
) -> List[CandidateResult]:
    """
    Match candidates using basic skill matching.
    
    Args:
        resumes: List of resume dictionaries with 'Name' and 'Skills'
        required_skills: Set of normalized required skills
        threshold: Minimum match percentage to select (default 60.0)
        
    Returns:
        List of CandidateResult objects sorted by match percentage
    """
```

---

## 🔮 Future Improvements

The following enhancements are planned:

- **📄 PDF/DOCX Parsing** - Parse resume files directly instead of CSV-only
- **🌐 Web Interface** - Full Flask/Django web application with database
- **🗄️ Database Support** - Store candidates and job requirements in PostgreSQL/MySQL
- **🤖 NLP Enhancement** - Smart skill extraction using natural language processing
- **📋 Job Description Input** - Accept job descriptions directly and extract skills
- **📊 Interactive Dashboards** - Real-time analytics and visualization
- **🔐 Role-based Access** - Multi-user support with permissions
- **📧 Email Notifications** - Notify candidates of application status
- **🏷️ Skill Categorization** - Group skills by category (languages, frameworks, tools)

---

## 🆘 Troubleshooting

### Issue: "FileNotFoundError: Input file not found"

**Cause:** The CSV file path is incorrect or doesn't exist.

**Solution:**
```bash
# Verify the file exists
ls sample_resumes.csv

# Use correct path
python resume_shortlisting_system.py --input /path/to/your/resumes.csv
```

### Issue: "CSV must contain columns: Name, Skills"

**Cause:** Your CSV doesn't have the required header columns.

**Solution:**
Ensure your CSV has exactly these columns:
```csv
Name,Skills
John Doe,"Python, SQL"
```

### Issue: "Please enter at least one required skill"

**Cause:** You didn't enter any skills when prompted.

**Solution:**
Enter at least one skill separated by commas:
```
Enter required skills (comma-separated): Python, SQL, Docker
```

### Issue: "No valid resumes found in input file"

**Cause:** The CSV has no valid rows (missing Name or Skills).

**Solution:**
Check that each row has:
- Non-empty Name value
- Non-empty Skills value

### Issue: "ModuleNotFoundError: No module named 'reportlab'"

**Cause:** Dependencies not installed.

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Invalid choice. Please select 1, 2, or 3"

**Cause:** You entered an invalid menu option.

**Solution:**
Enter only `1`, `2`, or `3` at the menu prompt.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

### MIT License Summary
- ✓ Free to use, modify, and distribute
- ✓ Commercial use permitted
- ✓ Must include license notice
- ✗ No liability or warranty

---

## 👤 Author

**Narendra Borhade**

- GitHub: [@Creator-Naren](https://github.com/Creator-Naren)
- Repository: [Resume-Short-lister](https://github.com/Creator-Naren/Resume-Short-lister)

---

## 🤝 Contributing

While this is a portfolio project, suggestions and feedback are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest improvements in Discussions
- Fork and create Pull Requests

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| Language | Python 3.10+ |
| License | MIT |
| Sample Candidates | 8 |
| Matching Algorithms | 2 (Basic + Weighted) |
| Export Formats | CSV |
| Browser Demo | Yes (GitHub Pages) |

---

## 🎯 Use Cases

This tool is perfect for:

- **HR Teams:** Quick resume screening for large candidate pools
- **Hiring Managers:** Objective skill-based candidate evaluation
- **Recruitment Agencies:** Batch processing multiple job requirements
- **Students:** Portfolio project showcasing Python skills
- **Learning:** Understanding CSV processing, algorithms, and CLI tools

---

## 📞 Support

For questions or issues:
1. Check the **Troubleshooting** section above
2. Review the **Examples** section
3. Examine the `resume_shortlisting_system.py` source code
4. Consult the project report in `docs/`

---

**Last Updated:** July 3, 2026  
**Status:** Active & Maintained
