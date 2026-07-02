from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    Image as RLImage,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
ASSETS_DIR = ROOT / "artifacts"
REPORT_PATH = ROOT / "LinkedIn_Resume_Shortlisting_Project_Report.pdf"


def run_demo_and_capture_output() -> str:
    command = [sys.executable, "resume_shortlisting_system.py", "--demo"]
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def read_shortlisted_csv(csv_path: Path) -> List[Tuple[str, float]]:
    if not csv_path.exists():
        return []
    rows: List[Tuple[str, float]] = []
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = (row.get("Name") or "").strip()
            score_raw = (row.get("MatchPercentage") or "0").strip()
            try:
                score = float(score_raw)
            except ValueError:
                score = 0.0
            if name:
                rows.append((name, score))
    return rows


def get_mono_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
    ]
    for font_path in candidates:
        path = Path(font_path)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def get_ui_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for font_path in candidates:
        path = Path(font_path)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def save_terminal_output_image(text: str, output_path: Path) -> None:
    font = get_mono_font(20)
    lines = text.splitlines() or ["(no output)"]
    padding = 30
    line_height = 28
    width = 1600
    height = padding * 2 + max(1, len(lines)) * line_height

    image = Image.new("RGB", (width, height), color=(18, 20, 28))
    draw = ImageDraw.Draw(image)
    y = padding
    for line in lines:
        draw.text((padding, y), line, fill=(230, 235, 245), font=font)
        y += line_height
    image.save(output_path)


def save_scores_chart(data: List[Tuple[str, float]], output_path: Path) -> None:
    width, height = 1600, 900
    image = Image.new("RGB", (width, height), color=(248, 250, 252))
    draw = ImageDraw.Draw(image)
    title_font = get_ui_font(46)
    label_font = get_ui_font(24)

    draw.text((50, 30), "Selected Candidates Match Score (%)", fill=(21, 43, 77), font=title_font)

    if not data:
        draw.text((50, 130), "No selected candidates found.", fill=(180, 40, 40), font=label_font)
        image.save(output_path)
        return

    plot_left = 150
    plot_top = 170
    plot_right = 1500
    plot_bottom = 780

    draw.rectangle([plot_left, plot_top, plot_right, plot_bottom], outline=(180, 190, 205), width=2)
    draw.line([plot_left, plot_bottom, plot_right, plot_bottom], fill=(70, 85, 110), width=3)
    draw.line([plot_left, plot_top, plot_left, plot_bottom], fill=(70, 85, 110), width=3)

    for tick in range(0, 101, 20):
        y = plot_bottom - int((tick / 100) * (plot_bottom - plot_top))
        draw.line([plot_left - 8, y, plot_left, y], fill=(70, 85, 110), width=2)
        draw.text((85, y - 12), str(tick), fill=(70, 85, 110), font=label_font)
        if tick > 0:
            draw.line([plot_left, y, plot_right, y], fill=(225, 232, 240), width=1)

    count = len(data)
    bar_space = (plot_right - plot_left) // max(1, count)
    bar_width = int(bar_space * 0.6)
    bar_color = (39, 117, 176)

    for idx, (name, score) in enumerate(data):
        x_center = plot_left + int((idx + 0.5) * bar_space)
        x1 = x_center - bar_width // 2
        x2 = x_center + bar_width // 2
        bar_height = int((score / 100) * (plot_bottom - plot_top))
        y1 = plot_bottom - bar_height
        y2 = plot_bottom
        draw.rectangle([x1, y1, x2, y2], fill=bar_color, outline=(20, 80, 130))
        draw.text((x1, y1 - 35), f"{score:.1f}", fill=(21, 43, 77), font=label_font)
        draw.text((x1 - 20, plot_bottom + 12), name.split()[0], fill=(21, 43, 77), font=label_font)

    image.save(output_path)


