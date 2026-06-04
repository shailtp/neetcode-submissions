class Solution:
    def reverse(self, x: int) -> int:
        if x>((2**31)-1) or x<-((2**31)-1):
            return 0
        rev=0
        if x>0:
            sign=1
        else:
            sign=-1
        
        x=abs(x)
        while x>0:
            rev=rev*10+(x%10)
            x=x//10
        
        if rev>((2**31)-1) or rev<-((2**31)-1):
            return 0
        else:
            return rev*sign
        