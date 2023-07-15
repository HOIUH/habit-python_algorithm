# 230716
# [PGS] k의 개수 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    '''
    answer = 0
    k = str(k)

    for num in range(i, j + 1):
        answer += str(num).count(k)

    return answer
    '''

    # 다른 사람 풀이
    # 1. sum과 list comprehension 사용
    # return sum([str(num).count(str(k)) for num in range(i, j + 1)])

    # 2. sum과 map, lambda 사용
    return sum(map(lambda num: str(num).count(str(k)), range(i, j + 1)))
