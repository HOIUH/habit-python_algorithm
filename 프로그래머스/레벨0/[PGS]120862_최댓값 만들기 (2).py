# 230627
# [PGS] 최댓값 만들기 (2) / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120862

def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-2] * numbers[-1])
