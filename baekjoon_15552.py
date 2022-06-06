# 220606
# 빠른 A+B
# https://www.acmicpc.net/problem/15552

import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)