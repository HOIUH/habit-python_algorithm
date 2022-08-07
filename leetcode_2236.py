# 220807
# Root Equals Sum of Children
# https://leetcode.com/problems/root-equals-sum-of-children/

# Optional[TreeNode] => 파라미터 타입이 TreeNode 아니면 None인 경우
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        # one liner solution
        return root.val == root.left.val + root.right.val

        # 나의 풀이
        '''
        if root.val == root.left.val + root.right.val: return True
        else: return False
        '''