class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #so rate of eating banana's can be anywhere between 1 to max(piles) and we can do binary search. its given that h is larger than len of piles.
        left=1
        right=max(piles)

        while(left<=right):
            mid=left+(right-left)//2
            hours=0
            for p in piles:
                hours+=(p//mid)
                if p%mid!=0:
                    hours+=1
            
            if hours<=h: #fine, but we need to minimize hours
                ans=mid
                right=mid-1
            else:
                left=mid+1
    
        return ans






        