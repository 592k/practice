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
    D_ = []
    P = []
    answer = []
    l = len(grid)
    for i in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        D = [[m,n],i]
        if D not in P:
            while D_ != D or D not in P:
                if D[1][0] >= l:
                    D[1][0] -= l
                elif D[1][0] < -l:
                    D[1][0] += l

                if D[1][1] >= l:
                    D[1][1] -= l
                elif D[1][1] < -l:
                    D[1][1] += l

                A = grid[D[1][0]][D[1][1]]
                P.append(D)
                x,y = D[1]

                if A == 'R':
                    D_ = [[x,y],R(D)]
                elif A == 'L':
                    D_ = [[x,y],L(D)]
                elif A == 'S':
                    D_ = [[x,y],S(D)]
                
                D = D_
            answer.append(len(P))

    return answer
# length 보다 over하는 location 조절 해야함!

print(solution(["SL", "LR"]))
