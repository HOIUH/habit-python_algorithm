# 220617
# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # string.split() => 공백 기준 문자열 나눈 후 리스트 반환환
       return len(s.split()[-1])