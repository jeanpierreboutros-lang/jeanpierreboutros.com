#!/usr/bin/env python3
"""Build the one-page professional profile from confirmed portfolio facts.

Requires ReportLab. Fonts are embedded in the PDF; viewers need no fonts installed.
Set JPB_PROFILE_FONT_DIR to a directory containing the four TTF files below when
building somewhere other than the author's Mac.
"""
from html import escape
import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/jean-pierre-boutros-profile.pdf"
FONT_DIR = Path(os.environ.get("JPB_PROFILE_FONT_DIR", "/System/Library/Fonts/Supplemental"))
for name, filename in [
    ("ProfileSerif", "Georgia.ttf"),
    ("ProfileSerifItalic", "Georgia Italic.ttf"),
    ("ProfileSans", "Arial.ttf"),
    ("ProfileSansBold", "Arial Bold.ttf"),
]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily("ProfileSans", normal="ProfileSans", bold="ProfileSansBold")

INK = colors.HexColor("#1C1C1A")
MUTED = colors.HexColor("#575750")
PAPER = colors.HexColor("#FAF9F5")
GOLD = colors.HexColor("#C8A96E")
DARK_GOLD = colors.HexColor("#80602D")
RULE = colors.HexColor("#DDD9CE")
SITE = "https://www.jeanpierreboutros.com/"

PRODUCTIONS = [
    (
        "The Eighties... The Knockout", "the-eighties",
        "FOH engineer | Kuwait | October 2026",
        "National Theatre, Sheikh Jaber Al-Ahmad Cultural Centre (JACC).",
    ),
    (
        "Abeer Nehme with Qatar Philharmonic Orchestra", "abeer-nehme-qatar",
        "FOH engineer | Doha, Qatar | 23 January 2026",
        "U VENUE. Presented by U Events.",
    ),
    (
        "Marina Viotti - Opera gala", "marina-viotti",
        "FOH engineer | Lebanon | 8 September 2026",
        "Beirut International Opera Festival gala, Roman Amphitheatre, Zouk Mikael.",
    ),
    (
        "Lebanese National Philharmonic Orchestra", "lebanese-philharmonic-diman",
        "FOH engineer | Diman, North Lebanon | 26 July 2026",
        "Eternal Covenant. Patriarchal Summer Residence; conductor Harout Fazlian.",
    ),
    (
        "Cartoon Orchestra", "cartoon-orchestra",
        "FOH engineer | Kuwait | 4 October 2025",
        "JACC National Theatre. Musical direction: Dr Khaled Noori.",
    ),
    (
        "Marcel Khalifé - Selected FOH credits", "marcel-khalife-muscat",
        "FOH engineer | Istanbul, 2017; Muscat, Oman, 2019",
        "Al Sharq Symphony: Istanbul Philharmonic, Lubnan Baalbaki. "
        "Royal Opera House Muscat: House of Musical Arts, 26-27 Sep 2019.",
    ),
    (
        "Nancy Ajram - FOH & monitor credits", "nancy-ajram-olympia",
        "FOH engineer | L'Olympia, Paris | 10 June 2022",
        "Monitor engineer: Expo 2020 Dubai (2021); Baligh Hamdi Night and "
        "Night of Arab Stars, Riyadh (2023); Warda Night, Jeddah (2024).",
    ),
    (
        "Papal Mass broadcast", "work",
        "Broadcast sound engineer | Beirut Waterfront | 2025",
        "Production during Pope Leo XIV's visit to Lebanon.",
    ),
]


def paragraph(pdf, text, x, top, width, *, font="ProfileSans", size=9.6,
              leading=13.3, color=INK, gap=0):
    style = ParagraphStyle("profile", fontName=font, fontSize=size, leading=leading,
                           textColor=color, alignment=TA_LEFT, spaceAfter=0,
                           splitLongWords=False, allowWidows=0, allowOrphans=0)
    block = Paragraph(text, style)
    _, height = block.wrap(width, 2000)
    block.drawOn(pdf, x, top - height)
    return top - height - gap


