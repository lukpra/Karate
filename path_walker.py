from os import listdir
import sheet_parser as pars
import sorting as sorti
import random_players as rp

def printListFiles(dir):
    print(listdir(dir))

def fileNumber(dir):
    return len(listdir(dir))

def xlsxNumber(dir):
    flist = listdir(dir)
    iter = 0
    for index in range(len(flist)):
        if (flist[index][-4:] == "xlsx" or flist[index][-3:] == "xls") and flist[index][0] != "~":
            iter += 1
    return iter

def listFormat(dir):
    flist = listdir(dir)
    parsed = []
    for index in range(len(flist)):
        if (flist[index][-4:] == "xlsx" or flist[index][-3:] == "xls") and flist[index][0] != "~":
            parsed.append(flist[index])
    return { 'list': parsed, 'number': len(parsed), 'dir': dir }

# funkcja zwraca liste objekowt School dla kazdego arkusza
def parsePath(tuple):
    _number = tuple['number']
    _list = tuple['list']
    _dir = tuple['dir']
    _outputList = []

    print _number
    print _dir
    print _list

    for i in range(_number):
        sh = pars.prepareSheet(_dir, _list[i])
        shObj = pars.parseSheet(sh)
        _outputList.append(shObj)

    return _outputList

def genAll(options, path, case):
    _tuple = listFormat(path)
    _myList = parsePath(_tuple)
    _sorted = sorti.selector(_myList, options, case)

    rp.printToFile(rp.tournamentTree(_sorted), options, case)

