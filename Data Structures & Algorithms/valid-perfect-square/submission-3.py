class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 1
        right = num/2
        ans = False
        while(left<=right):
            mid = int((left+right)/2)
            target = mid * mid
            if (target) > num:
                right= mid - 1
            elif (target < num):
                left = mid + 1
            else:
                ans = True
                break
        return ans
        
        