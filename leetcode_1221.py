# 220820
# Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

'''
1. Greedy Algorithm: 선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 해답에 도달하는 방법
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0

        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt == 0:
                res += 1

        return res
