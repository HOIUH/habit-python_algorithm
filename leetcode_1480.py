# 220627
# Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        runningSum = 0

        for num in nums:
            runningSum += num
            result.append(runningSum)

        return result




