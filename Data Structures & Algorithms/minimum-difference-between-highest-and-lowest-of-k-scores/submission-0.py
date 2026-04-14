class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        window = list(nums[:k]) 
        min_diff = max(window)-min(window)
        for i in range(k,len(nums)):
            window.remove(nums[i-k])
            window.append(nums[i])
            maxi = max(window)
            mini = min(window)
            min_diff = min(min_diff,maxi-mini)
        return min_diff