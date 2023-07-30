# 230730
# [PGS] 종이 자르기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120922

def solution(M, N):
    # 나의 풀이
    # M이 1이 되기 위해 M-1 번의 가위질 필요. N번 반복
    return (M - 1) * N + (N - 1)    # (M * N) - 1


print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))
