# 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    for i in range(len(arr)):    
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i-1] != arr[i]:
                answer.append(arr[i])
    return answer
