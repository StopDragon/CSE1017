# -*- coding: utf-8 -*-
# 해와 달 수를 날짜 수로 환산 
print('해와 달 수를 날짜 수로 환산해드립니다.')
year = int(input('몇 년?'))
month = int(input('몇 개월?'))
answer = (year * 365) + (month * 30)
print(year, '년', month, '개월은 날짜로 환산하면',int(answer), '일입니다.')
