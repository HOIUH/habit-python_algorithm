# 231210
# [PGS] 합성수 찾기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    # 풀이 1
    # 합성수 = 소수가 아닌 수 임을 이용
    sosu = 1

    for i in range(2, n + 1):
        sosu += 1
        for k in range(2, i // 2 + 1):
            if i % k == 0:
                sosu -= 1
                break

    return n - sosu
