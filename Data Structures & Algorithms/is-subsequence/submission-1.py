class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        count=0
        for i in t:
            if j<len(s) and i == s[j]:
                count+=1
                j+=1
        return len(s) == count

        