# 기능개발
import math
def solution(progresses, speeds):
    answer = []
    l = []
    n = 0
    for i in range(len(speeds)):
        l.append(math.ceil((100 - progresses[i])/speeds[i]))
        if l[i] > n:
            answer.append(1)
            n = l[i]
        else:
            answer[-1] = answer[-1] + 1
    return answer