from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
          
        count = defaultdict(int)
        max_len = 0
        l=0
        
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            
            while len(count)>2:
                leftfruit = fruits[l]
                count[leftfruit]-=1
                if count[leftfruit]==0:
                    del count[leftfruit]
                l+=1
                
            max_len = max(max_len,r-l+1)
            
        return max_len
                    
            