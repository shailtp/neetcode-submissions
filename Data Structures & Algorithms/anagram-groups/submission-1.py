
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use hashmap in which counter/canonical form (sorted string) is key and values are list of corresponding strings
        hash_map={}

        for string in strs:
            canonical=''.join(sorted(string))
            if canonical not in hash_map:
                hash_map[canonical]=[]
                hash_map[canonical].append(string)
            else:
                hash_map[canonical].append(string)

        res=[]
        for key in hash_map:
            res.append(hash_map[key])

        return res


