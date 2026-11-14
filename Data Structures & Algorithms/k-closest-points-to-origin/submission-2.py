class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return x**2+y**2

        heap = []

        for x,y in points:
            d = distance(x,y)

            if len(heap)<k:
                heapq.heappush(heap, (-d,x,y))

            else:
                heapq.heappush(heap, (-d,x,y))
                heapq.heappop(heap)

        res = []
        for d,x,y in heap:
            res.append((x,y))
        
        return res

        #time: O(nlogk), space:O(k)
        