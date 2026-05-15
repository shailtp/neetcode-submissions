class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying=prices[0]
        max_profit=0
        for selling in prices:
            buying=min(buying, selling)
            profit=selling-buying
            max_profit=max(max_profit, profit)

        return max_profit

        #O(n) time complexity, O(1) space complexity

        #O(n**2) would be the brute force approach where we check all possible pairs of buying/selling prices, which is not optimal...


        