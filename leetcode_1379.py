# 220812
# Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# 참고: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/solution/

'''
1. Tree DFS 중위 순회 (재귀 & 반복)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 풀이 1. DFS: 재귀로 중위 순회
    # Time complexity: O(n) / Space complexity: O(n)
    '''
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)

        inorder(original, cloned)
        return self.ans
    '''

    # 풀이 2. DFS: 반복으로 중위 순회
    # Time complexity: O(n) / Space complexity: O(n)
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack_o, stack_c = [], []
        node_o, node_c = original, cloned

        while stack_o or node_c:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)

                node_o = node_o.left
                node_c = node_c.left

            node_o = stack_o.pop()
            node_c = stack_c.pop()

            if node_o is target:
                return node_c

            node_o = node_o.right
            node_c = node_c.right
