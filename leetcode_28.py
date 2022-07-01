# 220701
# Implement strStr()
# https://leetcode.com/problems/implement-strstr/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        else:
            # find 함수는 needle이 haystack에 없으면 -1 리턴함
            return haystack.find(needle)