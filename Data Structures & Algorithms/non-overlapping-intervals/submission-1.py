class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0 or len(intervals)==1:
            return 0
        intervals.sort()

        prev_end = intervals[0][1]
        ans = 0

        for i in range(1, len(intervals)):
            if intervals[i][0]>=prev_end:
                prev_end = intervals[i][1]

            else:
                ans+=1
                prev_end = min(prev_end, intervals[i][1])

        return ans

        #time: O(nlogn), space: O(n)




        