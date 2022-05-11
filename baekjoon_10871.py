# 220511
# X보다 작은 수
# https://www.acmicpc.net/problem/10871
import sys

n, x = map(int, sys.stdin.readline().split())
list_a = list(map(int, sys.stdin.readline().split()))

result = ''
for i in list_a:
    if i < x:
        result += str(i)+' '

print(result.strip())