# -*- coding: utf-8 -*-
def isfloat(s):
    P = s.partition('.')
    if '.' > P[0] >= '-':
        return P[2].isdigit() or P[2] == ''
    elif P[0].isdigit():
        return P[2].isdigit() or P[2] == ''
    elif P[0] == '':
        return P[2].isdigit()
    else:
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
