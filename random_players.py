# -*- coding: utf-8 -*-
import random
import pdf_gen as pd

def countPlayers(schoolList):
    counter = 0
    for i in range(len(schoolList)):
        counter += len(schoolList[i])
    return counter

def printToFile(outputList, options, case):
    outputList.sort()
    print outputList
    # DO PLIKU KURWA!!!!

    opt = []

    #c0 = kategoria [ true = kata , false = kumite ], sex = [ m , k ], age from, age to, weight from, weight to, exp = [ 'doswiadczony','nie doswiadczony']
    #c1 = sex,exp,kategoria



    if case == 0:
        if options[1] == True:
            opt.append("M")
        else:
            opt.append("K")

        if options[0] == True:
            opt.append("Kata")
        else:
            opt.append("Kumite")


        opt.append(options[2])
        opt.append(options[3])
        opt.append(options[4])
        opt.append(options[5])

        if options[7] == True:
            opt.append("Doświadczony")
        else:
            opt.append("Niedoświadczony")

    elif case == 1:
        if options[0] == True:
            opt.append("M")
        else:
            opt.append("K")

        if options[1] == True:
            opt.append("Doświadczony")
        else:
            opt.append("Niedoświadczony")

        if options[2] == True:
            opt.append("Kata")
        else:
            opt.append("Kumite")
    elif case == 2:
        if options[0] == True:
            opt.append("M")
        else:
            opt.append("K")

        opt.append(options[1])
        opt.append(options[2])

    pd.generatePdf(outputList, opt, case)



def tournamentTree(schoolList):
    _counter = countPlayers(schoolList)
    inL = []
    inR = []
    _left = []
    _right = []
    print _counter

    _finalOutList = []

    for i in range(_counter/2):
        inL.append(i)
        inR.append(i)

    LLen = len(inL)
    RLen = len(inR)

    if (_counter % 2):
        inL.append(_counter/2 + 1)
        LLen = len(inL)

    for i in range(len(schoolList)):
        SLen =  len(schoolList[i])
        count = 0
        while (SLen > 0):

            kk = schoolList[i][random.randrange( SLen)]
            if (LLen > 0):
                k = inL[random.randrange( LLen)]
                _left.insert(k,[kk.getName(), i])
                inL.remove(k)
                LLen -= 1
                SLen -= 1
                schoolList[i].remove(kk)
                continue
            elif (RLen > 0):

                k = inR[random.randrange( RLen)]

                if (_left[k][1] == i):
                    print (str(_left[k][1]) + " nasze i " + str(i) + " " + str(k))
                    while (count < len(inR)):
                        if (_left[inR[count]][1] != i):
                            print ("No i super " + str(_left[inR[count]]) + " nasze i " + kk.getName() + " " + str(i) + "k: " + str(inR[count]))
                            _right.insert(inR[count],[kk.getName(), i])
                            _finalOutList.append( [inR[count], _left[inR[count]], [kk.getName(), i]] )
                            inR.remove(inR[count])
                            schoolList[i].remove(kk)
                            RLen -= 1
                            SLen -= 1
                            count = 0
                            break
                        else:
                            count += 1

                    if (count > len(inR)-1):
                        _finalOutList.append( [inR[len(inR)-1], _left[inR[len(inR)-1]], [kk.getName(), i]] )
                        inR.remove(inR[len(inR)-1])
                        schoolList[i].remove(kk)
                        RLen -= 1
                        SLen -= 1
                        count = 0

                else:
                    _right.insert(k,[kk.getName(), i])
                    _finalOutList.append( [k, _left[k], [kk.getName(), i]] )
                    inR.remove(k)
                    RLen -= 1
                    SLen -= 1
                    schoolList[i].remove(kk)

    print len(_left)
    for i in range(len(_right)):
        print (str(i) + " " + str(_left[i]) + " " + str(_right[i]) )

    if (_counter % 2):
        _finalOutList.append( [len(_left)-1, _left[len(_left)-1], ['']] )
        print (str((len(_left)-1)) + " " + str(_left[len(_left)-1]))

    print len(_finalOutList)
    for i in range(len(_finalOutList)):
        print _finalOutList[i]

    return _finalOutList


