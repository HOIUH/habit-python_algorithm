# 220815
# Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    # def findCenter(self, edges: List[List[int]]) -> int:
    def findCenter(self, edges) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        elif edges[0][1] in edges[1]:
            return edges[0][1]