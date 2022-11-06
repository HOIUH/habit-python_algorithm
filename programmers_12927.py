# 221106
# 야근 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

'''
1. heapq => 최소값을 배열의 맨 앞에 유지시켜주는 모듈
'''

import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    answer = 0

    # works 원본 그대로 heapq 만들면 [3, 3, 4] 순서가 되기 때문에
    # 원소에 - 붙여서 [-4, -3, -3] 순서로 만듦듦
   works = [-work for work in works]
    heapq.heapify(works)

    while n:
        max_val = heapq.heappop(works)
        heapq.heappush(works, max_val+1)
        n -= 1

    for work in works:
        answer += work ** 2

    return answer

'''
    # 나의 풀이
    # 효율성 실패
    if sum(works) <= n:
        return 0

    answer = 0
    while n:
        works.sort(reverse=True)
        if works[0] - works[1] > n:
            works[0] -= n
            break
        works[0] -= 1
        n -= 1

    for work in works:
        answer += work ** 2

    return answer
    '''

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
