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