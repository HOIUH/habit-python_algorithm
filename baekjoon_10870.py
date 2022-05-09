# 220509
# 피보나치 수 5
# https://www.acmicpc.net/problem/10870
import sys

# 입력값 받음
n = int(sys.stdin.readline().strip())

# 재귀 함수 사용
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(n))

# for문 사용
'''
fb_list = [0, 1]

for i in range(2, n+1):
    fb_list.append(fb_list[i-2]+fb_list[i-1])

print(fb_list[n])
'''