# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        ans = 0
        while(left<=right):
            mid = int((left+right)/2)
            pickme = guess(mid)
            if pickme == 1:
                left = mid + 1
            elif pickme == -1:
                right = mid - 1 
            else:
                ans = mid
                break
        return ans
        
        