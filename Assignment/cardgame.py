# -*- coding: utf-8 -*-
import random
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    # 중첩 for 문으로 52장의 카드를 만들어 리스트 deck을 만든다.
    for s in suits:
        for r in ranks:
            deck = deck + [{'suit': s,'rank': r}]
    # deck을 무작위로 섞는다.
    random.shuffle(deck)
    return deck
    
def hit(deck):
    # deck이 비어있으면
    # 카드 1벌을 새로 만듬
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if (card.get('rank') == 'J') or (card.get('rank') == 'Q') or (card.get('rank') == 'K'):
            score = score + 10
        elif (card.get('rank') == 'A'):
            number_of_ace = number_of_ace + 1
            score += 11
        else:
            score = score + card.get('rank')
    if (score > 21) and (number_of_ace >= 1):
        score -= 10
    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        print(" ", card.get('suit'), card.get('rank'))

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

def divide(x,y):
    if y > 0:
        return "{0:.1f}".format(((x/y)*100))
    else:
        return 0

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    num = 1
    print("All-time Top 5 based on the number of chips earned")
    for name in sorted_members:
        if name[1][3] > 0:
            if num <= 5:
                print(num,'. ', name[0], ' : ', name[1][3],sep='')
                num += 1

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'              
        file.write(line)
    file.close()

def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

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
        members[username] = (trypasswd, 0,0,0)
        return username, 0, 0, 0, members

