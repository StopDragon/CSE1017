# -*- coding: utf-8 -*-
class NegativeInteger(Exception): pass
def input_float_one():
    while True:
        try:
            s = float(input('고정소수점를 입력하세요.'))
            if not -1 <= s <= 1: raise NegativeInteger
        except NegativeInteger:
            print('-1부터 1까지의 수만 입력할 수 있습니다.')
        except ValueError as e:
            print(e,'은(는) 고정소수점이 아닙니다.')
        except:
            print('알 수 없는 오류가 발생하였습니다. 다시 입력해주세요.')
        else:
            print('입력한 고정소수점은 ',s,'입니다.',sep='')
            break
input_float_one()