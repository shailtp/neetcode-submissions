class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        visited=set()
        left=0

        #sliding window approach
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
            
            max_len = max(max_len, right-left+1)
            visited.add(s[right])
        
        return max_len





        