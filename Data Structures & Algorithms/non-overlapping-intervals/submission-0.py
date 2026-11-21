class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0 or len(intervals)==1:
            return 0
        intervals.sort(key=lambda x:x[1])
        ans = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            #overlap
            if prev_end > intervals[i][0]:
                ans+=1

            #no overlap, update previous end
            else:
                prev_end = intervals[i][1]

        return ans
        #time: O(nlogn), space: O(n) - sorting space



        