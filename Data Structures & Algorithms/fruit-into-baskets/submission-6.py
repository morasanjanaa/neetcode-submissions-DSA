from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low = 0
        max_len = 0
        freq = dict()
        for right in range(0,len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0)+1
            while(len(freq)>2):
                freq[fruits[low]]-=1
                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]
                low+=1
            max_len = max(max_len,right-low+1)
        return max_len


                


        
        