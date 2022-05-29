# 220529
# Maximum Subarray
# https://www.acmicpc.net/problem/10211
import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    x = list(map(int, sys.stdin.readline().split()))

    # 풀이 1: 메모이제이션 (Memoization)
    # Memoization은 주어진 입력값에 대한 결과를 저장함으로써
    # 같은 입력값에 대해 함수가 한 번만 실행되는 것을 보장한다
    # (보통 딕셔너리에 저장한다)
    for i in range(1, n):
        x[i] += x[i-1] if x[i-1] > 0 else 0

    print(max(x))

    # 풀이 2: 카데인 알고리즘 (Kadane)
    # 이해가 안 감

    # 내 풀이
    '''
    sum_list = []
    s = 0

    for i in range(n):
        if i == n-1:
            sum_list.append(x[i])9

        s = x[i]
        sum_list.append(s)

        for k in range(i+1, n):
            s += x[k]
            sum_list.append(s)

    print(max(sum_list))
    '''
