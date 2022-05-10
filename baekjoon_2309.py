# 20220510
# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

# What is Brute Force?
'''
# : 무식한 힘
# 완전탐색 알고리즘. 즉, 가능한 모든 경우의 수를 모두 탐색하면서 요구조건에 충족되는 결과만을 가져옴.
# 예외 없이 100%의 확률로 정답만을 출력.
# 알고리즘 설계의 가장 기본적인 접근 방법은 해가 존재할 것으로 예상되는 모든 영역을 전체 탐색하는 방법.
# 선형 구조를 전체적으로 탐색하는 순차 탐색,
# 비선형 구조를 전체적으로 탐색하는 깊이 우선 탐색(DFS, Depth First Search)과
# 너비 우선 탐색(BFS, Breadth First Search)이 가장 기본적인 도구.
# 너비 우선 탐색은 브루트 포스와 관련 깊고, 깊이 우선 탐색은 백트래킹과 관련 깊음.

# 문제 해결 방법
# 1. 주어진 문제를 선형 구조로 구조화한다.
# 2. 구조화된 문제공간을 적절한 방법으로 해를 구성할 때까지 탐색한다.
# 3. 구성된 해를 정리한다.
'''

import sys

height_list = []
for _ in range(9):
    height_list.append(int(sys.stdin.readline().strip()))

sum_wrong = sum(height_list)-100

for height in height_list:
    wrong_dwarf = sum_wrong-height

    if wrong_dwarf in height_list[height_list.index(height)+1:]:
        height_list.remove(height)
        height_list.remove(wrong_dwarf)
        break

height_list.sort()
for i in height_list:
    print(i)

