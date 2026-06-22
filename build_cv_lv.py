# -*- coding: utf-8 -*-
"""Latviešu PDF CV priekš Kristofera Avotiņa.
Apvieno portfolio vietnes saturu ar detalizēto informāciju no oriģinālā CV
(darba pienākumi, stiprās puses, attīstības virzieni). ATS-draudzīgs: īsts
atlasāms teksts, iegults Arial fonts (pilns latviešu burtu atbalsts)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
)

# ---------- Fonti (latviešu diakritiķi prasa iegultu TrueType fontu) ----------
FONTS = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("Body", FONTS + r"\arial.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", FONTS + r"\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", FONTS + r"\ariali.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic")

INK   = colors.HexColor("#000000")
GRAY  = colors.HexColor("#4a4a4a")
FAINT = colors.HexColor("#7a7a7a")
RULE  = colors.HexColor("#111111")

OUT = r"C:\Users\jiyot\KristofersPortfolio\Kristofers_Avotins_CV_LV.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=A4,
    leftMargin=1.5 * cm, rightMargin=1.5 * cm,
    topMargin=1.2 * cm, bottomMargin=1.0 * cm,
    title="Kristofers Avotins - CV (LV)", author="Kristofers Avotins",
    subject="CV / Dzives apraksts", creator="reportlab",
)

# ---------- Stili ----------
name_st = ParagraphStyle("name", fontName="Body-Bold", fontSize=23, leading=25, textColor=INK, spaceAfter=2)
title_st = ParagraphStyle("title", fontName="Body", fontSize=10.5, leading=14, textColor=GRAY, spaceAfter=4)
contact_st = ParagraphStyle("contact", fontName="Body", fontSize=8.6, leading=12, textColor=FAINT)
sec_st = ParagraphStyle("sec", fontName="Body-Bold", fontSize=10, leading=12, textColor=INK,
                        spaceBefore=10, spaceAfter=3, tracking=1.0)
body_st = ParagraphStyle("body", fontName="Body", fontSize=9.2, leading=12.6,
                         textColor=colors.HexColor("#1c1c1c"), alignment=TA_LEFT)
bullet_st = ParagraphStyle("bullet", parent=body_st, leftIndent=13, firstLineIndent=-13, spaceAfter=3)
skill_st = ParagraphStyle("skill", parent=body_st, spaceAfter=4)
role_st = ParagraphStyle("role", fontName="Body-Bold", fontSize=10, leading=13, textColor=INK)
meta_st = ParagraphStyle("meta", fontName="Body-Italic", fontSize=8.8, leading=12, textColor=FAINT, spaceAfter=3)
proj_st = ParagraphStyle("proj", parent=body_st, leftIndent=13, firstLineIndent=-13, spaceAfter=4)


def rule(weight=0.8, color=RULE, space_after=2):
    return HRFlowable(width="100%", thickness=weight, color=color, spaceBefore=2, spaceAfter=space_after, lineCap="round")


def section(title):
    return [Paragraph(title.upper(), sec_st), rule(0.8, RULE, 4)]


def bullet(text):
    return Paragraph("–  " + text, bullet_st)


story = []

# ---------- Galvene ----------
story.append(Paragraph("KRISTOFERS AVOTIŅŠ", name_st))
story.append(Paragraph("IT Speciālists&nbsp;&nbsp;&middot;&nbsp;&nbsp;Full-Stack izstrādātājs&nbsp;&nbsp;&middot;&nbsp;&nbsp;Vibe Coder", title_st))
story.append(Paragraph(
    "Uzvaras iela 5, Ogre, Ogre nov., LV-5001&nbsp;&nbsp;|&nbsp;&nbsp;"
    "jiyotaka352199@gmail.com&nbsp;&nbsp;|&nbsp;&nbsp;+371 29165331", contact_st))
story.append(Spacer(1, 5))
story.append(rule(1.3, INK, 1))

# ---------- Par mani ----------
story += section("Par mani")
story.append(Paragraph(
    "Mērķtiecīgs IT speciālists ar starptautisku izglītību un praktiskām iemaņām digitālajās "
    "tehnoloģijās; brīvi pārvaldu angļu valodu un esmu gatavs jauniem izaicinājumiem. Apvienoju "
    "spēcīgus tehniskos pamatus (Python, PHP, SQL) ar mūsdienīgu, mākslīgā intelekta paātrinātu "
    "darbplūsmu (vibe coding), kas ļauj sarežģītus risinājumus izstrādāt stundās, nevis nedēļās. "
    "Uzņēmumā paaugstināju produktivitāti par <b>20%</b> ar radošu problēmu risināšanu un precīzu "
    "tehnisko analīzi.", body_st))

# ---------- Tehniskās prasmes ----------
story += section("Tehniskās prasmes")
skills = [
    ("Valodas un ietvari", "Python, PHP, SQL, HTML5, CSS3, JavaScript (ES6)"),
    ("Datubāzes un arhitektūra", "MS SQL Server, SQLite, MS Access, MS Excel (padziļināta analītika), VS Code"),
    ("MI orķestrēšana un prompting", "Claude 3.5 Sonnet, OpenAI GPT-4o, Cursor OS, GitHub Copilot, padziļināta promptu inženierija (Chain-of-Thought, konteksta pārvaldība)"),
    ("Dizains un multivide", "Adobe Photoshop, video montāža / rediģēšana, UI/UX prototipēšana, Canva Pro"),
]
for label, items in skills:
    story.append(Paragraph("<b>%s:</b>&nbsp;&nbsp;%s" % (label, items), skill_st))

# ---------- Darba pieredze ----------
story += section("Darba pieredze")
story.append(Paragraph("IT atbalsta speciālists", role_st))
story.append(Paragraph("Tehnoloģiju uzņēmums, Latvija&nbsp;&nbsp;&middot;&nbsp;&nbsp;Jan. 2023 – Apr. 2026", meta_st))
for b in [
    "Uzturēju uzņēmuma informācijas sistēmas, nodrošinot to efektivitāti, un ieviesu jaunus IT "
    "risinājumus, kas palielināja produktivitāti par <b>20%</b>.",
    "<b>Datu analītika un datubāžu pārvaldība:</b> sarežģītu datu tabulu izveide, manipulācija un "
    "analīze MS Excel vidē; datu atlase un vaicājumi ar SQL; strukturētu datubāzu projektēšana un "
    "uzturēšana MS Access.",
    "<b>Sistēmu dokumentācija un vizualizācija:</b> profesionālu tehnisko atskaišu (reports) un "
    "dokumentācijas sagatavošana MS Word; informatīvu posteru un vizuālo materiālu izstrāde "
    "platformās Canva un Adobe Photoshop.",
    "<b>Tīmekļa izstrāde (Frontend):</b> mājaslapu izstrāde (HTML, CSS, JavaScript) atbilstoši "
    "kodēšanas standartiem VS Code vidē.",
    "<b>Programmēšana un skriptēšana:</b> programmatūras un loģikas izstrāde Python valodā; "
    "pamatzināšanas un neliela pieredze servera puses programmēšanā ar PHP.",
    "<b>Prezentāciju un dizaina izstrāde:</b> augstas kvalitātes interaktīvas prezentācijas MS "
    "PowerPoint; mājaslapu prototipu un grafisko elementu dizains platformā Canva.",
]:
    story.append(bullet(b))

# ---------- Projekti ----------
story += section("Atlasītie projekti")
projects = [
    ("AuraDB", "Python, SQL, SQLite",
     "Automatizēta inventāra un relāciju datu plūsma: Python skripti pārveido nestrukturētus CSV "
     "loģistikas datus relāciju shēmās; pielāgota SQL indeksēšana paātrināja datu izgūšanu lielās "
     "tabulās <b>3.4x</b>."),
    ("CorePulse", "PHP, Frontend/Backend",
     "Iekšējais korporatīvais ERP un analītikas portāls: drošs tīmekļa risinājums ar PHP REST API "
     "(PDO + MS SQL) un dinamisku JavaScript saskarni; automātiska PDF atskaišu ģenerēšana."),
    ("OmniForm", "JavaScript, Regex, SQL",
     "Dinamiska tīmekļa anketa un datu uztveršanas dzinis: reāllaika klienta puses Regex validācija "
     "un dinamiska DOM renderēšana, droši sadarbojoties ar SQL aizmugursistēmu."),
    ("InSight", "Datu analītika",
     "Padziļināts MS Excel datu analītikas modelis: Pivot izsekošana un daudznosacījumu meklēšana, "
     "salīdzinot <b>50 000+</b> rindas ar SQL Server, lai automātiski ģenerētu paneļus bez aiztures."),
    ("QuantBot", "Python",
     "Automatizēts Python tīmekļa skrāpis un uzdevumu plānotājs: plānota datu vākšana un JSON "
     "apstrāde nedēļas datu failos; datu apkopošanas laiks samazināts no nedēļām uz stundām."),
    ("VividMedia", "Dizains un montāža",
     "Zīmola identitāte un reklāmas video komplekts: augstas precizitātes prototipi Canva, vizuālā "
     "apstrāde Adobe Photoshop un kinematogrāfiska īsformāta video montāža precīzi pēc audio."),
]
for name, tags, desc in projects:
    story.append(Paragraph(
        "<b>%s</b>&nbsp;&nbsp;<font color='#7a7a7a'>&middot; %s</font><br/>%s" % (name, tags, desc), proj_st))

# ---------- Izglītība ----------
story += section("Izglītība")
edu = [
    ("ATHE Level 3 Diploma in Information and Digital Technologies",
     "UKversity, Londona, Apvienotā Karaliste", "2025 – 2026", "Merit / ar atzinību"),
    ("BTEC Level 2 Information and Technology",
     "South Bank Colleges, Londona", "2023 – 2025", "Pass / sekmīgi absolvēts"),
    ("Vispārējā vidējā izglītība",
     "Rīgas Strazdumuižas vidusskola – attīstības centrs", "2011 – 2022",
     "Matemātika 5 &middot; Angļu valoda 6 &middot; Latviešu valoda 4"),
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

# ---------- Stiprās puses ----------
story += section("Personības profils — Stiprās puses")
for b in [
    "<b>Analītiskā domāšana:</b> spēja efektīvi strādāt ar lieliem datu apjomiem (Excel, SQL) un "
    "saskatīt sakarības, lai automatizētu procesus.",
    "<b>Starptautiska komunikācija:</b> pateicoties pieredzei Londonā, brīvi pārvaldu profesionālo "
    "angļu valodu un spēju strādāt multikulturālā komandā.",
    "<b>Tehniskā adaptācija:</b> ātri apgūstu jaunas programmēšanas valodas (Python, JavaScript, "
    "PHP) un rīkus, pielāgojoties projekta vajadzībām.",
    "<b>Precizitāte un rūpība:</b> augsta atbildības sajūta, veidojot tehnisko dokumentāciju un "
    "uzturot informācijas sistēmas.",
]:
    story.append(bullet(b))

# ---------- Attīstības virzieni ----------
story += section("Attīstības virzieni")
for b in [
    "<b>Publiskā uzstāšanās:</b> šobrīd komfortablāk jūtos ar tehniskiem uzdevumiem nekā uzstājoties "
    "lielas auditorijas priekšā, taču aktīvi strādāju pie prezentēšanas prasmju uzlabošanas.",
    "<b>Tieksme uz perfekcionismu:</b> reizēm veltu pārāk daudz laika sīkām detaļām (dizaina "
    "niansēm Canva vai koda optimizācijai), taču mācos efektīvāk plānot laiku, lai iekļautos "
    "stingros termiņos.",
    "<b>Backend pieredze (PHP / JavaScript):</b> pārzinu pamatus, taču turpinu patstāvīgas studijas, "
    "lai paplašinātu savu Backend izstrādātāja arsenālu.",
]:
    story.append(bullet(b))

doc.build(story)
print("OK ->", OUT)
