# 키패드 누르기
def mid(L, R):
    LD, RD = {}, {}
    if L == '*':
        LD = {'0':1, '8':2, '5':3, '2':4}
    elif L == '7':
        LD = {'0':2, '8':1, '5':2, '2':3}
    elif L == '4':
        LD = {'0':3, '8':2, '5':1, '2':2}
    elif L == '1':
        LD = {'0':4, '8':3, '5':2, '2':1}
    elif L == '0':
        LD = {'0':0, '8':1, '5':2, '2':3}
    elif L == '8':
        LD = {'0':1, '8':0, '5':1, '2':2}
    elif L == '5':
        LD = {'0':2, '8':1, '5':0, '2':1}
    elif L == '2':
        LD = {'0':3, '8':2, '5':1, '2':0}

    if R == '#':
        RD = {'0':1, '8':2, '5':3, '2':4}
    elif R == '9':
        RD = {'0':2, '8':1, '5':2, '2':3}
    elif R == '6':
        RD = {'0':3, '8':2, '5':1, '2':2}
    elif R == '3':
        RD = {'0':4, '8':3, '5':2, '2':1}
    elif R == '0':
        RD = {'0':0, '8':1, '5':2, '2':3}
    elif R == '8':
        RD = {'0':1, '8':0, '5':1, '2':2}
    elif R == '5':
        RD = {'0':2, '8':1, '5':0, '2':1}
    elif R == '2':
        RD = {'0':3, '8':2, '5':1, '2':0}
    return LD, RD

def solution(numbers, hand):
    answer = ''
    L = '*'
    R = '#'
    for i in numbers:
        s = str(i)
        if i in [1,4,7]:
            answer += 'L'
            L = s
        elif i in [3,6,9]:
            answer += 'R'
            R = s
        elif i in [2,5,8,0]:
            LD, RD = mid(L, R)
            if hand == "right":
                if LD[s] >= RD[s]:
                    answer += 'R'
                    R = s
                else:
                    answer +='L'
                    L = s
            elif hand == "left":
                if LD[s] <= RD[s]:
                    answer += 'L'
                    L = s
                else:
                    answer +='R'
                    R = s
    return answer