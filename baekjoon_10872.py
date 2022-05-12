# 20220512
# 팩토리얼
# https://www.acmicpc.net/problem/10872

import sys

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

n = int(sys.stdin.readline())

print(factorial(n))
