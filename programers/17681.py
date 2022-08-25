# 비밀지도
def bin(arr):
    return list(map(lambda x:int(format(x, 'b')), arr))

def solution(n, arr1, arr2):
    answer = []
    a = bin(arr1)
    b = bin(arr2)
    for t, i in zip(a, b):
        answer.append(str(t+i).zfill(n).replace('0', ' ').replace('1','#').replace('2','#'))
    return answer