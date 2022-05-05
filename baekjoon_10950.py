# 20220505
# A+B - 3
# https://www.acmicpc.net/problem/10950

import sys

t = int(input())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
