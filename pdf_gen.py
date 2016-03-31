# -*- coding: utf-8 -*-
from docxtpl import DocxTemplate

def generatePdf(list, opt, case):

    outputName = ""

    if case == 0:
        sex, category, age, weight, experiance = [ opt[0], opt[1], [opt[2], opt[3]], [opt[4], opt[5]], opt[6] ]

        if experiance == 'Doświadczony':
            outputName += 'ind_' + sex + '_' + category + '_Wiek_' + age[0] + '_' + age[1] + '_Waga_' + weight[0] + '_' + weight[1] + '_doswiadczony'
        else:
            outputName += 'ind_' + sex + '_' + category + '_Wiek_' + age[0] + '_' + age[1] + '_Waga_' + weight[0] + '_' + weight[1] + '_niedoswiadczony'
    elif case == 1:
        sex, experiance, category = [ opt[0], opt[1], opt[2]]
		
        if experiance == 'Doświadczony':
            outputName += 'dru_' + sex + '_' + category  + '_doswiadczony'
        else:
            outputName += 'dru_' + sex + '_' + category  + '_niedoswiadczony'
			
    elif case == 2:
        sex, weight = [ opt[0], [opt[1], opt[2]] ]
		
        outputName = 'fukugo_' + sex + '_Waga_' + weight[0] + '_' + weight[1]
		
    outputName += '.docx'
	
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
        inputFile = "template_64.docx"
    elif listLen > 16:
        iterElem = 32
        graphList = graph32
        inputFile = "template_32.docx"
    elif listLen > 8:
        iterElem = 16
        graphList = graph16
        inputFile = "template_16.docx"
    elif listLen > 4:
        iterElem = 8
        graphList = graph8
        inputFile = "template_8.docx"
    elif listLen > 2:
        iterElem = 4
        graphList = graph4
        inputFile = "template_4.docx"
    else:
        iterElem = 2
        graphList = graph2	
        inputFile = "template_2.docx"

    context = {
				'zawody': "",
				'data' : "",
				'konkurencja' : ""}
    slot = 1
    for i in range(iterElem/2):
        print ("iterator")+str(i)+(" list len ")+str(listLen)+" iterElem "+str(iterElem/2)
        valGraphList = graphList[(2*i)+1]-1 # i -> numer osoby, *2 by uzyskac pare. +1 bo iterujemy liste od zera. -1 poniewaz chcemy sprawdzic nieparzysta osobe z pary. Jesli ona jest, jest parzysta. Jesli nie, to nie ma koniec.
        if valGraphList != 0:
            valGraphList = valGraphList/2
        print(str(valGraphList))
        if valGraphList*2 <= listLen-1:
            context['slot_'+slot] = '%s: %s' % (list[valGraphList][0]+1,list[valGraphList][1][0])
            slot = slot + 1
            context['slot_'+slot] = '%s: %s' % (list[valGraphList][0]+1,list[valGraphList][1][0])
            slot = slot + 1
            print("dodane do slownika")
	
	
    doc = DocxTemplate("templates/"+inputFile)
    doc.render(context)
    print("saving")
    doc.save(outputName)