from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

def generate_pdf(report):
    filename = "Project_Report.pdf"

    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    title = styles["Title"]
    heading = styles["Heading1"]
    normal = styles["BodyText"]

    story = []

    # COVER PAGE
    story.append(Spacer(1, 80))
    story.append(Paragraph("<b>COLLEGE PROJECT REPORT</b>", title))
    story.append(Spacer(1, 25))
    story.append(Paragraph("<b>PROJECT REPORT GENERATOR</b>", heading))
    story.append(Spacer(1, 60))

    # DETAILS TABLE
    data = []

    for key, value in report.items():
        data.append([f"<b>{key}</b>", str(value)])

    table = Table(data, colWidths=[180, 300])

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,1),(0,-1),colors.lightgrey),
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
    ]))

    story.append(table)

    story.append(Spacer(1,30))

    story.append(Paragraph("<b>ABSTRACT</b>", heading))
    story.append(Paragraph(report.get("Abstract",""), normal))

    story.append(Spacer(1,20))

    story.append(Paragraph("<b>OBJECTIVES</b>", heading))
    story.append(Paragraph(report.get("Objectives",""), normal))

    story.append(Spacer(1,20))

    story.append(Paragraph("<b>METHODOLOGY</b>", heading))
    story.append(Paragraph(report.get("Methodology",""), normal))

    story.append(Spacer(1,20))

    story.append(Paragraph("<b>CONCLUSION</b>", heading))
    story.append(Paragraph(report.get("Conclusion",""), normal))

    doc.build(story)

    return filename