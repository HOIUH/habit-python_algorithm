# 220829
# Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for i in range(len(s)):
            if s[i] in t[idx:]:
                # t[idx:]의 index로 idx 값 업데이트 해줘야함
                idx += t[idx:].index(s[i]) + 1
            else:
                return False

        return True

s, t = 'abc', 'ahbgdc'
# s, t = 'axc', 'ahbgdc'
# s, t = 'aaaaaa', 'bbaaaa'
a = Solution()
print(a.isSubsequence(s, t))