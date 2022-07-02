# 220702
# Add Binary
# https://leetcode.com/problems/add-binary/
'''
1. int(string, 2) => 문자열을 2진수로 취급하여 십진수 int로 변환
2. bin(decimal) => 십진수 int를 2진수로 변환
3. f'{integer:b}' => 십진수 int를 2진수 문자열로 변환
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # <f-string 사용>
        # f-string은 python 3.6부터 사용 가능
        # a, b를 십진수 int로 바꾼후 덧셈 -> f-string 사용하여 2진수 문자열로 변환
        return f'{int(a, 2) + int(b, 2):b}'

        # return str(bin(int(a, 2) + int(b, 2)))[2:]

        # <나의 풀이>
        '''
        len_a = len(a)
        len_b = len(b)

        dec_a = 0
        dec_b = 0

        for i in range(len_a):
            dec_a += int(a[i])*(2**(len_a-1-i))
            #dec_a += int(a[i])*pow(2, len_a-1-i)

        for i in range(len_b):
            dec_b += int(b[i])*(2**(len_b-1-i))
            #dec_b += int(b[i])*pow(2, len_b-1-i)

        dec_sum = dec_a + dec_b

        return str(bin(dec_sum))[2:]
        '''


