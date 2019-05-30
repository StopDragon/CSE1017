# -*- coding: utf-8 -*-
def searchWidestGap(list):
    temp = 0
    position = 0
    if list == []:
        return (0,-1)
    for a in range(len(list)-2):
        front = abs(list[a] - list[a+1])
        back = abs(list[a+1] - list[a+2])
        if front < back and temp < back:
            temp = back
            position = a + 1
        elif front > back and temp < front:
            temp = front
            position = a
    return (temp,position)
