# -*- coding: utf-8 -*-
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def generatePdf(list, opt, case):

    #width, height = A4
    # dodanie czcionek
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleN.fontSize = 14
    styleN.fontName = 'Arial-Bold'


	
    Story=[]
    age = []
    weight = []
    name = ''

    if case == 0:
        sex, category, age, weight, experiance = [ opt[0], opt[1], [opt[2], opt[3]], [opt[4], opt[5]], opt[6] ]

        ptext = "Kategoria: %s" % category
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        ptext = "Uczestnik: %s" % experiance
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        ptext = "Płeć: %s" % sex
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        ptext = "Wiek od: %s do: %s" % (age[0], age[1])
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        ptext = "Waga od: %s do: %s" % (weight[0], weight[1])
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        if experiance == 'Doświadczony':
            name += 'ind_' + sex + '_' + category + '_Wiek_' + age[0] + '_' + age[1] + '_Waga_' + weight[0] + '_' + weight[1] + '_doswiadczony'
        else:
            name += 'ind_' + sex + '_' + category + '_Wiek_' + age[0] + '_' + age[1] + '_Waga_' + weight[0] + '_' + weight[1] + '_niedoswiadczony'
    elif case == 1:
        sex, experiance, category = [ opt[0], opt[1], opt[2]]

        ptext = "Kategoria: %s" % category
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        ptext = "Uczestnik: %s" % experiance
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        ptext = "Płeć: %s" % sex
        Story.append(ptext)
        #Story.append(Spacer(1, 4))

        if experiance == 'Doświadczony':
            name += 'dru_' + sex + '_' + category  + '_doswiadczony'
        else:
            name += 'dru_' + sex + '_' + category  + '_niedoswiadczony'

    elif case == 2:
        sex, weight = [ opt[0], [opt[1], opt[2]] ]

        ptext = "Płeć: %s" % sex
        Story.append(ptext)
        #Story.append(Paragraph(ptext, styles["Normal"]))
        #Story.append(Spacer(1, 4))

        ptext = "Waga od: %s do: %s" % (weight[0], weight[1])
        Story.append(ptext)
        #Story.append(Paragraph(ptext, styles["Normal"]))
        #Story.append(Spacer(1, 4))

        name += 'wolna_' + sex + '_Waga_' + weight[0] + '_' + weight[1]


    name += '.pdf'

    '''
    doc = SimpleDocTemplate(name, pagesize=letter,
                        rightMargin=72,leftMargin=42,
                        topMargin=12,bottomMargin=12)

    Story.append(Spacer(1, 12))

    for i in range(len(list)):
        ptext = '<font size=12>%s: %s</font>' % (list[i][0]+1,list[i][1][0])
        Story.append(Paragraph(ptext, styles["Normal"]))
        ptext = '<font size=12>%s: %s</font>' % (list[i][0]+1, list[i][2][0])
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 12))

    # doc.build(Story)
    '''
    num = 0
    #name = 'hello.pdf'
    c = canvas.Canvas(name, pagesize=A4)
    c.setFont('Arial-Bold', 16)
    width, height = A4

    graphic = "v3.jpg"
    mask = [254,255, 254,255, 254,255]
    c.drawImage(graphic, 0, 0, width=width, height=height, mask=mask)

    c.drawString(width/2, 5 , '%s' % str(num))
    num += 1

    hy = height
    for i in range(len(Story)):
        c.drawString(50, hy - 40 , '%s' % Story[i])
        hy -= 20

    xx = 10
    yy = 66
	
    afterFirst = False
    graph2 = [1,2]
    graph4 = [1,2,3,4]
    graph8 = [1,2,5,6,3,4,7,8]
    graph16 = [1,2,9,10,5,6,13,14,3,4,11,12,7,8,15,16]
    graph32 = [1,2,17,18,5,6,21,22,9,10,25,26,13,14,29,30,3,4,19,20,7,8,23,24,11,12,27,28,15,16,31,32]
    graph64 = [1,2,33,34,17,18,49,50,9,10,41,42,25,26,57,58,5,6,37,38,21,22,53,54,13,14,45,46,29,30,61,62,3,4,35,36,19,20,51,52,11,12,43,44,27,28,59,60,7,8,39,40,23,24,55,56,15,17,47,48,31,32,63,64]
		
    listLen = len(list)*2
		
    if listLen > 32:
        iterElem = 64
        graphList = graph64
    elif listLen > 16:
        iterElem = 32
        graphList = graph32
    elif listLen > 8:
        iterElem = 16
        graphList = graph16
    elif listLen > 4:
        iterElem = 8
        graphList = graph8
    elif listLen > 2:
        iterElem = 4
        graphList = graph4
    else:
        iterElem = 2
        graphList = graph2		
		
    for i in range(iterElem/2):
        print ("iterator")+str(i)+(" list len ")+str(listLen)
        if ((i)%8 == 0):
            if (afterFirst):
                c.showPage()
            afterFirst = True
            c.setFont('Arial-Bold', 16)
            width, height = A4

            graphic = "v3.jpg"
            mask = [254,255, 254,255, 254,255]
            xx = 10
            yy = 66
            c.drawImage(graphic, 0, 0, width=width, height=height, mask=mask)
            c.drawString(width/2, 5 , '%s' % str(num))
            num += 1

            hy = height
            for j in range(len(Story)):
                c.drawString(50, hy - 40 , '%s' % Story[j])
                hy -= 20
        valGraphList = graphList[(2*i)+1]-1
        if valGraphList != 0:
		    valGraphList = valGraphList/2
        print(str(valGraphList))
        if valGraphList*2 <= listLen-1:
            c.drawString(xx,yy, '%s: %s' % (list[valGraphList][0]+1,list[valGraphList][1][0]))
            yy += 30

            c.drawString(xx,yy, '%s: %s' % (list[valGraphList][0]+1, list[valGraphList][2][0]))
            yy += 51.5
        else:
            yy += 30
            yy += 51.5
			

    c.showPage()
    c.save()