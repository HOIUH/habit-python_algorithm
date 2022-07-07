# 220707
# Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

'''
1. list.index(찾을값)
2. pow(x, y) => x**y
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        # 나의 풀이
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        len_columnTitle = len(columnTitle)
        result = 0

        for i in range(len_columnTitle):
            # columnTitle 숫자값을 26진수 취급
            # A부터 Z까지는 각각 1부터 26까지로 취급
            # 예) "ZY" = (26**1)*26 + (26**0)*25
            result += pow(26, len_columnTitle - 1 - i) * (alphabet.index(columnTitle[i]) + 1)

        return result



