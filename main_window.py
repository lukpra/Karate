import wx
import path_walker as pw
import notebooks as nbs
import sheet_parser as sp
import sorting as sorting

class program_window(wx.Frame):
    def __init__(self,parent,id,x,y):
        self.x_rez = x
        self.y_rez = y
        wx.Frame.__init__(self,parent,id,'Program do tabelek w turnieju', size=(self.x_rez,self.y_rez))
        self.Bind(wx.EVT_CLOSE, self.closeWindow) ### window cross
        self.panel = wx.Panel(self)
        self.nb = wx.Notebook(self.panel)

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.nbCurrPage, self.nb)

        self.page1 = nbs.PageOne(self.nb)
        self.page2 = nbs.PageTwo(self.nb)
        self.page3 = nbs.PageThree(self.nb)

        self.kryteria = []
        self.file_path = ''
        self.currentNbPage = 0

        self.nb.AddPage(self.page1, "Indywidualna")
        self.nb.AddPage(self.page2, "Druzynowa")
        self.nb.AddPage(self.page3, "Wolna")

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.nb, 1, wx.EXPAND)
        #self.sizer.AddStretchSpacer(prop=1)

        self.topSizer = wx.BoxSizer(wx.VERTICAL) # global container
        self.horizontalSizer = wx.BoxSizer(wx.HORIZONTAL) # horizontal container
        self.titleSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.titleSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.leftSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.rightSizer = wx.BoxSizer(wx.VERTICAL)
        self.rightRow1 = wx.BoxSizer(wx.HORIZONTAL)
        self.rightRow2 = wx.BoxSizer(wx.HORIZONTAL)
        # top info
        self.labelLabelFilePath = wx.StaticText(self.panel, wx.ID_ANY, 'Sciezka do katalogu z plikami: ')
        self.labelFilePath = wx.StaticText(self.panel, wx.ID_ANY, "Nie wybrano folderu!")
        self.labelLabelFileNum = wx.StaticText(self.panel, wx.ID_ANY,'Liczba plikow arkusza w katalogu: ')
        self.labelFileNum = wx.StaticText(self.panel, wx.ID_ANY, '0')
        # right panel
        #self.labelRightPanelLabel = wx.StaticText(self.panel, wx.ID_ANY, 'Zakresy:')
        #self.labelRightPanelAge = wx.StaticText( self.panel, wx.ID_ANY, "Wiek od: ")
        #self.labelRightPanelAge2 = wx.StaticText( self.panel, wx.ID_ANY, " do ")
        #self.labelRightPanelAgeFrom = wx.StaticText( self.panel, wx.ID_ANY, " ? ")
        #self.labelRightPanelAgeTo = wx.StaticText( self.panel, wx.ID_ANY, " ? ")

        #self.labelRightPanelWeight = wx.StaticText ( self.panel, wx.ID_ANY, "Waga od: ")
        #self.labelRightPanelWeight2 = wx.StaticText ( self.panel, wx.ID_ANY, " do ")
        #self.labelRightPanelWeightFrom = wx.StaticText( self.panel, wx.ID_ANY, " ? ")
        #self.labelRightPanelWeightTo = wx.StaticText( self.panel, wx.ID_ANY, " ? ")

        self.btnGen = wx.Button(self.panel, wx.ID_ANY, 'Generuj')
        self.Bind(wx.EVT_BUTTON, self.getData, self.btnGen)

        self.titleSizer1.Add(self.labelLabelFilePath, 0, wx.ALL, 5)
        self.titleSizer1.Add(self.labelFilePath, 0, wx.ALL, 5)
        self.titleSizer2.Add(self.labelLabelFileNum, 0, wx.ALL, 5)
        self.titleSizer2.Add(self.labelFileNum, 0, wx.ALL, 5)
        '''
        self.rightRow1.Add(self.labelRightPanelAge, 0, wx.ALL, 5)
        self.rightRow1.Add(self.labelRightPanelAgeFrom, 0, wx.ALL, 5)
        self.rightRow1.Add(self.labelRightPanelAge2, 0, wx.ALL, 5)
        self.rightRow1.Add(self.labelRightPanelAgeTo, 0, wx.ALL, 5)
        self.rightRow2.Add(self.labelRightPanelWeight, 0, wx.ALL, 5)
        self.rightRow2.Add(self.labelRightPanelWeightFrom, 0, wx.ALL, 5)
        self.rightRow2.Add(self.labelRightPanelWeight2, 0, wx.ALL, 5)
        self.rightRow2.Add(self.labelRightPanelWeightTo, 0, wx.ALL, 5)
        '''
        #self.rightSizer.Add(self.labelRightPanelLabel, 0, wx.CENTER)
        #self.rightSizer.Add(self.rightRow1, 0, wx.LEFT)
        #self.rightSizer.Add(self.rightRow2, 0, wx.LEFT)
        #elf.rightSizer.Add(self.btnGen, 0, wx.LEFT)


        #self.horizontalSizer.Add(self.sizer,0, wx.ALL, 0)
        #self.horizontalSizer.Add(self.rightSizer,0,wx.ALL,0)

        self.topSizer.Add(self.titleSizer1, 0 , wx.LEFT)
        self.topSizer.Add(self.titleSizer2, 0, wx.LEFT)
        self.topSizer.Add(wx.StaticLine(self.panel), 0 , wx.ALL|wx.EXPAND, 5)
        #self.topSizer.Add(self.horizontalSizer, 0 , wx.ALL|wx.EXPAND, 5)
        self.topSizer.Add(self.sizer, 0, wx.LEFT)
        self.topSizer.Add(self.btnGen, 0, wx.CENTER, 1)
        self.panel.SetSizer(self.topSizer)


        self.menubar = wx.MenuBar()
        self.menuFirst = wx.Menu()
        self.menuSecond = wx.Menu()
        self.menuThird = wx.Menu()
        self.genMenuBar(self)
        #self.genFirstRowWidgets(self)



        #slider = wx.Slider(self.panel, -1, 1, 1, 2, pos = (300,300), size = (90, 50), style = wx.SL_AUTOTICKS | wx.SL_LABELS)
        #slider.SetTickFreq(1,1)

        #spinner = wx.SpinCtrl(self.panel, -1, "", pos = (150 , 250), size = (90, -1))
        #spinner.SetRange(1,100)
        #spinner.SetValue(10)

        #wx.CheckBox(self.panel, -1, "Apples", (20,20), (160, -1))
        #wx.CheckBox(self.panel, -1, "Tuna", (20,40), (160, -1))
        #wx.CheckBox(self.panel, -1, "Dere", (20,60), (160, -1))

        #mylist = ['beef', 'tuna', 'coconuts', 'more beef', 'cereal']
        #count = wx.ListBox(self.panel, -1, (20,500), (80,60), mylist, wx.LB_SINGLE)
        #count.SetSelection(3)

    def nbCurrPage(self, e):
        self.currentNbPage = self.nb.GetSelection()
        print self.currentNbPage

    def getData(self,e):
        if int(self.currentNbPage) == 0:
            self.kryteria = self.page1.getData(1)
            print " Pobieram z strony 1"
        elif int(self.currentNbPage) == 1:
            self.kryteria = self.page2.getData(1)
            print " Pobieram z strony 2"
        elif int(self.currentNbPage) == 2:
            self.kryteria = self.page3.getData(1)
            print " Pobieram z strony 3"
        if self.kryteria != 'Err':
            if len(self.file_path) <= 0:
                self.showMessage("Nie wybrano katalogu z plikami!")
            else:
                pw.genAll(self.kryteria, self.file_path, self.currentNbPage)

    def showMessage(self,text):
        wx.MessageBox(text, "Komunikat",
            wx.OK | wx.ICON_INFORMATION)

    def popAlertWidget(self,question,title,defVal):
        box = wx.TextEntryDialog(None, question, title, defVal)
        if box.ShowModal()==wx.ID_OK:
            answer=box.GetValue()
            box.Destroy()
            return answer
        else:
            return ''

    def genFirstRowWidgets(self, event):
        #btnExit=wx.Button(self.panel,label = "Exit",pos=(1,1), size=(40 , 20))
        #self.Bind(wx.EVT_BUTTON,self.closeButton, btnExit)
        self.genLabel("Sciezka do katalogu z plikami: ",10,10)
        self.genLabel("Liczba plikow w katalogu: ", 10, 30)

        pic = wx.Image("logo.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.button = wx.BitmapButton(self.panel, -1, pic, pos = (500,10))
        self.Bind (wx.EVT_BUTTON, self.onDir, self.button)
        self.button.SetDefault()
        return

    def genLabel(self,text,x,y):
        return wx.StaticText(self.panel,-1,text,(x,y))

    def genMenuBar(self, event):
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        #first.Append(wx.NewId(),"Wczytaj z katalogu ...")
        #first.Append(wx.ID_EXIT,"Wyjscie","Open a new file")
        firstDirSelect = first.Append(wx.NewId(),"Wczytaj z katalogu ...", "Wybierz katalog")
        firstExit = first.Append(wx.ID_EXIT,"Wyjscie","Wyjdz z programu")
        menubar.Append(first,"Plik")
        #menubar.Append(second,"To DO")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onDir, firstDirSelect)
        self.Bind(wx.EVT_MENU, self.onQuit, firstExit)

    def onDir(self, event):
        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            print "You chose %s" % dlg.GetPath()
            self.labelFilePath.SetLabel(dlg.GetPath())
            number = int(pw.xlsxNumber(dlg.GetPath()))
            if number > 0:
                self.labelFileNum.SetLabel(str(number))
                self.file_path = dlg.GetPath()
            else:
                self.labelFileNum.SetLabel("0")
                self.showMessage("Brak plikow *.xlsx we wskazanym folderze!")
        dlg.Destroy()

    def onOpen(self,event):
        """Open a file"""
        openFileDialog = wx.FileDialog(self,"Open log file","","","Pliki Arkusza (*.txt)|*.txt",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST |wx.FD_CHANGE_DIR)

        openFileDialog.SetDirectory("C:/")

        print openFileDialog.GetDirectory()
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return

    def setDir (self, event):
        openFileDialog = wx.FileDialog(self,"Wybierz katalog z zgloszeniami","","","",wx.FD_CHANGE_DIR)

        openFileDialog.SetDirectory("C:/")

        print openFileDialog.GetDirectory()
        return

    def closeButton(self,event):
        self.Close(True)

    def closeWindow(self,event):
        self.Destroy()

    def onQuit(self,event):
        self.Close()

if __name__=='__main__':
    app=wx.App()
    frame=main_window.program_window(parent=None,id=-1,x=300,y=510)
    frame.Show()
    app.MainLoop()