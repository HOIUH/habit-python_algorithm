# 220708
# Reverse Bits
# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)

        # 나의 오답 풀이
        '''
        str_n = str(n).zfill(32)
        result = 0

        for i in range(32):
            result += int(str_n[i]) * pow(2, i)

        return f'{result} ({str_n[::-1]})'
        '''
