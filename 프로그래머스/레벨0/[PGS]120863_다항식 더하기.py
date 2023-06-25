# 230626
# [PGS] 다항식 더하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    coefficient, constant = 0, 0
    answer = ''

    p = polynomial.split(' + ')
    for e in p:
        if e == 'x':
            coefficient += 1
        elif e[-1] == 'x':
            coefficient += int(e[:-1])
        else:
            constant += int(e)

    if coefficient == 0:
        answer = str(constant)
    else:
        if coefficient == 1:
            answer = 'x'
            if constant:
                answer += ' + ' + str(constant)
        else:
            answer = str(coefficient) + 'x'
            if constant:
                answer += ' + ' + str(constant)

    return answer