def section(pdf, title, x, top, width):
    return paragraph(pdf, title, x, top, width, font="ProfileSerif", size=15,
                     leading=18, gap=12)


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1, invariant=1,
                        lang="en-US")
    pdf.setTitle("Jean-Pierre Boutros | Professional Profile")
    pdf.setAuthor("Jean-Pierre Boutros")
    pdf.setSubject("FOH, monitor, studio and broadcast sound engineering; selected credits and contact")
    pdf.setKeywords("Jean-Pierre Boutros, FOH, monitor engineer, sound engineer, StudioJPB, Zynforge Audio")
    pdf.setCreator("Jean-Pierre Boutros portfolio")
    pdf.setViewerPreference("DisplayDocTitle", "true")
    width, height = A4
    margin = 40
    usable = width - 2 * margin
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, fill=1, stroke=0)

    # A restrained brand header leaves the body easy to read and print.
    header_bottom = height - 166
    pdf.setFillColor(colors.HexColor("#111210"))
    pdf.rect(0, header_bottom, width, 166, fill=1, stroke=0)
    pdf.saveState()
    pdf.setFillColor(GOLD)
    label = pdf.beginText(margin, height - 29)
    label.setFont("ProfileSansBold", 7.3)
    label.setCharSpace(1.6)
    label.textOut("PROFESSIONAL PROFILE")
    pdf.drawText(label)
    pdf.restoreState()
    pdf.setFillColor(colors.HexColor("#F3F0E8"))
    pdf.setFont("ProfileSerif", 29)
    pdf.drawString(margin - 1, height - 70, "Jean-Pierre")
    pdf.setFillColor(GOLD)
    pdf.setFont("ProfileSerifItalic", 31)
    pdf.drawString(margin - 1, height - 108, "Boutros")
    pdf.setFillColor(colors.HexColor("#F3F0E8"))
    pdf.setFont("ProfileSans", 10)
    pdf.drawString(margin, height - 134, "Live, studio & broadcast sound engineer")
    pdf.setFillColor(colors.HexColor("#C9C6BB"))
    pdf.setFont("ProfileSans", 8.4)
    pdf.drawString(margin, height - 151, "Lebanon | Working internationally")
    photo_width, photo_height = 154, 154 * 2 / 3
    photo_x, photo_y = width - margin - photo_width, height - 137
    pdf.drawImage(str(ROOT / "photos/about-portrait.jpg"), photo_x, photo_y,
                  width=photo_width, height=photo_height, preserveAspectRatio=True)
    pdf.setFillColor(GOLD)
    pdf.rect(photo_x, photo_y - 6, photo_width, 1.4, fill=1, stroke=0)

    bio = (
        "Jean-Pierre Boutros is a sound engineer based in Lebanon, working internationally "
        "across FOH and monitor engineering, studio production, broadcast and audio system integration. "
        "He founded StudioJPB in Jounieh in 2008 and develops audio software through Zynforge Audio."
    )
    top = paragraph(pdf, bio, margin, header_bottom - 23, usable,
                    size=10, leading=14, gap=23)
    left_width, right_x = 316, 383
    right_width = width - margin - right_x
    pdf.setStrokeColor(RULE)
    pdf.setLineWidth(.6)
    pdf.line(369, top + 3, 369, 127)

    left = section(pdf, "Selected productions", margin, top, left_width)
    for title, anchor, metadata, detail in PRODUCTIONS:
        left = paragraph(pdf, f'<link href="{SITE}#{anchor}">{escape(title)}</link>',
                         margin, left, left_width, font="ProfileSansBold", size=9.9,
                         leading=12.4, gap=2)
        left = paragraph(pdf, escape(metadata), margin, left, left_width,
                         size=8.4, leading=10.8, color=DARK_GOLD, gap=2)
        left = paragraph(pdf, escape(detail), margin, left, left_width,
                         size=9.1, leading=12, color=MUTED, gap=5)

    left = paragraph(pdf,
        "<b>Selected collaborators</b><br/>"
        "Nancy Ajram, Marcel Khalifé, Georges Wassouf, Carole Samaha, "
        "Abeer Nehme, Ramy Ayyach, Charbel Rouhana, Rasha Rizk and Marina Viotti.",
        margin, left - 4, left_width, size=9.1, leading=12.5, color=MUTED)

    right = section(pdf, "Expertise", right_x, top, right_width)
    for item in ["Live sound & FOH", "Monitor engineering", "Broadcast sound", "Recording & tracking",
                 "Mixing & mastering", "Audio system integration",
                 "Sound design & post-production"]:
        right = paragraph(pdf, escape(item), right_x, right, right_width,
                          size=9.4, leading=12.5, gap=3)
    right = section(pdf, "Studio & systems", right_x, right - 12, right_width)
    right = paragraph(pdf, "<b>StudioJPB</b><br/>Founder | Jounieh, 2008", right_x,
                      right, right_width, size=9.2, leading=12.7, gap=9)
    right = paragraph(pdf, "Integration work includes Merwas Studios, Riyadh, and "
                      "Playsound Studios, Lebanon.", right_x, right, right_width,
                      size=9.2, leading=12.7, color=MUTED, gap=18)
    right = section(pdf, "Software", right_x, right, right_width)
    right = paragraph(pdf, "<b>Founder, Zynforge Audio</b><br/>Live, Recording &amp; Stage", right_x, right,
                      right_width, size=9.2, leading=14, gap=18)
    right = section(pdf, "Television", right_x, right, right_width)
    for programme, channel in [("Hek Menghanni", "MTV Lebanon"),
                               ("Ghanni Al Aali", "Abu Dhabi TV"),
                               ("Ethnophilia", "Al Mayadeen TV")]:
        right = paragraph(pdf, f"<b>{programme}</b><br/>{channel}", right_x,
                          right, right_width, size=9, leading=12.3,
                          color=MUTED, gap=8)
    if min(left, right) < 124:
        raise ValueError(f"Content exceeds the one-page layout: left={left}, right={right}")

    # Clickable contact details remain selectable text, including in print copies.
    pdf.setStrokeColor(RULE)
    pdf.line(margin, 108, width - margin, 108)
    paragraph(pdf, "Discuss a production", margin, 94, usable,
              font="ProfileSerif", size=14, leading=17)
    paragraph(pdf, '<link href="mailto:jp@jeanpierreboutros.com">'
              'jp@jeanpierreboutros.com</link>', margin, 67, 245,
              size=9.5, leading=12)
    paragraph(pdf, '<link href="https://wa.me/9613883863">+961 3 883 863 | WhatsApp</link>',
              344, 67, 211, size=9.5, leading=12)
    paragraph(pdf, f'<link href="{SITE}">www.jeanpierreboutros.com</link>',
              margin, 46, 245, size=9, leading=12, color=DARK_GOLD)
    paragraph(pdf, "Full credits & project details online", 344, 46, 211,
              size=8.1, leading=12, color=MUTED)
    pdf.showPage()
    pdf.save()
    print(f"Created {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build()
