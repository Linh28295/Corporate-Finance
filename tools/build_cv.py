#!/usr/bin/env python3
"""Build the CV PDF from structured content.

Usage:
    python3 tools/build_cv.py

Writes deliverables/Nguyen-Bui-Ngoc-Linh-CV.pdf.

Style: A4, ATS-friendly Liberation Sans, navy-and-white, left-aligned bullets,
two-page layout. Mirrors the prior ReportLab build (commits 2ad7a70 ..  890f93a).
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether,
)


# ── Fonts ─────────────────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/liberation"
pdfmetrics.registerFont(TTFont("LibSans",        f"{FONT_DIR}/LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("LibSans-Bold",   f"{FONT_DIR}/LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("LibSans-Italic", f"{FONT_DIR}/LiberationSans-Italic.ttf"))

NAVY = HexColor("#0B2545")
GREY = HexColor("#54606C")


# ── Paragraph styles ──────────────────────────────────────────────────────────
def _style(name, **kw):
    base = dict(fontName="LibSans", fontSize=10, leading=13, textColor=black, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name=name, **base)


S_NAME       = _style("Name",       fontName="LibSans-Bold",   fontSize=22, leading=26, textColor=NAVY, spaceAfter=2)
S_TITLE      = _style("Title",      fontName="LibSans-Italic", fontSize=11, leading=14, textColor=GREY, spaceAfter=4)
S_CONTACT    = _style("Contact",    fontSize=9,  leading=12, textColor=GREY, spaceAfter=2)
S_SECTION    = _style("Section",    fontName="LibSans-Bold",   fontSize=13, leading=16, textColor=NAVY, spaceBefore=8, spaceAfter=2)
S_ROLE_ORG   = _style("RoleOrg",    fontName="LibSans-Bold",   fontSize=10.5, leading=13, spaceBefore=6, spaceAfter=0)
S_ROLE_TITLE = _style("RoleTitle",  fontName="LibSans-Italic", fontSize=10, leading=12, textColor=GREY, spaceAfter=0)
S_ROLE_DATES = _style("RoleDates",  fontSize=9.5, leading=11.5, textColor=GREY, spaceAfter=3)
S_SUBHEAD    = _style("SubHead",    fontName="LibSans-Bold",   fontSize=10, leading=12, fontStyle="Italic", spaceBefore=4, spaceAfter=1)
S_BULLET     = _style("Bullet",     fontSize=10, leading=13, leftIndent=10, bulletIndent=0, spaceAfter=2)
S_PARA       = _style("Para",       fontSize=10, leading=13, spaceAfter=4)
S_KEY        = _style("KeyVal",     fontName="LibSans-Bold",   fontSize=10, leading=12.5)
S_VAL        = _style("Val",        fontSize=10, leading=12.5)


# ── Helpers ───────────────────────────────────────────────────────────────────
def section(title):
    return [Paragraph(title, S_SECTION),
            HRFlowable(width="100%", thickness=0.6, color=NAVY, spaceBefore=1, spaceAfter=4)]


def bullet(text):
    return Paragraph(f"• {text}", S_BULLET)


def subhead(text):
    # Italic + bold sub-header inside a role
    return Paragraph(f"<i><b>{text}</b></i>", S_SUBHEAD)


def role_block(org, title, dates, subhead_bullets):
    """`subhead_bullets`: list of (subheader_or_None, [bullet_text, ...]) tuples."""
    flowables = [
        Paragraph(f"<b>{org}</b>", S_ROLE_ORG),
        Paragraph(title, S_ROLE_TITLE),
        Paragraph(dates, S_ROLE_DATES),
    ]
    for sub, bullets in subhead_bullets:
        if sub:
            flowables.append(subhead(sub))
        for b in bullets:
            flowables.append(bullet(b))
    return flowables


def award_block(title, line, body):
    return [
        Paragraph(f"<b>{title}</b>", _style("AwardTitle", fontName="LibSans-Bold", fontSize=10.5, leading=13, spaceBefore=4)),
        Paragraph(line, S_ROLE_DATES),
        Paragraph(body, S_PARA),
    ]


# ── Content ───────────────────────────────────────────────────────────────────
def build_story():
    s = []

    # Header
    s.append(Paragraph("Nguyen Bui Ngoc Linh", S_NAME))
    s.append(Paragraph("Senior Manager, Operations &amp; Technology Strategy &amp; Transformation — Prudential Vietnam", S_TITLE))
    s.append(Paragraph(
        "nguyenbuingoclinh546@gmail.com · +84 9677 99 546 · Ho Chi Minh City, Vietnam · "
        "<link href='https://linkedin.com/in/linh-nguyen-b89436143'>linkedin.com/in/linh-nguyen-b89436143</link>",
        S_CONTACT,
    ))
    s.append(HRFlowable(width="100%", thickness=1.0, color=NAVY, spaceBefore=4, spaceAfter=2))

    # Professional Summary
    s += section("Professional Summary")
    s.append(Paragraph(
        "Strategy and transformation leader with 8 years across life insurance, retail, and financial "
        "services in Vietnam. Specialist in enterprise transformation, Target Operating Model design, and "
        "portfolio governance — leading multi-disciplinary teams and converting executive ambition into "
        "measurable business outcomes. PROSCI-certified change practitioner; Executive MBA candidate at "
        "the University of Hawaiʻi at Mānoa (AACSB-accredited).",
        S_PARA,
    ))

    # Professional Experience
    s += section("Professional Experience")

    s += role_block(
        "Prudential Vietnam — Ho Chi Minh City, Vietnam",
        "Senior Manager, Operations &amp; Technology Strategy &amp; Transformation",
        "March 2024 – Present",
        [
            ("Strategic Planning &amp; Portfolio Oversight", [
                "Lead a multi-disciplinary team of 9 driving a USD 10M annual transformation roadmap "
                "aligned with Executive Committee (ExCo) priorities and enterprise-wide strategic objectives.",
                "Govern a comprehensive transformation portfolio across business units, ensuring rigorous delivery "
                "against milestones and sustaining execution accountability through structured governance rhythms.",
                "Orchestrate end-to-end change management and communication strategies, ensuring organisational "
                "buy-in for large-scale transformation efforts.",
                "Architect Target Operating Model (TOM) design and roadmap structuring for major strategic shifts, "
                "converting abstract goals into measurable, executable action plans.",
            ]),
            ("Financial Stewardship &amp; Operational Excellence", [
                "Oversee USD 50M BAU and investment budget governance, realising USD 10M+ in cost savings "
                "through a structured optimisation programme — eliminating non-value-adding activities, "
                "renegotiating vendor contracts, and redesigning operating models.",
                "Deploy Celonis process mining to map end-to-end processes, surface inefficiencies, and "
                "generate data-driven insights that underpin operational improvement and strategic decisions.",
                "Synthesise cross-functional performance data into executive-ready insights, directly informing "
                "C-suite decisions on resource allocation and strategic priorities.",
            ]),
        ],
    )

    s += role_block(
        "Prudential Vietnam — Ho Chi Minh City, Vietnam",
        "Manager, Corporate Strategy",
        "October 2021 – March 2024",
        [(None, [
            "Owned the enterprise strategic planning cycle — translated company ambition into annual plans, "
            "functional priorities, and KPIs aligned with ExCo direction.",
            "Conducted competitive analysis and market intelligence to drive strategic positioning, "
            "opportunity sizing, and investment prioritisation across business units.",
            "Built board-level strategy presentations and reporting, synthesising cross-functional data into "
            "clear narratives for senior leadership decision-making.",
            "Established governance rhythms — strategy reviews, performance tracking, risk and dependency "
            "reporting — to sustain accountability from planning through execution.",
        ])],
    )

    s += role_block(
        "AIA Vietnam — Ho Chi Minh City, Vietnam",
        "Supervisor, Business Strategy",
        "September 2020 – September 2021",
        [(None, [
            "Consolidated strategic inputs across all business units into a unified company performance plan "
            "and KPI framework adopted for senior leadership review.",
            "Delivered monthly strategy and performance reporting to C-suite, directly informing resource "
            "allocation and initiative prioritisation decisions.",
            "Identified performance gaps through business metrics analysis and surfaced corrective "
            "recommendations adopted by leadership.",
        ])],
    )

    s += role_block(
        "PNJ Group — Ho Chi Minh City, Vietnam",
        "Management Trainee &amp; Assistant to Chief Strategy Officer",
        "July 2018 – September 2020",
        [(None, [
            "Worked directly with the Chief Strategy Officer on business planning, competitive analysis, and "
            "strategic initiative tracking at one of Vietnam's leading retail groups.",
            "Supported preparation of strategy documents, executive presentations, and market research for "
            "senior leadership and board-level discussions.",
            "Rotated across Strategy, Sales, and Marketing — building cross-functional business acumen and "
            "stakeholder management skills.",
        ])],
    )

    # Education
    s += section("Education")
    s.append(Paragraph("<b>University of Hawaiʻi at Mānoa — Shidler College of Business</b>", S_ROLE_ORG))
    s.append(Paragraph("Executive MBA (EMBA) · Expected July 2027 · Focus: Corporate finance, enterprise leadership, organisational transformation", S_ROLE_TITLE))
    s.append(Spacer(1, 4))
    s.append(Paragraph("<b>Curtin Singapore</b>", S_ROLE_ORG))
    s.append(Paragraph("Bachelor of Commerce, Marketing and Management · September 2017", S_ROLE_TITLE))

    # Awards
    s += section("Honours &amp; Awards")
    s += award_block(
        "Talent Group · Prudential Vietnam Assurance · 2025 &amp; 2026",
        "",
        "Identified as a high-potential leader and selected for PVA's Talent Group for two consecutive years.",
    )
    s += award_block(
        "Alexandrite Award — BPR for Claims · Prudential Vietnam · January 2026",
        "",
        "Awarded for leading Claims BPR using Celonis process mining, significantly enhancing delivery speed and accuracy.",
    )
    s += award_block(
        "Alexandrite Award — Health Strategy · Prudential Vietnam · December 2024",
        "",
        "Recognised by Group and Executive Committee for architecting Prudential Vietnam's Health business strategy "
        "from the ground up — encompassing the 2024–2030 strategic vision, Target Operating Model, technology "
        "roadmap, and product portfolio — establishing the full foundation for a new line of business.",
    )

    # Skills & Certifications (two-column table)
    s += section("Skills &amp; Certifications")
    rows = [
        ("Languages",      "Vietnamese (Native) · English (Professional Working Proficiency)"),
        ("Technical",      "Celonis Process Mining · Process Mapping (BPR) · Data Analysis · PMO Tracking Tools · Advanced Excel · PowerPoint"),
        ("Certifications", "PROSCI Taking Charge of Change (May 2025)"),
        ("Competencies",   "Corporate Strategy · Business Transformation · Portfolio Governance · Change Management · TOM Design · "
                           "Financial Governance · People Leadership · Cross-functional Leadership · Stakeholder Management · "
                           "Executive Communication · Strategic Storytelling"),
    ]
    table_data = [[Paragraph(k, S_KEY), Paragraph(v, S_VAL)] for k, v in rows]
    t = Table(table_data, colWidths=[34*mm, 138*mm], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
    ]))
    s.append(t)

    return s


def main():
    doc = SimpleDocTemplate(
        "deliverables/Nguyen-Bui-Ngoc-Linh-CV.pdf",
        pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=14*mm, bottomMargin=14*mm,
        title="Nguyen Bui Ngoc Linh — CV",
        author="Nguyen Bui Ngoc Linh",
    )
    doc.build(build_story())
    print("Wrote deliverables/Nguyen-Bui-Ngoc-Linh-CV.pdf")


if __name__ == "__main__":
    main()
