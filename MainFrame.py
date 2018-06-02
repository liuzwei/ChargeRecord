import wx
from wx.lib.pubsub import pub

import LoginDialog
import SettingFrame


class MainFrame(wx.Frame):
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Main App", size=(1080, 560))

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"EMS地址", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem1)

        self.m_menubar1.Append(self.m_menu1, u"设置")

        # Connect Events
        self.Bind(wx.EVT_MENU, self.openSettingFrame, id=self.m_menuItem1.GetId())

        self.m_menu3 = wx.Menu()
        self.m_menuItem2 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"绿洲", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_menuItem2)

        self.m_menubar1.Append(self.m_menu3, u"帮助")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

        panel = MainPanel(self)
        pub.subscribe(self.myListener, "frameListener")

        # Ask user to login
        dlg = LoginDialog.LoginDialog()
        dlg.ShowModal()
    def openSettingFrame(self, event):
        print("事件触发")
        settingFrame = SettingFrame.SettingFrame()

    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        if "show"==message:
            self.Show()
        else:
            self.Destroy()

class MainPanel(wx.Panel):
    """"""
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(1080, 560),
                          style=wx.TAB_TRAVERSAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"主板编号:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(12, 70, 90, 90, False, wx.EmptyString))

        bSizer4.Add(self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 50)

        self.m_textCtrl1 = wx.TextCtrl(self, 10000, wx.EmptyString, wx.DefaultPosition, wx.Size(220, -1), style=wx.TE_PROCESS_ENTER)
        bSizer4.Add(self.m_textCtrl1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 20)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"序号", wx.DefaultPosition, wx.Size(30, -1), wx.ALIGN_CENTRE)
        self.m_staticText3.Wrap(-1)
        bSizer5.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"从版编号", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText4.Wrap(-1)
        bSizer5.Add(self.m_staticText4, 1, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"电池生产编号", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText5.Wrap(-1)
        bSizer5.Add(self.m_staticText5, 1, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"电池编号备注", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText6.Wrap(-1)
        bSizer5.Add(self.m_staticText6, 1, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"系统电池组编号", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText7.Wrap(-1)
        bSizer5.Add(self.m_staticText7, 1, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"电池状态", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText8.Wrap(-1)
        bSizer5.Add(self.m_staticText8, 1, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"告警详情", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText9.Wrap(-1)
        bSizer5.Add(self.m_staticText9, 1, wx.ALL, 5)

        bSizer1.Add(bSizer5, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        self.m_staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline3, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(30, -1), wx.ALIGN_CENTRE)
        self.m_staticText14.Wrap(-1)
        bSizer8.Add(self.m_staticText14, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, 10010, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,style=wx.TE_PROCESS_ENTER)
        bSizer8.Add(self.m_textCtrl4, 1, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, 10011, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_textCtrl5, 1, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, 10012, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_textCtrl6, 1, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, 10013, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_textCtrl7, 1, wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, 10014, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_textCtrl8, 1, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, 10015, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_textCtrl9, 1, wx.ALL, 5)

        bSizer1.Add(bSizer8, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText141 = wx.StaticText(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText141.Wrap(-1)
        bSizer81.Add(self.m_staticText141, 0, wx.ALL, 5)

        self.m_textCtrl41 = wx.TextCtrl(self, 10020, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer81.Add(self.m_textCtrl41, 1, wx.ALL, 5)

        self.m_textCtrl51 = wx.TextCtrl(self, 10021, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_textCtrl51, 1, wx.ALL, 5)

        self.m_textCtrl61 = wx.TextCtrl(self, 10022, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_textCtrl61, 1, wx.ALL, 5)

        self.m_textCtrl71 = wx.TextCtrl(self, 10023, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_textCtrl71, 1, wx.ALL, 5)

        self.m_textCtrl81 = wx.TextCtrl(self, 10024, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_textCtrl81, 1, wx.ALL, 5)

        self.m_textCtrl91 = wx.TextCtrl(self, 10025, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer81.Add(self.m_textCtrl91, 1, wx.ALL, 5)

        bSizer1.Add(bSizer81, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer82 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText142 = wx.StaticText(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText142.Wrap(-1)
        bSizer82.Add(self.m_staticText142, 0, wx.ALL, 5)

        self.m_textCtrl42 = wx.TextCtrl(self, 10030, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer82.Add(self.m_textCtrl42, 1, wx.ALL, 5)

        self.m_textCtrl52 = wx.TextCtrl(self, 10031, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_textCtrl52, 1, wx.ALL, 5)

        self.m_textCtrl62 = wx.TextCtrl(self, 10032, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_textCtrl62, 1, wx.ALL, 5)

        self.m_textCtrl72 = wx.TextCtrl(self, 10033, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_textCtrl72, 1, wx.ALL, 5)

        self.m_textCtrl82 = wx.TextCtrl(self, 10034, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_textCtrl82, 1, wx.ALL, 5)

        self.m_textCtrl92 = wx.TextCtrl(self, 10035, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer82.Add(self.m_textCtrl92, 1, wx.ALL, 5)

        bSizer1.Add(bSizer82, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer83 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText143 = wx.StaticText(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText143.Wrap(-1)
        bSizer83.Add(self.m_staticText143, 0, wx.ALL, 5)

        self.m_textCtrl43 = wx.TextCtrl(self, 10040, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer83.Add(self.m_textCtrl43, 1, wx.ALL, 5)

        self.m_textCtrl53 = wx.TextCtrl(self, 10041, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_textCtrl53, 1, wx.ALL, 5)

        self.m_textCtrl63 = wx.TextCtrl(self, 10042, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_textCtrl63, 1, wx.ALL, 5)

        self.m_textCtrl73 = wx.TextCtrl(self, 10043, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_textCtrl73, 1, wx.ALL, 5)

        self.m_textCtrl83 = wx.TextCtrl(self, 10044, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_textCtrl83, 1, wx.ALL, 5)

        self.m_textCtrl93 = wx.TextCtrl(self, 10045, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer83.Add(self.m_textCtrl93, 1, wx.ALL, 5)

        bSizer1.Add(bSizer83, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer84 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText144 = wx.StaticText(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText144.Wrap(-1)
        bSizer84.Add(self.m_staticText144, 0, wx.ALL, 5)

        self.m_textCtrl44 = wx.TextCtrl(self, 10050, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer84.Add(self.m_textCtrl44, 1, wx.ALL, 5)

        self.m_textCtrl54 = wx.TextCtrl(self, 10051, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer84.Add(self.m_textCtrl54, 1, wx.ALL, 5)

        self.m_textCtrl64 = wx.TextCtrl(self, 10052, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer84.Add(self.m_textCtrl64, 1, wx.ALL, 5)

        self.m_textCtrl74 = wx.TextCtrl(self, 10053, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer84.Add(self.m_textCtrl74, 1, wx.ALL, 5)

        self.m_textCtrl84 = wx.TextCtrl(self, 10054, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer84.Add(self.m_textCtrl84, 1, wx.ALL, 5)

        self.m_textCtrl94 = wx.TextCtrl(self, 10055, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer84.Add(self.m_textCtrl94, 1, wx.ALL, 5)

        bSizer1.Add(bSizer84, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer85 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText145 = wx.StaticText(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText145.Wrap(-1)
        bSizer85.Add(self.m_staticText145, 0, wx.ALL, 5)

        self.m_textCtrl45 = wx.TextCtrl(self, 10060, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer85.Add(self.m_textCtrl45, 1, wx.ALL, 5)

        self.m_textCtrl55 = wx.TextCtrl(self, 10061, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer85.Add(self.m_textCtrl55, 1, wx.ALL, 5)

        self.m_textCtrl65 = wx.TextCtrl(self, 10062, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer85.Add(self.m_textCtrl65, 1, wx.ALL, 5)

        self.m_textCtrl75 = wx.TextCtrl(self, 10063, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer85.Add(self.m_textCtrl75, 1, wx.ALL, 5)

        self.m_textCtrl85 = wx.TextCtrl(self, 10064, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer85.Add(self.m_textCtrl85, 1, wx.ALL, 5)

        self.m_textCtrl95 = wx.TextCtrl(self, 10065, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer85.Add(self.m_textCtrl95, 1, wx.ALL, 5)

        bSizer1.Add(bSizer85, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer86 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText146 = wx.StaticText(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText146.Wrap(-1)
        bSizer86.Add(self.m_staticText146, 0, wx.ALL, 5)

        self.m_textCtrl46 = wx.TextCtrl(self, 10070, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer86.Add(self.m_textCtrl46, 1, wx.ALL, 5)

        self.m_textCtrl56 = wx.TextCtrl(self, 10071, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_textCtrl56, 1, wx.ALL, 5)

        self.m_textCtrl66 = wx.TextCtrl(self, 10072, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_textCtrl66, 1, wx.ALL, 5)

        self.m_textCtrl76 = wx.TextCtrl(self, 10073, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_textCtrl76, 1, wx.ALL, 5)

        self.m_textCtrl86 = wx.TextCtrl(self, 10074, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_textCtrl86, 1, wx.ALL, 5)

        self.m_textCtrl96 = wx.TextCtrl(self, 10075, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer86.Add(self.m_textCtrl96, 1, wx.ALL, 5)

        bSizer1.Add(bSizer86, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer87 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText147 = wx.StaticText(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size(30, -1),
                                             wx.ALIGN_CENTRE)
        self.m_staticText147.Wrap(-1)
        bSizer87.Add(self.m_staticText147, 0, wx.ALL, 5)

        self.m_textCtrl47 = wx.TextCtrl(self, 10080, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PROCESS_ENTER)
        bSizer87.Add(self.m_textCtrl47, 1, wx.ALL, 5)

        self.m_textCtrl57 = wx.TextCtrl(self, 10081, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer87.Add(self.m_textCtrl57, 1, wx.ALL, 5)

        self.m_textCtrl67 = wx.TextCtrl(self, 10082, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer87.Add(self.m_textCtrl67, 1, wx.ALL, 5)

        self.m_textCtrl77 = wx.TextCtrl(self, 10083, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer87.Add(self.m_textCtrl77, 1, wx.ALL, 5)

        self.m_textCtrl87 = wx.TextCtrl(self, 10084, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer87.Add(self.m_textCtrl87, 1, wx.ALL, 5)

        self.m_textCtrl97 = wx.TextCtrl(self, 10085, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer87.Add(self.m_textCtrl97, 1, wx.ALL, 5)

        bSizer1.Add(bSizer87, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"提示：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        self.m_staticText10.SetFont(wx.Font(12, 70, 90, 92, False, wx.EmptyString))

        bSizer6.Add(self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 50)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1),
                                       wx.TE_MULTILINE)
        bSizer6.Add(self.m_textCtrl2, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)

        self.m_staticline4 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline4, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 20)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        bSizer7.Add(self.m_staticText11, 1, wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        bSizer7.Add(self.m_staticText12, 1, wx.ALL, 5)

        self.m_button23 = wx.Button(self, wx.ID_ANY, u"取消提交", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button23, 1, wx.ALL, 5)

        self.m_button24 = wx.Button(self, wx.ID_ANY, u"确认提交", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button24, 1, wx.ALL, 5)

        self.m_button25 = wx.Button(self, wx.ID_ANY, u"异常充电", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button25, 1, wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer7.Add(self.m_staticText13, 1, wx.ALL, 5)

        bSizer1.Add(bSizer7, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        #绑定事件
        self.m_textCtrl1.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl4.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl41.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl42.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl43.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl44.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl45.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl46.Bind(wx.EVT_CHAR, self.enter)
        self.m_textCtrl47.Bind(wx.EVT_CHAR, self.enter)
    def enter(self, event):
        eIds = [10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070]
        eId = event.Id
        if eId in eIds:
            textCtrl = self.FindWindowById(event.Id+10)
            textCtrl.SetFocus()
            print("回车事件")
