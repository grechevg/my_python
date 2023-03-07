import wx

def tach1(event):
    global fl
    if btn1.GetLabel() == '':
        if fl:
            btn1.SetLabel("X")
            fl = False
        else:
            btn1.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

def tach2(event):
    global fl
    if btn2.GetLabel() == '':
        if fl:
            btn2.SetLabel("X")
            fl = False
        else:
            btn2.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

def tach3(event):
    global fl
    if btn3.GetLabel() == '':
        if fl:
            btn3.SetLabel("X")
            fl = False
        else:
            btn3.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

def tach4(event):
    global fl
    if btn4.GetLabel() == '':
        if fl:
            btn4.SetLabel("X")
            fl = False
        else:
            btn4.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

def tach5(event):
    global fl
    if btn5.GetLabel() == '':
        if fl:
            btn5.SetLabel("X")
            fl = False
        else:
            btn5.SetLabel("O")
            fl = True
    print('сработала кнопка 5', fl, event)

def tach6(event):
    global fl
    if btn6.GetLabel() == '':
        if fl:
            btn6.SetLabel("X")
            fl = False
        else:
            btn6.SetLabel("O")
            fl = True
    print('сработала кнопка 6', fl, event)

def tach7(event):
    global fl
    if btn7.GetLabel() == '':
        if fl:
            btn7.SetLabel("X")
            fl = False
        else:
            btn7.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

def tach8(event):
    global fl
    if btn8.GetLabel() == '':
        if fl:
            btn8.SetLabel("X")
            fl = False
        else:
            btn8.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

def tach9(event):
    global fl
    if btn9.GetLabel() == '':
        if fl:
            btn9.SetLabel("X")
            fl = False
        else:
            btn9.SetLabel("O")
            fl = True
    print('сработала кнопка 1', fl, event)

app = wx.App()
fl = True
frame = wx.Frame(None, title='Крестики Нолики')

font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
font.SetPointSize(32)
frame.SetFont(font)
loc = wx.IconLocation('003.bmp')
frame.SetIcon(wx.Icon(loc))
btn1 = wx.Button(frame, 1, "", size=(80, 80), pos=(40, 40))
btn2 = wx.Button(frame, 2, "", size=(80, 80), pos=(140, 40))
btn3 = wx.Button(frame, 3, "", size=(80, 80), pos=(240, 40))

btn4 = wx.Button(frame, 4, "", size=(80, 80), pos=(40, 140))
btn5 = wx.Button(frame, 5, "", size=(80, 80), pos=(140, 140))
btn6 = wx.Button(frame, 6, "", size=(80, 80), pos=(240, 140))

btn7 = wx.Button(frame, 7, "", size=(80, 80), pos=(40, 240))
btn8 = wx.Button(frame, 8, "", size=(80, 80), pos=(140, 240))
btn9 = wx.Button(frame, 9, "", size=(80, 80), pos=(240, 240))

str_out = wx.StaticText(frame, label='Text: ',  pos=(40, 380))

frame.Bind(wx.EVT_BUTTON, tach1, btn1)
frame.Bind(wx.EVT_BUTTON, tach2, btn2)
frame.Bind(wx.EVT_BUTTON, tach3, btn3)
frame.Bind(wx.EVT_BUTTON, tach4, btn4)
frame.Bind(wx.EVT_BUTTON, tach5, btn5)
frame.Bind(wx.EVT_BUTTON, tach6, btn6)
frame.Bind(wx.EVT_BUTTON, tach7, btn7)
frame.Bind(wx.EVT_BUTTON, tach8, btn8)
frame.Bind(wx.EVT_BUTTON, tach9, btn9)




frame.Show()
app.MainLoop()
