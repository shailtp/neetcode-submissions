import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #need a max heap to pop largest 2 elements and collision condition
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones)>1:
            largest = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if largest!=second:
                heapq.heappush(stones, largest-second)

        if len(stones)==1:
            return -1*heapq.heappop(stones)

        else:
            return 0

        #time: O(nlogn), space: O(1)



        