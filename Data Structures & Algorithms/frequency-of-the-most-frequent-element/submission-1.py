class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 0
        max_len = 0
        total = 0
        while(right<len(nums)):
            total+=nums[right]
            while(nums[right]*(right-left+1)>k+total):
                    total-=nums[left]
                    left+=1
            max_len = max(max_len,right-left+1)
            right+=1
            
        return max_len



        