class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        w = sorted(words, key=len, reverse=True)
        ans = set()
        for i in range(0,len(w)):
            for j in range(i+1,len(w)):
                if w[j] in w[i]:
                    ans.add(w[j])
        return list(ans)

        