class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for i in freq.keys():
            if freq[i] > len(nums)/2:
                return i
        return None


        