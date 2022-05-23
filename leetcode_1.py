# 20220523
# Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 풀이1: 브루트 포스(Brute-Force)로 계산
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
        '''

        # 풀이2: in을 이용한 탐색
        for i, num in enumerate(nums):
            complement = target-num

            if complement in nums[i+1:]:    # Because I can't use the same element twice
                return [i, nums[i+1:].index(complement) +(i+1)]
