class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=0
        ans=float('-inf')

        for i in nums:
            max_sum=max(max_sum+i, i)
            ans=max(ans, max_sum)


        return ans


            
        