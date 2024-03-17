# 240317
# [PGS] 등차수열의 특정한 항만 더하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/181931

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + d * i
    return answer
