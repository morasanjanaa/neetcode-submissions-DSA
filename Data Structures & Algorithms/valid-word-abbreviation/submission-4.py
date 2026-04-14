class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l,r = 0,0
        while(l<len(word) and r < len(abbr)):

         if abbr[r].isdigit():
            if abbr[r] == '0':
                    return False
            num = 0
            while(r<len(abbr) and abbr[r].isdigit()):
                num = num * 10 + int(abbr[r])
                r+=1
            l+=num
        
         else:
            if (abbr[r]!=word[l]):
                return False
            l+=1
            r+=1
        
        return len(word)==l and len(abbr)==r
