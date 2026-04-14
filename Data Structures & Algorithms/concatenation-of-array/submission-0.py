class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n*2)
        j = 0
        for i in range(0,len(ans)):
            if i == n:
                j = 0
            ans[i] = nums[j]
            j+=1
        return ans
            

        