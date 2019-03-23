# -*- coding: utf-8 -*-
def isfloat(s):
    if s >= 0 and (s.partition('.')[2]).isdigit():
        return True
    elif s[0] == '-' and s[1].isdigit() or (s.partition('.')[2]).isdigit():
        return True
    elif s[0].isdigit():
        return True
    else :
        return False

print(isfloat(".112"))#True
print(isfloat("-.112"))#True
print(isfloat("3.14"))#True
print(isfloat("-3.14"))#True
print(isfloat("5."))#True
print(isfloat("5.0"))#True
print(isfloat("-777.0"))#True
print(isfloat("-777."))#True
print(isfloat("."))#False
print(isfloat(".."))#False
