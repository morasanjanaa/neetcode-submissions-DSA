class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        max_fruits = 0
        start = 0
        for i in range(0,len(fruits)):
            freq[fruits[i]] = freq.get(fruits[i],0)+1
            while len(freq)>2:
                freq[fruits[start]] -= 1
                if freq[fruits[start]] == 0:
                    del freq[fruits[start]]
                start += 1
            max_fruits = max(max_fruits,i-start+1)
        return max_fruits


        