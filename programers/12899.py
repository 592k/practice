# 124 나라의 숫자
def solution(n):
    answer = ''
    while n != 0:
        n, y = divmod(n, 3)
        if y == 0:
            answer = '4' + answer
            n -= 1
        else:
            answer = str(y) + answer
    return answer