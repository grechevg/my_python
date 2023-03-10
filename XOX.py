import wx
from random import randint

def step_bot(xy, xo):
    if xy == (0, 0):
        btn1.SetLabel(xo)
    elif xy == (0, 1):
        btn2.SetLabel(xo)
    elif xy == (0, 2):
        btn3.SetLabel(xo)
    elif xy == (1, 0):
        btn4.SetLabel(xo)
    elif xy == (1, 1):
        btn5.SetLabel(xo)
    elif xy == (1, 2):
        btn6.SetLabel(xo)
    elif xy == (2, 0):
        btn7.SetLabel(xo)
    elif xy == (2, 1):
        btn8.SetLabel(xo)
    elif xy == (2, 2):
        btn9.SetLabel(xo)

def check_xo(xo):
    #TODO вместе тру выводить список выйграшных координат для выделения цветом
    global lst
    res = [[],[],[],[],[]]
    for i in range(3):
        res.append(lst[i])
        for j in range(3):
            res[j].append(lst[i][j])
            if j == i:
                res[3].append(lst[i][j])
            if j == 2 - i:
                res[4].append(lst[i][j])
    return any([l.count(xo) == 3 for l in res])

def step_level():
    global lst
    if check_xo(gemer):
        str_out.SetLabel('Победил: X')
        print('-----------------', ' Ura !!! Победил: ', gemer)
    else:
        i, j = randint(0, 2), randint(0, 2)
        while lst[i][j] != 'z':
            i, j = randint(0, 2), randint(0, 2)
        lst[i][j] = bot
        step_bot((i, j), bot)
        if check_xo(bot):
            str_out.SetLabel('Победил: O')
            print('-----------------', ' Ura !!! Победил: ', bot)


def tach1(event):
    global lst
    if btn1.GetLabel() == '':
        lst[0][0] = gemer
        btn1.SetLabel(gemer)
        step_level()
    print('сработала кнопка 1', event)

def tach2(event):
    global lst
    if btn2.GetLabel() == '':
        lst[0][1] = gemer
        btn2.SetLabel(gemer)
        step_level()
    print('сработала кнопка 2', event)

def tach3(event):
    global lst
    if btn3.GetLabel() == '':
        lst[0][2] = gemer
        btn3.SetLabel(gemer)
        step_level()
    print('сработала кнопка 3', event)

def tach4(event):
    global lst
    if btn4.GetLabel() == '':
        lst[1][0] = gemer
        btn4.SetLabel(gemer)
        step_level()
    print('сработала кнопка 4', event)

def tach5(event):
    global lst
    if btn5.GetLabel() == '':
        lst[1][1] = gemer
        btn5.SetLabel(gemer)
        step_level()
    print('сработала кнопка 5', event)

def tach6(event):
    global fl
    if btn6.GetLabel() == '':
        lst[1][2] = gemer
        btn6.SetLabel(gemer)
        step_level()
    print('сработала кнопка 6', event)

def tach7(event):
    global fl
    if btn7.GetLabel() == '':
        lst[2][0] = gemer
        btn7.SetLabel(gemer)
        step_level()
    print('сработала кнопка 7', event)

def tach8(event):
    global fl
    if btn8.GetLabel() == '':
        lst[2][1] = gemer
        btn8.SetLabel(gemer)
        step_level()
    print('сработала кнопка 8', event)

def tach9(event):
    global lst
    if btn9.GetLabel() == '':
        lst[2][2] = gemer
        btn9.SetLabel(gemer)
        step_level()
    print('сработала кнопка 9', event)

app = wx.App()

frame = wx.Frame(None, title='Крестики Нолики', size=(380, 600))
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

#TODO что делать дальше

lst = [['z', 'z', 'z'],
       ['z', 'z', 'z'],
       ['z', 'z', 'z']]
gemer, bot = 'X', 'O'
print('dct ajslfajsd')
frame.Show()
app.MainLoop()
