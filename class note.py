def isfloat(s):
    good = s.partition('.')
    if '-' <= good[0] < '.' :
        return good[2].isdigit() or good[2] == ''
    elif good[0].isdigit() :
        return good[2].isdigit() or good[2] == ''
    elif good[0] == '' :
        return good[2].isdigit()
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
