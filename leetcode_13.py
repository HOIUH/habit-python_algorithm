# 220527
# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# 1. string 및 list 요소 개수 셀 때 => string.count(찾을 내용)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_nums = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM'
            , 'M', 'D', 'C', 'L', 'X', 'V', 'I']
        arabian_nums = [4, 9, 40, 90, 400, 900
            , 1000, 500, 100, 50, 10, 5, 1]

        '''
        sub_roman_nums = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        sub_arabian_nums = [4, 9, 40, 90, 400, 900]
        roman_nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        arabian_nums = [1000, 500, 100, 50, 10, 5, 1]
        '''

        output = 0
        for i in range(len(roman_nums)):
            output += s.count(roman_nums[i]) * arabian_nums[i]
            s = s.replace(roman_nums[i], '')

        return output
