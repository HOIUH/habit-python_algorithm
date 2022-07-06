# 220706
# Majority Element
# https://leetcode.com/problems/majority-element/

# Follow-up: Could you solve the problem in linear time and in O(1) space?
# => Using Boyer-Moore Majority Vote Algorithm

'''
1. Boyer-Moore Voting Algorithm
2. Counter(list).most_common
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 나의 풀이
        # 170 ms , 15.6 MB
        # return Counter(nums).most_common()[0][0]

        # Solution 2
        # HashMap
        # 251 ms , 15.6 MB
        '''
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        '''

        # Solution 6
        # Boyer-Moore Voting Algorithm
        # 참고: https://sgc109.github.io/2020/11/30/boyer-moore-majority-vote-algorithm/
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate






