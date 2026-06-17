class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={'(':')', '{':'}', '[':']'}

        for i in range(len(s)):
            if s[i] in hash_map: #opening brakcet
                stack.append(s[i])
            else: #closing bracket
                #no corresponding opening bracket found
                if not stack:
                    return False
                else:
                    temp=stack.pop()
                    if hash_map[temp]!=s[i]:
                        return False

        return len(stack)==0 #no extra opening brackets 

        