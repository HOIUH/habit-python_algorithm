# 220601
# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# 86. Maximum Subarray 문제와 유사
# 저점과 현재 값과의 차이 계산
# 카데인 알고리즘을 응용한 O(n)에 풀이

import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        profit = 0  # -sys.maxsize

        # 최소값과 최대 수익을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

