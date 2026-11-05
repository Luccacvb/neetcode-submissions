class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = float("inf")
        profit = 0

        for price in prices:
            min_v = min(price, min_v)
            profit = max(profit, price - min_v)

        return profit
