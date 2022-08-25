# 성격 유형 검사하기
def solution(survey, choices):
    table = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    for i in range(len(survey)):
        a = survey[i][1]
        b = survey[i][0]
        c = choices[i]
        if choices[i] > 4:
            table[a] = table[a] + c - 4
        elif choices[i] < 4:
            table[b] = table[b] + round(3/c)
    
    if table['R'] >= table['T']:
        answer = 'R'
    elif table['R'] < table['T']:
        answer = 'T'

    if table['C'] >= table['F']:
        answer += 'C'
    elif table['C'] < table['F']:
        answer += 'F'

    if table['J'] >= table['M']:
        answer += 'J'
    elif table['J'] < table['M']:
        answer += 'M'

    if table['A'] >= table['N']:
        answer += 'A'
    elif table['A'] < table['N']:
        answer += 'N'

    return answer

print(solution(['TR','RT','TR'], [7,1,3]))