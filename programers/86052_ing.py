# 빛의 경로 사클
def R(D):
    d0, d1 = D
    w, q = d1
    dx = d1[0] - d0[0]
    dy = d1[1] - d0[1]
    if dx > 0:
        q = d1[1] - 1
    elif dx < 0:
        q = d1[1] + 1
    elif dy > 0:
        w = d1[0] + 1
    elif dy < 0:
        w = d1[0] - 1
    return [w,q]

def L(D):
    d0, d1 = D
    w, q = d1
    dx = d1[0] - d0[0]
    dy = d1[1] - d0[1]
    if dx > 0:
        q = d1[1] + 1
    elif dx < 0:
        q = d1[1] - 1
    elif dy > 0:
        w = d1[0] - 1
    elif dy < 0:
        w = d1[0] + 1
    return [w,q]

def S(D):
    d0, d1 = D
    w, q = d1
    dx = d1[0] - d0[0]
    dy = d1[1] - d0[1]
    if dx > 0:
        w = d1[0] + 1
    elif dx < 0:
        w = d1[0] - 1
    elif dy > 0:
        q = d1[1] - 1
    elif dy < 0:
        q = d1[1] + 1
    return [w,q]

def solution(grid):
    m = 0
    n = 0
    c = 0
    D_ = []
    P = []
    for x,y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        T = [[m,n],[x,y]]
        D = [[m,n],[x,y]]
        while T != D or D not in P:
            A = grid[x][y]
            if A == 'R':
                D_ = [[x,y],R(D)]
            elif A == 'L':
                D_ = [[x,y],L(D)]
            elif A == 'S':
                D_ = [[x,y],S(D)]
            
            D = D_


    answer = []
    return answer
# length 보다 over하는 location 조절 해야함!

print(solution(["SL", "LR"]))
