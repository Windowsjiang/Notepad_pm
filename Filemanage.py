#coding:utf-8

import wx

class Main(wx.Frame, wx.Dialog):
    def __init__(self):
        super().__init__(None, title="Notepad +-:文件管理选项", size=(200, 300))
        panel = wx.Panel(self)
        st1 = wx.StaticText(panel, label="控制选项:")

        box1 = wx.StaticBox(panel, label="打开")
        st2 = wx.StaticText(panel, label="打开以查看或编辑一个文件")
        bt1 = wx.Button(panel, id=1, label="打开...")
        wx.Bind(wx.MouseEvent.Click, id=1, onclick1, bt1)
        sz1 = wx.StaticBoxSizer(box1, wx.VERTICAL)
        sz1.Add(st2)
        sz1.Add(bt1)

        box2 = wx.StaticBox(panel, label="管理(文件)")
        st3 = wx.StaticText(panel, label="新建，删除文件")
        bt2 = wx.Button(panel, id=2, label="管理...")
        wx.Bind(wx.MouseEvent.Click, id=2, onclick2, bt2)
        sz2 = wx.StaticBoxSizer(wx.VERTICAL)
        sz2.Add(st3)

        box3 = wx.StaticBox(panel, label="管理(文件夹)")
        st4 = wx.StaticText(panel, label="新建，删除文件夹")
        bt3 = wx.Button(panel, id=3, label="管理...")
        wx.Bind(wx.MouseEvent.Click, id=3, onclick3, bt3)
        sz2 = wx.StaticBoxSizer(wx.VERTICAL)
        sz2.Add(bt3)
        sz2.Add(st4)

        bt4 = wx.Button(panel, id=4, label="应用(确定)")
        bt5 = wx.Button(panel, id=5, label="取消")
        wx.Bind(wx.MouseEvent.Click, id=4, onclick4, bt4)
        wx.Bind(wx.MouseEvent.Click, id=5, onclick5, bt5)

        hbox = wx.BoxSizer()
        hbox.Add(sz1, proportion=10, wx.CENTER, border=5)
        hbox.Add(sz2, proportion=10, wx.CENTER, border=5)
        hbox.Add(sz3, proportion=10, wx.CENTER, border=5)
        hbox.Add(bt4, proportion=10, wx.CENTER, border=5)
        hbox.Add(bt5, proportion=10, wx.CENTER, border=5)

        panel.SetSizer(hbox)

    def onclick1(self, event):
        fileDialog = wx.FileDialog(self, message = "选择单个文件", wildcard = filesFilter, style = wx.FD_OPEN)
    
    def onclick2(self, event):
        form = FileDelete()
        form.show()
    
    def onclick3(self, event):
        form = FileDelte()
        form.show()

    def onclick4(self, event):
        self.destroy()
    
    def onclick5(self, event):
        self.refresh()
        self.destroy()

class FileDelete(wx.Dialog):
    def __init__(self):
        super().__init__(None, title="选择...", size=(200, 300), wx.CloseBox, wx.STAY_ON_TOP)

        panel = wx.Panel(self)
        st = wx.StaticText(panel, label="选择文件以删除")
        tc = wx.TextCtrl(panel, label="", wx.TE_READONLY)
        bt1 = wx.Button(panel, id=1, label="删除")
        wx.Bind(wx.MouseEvent.Click, onclick1, id=1, bt1)

        def onclick1(self, event):
            dlg = wx.TextEntryDialog(self, "删除文件(夹)", "请输入文件(夹)名", wx.STAY_ON_TOP, wx.CloseBox)
            value = dlg.GetValue()
            if value == "":
                frm = Forms.Error(self, 404)
                frm.show()
            else:
                tc.SetValue(value)
                try:
                    os.remove(value)
                except:
                    try:
                        os.removedir(value)
                    except:
                        try:
                            os.rmdir(value)
                        except:
                            frm = Forms.Error(self, 404)
                            frm.show()

frmm = Main()
frmm.show()
frmm.app = wx.App()
frmm.MainLoop()