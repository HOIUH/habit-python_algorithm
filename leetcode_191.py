# 220724
# Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

'''
1. 2진수 int => n = 0b1101
2. bin(10진수 int) 또는 bin(2진수 int) => return type: string
3. 비트 연산자 &: a & b 비트값이 둘다 1이여야 결과로 1 반환
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        # input n은 0b11011 이런식으로 주어짐

        '''
        # 나의 풀이
        n_str = str(n)  # 10진수 문자열
        b = bin(int(n_str))
        return b.count('1')
        '''

        # Solution 1
        # return bin(n).count('1')

        # Solution 2
        # instantly find a bit with value 1 and then count it and then move to the next value 1
        # 참고: https://python.plainenglish.io/leet-code-191-number-of-1-bits-explained-python3-solution-661a2b77e8c3
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1

        return cnt