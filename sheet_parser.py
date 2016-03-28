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
    def __init__(self, name, sex, birth, weight, kata, kumite, fuku_go):
        localtime = time.localtime(time.time())
        if(kata == 'xpk' or kata == 'XPK' or kumite == 'xpk' or kumite == 'XPK'):
            self._kataPK = 'X' #kataPK oznacza doswiadczenie tak samo dla kata i kumite. Nie chcialo mi sie wszedzie zmieniac zazwy zmiennej :D
        else:
            self._kataPK = ''
        name = name.split(" "[0])
        self._name = str(name[0].title() + ' ' + name[1].title())
        self._sex = sex
        self._age = localtime.tm_year - birth
        self._weight = weight
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
    def __init__(self, name, people, sex, birth, kata, kumite):
        localtime = time.localtime(time.time())
        if(kata == 'xpkd' or kata == 'XPKD' or kumite == 'xpkd' or kumite == 'XPKD'):
            self._kataPK = 'X' #kataPK oznacza doswiadczenie tak samo dla kata i kumite. Nie chcialo mi sie wszedzie zmieniac zazwy zmiennej :D
        else:
            self._kataPK = ''
        self._name = name
        self._people = people
        self._sex = sex
        self._kata = kata
        self._kumite = kumite
        self._birth = localtime.tm_year - birth

    def __str__(self):
        print (u"Nazwa i wiek \t%s\t%s" % (self._name, self._birth))
        print (u"Ludzie \t\t\t%s" % (self._people))
        print (u"Kumite \t\t\t%s" % self._kumite)
        print (u"Kata \t\t\t%s" % self._kata)
        print (u"Dośw \t\t\t%s" % self._kataPK)
        return ''

    def getName(self):
        return str(self._name + ': ' +self._people)

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
    lp_column = 1
    name_column = 2
    birth_column = 3
    kata_column = 4
    kumite_column = 5
    fukugo_column = 6
    weight_column = 7
    sex_column = 8


    #index = None # kiedyś jak zrobimy inteligentną tabelke z przemieszczeniem to będzie pod LP
    for rx in range(sh.nrows):
        row = sh.row(rx)
        #print row[lp_column].value
        #if (row[lp_column].value == 'LP.'):
        #    print 'NO KURWA'


        if (row[1].value != '' and tabela == False): # Wyszukujemy nazwe druzyny
            #print row[0].value
            club[row[1].value] = row[2].value
        if (tabela == True):
            if(row[lp_column].value != ''):
                #row2 = sh.row(rx+1)
                if(row[kata_column].value == 'x' or row[kata_column].value == 'X' or row[kata_column].value == 'xpk' or row[kata_column].value == 'XPK' or row[kumite_column].value == 'x' or row[kumite_column].value == 'X' or row[kumite_column].value == 'xpk' or row[kumite_column].value == 'XPK' or row[fukugo_column].value == 'x' or row[fukugo_column].value == 'X'):
                #if(row[0+2].value == 'M' or row2[0+2].value == 'M' or row[0+2].value == 'm' or row2[0+2].value == 'm' or row[0+2].value == 'K' or row2[0+2].value == 'K' or row[0+2].value == 'k' or row2[0+2].value == 'k'): # jak nie ma płci to mamy indywidualnego ludzia
                    name = row[name_column].value
                    sex = row[sex_column].value
                    birth = str(str(row[birth_column].value)) # dodac parsowanie
                    birthreg = float(re.sub(r'[a-zA-Z]*','',birth))
                    weight = str("0"+str(row[weight_column].value)) # dodac parsowanie, cebularne zero plus jest po to aby pusty string '' zostal skonwertowany na inta. String 02001 zostanie zmieniony na 2001
                    weightreg = float(re.sub(r'[a-zA-Z]*','',weight))
                    kata = row[kata_column].value
                    kumite = row[kumite_column].value
                    fuku_go = row[fukugo_column].value
                    if(name != ' ' and sex != '' ):
                        ch = Child(name, sex, birthreg, weightreg, kata, kumite, fuku_go)
                        print ch
                        print len(name)
                        childList.append(ch)
                elif(row[kata_column].value == 'xd' or row[kata_column].value == 'XD' or row[kata_column].value == 'xpkd' or row[kata_column].value == 'XPKD' or row[kumite_column].value == 'xd' or row[kumite_column].value == 'XD' or row[kumite_column].value == 'xpkd' or row[kumite_column].value == 'XPKD'): #druzynowe
                    #name = row[0+1].value
                    #people = row2[0+1].value
                    baza = row[name_column].value.split(":"[0])
                    name = baza[0]
                    people = baza[1]
                    sex = row[sex_column].value
                    birth = str("0" +str(row[birth_column].value)) # dodac parsowanie
                    birthreg = float(re.sub(r'[a-zA-Z]*','',birth))
                    kata = row[kata_column].value
                    kumite = row[kumite_column].value
                    if(name != ''):
                        tm = Team(name, people, sex, birthreg, kata, kumite)
                        print tm
                        teamList.append(tm)

        if(row[lp_column].value == 'LP.' or row[lp_column].value == 'Lp.' or row[lp_column].value == 'lp.' or row[lp_column].value == 'LP' or row[lp_column].value == 'Lp' or row[lp_column].value == 'lp'):
            tabela = True
            #if ((row[5].value == 'K' or row[5].value == 'M' or row[5].value == 'k' or row[5].value == 'm') and row[10].value == '' ): # Parsujemy tylko pojedynczych ludzi
            #    childList.append(parseRow(row))
            #elif ((row[5].value == 'K' or row[5].value == 'M') and row[10].value != '' ): # Parsujemy druzyny
            #    teamList.append( Team(row[2].value, row[10].value, row[12].value, row[5].value, row[8].value) )

    print 'ludzie'
    print childList
    print 'teamy'
    print teamList

    #print 'club'
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