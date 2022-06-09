# 220609
# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s).items()

        for c in counter:
            if c[1] == 1:
                return s.index(c[0])

        return -1  # count 값이 1인 경우가 없으면 -1 출력


