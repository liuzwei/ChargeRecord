import wx
from wx.lib.pubsub import pub


class LoginDialog(wx.Dialog):
    """
    Class to define login dialog
    """

    def __init__(self):
        """Constructor"""
        no_close = (wx.SYSTEM_MENU | wx.CAPTION | wx.CLIP_CHILDREN)
        wx.Dialog.__init__(self, None, title="Login",  style=no_close)
        vboxMain = wx.BoxSizer(wx.VERTICAL)
        # 用户名
        vboxUsername = wx.BoxSizer(wx.HORIZONTAL)
        username = wx.StaticText(self, label='账 号:')
        vboxUsername.Add(username, 0, wx.LEFT | wx.RIGHT, 5)
        self.usernameContent = wx.TextCtrl(self, style=wx.ST_NO_AUTORESIZE)
        vboxUsername.Add(self.usernameContent, 0, wx.LEFT, 5)

        # 密码
        vboxPasswd = wx.BoxSizer(wx.HORIZONTAL)

        passwd = wx.StaticText(self, label='密 码:')
        vboxPasswd.Add(passwd, 0, wx.LEFT | wx.RIGHT, 5)
        self.passwdContent = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.ST_NO_AUTORESIZE)
        vboxPasswd.Add(self.passwdContent, 0, wx.LEFT, 5)

        vboxMain.Add(vboxUsername, 0, wx.CENTER | wx.TOP, 50)
        vboxMain.Add(vboxPasswd, 0, wx.CENTER | wx.TOP, 20)

        # 登录按钮
        vboxLogin = wx.BoxSizer(wx.VERTICAL)
        loginBtn = wx.Button(self, -1, "登录")
        logoutBtn = wx.Button(self, -1, "退出")
        loginBtn.Bind(wx.EVT_BUTTON, self.onLogin)
        logoutBtn.Bind(wx.EVT_BUTTON, self.onLogout)
        vboxLogin.Add(loginBtn, 0, wx.LEFT, 180)
        vboxLogin.Add(logoutBtn, 0, wx.LEFT, 180)

        vboxMain.Add(vboxLogin, 0, wx.TOP, 30)

        self.SetSizer(vboxMain)

    def onLogin(self, event):
        """
        Check credentials and login
        """
        stupid_password = "123456"
        user_password = self.passwdContent.GetValue()
        if user_password == stupid_password:
            print("You are now logged in!")
            pub.sendMessage("frameListener", message="show")
            self.Destroy()
        else:
            print("Username or password is incorrect!")
    def onLogout(self, event):
        pub.sendMessage("frameListener", message="logout")
        self.Destroy()