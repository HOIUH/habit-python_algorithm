# 20220514
# N번째 큰 수
# https://www.acmicpc.net/problem/2075

import heapq
import sys

n = int(sys.stdin.readline().strip())
heap = []

for _ in range(n):
    nums = list(map(int, sys.stdin.readline().split()))

    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])

'''
# 메모리 초과 발생
import sys

n = int(sys.stdin.readline().strip())

all_list = []
for _ in range(n):
    all_list.append(list(map(int, sys.stdin.readline().split())))

# numpy 없이 list를 transpose
# zip 결과는 tuple이므로 list로 형변환
all_list = [list(x) for x in zip(*all_list)]

x = 0
while x < n:
    min_idx = 0
    min_num = all_list[0][0]

    for i in range(n):
        if all_list[i][0] < min_num:
            min_idx = i
            min_num = all_list[i][0]

    all_list[min_idx].remove(min_num)
    x += 1

print(min_num)
'''
