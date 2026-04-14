class Solution:
    def trap(self, height: List[int]) -> int:
            leftmax = list()
            ans = 0
            print(leftmax)
            rightmax = list()
            left_max = height[0]
            right_max=height[len(height)-1]
            for i in height:
                left_max=max(left_max,i)
                leftmax.append(left_max)
            for i in range (len(height)-1,-1,-1):
                right_max = max(right_max,height[i])
                rightmax.append(right_max)
            maxi = rightmax[::-1]    
            for i in range(0,len(height)):
                ans+=min(leftmax[i],maxi[i])-height[i]
            return ans
           

        