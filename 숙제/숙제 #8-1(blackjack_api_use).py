# -*- coding: utf-8 -*-
from cardgame import *
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
    return 'Bye!'

print(blackjack())