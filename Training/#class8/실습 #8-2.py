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
        fresh_deck()
        card = deck[0]
        deck = deck[1:]
        return (card, deck)
    else:
        card = deck[0]
        deck = deck[1:]
    return (card, deck) # (맨 앞의 카드 한장 , 남은 deck)
