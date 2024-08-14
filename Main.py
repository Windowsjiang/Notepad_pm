# coding:utf-8

import Forms as For
import Compiler as Com
import wx
import time

MainForm = For.MainForm.App()
MainForm.show()
time.sleep(100)
Com.Compil.Compil.start("stdin.ul")