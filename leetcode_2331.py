# 220811
# Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# 내 노션정리: https://www.notion.so/Tree-16e4b6566fd7410685d258665059b3d0

'''
1. 재귀로 트리 후위 순회 (Postorder)
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # 후위 순회 (postorder)
        # left > right > root
        if not root.left and not root.right:    # leaf node인 경우
            return True if root.val else False
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        return (l and r) if root.val == 3 else (l or r)

