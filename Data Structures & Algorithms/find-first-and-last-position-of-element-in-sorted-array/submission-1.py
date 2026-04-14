class Solution:
    
    def upper_bound(self,arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    def lower_bound(self,arr, target):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower = self.lower_bound(nums,target)
        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]
        upper = self.upper_bound(nums,target)-1
        return [lower,upper]
        





        