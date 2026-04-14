class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        window = dict()
        for right in range(0,len(s)):
            window[s[right]]= window.get(s[right],0)+1
            while(len(window)>k):
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1

            ans = max(ans, right - left+1)
        return ans


        