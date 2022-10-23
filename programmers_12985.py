# 221023
# 2017 팁스타운 > 예상 대진표
# https://school.programmers.co.kr/learn/courses/30/lessons/12985

# 더 간단한 풀이
def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

# 나의 풀이
'''
from math import ceil

def solution(n, a, b):
    answer = 0
    a, b = min(a, b), max(a, b)

    while True:
        answer += 1
        ceil_a, ceil_b = ceil(a / 2), ceil(b / 2)

        if ceil_a == ceil_b:
            return answer

        a, b = ceil_a, ceil_b
'''