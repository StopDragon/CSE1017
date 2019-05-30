# -*- coding: utf-8 -*-
def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if card.get('rank') == 'J' or card.get('rank') == 'Q' or card.get('rank') == 'K':
            score = score + 10
        elif card.get('rank') == 'A':
            number_of_ace = number_of_ace + 1
            score = score + 11
        elif 2 <= card.get('rank') <= 9:
            score = score + card.get('rank')
    while score > 21:
        score = score - 10
    return score

# {"suit": "Heart", "rank": 7}
