import wx


class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(900, 450))

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(16)


        panel = wx.Panel(self)
        panel.SetFont(font)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='Путь к файлу:')
        tc = wx.TextCtrl(panel)

        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        hbox1.Add(tc, proportion=1)

        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        st2 = wx.StaticText(panel, label='Содержимое файла')
        vbox.Add(st2, flag=wx.EXPAND | wx.ALL, border=10)


        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        vbox.Add(tc2, proportion=2, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=20)


        btnOk = wx.Button(panel, label='Да', size=(100, 40))
        btnCn = wx.Button(panel, label='Отмена', size=(100, 40))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(btnOk, flag=wx.LEFT, border=20)
        hbox2.Add(btnCn, flag=wx.LEFT, border=20)

        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, border=10)
        panel.SetSizer(vbox)





app = wx.App()
frame = MyFrame(None, 'wxPyhthon')
frame.Show()
app.MainLoop()