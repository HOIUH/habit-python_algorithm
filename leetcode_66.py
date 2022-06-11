# 220611
# Plus One
# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        l = len(digits)
        result = 1

        for i in range(l):
            exponent = l - i - 1

            # 리스트 각 요소에 10의 지수승을 곱함
            result += digits[i] * 10 ** exponent

        # map 사용한 return
        # return list(map(int, str(result)))

        # list comprehension 사용한 return
        return [i for i in str(result)]
