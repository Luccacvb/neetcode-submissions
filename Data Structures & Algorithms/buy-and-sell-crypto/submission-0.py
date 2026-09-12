class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]

        for i in range(1, len(prices)):
            current_value = prices[i]
            max_profit = max(max_profit, current_value - min_value)
            min_value = min(min_value, current_value)

        return max_profit
