class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        right = len(nums)-1
        ans = 0
        while(low<=right):
            mid = int((low+right)/2)
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else :
                ans = mid
                break
        return low if ans == 0 else ans
        