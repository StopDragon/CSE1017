# -*- coding: utf-8 -*-
# 대출 원리금 균등분할 상환금 계산 함수 
def monthlyPaymentPlan(principal, interest, year):
    d = int((((1 + (interest/1200)) ** (year*12)) * principal * (interest/1200)) / (((1 + (interest/1200)) ** (year*12)) - 1))
    return d
print(monthlyPaymentPlan(10000000, 2.8, 4))
# should print 220460
