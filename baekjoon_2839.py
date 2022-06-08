# 220608
# 설탕 배달
# https://www.acmicpc.net/problem/2839

import sys

n = int(sys.stdin.readline().strip())

d = divmod(n, 5)

if (d[1] % 3) == 0:
    print(d[0] + (d[1]//3))
else:
    if n % 3 == 0:
        print(n//3)
    else:
        print(-1)

"""
if (d[1] % 3) == 0:
    print(d[0] + (d[1]//3))
elif (n % 3) == 0:
    print(n // 3)
else:
    for i in range(d[0]-1, 0, -1):
        print(-1)
"""

