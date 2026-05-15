
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use hashmap in which counter/canonical form is key and values are list of corresponding strings
        hash_map={}

        for string in strs:
            temp=''.join(sorted(string))
            if temp not in hash_map:
                hash_map[temp]=[]
                hash_map[temp].append(string)

            else:
                hash_map[temp].append(string)

        res=[]
        print(hash_map)
        for key in hash_map:
            res.append(hash_map[key])

        return res

        #Time: O(n), space: O(n)


