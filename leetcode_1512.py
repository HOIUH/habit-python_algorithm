# 220724
# Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

'''
1. list(collections.Counter(list).values()) => Counter의 value들만 뽑아서 list로
'''

import collections

class Solution:
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    def numIdenticalPairs(self, nums) -> int:
        nums = list(collections.Counter(nums).values())     # Counter의 value들만 뽑아서 list로
        cnt = 0
        for num in nums:
            for i in range(0, num):
                cnt += i

        return cnt

nums = [1,2,3,1,1,3]
a = Solution()
print(a.numIdenticalPairs(nums))