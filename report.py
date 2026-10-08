"""PDF report generation (ReportLab)."""
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from knowledge import DISCLAIMER, FOOD_GROUPS, ORDER, VITAMINS

GREEN, DARK, MUTED = colors.HexColor("#0f766e"), colors.HexColor("#0f172a"), colors.HexColor("#64748b")
RED, OK = colors.HexColor("#dc2626"), colors.HexColor("#16a34a")


def build_report(user, assessment, ranges, cutoffs) -> bytes:
    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                            topMargin=16 * mm, bottomMargin=16 * mm,
                            title="Vitamin Deficiency Report", author="Vitamin Deficiency Prediction & Food Recommendation")
    ss = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=ss["Title"], textColor=GREEN, fontSize=18, leading=22, alignment=0, spaceAfter=2)
    h2 = ParagraphStyle("h2", parent=ss["Heading2"], textColor=DARK, fontSize=13, spaceBefore=14, spaceAfter=6)
    body = ParagraphStyle("b", parent=ss["BodyText"], textColor=DARK, fontSize=10, leading=14)
    small = ParagraphStyle("s", parent=body, textColor=MUTED, fontSize=8.5, leading=12)

    flags, levels = assessment["flags"], assessment["levels"]
    deficient = [v for v in ORDER if flags[v]]
    s = [Paragraph("Vitamin Deficiency Prediction &amp; Food Recommendation", h1),
         Paragraph("Personal Vitamin Report", body), Spacer(1, 8)]

    meta = Table([
        ["Name", user["name"], "Report ID", f"#{assessment['id']:05d}"],
        ["Email", user["email"], "Date", assessment["created_at"] + " UTC"],
    ], colWidths=[22 * mm, 66 * mm, 24 * mm, 60 * mm])
    meta.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 9), ("TEXTCOLOR", (0, 0), (0, -1), MUTED),
        ("TEXTCOLOR", (2, 0), (2, -1), MUTED), ("TEXTCOLOR", (1, 0), (1, -1), DARK),
        ("TEXTCOLOR", (3, 0), (3, -1), DARK), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBELOW", (0, -1), (-1, -1), 0.6, colors.HexColor("#e2e8f0")),
    ]))
    s.append(meta)

    s.append(Paragraph("Summary", h2))
    if deficient:
        names = ", ".join(VITAMINS[v]["name"] for v in deficient)
        s.append(Paragraph(f"<b>{len(deficient)} of 6</b> vitamins were flagged as low: "
                           f"<font color='#dc2626'><b>{names}</b></font>.", body))
    else:
        s.append(Paragraph("<font color='#16a34a'><b>All 6 vitamins are in the healthy range.</b></font> "
                           "Keep up a varied, balanced diet.", body))

    s.append(Paragraph("Your vitamin levels", h2))
    rows = [["Vitamin", "Your value", "Dataset range", "Low if at or below", "Status"]]
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), GREEN), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#e2e8f0")),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    for i, v in enumerate(ORDER, start=1):
        lo, hi = ranges[v]
        low = flags[v]
        rows.append([VITAMINS[v]["name"], f"{levels[v]:g}", f"{lo:g} - {hi:g}",
                     f"{cutoffs[v]:g}", "LOW" if low else "Normal"])
        style += [("TEXTCOLOR", (4, i), (4, i), RED if low else OK),
                  ("FONTNAME", (4, i), (4, i), "Helvetica-Bold")]
    t = Table(rows, colWidths=[44 * mm, 28 * mm, 34 * mm, 36 * mm, 28 * mm])
    t.setStyle(TableStyle(style))
    s.append(t)

    s.append(Paragraph("Food recommendations", h2))
    if deficient:
        g = FOOD_GROUPS.get(assessment["food_group"])
        if g:
            s.append(Paragraph(f"<b>Suggested food pattern:</b> {g[0]} - {g[2]}", body))
            s.append(Spacer(1, 6))
        frows = [["Low vitamin", "Why it matters", "Good food sources"]]
        for v in deficient:
            info = VITAMINS[v]
            frows.append([Paragraph(f"<b>{info['name']}</b>", body), Paragraph(info["role"], body),
                          Paragraph(", ".join(info["foods"]), body)])
        ft = Table(frows, colWidths=[34 * mm, 56 * mm, 80 * mm])
        ft.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), DARK), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, 0), 9),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#e2e8f0")),
            ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ]))
        s.append(ft)
        s.append(Paragraph("Possible signs of low levels", h2))
        for v in deficient:
            s.append(Paragraph(f"<b>{VITAMINS[v]['name']}:</b> {VITAMINS[v]['symptoms']}", body))
            s.append(Spacer(1, 3))
    else:
        s.append(Paragraph("No deficiency detected. Continue eating a colourful mix of fruits, vegetables, "
                           "whole grains, dairy or protein, and nuts.", body))

    s.append(Spacer(1, 18))
    s.append(Paragraph(f"<b>Disclaimer.</b> {DISCLAIMER}", small))
    doc.build(s)
    return buf.getvalue()
