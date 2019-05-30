# -*- coding: utf-8 -*-
def input_float():
    while True:
        try:
            s = float(input('고정소수점를 입력하세요.'))
        except ValueError as e:
            print(e,'은(는) 고정소수점이 아닙니다.')
        except:
            print('알 수 없는 오류가 발생하였습니다. 다시 입력해주세요.')
        else:
            print('입력한 고정소수점은 ',s,'입니다.',sep='')
            break
input_float()