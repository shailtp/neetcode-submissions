class Solution:
    def climbStairs(self, n: int) -> int:

        #at each step i, you can either come from i-1 or i-2
        #thus recurrence dp: dp[i] = dp[i-1]+dp[i-2]


        if n==1:
            return 1
        elif n==2:
            return 2

        dp=[1]*n

        dp[1]=2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
    

        return dp[n-1]
        