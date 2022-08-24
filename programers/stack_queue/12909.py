# 올바른 괄호
def solution(s):
    n=0
    for i in s:
        if i =='(':
            n+=1
        else:
            n-=1
        if n<0:
            answer = False
            break
    if n == 0:
        answer = True
    else:
        answer = False

    return answer

s = '(()('
print(solution(s))