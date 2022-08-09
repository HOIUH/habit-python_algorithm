# 220809
# Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# 참고
# 1. https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
# 2. [파이썬의 heapq 모듈로 힙 자료구조 사용하기] https://www.daleseo.com/python-heapq/

'''
1. heapq 모듈
2. maxheap, minheap
'''

from heapq import heappush, heappop

class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    def kthSmallest(self, matrix, k: int) -> int:

        # maxHeap 사용한 풀이
        # Complexity - Time: O(M*N*logK), where M<=300 is the number of rows, N<=300 is the number of columns.
        #            - Space: O(K), space for heap which stores up to k elements.
        m, n = len(matrix), len(matrix[0])
        maxHeap = []

        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])    # maxHeap이므로 마이너스 붙여서 push
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -heappop(maxHeap)
