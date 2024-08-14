#coding:utf-8

import wx

class MainForm(wx.Frame):
    def init(self):
        self.frame = wx.Frame(self, parent=None, title="Notepad+- [Empty]", size=(640, 360))
        icon = wx.EmptyIcon()
        icon.LoadFile("icon.ico", wx.BITMAP_TYPE_ICO)
        frame.SetIcon(icon)
        self.pnl = wx.Panel(parent=self.frame)
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  
        # create parent panel for button
        self.pnl = wx.Panel(self)
  
        # create wx.Bitmap object 
        bmp = wx.Bitmap('font.png')
  
        # create button at point (20, 20)
        self.st1 = wx.Button(self.pnl, id = 1, label ="字体", pos =(20, 20), size =(100, 30),  name ="button1")
        wx.Bind(wx.MouseEvent.Click, st4, id = 1, id1evt)
        # set bmp as bitmap for button
        self.st1.SetBitmap(bmp)
  
        self.SetSize((190, 100))
        self.SetTitle('wx.Button')
        self.Centre()

        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  
        # create parent panel for button
        self.pnl = wx.Panel(self)
  
        # create wx.Bitmap object 
        bmp = wx.Bitmap('bold.png')
  
        # create button at point (20, 20)
        self.st2 = wx.Button(self.pnl, id = 2, label ="加粗", pos =(220, 20), size =(100, 30),  name ="button2")
        wx.Bind(wx.MouseEvent.Click, st4, id = 2, id2evt)
        # set bmp as bitmap for button
        self.st2.SetBitmap(bmp)
  
        self.SetSize((190, 100))
        self.SetTitle('wx.Button')
        self.Centre()

        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  
        # create parent panel for button
        self.pnl = wx.Panel(self)
  
        # create wx.Bitmap object 
        bmp = wx.Bitmap('tools.png')
  
        # create button at point (20, 20)
        self.st3 = wx.Button(self.pnl, id = 3, label ="工具", pos =(420, 20), size =(100, 30),  name ="button3")
        wx.Bind(wx.MouseEvent.Click, st4, id = 3, id3evt)
          
        # set bmp as bitmap for button
        self.st3.SetBitmap(bmp)
  
        self.SetSize((190, 100))
        self.SetTitle('wx.Button')
        self.Centre()

        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
  
        # create parent panel for button
        self.pnl = wx.Panel(self)
  
        # create wx.Bitmap object 
        bmp = wx.Bitmap('file.png')
  
        # create button at point (20, 20)
        self.st4 = wx.Button(self.pnl, id = 4, label ="文件", pos =(620, 20), size =(100, 30),  name ="button4")
        wx.Bind(wx.MouseEvent.Click, st4, id = 4, id4evt)
        # set bmp as bitmap for button
        self.st.SetBitmap(bmp)
  
        self.SetSize((190, 100))
        self.SetTitle('wx.Button')
        self.Centre()

        self.tc1 = wx.TextCtrl(self.pnl, (315, 225), (630, 250), style=wx.MULTILINE|wx.RICH2)
        while True:
            long = len(tc1.GetValue())
            if len(tc1.GetValue()) > long:
                for i in range(len(Sourse.Word_list) - 1):
                    j = 0
                    pos1 = Sourses.GetSoursePos(Sourses.Word_list[i], "begin")[j]
                    pos2 = Sourses.GetSoursePos(Sourse.Word_list[i], "end")[j]

                    eval(Sourses.Set_sentence[i])
            else:
                pnl.RefeshPanel()
        
        hbox1 = wx.BoxSizer()
        hbox1.Add(st1, proportion=10, wx.HORZENAL, border=5)
        hbox1.Add(st2, proportion=10, wx.HORZENAL, border=5)
        hbox1.Add(st3, proportion=10, wx.HORZENAL, border=5)
        hbox1.Add(st4, proportion=10, wx.HORZENAL, border=5)
        pnl.Add(hbox1, proportion=10, wx.CENTER, border=5)
    
    def id1evt(self, event):
        open("Font.py")
    def id2evt(self, event):
        font = wx.Font(14, wx.FontFamilyDefault, wx.Bold, wxFontWeightDefault, False, "Arial")
        self.tc1.SetFont(font)
    def id3evt(self, event):
        open("Tools.py")
    def id4evt(self, event):
        open("Filemanage.py")

class Tips(wx.Frame):
    def __init__(self):
        frame = wx.Frame(self, parent = None, title="Notepad+- - Waring", size=(300, 200))
        icon = wx.EmptyIcon()
        icon.LoadFile("Waring.ico", wx.BITMAP_TYPE_ICO)
        frame.SetIcon(icon)

        pnl = wx.Panel(frame)
        st1 = wx.StaticText(pnl, label="警告:{}".format(Err_no))
        bt1 = wx.Button(pnl, id=1, label="确定")
        wx.Bind(wx.MouseEvent.Click, bt1, id=1, id1_evt)

        hbox = wx.BoxSizer()
        hbox.Add(st1, proportion=10, wx.HORZENAL, border=5)
        hbox.Add(bt1, proportion=10, wx.HORZENAL, border=5)

        panel.Add(hbox, proportion=10, wx.CENTER, border=5)
    
    def id1_evt(self, event):
        frame.hide()

class Error(wx.Frame):
    def __init__(self, err_id):
        frame = wx.Frame(self, parent = None, title="Notepad+- - Error", size=(300, 200))
        icon = wx.EmptyIcon()
        icon.LoadFile("Error.ico", wx.BITMAP_TYPE_ICO)
        frame.SetIcon(icon)

        pnl = wx.Panel(frame)
        st1 = wx.StaticText(pnl, label="错误:{}".format(err_id))
        bt1 = wx.Button(pnl, id=1, label="确定")
        wx.Bind(wx.MouseEvent.Click, bt1, id=1, id1_evt)

        hbox = wx.BoxSizer()
        hbox.Add(st1, proportion=10, wx.HORZENAL, border=5)
        hbox.Add(bt1, proportion=10, wx.HORZENAL, border=5)

        panel.Add(hbox, proportion=10, wx.CENTER, border=5)
    
    def id1_evt(self, event):
        frame.hide()
        open("SolveError{}.py".format(err_id))

