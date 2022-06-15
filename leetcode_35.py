# 220615
# Search Insert Position
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] < target:
                if i == len(nums)-1:
                    return i+1
                else:
                    pass
            else:
                return i