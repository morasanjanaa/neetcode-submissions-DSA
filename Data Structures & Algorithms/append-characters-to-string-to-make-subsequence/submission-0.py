class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        count = 0
        while(i<len(s) and j < len(t)):
            if s[i]==t[j]:
                j+=1
                count+=1
            i+=1
        return len(t)-count