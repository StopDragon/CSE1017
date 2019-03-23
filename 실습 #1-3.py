# -*- coding: utf-8 -*-
print('화씨온도를 섭씨로 바꿔 줄께')
F = int(input('화씨로 몇 도?'))
C = (F - 32) * (5/9)
print('섭씨로', '%0.1f' % C, '도')
