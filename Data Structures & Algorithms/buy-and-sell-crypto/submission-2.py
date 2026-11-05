class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = float("inf")
        max_v = 0
        profit = 0

        for price in prices:
            if price < min_v:
                min_v = price
                max_v = price

            if price > max_v:
                max_v = price

            profit = max(profit, max_v - min_v)

        return profit
