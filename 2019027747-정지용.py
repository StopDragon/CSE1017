# 반 : 10시
# 학번 : 2019027747
# 이름 : 정지용
# 구글클래스 이름 : 프로그래밍기초 ICT10

### 1. 독서 퀴즈 (이노베이터)
# (1) O
# (2) O
# (3) X
# (4) O

### 2. 환율 계산

def yen2usdollar(yen,jpywon,usdwon):
    return round((((jpywon * 1000) / (usdwon * 1000))* (yen/100)),2)

# print(yen2usdollar(10000,1107.15,1138.95)) # 97.21
# print(yen2usdollar(50000,1107.15,1138.95)) # 486.04

### 3. 비감소 리스트 확인

def nondecreasing(ns):
    if len(ns) > 1:
        for a in ns:
            for b in ns[1]:
                if a > b:
                    return False
                else a <= b:
                    return True
    else:
        return True

# print(nondecreasing([])) # True
# print(nondecreasing([3])) # True
# print(nondecreasing([3,3])) # True
# print(nondecreasing([3,4,5,5,8,9])) # True
# print(nondecreasing([3,4,3,3,8,9])) # False
# print(nondecreasing([1,3,5,14,22,59,59])) # True
# print(nondecreasing([1,3,5,14,22,59,58])) # False

### 4. 일반재귀 함수를 꼬리재귀 함수로 변환하기

def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0]//2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []

# print(updown([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
# print(updown([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]

def updownT(ns):
    def loop(ns,ss):
        if ns != []:
            if ns[0] % 2 == 0:
                ss = ss + [ns[0]//2]
                ns = ns[1:]
                return loop(ns,ss)
            else:
                ss = ss + [ns[0]*2]
                ns = ns[1:]
                return loop(ns,ss)
        else:
            return ss
    return loop(ns,[])

# print(updownT([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
# print(updownT([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]

### 5. 꼬리재귀 함수를 while 루프 함수로 변환하기

def updownW(ns):
    ss = []
    while ns != []:
        if ns[0] % 2 == 0:
            ss = ss + [ns[0]//2]
            ns = ns[1:]
        else:
            ss = ss + [ns[0]*2]
            ns = ns[1:]
    return ss

# print(updownW([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
# print(updownW([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]

### 6. for 루프 함수로 만들기

def updownF(ns):
    ss = []
    for i in ns:
        if i % 2 == 0:
            i = i//2
            ss = ss + [i]
        else:
            i = i * 2
            ss = ss + [i]
    return ss

# print(updownF([4, 6,  5, 3,  7, 6, 2, 1, 3, 2]))
# #            [2, 3, 10, 6, 14, 3, 1, 2, 6, 1]
# print(updownF([14, 69, 87, 13, 0, 16, 83, 19, 45, 88]))
# #            [7, 138, 174, 26, 0, 8, 166, 38, 90, 44]


### 7. 12시간 시계 형식 확인
def validClock12(time):
    (hour, colon, minuteplus) = time.partition(":")
    minute = minuteplus[:-2]
    amORpm = minuteplus[-2:]
    return len(minute[-2:]) == 2 and  minute[-2:] != '60' and (hour == '1' or hour == '2' or hour == '3' or hour == '4' or hour == '5' or hour == '6' or hour == '7' or \
    hour == '8' or hour == '9' or hour == '10' or hour == '11' or hour == '12')

# print(validClock12("1:30am")) # True
# print(validClock12("9:12pm")) # True
# print(validClock12("3:05am")) # True
# print(validClock12("10:14pm")) # True
# print(validClock12("11:59pm")) # True
# print(validClock12("12:00am")) # True
# print(validClock12("12:00pm")) # True
# print(validClock12("0:15am")) # False
# print(validClock12("09:18pm")) # False
# print(validClock12("3:5am")) # False
# print(validClock12("00:00pm")) # False
# print(validClock12("5:60am")) # False

### 8. 12시간 시계를 24시간 시계로 변환
def clock12to24(time):
        (hour, colon, minuteplus) = time.partition(":")
        minute = minuteplus[:-2]
        amORpm = minuteplus[-2:]
        return len(minute[-2:]) == 2 and  minute[-2:] != '60' and (hour == '01' or hour == '02' or hour == '03' or hour == '04' or hour == '05' or hour == '06' or hour == '07' or \
        hour == '08' or hour == '09' or hour == '10' or hour == '11' or hour == '12')

# print(clock12to24("12:00am")) # 00:00
# print(clock12to24("12:05am")) # 00:05
# print(clock12to24("1:30am")) # 01:30
# print(clock12to24("3:05am")) # 03:05
# print(clock12to24("12:00pm")) # 12:00
# print(clock12to24("12:08pm")) # 12:08
# print(clock12to24("3:50pm")) # 15:50
# print(clock12to24("9:12pm")) # 21:12
# print(clock12to24("11:59pm")) # 23:59


### 9. 종료시간 계산하기

def minutesAfter(time, passedMinute):
    (hour,_,minute) = time.partition(":")
    passedHour = passedMinute // 60
    passedMinute = passedMinute % 60
    hour = int(hour) + int(passedHour)
    minute = int(minute) + int(passedMinute)
    time = str(hour) + ":" + str(minute)
    (hour,_,minute) = time.partition(":")
    while minute > 60:
        passedHour = int(minute) // 60
        passedMinute = int(minute) % 60
        hour = int(hour) + int(passedHour)
        minute = int(passedMinute)
    return str(hour) + ":" + str(minute)

# print(minutesAfter("3:34",100)) # 5:14
# print(minutesAfter("11:45",20)) # 12:5
# print(minutesAfter("9:59",1)) # 10:0
# print(minutesAfter("123:10",200)) # 126:30

# 10 아이소그램 확인

def isisogram(word):
    temp = 'word[0]'
    turn = 0
    if word == '':
        return True
    elif len(word) == 1:
        return True
    elif word[0] == word[1]:
        return False
    else:
        if word.find(temp) == -1:
            turn += 1
            return False

# print(isisogram("")) # True
# print(isisogram("a")) # True
# print(isisogram("aa")) # False
# print(isisogram("and")) # True
# print(isisogram("hanyang")) # False
# print(isisogram("playground")) # True
# print(isisogram("uncopyrightables")) # True


### 11. 짝 찾기
def findAllPairs(ns,n):
    pairs = []
    pass # 이 부분을 중첩 for 루프 코드로 채운다.
    return pairs

# print(findAllPairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],10))
# # [(0, 1), (0, 5), (3, 4), (4, 8)]
# print(findAllPairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],5))
# # [(0, 7), (3, 6), (3, 9), (6, 8), (8, 9)]
# print(findAllPairs([4, 6, 5, 3, 7, 6, 2, 1, 3, 2],7))
# # [(0, 3), (0, 8), (1, 7), (2, 6), (2, 9), (5, 7)]


# 12. 이진수 시프트(좌우로 밀기) 연산

def shift(ds,move):
    if move < 0:
        pass # 이 부분을 코드로 채운다.
    else:
        return ds[:-move]

# print(shift("11011",3)) # 11011000
# print(shift("11011",2)) # 1101100
# print(shift("11011",1)) # 110110
# print(shift("11011",0)) # 11011
# print(shift("11011",-1)) # 1101
# print(shift("11011",-2)) # 110
# print(shift("11011",-3)) # 11
# print(shift("11011",-4)) # 1
# print(shift("11011",-5)) # 0
# print(shift("11011",-6)) # 0
