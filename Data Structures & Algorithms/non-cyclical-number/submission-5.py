class Solution:
    def isHappy(self, n: int) -> bool:    
        visited=set()
        if n==1:
            return True
        
        def digitsum(n: int)-> int:
            res=0
            while n>0:
                res=res+(n%10)**2
                n=n//10


            return res

        

        while True:
            temp=digitsum(n)
            if temp==1:
                return True

            if temp in visited:
                return False

            visited.add(temp)
            n = temp
        

        





