# 신규 아이디 추천
def solution(new_id):
    n = new_id.lower()
    
    
    if len(n) < 3:
        while len(n) !=3:
            n.append(n[-1])
    return answer