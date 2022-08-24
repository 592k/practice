# 프린터
def solution(priorities, location):
    answer = 0
    m = sorted(priorities)
    l = list(enumerate(priorities))
    while True:
        a,b = l[0]
        if int(b) >= m[-1]:
            answer+=1
            m.pop()
            if int(a) == location:
                break
            l.pop(0)
        else:
            l.append(l[0])
            l.pop(0)

    return answer

# 개선
def solution(priorities, location):
    answer = 0
    m = sorted(priorities)
    l = list(enumerate(priorities))
    while True:
        a,b = l.pop(0)
        if int(b) >= m[-1]:
            answer+=1
            m.pop()
            if int(a) == location:
                break
        else:
            l.append((a,b))

    return answer