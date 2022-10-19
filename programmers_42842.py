# 221019
# 완전탐색 > 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

'''
1. math.sqrt(number) == number**1/2
'''

import math

def solution(brown, yellow):
    total_tile_cnt = brown + yellow

    # for x in range(3, int(brown / 2)):    # 나의 풀이
    # for x in range(3, int(total_tile_cnt**1/2)+1):    # math.sqrt 대신 기본 연산자로 제곱근 구함
    for x in range(3, int(math.sqrt(total_tile_cnt))+1):
        y, remainder = divmod(total_tile_cnt, x)
        if not remainder and x + y == (brown / 2) + 2:
            return sorted([x, y], reverse=True)


print(solution(10, 2))
