class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total=sum(arr[:k])
        ans = 0
        if ((total/k)>=threshold):
            ans+=1
        for i in range(k,len(arr)):
            total = total-arr[i-k]
            total = total+arr[i]
            if ((total/k)>=threshold):
               ans+=1
        return ans




        