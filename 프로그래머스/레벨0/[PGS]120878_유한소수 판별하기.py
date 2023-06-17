# 230616
# [PGS] 유한소수 판별하기 / 레벨0
# https://school.programmers.co.kr/learn/courses/30/lessons/120878

def solution(a, b):
    # 1. a와 b의 최대공약수 구하기
    # 2. 최대공약수로 b를 나누기 => b값 재할당
    # 3. b의 소인수가 2와 5뿐인지 확인
    #     3-1. b를 2로 루프돌며 나누다가 나눠떨어지지 않으면 5로 나누기
    #     3-2. 5로 나눠떨어지면 루프 빠져나와 return 1
    #     3-3. 2나 5로 나눠떨어지지 않으면 return 2
    from math import gcd

    gcd_val = gcd(a, b)
    b = b // gcd_val

    x = 2
    while b > 1:
        if (b % x) == 0:
            b = b // x
        else:
            if x == 2:
                x = 5
            else:
                return 2
    return 1

