class Solution:
    def atmost(self,goal,nums):
        if goal < 0:
            return 0
        left = 0
        total = 0
        ans = 0
        for right in range(len(nums)):
            total += nums[right]
            while(total > goal):
                total -= nums[left]
                left +=1
            ans += (right - left + 1)
        return ans
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmost(goal,nums) - self.atmost(goal-1,nums)

        