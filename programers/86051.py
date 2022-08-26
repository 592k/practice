# 없는 숫자 더하기
def solution(numbers):
    A = {1,2,3,4,5,6,7,8,9}
    B = A - set(numbers)
    answer = sum(B)
    return answer