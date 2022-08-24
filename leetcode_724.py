# 220824
# Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

'''
1. for i, v in enumerate(List)
'''

class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex(self, nums) -> int:
        # 내 풀이와 Solution 풀이 둘 다 sum(nums)을 이용하지만
        # 내 풀이는 case를 지나치게 세분화하여 nums를 전부 돌게 만들었음

        # 나의 풀이
        '''
        if sum(nums[1:]) == 0:
            return 0
        else:
            nums_sum = sum(nums)
            for i in range(1, len(nums) - 1):
                if sum(nums[:i]) == (nums_sum - nums[i]) / 2:
                    return i
            if sum(nums[:-1]) == 0:
                return len(nums) - 1
            else:
                return -1
        '''

        # Solution 풀이
        # Time Complexity: O(N), where N is the length of nums
        # Space Complexity: O(1), the space used by leftsum and nums_sum
        nums_sum = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (nums_sum - leftsum - x):
                return i
            leftsum += x
        return -1

a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))