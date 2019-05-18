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
        if trypasswd == members[username][0]:  ##<trypasswd가 username의 비밀번호와 일치한다>:
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            print('You played ' + str(tries) + ' games and won ' + str(wins) + ' of them.')
            print('Your all-time winning percentage is ' + str(divide(wins,tries)) + ' %')
            if chips >= 0:
                print('You have ' + str(chips) + ' chips.')
            else:
                print('You owe ' + str(abs(chips)) + ' chips.')
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (username, 0,0,0)
        # username을 members 사전에 추가한다.
        return username, 0, 0, 0, members