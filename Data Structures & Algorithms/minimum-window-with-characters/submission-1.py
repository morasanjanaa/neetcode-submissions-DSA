from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        window = Counter(t)
        need = dict()
        have = 0
        res,res_len = [-1,-1],float('inf')
        low = 0
        for right in range(len(s)):
            x = s[right]
            need[x] = need.get(x,0)+1

            if x in window and need[x] == window[x]:
                have+=1
            
            while(have==len(window)):
                if (right - low + 1)<res_len:
                    res = low,right
                    res_len = right-low+1
                need[s[low]] = need.get(s[low],0)-1
                if s[low] in window and need[s[low]]<window[s[low]]:
                    have-=1
                low+=1
        l,r = res[0],res[1]
        return s[l:r+1] if res_len!=float('inf') else ""

            

