class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        ans_length = 0
        while(right<len(s) and left<len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                cur_length = len(seen)
                ans_length = max(cur_length,ans_length)
                right+=1
            else:
                seen.remove(s[left])
                left+=1
        return ans_length
            

        