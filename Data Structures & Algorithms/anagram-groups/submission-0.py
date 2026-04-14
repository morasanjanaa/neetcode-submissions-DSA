class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word = []
        group = dict()
        for i in strs:
            x = "".join(sorted(i))
            if x not in group:
                group[x] = [i]
            else:
                group[x].append(i)
        
        return list(group.values())   