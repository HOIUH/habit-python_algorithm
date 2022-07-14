# 220714
# Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))

            # 위처럼 max() 함수 사용하는 게 더 빠름
            # if sum(account) > max_wealth: max_wealth = sum(account)

        return max_wealth