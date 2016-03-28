# -*- coding: utf-8 -*-
from xlutils.display import quoted_sheet_name
from os import listdir
import xlrd
import time
import re
from xlrd.sheet import Cell
from xlutils.display import cell_display

import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Child:
    def __init__(self, name, sex, birth, weight, kata, kataPK, kumite, fuku_go):
        localtime = time.localtime(time.time())
        self._name = name
        self._sex = sex
        self._age = localtime.tm_year - birth
        self._weight = weight
        self._kataPK = kataPK
        self._kata = kata
        self._kumite = kumite
        self._fuku_go = fuku_go

    def __str__(self):
        st = []
        st.append(self._name)
        st.append(self._sex)
        st.append(self._age)
        st.append(self._weight)
        st.append(self._kata)
        st.append(self._kumite)
        st.append(self._fuku_go)
        st.append(self._kataPK)
        print (u"Imię i Nazwisko \t%s" % self._name)
        print (u'Plec \t\t\t\t%s' % self._sex)
        print (u"Wiek \t\t\t\t%s" %  self._age)
        print (u"Waga \t\t\t\t%s" % self._weight)
        print (u"Kata \t\t\t\t%s" % self._kata)
        print (u"Kumite \t\t\t\t%s" % self._kumite)
        print (u"FUKU-GO \t\t\t\t%s" % self._fuku_go)
        print (u"Dośw \t\t\t\t%s" % self._kataPK)
        return '' # str( st )

    def getName(self):
        return self._name

class Team:
    def __init__(self, name, people, sex, birth, kumite, kata, kataPK):
        localtime = time.localtime(time.time())
        self._name = name
        self._people = people
        self._sex = sex
        self._kata = kata
        self._kumite = kumite
        self._birth = localtime.tm_year - birth
        self._kataPK = kataPK

    def __str__(self):
        print (u"Nazwa i wiek \t%s\t%s" % (self._name, self._birth))
        print (u"Ludzie \t\t\t%s" % (self._people))
        print (u"Kumite \t\t\t%s" % self._kumite)
        print (u"Kata \t\t\t%s" % self._kata)
        print (u"Dośw \t\t\t%s" % self._kataPK)
        return ''

    def getName(self):
        return self._name

class School:
    def __init__(self, club, childList, teamList):
        self._club = club
        self._childList = childList
        self._teamList = teamList

    def getContestantNum(self):
        return len(self._childList)

    def __str__(self):
        print self._club
        for i in range(len(self._childList)):
            print self._childList[i]
        print "Druzyny"
        for i in range(len(self._teamList)):
            print self._teamList[i]
        return ''


#def parseRow(row):
#    return Child(row[2].value, row[5].value, row[6].value, row[7].value, row[8].value, row[9].value, row[11].value, row[13].value)



def parseSheet(sh):
    childList = []
    teamList = []
    club = {}
    tabela = False
    #index = None # kiedyś jak zrobimy inteligentną tabelke z przemieszczeniem to będzie pod LP
    for rx in range(sh.nrows-1):
        row = sh.row(rx)


        if (row[0].value != '' and tabela == False): # Wyszukujemy nazwe druzyny
            #print row[0].value
            club[row[0].value] = row[1].value
        if (tabela == True):
            if(row[0].value != ''):
                row2 = sh.row(rx+1)
                if(row[0+2].value == 'M' or row2[0+2].value == 'M' or row[0+2].value == 'm' or row2[0+2].value == 'm' or row[0+2].value == 'K' or row2[0+2].value == 'K' or row[0+2].value == 'k' or row2[0+2].value == 'k'): # jak nie ma płci to mamy indywidualnego ludzia
                    name = row[0+1].value + ' ' + row2[0+1].value
                    sex = row[0+2].value + '' + row2[0+2].value
                    birth = str(str(row[0+3].value) + '' + str(row2[0+3].value)) # dodac parsowanie
                    birth = float(re.sub(r'[a-zA-Z]*','',birth))
                    weight = str("0"+str(row[0+4].value) + '' + str(row2[0+4].value)) # dodac parsowanie, cebularne zero plus jest po to aby pusty string '' zostal skonwertowany na inta. String 02001 zostanie zmieniony na 2001
                    weight = float(re.sub(r'[a-zA-Z]*','',weight))
                    kata = row[0+5].value + '' + row2[0+5].value
                    kataPK = row[0+6].value + '' + row2[0+6].value
                    kumite = row[0+7].value + '' + row2[0+7].value
                    fuku_go = row[0+9].value + '' + row2[0+9].value
                    if(name != ' ' and sex != '' ):
                        ch = Child(name, sex, birth, weight, kata, kataPK, kumite, fuku_go)
                        print ch
                        #print len(name)
                        childList.append(ch)
                else: #druzynowe
                    name = row[0+1].value
                    people = row2[0+1].value
                    sex = row[0+2].value + '' + row2[0+2].value
                    birth = str("0" +str(row[0+3].value) + '' + str(row2[0+3].value)) # dodac parsowanie
                    birth = float(re.sub(r'[a-zA-Z]*','',birth))
                    kumite = row[0+8].value + '' + row2[0+8].value
                    kata = row[0+10].value + '' + row2[0+10].value
                    kataPK = row[0+11].value + '' + row2[0+11].value
                    if(name != ''):
                        tm = Team(name, people, sex, birth, kumite, kata, kataPK)
                        #print tm
                        teamList.append(tm)

        if(row[0].value == 'LP.' or row[0].value == 'Lp.' or row[0].value == 'lp.' or row[0].value == 'LP' or row[0].value == 'Lp' or row[0].value == 'lp'):
            tabela = True
            #if ((row[5].value == 'K' or row[5].value == 'M' or row[5].value == 'k' or row[5].value == 'm') and row[10].value == '' ): # Parsujemy tylko pojedynczych ludzi
            #    childList.append(parseRow(row))
            #elif ((row[5].value == 'K' or row[5].value == 'M') and row[10].value != '' ): # Parsujemy druzyny
            #    teamList.append( Team(row[2].value, row[10].value, row[12].value, row[5].value, row[8].value) )

    print 'ludzie'
    #print childList
    print 'teamy'
    #print teamList

    #print club
    return School(club, childList, teamList)


def prepareSheet(dir, fileName):
    book = xlrd.open_workbook(dir+"\\"+fileName, encoding_override="cp1252")
    sh = book.sheet_by_index(0)
    return sh

if __name__=='__main__':
    dir = 'D:/zawodnicy/testy'
    filename = 'test.xls'
    dupa = parseSheet(prepareSheet(dir, filename))
    print dupa