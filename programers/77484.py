# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    x = 0
    y = 0
    for n in lottos:
        if n in win_nums:
            x+=1
        elif n == 0:
            y+=1
    a = 7-x-y
    b = 7-x
    if a == 7:
        a=6
    if b == 7:
        b=6
    answer = [a, b]

    return answer