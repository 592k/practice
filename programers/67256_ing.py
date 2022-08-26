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

    if R == '#':
        RD = {'0':1, '8':2, '5':3, '2':4}
    elif L == '9':
        RD = {'0':2, '8':1, '5':2, '2':3}
    elif L == '6':
        RD = {'0':3, '8':2, '5':1, '2':2}
    elif L == '3':
        RD = {'0':4, '8':3, '5':2, '2':1}
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
                else:
                    answer +='L'
            if hand == "left":
                if LD[s] <= RD[s]:
                    answer += 'L'
                else:
                    answer +='R'
    return answer
    
print(solution([1,3,4,5,8,2,1,4,5,9,5], "right"))