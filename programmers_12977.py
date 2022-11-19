# 221119
# Summer/Winter Coding(~2018) > 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
from math import sqrt


def solution(nums):
    nC3 = list(combinations(nums, 3))
    answer = len(nC3)

    for element in nC3:
        s = sum(element)
        for i in range(2, int(sqrt(s))+1):
            if s % i == 0:
                answer -= 1
                break

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
