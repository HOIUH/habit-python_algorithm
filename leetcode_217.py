# 220530
# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from collections import Counter

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 풀이 1. collections.Counter 사용
        # list 요소 개수 count
        # most_common 쓰면 count 큰 순서대로 오른쪽과 같이 출력됨. [(key, value), (key, value), ...]
        if Counter(nums).most_common(1)[0][1] > 1:
            return True
        else:
            return False

        # 풀이 2. set 사용
        a = len(nums)
        b = len(set(nums))
        return a != b


