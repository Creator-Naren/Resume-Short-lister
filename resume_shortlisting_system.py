"""
Resume Shortlisting System (Week 3 Python Task)

Features:
- Reads multiple resumes from CSV
- Accepts required skills from user
- Calculates skill match percentage
- Classifies candidates (Selected / Not Selected)
- Ranks candidates by match score
- Exports selected candidates to CSV
- Optional weighted skill matching
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set


@dataclass
class CandidateResult:
    name: str
    candidate_skills: Set[str]
    matched_skills: Set[str]
    match_percentage: float
    status: str


def normalize_skill(skill: str) -> str:
    return skill.strip().lower()


def parse_skills(skill_text: str) -> Set[str]:
    return {normalize_skill(s) for s in skill_text.split(",") if s.strip()}


def title_case_skills(skills: Iterable[str]) -> str:
    return ", ".join(sorted(s.title() for s in skills))


def load_resumes(csv_path: Path) -> List[Dict[str, str]]:
    if not csv_path.exists():
        raise FileNotFoundError(f"Input file not found: {csv_path}")

    resumes: List[Dict[str, str]] = []
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required_columns = {"Name", "Skills"}
        if not required_columns.issubset(set(reader.fieldnames or [])):
            raise ValueError("CSV must contain columns: Name, Skills")

        for row in reader:
            name = (row.get("Name") or "").strip()
            skills = (row.get("Skills") or "").strip()
            if name and skills:
                resumes.append({"Name": name, "Skills": skills})
    return resumes


def basic_match(
    resumes: Sequence[Dict[str, str]],
    required_skills: Set[str],
    threshold: float = 60.0,
) -> List[CandidateResult]:
    if not required_skills:
        raise ValueError("Required skills list cannot be empty.")

    results: List[CandidateResult] = []
    total_required = len(required_skills)

    for resume in resumes:
        name = resume["Name"]
        skills = parse_skills(resume["Skills"])
        matched = required_skills.intersection(skills)
        percentage = (len(matched) / total_required) * 100
        status = "Selected" if percentage >= threshold else "Not Selected"
        results.append(
            CandidateResult(
                name=name,
                candidate_skills=skills,
                matched_skills=matched,
                match_percentage=round(percentage, 2),
                status=status,
            )
        )

    results.sort(key=lambda item: item.match_percentage, reverse=True)
    return results


def weighted_match(
    resumes: Sequence[Dict[str, str]],
    skill_weights: Dict[str, float],
    threshold: float = 60.0,
) -> List[CandidateResult]:
    if not skill_weights:
        raise ValueError("Skill weights cannot be empty.")

    total_weight = sum(skill_weights.values())
    if total_weight <= 0:
        raise ValueError("Total skill weight must be greater than zero.")

    required_skills = set(skill_weights.keys())
    results: List[CandidateResult] = []

    for resume in resumes:
        name = resume["Name"]
        skills = parse_skills(resume["Skills"])
        matched = required_skills.intersection(skills)
        matched_weight = sum(skill_weights[skill] for skill in matched)
        percentage = (matched_weight / total_weight) * 100
        status = "Selected" if percentage >= threshold else "Not Selected"
        results.append(
            CandidateResult(
                name=name,
                candidate_skills=skills,
                matched_skills=matched,
                match_percentage=round(percentage, 2),
                status=status,
            )
        )

    results.sort(key=lambda item: item.match_percentage, reverse=True)
    return results


def export_selected(results: Sequence[CandidateResult], output_path: Path) -> int:
    selected = [r for r in results if r.status == "Selected"]
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Rank", "Name", "MatchPercentage", "MatchedSkills"])
        for rank, row in enumerate(selected, start=1):
            writer.writerow(
                [
                    rank,
                    row.name,
                    f"{row.match_percentage:.2f}",
                    title_case_skills(row.matched_skills),
                ]
            )
    return len(selected)


def print_results(results: Sequence[CandidateResult]) -> None:
    print("\n=== Candidate Ranking ===")
    print(
        f"{'Rank':<5} {'Name':<20} {'Match %':<10} {'Status':<13} Matched Skills"
    )
    print("-" * 80)
    for rank, row in enumerate(results, start=1):
        matched = title_case_skills(row.matched_skills) or "-"
        print(
            f"{rank:<5} {row.name:<20} {row.match_percentage:<10.2f} "
            f"{row.status:<13} {matched}"
        )


def parse_required_skills_input(raw_input: str) -> Set[str]:
    skills = {normalize_skill(s) for s in raw_input.split(",") if s.strip()}
    if not skills:
        raise ValueError("Please enter at least one required skill.")
    return skills


def parse_weighted_skills_input(raw_input: str) -> Dict[str, float]:
    """
    Expected format:
    python:3, sql:2, react:2, docker:1
    """
    skill_weights: Dict[str, float] = {}
    for token in raw_input.split(","):
        if ":" not in token:
            continue
        skill, weight = token.split(":", maxsplit=1)
        skill = normalize_skill(skill)
        weight = weight.strip()
        if not skill or not weight:
            continue
        try:
            skill_weights[skill] = float(weight)
        except ValueError:
            continue

    if not skill_weights:
        raise ValueError(
            "Invalid weighted input. Example: python:3, sql:2, react:1"
        )
    return skill_weights


def run_cli(csv_path: Path) -> None:
    resumes = load_resumes(csv_path)
    if not resumes:
        print("No valid resumes found in input file.")
        return

    while True:
        print("\n=== Resume Shortlisting System ===")
        print("1. Basic Skill Matching")
        print("2. Weighted Skill Matching (Bonus)")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            raw_skills = input(
                "Enter required skills (comma-separated): "
            ).strip()
            threshold_raw = input(
                "Enter selection threshold percentage (default 60): "
            ).strip()
            threshold = float(threshold_raw) if threshold_raw else 60.0

            required = parse_required_skills_input(raw_skills)
            results = basic_match(resumes, required, threshold=threshold)
            print_results(results)

            export_choice = input(
                "\nExport selected candidates to CSV? (y/n): "
            ).strip().lower()
            if export_choice == "y":
                count = export_selected(results, Path("shortlisted_candidates.csv"))
                print(
                    f"Exported {count} selected candidates to "
                    "shortlisted_candidates.csv"
                )

        elif choice == "2":
            raw_weighted = input(
                "Enter weighted skills (skill:weight comma-separated): "
            ).strip()
            threshold_raw = input(
                "Enter selection threshold percentage (default 60): "
            ).strip()
            threshold = float(threshold_raw) if threshold_raw else 60.0

            skill_weights = parse_weighted_skills_input(raw_weighted)
            results = weighted_match(resumes, skill_weights, threshold=threshold)
            print_results(results)

            export_choice = input(
                "\nExport selected candidates to CSV? (y/n): "
            ).strip().lower()
            if export_choice == "y":
                count = export_selected(
                    results, Path("shortlisted_candidates_weighted.csv")
                )
                print(
                    f"Exported {count} selected candidates to "
                    "shortlisted_candidates_weighted.csv"
                )

        elif choice == "3":
            print("Good luck with your project.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def run_demo(csv_path: Path) -> List[CandidateResult]:
    resumes = load_resumes(csv_path)
    required = {"python", "react", "sql", "docker"}
    threshold = 60.0
    print("Running demo with required skills: Python, React, SQL, Docker")
    results = basic_match(resumes, required, threshold=threshold)
    print_results(results)
    count = export_selected(results, Path("shortlisted_candidates.csv"))
    print(f"\nSelected candidates exported: {count}")
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resume Shortlisting System")
    parser.add_argument(
        "--input",
        default="sample_resumes.csv",
        help="Path to input CSV (default: sample_resumes.csv)",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run predefined demo and export shortlisted candidates.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    csv_path = Path(args.input)
    if args.demo:
        run_demo(csv_path)
    else:
        run_cli(csv_path)


if __name__ == "__main__":
    main()
