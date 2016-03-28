import main_window
import wx

if __name__=='__main__':
    app=wx.App()
    frame=main_window.program_window(parent=None,id=-1,x=300,y=510)
    frame.Show()
    app.MainLoop()