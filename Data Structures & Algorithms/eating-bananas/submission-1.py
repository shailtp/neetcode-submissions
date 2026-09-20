class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #no of bananas can be between 1 and max(piles)
        #binary search and validation function to tesst if all bananas can be completed greedily  in <= hours

        right = max(piles)
        left = 1

        def hours(speed):
            res = 0 
            for p in piles:
                res = res + p//speed
                if p%speed!=0:
                    res+=1

            return res 

        while left<right:
            mid = left+(right-left)//2

            if hours(mid) <= h:
                right = mid
            else:
                left = mid+1
    
        return left