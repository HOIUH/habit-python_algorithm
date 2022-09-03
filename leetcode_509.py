# 220903
# Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

'''
print(f'a: {a}, b: {b}') 의 결과
1. # a: 100, b: 200
a, b = 4, 100
a = b
b = a+b
2. # a: 100, b: 104
a, b = 4, 100
a, b = b, a+b
'''

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a+b   # a값과 b값이 동시에 업데이트됨!
        return a

        # 나의 풀이
        '''
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
        '''

x = Solution()
print(x.fib(6))
