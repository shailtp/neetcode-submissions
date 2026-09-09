class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        #at a position i, you can either come from i-1 or i-2. 
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))


        