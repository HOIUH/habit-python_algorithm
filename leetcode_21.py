# 220528
# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(-1)
        cursor = head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cursor.next = l1  # Update next node
                l1 = l1.next      # Update l1
            else:
                cursor.next = l2  # Update next node
                l2 = l2.next  # Updata l2

            cursor = cursor.next  # Move cursor

        # Last node
        if l1 != None:
            cursor.next = l1

        else:
            cursor.next = l2

        return head.next

        # 에러 발생하는 코드
        '''
        # list1과 list2의 값을 비교하여 작은 값이 왼쪽에 오게 하고,
        # next는 그 다음 값이 엮이도록 재귀 호출

        if (not list1) or (list2 and (list1.val > list2.val)) :
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, 12)

        return list1
        '''