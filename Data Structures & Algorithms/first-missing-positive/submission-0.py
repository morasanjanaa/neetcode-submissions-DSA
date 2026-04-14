class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxi = max(nums)
        if maxi <=0:
            return 1
        for i in range(1,maxi):
            if i not in seen:
                return i
        return maxi+1

        
        