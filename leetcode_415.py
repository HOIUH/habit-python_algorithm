# 220709
# Add Strings
# https://leetcode.com/problems/add-strings/

'''
1. list[::-1] => 리스트 reverse
2. ''.join(list) => list 문자열 요소들을 하나로 합치기
3. carry = digit > 9 => digit > 9 인 경우, carry는 True (1) / 아닌 경우, carry는 False (0)
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        index1 = len(num1)
        index2 = len(num2)

        digit = 0  # 각 자릿수의 합
        carry = 0  # 자릿수 합이 10 이상인 경우 1이 됨
        result_list = []

        # or carry가 붙는 이유: num1, num2 자릿수가 같고 제일 왼쪽 자릿수 합이 10 이상인 경우 존재해서
        while index1 or index2 or carry:
            digit = carry

            if index1:
                index1 -= 1
                digit += int(num1[index1])
            if index2:
                index2 -= 1
                digit += int(num2[index2])

            # digit > 9 인 경우, carry는 True => 1
            # digit > 9 아닌 경우, carry는 False => 0
            carry = digit > 9
            result_list.append(str(digit % 10))

        # join 함수 사용하여 list 문자열 요소들을 하나로 합치기
        # 장 작은 자릿수부터 result_list에 담았으므로 reverse하여 return
        return ''.join(result_list[::-1])
