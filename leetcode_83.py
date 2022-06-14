# 220614
# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # The key is that head has been already sorted
        curr = head

        # Wrong Answer
        # while curr.next != None:

        while curr:
            # curr.next is essential
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        # Wrong Answer
        # return curr

        return head

        '''
        temp = set()
        while head:
            temp.add(head.val)
            head = head.next

        temp = list(temp)

        result = ListNode(temp[0])
        # result.val = temp[0]

        for i in range(len(temp)):
            if i == len(temp) - 1:
                result.next = None
                # pass
            else:
                result.next = temp[i + 1]

            # result = result.next

        return result
        '''










