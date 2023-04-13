
class Solution:
    def maxProfit(self, prices) -> int:
        left = 0 #buy
        right = 1 #sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit