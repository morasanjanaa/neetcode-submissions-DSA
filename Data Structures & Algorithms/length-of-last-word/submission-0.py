class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.strip()
        ans = k.split(" ")
        return len(ans[len(ans)-1])
        