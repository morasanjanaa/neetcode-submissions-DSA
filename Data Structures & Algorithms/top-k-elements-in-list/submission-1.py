class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            freq1 = dict()
            ans = []
            for i in nums:
                freq1[i] = freq1.get(i,0)+1
            sorted_dict_desc = dict(sorted(freq1.items(), key=lambda item: item[1], reverse=True))
            for i in sorted_dict_desc.keys():
                if k==0:
                    break
                ans.append(i)
                k-=1
            return ans



        