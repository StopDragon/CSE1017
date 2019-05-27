# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input("자연수를 입력해주세요: "))
        assert n >= 0
    except ValueError as e:
        print(e, "은(는) 자연수가 아닙니다.",sep='')
    except AssertionError:
        print(n,"은(는) 자연수가 아닙니다.",sep='')
    else:
        print('입력한 자연수는 ',n,'입니다.',sep='')
        break