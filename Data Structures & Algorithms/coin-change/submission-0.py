class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        coins.sort()

        for i in range(1, amount+1):
            min_c = float('inf')

            for c in coins:
                diff = i-c
                if diff<0:
                    break

                min_c = min(min_c, dp[diff]+1)

            dp[i] = min_c

        if dp[amount]<float('inf'):
            return dp[amount]

        else:
            return -1

        #time: O(coins*amount) , space: O(amount)


        