from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

document =[]
document.append(Image('logo.png', 2.2*inch, 2.2*inch))

def addTitle(doc):
    doc.append(Spacer(1,20))
    doc.append(Paragraph('Meme1 God', ParagraphStyle(name="Name", fontFamily='Helvetica',
    fontSize=36, alignment=TA_CENTER)))
    doc.append(Spacer(1,50))
    return doc

def addParagraph(doc):
    with open('text.txt') as txt:
        for line in txt.read().split('\n'):
            doc.append(Paragraph(line))
            doc.append(Spacer(1,12))
    return doc

document=addTitle(document)

SimpleDocTemplate('meme-god.pdf', pagesize=letter,
                    rightMargin=12, leftmargin=12,
                    topMargin=12, bottomMargin=6).build(addParagraph(document))

