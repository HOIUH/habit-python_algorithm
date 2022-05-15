# 20220515
# 소수 찾기
# https://www.acmicpc.net/problem/1978

import sys
from math import sqrt

N = int(input())

nums = list(map(int, sys.stdin.readline().split()))

prime_num = N
for num in nums:

    if num == 1:
        prime_num -= 1
        continue

    for k in range(2, int(sqrt(num)) + 1):  # 2와 3은 소수이므로 이 for문 돌지 않아도 됨
        if num % k == 0:  # & (num != k)
            prime_num -= 1
            break

print(prime_num)