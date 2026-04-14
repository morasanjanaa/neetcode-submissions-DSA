class Solution:
    def maxArea(self, arr: List[int]) -> int:
        total_max = 0
        i = 0
        j = len(arr)-1
        while(i<j):
            mini = min(arr[i],arr[j])
            ans = (j-i)*mini
            total_max = max(ans,total_max)
            if (arr[i]<arr[j]):
                i+=1
            else:
                j-=1
        return total_max

        