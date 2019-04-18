# -*- coding: utf-8 -*-
def binSearchClosest(list,key):
    position = 0
    temp = key**10
    if list == []:
        return None
    for a in range(len(list)-1):
        first = abs(list[a] - key)
        second = abs(list[a+1] - key)
        if list[0] == key:
            return position
        elif first > second and temp > second:
            position = a + 1
            temp = second
        elif first < second and temp > first:
            position = a + 1
            temp = first
    return (position)
