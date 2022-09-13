# 220913
# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

'''
1. 재귀로 permutaion(순열)과 factorial 구현
'''

def permutaion(x: int, y: int) -> int:
    if y == 0:
        return 1
    return x * permutaion(x-1, y-1)

def factorial(num: int) -> int:
    if num == 0:
        return 1
    return num * factorial(num - 1)

class Solution:
    def climbStairs(self, n: int) -> int:
        answer = 0
        two_cnt_max = int(n//2)+1
        for two_cnt in range(two_cnt_max):
            one_cnt = n-2*two_cnt
            answer += permutaion(one_cnt+two_cnt, two_cnt) // factorial(two_cnt)    # Combination과 동일

        return answer
