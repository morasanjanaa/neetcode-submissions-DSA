from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)==1:
            return 1
        low = 0
        window = Counter(fruits[:2])
        cur_len = 2
        max_len = cur_len
        for i in range(2,len(fruits)):
            window[fruits[i]]+=1
            cur_len+=1
            while(len(window)>2):
                window[fruits[low]]-=1
                cur_len-=1
                if window[fruits[low]] == 0:
                    del window[fruits[low]]
                low+=1
            max_len = max(cur_len,max_len)
        return max_len
            

                


        
        