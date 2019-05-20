# -*- coding: utf-8 -*-
members = {"doh": ("sid73", 994, 550, 35), "didi": ("edd484", 130, 55, 10), "hy": ("er878re", 35, 18, 2), "dr": ("qwert", 18, 0, -5),"who": ("poiuy", 34, 18, 0)}
def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    num = 1
    print("All-time Top 5 based on the number of chips earned")
    for name in sorted_members:
        if name[1][3] > 0:
            print(num,'. ', name[0], ' : ', name[1][3],sep='')
            num += 1

