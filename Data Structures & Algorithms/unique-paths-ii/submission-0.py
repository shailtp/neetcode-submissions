class Solution:
    def uniquePathsWithObstacles(self, nums: List[List[int]]) -> int:
    
        m=len(nums)
        n=len(nums[0])

        if nums[0][0]==1:
            return 0

        #elements in first row and first column have only 1 way of traversal
        #dp[i, j] = dp[i-1, j] +dp[i, j-1]

        dp = [[1 for _ in range(n)] for _ in range(m)]

        

        for i in range(1,m):
            if nums[i][0]!=1:
                dp[i][0]=dp[i-1][0]

            else:
                dp[i][0]=0

        for j in range(1, n):
            if nums[0][j]!=1:
                dp[0][j]=dp[0][j-1]

            else:
                dp[0][j]=0

        

        for i in range(1, m):
            for j in range(1, n):
                if nums[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else:
                    dp[i][j]=0

        return dp[m-1][n-1]
        