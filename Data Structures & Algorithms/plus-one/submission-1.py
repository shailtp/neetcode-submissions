class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=0
        for i in digits:
            number=number*10+i

        number+=1

        res=[]
        while number>0:
            res.append(number%10)
            number=number//10

        left=0
        right=len(res)-1

        while left<right:
            res[right], res[left] = res[left], res[right]
            left+=1
            right-=1

        return res

        #Time: O(n), space: O(n)