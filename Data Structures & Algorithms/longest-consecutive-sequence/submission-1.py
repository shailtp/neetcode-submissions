class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #O(nlogn) solution would be to sort the input array and check consecutive to find max length

        #O(n) solution can be using set (O(n) space) and checking only valid sequence starts
        num_set=set(nums)

        max_len=0
        for i in num_set:
            if i-1 not in num_set:
                curr_len=1
                while i+1 in num_set:
                    curr_len+=1
                    i+=1
                max_len=max(max_len, curr_len)


        return max_len
                    
                
                    
        