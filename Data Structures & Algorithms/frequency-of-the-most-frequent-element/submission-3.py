class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        ans = 0
        total = 0
        for i in range(0,len(nums)):
            total += nums[i]
            if nums[i] * (i - start + 1 ) - total <= k:
                ans = max(ans,i - start + 1)
            else:
                total -= nums[start]
                start += 1
        if ans == 0:
            return 1
        return ans
        


        


        