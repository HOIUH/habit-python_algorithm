# 230903
# [PGS] 가장 큰 수 찾기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):

    # 나의 풀이
    '''
    b_num = array[0]
    answer = [b_num, 0]

    for i in range(1, len(array)):
        if b_num < array[i]:
            b_num = array[i]
            answer = [b_num, i]

    return answer
    '''

    # 다른 사람 풀이
    # max 함수와 index 함수 사용
    val = max(array)
    return [val, array.index(val)]


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))
