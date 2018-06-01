import wx

class SettingFrame(wx.Frame):
    init = 0
    instance=None
    def __new__(self, *args, **kwargs):
        """"""
        if self.instance is None:
            self.instance = wx.Frame.__new__(self)
        elif not self.instance:
            self.instance = wx.Frame.__new__(self)

        return self.instance
    def __init__(self):
        print("创建开始")
        if self.init:
            return
        print("创建窗口")
        self.init = 1
        wx.Frame.__init__(self, None, title="EMS地址设置")
        panel = SettingPanel(self)
        self.Show()
        print("窗口显示")
class SettingPanel(wx.Panel):
    """"""
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)