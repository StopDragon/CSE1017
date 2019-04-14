# -*- coding: utf-8 -*-
# 동전 합산 서비스 
print('동전 합산 해줄께... 음수는 넣지마.')
FH = int(input('오백원짜리 몇개?'))
H = int(input('백원짜리 몇개?'))
FT = int(input('오십원짜리 몇개?'))
T = int(input('십원짜리 몇개?'))
answer = FH * 500 + H * 100 + FT * 50 + T * 10
print('자기가 갖고 있는 동전은 총', answer,'원 이야.')
