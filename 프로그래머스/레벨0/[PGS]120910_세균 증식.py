# 230730
# [PGS] 세균 증식 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, t):
    # 나의 풀이
    # return n * (2 ** t)

    # 다른 사람 풀이
    # 시프트 연산자 사용. <<는 비트를 왼쪽으로 이동시킴
    return n << t   # n * (2 ** t) 와 동일


print(solution(2, 10))
print(solution(7, 15))
