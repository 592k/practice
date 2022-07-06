# 완주하지 못한 선수
def solution(participant, completion):
    answer = list()
    for part in participant:
        if part in completion:
            completion.remove(part)
        elif part not in  completion:
            answer.append(part)

    return answer[0]

solution(participant, completion)
