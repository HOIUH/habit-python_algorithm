# 20220508
# 지능형 기차 2
# https://www.acmicpc.net/problem/2460
import sys

current = 0
maxpass = 0
for i in range(10):
    people_out, people_in = map(int, sys.stdin.readline().split())
    current += people_in-people_out

    if maxpass < current: maxpass = current

print(maxpass)

'''
result = []
for i in range(10):
    a, b = map(int, sys.stdin.readline().split())

    if i == 0:
        result.append(b)
    else:
        result.append(result[i-1]+b-a)

#print(result)
print(max(result))
'''



