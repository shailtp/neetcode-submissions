class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals already sorted

        merged = []
        for i in range(len(intervals)):
            interval = intervals[i]

            #current interval is before the new one
            if interval[1]<newInterval[0]:
                merged.append(interval)

            
            #curr interval after newInterval,
            elif newInterval[1]<interval[0]:
                merged.append(newInterval)
                return merged+intervals[i:]


            #overlap, merge and update newInterval start and end
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        merged.append(newInterval)
        return merged

        #time: O(n), space: O(n)