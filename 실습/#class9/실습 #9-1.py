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
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            # username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
            print('You played', str(chips), 'games and won', str(wins), 'of them.')
            # 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
            print('Your all-time winning percentage is', divide(wins, tries), '%')
            # 칩 보유개수를 보여줌
            if chips >= 0:
                print('You have', str(chips), 'chips.')
            else:
                print('You owe', abs(str(chips)), 'chips.')
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (username, 0, 0, 0)
        # username을 members 사전에 추가한다.
        return username, 0, 0, 0, members

login(members)
