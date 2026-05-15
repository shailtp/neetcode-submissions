class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_string=''
        for i in range(len(s)):
            if s[i].isalnum():
                processed_string+=s[i].lower()

        left=0
        right=len(processed_string)-1

        while left<right:
            if processed_string[left]!=processed_string[right]:
                return False
            left+=1
            right-=1

        return True

        