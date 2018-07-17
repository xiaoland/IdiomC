# -*- encoding=utf-8 -*-
import re

def turn(file):

    file.replace(" → ", "\")
    trunlist = []
    a = 0
    b = 3
    while 1 == 1:
        try:
            trunlist.append(file[a:b])
        except:
            break
        else:
            a = a + 5
            b = b + 4
    print(trunlist[0:len(trunlist) - 1])


turn()

