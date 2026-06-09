class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum=0
        max_sum=float('-inf')

        for num in nums:
            running_sum=max(running_sum+num, num)
            max_sum=max(running_sum, max_sum)

        return max_sum
        