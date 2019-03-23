# -*- coding: utf-8 -*-
# 주민등록번호 검증 함수
def front_ok(front):
    if int(front[2]) < 2 :
        if front[2:4] == '02':
            if int(front[4:6]) == 29:
                if int(front[0:2]) % 4 == 0:
                    return True
                else:
                    return False
            elif int(front[4:6]) <= 28:
                return True
            else:
                return False
        elif front[2:4] == '01' or '03' or '05' or '07' or '08' or '10' or '12':
            if int(front[4:6]) <= 31:
                return True
        elif front[2:4] == '04' or '06' or '09' or '11':
            if int(front[4:6]) <= 30:
                return True
        else:
            return False
    else:
        return False

def back_ok(s):
    if int(s[13]) == 11 - ((2 * int(s[0]) + 3 * int(s[1]) + 4 * int(s[2]) + 5 * int(s[3])\
     + 6 * int(s[4]) + 7 * int(s[5]) + 8 * int(s[7]) + 9 * int(s[8]) + 2 * int(s[9])\
      + 3 * int(s[10]) + 4 * int(s[11]) + 5 * int(s[12])) % 11):
        return True
    else:
        return False

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)
