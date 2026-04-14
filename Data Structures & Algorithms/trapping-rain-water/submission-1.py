class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case: if array is empty, no water can be trapped
        if not height:
            return 0
        
        n = len(height)
        
        # leftmax[i] will store the maximum height to the left of index i (including itself)
        leftmax = [0]*n
        
        # rightmax[i] will store the maximum height to the right of index i (including itself)
        rightmax = [0]*n
        
        # First element left max is the element itself
        leftmax[0] = height[0]
        
        # Build leftmax array
        for i in range(1, n):
            # maximum of previous left max or current height
            leftmax[i] = max(leftmax[i-1], height[i])
        
        # Last element right max is the element itself
        rightmax[n-1] = height[n-1]
        
        # Build rightmax array from right to left
        for i in range(n-2, -1, -1):
            # maximum of next right max or current height
            rightmax[i] = max(rightmax[i+1], height[i])
        
        ans = 0
        
        # Water trapped at each index =
        # min(leftmax[i], rightmax[i]) - height[i]
        for i in range(n):
            ans += min(leftmax[i], rightmax[i]) - height[i]
        
        # Return total trapped water
        return ans


        