class Solution:
    def isHappy(self, n: int) -> bool:    
        if n==1:
            return True

        

        slow, fast = n, self.digitsum(n)

        while slow != fast:
            fast = self.digitsum(fast)
            fast = self.digitsum(fast)
            slow = self.digitsum(slow)
        return True if fast == 1 else False

    def digitsum(self, n: int)-> int:
        res=0
        while n>0:
            res=res+(n%10)**2
            n=n//10


        return res
        

        





