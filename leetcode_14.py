# 220616
# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)
        min_str = strs.pop(0)

        tmp = min_str
        for str in strs:

            for i in range(len(min_str)):
                if min_str[i] != str[i]:
                    tmp = min_str[:i]
                    break

            min_str = tmp

        return min_str






