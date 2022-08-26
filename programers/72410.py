# 신규 아이디 추천
def solution(new_id):
    # 1
    l = new_id.lower()
    # 2
    n = ''
    for i in l:
        if i.isalpha() == True or i.isdigit() == True or i in ['-','_','.']:
            n+=i     
    # 3
    if '..' in n:
        while '..' in n:
            n = n.replace('..','.')
    # 4
    if len(n) != 0:
        if n[-1] == '.':
            n = n[:-1]
    if len(n) != 0:
        if n[0] == '.':
            n = n[1:]
    # 5
    if len(n) == 0:
        n = 'a'
    # 6
    if len(n) >= 16:
        n = n[:15]

    if n[-1] == '.':
        n = n[:-1]
    # 7
    if len(n) < 3:
        while len(n) !=3:
            n+=n[-1]
    answer = n
    return answer