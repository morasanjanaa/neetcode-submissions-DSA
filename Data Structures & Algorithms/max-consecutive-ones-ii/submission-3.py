class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # left pointer of sliding window
        left = 0
        
        # number of zeros currently inside the window
        zeros = 0
        
        # stores maximum window length found
        ans = 0

        # right pointer expands the window
        for right in range(len(nums)):
            
            # if current element is zero, count it
            if nums[right] == 0:
                zeros += 1

            # if more than one zero appears,
            # shrink window from left until window becomes valid again
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # window is valid here (at most one zero)
            # update answer using current window size
            ans = max(ans, right - left + 1)

        return ans
