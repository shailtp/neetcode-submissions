class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buying = prices[0]
        max_profit = 0

        for selling in prices:
            min_buying = min(min_buying, selling)
            max_profit = max(max_profit, selling - min_buying)

        return max_profit

        
        