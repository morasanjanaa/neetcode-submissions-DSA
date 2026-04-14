class Solution:
    def atmost(self,k,nums):
        left = 0 
        seen = {}
        ans = 0
        for right in range(0,len(nums)):
            seen[nums[right]] = seen.get(nums[right],0)+1
            while(len(seen) > k):
                seen[nums[left]] -= 1
                if seen[nums[left]] == 0:
                    del seen[nums[left]] 
                left+=1
            ans += (right - left +  1)
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(k,nums) - self.atmost(k-1,nums)
        

        