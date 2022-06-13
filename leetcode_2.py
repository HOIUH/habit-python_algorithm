# 220613
# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        str_l1 = ""
        str_l2 = ""
        while l1:
            str_l1 = str(l1.val) + str_l1
            l1 = l1.next

        while l2:
            str_l2 = str(l2.val) + str_l2
            l2 = l2.next

        result = str(int(str_l1) + int(str_l2))
        # result_list = list(map(int, str(result)))
        # result_listnode = ListNode()  

        prev = None
        for r in str(result):
            node = ListNode(r)
            node.next = prev
            prev = node

        '''
        for i in range(len(result_list)-1, 0, -1):
            result_listnode.val = result_list[i]
            result_listnode.next = result_list[i-1]
        '''

        return node
