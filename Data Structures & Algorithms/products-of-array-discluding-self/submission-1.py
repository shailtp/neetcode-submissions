class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
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

        '''

        

        #O(n) time, O(n) space. Another trick is finding out number of zeroes and
        #multiplication of non zero elements 
        zero_count = 0
        product = 1
        for n in nums:
            if n==0:
                zero_count+=1

            else:
                product=product*n

        res=[]

        if zero_count>1:
            for _ in range(len(nums)):
                res.append(0)

        elif zero_count==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    res.append(product)
                else:
                    res.append(0)

        else:
            for n in nums:
                res.append(product//n)

        return res
            
    