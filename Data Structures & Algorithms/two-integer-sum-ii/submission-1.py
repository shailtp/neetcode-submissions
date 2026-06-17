class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #since numbers are already sorted. a 2 pointer approach seems better or binary search
        left = 0
        right = len(nums)-1

        while left<right:
            if nums[left]+nums[right]==target:
                return [left+1, right+1]
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                right-=1

        


                