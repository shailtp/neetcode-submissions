class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap implementation
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

        #time: O(N + k log N), space: O(1)

        