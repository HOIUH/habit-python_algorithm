# 20220516
# 소수
# https://www.acmicpc.net/problem/2581
import sys
from math import sqrt

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

sum_prime_nums = 0
min_prime_num = 0
for i in range(M, N+1):
    if i == 1: continue

    err = 0
    for k in range(2, int(sqrt(i)+1)):
        if i % k == 0:
            err = 1
            break

    if err == 0:
        sum_prime_nums += i
        if min_prime_num == 0:
            min_prime_num = i

if sum_prime_nums == 0:
    print(-1)
else:
    print(sum_prime_nums)
    print(min_prime_num)
