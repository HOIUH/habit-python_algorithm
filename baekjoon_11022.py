# 20220518
# A+B - 8
# https://www.acmicpc.net/problem/11022

# python f-string
# https://blockdmask.tistory.com/429

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
