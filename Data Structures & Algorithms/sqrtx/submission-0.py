class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        ans = 0
        while(left<=right):
            mid = int((right+left)/2)
            target = mid * mid
            if (target) > x:
                right = mid - 1
            elif (target < x):
                left = mid + 1
            else:
                ans = mid
                break
        return left-1 if ans == 0 else ans


        