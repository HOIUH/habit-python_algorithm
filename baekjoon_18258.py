# 20220522
# 큐2
# https://www.acmicpc.net/problem/18258

# 시간 제한 존재 Python 3: 3초
# 리스트 사용하면 시간 초과
# deque 사용하여 통과

import sys
from collections import deque

n = int(sys.stdin.readline())

result = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        result.append(int(command[1]))
    elif command[0] == "pop":
        if not result:
            print(-1)
        else:
            print(result.popleft())
    elif command[0] == "size":
        print(len(result))
    elif command[0] == "empty":
        if not result:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not result:
            print(-1)
        else:
            print(result[0])
    elif command[0] == "back":
        if not result:
            print(-1)
        else:
            print(result[-1])


# 시간 초과
'''
result = []
for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        result.append(int(command[1]))
    elif command[0] == "pop":
        if not result:
            print(-1)
        else:
            print(result.pop(0))
    elif command[0] == "size":
        print(len(result))
    elif command[0] == "empty":
        if not result:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not result:
            print(-1)
        else:
            print(result[0])
    elif command[0] == "back":
        if not result:
            print(-1)
        else:
            print(result[-1])
'''