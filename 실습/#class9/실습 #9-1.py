# -*- coding: utf-8 -*-
members = {"doh": ("sid73", 994, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 0, -5),"who": ("poiuy", 34, 18, 0)}
def divide(x,y):
    if y > 0:
        return "{0:.1f}".format(((x/y)*100))
    else:
        return 0

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if members.get(username):
        if (trypasswd == members[username][0]):
            # username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
            print('You played', str(members[username][1]), 'games and won', str(members[username][2]), 'of them.')
            # 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
            print('Your all-time winning percentage is', str(divide(members[username][2], members[username][1])), '%')
            # 칩 보유개수를 보여줌
            if (members[username][3] >= 0):
                print('You have', str(members[username][3]), 'chips.')
            else:
                print('You owe', str(abs(members[username][3])), 'chips.')
        else:
            return login(members)
    else:
        members[username] = (username, 0,0,0)
        # username을 members 사전에 추가한다.
        return username, 0, 0, 0, members

login(members)
