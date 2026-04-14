from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)

        if n1>n2 :
            return False

        window_count = Counter(s2[:n1])
        s1_count = Counter(s1)

        if window_count==s1_count:
            return True

        for j in range(n1,n2):
            window_count[s2[j]]+=1
            window_count[s2[j-n1]]-=1
            if window_count[s2[j-n1]] == 0:
                del window_count[s2[j-n1]]
            if window_count==s1_count:
               return True

        return False