def save_summary_table_image(data: List[Tuple[str, float]], output_path: Path) -> None:
    width, height = 1300, 600
    image = Image.new("RGB", (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    title_font = get_ui_font(38)
    body_font = get_ui_font(26)

    draw.text((40, 25), "Shortlisted Candidates (Export Preview)", fill=(10, 60, 100), font=title_font)

    header_y = 110
    row_height = 60
    col_x = [40, 140, 800]

    draw.rectangle([40, header_y, 1260, header_y + row_height], fill=(12, 84, 130))
    draw.text((col_x[0], header_y + 15), "Rank", fill=(255, 255, 255), font=body_font)
    draw.text((col_x[1], header_y + 15), "Candidate", fill=(255, 255, 255), font=body_font)
    draw.text((col_x[2], header_y + 15), "Match %", fill=(255, 255, 255), font=body_font)

    for i, (name, score) in enumerate(data[:6], start=1):
        y = header_y + row_height * i
        fill_color = (243, 248, 252) if i % 2 == 1 else (255, 255, 255)
        draw.rectangle([40, y, 1260, y + row_height], fill=fill_color)
        draw.rectangle([40, y, 1260, y + row_height], outline=(220, 230, 238))
        draw.text((col_x[0], y + 15), str(i), fill=(25, 35, 45), font=body_font)
        draw.text((col_x[1], y + 15), name, fill=(25, 35, 45), font=body_font)
        draw.text((col_x[2], y + 15), f"{score:.2f}", fill=(25, 35, 45), font=body_font)

    image.save(output_path)


def build_pdf_report(
    output_text_image: Path, chart_image: Path, table_image: Path, selected: List[Tuple[str, float]]
) -> None:
    doc = SimpleDocTemplate(
        str(REPORT_PATH),
        pagesize=A4,
        leftMargin=1.8 * cm,
        rightMargin=1.8 * cm,
        topMargin=1.6 * cm,
        bottomMargin=1.6 * cm,
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=22,
        textColor=colors.HexColor("#0b4f7a"),
        spaceAfter=10,
    )
    sub_style = ParagraphStyle(
        "SubStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#222222"),
    )
    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.HexColor("#0a4061"),
        spaceBefore=8,
        spaceAfter=4,
    )

    story = []
    story.append(Paragraph("Resume Shortlisting System (Python Project)", title_style))
    story.append(
        Paragraph(
            "A practical HR screening automation project built in Python. "
            "This report summarizes objectives, implementation, outputs, and results for LinkedIn sharing.",
            sub_style,
        )
    )
    story.append(Spacer(1, 10))

    story.append(Paragraph("Project Objective", heading_style))
    story.append(
        Paragraph(
            "Build a system that reads resumes, matches candidate skills against required job skills, "
            "calculates match percentage, ranks applicants, and shortlists top profiles.",
            sub_style,
        )
    )

    story.append(Paragraph("Implemented Features", heading_style))
    features = [
        "Read multiple resumes from CSV format",
        "User-defined required skills input",
        "Match percentage calculation",
        "Selection classification using threshold",
        "Candidate ranking by score",
        "CSV export of selected candidates",
        "Bonus: weighted skill matching support",
        "Bonus: CLI menu interface",
    ]
    feature_data = [[f"- {item}"] for item in features]
    feature_table = Table(feature_data, colWidths=[17 * cm])
    feature_table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("LEADING", (0, 0), (-1, -1), 14),
                ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#1f1f1f")),
            ]
        )
    )
    story.append(feature_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Output Snapshot (Console)", heading_style))
    story.append(RLImage(str(output_text_image), width=17.5 * cm, height=8.4 * cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Shortlisted Candidates Visualization", heading_style))
    story.append(RLImage(str(chart_image), width=17.5 * cm, height=9.6 * cm))
    story.append(Spacer(1, 10))
    story.append(RLImage(str(table_image), width=17.5 * cm, height=6.4 * cm))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Final Results", heading_style))
    if selected:
        summary_rows = [["Rank", "Candidate", "Match %"]]
        for i, (name, score) in enumerate(selected, start=1):
            summary_rows.append([str(i), name, f"{score:.2f}"])
        result_table = Table(summary_rows, colWidths=[2 * cm, 9 * cm, 3 * cm])
        result_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0b4f7a")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("ALIGN", (0, 0), (0, -1), "CENTER"),
                    ("ALIGN", (2, 0), (2, -1), "CENTER"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#bfd2de")),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#eef6fb")]),
                ]
            )
        )
        story.append(result_table)
    else:
        story.append(Paragraph("No candidates were selected for the chosen criteria.", sub_style))

    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Tech Stack: Python, csv, argparse, dataclasses, ReportLab, Pillow.",
            sub_style,
        )
    )

    doc.build(story)


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    output_text = run_demo_and_capture_output()
    shortlisted = read_shortlisted_csv(ROOT / "shortlisted_candidates.csv")

    output_img = ASSETS_DIR / "output_console.png"
    chart_img = ASSETS_DIR / "selected_candidates_chart.png"
    table_img = ASSETS_DIR / "shortlist_table.png"

    save_terminal_output_image(output_text, output_img)
    save_scores_chart(shortlisted, chart_img)
    save_summary_table_image(shortlisted, table_img)
    build_pdf_report(output_img, chart_img, table_img, shortlisted)

    print(f"Report generated: {REPORT_PATH}")
    print(f"Images generated in: {ASSETS_DIR}")


if __name__ == "__main__":
    main()
