class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""

        for ch in s:
            if ch.isalnum():
                x += ch.lower()

        i, j = 0, len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1

        return True
