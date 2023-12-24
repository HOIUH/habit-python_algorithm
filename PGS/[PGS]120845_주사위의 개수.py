# 231224
# [PGS] 주사위의 개수 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    answer = 1

    for b in box:
        answer *= b // n

    return answer
