from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        window_count = Counter(blocks[:k])
        if window_count['B']==k:
            return 0
        else:
            ans = min(ans,k-window_count['B'])
        for i in range(k,len(blocks)):
            window_count[blocks[i]]+=1
            window_count[blocks[i-k]]-=1
            ans = min(ans,k-window_count['B'])
        return ans
