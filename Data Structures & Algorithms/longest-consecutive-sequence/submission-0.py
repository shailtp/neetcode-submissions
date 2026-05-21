class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #O(nlogn) solution would be to sort the input array and check consecutive to find max length

        #O(n) solution can be using set (O(n) space) and checking only valid sequence starts
        res = 0
        store = set(nums)

        for num in nums:
            # ONLY start a streak if 'num' is the start of a sequence
            if num - 1 not in store:
                streak, curr = 0, num
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res