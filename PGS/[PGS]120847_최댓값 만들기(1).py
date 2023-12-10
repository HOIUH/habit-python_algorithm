# 231210
# [PGS] 최댓값 만들기(1) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]
