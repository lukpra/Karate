import wx

class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.categoryList = ['Kata','Kumite']
        self.sexList = ['M','K']
        self.expList = ['Doswiadczony','Poczatkujacy']
        self.rbSex = wx.RadioBox(self, label="Plec", choices=self.sexList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rbSex)
        self.rbCategory = wx.RadioBox(self, label = "Kategoria", choices = self.categoryList, majorDimension = 2,
                          style=wx.RA_SPECIFY_COLS)
        self.rbExp = wx.RadioBox(self, label = "Doswiadczenie", choices = self.expList, majorDimension = 2,
                                 style = wx.RA_SPECIFY_ROWS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rbExp)
        self.inputTxtAgeFrom = wx.TextCtrl(self, wx.ID_ANY,'')
        self.inputTxtAgeTo = wx.TextCtrl(self, wx.ID_ANY, '')
        self.inputTxtWeightFrom = wx.TextCtrl(self, wx.ID_ANY, '')
        self.inputTxtWeightTo = wx.TextCtrl(self, wx.ID_ANY, '')
        #self.inputTxtCategory = wx.TextCtrl(self, wx.ID_ANY, '')

        #self.btnGen = wx.Button(self, wx.ID_ANY, 'OK')
        #self.Bind(wx.EVT_BUTTON, self.getData, self.btnGen)

        self.topSizer = wx.BoxSizer(wx.VERTICAL)
        self.rowSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        #self.labelKata = wx.StaticText(self, wx.ID_ANY, 'Kata:')
        #self.labelSex = wx.StaticText(self, wx.ID_ANY, 'Plec:')
        self.labelAge = wx.StaticText(self, wx.ID_ANY, 'Wiek:')
        self.labelWeight = wx.StaticText(self, wx.ID_ANY, 'Waga:')
        #self.labelCategory = wx.StaticText(self, wx.ID_ANY, 'Kategoria:')
        self.rowSizer6.Add(self.rbExp, 0, wx.ALL, 5)
        #self.rowSizer1.Add(self.labelKata, 0, wx.ALL,5)
        self.rowSizer1.Add(self.rbCategory, 0, wx.ALL,5)
        #self.rowSizer2.Add(self.labelSex, 0, wx.ALL, 5)
        self.rowSizer2.Add(self.rbSex,0, wx.ALL, 5)
        self.rowSizer3.Add(self.labelAge, 0, wx.ALL, 5)
        self.rowSizer3.Add(self.inputTxtAgeFrom, 0, wx.ALL, 5)
        self.rowSizer3.Add(self.inputTxtAgeTo, 0, wx.ALL, 5)
        self.rowSizer4.Add(self.labelWeight, 0, wx.ALL, 5)
        self.rowSizer4.Add(self.inputTxtWeightFrom, 0, wx.ALL, 5)
        self.rowSizer4.Add(self.inputTxtWeightTo, 0, wx.ALL, 5)
        #self.rowSizer5.Add(self.labelCategory, 0, wx.ALL, 5)
        #self.rowSizer5.Add(self.inputTxtCategory, 0, wx.ALL, 5)

        self.topSizer.Add(self.rowSizer1,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer2,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer3,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer4,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer5,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer6,0, wx.LEFT)
        #self.topSizer.Add(self.btnGen,0,wx.CENTER)

        self.SetSizer(self.topSizer)

    def EvtRadioBox(self, event):
        #self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
        return

    def getData(self,a):
        lista = []
        if self.rbCategory.GetStringSelection() == 'Kata':
            lista.append(True)
        else:
            lista.append(False)

        if self.rbSex.GetStringSelection() == 'M':
            lista.append(True)
        else:
            lista.append(False)
        lista_pom = []

        lista_pom.append(self.inputTxtAgeFrom)
        lista_pom.append(self.inputTxtAgeTo)
        lista_pom.append(self.inputTxtWeightFrom)
        lista_pom.append(self.inputTxtWeightTo)
        #lista_pom.append(self.inputTxtCategory)

        for index in range (len(lista_pom)):
            temp_value = self.validateData(lista_pom[index])
            if temp_value != "Err":
                lista.append(temp_value)
            else:
                print "Error! Data in fields incorrect!"
                self.showMessage("Pola nie moga byc puste! Oraz musza zawierac tylko cyfry!")
                return "Err"
        lista.append("1") # zamiast braku kategorii
        if self.rbExp.GetStringSelection() == 'Doswiadczony': # 3 param
            lista.append(True)
        else:
            lista.append(False)
        print lista
        return lista

    def validateData(self,ctrl):
        if len(ctrl.GetValue())>0 and ctrl.GetValue().isdigit():
            return ctrl.GetValue()
        else:
            return "Err"

    def showMessage(self,text):
        wx.MessageBox(text, "Komunikat",
        wx.OK | wx.ICON_INFORMATION)

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # self.categoryList = ['Kata','Kumite']
        self.sexList = ['M','K']
        self.expList = ['Doswiadczony','Poczatkujacy']
        self.categoryList = ['Kata','Kumite']
        self.rbSex = wx.RadioBox(self, label="Plec", choices=self.sexList,  majorDimension=3,
                        style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rbSex)
        self.rbExp = wx.RadioBox(self, label = "Doswiadczenie", choices = self.expList, majorDimension = 2,
                        style = wx.RA_SPECIFY_ROWS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rbExp)
        self.rbCategory = wx.RadioBox(self, label = "Kategoria", choices = self.categoryList, majorDimension = 2,
                            style=wx.RA_SPECIFY_COLS)

        # self.rbCategory = wx.RadioBox(self, label = "Kategoria", choices = self.categoryList, majorDimension = 2,
        #                   style=wx.RA_SPECIFY_COLS)
        #
        # self.inputTxtAgeFrom = wx.TextCtrl(self, wx.ID_ANY,'')
        # self.inputTxtAgeTo = wx.TextCtrl(self, wx.ID_ANY, '')
        # self.inputTxtWeightFrom = wx.TextCtrl(self, wx.ID_ANY, '')
        # self.inputTxtWeightTo = wx.TextCtrl(self, wx.ID_ANY, '')
        # self.inputTxtCategory = wx.TextCtrl(self, wx.ID_ANY, '')
        #
        #self.btnGen = wx.Button(self, wx.ID_ANY, 'OK')
        #self.Bind(wx.EVT_BUTTON, self.getData, self.btnGen)
        #
        self.topSizer = wx.BoxSizer(wx.VERTICAL)
        # self.rowSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        # self.rowSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        # self.rowSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        #
        # #self.labelKata = wx.StaticText(self, wx.ID_ANY, 'Kata:')
        # #self.labelSex = wx.StaticText(self, wx.ID_ANY, 'Plec:')
        # self.labelAge = wx.StaticText(self, wx.ID_ANY, 'Wiek:')
        # self.labelWeight = wx.StaticText(self, wx.ID_ANY, 'Waga:')
        # self.labelCategory = wx.StaticText(self, wx.ID_ANY, 'Kategoria:')
        #
        # #self.rowSizer1.Add(self.labelKata, 0, wx.ALL,5)
        # self.rowSizer1.Add(self.rbCategory, 0, wx.ALL,5)
        # #self.rowSizer2.Add(self.labelSex, 0, wx.ALL, 5)
        self.rowSizer2.Add(self.rbSex,0, wx.ALL, 5)
        # self.rowSizer3.Add(self.labelAge, 0, wx.ALL, 5)
        # self.rowSizer3.Add(self.inputTxtAgeFrom, 0, wx.ALL, 5)
        # self.rowSizer3.Add(self.inputTxtAgeTo, 0, wx.ALL, 5)
        # self.rowSizer4.Add(self.labelWeight, 0, wx.ALL, 5)
        # self.rowSizer4.Add(self.inputTxtWeightFrom, 0, wx.ALL, 5)
        # self.rowSizer4.Add(self.inputTxtWeightTo, 0, wx.ALL, 5)
        # self.rowSizer5.Add(self.labelCategory, 0, wx.ALL, 5)
        # self.rowSizer5.Add(self.inputTxtCategory, 0, wx.ALL, 5)
        #
        # self.topSizer.Add(self.rowSizer1,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer2,0, wx.LEFT)
        # self.topSizer.Add(self.rowSizer3,0, wx.LEFT)
        # self.topSizer.Add(self.rowSizer4,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer5,0, wx.LEFT)
        self.topSizer.Add(self.rbExp, 0, wx.LEFT)
        self.topSizer.Add(self.rbCategory, 0, wx.LEFT)
        #self.topSizer.Add(self.btnGen,0,wx.CENTER)

        self.SetSizer(self.topSizer)

    def EvtRadioBox(self, event):
        #self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
        return

    def getData(self,a):
        lista = []
        if self.rbSex.GetStringSelection() == 'M':
            lista.append(True)
        else:
            lista.append(False)
        if self.rbExp.GetStringSelection() == 'Doswiadczony':
            lista.append(True)
        else:
            lista.append(False)
        if self.rbCategory.GetStringSelection() == 'Kata':
            lista.append(True)
        else:
            lista.append(False)
        print lista
        return lista

