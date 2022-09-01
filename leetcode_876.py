# 220831
# Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

'''
1. Singly-linked list
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # while (fast != None) and (fast.next != None):     # 아래와 동일
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

'''
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

a = Solution()
answer = a.middleNode(node1)
print(answer.val)
print(answer.next.val)
print(answer.next.next.val)
'''