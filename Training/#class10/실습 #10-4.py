# -*- coding: utf-8 -*-
class Ready(Exception): pass
class notReady(Exception): pass
class notsatis(Exception): pass
class negative(Exception): pass
def combPascal(n, r):
    matrix = [[]] * (n - r + 1)
    matrix[0] = [1] * (r + 1)
    for i in range(1, n - r + 1):
        matrix[i] = [1]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]
print('This program computes combination of two natural numbers, n and r.')
print('Press Control-C to quit.')
while True:
    try:
        enter = input('Press Enter when you are ready.')
        if enter == '': raise Ready
        if not enter == '': raise notReady
        if r > n: raise notsatis
    except notReady:
        continue
    except notsatis:
        print('"r"is bigger than "r"(r =< n)')
    except KeyboardInterrupt: # 종료
        print('Goodbye!')
        break
    except Ready: #모든 조건 만족
        while True:
            try:
                n = int(input('Enter n:'))
                r = int(input('Enter r:'))
                if (n <= 0) or (r <= 0): raise negative
            except ValueError as e:
                print(e, "은(는) 자연수가 아닙니다.",sep='')
            except negative:
                print(n,"은(는) 자연수가 아닙니다.",sep='')
            else:
                break
        print(n,'C',r,'=', combPascal(n,r))
