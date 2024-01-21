# 240121
# [PGS] 짝수의 합 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    # 풀이 1
    # for 문 사용
    '''
    answer = 0
    for i in range(0,n+1,2):
        answer += i
    return answer
    '''

    # 풀이 2
    # sum과 range 사용
    return sum(range(0, n + 1, 2))



