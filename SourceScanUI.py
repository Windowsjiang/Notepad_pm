#coding:utf-8

import wx

class CompilerSelect(wx.Dialog):
    def __init__(self):
        super().__init__(None, title="Notepad+- :选择编译(解释)器", size=(300, 200), wx.CloseBox)
        panel=wx.Panel(self)

        box1 = wx.StaticBox(panel, label="选择编译(解释)器")
        st1 = wx.StaticText(panel, label="编译器可以帮助您更快地发现问题")
        bt1 = wx.Button(panel, id=1, label="按文件格式选择")
        bt2 = wx.Button(panel, id=2, label="选择默认编译器")
        wx.Bind(wx.MouseEvent.Click, on_click1, id=1, bt1)
        wx.Bind(wx.MouseEvent.Click, on_click2, id=2, bt2)
        