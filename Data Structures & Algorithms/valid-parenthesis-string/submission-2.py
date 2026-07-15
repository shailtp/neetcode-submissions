class Solution:
    def checkValidString(self, s: str) -> bool:
        #need 2 stacks of left and right, to store ( and * indexes


        left = []
        right = []


        for i in range(len(s)):
            if s[i]=='(':
                left.append(i)

            elif s[i]=='*':
                right.append(i)

            else:
                #closing bracket encountered. check if left stack has elements
                if not left and not right:
                    return False
                if left:
                    left.pop()
                else:
                    right.pop()
        while left and right:
            if left.pop()>right.pop():
                return False

        return len(left)==0