class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #self.categoryList = ['Kata','Kumite']
        self.sexList = ['M','K']
        #self.expList = ['Senior','Poczatkujacy']
        self.rbSex = wx.RadioBox(self, label="Plec", choices=self.sexList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rbSex)
        #self.rbCategory = wx.RadioBox(self, label = "Kategoria", choices = self.categoryList, majorDimension = 2,
        #                  style=wx.RA_SPECIFY_COLS)
        #self.rbExp = wx.RadioBox(self, label = "Doswiadczenie", choices = self.expList, majorDimension = 2,
        #                         style = wx.RA_SPECIFY_ROWS)
        #self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, self.rbExp)
        #self.inputTxtAgeFrom = wx.TextCtrl(self, wx.ID_ANY,'')
        #self.inputTxtAgeTo = wx.TextCtrl(self, wx.ID_ANY, '')
        self.inputTxtWeightFrom = wx.TextCtrl(self, wx.ID_ANY, '')
        self.inputTxtWeightTo = wx.TextCtrl(self, wx.ID_ANY, '')
        #self.inputTxtCategory = wx.TextCtrl(self, wx.ID_ANY, '')

        #self.btnGen = wx.Button(self, wx.ID_ANY, 'OK')
        #self.Bind(wx.EVT_BUTTON, self.getData, self.btnGen)

        self.topSizer = wx.BoxSizer(wx.VERTICAL)
        self.rowSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.rowSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        #self.labelKata = wx.StaticText(self, wx.ID_ANY, 'Kata:')
        #self.labelSex = wx.StaticText(self, wx.ID_ANY, 'Plec:')
        #self.labelAge = wx.StaticText(self, wx.ID_ANY, 'Wiek:')
        self.labelWeight = wx.StaticText(self, wx.ID_ANY, 'Waga:')
        #self.labelCategory = wx.StaticText(self, wx.ID_ANY, 'Kategoria:')
        #self.rowSizer6.Add(self.rbExp, 0, wx.ALL, 5)
        #self.rowSizer1.Add(self.labelKata, 0, wx.ALL,5)
        #self.rowSizer1.Add(self.rbCategory, 0, wx.ALL,5)
        #self.rowSizer2.Add(self.labelSex, 0, wx.ALL, 5)
        self.rowSizer2.Add(self.rbSex,0, wx.ALL, 5)
        #self.rowSizer3.Add(self.labelAge, 0, wx.ALL, 5)
        #self.rowSizer3.Add(self.inputTxtAgeFrom, 0, wx.ALL, 5)
        #self.rowSizer3.Add(self.inputTxtAgeTo, 0, wx.ALL, 5)
        self.rowSizer4.Add(self.labelWeight, 0, wx.ALL, 5)
        self.rowSizer4.Add(self.inputTxtWeightFrom, 0, wx.ALL, 5)
        self.rowSizer4.Add(self.inputTxtWeightTo, 0, wx.ALL, 5)
        #self.rowSizer5.Add(self.labelCategory, 0, wx.ALL, 5)
        #self.rowSizer5.Add(self.inputTxtCategory, 0, wx.ALL, 5)

        self.topSizer.Add(self.rowSizer1,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer2,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer3,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer4,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer5,0, wx.LEFT)
        self.topSizer.Add(self.rowSizer6,0, wx.LEFT)
        #self.topSizer.Add(self.btnGen,0,wx.CENTER)

        self.SetSizer(self.topSizer)

    def EvtRadioBox(self, event):
        #self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
        return

    def getData(self,a):
        lista = []
        if self.rbSex.GetStringSelection() == 'M':
            lista.append(True)
        else:
            lista.append(False)
        lista_pom = []

        lista_pom.append(self.inputTxtWeightFrom)
        lista_pom.append(self.inputTxtWeightTo)

        for index in range (len(lista_pom)):
            temp_value = self.validateData(lista_pom[index])
            if temp_value != "Err":
                lista.append(temp_value)
            else:
                print "Error! Data in fields incorrect!"
                self.showMessage("Pola nie moga byc puste! Oraz musza zawierac tylko cyfry!")
                return "Err"
        print lista
        return lista

    def validateData(self,ctrl):
        if len(ctrl.GetValue())>0 and ctrl.GetValue().isdigit():
            return ctrl.GetValue()
        else:
            return "Err"

    def showMessage(self,text):
        wx.MessageBox(text, "Komunikat",
        wx.OK | wx.ICON_INFORMATION)