import sheet_parser as sp


def sortSex(list, men):
    _men = []
    _women = []
    for i in range(len(list)):
        if (list[i]._sex == 'K' or list[i]._sex == 'k'):
            _women.append(list[i])
        else:
            _men.append(list[i])

    if men == True:
        return _men
    else:
        return _women

def sortExp(list, exp):
    _sen = []
    _ch = []
    for i in range(len(list)):
        if (list[i]._kataPK != ''):
            _sen.append(list[i])
        else:
            _ch.append(list[i])

    if exp == True:
        return _ch
    else:
        return _sen

def sortKata(list, kata):
    _kata = []
    _kumite = []
    for i in range(len(list)):
        if (list[i]._kata != ''):
            _kata.append(list[i])
        if (list[i]._kumite != ''):
            _kumite.append(list[i])

    if kata == True:
        return _kata
    else:
        return _kumite

def sortBirth(list, ageFrom, ageTo):
    _age = []
    for i in range(len(list)):
        if ( list[i]._age >= int(ageFrom) and list[i]._age <= int(ageTo) ):
            _age.append(list[i])
    return _age

def sortWeight(list, weightFrom, weightTo):
    _weight = []
    for i in range(len(list)):
        if ( list[i]._weight >= int(weightFrom) and list[i]._weight <= int(weightTo)  ):
            _weight.append(list[i])
    return _weight


def selectChilds(listIn, kata, sex, ageFrom, ageTo, weightFrom, weightTo, category, exp):
    _output = sortBirth(listIn, ageFrom, ageTo)

    #if (kata == False): #tu mamy kumite dlatego dodajemy wage
        #_output = sortSex(listIn, sex)
        #_output = sortWeight(_output, weightFrom, weightTo)


    if (exp == True):
        _output = sortKata(_output, kata)
        _output = sortSex(_output, sex)
        if (kata == False): #tu mamy kumite dlatego dodajemy wage
            _output = sortWeight(_output, weightFrom, weightTo)
    elif(exp == False):
        _output = sortExp(_output, exp)


    return _output

def selectTeams(listIn, sex, exp, kata, ageFrom, ageTo):
    _output = sortSex(listIn, sex)
    _output = sortExp(_output, exp)
    _output = sortKata(_output, kata)

    return _output

def selectFree(listIn, sex, weightFrom, weightTo):
    _output = sortSex(listIn, sex)
    _output = sortWeight(_output, weightFrom, weightTo)

    return _output

def selector(schoolList, options, case):
    _selectedList = []
    print options
    print case
    if case == 0:
        for i in range(len(schoolList)):
            _selectedList.append( selectChilds(schoolList[i]._childList, options[0], options[1], options[2], options[3], options[4], options[5], options[6], options[7]))
    elif case == 1:
        for i in range(len(schoolList)):
            _selectedList.append( selectTeams(schoolList[i]._teamList, options[0], options[1], options[2], options[3], options[4]))
    elif case == 2:
        for i in range(len(schoolList)):
            _selectedList.append( selectFree(schoolList[i]._childList, options[0], options[1], options[2]))

    print _selectedList
    return _selectedList
