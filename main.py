import MainFrame
import wx

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame.MainFrame()
    app.MainLoop()