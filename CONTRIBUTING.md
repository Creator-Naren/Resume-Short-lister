# Contributing to Resume Shortlister

Thank you for your interest in contributing to the Resume Shortlister project! This document provides guidelines and instructions for contributing.

## 📋 Code of Conduct

Be respectful, inclusive, and professional in all interactions. We're building a welcoming community for developers of all skill levels.

## 🐛 Reporting Bugs

Found a bug? Please follow these steps:

1. **Check existing issues** - Search the [Issues](https://github.com/Creator-Naren/Resume-Short-lister/issues) tab to avoid duplicates
2. **Create a clear report** with:
   - Descriptive title
   - Step-by-step reproduction steps
   - Expected vs. actual behavior
   - Python version and environment details
   - Any error messages or logs

**Example:**
```
Title: FileNotFoundError when using relative paths

Steps:
1. Run: python resume_shortlisting_system.py --input ../resumes.csv
2. Expected: Program loads the file successfully
3. Actual: FileNotFoundError is raised
```

## 💡 Suggesting Enhancements

Have an idea to improve the project?

1. **Check existing discussions** - See [Future Improvements](README.md#-future-improvements) section
2. **Open a Discussion** or Issue with:
   - Clear description of the enhancement
   - Motivation (why is this useful?)
   - Proposed implementation approach (if applicable)
   - Examples showing the benefit

## 🔧 Development Setup

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- Git

### Setup Instructions

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork locally
git clone https://github.com/YOUR-USERNAME/Resume-Short-lister.git
cd Resume-Short-lister

# 3. Create a feature branch
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b bugfix/issue-description

# 4. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Test your changes
python resume_shortlisting_system.py --demo

# 7. Run the program interactively
python resume_shortlisting_system.py --input sample_resumes.csv
```

## 📝 Making Changes

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep lines under 100 characters when possible

### Testing Your Changes

```bash
# Test with the demo
python resume_shortlisting_system.py --demo

# Test with custom CSV
python resume_shortlisting_system.py --input test_data.csv

# Test programmatic usage
python -c "from resume_shortlisting_system import load_resumes; print(load_resumes('sample_resumes.csv'))"
```

### Documentation

- Update **README.md** if your change affects usage
- Add docstrings to new functions following the existing format
- Update the project report if adding significant features

## 🚀 Submitting a Pull Request

### Before You Start
1. **Create an issue first** for major changes (discuss your approach)
2. **Ensure your branch is up-to-date** with main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

### PR Checklist

- [ ] Branch is based on `main`
- [ ] Changes follow PEP 8 style guidelines
- [ ] All functions have docstrings
- [ ] Code tested locally with `--demo` and custom data
- [ ] README.md updated if needed
- [ ] Commit messages are clear and descriptive

### Writing Your PR

**Title:** Use the format `[Feature/Fix/Docs] Brief description`

**Examples:**
- `[Feature] Add PDF resume parsing support`
- `[Fix] Handle edge case in skill normalization`
- `[Docs] Update installation instructions`

**Description:** Include:
- What does this PR do?
- Why is this change needed?
- Related issues (if applicable): Closes #123
- Testing performed

**Example PR Description:**
```
## What
Adds weighted skill matching feature for prioritizing critical skills

## Why
Recruiters need to differentiate between must-have and nice-to-have skills. The basic matching treats all skills equally, which doesn't reflect real hiring needs.

## Testing
- [x] Tested with sample_resumes.csv
- [x] Verified output CSV format
- [x] Tested edge cases (no matches, duplicate skills)

Closes #45
```

## 📖 Documentation Standards

### Function Docstrings
```python
def basic_match(
    resumes: Sequence[Dict[str, str]],
    required_skills: Set[str],
    threshold: float = 60.0,
) -> List[CandidateResult]:
    """
    Match candidates using basic skill matching algorithm.
    
    All required skills have equal importance in this approach.
    Candidates are ranked by match percentage in descending order.
    
    Args:
        resumes: List of resume dictionaries with 'Name' and 'Skills' keys
        required_skills: Set of normalized skill strings to match against
        threshold: Minimum match percentage to select (0-100, default 60.0)
        
    Returns:
        List of CandidateResult objects sorted by match percentage (highest first)
        
    Raises:
        ValueError: If threshold is not between 0 and 100
        
    Example:
        >>> resumes = [{'Name': 'Alice', 'Skills': 'Python, SQL'}]
        >>> results = basic_match(resumes, {'python', 'sql'}, threshold=75)
    """
```

## 🎯 Areas We'd Love Help With

- **Testing** - Add more test coverage
- **Performance** - Optimize for larger datasets
- **Documentation** - Improve clarity or add examples
- **Features** - See [Future Improvements](README.md#-future-improvements)
- **Bug Fixes** - Check [open issues](https://github.com/Creator-Naren/Resume-Short-lister/issues)

## ❓ Questions?

1. Check the [README.md](README.md) and [Troubleshooting](README.md#-troubleshooting) section
2. Review [existing issues](https://github.com/Creator-Naren/Resume-Short-lister/issues) and discussions
3. Open a new discussion if you can't find an answer

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Thank you for helping make Resume Shortlister better!** 🎉

Last updated: July 6, 2026
