class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash_map={'(':')', '{':'}', '[':']'}

        for i in range(len(s)):
            if s[i] in hash_map:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    opening=stack.pop()
                    if hash_map[opening]!=s[i]:
                        return False

        return len(stack)==0



        