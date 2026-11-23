class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        l,r = 0,0

        while r<len(nums):
            #before appending check that there are no smaller values in queue
            while q and q[-1]<nums[r]:
                q.pop()

            q.append(nums[r])

            #check if sliding window has reached size k
            if r-l+1==k:
                result.append(q[0])

                #check if the max value is coming from left pointer since we need to pop it
                if q[0]==nums[l]:
                    q.popleft()

                l+=1
            r+=1

        return result

        #time: O(n), space: O(1)
        