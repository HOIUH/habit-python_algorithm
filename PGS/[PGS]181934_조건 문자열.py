# 231203
# [PGS] 조건 문자열 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181934

def solution(ineq, eq, n, m):
    # 풀이 1
    '''
    if (eq == "=") & (n == m):
        return 1

    if (ineq == "<") & (n < m):
        return 1
    elif (ineq == ">") & (n > m):
        return 1

    return 0
    '''

    # 풀이 2
    # eval() 활용 => string 형태의 계산식의 결과를 bool 타입으로 리턴
    # eval은 보안 취약점 때문에 실무 코드엔 사용하지 않음
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))

