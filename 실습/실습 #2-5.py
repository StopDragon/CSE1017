# -*- coding: utf-8 -*-
def isleapyear(year):
    if year >= 0:
        if year < 100:
            if year % 4 == 0:
                return True
            else:
                return False
        else:
            if year % 100 == 0:
                if year % 400 != 0:
                    return False
                else:
                    return True
            elif year % 4 == 0:
                return True
            else:
                return False
    else:
        return None
print (isleapyear(0)) #true
print (isleapyear(1)) #false
print (isleapyear(4)) #true
print (isleapyear(2010)) #false
print (isleapyear(2011)) #flase
print (isleapyear(2012)) #true
print (isleapyear(2013)) #false
print (isleapyear(2016)) #true
print (isleapyear(1900)) #flase
print (isleapyear(2000)) #true
print (isleapyear(2100)) #flase
print (isleapyear(2200)) #flase
print (isleapyear(2400)) #true
print (isleapyear(-2000)) #none
