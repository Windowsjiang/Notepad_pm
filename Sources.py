#coding:utf-8

import SourseScanUI as ssui
import Forms.MainForm.__init__

def GetSoursePos(Sourse, target) -> list:
    open(__file__, 'r')
    data = __file__.raed()
    indexes=[]
    for i in range(len(Sourse) - 1):
        char = Sourse[i]
        for Sourse, c in enumerate(SourseScanUI):
            if char == c:
                if target == "begin":
                    indexes.append(index)
                elif target == "end":
                    indexes.append(index + 1)
                else:
                    raise Exception("该名称不存在:{}".format(target))
        
        return indexes

Set_sentence = []

language = ssui.Scan(tc.GetValue)
ssui.Change_set_sentence(language)

def IsPrime(Number) -> bool:
    if type(Number) == "<class 'float'>":
        return False
    else:
        if Number == 2:
            return True
        else:
            for i in range(1, int(sqrt(Number))):
                if Number % i == 0:
                    return False
        
            return True

def __file__() -> str:
    