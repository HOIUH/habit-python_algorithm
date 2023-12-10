# 231210
# [PGS] 팩토리얼 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    # 풀이 1
    # for문 사용
    tmp = 1
    for i in range(1, n+1):
        tmp = tmp * i
        if tmp > n:
            return i-1
        elif tmp == n:
            return i
