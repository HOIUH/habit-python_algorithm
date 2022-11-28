# 221128
# 행렬의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    return [[x + y for x, y in zip(X, Y)] for X, Y in zip(arr1, arr2)]

'''
    # 나의 풀이
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer
'''

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
