
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

def genBodyTable(width, height):
    widthList =[
        width * 10/100,  # left "PADDING"
        width * 80/100,  # value
        width * 10/100,   # right "PADDING"

    ]
    heightList = [ 
        height * 10/100, # offer
        height * 15/100, # contacts
        height * 35/100, #price list
        height * 30/100,#descpition
        height * 10/100, #about
    ]


    color =colors.HexColor('#003363')
    leftPadding = 20 

    res = Table([
        ['','Offer', ''],
        ['',_genContactsTable(widthList[1],heightList[1]), ''],
        ['',_genPriceListTable(widthList[1],heightList[2]), ''],
        ['',_genDescriptionParas(), ''],
        ['',_genAboutTable(widthList[1], heightList[4]), ''],
    ], widthList,
    heightList)



    res.setStyle([
        ('GRID', (0,0),(-1,-1), 1, 'red'),
        ('LINEBELOW', (1,0), (1,1), 1, color),
        ('LINEBELOW', (1,3), (1,3), 1, color),

        ('LEFTPADDING', (1,0),(1,3), leftPadding),
        ('FONTSIZE', (1,0), (1,0), 30),
        ('BOTTOMPADDING', (1,0), (1,0), 30),
        ('BOTTOMPADDING', (1,1), (1,2), 0),
        ('BOTTOMPADDING', (1,3), (1,3), 40),
        ('BOTTOMPADDING', (1,4), (1,4), 0),
        ('LEFTPADDING', (1,4), (1,4), 0),

    ])
    return res

def _genContactsTable(width, height):


    return 'CONTACT'


def _genPriceListTable(width, height):
    return 'PRICES'

def _genDescriptionParas():
    paraList =[]
    para1Style= ParagraphStyle('para1d')
    para1Style.fontSize = 10
    para1Style.spaceAfter = 15
    para1Style.textColor = colors.HexColor('#003363')

    para1 = Paragraph("""
    <b>
    Thank you very much for using the services from us at Palms. 
    Here at Palms Hotel we have living rooms and well-equipped
    meeting rooms of all sizes with a capacity from 8 - 300 people,
    so that we will be well prepared for most needs you may have.
    </b>
    """, para1Style)

    para2Style= ParagraphStyle('para2d')
    para2Style.fontSize = 10
    para2Style.spaceAfter = 15
    para2 = Paragraph("""
    <i>
    Palms Hotel is also known for its cuisine and good service,
    therefore you can feel confident that your needs and desires
    will be well taken care of, whether you choose to use our
    beautiful Restaurant Palms or other living rooms,
    we guarantee a <u>good experience with us.</u>
    </i>
    """, para2Style)

    paraList.append(para1)
    paraList.append(para2)
    return paraList



def _genAboutTable(width, height):
    widthList=[ 
        width * 20/100,
        width * 80/100,
    ]
    img =Image(
       'resources\logoParadise.png',
       widthList[0],
       height,
       kind = 'proportional'
    )
    para1Style= ParagraphStyle('para1')
    para1Style.fontSize = 14
    para1Style.spaceAfter =15

    para2Style= ParagraphStyle('para2')
    para2Style.fontSize = 8
    
    para1 = Paragraph('Palms Hotels', para1Style)
    para2 = Paragraph("""
    Ever since 2004, Palms Hotels has received accommodation and
    dining guests. The hotel and the restaurants has been run
    and owned by the Dubai SGPS.
    """, para2Style)

    paraList=[para1,para2]

    res = Table([
        [ img, paraList]
    ], 
    widthList,
    height)

    res.setStyle(
       [('GRID', (0,0), (-1,-1), 1, 'red') ,
       ('LEFTPADDING',(0,0),(0,0),0),
       ('BOTTOMPADDING',(0,0),(1,0),0),

       ('ALIGN',(0,0),(0,0), 'CENTER'),
        ('VALIGN',(0,0),(1,0), 'MIDDLE'), # both cells vertical centered
       
       ]
    )

    return res 