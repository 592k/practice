# 타겟 넘버
def solution(numbers, target):
    answer = 0
    for i in range(2**len(numbers)):
        b = format(i, 'b').zfill(len(numbers))
        p = []

        for t in range(len(b)):
            if b[t] == '0':
                p.append(-numbers[t])
            else:
                p.append(numbers[t])

        if sum(p) == target:
            answer +=1
    return answer