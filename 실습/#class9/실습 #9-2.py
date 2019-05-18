# -*- coding: utf-8 -*-
members = {"doh": ("sid73", 994, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 0, -5),"who": ("poiuy", 34, 18, 0)}
def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    print('1. ', sorted_members[0]), ':', ((sorted_members[0])[3]))
    # sorted_members[:5]의 원소를 차례대로 참고하여 보여주되 0이하는 무시한다.
show_top5(members)