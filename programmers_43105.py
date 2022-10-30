# 221030
# 동적계획법(Dynamic Programming) > 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

'''
1. Memoization: 이전에 계산한 값을 메모리에 저장. Dynamic Programming에서 많이 사용되는 기술.
'''

def solution(triangle):
    for i in range(1, len(triangle)):
        len_i = len(triangle[i])
        for j in range(len_i):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len_i - 1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
