# 20220513
# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

# 최대공약수 by 유클리드 호제법
# 최소공배수 * 최대공약수 = 두수의 곱

import sys
x, y = map(int, sys.stdin.readline().split())

if x >= y: big, small = x, y
else: big, small = y, x

# python엔 do-while 구문 없음
while True:
    a = big % small
    if a > 0:
        big = small
        small = a
        continue
    break

# 최대공약수
print(small)
# 최소공배수
print(int(x * y / small))
