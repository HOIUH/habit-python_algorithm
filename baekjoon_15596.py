# 20220427
# 정수 N개의 합
# https://www.acmicpc.net/problem/15596

def solve(a: list) -> int:
    #n = len(a)
    sum = 0
    for i in a:     # 이렇게 사용하면 n = len(a) 필요없음
        sum += i

    return sum
