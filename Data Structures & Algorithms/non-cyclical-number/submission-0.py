class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        #use set to detect cycles, if seen number is already there, then return False

        if n==1:
            return True
        def digitsquaresum(a: int) -> int:
            res=0
            while a>0:
                res=res+(a%10)**2
                a=a//10

            return res

        while True:
            temp=digitsquaresum(n)

            if temp==1:
                return True

            if temp in visited:
                return False

            
            visited.add(temp)
            n=temp


        