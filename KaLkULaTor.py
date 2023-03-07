import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(450, 450))

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(22)
        panel = wx.Panel(self)
        panel.SetFont(font)
        vbox = wx.BoxSizer(wx.VERTICAL)

        tc = wx.TextCtrl(panel)
        vbox.Add(tc, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP , border=25)

        gbox = wx.GridSizer(3, 3, 3)
        gbox.AddMany([(wx.Button(panel, label='1'), 1, wx.EXPAND),
                      (wx.Button(panel, label='2'), 2, wx.EXPAND),
                      (wx.Button(panel, label='3'), 3, wx.EXPAND),
                      (wx.Button(panel, label='4'), 4, wx.EXPAND),
                      (wx.Button(panel, label='5'), 5, wx.EXPAND),
                      (wx.Button(panel, label='6'), 6, wx.EXPAND),
                      (wx.Button(panel, label='7'), 7, wx.EXPAND),
                      (wx.Button(panel, label='8'), 8, wx.EXPAND),
                      (wx.Button(panel, label='9'), 9, wx.EXPAND)])
        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=40)
        panel.SetSizer(vbox)


app = wx.App()
frame = MyFrame(None, 'wxPyhthon')
frame.Show()
app.MainLoop()
