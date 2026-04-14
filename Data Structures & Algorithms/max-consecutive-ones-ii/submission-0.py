class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        low = 0
        count=0
        high = 0
        cur_ans=0
        ans = 0
        while(high<len(nums)):
            if nums[high]==1:
                cur_ans+=1
                high+=1
                ans = max(cur_ans,ans)
                continue
            if nums[high]==0 and count==0:
                count+=1
                cur_ans+=1
                ans = max(cur_ans,ans)
            else:
                cur_ans = 0
                count=0
            high+=1
        return ans
            
            


        