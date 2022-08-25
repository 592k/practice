# 최소직사각형
def solution(sizes):
    answer = 0
    a = 0
    b = 0
    for i in sizes:
        m = max(i)
        n = min(i)
        if m > a:
            a = m
        if n > b:
            b = n
    answer = a * b
    return answer