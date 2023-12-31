# 231231
# [PGS] 피자 나눠 먹기 (1) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    # 풀이 1
    # divmod 사용
    '''
    a, b = divmod(n, 7)
    return a + 1 if b else a
    '''

    # 풀이 2
    return (n - 1) // 7 + 1
