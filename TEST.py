# -*- coding: utf-8 -*-
members = {"doh": ("sid73", 994, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 0, -5),"who": ("poiuy", 34, 18, 0)}

def divide(x,y):
    return x/y if y > 0 else 0

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members:  ##<members의 키 중에서 username이 있다>:
        if trypasswd == members[username][0]:  ##<trypasswd가 username의 비밀번호와 일치한다>:
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            print('You played ' + str(tries) + ' games and won ' + str(wins) + ' of them.')
            print('Your all-time winning percentage is ' + str("{0:.1f}".format(divide(wins, tries)*100)) + ' %')
            if chips >= 0:
                print('You have ' + str(chips) + ' chips.')
            else:
                print('You owe ' + str(abs(chips)) + ' chips.')
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (username, 0, 0, 0)# username을 members 사전에 추가한다.
        return username, 0, 0, 0, members

login(members)