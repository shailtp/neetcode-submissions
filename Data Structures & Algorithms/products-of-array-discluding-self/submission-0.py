class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #do not use division operator.
        #use two arrays left and right (to store product of elements on left of element and right of the element)
        n=len(nums)
        left=[1]*n
        right=[1]*n

        for i in range(1, n):
            left[i]=left[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            right[i]=right[i+1]*nums[i+1]

        res=[0]*n

        for i in range(n):
            res[i]=left[i]*right[i]

        return res

        #O(n) time, O(n) space
        