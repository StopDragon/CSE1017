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

def blackjack():
    play_more = True
    print("Welcome to SMaSH Casino!")
    deck = fresh_deck() # deck 구성
    chips = 0 # 점수 초기화
    while play_more == True:
        print('-----')
        dealer = []
        player = []
        card, deck = hit(deck) # 1장 뽑아서
        player.append(card) # 손님에게 주고
        card, deck = hit(deck) # 1장 뽑아서
        dealer.append(card) # 딜러에게 주고
        card, deck = hit(deck) # 1장 뽑아서
        player.append(card) # 손님에게 주고
        card, deck = hit(deck) # 1장 뽑아서
        dealer.append(card) # 딜러에게 준다.
        # 딜러의 첫 카드를 제외하고 모두 보여준다.
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        # 손님의 카드를 보여준다.
        show_cards(player, "Your cards are:")
        # 손님 카드 합 계산
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            chips += 2
            print('Blackjack! You won.')
            print('chips = ', chips)
            play_more = more('Play more? (y/n)')
        else:
            hit_more = more('Hit? (y/n)')
            while hit_more == True:
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ", card["suit"], card["rank"])
                show_cards(player, "Your cards are:")
                if score_player > 21:
                    chips -= 1
                    print('You bust! I won.')
                    print('chips = ', chips)
                    play_more = more('Play more? (y/n)')
                    break
                hit_more = more('Hit? (y/n)')
            else:    
                while score_dealer <= 16:
                    card, deck = hit(deck) # 1장 뽑아서
                    dealer.append(card) # 딜러에게 준다.                    
                    score_dealer = count_score(dealer)
                show_cards(dealer, 'My cards are:')

                if score_dealer > 21:
                    chips += 1
                    print('I bust! You won.')
                    print('chips = ', chips)
                    play_more = more('Play more? (y/n)')
                else:
                    if score_dealer == score_player:
                        print('We draw.')
                        print('chips = ', chips)
                        play_more = more('Play more? (y/n)')
                    elif score_player > score_dealer:
                        chips += 1
                        print('Yon won.')
                        print('chips = ', chips)
                        play_more = more('Play more? (y/n)')
                    elif score_player < score_dealer:
                        chips -= 1
                        print('I won.')
                        print('chips = ', chips)
                        play_more = more('Play more? (y/n)')                   
    print('Bye!')

blackjack()