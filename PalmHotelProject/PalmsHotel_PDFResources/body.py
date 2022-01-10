
from reportlab.platypus import Table, Image, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

import csv

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
    tablesWidth = widthList[1]- leftPadding

    res = Table([
        ['','Offer', ''],
        ['',_genContactsTable(tablesWidth,heightList[1]), ''],
        ['',_genPriceListTable(tablesWidth,heightList[2]), ''],
        ['',_genDescriptionParas(), ''],
        ['',_genAboutTable(widthList[1], heightList[4]), ''],
    ], widthList,
    heightList)



    res.setStyle([
        #('GRID', (0,0),(-1,-1), 1, 'red'),
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

#Contact informatiion after header
def _genContactsTable(width, height):
    widthList=[
        width *30 /100,
        width *30 /100,
        width *20 /100,
        width *20 /100,
    ]
    heightList =[
        height * 25 /100,
        height * 25 /100,
        height * 25 /100,
        height * 25 /100,
       
    ]
    dataList =[]
    with open(r'C:\Users\qinqin.zha\OneDrive - NeoGenomics Laboratories, Inc\Documents\QZ_JR_presentations -NSM\BI\PalmHotelProject\PalmsHotel_PDFResources\resources\tabledata.txt', 'r') as file: 
        for line in file:
            if line != '\n':
                dataList.append(line.replace('\n','')) # problem 2
    matrix =[
        ['', '','',''],
        ['', '','',''],
        ['', '','',''],
        ['', '','',''],
       
    ]

    idx=0
    for ridx, row in enumerate(matrix):
        for cidx, col in enumerate(row):
            matrix[ridx][cidx]= dataList[idx]
            idx +=1 # problem 3 and 4
            if idx == len(dataList):
                break
        if idx == len(dataList):
            break

    res =Table(matrix, widthList, heightList)
    res.setStyle([
        #('GRID', (0,0), (-1,-1), 1, 'red') ,

        ('ALIGN', (3,0),(3,-1), 'RIGHT'),
        ('RIGHTPADDING', (3,0),(3,-1), 20),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),

    ])
    return res

    

#price table after contact table
def _genPriceListTable(width, height):
    style =ParagraphStyle('titleprices')
    style.fontSize=20
    style.fontName= 'Helvetica-Bold'
    style.spaceAfter = 15

    titlePara = Paragraph('Details', style)

    priceTable = _genPricesTable(width, height * 70/100)


    elementsList =[titlePara, priceTable]
    res = Table(
        [
            [elementsList]
        ],
        width, 
        height)

    res.setStyle([
        # ('GRID', (0,0), (-1,-1), 1, 'red'),
        ('LEFTPADDING',(0,0),(0,0),0),
       ('BOTTOMPADDING',(0,0),(1,0),0),
    ])
    return res

#load data from csv file

def _genPricesTable(width, height):

    matrix = []
    with open(r'C:\Users\qinqin.zha\OneDrive - NeoGenomics Laboratories, Inc\Documents\QZ_JR_presentations -NSM\BI\PalmHotelProject\PalmsHotel_PDFResources\resources\pricesTable.csv', 'r') as file:
        matrix =list(csv.reader(file))
    if len(matrix) <2 or len(matrix[0]) !=6:
        return Table([['no data']])

    widthList=[
        width * 20/100,
        width * 20/100,
        width * 25/100,
        width * 15/100,
        width * 10/100,
        width * 10/100,

    ]
    rowCount = len(matrix)
    res = Table(matrix,widthList, height/rowCount)
    #r-red, g- green, b- blue, a -alpha (opacity)
    color =colors.toColor('rgba(0, 115, 153, 0.9)')

    res.setStyle([
       # ('GRID', (0,0), (-1,-1), 1, 'red') ,
        ('INNERGRID', (0,0), (-1,-1), 0.5, 'grey'),
        ('BACKGROUND', (0,0), (-1, 0), color),
        ('TEXTCOLOR', (0,0), (-1, 0), 'white'),
        ('FONTSIZE', (0,0), (-1, 0), 12),
        ('FONTNAME', (0,0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (1,0), (-1, 0), 'CENTER'),
        ('ALIGN', (1,1), (2, -1), 'CENTER'),
        ('ALIGN', (5,1), (5, -1), 'RIGHT'),
        ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
        #('ROWBACKGROUNDs', (0,1),(-1,-1), ['antiquewhite', 'beige', colors.grey]) #not working, need to figuout

    ])
    for i in range(1, rowCount):
        if i % 2 == 0:
            bc=colors.antiquewhite
        else:
            bc=colors.beige

        res.setStyle([
            ('BACKGROUND', (0, i), (-1, i),bc)
        ])
    return res


#Function for paragraph style and paragraph lists and html style.
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
       [#('GRID', (0,0), (-1,-1), 1, 'red') ,
       ('LEFTPADDING',(0,0),(0,0),0),
       ('BOTTOMPADDING',(0,0),(1,0),0),

       ('ALIGN',(0,0),(0,0), 'CENTER'),
        ('VALIGN',(0,0),(1,0), 'MIDDLE'), # both cells vertical centered
       
       ]
    )

    return res 