# 220917
# 완전탐색 > 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# 나의 풀이
'''
    max_width = 0
    max_length = 0

    for size in sizes:
        size.sort()
        width = size.pop()
        length = size.pop()

        max_width, max_length = max(max_width, width), max(max_length, length)

    return max_width*max_length
'''

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))