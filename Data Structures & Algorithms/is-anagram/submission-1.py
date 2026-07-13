from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #or keep frequency bucket of len 26 or use hashmap counter
        return Counter(s)==Counter(t)


        

        