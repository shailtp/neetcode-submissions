class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res_str = ''
        def expand(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1

            return s[left+1:right]

        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i, i+1)

            if len(odd)>longest:
                res_str = odd
                longest = len(odd)

            if len(even)>longest:
                res_str = even
                longest = len(even)

        
        return res_str
                
            

        
            
        