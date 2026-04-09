class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        sell_index = len(prices) - 1

        while sell_index > 0:
            buy = min(prices[0:sell_index])
            if prices[sell_index] - buy > profit:
                profit = prices[sell_index] - buy
            sell_index -= 1
        
        return profit
        