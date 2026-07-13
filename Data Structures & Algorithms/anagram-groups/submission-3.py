class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a hashmap to store canonical/sorted string as key and value is a set of corresponding strings
        hashmap = {}

        for string in strs:
            canonical = ''.join(sorted(string))
            if canonical not in hashmap: 
                hashmap[canonical] = []
                hashmap[canonical].append(string)  
            else:
                hashmap[canonical].append(string)

        res=[]

        for key in hashmap:
            res.append(list(hashmap[key]))

        return res
        