# 220715
# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

'''
1. c = Counter(string)
2. num = c.get(string)
https://www.daleseo.com/python-collections-counter/
'''

from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0

        counter_stones = Counter(stones)

        for jewel in jewels:
            num = counter_stones.get(jewel)
            if num:
                answer += num

        return answer

'''
jewels = "aA"
stones = "aAAAbb"
a = Solution()
print(Solution.numJewelsInStones(a, jewels, stones))
'''