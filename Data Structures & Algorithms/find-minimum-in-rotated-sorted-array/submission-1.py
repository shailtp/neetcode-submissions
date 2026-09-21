class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        min_e = float('inf')
        for i in range(n):
            min_e = min(min_e, nums[i])

        return min_e
            






         


        