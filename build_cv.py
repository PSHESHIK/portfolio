# -*- coding: utf-8 -*-
"""Build a premium black & white one/two-page PDF CV for Kristofers Avotins.
Content sourced from the portfolio website (index.html). ATS-friendly: real
selectable text, simple structure, Latvian-capable embedded Arial font."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
)

# ---------- Fonts (Latvian diacritics need an embedded TrueType font) ----------
FONTS = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Body", FONTS + r"\arial.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", FONTS + r"\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", FONTS + r"\ariali.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic")

INK   = colors.HexColor("#000000")
GRAY  = colors.HexColor("#4a4a4a")
FAINT = colors.HexColor("#7a7a7a")
RULE  = colors.HexColor("#111111")

OUT = r"C:\Users\jiyot\KristofersPortfolio\Kristofers_Avotins_CV.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=1.5 * cm, rightMargin=1.5 * cm,
    topMargin=1.25 * cm, bottomMargin=1.1 * cm,
    title="Kristofers Avotins - CV", author="Kristofers Avotins",
    subject="Curriculum Vitae", creator="reportlab",
)

# ---------- Styles ----------
name_st = ParagraphStyle("name", fontName="Body-Bold", fontSize=23, leading=25,
                         textColor=INK, spaceAfter=2, tracking=0)
title_st = ParagraphStyle("title", fontName="Body", fontSize=10.5, leading=14,
                          textColor=GRAY, spaceAfter=4)
contact_st = ParagraphStyle("contact", fontName="Body", fontSize=8.8, leading=12,
                            textColor=FAINT)
sec_st = ParagraphStyle("sec", fontName="Body-Bold", fontSize=10, leading=12,
                        textColor=INK, spaceBefore=11, spaceAfter=3,
                        tracking=1.2)
body_st = ParagraphStyle("body", fontName="Body", fontSize=9.3, leading=13,
                         textColor=colors.HexColor("#1c1c1c"), alignment=TA_LEFT)
bullet_st = ParagraphStyle("bullet", parent=body_st, leftIndent=13,
                           firstLineIndent=-13, spaceAfter=3)
skill_st = ParagraphStyle("skill", parent=body_st, leftIndent=0, spaceAfter=4)
role_st = ParagraphStyle("role", fontName="Body-Bold", fontSize=10, leading=13,
                         textColor=INK)
meta_st = ParagraphStyle("meta", fontName="Body-Italic", fontSize=8.8, leading=12,
                         textColor=FAINT, spaceAfter=3)
proj_st = ParagraphStyle("proj", parent=body_st, leftIndent=13, firstLineIndent=-13,
                         spaceAfter=4)


def rule(weight=0.8, color=RULE, space_after=2):
    return HRFlowable(width="100%", thickness=weight, color=color,
                      spaceBefore=2, spaceAfter=space_after, lineCap="round")


def section(title):
    return [Paragraph(title.upper(), sec_st), rule(0.8, RULE, 4)]


def bullet(text):
    return Paragraph("&ndash;&nbsp;&nbsp;" + text, bullet_st)


story = []

# ---------- Header ----------
story.append(Paragraph("KRISTOFERS AVOTI&#326;&#352;", name_st))
story.append(Paragraph("IT Specialist&nbsp;&nbsp;&middot;&nbsp;&nbsp;Full-Stack Developer&nbsp;&nbsp;&middot;&nbsp;&nbsp;Vibe Coder", title_st))
story.append(Paragraph(
    "Ogre, Latvia &middot; LV-5001&nbsp;&nbsp;|&nbsp;&nbsp;"
    "jiyotaka352199@gmail.com&nbsp;&nbsp;|&nbsp;&nbsp;+371 29165331", contact_st))
story.append(Spacer(1, 5))
story.append(rule(1.3, INK, 1))

# ---------- Professional Summary ----------
story += section("Professional Summary")
story.append(Paragraph(
    "Results-driven IT Specialist and passionate vibe coder combining international "
    "training with deep technical analysis to engineer high-efficiency digital "
    "infrastructure. Expert in data management, backend logic, and clean web "
    "engineering. Proven track record of boosting enterprise productivity by 20% "
    "through creative problem-solving and an AI-augmented workflow that compresses "
    "weeks of manual development into focused hours of high-leverage engineering.",
    body_st))

# ---------- Technical Skills ----------
story += section("Technical Skills")
skills = [
    ("Languages &amp; Frameworks", "Python, PHP, SQL, HTML5, CSS3, JavaScript (ES6)"),
    ("Databases &amp; Architecture", "MS SQL Server, SQLite, MS Access, MS Excel (Advanced Analytics), VS Code"),
    ("AI Orchestration &amp; Prompting", "Claude 3.5 Sonnet, OpenAI GPT-4o, Cursor OS, GitHub Copilot, Advanced Prompt Engineering (Chain-of-Thought, Context Management)"),
    ("Design &amp; Multimedia", "Adobe Photoshop, Video Montage / Editing, UI/UX Prototyping, Canva Pro"),
]
for label, items in skills:
    story.append(Paragraph("<b>%s:</b>&nbsp;&nbsp;%s" % (label, items), skill_st))

# ---------- Professional Experience ----------
story += section("Professional Experience")
story.append(Paragraph("IT Atbalsta Speci&#257;lists (IT Support Specialist)", role_st))
story.append(Paragraph("Technology Company, Latvia&nbsp;&nbsp;&middot;&nbsp;&nbsp;Jan 2023 &ndash; Apr 2026", meta_st))
for b in [
    "Developed and deployed custom data scripts, boosting system infrastructure "
    "productivity by <b>20%</b> and streamlining optimization workflows.",
    "Maintained, audited, and optimized enterprise database systems using MS Access, "
    "MS Excel (Advanced Analytics), and custom SQL query optimization.",
    "Authored clean technical documentation, user instruction manuals, and system "
    "reports in MS Word; created digital assets and visuals in Canva and Adobe Photoshop.",
    "Developed crisp frontend user interfaces (HTML, CSS, JavaScript) to modern "
    "JavaScript benchmarks in VS Code, with backend logic in Python and foundational PHP.",
]:
    story.append(bullet(b))

# ---------- Projects ----------
story += section("Selected Projects")
projects = [
    ("AuraDB", "Python, SQL, SQLite",
     "Enterprise data pipeline mapping and normalizing raw logistics CSVs into relational "
     "schemas; custom SQL indexing optimized data-retrieval times across large tables by <b>3.4x</b>."),
    ("CorePulse", "PHP, Frontend/Backend",
     "Secure web ERP monitoring processing loads and auto-generating PDF reports; PHP REST "
     "API with PDO over MS SQL, driving a responsive modular JavaScript front-end."),
    ("OmniForm", "JavaScript, Regex, SQL",
     "Dynamic client-onboarding engine with real-time Regex validation and fluid DOM "
     "mutations, interfacing safely with an SQL backend database."),
    ("InSight", "Data Analytics",
     "Advanced Excel analytics model using Pivot tracking and multi-conditional lookups, "
     "cross-referencing <b>50,000+</b> rows with SQL Server to auto-generate dashboards with zero latency."),
    ("QuantBot", "Python",
     "Automated Python web scraper and task scheduler parsing JSON feeds into clean weekly "
     "data files &mdash; cutting data-compilation time from weeks to focused hours."),
    ("VividMedia", "Design &amp; Montage",
     "Brand-identity and promotional video suite: high-fidelity prototypes in Canva, visual "
     "compositing in Adobe Photoshop, and cinematic short-form montage edited to precise audio cues."),
]
for name, tags, desc in projects:
    story.append(Paragraph(
        "<b>%s</b>&nbsp;&nbsp;<font color='#7a7a7a'>&middot; %s</font><br/>%s"
        % (name, tags, desc), proj_st))

# ---------- Education ----------
story += section("Education")
edu = [
    ("ATHE Level 3 Diploma in Information and Digital Technologies",
     "UKversity, London, UK", "2025 &ndash; 2026", "Merit / Ar atzin&#299;bu"),
    ("BTEC Level 2 Information and Technology",
     "South Bank Colleges, London, UK", "2023 &ndash; 2025", "Pass / Sekm&#299;gi absolv&#275;ts"),
    ("General Secondary Education",
     "R&#299;gas Strazdumui&#382;as vidusskola &ndash; att&#299;st&#299;bas centrs", "2011 &ndash; 2022",
     "Math 5 &middot; English 6 &middot; Latvian 4"),
]
edu_rows = []
for prog, school, years, grade in edu:
    left = Paragraph(
        "<b>%s</b><br/><font color='#4a4a4a'>%s</font> &nbsp;<font color='#7a7a7a'>&middot; %s</font>"
        % (prog, school, grade), body_st)
    right = Paragraph("<font color='#7a7a7a'>%s</font>" % years,
                      ParagraphStyle("yr", parent=body_st, alignment=2))
    edu_rows.append([left, right])
edu_tbl = Table(edu_rows, colWidths=[14.0 * cm, 3.9 * cm])
edu_tbl.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
]))
story.append(edu_tbl)

# ---------- Key Strengths ----------
story += section("Key Strengths")
story.append(Paragraph(
    "Analytical thinking (multi-layered data &amp; automation) &nbsp;&middot;&nbsp; "
    "International communication (London-educated, fluent professional English) &nbsp;&middot;&nbsp; "
    "Rapid technical adaptation &amp; prototyping &nbsp;&middot;&nbsp; "
    "Precision in both code and technical documentation.", body_st))

doc.build(story)
print("OK ->", OUT)
