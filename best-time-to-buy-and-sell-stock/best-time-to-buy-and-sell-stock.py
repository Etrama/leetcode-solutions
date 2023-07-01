class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > best_profit:
                best_profit = prices[i] - min_price
        return best_profit