#coding:utf-8

import wx
 
 
class About(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
             
        self.InitUI()
         
    def InitUI(self):    
 
        menubar = wx.MenuBar()
        help = wx.Menu()
        help.Append(100, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id=100)
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)
 
        self.SetSize((300, 200))
        self.SetTitle('About')
        self.Centre()
        self.Show(True)
 
    def OnAboutBox(self, e):
         
        description = """Notepad +- 是一个文件编辑器，支持.py, .cpp, .txt,
         .c, .h等多种文件类型的编辑。且有代码高亮，富文本编辑等功能(测试中), 
         可以替换(初期功能可能稀缺)Notepad ++.
         本软件的翻译可能有误，请谅解
"""
 
        licence = """Notepad +- is free software; you can redistribute 
it and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation; either version 2 of the License, 
or (at your option) any later version.
 
Notepad +- is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
See the GNU General Public License for more details. You should have 
received a copy of the GNU General Public License along with Notepad +-; 
if not, write to the Free Software Foundation, Inc., 59 Temple Place, 
Suite 330, Boston, MA  02111-1307  USA

Notepad+-是免费软件；您可以重新分发它。
它和(或)根据GNU通用公共许可证的条款对其进行修改，如由[1]自由软件基金会发布；
本许可证的版本2，
或（由您选择）任何更高版本。
分发Notepad+-是希望它有用，
但没有任何保证；甚至没有暗示的保证
适销性或适合的特定用途。
有关更多详细信息，请参阅[2]GNU通用公共许可证。你应该有
收到一份GNU通用公共许可证的副本和Notepad+-；
如果没有，请写信给自由软件基金会。
地址：
59 Temple Place，
330room，Boston，MA02111-1307 USA

[1]:英Free Software Foundation
[2]:英GNU General Public Licence"""
 
 
        info = wx.AboutDialogInfo()
 
        info.SetIcon(wx.Icon('Icon.ico', wx.BITMAP_TYPE_ICO))
        info.SetName('Notepad +-')
        info.SetVersion('0.0.1')
        info.SetDescription(description)
        info.SetCopyright('(C) 2024 Windowsjiang')
        info.SetLicence(licence)
        info.AddDeveloper('Windowsjiang')
        info.AddDocWriter('Windowsjiang')
        info.AddArtist('Windowsjiang')
        info.AddTranslator('Windowsjiang')
 
        wx.AboutBox(info)
 
 
def main():
     
    ex = wx.App()
    Example(None)
    ex.MainLoop()    
 
 
if __name__ == '__main__':
    main()